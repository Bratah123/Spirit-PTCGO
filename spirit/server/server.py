import asyncio
import logging
import socket
import ssl
import os
from spirit import config
from .client_handler import ClientHandler
from spirit.database.db_manager import db_manager
from spirit.server import metrics

class PTCGOServer:
    def __init__(self, host='0.0.0.0', port=config.TCP_PORT, use_ssl=True):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.server = None
        self.context = None
        
        if self.use_ssl:
            cert_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'server.crt'))
            key_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'server.key'))
            
            if os.path.exists(cert_path) and os.path.exists(key_path):
                self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
                self.context.load_cert_chain(certfile=cert_path, keyfile=key_path)
                logging.info("[TCP] SSL Context loaded successfully.")
            else:
                logging.warning("[TCP] SSL certificates not found. Falling back to raw TCP.")
                self.use_ssl = False

        self.clients = []
        # account_id -> ClientHandler, so presence/challenge/login-guard lookups are
        # O(1) instead of O(clients). Maintained by register_account/remove_client.
        self.clients_by_account = {}
        self.running = False
        self.shutting_down = False
        # account_ids whose login is past the guard but not yet indexed — closes the
        # check-then-await race where two logins for one account both pass.
        self.logins_in_flight = set()

        metrics.register_gauge("connections", lambda: len(self.clients))
        metrics.register_gauge("authenticated", lambda: len(self.clients_by_account))

    async def start(self):
        self.server = await asyncio.start_server(
            self._handle_client,
            self.host,
            self.port,
            ssl=self.context
        )
        self.running = True

        db_manager.start_writer()

        addr = self.server.sockets[0].getsockname()
        logging.info(f"[TCP] Server listening on {addr}")

        async with self.server:
            await self.server.serve_forever()

    def register_account(self, client_handler):
        """Indexes a client by account_id once authenticated (called from auth)."""
        account_id = getattr(getattr(client_handler, "player", None), "account_id", None)
        if account_id:
            self.clients_by_account[account_id] = client_handler

    def client_for_account(self, account_id):
        """O(1) authenticated-client lookup by account_id, or None."""
        return self.clients_by_account.get(account_id)

    async def _handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')

        if config.MAX_CONNECTIONS and len(self.clients) >= config.MAX_CONNECTIONS:
            logging.warning(f"[TCP] Connection cap ({config.MAX_CONNECTIONS}) reached; refusing {addr}")
            metrics.inc("connections_refused")
            writer.close()
            return

        logging.info(f"[TCP] New connection from {addr}")
        metrics.inc("connections_accepted")

        # Surface fully-dead peers (silent NAT drop, power-off) as read errors within
        # minutes instead of relying on the OS default (hours).
        try:
            sock = writer.get_extra_info("socket")
            if sock is not None:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                if hasattr(socket, "TCP_KEEPIDLE"):
                    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
                    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 20)
                    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 3)
        except (OSError, AttributeError):
            pass

        client_handler = ClientHandler(reader, writer, addr, self)
        self.clients.append(client_handler)

        # Create an asyncio task for the client
        try:
            await client_handler.handle()
        except Exception as e:
            logging.error(f"[TCP] Client handling error for {addr}: {e}")
        finally:
            self.remove_client(client_handler)

    async def stop(self):
        if not self.running:
            return

        self.running = False
        self.shutting_down = True  # disconnect() consults this to skip presence/grace fan-out
        logging.info("[TCP] Stopping server...")

        if self.server:
            self.server.close()
            await self.server.wait_closed()

        # Bounded, concurrent drain with an overall deadline — a serial per-client
        # await would take minutes at high connection counts.
        async def _drain():
            sem = asyncio.Semaphore(200)

            async def _one(c):
                async with sem:
                    try:
                        await c.disconnect()
                    except Exception:
                        pass
            await asyncio.gather(*(_one(c) for c in self.clients[:]))

        try:
            await asyncio.wait_for(_drain(), timeout=15.0)
        except asyncio.TimeoutError:
            logging.warning("[TCP] Shutdown drain timed out; forcing close.")

        db_manager.stop_writer()

        logging.info("[TCP] Server stopped.")

    def remove_client(self, client_handler):
        if client_handler in self.clients:
            self.clients.remove(client_handler)
            logging.info(f"[TCP] Client {client_handler.addr} removed.")
        account_id = getattr(getattr(client_handler, "player", None), "account_id", None)
        if account_id and self.clients_by_account.get(account_id) is client_handler:
            del self.clients_by_account[account_id]
