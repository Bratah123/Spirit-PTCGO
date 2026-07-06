import asyncio
import logging
import ssl
import os
from spirit import config
from .client_handler import ClientHandler
from spirit.database.db_manager import db_manager

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
        self.running = False

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

    async def _handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        logging.info(f"[TCP] New connection from {addr}")
        
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
        logging.info("[TCP] Stopping server...")
        
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            
        for client in self.clients[:]:
            await client.disconnect()
            
        db_manager.stop_writer()
            
        logging.info("[TCP] Server stopped.")

    def remove_client(self, client_handler):
        if client_handler in self.clients:
            self.clients.remove(client_handler)
            logging.info(f"[TCP] Client {client_handler.addr} removed.")
