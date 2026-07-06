import json
import logging
from spirit import config
from spirit.game.models.shop import Shop, FeaturedProduct
from spirit.game.models.product import Product
from spirit.game.attributes import AttrID, ProductType
from spirit.game.set_utils import eligible_booster_sets
from spirit.game.scripts.products import loader as product_loader
from spirit.database.economy_data import list_shop_items
from spirit.game.scripts.cards import loader as card_loader

DEFAULT_BOOSTER_PRICE = 200
LOCAL_IMG = config.PLACEHOLDER_IMG


class ShopManager:
    """Manages the global state of the Shop."""
    def __init__(self):
        self.shop = Shop()
        self.reload_from_db()

    def _add_tokens_product(self):
        cur_guid = "00000000-0000-0000-0000-000000000002"
        cur_attrs = {
            str(AttrID.NAME.value): {"type": "json", "value": json.dumps({"id": "ids_item_token"})},
            str(AttrID.EXPANSION.value): {"type": "string", "value": "core"},
            str(AttrID.PRODUCT_TYPE.value): {"type": "int", "value": 6},  # ProductType.CURRENCY
            str(AttrID.CURRENCY_TYPE.value): {"type": "int", "value": -706482148},  # CurrencyType.VIRTUAL_CURRENCY
            str(AttrID.ARCHETYPE_ID.value): {"type": "string", "value": cur_guid},
            str(AttrID.IMAGE_URL.value): {"type": "string", "value": LOCAL_IMG},
            str(AttrID.CATALOG_ID.value): {"type": "string", "value": cur_guid},
            str(AttrID.SET_CACHE_KEY.value): {"type": "string", "value": "core"},
            str(AttrID.SET_NUMBER.value): {"type": "int", "value": 100}
        }
        cur_prices = [{"name": AttrID.TRAINER_TOKENS.value, "value": 0}]
        self.shop.add_product(Product(cur_guid, "core", cur_attrs, cur_prices))

    def _feature(self, product):
        img_url = product.get_attribute_value(AttrID.IMAGE_URL, LOCAL_IMG)
        self.shop.featured_products.append(FeaturedProduct(product.guid, img_url))

    def reload_from_db(self):
        logging.info("[Shop] Reloading shop from database...")
        self.shop.clear()

        try:
            self._add_tokens_product()

            # Ensure cards are loaded before building products so packs get preview cards (attr
            # 201505). Guarded: never reload once loaded (that rebuilds effect registries).
            if not getattr(card_loader, "cards", None):
                card_loader.load_all()

            products = product_loader.load_all()

            # Admin-configured shop items override/extend the automatic listing
            try:
                shop_items = list_shop_items()
            except Exception as e:
                logging.warning(f"[Shop] Could not load shop items from DB ({e}); using automatic listing only.")
                shop_items = []
            items_by_guid = {i["product_guid"].lower(): i for i in shop_items}

            # 1. Automatic booster offerings: every set with >10 scripted cards
            eligible = {code.upper() for code in eligible_booster_sets()}
            for product in products:
                if product.product_type != ProductType.PACKS.value:
                    continue
                if product.key.upper() not in eligible:
                    continue
                if product.guid.lower() in items_by_guid:
                    continue  # admin row takes precedence
                product.prices = [{"name": AttrID.TRAINER_TOKENS.value, "value": DEFAULT_BOOSTER_PRICE}]
                sku = self.shop.add_as_sku(product)  # listed under a SKU GUID so the owned pack survives shop exit
                self.shop.top_selling_products.append(sku.guid)

            # 2. Admin-configured items (enabled only; disabled rows suppress auto listing)
            for item in shop_items:
                if not item["enabled"]:
                    continue
                product = product_loader.products_by_guid.get(item["product_guid"]) or \
                    product_loader.products_by_guid.get(item["product_guid"].lower())
                if not product:
                    logging.warning(f"[Shop] Shop item references unknown product {item['product_guid']}")
                    continue
                product.prices = [{"name": item["currency"], "value": item["price"]}]
                listed = self.shop.add_as_sku(product) \
                    if product.product_type == ProductType.PACKS.value else product
                if listed is product:
                    self.shop.add_product(product)
                if item["featured"]:
                    self._feature(listed)
                if item["top_selling"] and listed.guid not in self.shop.top_selling_products:
                    self.shop.top_selling_products.insert(0, listed.guid)

            # Always feature something so the shop landing isn't empty
            if not self.shop.featured_products and self.shop.top_selling_products:
                first = self.shop.available_products.get(self.shop.top_selling_products[0])
                if first:
                    self._feature(first)

            logging.info(f"[Shop] Loaded {len(self.shop.available_products)} products "
                         f"({len(self.shop.featured_products)} featured).")
        except Exception as e:
            logging.error(f"[Shop] Failed to reload shop: {e}", exc_info=True)

    def get_shop(self) -> Shop:
        return self.shop


# Global instance
shop_manager = ShopManager()
