import os
import json
import hashlib
import gzip
import logging
import re
import time
import zlib
import UnityPy

from spirit import config

class ManifestManager:
    """
    Dynamic Asset Manifest Generator.
    Scans multiple directories and builds a versioned manifest for the Unity client.
    """
    def __init__(self, asset_dirs: list):
        self.asset_dirs = asset_dirs
        self.manifest_cache = None
        # Use timestamp to force refresh
        self.manifest_version = int(time.time())

        self.asset_map = {}
        map_path = os.path.join(os.path.dirname(__file__), "asset_map.json")
        if os.path.exists(map_path):
            try:
                with open(map_path, "r") as f:
                    self.asset_map = json.load(f)
                logging.info(f"[Manifest] Loaded asset_map.json with {len(self.asset_map)} bundles.")
            except Exception as e:
                logging.error(f"[Manifest] Failed to load asset_map.json: {e}")

        for d in self.asset_dirs:
            if not os.path.exists(d):
                os.makedirs(d, exist_ok=True)
                logging.info(f"[Manifest] Created asset directory: {d}")

        # Initial scan
        self.generate_manifest(force_refresh=True)

    def _calculate_md5(self, filepath: str) -> str:
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def _calculate_crc(self, filepath: str) -> int:
        """Calculates CRC32 of a file, ensuring it fits in a uint32."""
        try:
            with open(filepath, "rb") as f:
                return zlib.crc32(f.read()) & 0xFFFFFFFF
        except Exception as e:
            logging.error(f"CRC calculation error: {e}")
            return 0

    def generate_manifest(self, force_refresh: bool = False) -> bytes:
        """Generates a GZipped manifest JSON for the client in the proprietary V3 format."""
        if self.manifest_cache and not force_refresh:
            return self.manifest_cache

        logging.info(f"[Manifest] Generating V3 Manifest (Version: {self.manifest_version})...")

        # Preload bundles: critical for scene loading
        # The client explicitly requests these by name.
        preload_names = ["LandingPage", "Logos", "Login", "lobby", "Background", "Localization", "ali"]

        # Dictionary to store unique descriptors by their logical name
        unique_descriptors = {}

        # Walk through all registered asset directories
        for asset_dir in self.asset_dirs:
            if not os.path.exists(asset_dir):
                continue
            
            entries = sorted(os.listdir(asset_dir))
            for entry in entries:
                entry_path = os.path.join(asset_dir, entry)
                bundle_file_path = None
                bundle_name_raw = entry.replace(".unity3d", "")
                
                if os.path.isfile(entry_path) and entry.endswith(".unity3d"):
                    bundle_file_path = entry_path
                elif os.path.isdir(entry_path):
                    for root, _, files in os.walk(entry_path):
                        if "__data" in files:
                            bundle_file_path = os.path.join(root, "__data")
                            break
                
                if not bundle_file_path:
                    continue

                logical_name = bundle_name_raw
                if logical_name.startswith("en_US_"):
                    logical_name = logical_name[6:]
                
                if logical_name in unique_descriptors:
                    continue

                # Calculate real CRC and version
                bundle_crc = self._calculate_crc(bundle_file_path)
                
                # Version logic: We use the file mtime as a simple versioning proxy
                # PTCGO client compares Version and CRC. If either changes, it redownloads.
                bundle_version = int(os.path.getmtime(bundle_file_path))

                asset_names = []
                aliases = {bundle_name_raw, logical_name}
                lower_entry = entry.lower()
                if "landingpage" in lower_entry: aliases.add("LandingPage")
                if "logos" in lower_entry: aliases.add("Logos")
                if "login" in lower_entry: aliases.add("Login")
                if "lobby" in lower_entry: aliases.add("lobby")
                if "background" in lower_entry: aliases.add("Background")
                if "ali_" in lower_entry: 
                    aliases.add("ali")
                    aliases.add("Localization")

                set_code = None
                map_lookup_name = bundle_name_raw
                if map_lookup_name.startswith("en_US_"):
                    map_lookup_name = map_lookup_name[6:]
                map_lookup_name = re.sub(r'_\d+$', '', map_lookup_name)
                
                exact_assets = self.asset_map.get(bundle_name_raw) or \
                               self.asset_map.get(f"en_US_{map_lookup_name}") or \
                               self.asset_map.get(map_lookup_name)

                # Dynamically load assets for cosmetic/product bundles if not in asset_map
                if not exact_assets and any(pat in bundle_name_raw for pat in ["cardSleeves", "coins", "deckBoxes", "packs", "pcdBoxes", "avatar", "GXToken", "VSTARToken"]):
                    try:
                        env = UnityPy.load(bundle_file_path)
                        exact_assets = []
                        prefix = ""
                        if "cardSleeves" in bundle_name_raw:
                            prefix = "cardSleeves"
                        elif "coins" in bundle_name_raw:
                            prefix = "coins"
                        elif "deckBoxes" in bundle_name_raw:
                            prefix = "deckBoxes"
                        elif "packs" in bundle_name_raw:
                            prefix = "packs"
                        elif "pcdBoxes" in bundle_name_raw:
                            prefix = "pcdBoxes"
                        elif "avatar_thumbs" in bundle_name_raw:
                            prefix = "avatar_thumbs"
                        elif "avatar" in bundle_name_raw:
                            prefix = "avatar"
                        elif "GXToken" in bundle_name_raw:
                            prefix = "gxtoken"
                        elif "VSTARToken" in bundle_name_raw:
                            prefix = "vstartoken"
                            
                        for obj in env.objects:
                            if obj.type.name == "Texture2D":
                                tex_name = obj.read().m_Name.lower()
                                exact_assets.append(tex_name)
                                if prefix:
                                    exact_assets.append(f"{prefix}/{tex_name}")
                                    # Add full URL-mode manifest mapping keys to satisfy client-side LoadTextureFromAssetBundle lookups
                                    url_route = f"{config.HTTP_BASE_URL}/products/{tex_name}.png"
                                    exact_assets.append(url_route)
                                    exact_assets.append(f"{prefix}/{url_route}")
                        logging.info(f"[Manifest] Dynamically loaded {len(exact_assets)} cosmetic/product assets with prefix '{prefix}' for {bundle_name_raw}")
                    except Exception as e:
                        logging.error(f"[Manifest] Failed to dynamically load cosmetic/product assets for {bundle_name_raw}: {e}")

                if exact_assets:
                    # Extract set code more reliably
                    set_code = None
                    if bundle_name_raw.startswith("en_US_"):
                        set_code = bundle_name_raw[6:]
                        # Remove versioning or collector number suffix (e.g., _1, _138)
                        # but keep set-internal underscores (e.g., Free_Energy)
                        # We only strip if it's a trailing number
                        set_code = re.sub(r'_\d+$', '', set_code)
                    else:
                        # Fallback for bundles without en_US prefix
                        parts = bundle_name_raw.split('_')
                        # Find the first part that isn't a known prefix or small version/locale
                        for part in parts:
                            if part not in ["en", "US", "CR", "CRR", "wp"] and len(part) >= 2:
                                set_code = part
                                break

                    foil_match = re.search(r'_(wp_[a-zA-Z0-9_]+?)(?:_\d+)?$', bundle_name_raw)

                    foil_prefix = foil_match.group(1) if foil_match else None
                    
                    for asset_key in exact_assets:
                        asset_names.append({"name": asset_key})

                        if set_code:
                            asset_names.append({"name": f"{set_code}/{asset_key}"})
                            asset_names.append({"name": f"{set_code}_{asset_key}"})

                            # "072", "foil_072", "072_energypip" also resolve
                            # without leading zeros
                            num_match = re.match(r'^(foil_)?(\d+)(_energypip|_toolpip)?$', asset_key)
                            if num_match:
                                short_num = num_match.group(2).lstrip("0") or "0"
                                if short_num != num_match.group(2):
                                    short_key = (f"{num_match.group(1) or ''}{short_num}"
                                                 f"{num_match.group(3) or ''}")
                                    asset_names.append({"name": f"{set_code}/{short_key}"})
                                    asset_names.append({"name": f"{set_code}_{short_key}"})
                        
                # Final asset list includes all aliases
                final_assets = asset_names + [{"name": a} for a in aliases]
                
                # Determine the 'best' name for the bundle descriptor
                # Special names like LandingPage must be UNIQUE in the manifest
                descriptor_name = logical_name
                for special in ["LandingPage", "Logos", "Login", "lobby", "Background", "Localization"]:
                    if special in aliases:
                        # Check if this special name is already taken
                        if not any(b['name'] == special for b in unique_descriptors.values()):
                            descriptor_name = special
                        break

                descriptor = {
                    "name": descriptor_name,
                    "assets": final_assets,
                    "versionings": [
                        {
                            "platform": "pc",
                            "locale": "en_US",
                            "version": bundle_version,
                            "alt_version": 0,
                            "CRC": 0 # Force CRC 0 for custom bundles to prevent crashes
                        }
                    ],
                    "precached": [],
                    "timesensitive": 0,
                    "WebPath": f"en_US/{bundle_name_raw}.unity3d"
                }
                unique_descriptors[logical_name] = descriptor

                # If this is a card set bundle, dynamically generate virtual type-split bundle descriptors
                # so the client can resolve things like "SWSH12_water" to this same physical bundle file.
                if set_code and exact_assets and not any(pat in bundle_name_raw for pat in ["cardSleeves", "coins", "deckBoxes", "packs", "pcdBoxes", "avatar"]):
                    card_types = [
                        "grass", "fire", "water", "lightning", "psychic", "fighting",
                        "darkness", "metal", "fairy", "dragon", "colorless", "trainer"
                    ]
                    for t_name in card_types:
                        virtual_name = f"{set_code}_{t_name}"
                        # Ensure we don't overwrite if physical file already exists
                        if virtual_name not in unique_descriptors:
                            unique_descriptors[virtual_name] = {
                                "name": virtual_name,
                                "assets": [{"name": virtual_name}],
                                "versionings": [
                                    {
                                        "platform": "pc",
                                        "locale": "en_US",
                                        "version": bundle_version,
                                        "alt_version": 0,
                                        "CRC": 0
                                    }
                                ],
                                "precached": [],
                                "timesensitive": 0,
                                "WebPath": f"en_US/{bundle_name_raw}.unity3d"
                            }

        bundle_descriptors = list(unique_descriptors.values())
        actual_preloads = [n for n in preload_names if any(b['name'] == n for b in bundle_descriptors)]

        logging.info(f"[Manifest] Generated {len(bundle_descriptors)} bundle descriptors. Preloading: {actual_preloads}")

        manifest_data = {
            "platform": "pc",
            "version": self.manifest_version,
            "bundles": bundle_descriptors,
            "preloadBundles": actual_preloads,
            "forceloadBundles": []
        }

        json_data = json.dumps(manifest_data).encode('utf-8')
        self.manifest_cache = gzip.compress(json_data)
        return self.manifest_cache

    def refresh(self):
        """Invalidates the cache and increments version."""
        self.manifest_version += 1
        self.generate_manifest(force_refresh=True)
