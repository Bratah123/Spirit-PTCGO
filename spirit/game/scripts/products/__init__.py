import os
import json
import uuid
import importlib.util
import logging
from typing import Dict, List
from spirit.game.models.product import Product, BoosterPack, Deck
from spirit.game.attributes import ProductType, AttrID, CardType, Rarities
from spirit.game.set_utils import eligible_booster_sets
from spirit.game.scripts.cards import loader as card_loader

BOOSTER_GUID_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, "spiritptcgo.auto.boosters")

# Pack art lives here; the client loads it from the "packs" bundle keyed by the PNG basename.
PACK_ART_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..', 'assets', 'products', 'custom_packs'))
GENERIC_PACK_IMAGE = "booster_generic"


def resolve_pack_image(set_code):
    """Bundle-asset name for a set's booster art. Must equal the PNG basename or the client
    requests a missing asset and shows the loading-hourglass placeholder."""
    base = f"{set_code.lower()}_booster"
    try:
        pngs = [f for f in os.listdir(PACK_ART_DIR) if f.lower().endswith('.png')]
    except OSError:
        pngs = []
    lower = {f.lower() for f in pngs}
    if f"{base}.png" in lower:
        return base
    for f in sorted(pngs):
        if f.lower().startswith(base):  # {set}_booster_{name}.png
            return os.path.splitext(f)[0].lower()
    return GENERIC_PACK_IMAGE if f"{GENERIC_PACK_IMAGE}.png" in lower else base

class ProductLoader:
    """Dynamically loads product definition scripts from the filesystem."""
    def __init__(self, scripts_dir: str):
        self.scripts_dir = os.path.abspath(scripts_dir)
        self.products: List[Product] = []
        self.products_by_guid: Dict[str, Product] = {}
        self.products_by_key: Dict[str, Product] = {}

    def load_all(self):
        """Scans the directory and loads all .py scripts."""
        self.products = []
        self.products_by_guid = {}
        self.products_by_key = {}
        
        logging.info(f"[Scripts] Loading product scripts from {self.scripts_dir}...")
        
        for root, _, files in os.walk(self.scripts_dir):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    file_path = os.path.join(root, file)
                    self._load_script(file_path)

        self._append_auto_boosters()
        self._attach_pack_preview_cards()

        logging.info(f"[Scripts] Successfully loaded {len(self.products)} product scripts.")
        return self.products

    def _attach_pack_preview_cards(self):
        """Gives each pack attr 201505 (up to 3 loaded set cards, rarest first) so the "i" popup
        marquee uses the cache-safe GetArchetype filter instead of the crashing set-featured path."""

        # Read already-loaded cards only; never reload here (card_loader.load_all rebuilds the
        # global effect registries, which would corrupt any in-flight game state).
        cards = getattr(card_loader, "cards", None) or []
        by_key: Dict[str, list] = {}
        for c in cards:
            ct = c.get_attribute_value(AttrID.CARD_TYPE)
            if ct == CardType.ENERGY.value:
                continue
            by_key.setdefault(c.key.lower(), []).append(c)

        def rarity_of(card):
            val = card.get_attribute_value(AttrID.RARITY)
            try:
                return int(val)
            except (TypeError, ValueError):
                return -1

        for p in self.products:
            if p.product_type != ProductType.PACKS.value:
                continue
            pool = sorted(by_key.get(p.key.lower(), []), key=rarity_of, reverse=True)
            preview, seen = [], set()
            for c in pool:
                if c.guid in seen:
                    continue
                seen.add(c.guid)
                preview.append(c.guid)
                if len(preview) == 3:
                    break
            if preview:
                p.attributes[str(AttrID.PACK_PREVIEW_CARDS.value)] = {
                    "type": "json", "value": json.dumps(preview)
                }

    def _append_auto_boosters(self):
        """Registers a booster pack product for every card set with >10 scripts that lacks one."""
        from spirit.game.data_utils import BoosterPackDef

        existing_pack_keys = {
            p.key.upper() for p in self.products
            if p.product_type == ProductType.PACKS.value
        }
        for set_code in eligible_booster_sets():
            if set_code.upper() in existing_pack_keys:
                continue
            pack_def = BoosterPackDef(
                guid=str(uuid.uuid5(BOOSTER_GUID_NAMESPACE, set_code.upper())),
                key=set_code,
                name=f"product.{set_code.lower()}.booster",
                image_url=resolve_pack_image(set_code)
            )
            archetype = pack_def.to_archetype_dict()
            prod_obj = BoosterPack(archetype["guid"], archetype["key"], archetype["attributes"])
            self.products.append(prod_obj)
            self.products_by_guid[prod_obj.guid] = prod_obj
            self.products_by_key[prod_obj.key] = prod_obj

    def _load_script(self, file_path: str):
        """Loads a single product script."""
        try:
            rel_path = os.path.relpath(file_path, self.scripts_dir)
            module_name = "product_script_" + rel_path.replace(os.path.sep, "_").replace(".py", "")
            
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                return

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'product'):
                prod_def = module.product
                archetype = prod_def.to_archetype_dict()
                guid = archetype["guid"]
                key = archetype["key"]
                attrs = archetype["attributes"]
                
                ptype = attrs.get(str(AttrID.PRODUCT_TYPE.value), {}).get("value", ProductType.UNSET.value)
                
                if ptype == ProductType.PACKS:
                    prod_obj = BoosterPack(guid, key, attrs)
                elif ptype == ProductType.DECKS:
                    prod_obj = Deck(guid, key, attrs)
                else:
                    prod_obj = Product(guid, key, attrs)
                
                self.products.append(prod_obj)
                self.products_by_guid[guid] = prod_obj
                self.products_by_key[key] = prod_obj
                
        except Exception as e:
            logging.error(f"[Scripts] Failed to load product script {file_path}: {e}")

# Global loader instance
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__))
loader = ProductLoader(SCRIPTS_DIR)
