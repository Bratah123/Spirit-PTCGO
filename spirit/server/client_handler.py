import logging
import json
import time
import uuid
import asyncio
from spirit import config
from spirit.network.protocol import WargProtocol, WargFlags
from spirit.packets.router import PacketRouter
from spirit.game.models.player import Player
from spirit.game.session.manager import GameSessionManager
from spirit.game.session.constants import GamePhase
from spirit.packets.handlers.social import SocialHandler
from spirit.server import metrics

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
        try:
            encoded_body = WargProtocol.encode_body(response_body, flags)

            if _log.isEnabledFor(logging.DEBUG):
                self._log_packet("Sent", response_body, request_id, flags, encoded_body)

            header = WargProtocol.encode_header(len(encoded_body), request_id, flags)
            self.writer.write(header + encoded_body)
            # Bound the drain: a peer whose receive window is full (wedged client,
            # zero-window) would otherwise block this coroutine forever, freezing the
            # match under _wire_lock. On timeout, abort and fall into the disconnect
            # path (detach + reconnect grace) — the designed behavior for a dead peer.
            try:
                await asyncio.wait_for(self.writer.drain(), timeout=config.SEND_TIMEOUT_SECONDS)
            except asyncio.TimeoutError:
                logging.warning(f"[TCP] [{self.addr}] Send drain timed out; aborting stalled peer.")
                metrics.inc("send_timeouts")
                try:
                    self.writer.transport.abort()
                except Exception:
                    pass
                await self.disconnect()
            metrics.inc("bytes_out", len(encoded_body) + WargProtocol.HEADER_SIZE)
        except Exception as e:
            logging.error(f"[TCP] [{self.addr}] Error sending packet: {e}")
            await self.disconnect()

    async def disconnect(self):
        if self.running:
            self.running = False
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
                from spirit.game.live_tournament import LiveTournamentManager
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

            self.writer.close()
            try:
                await self.writer.wait_closed()
            except Exception:
                pass
            self.server.remove_client(self)
