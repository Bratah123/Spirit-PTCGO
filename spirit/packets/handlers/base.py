from spirit.network.protocol import WargFlags
from spirit.network.message_names import OutboundMsg
from spirit.database.async_utils import run_db

def handle(msg_type):
    """Decorator to register a method as a handler for a message type; stackable."""
    def decorator(func):
        func._handled_msgs = list(getattr(func, "_handled_msgs", [])) + [msg_type]
        return func
    return decorator

class BaseHandler:
    def __init__(self, client):
        self.client = client

    @classmethod
    def _handler_specs(cls):
        """Scans the class once for @handle-decorated methods; cached per subclass."""
        specs = cls.__dict__.get("_handler_specs_cache")
        if specs is None:
            specs = [
                (str(msg), attr_name)
                for attr_name in dir(cls)
                for attr in [getattr(cls, attr_name, None)]
                if callable(attr)
                for msg in getattr(attr, "_handled_msgs", [])
            ]
            cls._handler_specs_cache = specs
        return specs

    def get_handlers(self):
        """Maps message names to bound handler methods for this instance."""
        return {msg: getattr(self, name) for msg, name in self._handler_specs()}

    async def send(self, payload: dict, request_id: int = 0):
        """Sends a standard clear-text JSON packet to this handler's client."""
        await self.client.send_packet(payload, request_id, flags=WargFlags.CLEAR)

    async def push_wallet(self):
        """Pushes the current wallet balance so the client HUD updates."""
        w_data = self.client.player.get_wallet_data()
        w_data["messageName"] = OutboundMsg.CURRENT_WALLET.value
        await self.send(w_data)

    async def push_collection(self):
        """Pushes the full collection count list (client-side collection refresh)."""
        from spirit.database.player_data import get_merged_collection_payload
        payload = await run_db(get_merged_collection_payload, self.client.player.account_id)
        await self.send({
            "messageName": OutboundMsg.COLLECTION_COUNT_FOUND.value,
            "collectionCountList": payload,
        })

    def online_client(self, account_id: str, exclude_self: bool = False):
        """Finds a logged-in client on this server by account ID, or None."""
        for other in list(self.client.server.clients):
            if exclude_self and other is self.client:
                continue
            if other.player and other.player.account_id == account_id:
                return other
        return None
