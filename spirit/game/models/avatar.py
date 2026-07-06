import os
import re
import uuid
import logging
import hashlib
import json
import UnityPy
import sys

# Ensure protobuf compiled directory is in sys.path
protobuf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'protobuf', 'compiled'))
if protobuf_path not in sys.path:
    sys.path.insert(0, protobuf_path)

from spirit.game.attributes import AttrID
from dwd.Protobuf import base_pb2

class AvatarArchetype:
    """
    Object-oriented representation of an Avatar Archetype, handling Protobuf conversion.
    """
    def __init__(self, guid: str, gender: int, group: int, base_name: str, style_hash: int, is_dummy: bool = False):
        self.guid = guid
        self.gender = gender
        self.group = group
        self.base_name = base_name
        self.style_hash = style_hash
        self.is_dummy = is_dummy

    def to_proto(self, proto_container, to_uuid_func):
        """
        Adds this archetype to a protobuf Archetypes container.
        """
        arch = proto_container.add()
        to_uuid_func(uuid.UUID(self.guid), arch.guid)

        def add_int(attr_id: int, val: int):
            attr = arch.attributes.add()
            attr.name = int(attr_id)
            attr.value.objectType = base_pb2.Object.Type.INT
            attr.value.intValue = val

        def add_json(attr_id: int, val_id: str):
            attr = arch.attributes.add()
            attr.name = int(attr_id)
            attr.value.objectType = base_pb2.Object.Type.JSON
            attr.value.stringValue = json.dumps({"id": val_id})

        def add_bool(attr_id: int, val: bool):
            attr = arch.attributes.add()
            attr.name = int(attr_id)
            attr.value.objectType = base_pb2.Object.Type.BOOL
            attr.value.boolValue = val

        # Shared Attributes
        add_int(AttrID.AVATAR_GENDER, self.gender)
        add_int(AttrID.AVATAR_GROUP, self.group)
        add_json(AttrID.AVATAR_BUNDLE_NAME, self.base_name)
        add_json(AttrID.NAME, self.base_name)
        add_json(AttrID.AVATAR_RARITY, "Common")
        add_bool(AttrID.AVATAR_IS_FREE, True)
        add_int(AttrID.AVATAR_STYLE_LINK_ID, self.style_hash)

        if not self.is_dummy:
            # Calculate style_name and gender suffix for real items
            style_name = self.base_name[1:] if (self.base_name.startswith("f") or self.base_name.startswith("m")) else self.base_name
            suffix = "_female" if self.gender == 0 else "_male"
            style_id_str = f"{style_name}{suffix}"
            add_json(AttrID.AVATAR_STYLE_COLLECTION_NAME, style_id_str)
        else:
            add_bool(AttrID.AVATAR_IS_DEFAULT, True)
            add_json(AttrID.AVATAR_STYLE_COLLECTION_NAME, f"{self.base_name}_male")


GROUPS = {
    "eyes": 0,
    "eyebrows": 1,
    "face": 2,
    "face_prop": 3,
    "face_makeup": 4,
    "facial_hair": 5,
    "hair": 6,
    "hat": 7,
    "jacket": 8,
    "trousers": 9,
    "mouth": 10,
    "nose": 11,
    "shirt": 12,
    "shoes": 13,
    "shape": 14,
    "skin_color": 15
}

# Thread-safe global cache
_AVATAR_ITEMS_CACHE = None

def parse_texture_name(tex_name: str):
    group_id = None
    base_name = tex_name
    for group_name, g_val in GROUPS.items():
        if tex_name.endswith(f"_{group_name}"):
            group_id = g_val
            base_name = tex_name[:-(len(group_name) + 1)]
            break
    if group_id is None:
        if "_jacket" in tex_name:
            group_id = GROUPS["jacket"]
            base_name = re.sub(r'_jacket[a-z]+$', '', tex_name)
        elif "_shirt" in tex_name:
            group_id = GROUPS["shirt"]
            base_name = re.sub(r'_shirt[a-z]+$', '', tex_name)
    gender = 1
    if tex_name.startswith("f"):
        gender = 0
    elif tex_name.startswith("m"):
        gender = 1
    return base_name, group_id, gender

def get_avatar_items() -> dict:
    """
    Lazy-loads and caches the list of all discovered avatar items from original asset bundles.
    """
    global _AVATAR_ITEMS_CACHE
    if _AVATAR_ITEMS_CACHE is not None:
        return _AVATAR_ITEMS_CACHE

    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "assets"))
    bundle_cache_dir = os.path.join(assets_dir, "bundleCache")
    external_cache_dir = os.path.join(assets_dir, "externalCache")

    items = {}

    # Inject standard skin colors to ensure the customizer has skin color choices (Group 15)
    skin_colors = {
        "dummy_skin_colorx_ffe0bd": "ffe0bd", # Light
        "dummy_skin_colorx_d4a373": "d4a373", # Tan
        "dummy_skin_colorx_8d5524": "8d5524"  # Dark
    }
    for name, hex_val in skin_colors.items():
        item_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"spirit_avatar_item_{name}"))
        items[name] = {
            "guid": item_id,
            "group": 15,
            "gender": 1, # Compatible
            "base_name": name,
            "style_hash": 1015
        }

    # Find directories to scan
    scan_dirs = []
    if os.path.exists(bundle_cache_dir):
        scan_dirs.append(bundle_cache_dir)
    if os.path.exists(external_cache_dir):
        scan_dirs.append(external_cache_dir)

    logging.info("[Avatar] Scanning bundle cache and external cache for avatar asset bundles...")
    for cache_dir in scan_dirs:
        for entry in os.listdir(cache_dir):
            if "avatar" in entry.lower() and not "thumbs" in entry.lower():
                folder_path = os.path.join(cache_dir, entry)
                bundle_file_path = None
                if os.path.isdir(folder_path):
                    for root, _, files in os.walk(folder_path):
                        if "__data" in files:
                            bundle_file_path = os.path.join(root, "__data")
                            break
                if bundle_file_path:
                    try:
                        env = UnityPy.load(bundle_file_path)
                        for obj in env.objects:
                            if obj.type.name == "Texture2D":
                                tex_name = obj.read().m_Name.lower()
                                if "characters" in tex_name or "mask" in tex_name:
                                    continue
                                base_name, group_id, gender = parse_texture_name(tex_name)
                                if group_id is not None:
                                    item_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"spirit_avatar_item_{base_name}"))

                                    # Generate a stable, unique 31-bit style hash (for P.F.f/200215 link ID lookup)
                                    style_name = base_name[2:] if (base_name.startswith("f_") or base_name.startswith("m_")) else base_name
                                    style_hash = int(hashlib.md5(style_name.encode()).hexdigest()[:8], 16) & 0x7FFFFFFF

                                    items[base_name] = {
                                        "guid": item_id,
                                        "group": group_id,
                                        "gender": gender,
                                        "base_name": base_name,
                                        "style_hash": style_hash
                                    }
                    except Exception as e:
                        logging.error(f"[Avatar] Failed to parse bundle {entry}: {e}")

    logging.info(f"[Avatar] Scanning complete. Cached {len(items)} unique avatar items.")
    _AVATAR_ITEMS_CACHE = items
    return items

def get_default_avatar_items_list() -> list:
    """
    Returns a default list of 16 avatar item GUIDs (one for each customization group),
    preferring real discovered Male items, falling back to dummy IDs.
    """
    real_items = get_avatar_items()
    avatar_items_list = []
    for g_idx in range(16):
        if g_idx == 15:
            # Inject our custom light skin color GUID as the default skin tone
            avatar_items_list.append("00000000-0000-0000-0000-000000000a0f")
            continue
        match = next((item for item in real_items.values() if item["group"] == g_idx and item["gender"] == 1), None)
        if match:
            avatar_items_list.append(match["guid"])
        else:
            avatar_items_list.append(f"00000000-0000-0000-0000-000000000a{g_idx:02x}")
    return avatar_items_list
