import logging
import inspect

from spirit.network.protocol import WargFlags
from spirit.network.message_names import InboundMsg
from .handlers.handshake import HandshakeHandler
from .handlers.auth import AuthHandler
from .handlers.system import SystemHandler
from .handlers.data_sync import DataSyncHandler
from .handlers.social import SocialHandler
from .handlers.shop import ShopHandler
from .handlers.redemption import RedemptionHandler
from .handlers.trade import TradeHandler
from .handlers.matchmaking import MatchmakingHandler
from .handlers.gameplay import GameplayHandler
from .handlers.tournaments import TournamentHandler

HANDLER_CLASSES = [
    HandshakeHandler,
    AuthHandler,
    SystemHandler,
    DataSyncHandler,
    SocialHandler,
    ShopHandler,
    RedemptionHandler,
    TradeHandler,
    MatchmakingHandler,
    GameplayHandler,
    TournamentHandler,
]

class PacketRouter:
    def __init__(self, client):
        self.client = client
        # {msg_name: (bound_handler, is_coroutine)}
        self.handlers = {}
        self.register_handlers()

    def register_handlers(self):
        for handler_cls in HANDLER_CLASSES:
            instance = handler_cls(self.client)
            for msg_name, func in instance.get_handlers().items():
                self.handlers[msg_name] = (func, inspect.iscoroutinefunction(func))

    async def route(self, message, request_id, flags):
        # Determine message name
        msg_name = None
        if isinstance(message, dict):
            msg_name = message.get("name")
            if not msg_name:
                # Duck-typing heuristic for unwrapped messages
                if "queueName" in message and "gameID" in message and "path" in message:
                    msg_name = InboundMsg.READY_FOR_MATCH_CONFIRMATION.value
                    # Re-wrap as a standard polymorphic message structure
                    message = {"name": msg_name, "value": message}

        elif hasattr(message, "DESCRIPTOR"):
            # For protobuf, we usually have a wrapper or need to know the type
            # The protocol.py currently passes the unwrapped proto object
            msg_name = message.DESCRIPTOR.full_name

        if not msg_name:
            logging.warning(f"[TCP] [{self.client.addr}] Unhandled packet received (no message name / unwrapped JSON): {message}")
            return

        entry = self.handlers.get(msg_name)
        if entry:
            handler_func, is_coro = entry
            try:
                payload = message.get("value") if isinstance(message, dict) else message
                if is_coro:
                    await handler_func(payload, request_id, flags)
                else:
                    handler_func(payload, request_id, flags)
            except Exception as e:
                logging.error(f"[TCP] [{self.client.addr}] Error in handler {msg_name}: {e}", exc_info=True)
        else:
            logging.warning(f"[TCP] [{self.client.addr}] No handler registered for message: {msg_name}")

    async def handle_raw_protobuf(self, message_name, proto_obj, request_id, flags):
        """
        Special entry point for protobuf messages that were identified by the protocol layer.
        """
        entry = self.handlers.get(message_name)
        if entry:
            handler_func, is_coro = entry
            if is_coro:
                await handler_func(proto_obj, request_id, flags)
            else:
                handler_func(proto_obj, request_id, flags)
        else:
            logging.warning(f"[TCP] [{self.client.addr}] No handler for Protobuf message: {message_name}")
