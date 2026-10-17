import json
import logging
import uuid
import time
from collections import Counter

from spirit import config
from spirit.network.message_names import InboundMsg, OutboundMsg
from .base import BaseHandler, handle
from spirit.shop import shop_manager
from spirit.game.scripts.products import loader as product_loader
from spirit.game.attributes import AttrID
from spirit.game.models.product import BoosterPack, Deck
from spirit.database.deck_products import open_products
from spirit.database.async_utils import run_db
from spirit.database.player_data import add_to_collection, get_decks_by_account_id
from spirit.database.economy_data import purchase_products

# ProductPurchaseFailure texts; unknown loc keys render verbatim in the failure dialog.
PURCHASE_ERROR_SIGN_IN = "Sign in to buy products."
PURCHASE_ERROR_UNAVAILABLE = "This product is no longer available. Please reopen the shop."
PURCHASE_ERROR_GENERIC = "Your purchase could not be completed. You have not been charged."

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

    def _open_products_sync(self, product_ids, is_tradable_override, purchased=False):
        """Opens products and persists collection changes; runs on a DB worker thread."""
        shop = shop_manager.get_shop()
        account_id = self.client.player.account_id if self.client.player else None
        owner_id = account_id or "0"

        products = []
        for p_id in product_ids:
            pack_guid = shop.resolve_product_guid(p_id)
            product = product_loader.products_by_guid.get(pack_guid) or \
                product_loader.products_by_guid.get(pack_guid.lower())
            if not product:
                raise ValueError("Unknown product requested")
            products.append(product)
        if not account_id:
            raise ValueError("Sign in before opening products")
        opened = open_products(account_id, products, purchased=purchased,
                               tradable_override=is_tradable_override)
        opened_items = []
        opened_products = []
        for guid, contents, tradable in opened:
            opened_products.append(build_item(owner_id, guid, tradable))
            opened_items.extend(build_item(owner_id, card_guid, tradable) for card_guid in contents)

        return opened_items, opened_products

    async def _send_notification(self, name: str, value: dict):
        """Pushes a Notification; the client also dispatches its payload as a normal message."""
        await self.send({
            "messageName": OutboundMsg.NOTIFICATION.value,
            "notificationID": str(uuid.uuid4()),
            "payload": json.dumps({"name": name, "value": value}),
            "notificationType": 0,
        })

    async def _process_opening(self, request_id, flags, product_ids, is_tradable_override=None,
                               purchased=False):
        try:
            opened_items, opened_products = await run_db(
                self._open_products_sync, product_ids, is_tradable_override, purchased)
        except Exception:
            logging.exception("[Shop] Product opening failed for %s", self._owner_id())
            await self.send({
                "messageName": OutboundMsg.PRODUCTS_OPENED_FAILURE.value,
                "error": {"id": "Unable to open these products. Please try again."},
            }, request_id)
            return

        opened = {
            "accountID": self._owner_id(),
            "items": opened_items,
            "products": opened_products,
            "additionalData": {}
        }
        products = [product_loader.products_by_guid.get(item["archetypeID"]) for item in opened_products]
        if any(isinstance(product, BoosterPack) for product in products):
            await self.send(dict(opened, messageName=OutboundMsg.PRODUCTS_OPENED.value), request_id)
        else:
            # No pack-opening sequence: the client only reacts to ProductsOpened as a notification.
            if self.client.player and any(isinstance(product, Deck) for product in products):
                self.client.player.decks = await run_db(
                    get_decks_by_account_id, self.client.player.account_id)
                payload = self.client.player.get_decks_data()
                await self.send(dict(payload, messageName=OutboundMsg.DECK_LIST.value))
            await self._send_notification(OutboundMsg.PRODUCTS_OPENED.value, opened)

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

        shop = shop_manager.get_shop()
        product_ids = [guid for guid in message.get("products", [])
                       if guid in shop.available_products]

        basket = [(shop.available_products.get(p_id), 1)
                  for p_id in product_ids if p_id in shop.available_products]
        if not await self._charge_for(basket, "PurchaseAndOpen"):
            return

        await self._process_opening(request_id, flags, product_ids,
                                    is_tradable_override=message.get("isTradable"), purchased=True)

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

        shop = shop_manager.get_shop()
        archetypes = {guid: qty for guid, qty in message.get("archetypes", {}).items()
                      if guid in shop.available_products and type(qty) is int and qty > 0}
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

    @staticmethod
    def _resolve_listings(shop, message):
        """Shop listings for a PurchaseCatalogProducts request (one entry per unit), or None
        if any is unknown. Prefers the exact listing GUIDs in selections over name loc-IDs."""
        selections = message.get("selections") or []
        requested = selections or message.get("products") or message.get("productIDs") or []
        listings = []
        for p_id in requested:
            p_id = str(p_id)
            listing = shop.available_products.get(p_id) or shop.available_products.get(p_id.lower())
            if listing is None and not selections:
                listing = next((p for p in shop.available_products.values() if p.name == p_id), None)
            if listing is None:
                logging.warning(f"[Shop] Purchase references unavailable product {p_id}")
                return None
            listings.append(listing)
        return listings or None

    async def _purchase_failed(self, request_id, reason: str):
        """Fails a pending purchase: closes the client's wait dialog with the reason."""
        await self.send({
            "messageName": OutboundMsg.PRODUCT_PURCHASE_FAILURE.value,
            "error": {"id": reason},
        }, request_id)
        if self.client.player:
            await self.push_wallet()  # the client already deducted its display locally

    @handle(InboundMsg.PURCHASE_CATALOG_PRODUCTS)
    async def handle_purchase_catalog_products(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Purchase Catalog Products.")
        player = self.client.player
        if not player:
            await self._purchase_failed(request_id, PURCHASE_ERROR_SIGN_IN)
            return

        shop = shop_manager.get_shop()
        listings = self._resolve_listings(shop, message)
        if listings is None:
            await self._purchase_failed(request_id, PURCHASE_ERROR_UNAVAILABLE)
            return

        charges = Counter()
        for listing in listings:
            for price in listing.prices[:1]:
                charges[price.get("name")] += max(0, int(price.get("value") or 0))
        purchase_type = message.get("purchaseType")
        if purchase_type is not None and any(charges.values()) and purchase_type not in charges:
            logging.warning(f"[Shop] purchaseType {purchase_type} differs from listed currencies {list(charges)}")
        product_guids = [shop.resolve_product_guid(listing.guid) for listing in listings]

        def _purchase_sync():
            error = purchase_products(player.account_id, charges, Counter(product_guids))
            if error is None:
                player.wallet.refresh_wallet()
            return error

        try:
            error = await run_db(_purchase_sync)
        except Exception:
            logging.exception(f"[Shop] Purchase failed for {player.username}")
            error = PURCHASE_ERROR_GENERIC
        if error:
            logging.warning(f"[Shop] Purchase rejected for {player.username}: {error}")
            await self._purchase_failed(request_id, error)
            return

        purchased_items = [build_item(player.account_id, guid, is_tradable=True)
                           for guid in product_guids]
        await self.send({
            "messageName": OutboundMsg.PRODUCTS_PURCHASED.value,
            "invoiceID": str(uuid.uuid4()),
            "items": purchased_items
        }, request_id)
        # No push_collection: the dialog command adds these items client-side (would double).
        await self._send_notification(OutboundMsg.PRODUCTS_FULFILLED.value, {"items": purchased_items})
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

        response = {
            "messageName": OutboundMsg.THEME_DECK_CONTENTS_MAP.value,
            "themeDeckContentsMap": product_loader.theme_decks.contents_map()
        }
        await self.send(response, request_id)
