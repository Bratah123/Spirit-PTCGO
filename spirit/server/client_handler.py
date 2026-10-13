import logging
import json
import time
import uuid
import asyncio
from spirit import config
from spirit.network.protocol import OutboundQueue, WargProtocol, WargFlags
from spirit.packets.router import PacketRouter
from spirit.game.models.player import Player
from spirit.game.session.manager import GameSessionManager
from spirit.game.session.constants import GamePhase
from spirit.packets.handlers.social import SocialHandler
from spirit.server import metrics
from spirit.game.tournaments.live import LiveTournamentManager

_log = logging.getLogger(__name__)

class ClientHandler:
    def __init__(self, reader, writer, addr, server):
        self.reader = reader
        self.writer = writer
        self.addr = addr
        self.server = server
        self.running = False
        self.router = PacketRouter(self)
        self.session_id = str(uuid.uuid4()) # Must be a valid Guid string for C# parsing
        self.player: Player | None = None  # Populated post-auth
        self.sent_archetypes = set() # Track GUIDs sent to client to prevent duplicates crash
        self.sent_archetype_keys = set() # Track catalog keys already served (byte-cache dedup)
        # Inbound token bucket (abuse guard); refilled lazily in _rate_ok.
        self._bucket_tokens = config.INBOUND_RATE_BURST
        self._bucket_ts = time.monotonic()
        self._rate_warned_at = 0.0
        self._disconnect_task = None
        self.outbound = OutboundQueue(writer, self._outbound_failed)

    def _rate_ok(self) -> bool:
        """Per-connection token bucket. Generous enough that legit play never trips it."""
        rate = config.INBOUND_RATE_PER_SEC
        if rate <= 0:
            return True
        now = time.monotonic()
        self._bucket_tokens = min(
            config.INBOUND_RATE_BURST,
            self._bucket_tokens + (now - self._bucket_ts) * rate,
        )
        self._bucket_ts = now
        if self._bucket_tokens < 1.0:
            if now - self._rate_warned_at > 5.0:  # log at most once per 5s per connection
                logging.warning(f"[TCP] [{self.addr}] Inbound rate limit hit; dropping packets.")
                self._rate_warned_at = now
            metrics.inc("packets_rate_limited")
            return False
        self._bucket_tokens -= 1.0
        return True

    async def handle(self):
        self.running = True
        try:
            while self.running:
                # Idle deadline: a header that never arrives means a half-open/dead
                # socket (the client pings regularly). Pre-auth is tighter.
                idle = (config.PREAUTH_TIMEOUT_SECONDS if self.player is None
                        else config.IDLE_TIMEOUT_SECONDS)
                try:
                    header_data = await asyncio.wait_for(
                        self.reader.readexactly(WargProtocol.HEADER_SIZE), timeout=idle)
                except asyncio.IncompleteReadError:
                    break
                except asyncio.TimeoutError:
                    logging.info(f"[TCP] [{self.addr}] Idle timeout ({idle}s); closing.")
                    break

                if not header_data:
                    break

                body_length, request_id, flags = WargProtocol.decode_header(header_data)

                try:
                    body_data = await self.reader.readexactly(body_length)
                except asyncio.IncompleteReadError:
                    break

                if not self._rate_ok():
                    continue  # drop over-limit packet, keep the connection

                message = WargProtocol.decode_body(body_data, flags)
                metrics.inc("packets_in")

                if _log.isEnabledFor(logging.DEBUG):
                    self._log_packet("Received", message, request_id, flags)

                await self.router.route(message, request_id, flags)

        except ConnectionResetError:
            logging.info(f"[TCP] [{self.addr}] Connection reset by peer.")
        except Exception as e:
            logging.error(f"[TCP] [{self.addr}] Error handling client: {e}")
        finally:
            await self.disconnect()

    def _log_packet(self, direction, body, request_id, flags, encoded_body=None):
        # Outbound carries "messageName"; inbound rides the {"name", "value"} wire envelope
        if isinstance(body, dict) and (
            body.get("messageName") in ("Ping", "Pong")
            or body.get("name") in ("Ping", "Pong")
        ):
            return
        log_msg = body
        if flags & WargFlags.PROTOBUF and encoded_body is not None:
            desc = getattr(body, 'DESCRIPTOR', None)
            proto_name = desc.full_name if desc is not None else "Raw"
            log_msg = f"Protobuf({proto_name}): {encoded_body.hex()}"
        elif isinstance(body, (dict, list)):
            log_msg = "\n" + json.dumps(body, indent=2)
        _log.debug(f"[TCP] [{self.addr}] {direction} [RID={request_id}, Flags={flags}]: {log_msg}")

    async def send_packet(self, response_body, request_id, flags=WargFlags.CLEAR):
        """Enqueue one packet; use flush_outbound only at delivery-sensitive boundaries."""
        return await self.send_packets([(response_body, request_id, flags)])

    async def send_packets(self, packets):
        """Encode and enqueue a complete ordered batch without waiting on the socket."""
        if self._disconnect_task is not None:
            return False
        try:
            return self.outbound.enqueue(self._encode_packets(packets))
        except Exception as error:
            self.outbound.fail(error)
            return False

    def _encode_packets(self, packets):
        for response_body, request_id, flags in packets:
            body = WargProtocol.encode_body(response_body, flags)
            if _log.isEnabledFor(logging.DEBUG):
                self._log_packet("Queued", response_body, request_id, flags, body)
            yield WargProtocol.encode_header(len(body), request_id, flags) + body

    async def flush_outbound(self):
        """Drain prior output and finish disconnect cleanup if sending failed."""
        drained = await self.outbound.flush()
        if not drained and self._disconnect_task is not None:
            await asyncio.shield(self._disconnect_task)
        return drained

    def _outbound_failed(self, error):
        logging.warning("[TCP] [%s] Outbound connection failed (%s): %s",
                        self.addr, type(error).__name__, error)
        self._begin_disconnect()

    def _begin_disconnect(self):
        if self._disconnect_task is None:
            self.running = False
            self._disconnect_task = asyncio.create_task(
                self._disconnect(), name="warg-disconnect")
        return self._disconnect_task

    async def disconnect(self):
        await asyncio.shield(self._begin_disconnect())

    async def _disconnect(self):
        await self.outbound.close()
        try:
            metrics.inc("disconnects")
            shutting_down = getattr(self.server, "shutting_down", False)

            # Remove from matchmaking queue gracefully
            try:
                # We assume GameSessionManager singleton is updated later
                await GameSessionManager().remove_from_queue(self, send_left_packet=False)
            except Exception as e:
                logging.error(f"[TCP] [{self.addr}] Error removing from matchmaking queue on disconnect: {e}")

            # Cancel any pending friend challenges so the other party's dialog unwinds
            try:
                await GameSessionManager().remove_challenges_for_client(self, notify_self=False)
            except Exception as e:
                logging.error(f"[TCP] [{self.addr}] Error cancelling pending challenges on disconnect: {e}")

            # Drop pre-game pairings still holding this client (ready-check window)
            try:
                GameSessionManager().remove_pending_pairings_for_client(self)
            except Exception as e:
                logging.error(f"[TCP] [{self.addr}] Error dropping pending pairings on disconnect: {e}")

            # Leave legacy tournament queues (with fee refund) and the Events channel
            try:
                await LiveTournamentManager().handle_disconnect(self)
            except Exception as e:
                logging.error(f"[TCP] [{self.addr}] Error cleaning tournament queues on disconnect: {e}")

            # Detach from any active game (keep the session alive for reconnect);
            # tear down only finished/stale sessions.
            if self.player:
                try:
                    manager = GameSessionManager()
                    session = manager.get_session_by_player_id(self.player.account_id)
                    if session is not None and session.game_phase != GamePhase.GAME_OVER:
                        await session.on_player_disconnect(
                            self.player.account_id, client_handler=self
                        )
                    else:
                        manager.remove_session_by_player_id(self.player.account_id)
                except Exception as e:
                    logging.error(f"[TCP] [{self.addr}] Error handling game session on disconnect: {e}")

                if not shutting_down:
                    try:
                        social_handler = SocialHandler(self)
                        # Router will route later, for now we will assume broadcast_presence is async
                        await social_handler.broadcast_presence("Offline")
                    except Exception as e:
                        logging.error(f"[TCP] [{self.addr}] Error broadcasting offline presence: {e}")

        finally:
            self.writer.close()
            try:
                await asyncio.wait_for(self.writer.wait_closed(), timeout=5)
            except Exception:
                self.writer.transport.abort()
            self.server.remove_client(self)
