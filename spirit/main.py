import time
import logging
import os
import json
import asyncio

# Configure logging at the very start
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from spirit import config
from spirit.server.server import PTCGOServer
from spirit.server.http_server import AssetHTTPServer, manifest_manager
from spirit.server.auto_bundle import check_and_generate_bundles
from spirit.database import Base, engine
from spirit.database.migrations import run_light_migrations
from spirit.database.admin_data import bootstrap_admins_from_env

async def run_server():
    tcp_server = PTCGOServer()
    
    # We want to catch asyncio.CancelledError to stop server gracefully
    try:
        await tcp_server.start()
    except asyncio.CancelledError:
        pass
    finally:
        await tcp_server.stop()

def main():
    logging.info(f"[Main] Public host: {config.PUBLIC_HOST} (HTTP {config.HTTP_PORT}, TCP {config.TCP_PORT})")
    if config.PUBLIC_HOST == "127.0.0.1":
        logging.warning("[Main] PUBLIC_HOST is 127.0.0.1 — remote clients will fail to log in. "
                        "Set it in spirit/config.py or via SPIRIT_PUBLIC_HOST.")

    # 0. Ensure all database tables exist (idempotent)
    Base.metadata.create_all(engine)
    run_light_migrations()
    bootstrap_admins_from_env()
    # Prime the tournament cache off-loop (handlers only read it afterwards)
    from spirit.game.tournament_manager import TournamentManager
    TournamentManager()

    # 1. Ensure asset_map.json exists for first-time setup
    map_path = "spirit/server/asset_map.json"
    if not os.path.exists(map_path):
        logging.info("ERROR: [Main] asset_map.json not found.")
        return

    # 2. Run the auto bundle generation
    check_and_generate_bundles()
    
    logging.info("[Main] Refreshing manifest manager...")
    # Reload asset map and refresh manifest to capture all compiled cards and cosmetics
    map_path = "spirit/server/asset_map.json"
    try:
        with open(map_path, "r") as f:
            manifest_manager.asset_map = json.load(f)
    except Exception as e:
        logging.error(f"[Main] Failed to reload asset_map.json: {e}")
    manifest_manager.refresh()

    http_server = AssetHTTPServer()
    http_server.start()

    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
        http_server.stop()

if __name__ == '__main__':
    main()
