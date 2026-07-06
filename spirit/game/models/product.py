import json
import copy
import uuid
import random
import logging
from typing import Any, Optional, Dict, List
from spirit.game.attributes import AttrID, ProductType, CardType, Rarities
import spirit.server.state as state
from spirit.game.scripts.cards import loader as card_loader

SHOP_SKU_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, "spiritptcgo.shop.sku")


def make_shop_sku(product: "Product") -> "Product":
    """A shop-facing alias of a product with its own GUID, so the client's dynamic-archetype
    eviction on shop exit (ClearDynamicArchetypes) never touches the owned collection GUID."""
    sku_guid = str(uuid.uuid5(SHOP_SKU_NAMESPACE, product.guid))
    attrs = copy.deepcopy(product.attributes)
    attrs[str(AttrID.ARCHETYPE_ID.value)] = {"type": "string", "value": sku_guid}
    attrs[str(AttrID.CATALOG_ID.value)] = {"type": "string", "value": sku_guid}
    return Product(sku_guid, product.key, attrs, [dict(p) for p in product.prices])

def safe_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

class Product:
    """Models a single product (Pack, Deck, Coin, etc.) in the server."""
    def __init__(self, guid: str, key: str, attributes: Optional[Dict[str, Any]] = None, prices: Optional[List[Dict[str, Any]]] = None):
        self.guid = guid
        self.key = key
        self.attributes = attributes or {}
        self.prices = prices or []

    def get_attribute_value(self, attr_id: AttrID, default: Any = None) -> Any:
        # Handle both AttrID and int/str
        attr_key = str(attr_id.value if isinstance(attr_id, AttrID) else attr_id)
        attr = self.attributes.get(attr_key)
        if attr:
            val = attr.get("value")
            # If it's a JSON type, it might be a string that needs parsing for some uses,
            # but usually for game logic we want the parsed version.
            if attr.get("type") == "json" and isinstance(val, str):
                try:
                    return json.loads(val)
                except:
                    return val
            return val if val is not None else default
        return default

    @property
    def product_type(self) -> int:
        return safe_int(self.get_attribute_value(AttrID.PRODUCT_TYPE, ProductType.UNSET.value))

    @property
    def name(self) -> str:
        name_data = self.get_attribute_value(AttrID.NAME)
        if isinstance(name_data, dict):
            return name_data.get("id", "")
        return str(name_data or "")

    @property
    def catalog_id(self) -> str:
        return str(self.get_attribute_value(AttrID.CATALOG_ID, ""))

    def to_archetype_dict(self) -> Dict[str, Any]:
        """Formats for ArchetypesFound (Protobuf). Keep wrapped for ProtoMessage."""
        return {
            "guid": self.guid,
            "key": self.key,
            "attributes": self.attributes
        }

    def to_archetype_json(self) -> Dict[str, Any]:
        """Serializes the product to the client's Archetype JSON format (Legacy Shop)."""
        attrs = []
        for name_str, attr_data in self.attributes.items():
            val = attr_data.get("value")
            
            # Shop JSON packets expect JSON attributes to be actual JSON objects/dicts, not strings
            if attr_data.get("type") == "json" and isinstance(val, str):
                try:
                    val = json.loads(val)
                except:
                    pass
            attrs.append({"name": int(name_str), "value": val})

        return {
            "archetypeID": self.guid,
            "attributes": attrs
        }

    def get_price_json(self) -> Dict[str, Any]:
        """Serializes the product's price for the AvailableProducts priceMap."""
        return {
            "name": AttrID.SHOP_PRICE_MAP.value,
            "value": self.prices
        }

    def open(self, account_id: str) -> list[str]:
        """Logic for opening the product. Returns list of Archetype GUIDs."""
        return []

class BoosterPack(Product):
    def __init__(self, guid: str, key: str, attributes: Optional[Dict[str, Any]] = None, prices: Optional[List[Dict[str, Any]]] = None):
        super().__init__(guid, key, attributes, prices)
        # Default card pool for BW1 boosters if not specified
        self.card_pool = [
            "7f4966fd-4082-5e69-1855-fee0e79f0ffa",
            "7167880e-4d58-c350-8cc7-adab87e8c6f7",
            "68975361-b02b-330e-b4e3-98c3b8e4bcda",
            "383f19f1-cb84-085b-63cc-e1d14b062cf6",
            "3202abdb-b395-f0c9-9b15-d10187c68255",
            "b7b3e2a1-385f-1466-7dae-47c081ff4626",
            "8597f163-fb9d-980d-32bc-38edc02852ff",
            "338b9be4-7534-1268-5aa4-2663a605d657",
            "eb6ebb86-4606-d7cb-22c4-196d294d0794",
            "96e32e96-f9b0-5157-21ba-9cd01fd43ff3"
        ]

    def open(self, account_id: str) -> list[str]:
        # Get all cards in the game
        all_cards = card_loader.cards
        
        # 1. Filter cards belonging to this set key (e.g., "SWSH8")
        set_cards = [c for c in all_cards if c.key.lower() == self.key.lower()]
        
        if not set_cards:
            # Fallback to default card pool if the set has no cards loaded
            if not self.card_pool:
                return []
            return random.choices(self.card_pool, k=10)
            
        # Helper to safely extract integer values
        def get_attr_int(c, attr):
            val = c.get_attribute_value(attr)
            if val is None:
                return -1
            try:
                return int(val)
            except:
                return -1

        # 2. Build the target pools
        commons = [
            c.guid for c in set_cards 
            if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value 
            and get_attr_int(c, AttrID.RARITY) == Rarities.Common.value
        ]
        
        uncommons = [
            c.guid for c in set_cards 
            if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value 
            and get_attr_int(c, AttrID.RARITY) == Rarities.Uncommon.value
        ]
        
        rares = [
            c.guid for c in set_cards 
            if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value 
            and get_attr_int(c, AttrID.RARITY) >= Rarities.Rare.value
        ]
        
        # Basic energies in this set
        basic_energies = [
            c.guid for c in set_cards 
            if get_attr_int(c, AttrID.CARD_TYPE) == CardType.ENERGY.value 
            and not c.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)
        ]
        
        # If set has no basic energies, find them in Free_Energy
        if not basic_energies:
            basic_energies = [
                c.guid for c in all_cards 
                if c.key.lower() == "free_energy" 
                and get_attr_int(c, AttrID.CARD_TYPE) == CardType.ENERGY.value 
                and not c.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)
            ]
            
        # Reverse holos can be any card from this set (excluding Energy)
        reverse_holos = [
            c.guid for c in set_cards 
            if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value
        ]
        
        # Fallback mappings in case a specific pool is empty due to incomplete script loads
        fallback_set_guids = [c.guid for c in set_cards]
        commons_pool = commons if commons else fallback_set_guids
        uncommons_pool = uncommons if uncommons else fallback_set_guids
        rares_pool = rares if rares else fallback_set_guids
        energy_pool = basic_energies if basic_energies else fallback_set_guids
        rev_holo_pool = reverse_holos if reverse_holos else fallback_set_guids
        
        # 3. Assemble the pack (10 cards ordered from common up to rare)
        pack_guids = []
        
        # 4 Commons
        pack_guids.extend(random.choices(commons_pool, k=4))
        
        # 3 Uncommons
        pack_guids.extend(random.choices(uncommons_pool, k=3))
        
        # 1 Basic Energy
        pack_guids.extend(random.choices(energy_pool, k=1))
        
        # 1 Reverse Holo
        pack_guids.extend(random.choices(rev_holo_pool, k=1))
        
        # 1 Rare / Hit
        pack_guids.extend(random.choices(rares_pool, k=1))
        
        return pack_guids

class Deck(Product):
    def __init__(self, guid: str, key: str, attributes: Optional[Dict[str, Any]] = None, prices: Optional[List[Dict[str, Any]]] = None):
        super().__init__(guid, key, attributes, prices)
        self.contents = [] # List of GUIDs

    def open(self, account_id: str) -> list[str]:
        return self.contents
