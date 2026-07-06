import logging
import uuid
import time

from spirit import config
from spirit.network.message_names import InboundMsg, OutboundMsg
from .base import BaseHandler, handle
from spirit.shop import shop_manager
from spirit.game.scripts.products import loader as product_loader
from spirit.game.attributes import AttrID
from spirit.database import db_session, Collection
from spirit.database.async_utils import run_db
from spirit.database.player_data import add_to_collection, remove_from_collection

def build_item(owner_id: str, archetype_id: str, is_tradable: bool = False) -> dict:
    """Builds the client's Item JSON shape (shared with the trade lots protocol)."""
    return {
        "itemID": str(uuid.uuid4()),
        "ownerID": owner_id,
        "archetypeID": archetype_id,
        "lockID": None,
        "created": int(time.time()),
        "isTradable": is_tradable,
        "name": "",
        "invoiceID": None,
        "attributes": []
    }

class ShopHandler(BaseHandler):
    def _owner_id(self) -> str:
        return self.client.player.account_id if self.client.player else "0"

    def _open_products_sync(self, product_ids, is_tradable_override):
        """Opens products and persists collection changes; runs on a DB worker thread."""
        shop = shop_manager.get_shop()
        account_id = self.client.player.account_id if self.client.player else None
        owner_id = account_id or "0"

        opened_items = []
        opened_products = []

        for p_id in product_ids:
            # p_id may be a shop SKU GUID (buy+open) or a real owned pack GUID (open from collection)
            pack_guid = shop.resolve_product_guid(p_id)
            product = product_loader.products_by_guid.get(pack_guid) or \
                product_loader.products_by_guid.get(pack_guid.lower())
            if not product:
                logging.warning(f"[Shop] Cannot open unknown product: {p_id}")
                continue

            # 1. Determine if the opened product is tradable
            is_tradable_pack = True
            if account_id:
                with db_session() as session:
                    item = session.query(Collection).filter_by(
                        account_id=account_id,
                        archetype_id=pack_guid
                    ).first()
                    if item:
                        if item.nontradable_count > 0:
                            is_tradable_pack = False
                        elif item.tradable_count > 0:
                            is_tradable_pack = True

            if is_tradable_override is not None:
                is_tradable_pack = bool(is_tradable_override)

            opened_products.append(build_item(owner_id, pack_guid, is_tradable=is_tradable_pack))

            # Consume the product from collection
            if account_id:
                remove_from_collection(account_id, pack_guid, count=1, is_tradable=is_tradable_pack)

            # Generate cards for this product
            generated_guids = product.open("-1")
            for g in generated_guids:
                opened_items.append(build_item(owner_id, g, is_tradable=is_tradable_pack))
                if account_id:
                    add_to_collection(account_id, g, count=1, is_tradable=is_tradable_pack)

        return opened_items, opened_products

    async def _process_opening(self, request_id, flags, product_ids, is_tradable_override=None):
        opened_items, opened_products = await run_db(
            self._open_products_sync, product_ids, is_tradable_override)

        response = {
            "messageName": OutboundMsg.PRODUCTS_OPENED.value,
            "accountID": self._owner_id(),
            "items": opened_items,
            "products": opened_products,
            "additionalData": {}
        }
        await self.send(response, request_id)

        # Sync collection count after opening (unsolicited sync uses request_id=0)
        if self.client.player:
            await self.push_collection()

    @staticmethod
    def _price_total(products_with_qty):
        """Sums each product's first listed price; returns (total, currency)."""
        total = 0
        currency = None
        for product, qty in products_with_qty:
            if product and product.prices:
                price = product.prices[0]
                total += price.get("value", 0) * qty
                currency = price.get("name")
        return total, currency

    async def _charge_for(self, products_with_qty, context: str) -> bool:
        """Deducts the summed price from the player wallet; False = insufficient funds."""
        total_cost, used_currency = self._price_total(products_with_qty)
        if self.client.player and used_currency is not None and total_cost > 0:
            if not await run_db(self.client.player.wallet.deduct_currency, used_currency, total_cost):
                logging.warning(f"[Shop] Player {self.client.player.username} has insufficient funds for {context}.")
                return False
        return True

    @handle(InboundMsg.PURCHASE_AND_OPEN_PRODUCTS)
    async def handle_purchase_and_open_products(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Purchase and Open Products.")

        product_ids = message.get("products", [])
        shop = shop_manager.get_shop()

        basket = [(shop.available_products.get(p_id), 1)
                  for p_id in product_ids if p_id in shop.available_products]
        if not await self._charge_for(basket, "PurchaseAndOpen"):
            return

        await self._process_opening(request_id, flags, product_ids, is_tradable_override=message.get("isTradable"))

        # Update wallet UI (unsolicited sync uses request_id=0)
        if self.client.player:
            await self.push_wallet()

    @handle(InboundMsg.OPEN_PRODUCTS_BY_ARCHETYPE_ID)
    async def handle_open_products_by_archetype_id(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Open Products by Archetype ID.")

        product_ids = message.get("products", [])
        await self._process_opening(request_id, flags, product_ids, is_tradable_override=message.get("isTradable"))

    @handle(InboundMsg.PURCHASE_ARCHETYPES)
    async def handle_purchase_archetypes(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Purchase Archetypes.")

        archetypes = message.get("archetypes", {})

        shop = shop_manager.get_shop()
        basket = [(shop.available_products.get(arch_id), qty)
                  for arch_id, qty in archetypes.items()]
        if not await self._charge_for(basket, "PurchaseArchetypes"):
            return

        def _persist_sync():
            purchased = []
            for arch_id, qty in archetypes.items():
                pack_guid = shop.resolve_product_guid(arch_id)
                for _ in range(qty):
                    purchased.append(build_item(self._owner_id(), pack_guid, is_tradable=True))
                if self.client.player:
                    add_to_collection(self.client.player.account_id, pack_guid, count=qty, is_tradable=True)
            return purchased

        purchased_items = await run_db(_persist_sync)

        response = {
            "messageName": OutboundMsg.ARCHETYPES_PURCHASED.value,
            "items": purchased_items,
            "transactionID": str(uuid.uuid4())
        }
        await self.send(response, request_id)

        # Sync collection + wallet after purchase (unsolicited sync uses request_id=0)
        if self.client.player:
            await self.push_collection()
            await self.push_wallet()

    @handle(InboundMsg.PURCHASE_CATALOG_PRODUCTS)
    async def handle_purchase_catalog_products(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Purchase Catalog Products.")

        # product_ids can be string IDs like "product.bw1.boostersmall"
        product_ids = message.get("productIDs") or message.get("products") or []

        shop = shop_manager.get_shop()

        # Resolve products (IDs may be names rather than GUIDs)
        target_guids = []
        for p_id in product_ids:
            target_guid = p_id
            if p_id not in shop.available_products:
                for guid, product in shop.available_products.items():
                    if product.name == p_id:
                        target_guid = guid
                        break

            if target_guid in shop.available_products:
                target_guids.append(target_guid)
            else:
                logging.warning(f"[Shop] Product not found: {p_id}")

        basket = [(shop.available_products[guid], 1) for guid in target_guids]
        if not await self._charge_for(basket, "PurchaseCatalogProducts"):
            return

        # Process successful purchase (SKU -> real collection pack GUID)
        def _persist_sync():
            purchased = []
            for target_guid in target_guids:
                pack_guid = shop.resolve_product_guid(target_guid)
                purchased.append(build_item(self._owner_id(), pack_guid, is_tradable=True))
                if self.client.player:
                    add_to_collection(self.client.player.account_id, pack_guid, count=1, is_tradable=True)
            return purchased

        purchased_items = await run_db(_persist_sync)

        response = {
            "messageName": OutboundMsg.PRODUCTS_PURCHASED.value,
            "invoiceID": str(uuid.uuid4()),
            "items": purchased_items
        }
        await self.send(response, request_id)

        # Sync collection + wallet after purchase (unsolicited sync uses request_id=0)
        if self.client.player:
            await self.push_collection()
            await self.push_wallet()

    @handle(InboundMsg.GET_AVAILABLE_PRODUCTS)
    async def handle_get_available_products(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Available Products.")

        shop = shop_manager.get_shop()

        # Basic banner info for all products to satisfy client deserialization/linking
        properties = {}
        for guid, product in shop.available_products.items():
            properties[guid] = {
                "bannerText": product.get_attribute_value(AttrID.NAME, {"id": ""}),
                "bannerImage": config.PLACEHOLDER_IMG
            }

        response = {
            "messageName": OutboundMsg.AVAILABLE_PRODUCTS.value,
            "availableProducts": shop.get_available_guids(),
            "priceMap": shop.get_price_map(),
            "newArchetypes": shop.get_new_archetypes(),
            "archetypeProperties": properties
        }
        await self.send(response, request_id)

    @handle(InboundMsg.GET_FEATURED_PRODUCTS)
    async def handle_get_featured_products(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Featured Products.")

        shop = shop_manager.get_shop()

        response = {
            "messageName": OutboundMsg.FEATURED_PRODUCTS.value,
            "products": shop.get_featured_json()
        }
        await self.send(response, request_id)

    @handle(InboundMsg.GET_TOP_SELLING_PRODUCTS)
    async def handle_get_top_selling_products(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Top Selling Products.")

        shop = shop_manager.get_shop()

        response = {
            "messageName": OutboundMsg.TOP_SELLING_PRODUCTS.value,
            "invoiceID": str(uuid.uuid4()),
            "products": shop.get_top_selling_json()
        }
        await self.send(response, request_id)

    @handle(InboundMsg.GET_THEME_DECK_CONTENTS)
    async def handle_get_theme_deck_contents(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Theme Deck Contents.")

        shop = shop_manager.get_shop()

        response = {
            "messageName": "ThemeDeckContentsMap",
            "themeDeckContentsMap": shop.theme_deck_contents
        }
        await self.send(response, request_id)
