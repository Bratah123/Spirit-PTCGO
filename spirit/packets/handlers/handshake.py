import ipaddress

from spirit import config
from spirit.network.protocol import WargFlags
from spirit.network.message_names import InboundMsg, OutboundMsg
from .base import BaseHandler, handle

class HandshakeHandler(BaseHandler):
    @handle(InboundMsg.REQ_CONNECTION_SERVICE_VERSION)
    async def handle_connection_service(self, message, request_id, flags):
        # The client drops the gateway socket and reconnects to this endpoint
        response = {
            "messageName": OutboundMsg.CONNECTION_SERVICE.value,
            "connectionEndPoint": f"{self._endpoint_host()}:{self.client.server.port}"
        }
        await self.client.send_packet(response, request_id)

    def _endpoint_host(self):
        """Loopback/LAN clients reconnect to the address they dialed (no NAT hairpin needed)."""
        try:
            if ipaddress.ip_address(self.client.addr[0]).is_private:
                return self.client.writer.get_extra_info("sockname")[0]
        except (ValueError, AttributeError, IndexError, TypeError):
            pass
        return config.PUBLIC_HOST

    @handle(InboundMsg.REQ_SESSION)
    async def handle_request_session(self, message, request_id, flags):
        response = {
            "messageName": OutboundMsg.GRANTED_SESSION.value,
            "version": "2.95.0.5815",
            "serverTime": 1620000000000,
            "options": {},
            "session": self.client.session_id
        }
        await self.client.send_packet(response, request_id, flags=WargFlags.GRANTED_SESSION)

    @handle(InboundMsg.REQ_LOGIN)
    async def handle_request_login(self, message, request_id, flags):
        response = {
            "messageName": OutboundMsg.REQ_AUTH_TYPE.value,
            "validAuthTypes": ["gas"]
        }
        await self.client.send_packet(response, request_id)
