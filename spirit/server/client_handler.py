import logging
import json
import uuid
import asyncio
from spirit.network.protocol import WargProtocol, WargFlags
from spirit.packets.router import PacketRouter
from spirit.game.models.player import Player
from spirit.game.session.manager import GameSessionManager
from spirit.game.session.constants import GamePhase
from spirit.packets.handlers.social import SocialHandler

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

    async def handle(self):
        self.running = True
        try:
            while self.running:
                try:
                    header_data = await self.reader.readexactly(WargProtocol.HEADER_SIZE)
                except asyncio.IncompleteReadError:
                    break
                    
                if not header_data:
                    break
                
                body_length, request_id, flags = WargProtocol.decode_header(header_data)
                
                try:
                    body_data = await self.reader.readexactly(body_length)
                except asyncio.IncompleteReadError:
                    break
                
                message = WargProtocol.decode_body(body_data, flags)

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
            await self.writer.drain()
        except Exception as e:
            logging.error(f"[TCP] [{self.addr}] Error sending packet: {e}")
            await self.disconnect()

    async def disconnect(self):
        if self.running:
            self.running = False

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
                        await session.on_player_disconnect(self.player.account_id)
                    else:
                        manager.remove_session_by_player_id(self.player.account_id)
                except Exception as e:
                    logging.error(f"[TCP] [{self.addr}] Error handling game session on disconnect: {e}")

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
