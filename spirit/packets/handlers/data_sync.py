import logging
import sys
import os
import hashlib
import json
import uuid
import sqlite3
import time

from spirit.game.models.avatar import get_avatar_items, get_default_avatar_items_list, AvatarArchetype
from spirit.database.player_data import merge_account_settings
from spirit.game.account_attributes import build_account_attributes
from spirit.network.protocol import WargFlags
from spirit.network.message_names import InboundMsg, OutboundMsg
from spirit.database.economy_data import list_dynamic_pages
from .base import BaseHandler, handle

# Pre-load the protobuf compiled path
p_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'protobuf', 'compiled')
)
if p_path not in sys.path:
    sys.path.insert(0, p_path)

from dwd.Protobuf.Progression import progression_pb2
from dwd.Protobuf.Collection import collection_pb2
from dwd.Protobuf.cake.item import cake_item_pb2
from dwd.Protobuf import base_pb2
from spirit.game.attributes import (
    AttrID, CardType, CurrencyType, ProductType, TrainerType, FeatureToken, DeckFormat
)

from spirit.database.social import get_incoming_invites_by_account_id
from spirit.database.player_data import get_merged_collection_payload, get_archetype_flags
from spirit.database.async_utils import run_db
from spirit.game.models.card import Card, PokemonCard, Rarities

from spirit.game.scripts.cards import loader as card_loader
from spirit.game.scripts.products import loader as product_loader

SETS_DB_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'database', 'json_data', 'sets.json')
)
LOC_DB_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..', '..', 'database', 'game_data', 'LocalizationDB-UTF8.db'
    )
)

CARDS_DB = []
CARDS_BY_KEY = {}
PRODUCTS_DB = []
SETS_DB = []
SETS_CHECKSUM = hashlib.md5(b"[]").hexdigest()

# Per-process caches invalidated on reload: serialized card attrs and static payloads
_CARD_ATTRS_CACHE = {}
_STATIC_PAYLOAD_CACHE = {}


def _clear_derived_caches():
    _CARD_ATTRS_CACHE.clear()
    _STATIC_PAYLOAD_CACHE.clear()


def _cached_payload(name, builder):
    """Memoizes payloads derived purely from the loaded card/product/set data."""
    val = _STATIC_PAYLOAD_CACHE.get(name)
    if val is None:
        val = builder()
        _STATIC_PAYLOAD_CACHE[name] = val
    return val


def reload_cards():
    global CARDS_DB, CARDS_BY_KEY
    try:
        CARDS_DB = card_loader.load_all(force=True)
        logging.info(f"[DB] Loaded {len(CARDS_DB)} cards from scripts.")
    except Exception as e:
        logging.error(f"[DB] Failed to load card scripts: {e}")
    index = {}
    for card in CARDS_DB:
        index.setdefault(card.key, []).append(card)
    CARDS_BY_KEY = index
    _clear_derived_caches()

def reload_products():
    global PRODUCTS_DB
    try:
        products = product_loader.load_all()
        # Convert models back to the dict format expected by this legacy handler for now
        # to minimize disruption, or update the handler to use models.
        PRODUCTS_DB = [p.to_archetype_dict() for p in products]
        logging.info(f"[DB] Loaded {len(PRODUCTS_DB)} products from scripts.")
    except Exception as e:
        logging.error(f"[DB] Failed to load product scripts: {e}")
    _clear_derived_caches()


def reload_sets():
    global SETS_DB, SETS_CHECKSUM
    if os.path.exists(SETS_DB_PATH):
        try:
            with open(SETS_DB_PATH, 'r') as f:
                SETS_DB = json.load(f)
            # featuredArchetypes hold original-PTCGO card GUIDs we never load; the pack "i" popup
            # feeds them UNFILTERED into CachedViewModel (KeyNotFoundException). Clear them so the
            # popup falls back to the cache-safe preview-cards path (attr 201505) or the text panel.
            for s in SETS_DB:
                if s.get("featuredArchetypes"):
                    s["featuredArchetypes"] = []
            logging.info(f"[DB] Loaded {len(SETS_DB)} sets.")
        except Exception as e:
            logging.error(f"[DB] Failed to load sets: {e}")
    SETS_CHECKSUM = hashlib.md5(json.dumps(SETS_DB).encode()).hexdigest()
    _clear_derived_caches()


reload_cards()
reload_products()
reload_sets()

# Global cache for localizations
CACHED_LOCALIZATIONS = None
CACHED_LOCALIZATIONS_DICT = {}


def _load_localizations():
    """Loads the localization DB plus card display names into the module caches (idempotent)."""
    global CACHED_LOCALIZATIONS
    if CACHED_LOCALIZATIONS is not None:
        return
    localizations = []
    if os.path.exists(LOC_DB_PATH):
        try:
            conn = sqlite3.connect(LOC_DB_PATH)
            cursor = conn.cursor()
            # Industry Fix: Force case-insensitivity and filter out empty strings
            cursor.execute("SELECT key, value FROM Lookup WHERE value != ''")
            for key, value in cursor.fetchall():
                localizations.append({"key": key, "value": value})
                CACHED_LOCALIZATIONS_DICT[key.lower()] = value
            conn.close()
        except Exception as e:
            logging.error(f"[TCP] Failed to load localizations: {e}")

    custom_strings = [
        {"key": "ids_card_name_spirit", "value": "Spirit Card"},
        {"key": "minspec.init.collection", "value": "Initializing Spirit Collection..."}
    ]

    # Register card-specific display names
    for card in CARDS_DB:
        if card.display_name:
            name_attr = card.get_attribute_value(AttrID.NAME)
            if name_attr:
                try:
                    # name_attr could be JSON or a literal token
                    if isinstance(name_attr, str) and name_attr.startswith('{'):
                        token_id = json.loads(name_attr).get("id")
                    else:
                        token_id = str(name_attr)
                    if token_id:
                        custom_strings.append({"key": token_id, "value": card.display_name})
                except Exception:
                    pass

    localizations.extend(custom_strings)
    for item in custom_strings:
        CACHED_LOCALIZATIONS_DICT[item["key"].lower()] = item["value"]
    CACHED_LOCALIZATIONS = localizations

# Archetype keys prioritized for Energy sets
# "Free_Energy" MUST be first to prevent KeyNotFoundException in OwnedStacks
ARCHETYPE_KEYS = [
    "Free_Energy", "Energy", "Basic_Energy", "NoSet", "CUSTOM",
    "TK7A", "XY6", "Promo_HGSS", "XY2", "TK5B", "BW10", "BW4", "BW7",
    "TK8A", "TK9B", "SM7", "TATM", "XY9", "AvatarItems", "CP", "BW6",
    "TwentiethAnn", "SWSH6", "XY0", "BW5", "SL", "BW8", "HGSS1",
    "SM_Energy", "BW1", "SM3", "TK10B", "XY5", "HGSS2", "XY8", "TK5A",
    "COL", "TK6B", "Promo_BW", "XY12", "XY_Energy", "BW2", "RSP", "SM4",
    "TK9A", "SWSH5", "RewardItems", "HGSS3", "BW9", "XY1", "XY4", "TK10A",
    "SM2", "TK7B", "XY7", "XY11", "Promo_SM", "DV", "SF", "TK6A",
    "Promo_XY", "HGSS4", "BW11", "XY3", "TK8B", "XY10", "BW_Energy",
    "BW3", "SM1"
]

BASIC_ENERGY_NAMES = [
    "Grass Energy", "Fire Energy", "Water Energy", "Lightning Energy",
    "Psychic Energy", "Fighting Energy", "Darkness Energy", "Metal Energy",
    "Fairy Energy", "Basic M Energy", "Basic P Energy"
]

FORMAT_GUID_TO_NAME = {
    DeckFormat.STANDARD.value: "Modified",
    DeckFormat.EXPANDED.value: "Expanded",
    DeckFormat.UNLIMITED.value: "Unlimited",
    DeckFormat.LEGACY.value: "Legacy",
    DeckFormat.THEME.value: "ThemeDeck",
    DeckFormat.TRAINER_CHALLENGE.value: "TrainerChallenge"
}

DEFAULT_VALIDATION_FORMATS = [
    DeckFormat.STANDARD.value,
    DeckFormat.EXPANDED.value,
    DeckFormat.UNLIMITED.value,
    DeckFormat.LEGACY.value,
    DeckFormat.THEME.value,
    DeckFormat.TRAINER_CHALLENGE.value
]


def _validation_results(deck_ids, formats_list):
    """Builds the always-valid DecksValidated result rows for each deck/format pair."""
    return [
        {
            "deckID": deck_id,
            "format": fmt,
            "formatName": FORMAT_GUID_TO_NAME.get(fmt, "Standard"),
            "valid": True,
            "results": []
        }
        for deck_id in deck_ids
        for fmt in formats_list
    ]


def _write_attr(attr, vt, vd, coerce=False):
    """Writes a typed value into a protobuf archetype attribute."""
    obj_type = base_pb2.Object.Type
    if vt == "json":
        attr.value.objectType = obj_type.JSON
        attr.value.stringValue = str(vd) if coerce else vd
    elif vt == "string":
        attr.value.objectType = obj_type.STRING
        attr.value.stringValue = str(vd) if coerce else vd
    elif vt == "int":
        attr.value.objectType = obj_type.INT
        attr.value.intValue = int(vd) if coerce else vd
    elif vt == "float":
        attr.value.objectType = obj_type.FLOAT
        attr.value.floatValue = float(vd) if coerce else vd
    elif vt == "bool":
        attr.value.objectType = obj_type.BOOL
        attr.value.boolValue = bool(vd)


def _card_final_attrs(card_data, key):
    """Cached archetype attrs per card. The NAME attr must stay exactly
    {"id": <token>}: LocalizableTextAnalyzer takes the LAST primitive in the
    JSON object as the loc ID, so any extra key hijacks the display name.
    Search works via the loc override (token -> display_name) -- the pie
    indexer indexes the RESOLVED name, never a raw attribute field."""
    cache_key = (card_data.guid, key)
    attrs = _CARD_ATTRS_CACHE.get(cache_key)
    if attrs is not None:
        return attrs

    attrs = card_data.to_archetype_attributes(key)
    _CARD_ATTRS_CACHE[cache_key] = attrs
    return attrs


class DataSyncHandler(BaseHandler):
    @handle(InboundMsg.ACKNOWLEDGE_NOTIFICATION)
    async def handle_acknowledge_notification(self, message, request_id, flags):
        notification_id = message.get("notificationID")
        logging.info(f"[TCP] [{self.client.addr}] Client acknowledged notification: {notification_id}")

    @handle(InboundMsg.USER_HAS_VISITED_SCENE)
    async def handle_user_has_visited_scene(self, message, request_id, flags):
        scene_name = message.get("sceneName")
        logging.info(f"[TCP] [{self.client.addr}] Client visited scene: {scene_name}")

    @handle(InboundMsg.SET_ACCOUNT_SETTINGS)
    async def handle_set_account_settings(self, message, request_id, flags):
        """Persists client settings (attr 10230). The client's SaveAccountSettings
        blocks until the account's settings attribute version bumps, so echo back
        AccountUpdated (ReplaceWith swaps all attrs) to release it."""

        if not self.client.player:
            return
        account_id = self.client.player.account_id
        settings = message.get("settings") or {}

        await run_db(merge_account_settings, account_id, settings)

        attributes = await run_db(build_account_attributes, account_id)
        await self.send({
            "messageName": OutboundMsg.ACCOUNT_UPDATED.value,
            "account": {
                "username": self.client.player.username,
                "accountID": account_id,
                "attributes": attributes,
            },
        })

    def _to_proto_uuid(self, uuid_obj, proto_uuid):
        """
        Converts a Python UUID object to the Protobuf UUID (lo/hi fixed64).
        Matches PTCGO client's ToGuid: 
        Tag 1 (lo) = Second half of GUID (Big-endian)
        Tag 2 (hi) = First half of GUID (Big-endian)
        """
        b = uuid_obj.bytes
        proto_uuid.lo = int.from_bytes(b[8:16], 'big')
        proto_uuid.hi = int.from_bytes(b[0:8], 'big')

    @handle(InboundMsg.GET_ARCHETYPE_CORRECTIONS)
    async def handle_get_archetype_corrections(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Archetype Corrections.")
        res = {"messageName": OutboundMsg.ARCHETYPE_CORRECTIONS.value, "corrections": []}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.CAKE_REQUEST_WEEKLY_LEADERBOARD_REWARDS)
    async def handle_cake_leaderboard_rewards(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Weekly Leaderboard Rewards.")
        res = {"messageName": OutboundMsg.CAKE_WEEKLY_LEADERBOARD_REWARDS.value, "rewards": []}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_ALL_BANNED_CARDS_BY_FORMATS)
    async def handle_get_all_banned_cards_by_formats(self, message, request_id, flags):
        res = {"messageName": OutboundMsg.ALL_BANNED_CARDS_BY_FORMAT.value,
               "cards": {}}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.VIEW_MY_LOTS)
    async def handle_view_my_lots(self, message, request_id, flags):
        c_res = {"messageName": OutboundMsg.MY_LOTS_RETRIEVED_COUNT.value,
                 "count": 0}
        await self.client.send_packet(c_res, request_id, flags=WargFlags.CLEAR)
        l_res = {"messageName": OutboundMsg.MY_LOTS_RETRIEVED.value,
                 "lots": [], "offers": []}
        await self.client.send_packet(l_res, 0, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_TIME_LOCKED_ARCHETYPES)
    async def handle_get_time_locked_archetypes(self, message, request_id, flags):
        res = {
            "messageName": OutboundMsg.TIME_LOCKED_ARCHETYPES.value,
            "currentServerTime": int(time.time()),
            "timeLockedArchetypes": {}
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_MOTD)
    async def handle_get_motd(self, message, request_id, flags):
        res = {
            "messageName": OutboundMsg.MOTD.value,
            "id": 1,
            "title": {"token": "SpiritPTCGO", "bundle": {}},
            "text": {"token": "Welcome to the Spirit PTCGO Private Server!", "bundle": {}}
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @staticmethod
    def _build_family_map():
        # Default family 0 MUST exist to prevent KeyNotFoundException (idk why)
        family_map = {
            "0": json.dumps({"id": "ids_family_none"})
        }
        for card in CARDS_DB:
            if not isinstance(card, PokemonCard):
                continue
            family_id = card.get_attribute_value(AttrID.FAMILY_ID)
            if family_id and family_id > 0:
                fid_str = str(family_id)
                if fid_str not in family_map:
                    # The value must be a JSON string of a LocalizableText object
                    name_token = card.get_attribute_value(AttrID.NAME)
                    if isinstance(name_token, str) and name_token.startswith('{'):
                        family_map[fid_str] = name_token
                    else:
                        family_map[fid_str] = json.dumps({"id": str(name_token)})
        return family_map

    @handle(InboundMsg.GET_POKEMON_FAMILY_MAP)
    async def handle_get_pokemon_family_map(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Pokemon Family Map.")
        family_map = _cached_payload("family_map", self._build_family_map)
        res = {
            "messageName": OutboundMsg.POKEMON_FAMILY_MAP.value,
            "pokemonFamilyMap": family_map
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.SET_CLIENT_SETTING)
    async def handle_set_client_setting(self, message, request_id, flags):
        key, val = message.get("key"), message.get("value")
        res = {"messageName": OutboundMsg.CLIENT_SETTING_SET.value, "key": key, "value": val}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_GUID_OVERRIDE)
    async def handle_get_guid_override(self, message, request_id, flags):
        res = {"messageName": OutboundMsg.NO_GUID_OVERRIDE.value}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_COLLECTION_COUNT)
    async def handle_get_collection_count(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Collection Count. Msg: {message}")

        cl = await run_db(get_merged_collection_payload, self.client.player.account_id) if self.client.player else []

        logging.info(f"[TCP] [{self.client.addr}] Sending {len(cl)} collection counts.")

        res = {"messageName": OutboundMsg.COLLECTION_COUNT_FOUND.value,
               "collectionCountList": cl}

        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_FEATURE_STATUSES_V2)
    async def handle_get_feature_statuses_v2(self, message, request_id, flags):
        # LEADERBOARDS stays closed: enabling it makes the client request the
        # unimplemented Cake weekly-leaderboard messages on every Refresh.
        features = [
            FeatureToken.TOURNAMENT_FEATURE,
            FeatureToken.CHAT_ENABLED,
            FeatureToken.CODES_ENABLED,
            FeatureToken.EXCHANGE_FEATURE,
            FeatureToken.COMMERCE_FEATURE,
            FeatureToken.GENERIC_FEATURE,
            FeatureToken.SOCIAL_FEATURE,
            FeatureToken.DECK_BUILDER_FEATURE,
            FeatureToken.STORE_GENERIC_FEATURE,
            FeatureToken.PROGRESSION_FEATURE,
            FeatureToken.MATCH_FEATURE,
            FeatureToken.DRAFT_FEATURE,
            FeatureToken.PROFILE_FEATURE,
        ]

        open_features = []
        for feat in features:
            open_features.append({
                "featureName": feat,
                "downMsg": "",
                "treatment": "on"
            })

        res = {
            "messageName": OutboundMsg.ALL_FEATURE_STATUSES_V2.value,
            "service": "core",
            "open": open_features,
            "closed": []
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_ARCHETYPE_FLAGS)
    async def handle_get_archetype_flags(self, message, request_id, flags):
        account_id = self.client.player.account_id if self.client.player else None
        archetype_flags = []
        if account_id:
            archetype_flags = await run_db(get_archetype_flags, account_id)

        res = {"messageName": OutboundMsg.ARCHETYPE_FLAGS_SET.value,
               "archetypeFlags": archetype_flags}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_DYNAMIC_PAGES)
    async def handle_get_dynamic_pages(self, message, request_id, flags):
        # Landing pages and maintenance banners are stored in the DB and
        # edited live through the Admin Dashboard (/admin -> Dynamic Pages).
        pages = []
        maintenance = []
        try:
            for row in await run_db(list_dynamic_pages, enabled_only=True):
                content = dict(row.get("content_json") or {})
                content.setdefault("sortOrder", row.get("sort_order", 0))
                if row.get("page_type") == "maintenance":
                    maintenance.append(content)
                else:
                    pages.append(content)
            pages.sort(key=lambda p: p.get("sortOrder", 0))
        except Exception as e:
            logging.error(f"[TCP] Failed to load dynamic pages from DB: {e}")

        res = {
            "messageName": OutboundMsg.DYNAMIC_LANDING_PAGES.value,
            "pageData": pages,
            "maintenanceData": maintenance
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_DYNAMIC_VERSIONS)
    async def handle_get_dynamic_versions(self, message, request_id, flags):
        v = {
            "major": "1", "minor": "0", "major_version_number": "1",
            "minor_version_number": "0", "content_data_version": "1",
            "content_data_version_id": "0", "cachedDisplayVersion": "1.0.0",
            "cachedCollectionVersion": "1.0.0", "androidpatchversion": "1.0.0",
            "iospatchversion": "1.0.0", "lastUpdatedAtVersion": "1.0.0",
            "opponentsDataVersion": "1.0.0", "progressionDataVersion": "1.0.0",
            "cachedDarkenDataVersion": "1.0.0",
            "LatestMacPatcherVersion": "1.0.0",
            "LatestWindowsPatcherVersion": "1.0.0",
            "LatestMacClientVersion": "1.0.0",
            "LatestWindowsClientVersion": "1.0.0",
            # Read (unguarded) by the client's VersionLabel.Start() for the
            # in-game Settings "Server" version label. Absent keys throw a
            # KeyNotFoundException in the client the moment Settings is opened.
            "ArchetypeContentType": "1.0.0",
            "LocalizationContentType": "1.0.0"
        }
        res = {"messageName": OutboundMsg.DYNAMIC_VERSIONS.value,
               "versionData": v}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_PROTOBUF_ALL_AVATAR_ARCHETYPES_LIST)
    async def handle_get_protobuf_all_avatar_archetypes_list(self, msg, rid, flags):
        proto = cake_item_pb2.AllAvatarArchetypesFound()
        proto.checksum = f"spirit_avatars_{int(time.time() / 3600)}"
        
        # Load real items dynamically from the separate avatar model
        real_items = get_avatar_items()
        
        # 1. Register all real items
        for base_name, item in real_items.items():
            avatar = AvatarArchetype(
                guid=item["guid"],
                gender=item["gender"],
                group=item["group"],
                base_name=base_name,
                style_hash=item.get("style_hash", 0),
                is_dummy=False
            )
            avatar.to_proto(proto.archetypes, self._to_proto_uuid)
            
        # 2. Register dummy items for all 16 groups (ALWAYS register them to ensure fallback IDs are valid archetypes and prevent NullReferenceException)
        for g_idx in range(16):
            guid_str = f"00000000-0000-0000-0000-000000000a{g_idx:02x}"
            dummy_id = "dummy_avatar_item_15xffe0bd" if g_idx == 15 else "EmptyAvatarItem"

            dummy_avatar = AvatarArchetype(
                guid=guid_str,
                gender=1, # Male
                group=g_idx,
                base_name=dummy_id,
                style_hash=1000 + g_idx,
                is_dummy=True
            )
            dummy_avatar.to_proto(proto.archetypes, self._to_proto_uuid)
            
        await self.client.send_packet(proto, rid, flags=WargFlags.PROTOBUF)


    @handle(InboundMsg.GET_PROTOBUF_ARCHETYPES_LIST)
    async def handle_get_protobuf_archetypes_list(self, message, request_id, flags):
        key = message.get("key", "unknown")
        proto = collection_pb2.ArchetypesFound()
        proto.key = key
        # Industry Hack: Use a dynamic checksum to force the client to reload archetypes
        proto.checksum = f"spirit_{key}_{int(time.time() / 3600)}"
        count = 0

        for card_data in CARDS_BY_KEY.get(key, ()):
            guid = card_data.guid
            if guid in self.client.sent_archetypes:
                continue

            arch = proto.archetypes.add()
            self._to_proto_uuid(uuid.UUID(guid), arch.guid)
            self.client.sent_archetypes.add(guid)

            for aid_str, aval in _card_final_attrs(card_data, key).items():
                attr = arch.attributes.add()
                attr.name = int(aid_str)
                _write_attr(attr, aval.get("type"), aval.get("value"))
            count += 1

        p_count = 0
        for p_data in PRODUCTS_DB:
            # Match by set key or product type for cosmetics categories requested by the client
            ptype_val = p_data.get("attributes", {}).get(str(AttrID.PRODUCT_TYPE.value), {}).get("value")
            is_match = False
            if p_data["key"] == key:
                is_match = True
            elif key == "cardSleeves" and ptype_val == ProductType.SLEEVE.value:
                is_match = True
            elif key == "coins" and ptype_val == ProductType.COINS.value:
                is_match = True
            elif key == "deckBoxes" and ptype_val == ProductType.DECK_BOX.value:
                is_match = True

            if is_match:
                guid = p_data["guid"]
                if guid in self.client.sent_archetypes:
                    continue

                arch = proto.archetypes.add()
                self._to_proto_uuid(uuid.UUID(guid), arch.guid)
                self.client.sent_archetypes.add(guid)

                # Ensure we have a fresh copy of attributes to modify if needed
                attrs = dict(p_data.get("attributes", {}))
                
                # Mandatory fields that MUST match the requested set key for client indexing
                attrs[str(AttrID.SET_CACHE_KEY.value)] = {"type": "string", "value": key}
                attrs[str(AttrID.EXPANSION.value)] = {"type": "string", "value": key}

                for aid_str, aval in attrs.items():
                    attr = arch.attributes.add()
                    attr.name = int(aid_str)
                    _write_attr(attr, aval.get("type"), aval.get("value"), coerce=True)
                count += 1
                p_count += 1

        if p_count > 0:
            logging.info(f"[TCP] Included {p_count} products for key: {key}")

        logging.info(f"[TCP] Sent {count} archetypes for key: {key}")
        await self.client.send_packet(proto, request_id, flags=WargFlags.PROTOBUF)

    @handle(InboundMsg.GET_WALLET)
    async def handle_get_wallet(self, message, request_id, flags):
        if self.client.player and self.client.player.wallet:
            w_data = self.client.player.get_wallet_data()
            w_data["messageName"] = OutboundMsg.CURRENT_WALLET.value
            await self.client.send_packet(w_data, request_id, flags=WargFlags.CLEAR)
        else:
            currs = [
                {"name": AttrID.TRAINER_TOKENS.value, "value": 0},
                {"name": AttrID.GEMS.value, "value": 0},
                {"name": AttrID.EVENT_TICKETS.value, "value": 0}
            ]
            res = {"messageName": OutboundMsg.CURRENT_WALLET.value,
                   "currencies": currs}
            await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_DECK_LIST)
    async def handle_get_deck_list(self, message, request_id, flags):
        res = {"messageName": OutboundMsg.DECK_LIST.value, "decks": []}
        if self.client.player:
            res = self.client.player.get_decks_data()
            res["messageName"] = OutboundMsg.DECK_LIST.value
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_AVATAR_DECK_LIST)
    async def handle_get_avatar_deck_list(self, message, request_id, flags):
        res = {"messageName": OutboundMsg.AVATAR_DECK_LIST.value, "decks": []}
        if self.client.player:
            res = self.client.player.get_avatar_decks_data()
            res["messageName"] = OutboundMsg.AVATAR_DECK_LIST.value
            
            # If no avatar decks are defined, provide a default mock avatar deck
            # that links to our dummy items to avoid client-side NullReferenceException,
            # assign a unique guid, and save it to the player's database profile.
            if not res.get("decks"):
                deck_id = str(uuid.uuid4())
                default_avatar_deck = {
                    "deckID": deck_id,
                    "deckName": "Default Avatar",
                    "piles": {
                        "AvatarItems": get_default_avatar_items_list()
                    },
                    "attributes": [
                        {
                            "name": AttrID.VALID_FORMATS.value,
                            "value": ["Modified", "Expanded", "Unlimited", "Legacy"]
                        },
                        {
                            "name": 201310, # active selected avatar deck
                            "value": True
                        },
                        {
                            "name": 201300, # save as default
                            "value": True
                        }
                    ]
                }
                if hasattr(self.client.player, "save_deck_data"):
                    def _save_and_refetch(player=self.client.player):
                        player.save_deck_data(default_avatar_deck, is_avatar=True)
                        return player.get_avatar_decks_data()
                    res = await run_db(_save_and_refetch)
                    res["messageName"] = OutboundMsg.AVATAR_DECK_LIST.value
                else:
                    res["decks"] = [default_avatar_deck]
                
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.CAKE_SAVE_DECK)
    async def handle_cake_save_deck(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested to save deck.")
        
        deck_dict = message.get("deck")
        if not deck_dict:
            logging.warning("[TCP] SaveDeck payload missing 'deck' object.")
            return

        deck_id = deck_dict.get("deckID")
        deck_name = deck_dict.get("deckName", "")

        if not deck_id or deck_id == '00000000-0000-0000-0000-000000000000': # Indicates that a new deck is being created
            deck_id = str(uuid.uuid4())
            deck_dict["deckID"] = deck_id

        # Ensure basic cosmetics are present in attributes with corrected default GUIDs
        # Note: In PTCGO JSON, 'attributes' maps to ReadOnlyAttributes, which is an IEnumerable collection
        # and therefore must be deserialized as a JSON LIST (array) of attribute dictionaries (e.g. [{"name": X, "value": Y}, ...]).
        # The client originally sends a list of attributes, but we temporarily convert to a dictionary
        # for ease of lookup and cosmetic defaulting, and then serialize it back as a list.
        attrs_list = deck_dict.get("attributes", [])
        attrs_dict = {}
        if isinstance(attrs_list, list):
            for item in attrs_list:
                name = item.get("name")
                if name is not None:
                    attrs_dict[str(name)] = item
        elif isinstance(attrs_list, dict):
            attrs_dict = {str(k): v for k, v in attrs_list.items()}

        # Default Coin
        coin_attr = str(AttrID.SELECTED_COIN.value)
        if coin_attr not in attrs_dict:
            attrs_dict[coin_attr] = {
                "name": AttrID.SELECTED_COIN.value,
                "value": "B9A4EA96-949E-11E1-890F-EFB676C7909C"
            }
        # Default Sleeve
        sleeve_attr = str(AttrID.SELECTED_SLEEVE.value)
        if sleeve_attr not in attrs_dict:
            attrs_dict[sleeve_attr] = {
                "name": AttrID.SELECTED_SLEEVE.value,
                "value": "e079c0d3-b934-4fbd-b021-545106c75693"
            }
        # Default Deck Box
        deckbox_attr = str(AttrID.SELECTED_DECK_BOX.value)
        if deckbox_attr not in attrs_dict:
            attrs_dict[deckbox_attr] = {
                "name": AttrID.SELECTED_DECK_BOX.value,
                "value": "e129b0d3-b934-4fbd-b021-545106c75694"
            }

        # Normalize attributes back to a list of dictionaries for JSON-compatibility
        deck_dict["attributes"] = list(attrs_dict.values())

        # Save deck using the player model
        if self.client.player:
            piles = deck_dict.get("piles", {}) or {}
            cards = deck_dict.get("cards", {}) or {}
            is_avatar = ("AvatarItems" in piles) or ("AvatarItems" in cards)
            await run_db(self.client.player.save_deck_data, deck_dict, is_avatar=is_avatar)
            logging.info(f"[TCP] [{self.client.addr}] Saved deck '{deck_name}' ({deck_id}) (is_avatar={is_avatar}) successfully.")

        # Validation results satisfy client-side deck legality checks
        validation_results = _validation_results([deck_id], [
            DeckFormat.STANDARD.value,
            DeckFormat.EXPANDED.value,
            DeckFormat.UNLIMITED.value
        ])

        res = {
            "messageName": OutboundMsg.DECK_SAVED.value,
            "deckID": deck_id,
            "deck": deck_dict,
            "validationResults": validation_results
        }

        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.CAKE_DELETE_DECK)
    async def handle_cake_delete_deck(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested to delete deck.")
        
        deck_id = message.get("deckID") or message.get("deckId") or message.get("DeckID")
        if not deck_id:
            logging.warning("[TCP] DeleteDeck payload missing 'deckID' or 'DeckID'.")
            return

        if self.client.player:
            is_avatar = False
            avatar_decks = getattr(self.client.player, "avatar_decks", [])
            for deck in avatar_decks:
                if deck.get("id") == deck_id or deck.get("deck_id") == deck_id:
                    is_avatar = True
                    break
            await run_db(self.client.player.delete_deck_data, deck_id, is_avatar=is_avatar)
            logging.info(f"[TCP] [{self.client.addr}] Deleted deck {deck_id} (is_avatar={is_avatar}) successfully.")

        res = {
            "messageName": OutboundMsg.DECK_DELETED.value,
            "deckID": deck_id
        }

        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.VALIDATE_DECKS)
    async def handle_validate_decks(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested validation of specific decks.")
        
        decks_list = message.get("decks", [])
        formats_list = message.get("formats", []) or DEFAULT_VALIDATION_FORMATS

        # TODO(brandon): Actually validate decks using rule logic
        deck_ids = [d.get("deckID") or d.get("DeckID") for d in decks_list]
        results = _validation_results([did for did in deck_ids if did], formats_list)

        res = {
            "messageName": OutboundMsg.DECKS_VALIDATED.value,
            "results": results
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.VALIDATE_ALL_DECKS)
    async def handle_validate_all_decks(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested validation of all decks.")
        
        formats_list = message.get("formats", []) or DEFAULT_VALIDATION_FORMATS

        results = []
        if self.client.player:
            deck_ids = [d.get("id") for d in self.client.player.decks if d.get("id")]
            results = _validation_results(deck_ids, formats_list)

        res = {
            "messageName": OutboundMsg.DECKS_VALIDATED.value,
            "results": results
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_PROTOBUF_SCENARIOS)
    async def handle_get_protobuf_scenarios(self, message, request_id, flags):
        sc_proto = progression_pb2.AllScenarios()
        leagues = [("ids_league_gold", 1), ("ids_league_platinum", 2),
                   ("ids_league_city", 3)]
        for token, lid in leagues:
            scenario = progression_pb2.Scenario()
            u_obj = uuid.UUID(bytes=hashlib.md5(token.encode()).digest())
            self._to_proto_uuid(u_obj, scenario.scenarioID)
            a_list = [
                (AttrID.SCENARIO_LEAGUE_ID, base_pb2.Object.Type.INT, lid),
                (AttrID.NAME, base_pb2.Object.Type.JSON, json.dumps({"id": token})),
                (AttrID.SCENARIO_DESCRIPTION, base_pb2.Object.Type.JSON,
                 json.dumps({"id": token + "_desc"})),
                (AttrID.SCENARIO_IMAGE, base_pb2.Object.Type.JSON,
                 json.dumps({"id": ""})),
                (201470, base_pb2.Object.Type.JSON, "{}"),
                (201500, base_pb2.Object.Type.JSON, "{}"),
                (202260, base_pb2.Object.Type.JSON, "{}"),
                (201700, base_pb2.Object.Type.JSON, "[]"),
                (202270, base_pb2.Object.Type.JSON, "[]")
            ]
            for aid, ot, val in a_list:
                attr = scenario.attributes.add()
                attr.name = int(aid)
                attr.value.objectType = ot
                if ot == base_pb2.Object.Type.INT:
                    attr.value.intValue = val
                else:
                    attr.value.stringValue = val
            sc_proto.available.append(scenario)
            sc_proto.roots.append(scenario)
        await self.client.send_packet(sc_proto, request_id, flags=WargFlags.PROTOBUF)

    @handle(InboundMsg.GET_NOTIFICATIONS)
    async def handle_get_notifications(self, message, request_id, flags):
        if not self.client.player:
            return

        invites = await run_db(get_incoming_invites_by_account_id, self.client.player.account_id)
        notifications = []
        
        for invite in invites:
            # Wrap the inner payload for the client's polymorphic deserializer
            invite_payload = {
                "name": OutboundMsg.FRIEND_INVITATION.value,
                "value": {
                    "friend": {
                        "accountID": invite['friend_id'],
                        "displayName": invite['screen_name']
                    }
                }
            }
            notifications.append({
                "notificationID": str(uuid.uuid4()),
                "payload": json.dumps(invite_payload),
                "notificationType": 0
            })

        res = {"messageName": OutboundMsg.NOTIFICATIONS_REQUESTED.value,
               "notificationList": notifications}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_ACHIEVEMENTS)
    async def handle_get_achievements(self, message, request_id, flags):
        res = {
            "messageName": OutboundMsg.LIST_ACHIEVEMENTS.value,
            "achievements": []
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @staticmethod
    def _build_archetype_keys():
        dynamic_keys = set(ARCHETYPE_KEYS)
        dynamic_keys.update(card.key for card in CARDS_DB)
        dynamic_keys.update(p.get("key") for p in PRODUCTS_DB if isinstance(p.get("key"), str))
        dynamic_keys.update(s.get("name") for s in SETS_DB if isinstance(s.get("name"), str))
        return sorted(k for k in dynamic_keys if k)

    @handle(InboundMsg.GET_ARCHETYPE_LIST_KEYS)
    async def handle_get_archetype_list_keys(self, message, request_id, flags):
        final_keys = _cached_payload("archetype_keys", self._build_archetype_keys)
        logging.info(f"[TCP] [{self.client.addr}] Sending {len(final_keys)} unique archetype keys.")
        res = {"messageName": OutboundMsg.ARCHETYPE_KEYS.value,
               "keys": final_keys}
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @staticmethod
    def _build_family_id_map():
        # EvolutionsRenderUtil map: { family_id: { stage_name (C# enum name): [guids] } }
        family_map = {}
        stage_name_map = {
            0: "Basic", 1: "Stage1", 2: "Stage2",
            3: "Restored", 4: "LevelUp", 5: "Legend",
            6: "Break", 7: "VMAX", 8: "VUNION", 9: "VSTAR"
        }
        for card in CARDS_DB:
            if not isinstance(card, PokemonCard):
                continue
            family_id = card.get_attribute_value(AttrID.FAMILY_ID)
            if family_id and family_id > 0:
                stage_val = card.get_attribute_value(AttrID.STAGE, 0)
                stage_name = stage_name_map.get(stage_val, "Basic")
                guids = family_map.setdefault(str(family_id), {}).setdefault(stage_name, [])
                if card.guid not in guids:
                    guids.append(card.guid)
        return family_map

    @handle(InboundMsg.GET_ARCHETYPE_IDS_BY_FAMILY)
    async def handle_get_archetype_ids_by_family(self, message, request_id, flags):
        family_map = _cached_payload("family_id_map", self._build_family_id_map)
        logging.info(f"[TCP] [{self.client.addr}] Sending {len(family_map)} families in ID map.")
        res = {
            "messageName": OutboundMsg.ARCHETYPE_IDS_BY_FAMILY.value,
            "familyMap": family_map
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @staticmethod
    def _build_format_legality():
        ll = [{"archetypeID": c.guid, "formatLegality": [True]*4,
               "formatLegalityTime": [0]*4} for c in CARDS_DB]
        for i in [2, 3]:
            ll.append({"archetypeID": f"00000000-0000-0000-0000-00000000000{i}",
                       "formatLegality": [True]*4,
                       "formatLegalityTime": [0]*4})
        return ll

    @handle(InboundMsg.GET_FORMAT_LEGALITY_FOR_ARCHETYPES)
    async def handle_get_format_legality_for_archetypes(self, msg, rid, flags):
        res = {"messageName": OutboundMsg.FORMAT_LEGALITY_FOR_ARCHETYPES.value,
               "archLegality": _cached_payload("format_legality", self._build_format_legality)}
        await self.client.send_packet(res, rid, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_ALL_LOCALIZATION_RELEASES)
    async def handle_get_all_localization_releases(self, message, request_id, flags):
        locale = message.get("locale", "en_US")
        if CACHED_LOCALIZATIONS is None:
            await run_db(_load_localizations)

        res = {
            "messageName": OutboundMsg.ALL_LOCALIZATION_RELEASES.value,
            "locale": locale, 
            "version": "spirit_v1", 
            "releases": {}
        }
        
        client_checksums = message.get("keyedChecksums", {})
        server_releases = ["core"]
        current_md5 = "spirit_hash_" + str(len(CACHED_LOCALIZATIONS))
        
        for rk in server_releases:
            if client_checksums.get(rk) != current_md5:
                res["releases"][rk] = {
                    "md5": current_md5,
                    "localizationList": CACHED_LOCALIZATIONS
                }
            
        logging.info(f"[TCP] Sent {len(CACHED_LOCALIZATIONS)} localization strings for {locale}.")
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.GET_SET_DATA)
    async def handle_get_set_data(self, message, request_id, flags):
        # Wrap the authentic set data in ChecksumDiff as seen in the game cache
        # We manually wrap nested objects because send_packet only wraps the top level
        res = {
            "messageName": OutboundMsg.CHECKSUM_DIFF.value,
            "dataType": "GetSetData",
            "ckSumDiff": [
                {
                    "name": "ChecksumDiffInfo",
                    "value": {
                        "groupKey": "all",
                        "ckSum": SETS_CHECKSUM,
                        "newData": {
                            "name": "SetDataList",
                            "value": {
                                "setDataList": SETS_DB
                            }
                        }
                    }
                }
            ]
        }
        await self.client.send_packet(res, request_id, flags=WargFlags.CLEAR)
