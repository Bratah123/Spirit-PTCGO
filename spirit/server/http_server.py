import http.server
import socketserver
import threading
from collections import OrderedDict
import logging
import json
import gzip
import time
import uuid
import os
import re
import hashlib
import UnityPy
from typing import Any
from spirit import config
import spirit.server.state as state

from spirit.server.state import issue_ticket
from spirit.database.accounts import get_account_by_username, verify_password, create_account
from spirit.server import metrics
from spirit.server.manifest_manager import ManifestManager
from urllib.parse import parse_qs
from urllib.parse import urlparse

# Global manifest manager instance
ASSET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
BUNDLE_CACHE_DIR = os.path.join(ASSET_DIR, 'bundleCache')

# We'll prioritize our local bundleCache
ASSET_PATHS = [BUNDLE_CACHE_DIR]

# Allow users to specify an external cache path via environment variable
# or use a local 'externalCache' directory to load original game assets without committing them
external_cache_env = os.environ.get('PTCGO_CACHE_DIR')
local_external_cache = os.path.join(ASSET_DIR, 'externalCache')

if external_cache_env:
    external_cache_env = os.path.abspath(os.path.expanduser(external_cache_env))
    nested_bundle_cache = os.path.join(external_cache_env, 'bundleCache')
    if os.path.isdir(nested_bundle_cache):
        external_cache_env = nested_bundle_cache

if external_cache_env and os.path.isdir(external_cache_env):
    logging.info(f"[HTTP] Found external cache via env: {external_cache_env}")
    ASSET_PATHS.append(external_cache_env)
elif os.path.isdir(local_external_cache):
    logging.info(f"[HTTP] Found local external cache: {local_external_cache}")
    ASSET_PATHS.append(local_external_cache)

manifest_manager = ManifestManager(ASSET_PATHS)

def _default_bundle_cache_bytes():
    # Cap the cache at 1/4 of system RAM (a 2 GB VPS gets 512 MB, not 1.5 GB —
    # the flat default OOM-killed small hosts); env SPIRIT_BUNDLE_CACHE_BYTES overrides.
    ceiling = 1536 * 1024 * 1024
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    total = int(line.split()[1]) * 1024
                    return max(128 * 1024 * 1024, min(ceiling, total // 4))
    except OSError:
        pass
    return ceiling

# LRU cache for customized virtual-split bundles. Bounded by TOTAL BYTES, not entry
# count: a split bundle can be ~84 MB, so a 128-entry count cap could pin ~7.7 GB.
VIRTUAL_BUNDLE_CACHE = OrderedDict()
VIRTUAL_BUNDLE_CACHE_MAX_BYTES = int(os.environ.get("SPIRIT_BUNDLE_CACHE_BYTES", str(_default_bundle_cache_bytes())))
_VIRTUAL_BUNDLE_BYTES = 0
_VIRTUAL_BUNDLE_LOCK = threading.Lock()

# Per-key build locks so a stampede of first requests for one split does ONE UnityPy
# reparse (a 60 MB bundle costs ~3s) while the rest wait and then hit the cache.
_VIRTUAL_BUILD_LOCKS = {}
_VIRTUAL_BUILD_LOCKS_GUARD = threading.Lock()

# Global cap on concurrent UnityPy rebuilds: each one peaks at several hundred MB
# (decompressed textures + LZ4 repack), and per-key locks alone let N sets build at once.
_VIRTUAL_BUILD_SEMAPHORE = threading.BoundedSemaphore(
    max(1, int(os.environ.get("SPIRIT_BUNDLE_BUILD_CONCURRENCY", "1"))))

def _bundle_build_lock(key):
    with _VIRTUAL_BUILD_LOCKS_GUARD:
        lock = _VIRTUAL_BUILD_LOCKS.get(key)
        if lock is None:
            lock = threading.Lock()
            _VIRTUAL_BUILD_LOCKS[key] = lock
        return lock

def _bundle_cache_get(key):
    with _VIRTUAL_BUNDLE_LOCK:
        data = VIRTUAL_BUNDLE_CACHE.get(key)
        if data is not None:
            VIRTUAL_BUNDLE_CACHE.move_to_end(key)
        return data

def _bundle_cache_put(key, data):
    global _VIRTUAL_BUNDLE_BYTES
    with _VIRTUAL_BUNDLE_LOCK:
        old = VIRTUAL_BUNDLE_CACHE.get(key)
        if old is not None:
            _VIRTUAL_BUNDLE_BYTES -= len(old)
        VIRTUAL_BUNDLE_CACHE[key] = data
        VIRTUAL_BUNDLE_CACHE.move_to_end(key)
        _VIRTUAL_BUNDLE_BYTES += len(data)
        while _VIRTUAL_BUNDLE_BYTES > VIRTUAL_BUNDLE_CACHE_MAX_BYTES and len(VIRTUAL_BUNDLE_CACHE) > 1:
            _, evicted = VIRTUAL_BUNDLE_CACHE.popitem(last=False)
            _VIRTUAL_BUNDLE_BYTES -= len(evicted)

# LRU cache of filename -> resolved on-disk path (skips the os.walk probing per request)
ASSET_PATH_CACHE = OrderedDict()
ASSET_PATH_CACHE_MAX = 1024
_ASSET_PATH_LOCK = threading.Lock()

def _asset_path_cache_get(filename):
    with _ASSET_PATH_LOCK:
        path = ASSET_PATH_CACHE.get(filename)
        if path is not None:
            ASSET_PATH_CACHE.move_to_end(filename)
    if path is not None and not os.path.exists(path):
        with _ASSET_PATH_LOCK:
            ASSET_PATH_CACHE.pop(filename, None)
        return None
    return path

def _asset_path_cache_put(filename, path):
    with _ASSET_PATH_LOCK:
        ASSET_PATH_CACHE[filename] = path
        ASSET_PATH_CACHE.move_to_end(filename)
        while len(ASSET_PATH_CACHE) > ASSET_PATH_CACHE_MAX:
            ASSET_PATH_CACHE.popitem(last=False)


def register_asset_path(path):
    """Adds a newly-created bundle cache to serving and refreshes the manifest.

    Admin-managed landing artwork can create ``externalCache`` after server
    startup, so the one-time module initialization above cannot be relied on to
    discover it.  ``ManifestManager`` intentionally shares the ASSET_PATHS list.
    """
    asset_path = os.path.abspath(os.fspath(path))
    if not os.path.isdir(asset_path):
        raise FileNotFoundError(f"Asset cache does not exist: {asset_path}")
    normalized = os.path.normcase(asset_path)
    if not any(os.path.normcase(os.path.abspath(p)) == normalized for p in ASSET_PATHS):
        ASSET_PATHS.append(asset_path)
    with _ASSET_PATH_LOCK:
        ASSET_PATH_CACHE.clear()
    manifest_manager.refresh()


class MockHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # HTTP/1.1 keep-alive reuses one TCP connection for many asset bundles
    # (remote clients otherwise pay a handshake per card set). Requires an
    # accurate Content-Length on EVERY response; timeout reaps idle sockets.
    protocol_version = "HTTP/1.1"
    timeout = 60

    def handle(self):
        # Idle keep-alive sockets get RST by the remote client/NAT; swallow the
        # benign disconnect instead of letting socketserver dump a traceback.
        try:
            super().handle()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError, TimeoutError):
            self.close_connection = True

    def log_message(self, format, *args):
        logging.debug(f"[HTTP] {self.client_address[0]} - - [{self.log_date_time_string()}] {format%args}")

    def log_error(self, format, *args):
        # Routine keep-alive reaping (idle timeout / reset) surfaces here — keep it out of INFO.
        logging.debug(f"[HTTP] {self.client_address[0]} - {format % args}")

    def serve_admin(self, method, parsed_path, body=None):
        """Delegates /admin requests to the Admin Dashboard API."""
        from spirit.server.admin_api import route_admin
        result = route_admin(method, parsed_path, body, headers=self.headers)
        extra_headers = []
        if len(result) == 4:
            status, payload, content_type, extra_headers = result
        else:
            status, payload, content_type = result
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.send_header('Content-Length', str(len(payload)))
        for name, value in extra_headers:
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        logging.debug(f"[HTTP] GET Request received for path: {self.path}")
        metrics.inc("http_requests")

        # Clean the path to ignore query parameters
        parsed_path = urlparse(self.path).path

        if parsed_path == '/health':
            return self._serve_health()
        if parsed_path == '/admin/api/metrics':
            return self.serve_admin('GET', parsed_path)

        if parsed_path == '/admin' or parsed_path.startswith('/admin/'):
            return self.serve_admin('GET', parsed_path)

        # The client adds dynamic GUIDs to the path, so we catch anything ending in .unity3d
        if parsed_path.endswith(".unity3d"):
            return self.handle_cdn_asset(parsed_path)

        # Routing dictionary
        routes = {
            "messaging/manifest.json": self.handle_messaging_manifest,
            "manifest.json": self.handle_patch_manifest,
            "manifest.version": self.handle_manifest_version,
            ".manifest": self.handle_asset_manifest,
            "config.json": self.handle_config,
            "dynamic_config.json": self.handle_config,
            "motd.json": self.handle_motd,
            "sso/login": self.handle_cas_login,
            "placeholder.png": self.handle_placeholder_image,
            "eula/en_us_agreement_pc.txt": self.handle_eula_us_agreement,
            "privacypolicy/en_us_privacy_policy_pc.txt": self.handle_privacy_policy,
        }

        # Check for product images
        # Intercept both explicit /products/ requests and logical asset name requests to prevent Shop 404s
        if "/products/" in parsed_path or not any(parsed_path.endswith(ext) for ext in [".unity3d", ".json", ".txt"]):
            filename = os.path.basename(parsed_path).lower()
            
            custom_dirs = [
                os.path.join(ASSET_DIR, "products", "custom_packs"),
                os.path.join(ASSET_DIR, "products", "custom_pcds"),
                os.path.join(ASSET_DIR, "products", "custom_sleeves"),
                os.path.join(ASSET_DIR, "products", "custom_coins"),
                os.path.join(ASSET_DIR, "products", "custom_deckboxes"),
                os.path.join(ASSET_DIR, "products"),
            ]
            
            base_name = filename.replace(".png", "")
            candidates = [filename, f"{filename}.png", base_name, f"{base_name}.png"]
            
            for d in custom_dirs:
                if not os.path.exists(d):
                    continue
                for cand in candidates:
                    product_path = os.path.join(d, cand)
                    if os.path.exists(product_path) and os.path.isfile(product_path):
                        logging.debug(f"[HTTP] Product Image Match Found: {parsed_path} -> {product_path}")
                        return self.serve_static_file(product_path, 'image/png')

        for route_key, handler in routes.items():
            if parsed_path.endswith(route_key):
                return handler()

        return self.handle_default()

    def handle_eula_us_agreement(self):
        eula_path = os.path.join(ASSET_DIR, "eula", "en_us_agreement_pc.txt")
        return self.serve_static_file(eula_path, 'text/plain; charset=utf-8')

    def handle_privacy_policy(self):
        privacy_path = os.path.join(ASSET_DIR, "eula", "en_us_privacy_policy_pc.txt")
        return self.serve_static_file(privacy_path, 'text/plain; charset=utf-8')

    def _serve_health(self):
        """Liveness/readiness probe: 200 once content is loaded, else 503."""
        try:
            from spirit.packets.handlers import data_sync
            ready = bool(getattr(data_sync, "CARDS_DB", None))
        except Exception:
            ready = False
        payload = json.dumps({"status": "ok" if ready else "loading", "ready": ready}).encode('utf-8')
        self.send_response(200 if ready else 503)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def serve_static_file(self, file_path, content_type):
        if os.path.exists(file_path):
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Content-Length', str(os.path.getsize(file_path)))
            self.end_headers()
            # Stream in chunks: a full f.read() of a large asset holds the whole file
            # in RAM per handler thread (up to ~84 MB for a set bundle).
            import shutil
            with open(file_path, 'rb') as f:
                shutil.copyfileobj(f, self.wfile, 256 * 1024)
        else:
            logging.warning(f"[HTTP] File Not Found: {file_path}")
            return self.handle_default()

    def handle_placeholder_image(self):
        """Serves a 1x1 transparent PNG to satisfy DuiTexture.LoadFromURL"""
        # 1x1 Transparent PNG
        png_data = bytes.fromhex("89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4890000000b4944415478da6360000000020001737501180000000049454e44ae426082")
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.send_header('Content-length', str(len(png_data)))
        self.end_headers()
        self.wfile.write(png_data)

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        # NEVER log the body: CAS login and /admin POST carry passwords/tickets.
        logging.debug(f"[HTTP] POST path={self.path} ({content_length} bytes)")
        parsed_path = urlparse(self.path).path

        if parsed_path == '/admin' or parsed_path.startswith('/admin/'):
            return self.serve_admin('POST', parsed_path, post_data)

        # Routing dictionary
        routes = {
            "sso/login": self.handle_cas_login
        }

        for route_key, handler in routes.items():
            if parsed_path.endswith(route_key):
                return handler(post_data)

        return self.handle_default()

    def send_json_response(self, data):
        """Helper to send standard JSON responses"""
        payload = json.dumps(data).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def handle_patch_manifest(self):
        """Source Logic: client_source/pie/pie-src/CheckForPatchBehavior.cs"""
        host = self.headers.get("Host", state.SERVER_HOST)
        response = {
            "LatestWindowsPatcherVersion": 240,
            "LatestMacPatcherVersion": 240,
            "LatestWindowsClientVersion": 5815,
            "LatestMacClientVersion": 5815,
            "WindowsPatcherDownloadLink": f"http://{host}/refresher.zip",
            "MacPatcherDownloadLink": f"http://{host}/refresher.zip"
        }
        self.send_json_response(response)

    def handle_messaging_manifest(self):
        """Source Logic: ServerManifestDataRetriever.cs — null 'messaging' array NREs the Tournament scene."""
        host = self.headers.get("Host", state.SERVER_HOST)
        self.send_json_response({"cdn_url": f"http://{host}/", "messaging": []})

    def handle_manifest_version(self):
        """Source Logic: LoadManifestVersion.cs"""
        logging.info(f"[HTTP] Sending Manifest Version: {manifest_manager.manifest_version}")
        payload = str(manifest_manager.manifest_version).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def handle_asset_manifest(self):
        """Source Logic: LoadManifest.cs (Requires GZip compression)"""
        logging.info("[HTTP] Sending Full Asset Manifest (GZipped)...")
        payload = manifest_manager.generate_manifest()
        self.send_response(200)
        self.send_header('Content-type', 'application/x-gzip')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def handle_cdn_asset(self, path):
        """Serves .unity3d files using a Robust Matcher to handle client path mangling."""
        filename = os.path.basename(path)
        asset_full_path = None

        # 1. Generate candidates for matching
        # Candidate 1: Full name without extension (e.g. en_US_Free_Energy_1)
        full_no_ext = filename.replace(".unity3d", "")

        # Candidate 2: Normalized (stripped redundant prefixes and version suffixes)
        # e.g. en_US_en_US_Free_Energy_1 -> en_US_Free_Energy
        normalized = re.sub(r'_\d+(\.unity3d)?$', '', filename)
        normalized = re.sub(r'^(en_US_)+', 'en_US_', normalized).replace(".unity3d", "")

        # Candidate 3: Clean base (no locale)
        clean_base = normalized.replace("en_US_", "")

        # Handle virtual type-split suffixes by stripping them (e.g. SWSH12_water -> SWSH12)
        split_suffixes = [
            "_grass", "_fire", "_water", "_lightning", "_psychic", "_fighting",
            "_darkness", "_metal", "_fairy", "_dragon", "_colorless", "_trainer"
        ]
        
        clean_base_stripped = clean_base
        for suffix in split_suffixes:
            if clean_base.lower().endswith(suffix):
                clean_base_stripped = clean_base[:-len(suffix)]
                break

        candidates = [full_no_ext, normalized, clean_base]

        # Candidate 4: Clean base without version suffix
        clean_no_suffix = re.sub(r'_\d+$', '', clean_base)
        if clean_no_suffix not in candidates:
            candidates.append(f"en_US_{clean_no_suffix}")
            candidates.append(clean_no_suffix)

        # Candidate 5: Stripped split-suffix variants (allows SWSH12_water -> en_US_SWSH12)
        if clean_base_stripped != clean_base:
            clean_stripped_no_suffix = re.sub(r'_\d+$', '', clean_base_stripped)
            for variant in [clean_base_stripped, clean_stripped_no_suffix]:
                if variant not in candidates:
                    candidates.append(f"en_US_{variant}")
                    candidates.append(variant)

        cached_path = _asset_path_cache_get(filename)
        if cached_path is not None:
            asset_full_path = cached_path

        # Search across all registered asset paths
        for base_dir in ASSET_PATHS if asset_full_path is None else []:
            if not os.path.exists(base_dir):
                continue

            # Priority 1: Exact directory match for candidates
            for candidate in candidates:
                potential_folder = os.path.join(base_dir, candidate)
                if os.path.exists(potential_folder) and os.path.isdir(potential_folder):
                    for root, _, files in os.walk(potential_folder):
                        if "__data" in files:
                            asset_full_path = os.path.join(root, "__data")
                            logging.debug(f"[HTTP] Match Found: {filename} -> {asset_full_path} (via {candidate})")
                            break
                if asset_full_path: break
            if asset_full_path: break
            # Priority 2: Direct file match
            test_path = os.path.join(base_dir, filename)
            if os.path.exists(test_path) and os.path.isfile(test_path):
                asset_full_path = test_path
                break
            
            # Priority 3: Fuzzy fallback (only if desperate)
            for entry in os.listdir(base_dir):
                entry_path = os.path.join(base_dir, entry)
                if clean_base_stripped.lower() in entry.lower():
                    if os.path.isdir(entry_path):
                        for root, _, files in os.walk(entry_path):
                            if "__data" in files:
                                asset_full_path = os.path.join(root, "__data")
                                logging.info(f"[HTTP] Fuzzy Match: {filename} -> {asset_full_path}")
                                break
                if asset_full_path: break
            if asset_full_path: break

        logging.debug(f"[HTTP] Asset Requested: {filename} (Path: {path})")

        if asset_full_path and cached_path is None:
            _asset_path_cache_put(filename, asset_full_path)

        if asset_full_path and os.path.exists(asset_full_path):
            is_virtual_split = (clean_base_stripped != clean_base)

            cached_bytes = _bundle_cache_get(filename) if is_virtual_split else None
            if cached_bytes is not None:
                file_bytes = cached_bytes
                logging.debug(f"[HTTP] Serving customized CAB for {filename} from MEMORY CACHE")
            elif is_virtual_split:
                # Serialize concurrent first-requests for this key onto ONE rebuild.
                build_lock = _bundle_build_lock(filename)
                with build_lock:
                    cached_bytes = _bundle_cache_get(filename)
                    if cached_bytes is not None:
                        file_bytes = cached_bytes
                    else:
                        file_bytes = self._build_virtual_split(
                            filename, asset_full_path, clean_base)
            else:
                with open(asset_full_path, 'rb') as f:
                    file_bytes = f.read()

            self.send_response(200)
            self.send_header('Content-type', 'application/vnd.unity')
            self.send_header('Content-Length', str(len(file_bytes)))
            # Enable client-side caching of static Unity asset bundles to prevent redownload cache write collisions
            self.send_header('Cache-Control', 'public, max-age=31536000')
            self.end_headers()
            self.wfile.write(file_bytes)
            logging.debug(f"[HTTP] Asset Sent Successfully: {filename} from {asset_full_path}")
            return
        else:
            logging.warning(f"[HTTP] Asset Not Found on Disk: {filename}")
            self.send_response(404)
            self.send_header('Content-Length', '0')
            self.end_headers()

    def _build_virtual_split(self, filename, asset_full_path, clean_base):
        """CAB-renames a virtual-split bundle and caches the result. Caller holds
        the per-key build lock so only one rebuild runs per key."""
        # Cross-key builds also serialize (global semaphore) to bound peak RAM.
        with _VIRTUAL_BUILD_SEMAPHORE:
            return self._build_virtual_split_locked(filename, asset_full_path, clean_base)

    def _build_virtual_split_locked(self, filename, asset_full_path, clean_base):
        with open(asset_full_path, 'rb') as f:
            file_bytes = f.read()

        # Stable, unique CAB name for this virtual split bundle (deterministic).
        h_virt = hashlib.md5(clean_base.encode('utf-8')).hexdigest()
        new_cab_name = f"CAB-{h_virt}"

        try:
            # Parse and safely rename inside the AssetBundle structure using UnityPy
            env: Any = UnityPy.load(file_bytes)

            # 1. Rename the entry key in env.file.files
            if hasattr(env, 'file') and hasattr(env.file, 'files'):
                old_keys = [k for k in env.file.files.keys() if k.startswith('CAB-')]
                for old_key in old_keys:
                    env.file.files[new_cab_name] = env.file.files.pop(old_key)

            # 2. Update all asset names inside env.assets
            for asset in env.assets:
                if hasattr(asset, 'name') and asset.name.startswith('CAB-'):
                    asset.name = new_cab_name

            # 3. Serialize back with LZ4 packer
            file_bytes = env.file.save(packer="lz4")
            _bundle_cache_put(filename, file_bytes)
            logging.info(f"[HTTP] Customized CAB via UnityPy for {filename} -> {new_cab_name} and cached.")
        except Exception as e:
            logging.warning(f"[HTTP] UnityPy CAB customize failed ({e}); raw byte replacement fallback.")
            # Fallback to byte replacement for non-standard/mock asset bundles (e.g. in test suites)
            new_cab_bytes = new_cab_name.encode('utf-8')
            old_cab_legacy = b"CAB-698f1293cb9396443b3f13ebe0cec855"

            physical_bundle_name = os.path.basename(os.path.dirname(os.path.dirname(asset_full_path)))
            h_phys = hashlib.md5(physical_bundle_name.encode('utf-8')).hexdigest()
            old_cab_phys = f"CAB-{h_phys}".encode('utf-8')

            if old_cab_legacy in file_bytes:
                file_bytes = file_bytes.replace(old_cab_legacy, new_cab_bytes)
            if old_cab_phys in file_bytes:
                file_bytes = file_bytes.replace(old_cab_phys, new_cab_bytes)

            _bundle_cache_put(filename, file_bytes)
        return file_bytes

    def handle_config(self):
        """Source Logic: PieDynamicConfig.cs"""
        # Dynamically record the host being used by the client
        host = self.headers.get("Host", state.SERVER_HOST)
        state.SERVER_HOST = host

        # The AssetURL is the base for all .unity3d downloads.
        cdn_base = f"http://{host}/"

        self.send_json_response({
            "hostName": f"http://{host}/cas",
            "AssetURL": cdn_base,
            "collectorURL": f"http://{host}/collector/",
            "helpButtonDestination": f"http://{host}/help/",
            "localizedSignup": f"http://{host}/signup/",
            "serviceID": "pokemon_tcgo",
            "bacgroundRelease": "lobby" # Points to the broad lobby alias in our manifest
        })

    def handle_motd(self):
        """Source Logic: ShowSystemMessageBehaviour.cs"""
        current_time_ms = int(time.time() * 1000)
        response = {
            "message": {
                "en": "Welcome to Brandon's PTCGO Private Server!",
                "en_US": "Welcome to Brandon's PTCGO Private Server!",
                "en_UK": "Welcome to Brandon's PTCGO Private Server!"
            },
            "urgency": "High",
            "date": current_time_ms
        }
        self.send_json_response(response)

    def handle_cas_login(self, post_data=None):
        """Source Logic: O.X.cs (CasAuthCommand)"""

        if self.command == 'GET':
            # The client's regex expects name="lt" value="..." and name="execution" value="..."
            # Based on PrivateImplementationDetails decryption, regexes are approx 45-52 chars.
            html = """
            <!DOCTYPE html>
            <html>
            <body>
                <form action="" method="post">
                    <input type="hidden" name="lt" value="LT-MOCK-TOKEN-12345" />
                    <input type="hidden" value="LT-MOCK-TOKEN-12345" name="lt" />
                    <input name="lt" type="hidden" value="LT-MOCK-TOKEN-12345" />

                    <input type="hidden" name="execution" value="e1s1" />
                    <input type="hidden" value="e1s1" name="execution" />
                    <input name="execution" type="hidden" value="e1s1" />

                    <input type="text" name="username" />
                    <input type="password" name="password" />
                    <input type="submit" name="submit" value="Login" />
                </form>
            </body>
            </html>
            """
            payload = html.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        elif self.command == 'POST':
            # 1. Parse Credentials
            if post_data is None:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode('utf-8')

            params = parse_qs(post_data)

            username = params.get('username', [''])[0]
            password = params.get('password', [''])[0]

            logging.info(f"[HTTP] Login attempt for user: {username}")

            # 2. Validate Password
            account = get_account_by_username(username)
            if not account:
                # Auto-register for this private server
                logging.info(f"[HTTP] User '{username}' not found. Auto-registering...")
                account = create_account(username, password)

            if account and verify_password(account['password_hash'], password):
                # 3. Success! Generate a Ticket (never log the ticket — it is a live
                # bearer credential valid for the CAS TTL).
                ticket = f"ST-{uuid.uuid4()}"
                state.sweep_expired_tickets()
                issue_ticket(ticket, username)
                logging.info(f"[HTTP] Password verified for '{username}'. Ticket issued.")
                metrics.inc("cas_tickets_issued")

                # 4. Redirect with Ticket
                host = self.headers.get("Host", state.SERVER_HOST)
                body = f"ticket={ticket}\n?ticket={ticket}\n&ticket={ticket}".encode('utf-8')
                self.send_response(302)
                self.send_header('Location', f'http://{host}/cas/sso/login?ticket={ticket}')
                self.send_header('Content-type', 'text/html')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            else:
                # 5. Failure
                logging.warning(f"[HTTP] Invalid password for user: {username}")
                body = b"Authentication Failed. Check your credentials."
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)


    def handle_default(self):
        """Fallback for unhandled assets or telemetry to prevent freezing"""
        payload = b"{}"
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

class AssetHTTPServer:
    def __init__(self, host='0.0.0.0', port=config.HTTP_PORT):
        self.host = host
        self.port = port
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        self.server = socketserver.ThreadingTCPServer((self.host, self.port), MockHTTPRequestHandler)
        self.thread = None

    def start(self):
        logging.info(f"Asset HTTP Server listening on http://{self.host}:{self.port}")
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()
        if self.thread:
            self.thread.join()
        logging.info("Asset HTTP Server stopped.")
