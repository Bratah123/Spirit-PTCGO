import unittest
import os
import tempfile
from unittest.mock import MagicMock, AsyncMock, patch

from spirit.database import db_manager

SWSH8_BOOSTER = "d017c195-83c5-c74e-0638-25128b3116c4"


def _pack_sku(shop, pack_guid):
    """The shop-facing SKU GUID that maps to a given collection pack GUID."""
    for sku, pack in shop.sku_to_pack.items():
        if pack == pack_guid:
            return sku
    return None


class TestDynamicShop(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        cls.db_patcher = patch('spirit.database.connection.DB_PATH', cls.db_path)
        cls.db_patcher.start()

        from spirit.database.setup_db import setup_database
        setup_database()

    @classmethod
    def tearDownClass(cls):
        cls.db_patcher.stop()
        try:
            os.close(cls.db_fd)
            os.unlink(cls.db_path)
        except OSError:
            pass

    def setUp(self):
        # Clear any admin shop rows between tests, then rebuild the shop
        from spirit.database import db_session, ShopItem
        with db_session() as session:
            session.query(ShopItem).delete()
        from spirit.shop import shop_manager
        shop_manager.reload_from_db()

    def test_shop_offers_boosters_only_for_eligible_sets(self):
        from spirit.shop import shop_manager
        from spirit.game.set_utils import eligible_booster_sets
        from spirit.game.attributes import ProductType

        shop = shop_manager.get_shop()
        eligible = {c.upper() for c in eligible_booster_sets()}

        pack_keys = {p.key.upper() for p in shop.available_products.values()
                     if p.product_type == ProductType.PACKS.value}
        self.assertEqual(pack_keys, eligible)
        self.assertNotIn("BW1", pack_keys)
        self.assertIn("SWSH12", pack_keys)

        # Every offered pack has a price
        for p in shop.available_products.values():
            if p.product_type == ProductType.PACKS.value:
                self.assertTrue(p.prices, f"pack {p.key} has no price")

    def test_admin_shop_item_overrides_price(self):
        from spirit.database.economy_data import upsert_shop_item
        from spirit.shop import shop_manager
        from spirit.game.attributes import AttrID

        upsert_shop_item(product_guid=SWSH8_BOOSTER, price=555,
                         currency=AttrID.TRAINER_TOKENS.value, featured=True)
        shop_manager.reload_from_db()

        shop = shop_manager.get_shop()
        sku = _pack_sku(shop, SWSH8_BOOSTER)
        self.assertIsNotNone(sku)
        product = shop.available_products[sku]
        self.assertEqual(product.prices[0]["value"], 555)
        self.assertIn(sku, [fp.product_id for fp in shop.featured_products])

    def test_disabled_admin_item_removes_product(self):
        from spirit.database.economy_data import upsert_shop_item
        from spirit.shop import shop_manager

        upsert_shop_item(product_guid=SWSH8_BOOSTER, enabled=False)
        shop_manager.reload_from_db()

        shop = shop_manager.get_shop()
        # Neither the raw pack GUID nor a SKU for it is listed when disabled
        self.assertNotIn(SWSH8_BOOSTER, shop.available_products)
        self.assertIsNone(_pack_sku(shop, SWSH8_BOOSTER))

    def test_owned_pack_guid_is_never_listed_in_shop(self):
        # The collection pack GUID must stay out of the shop (only its SKU is listed), so the
        # client never marks it dynamic and never evicts it from the collection on shop exit.
        from spirit.shop import shop_manager
        shop = shop_manager.get_shop()
        self.assertNotIn(SWSH8_BOOSTER, shop.available_products)
        sku = _pack_sku(shop, SWSH8_BOOSTER)
        self.assertIsNotNone(sku)
        self.assertNotEqual(sku, SWSH8_BOOSTER)
        self.assertIn(sku, shop.available_products)

    def _make_shop_handler(self, account_id):
        from spirit.packets.handlers.shop import ShopHandler
        from spirit.game.models.player import Player

        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 7777)
        mock_client.player = Player({
            "account_id": account_id,
            "username": "buyer",
            "screen_name": "Buyer"
        })
        return ShopHandler(mock_client), mock_client

    async def test_purchase_catalog_product_deducts_and_persists(self):
        from spirit.database.player_data import get_wallet_by_account_id, get_collection_by_account_id
        from spirit.network.message_names import OutboundMsg
        from spirit.game.attributes import AttrID

        account_id = "acc-shop-buy-1"
        get_wallet_by_account_id(account_id)  # seed wallet (50000 coins)

        from spirit.shop import shop_manager
        sku = _pack_sku(shop_manager.get_shop(), SWSH8_BOOSTER)

        handler, client = self._make_shop_handler(account_id)
        before_coins = handler.client.player.wallet.balances[AttrID.TRAINER_TOKENS]

        # Client buys the shop SKU; server grants the real collection pack GUID
        await handler.handle_purchase_catalog_products(
            {"productIDs": [sku], "purchaseType": 0}, 60, 0)

        sent = [c.args[0] for c in client.send_packet.call_args_list]
        purchased = [m for m in sent if m.get("messageName") == OutboundMsg.PRODUCTS_PURCHASED.value]
        self.assertEqual(len(purchased), 1)
        self.assertEqual(purchased[0]["items"][0]["archetypeID"], SWSH8_BOOSTER)

        # Wallet deducted by the default booster price
        after_coins = handler.client.player.wallet.balances[AttrID.TRAINER_TOKENS]
        self.assertEqual(after_coins, before_coins - 200)

        # Persisted in collection
        col = {c["archetype_id"]: c for c in get_collection_by_account_id(account_id)}
        self.assertIn(SWSH8_BOOSTER, col)
        self.assertEqual(col[SWSH8_BOOSTER]["tradable_count"], 1)

    async def test_purchase_insufficient_funds_rejected(self):
        from spirit.database.player_data import get_wallet_by_account_id, update_wallet
        from spirit.network.message_names import OutboundMsg

        account_id = "acc-shop-poor"
        get_wallet_by_account_id(account_id)
        update_wallet(account_id, 5, 0, 0)  # only 5 coins

        from spirit.shop import shop_manager
        sku = _pack_sku(shop_manager.get_shop(), SWSH8_BOOSTER)

        handler, client = self._make_shop_handler(account_id)
        await handler.handle_purchase_catalog_products(
            {"productIDs": [sku], "purchaseType": 0}, 61, 0)

        sent = [c.args[0] for c in client.send_packet.call_args_list]
        purchased = [m for m in sent if m.get("messageName") == OutboundMsg.PRODUCTS_PURCHASED.value]
        self.assertEqual(len(purchased), 0)

    async def test_open_booster_grants_ten_cards(self):
        from spirit.database.player_data import add_to_collection, get_collection_by_account_id
        from spirit.network.message_names import OutboundMsg

        account_id = "acc-shop-open-1"
        add_to_collection(account_id, SWSH8_BOOSTER, count=1, is_tradable=False)

        handler, client = self._make_shop_handler(account_id)
        await handler.handle_open_products_by_archetype_id(
            {"products": [SWSH8_BOOSTER]}, 62, 0)

        sent = [c.args[0] for c in client.send_packet.call_args_list]
        opened = [m for m in sent if m.get("messageName") == OutboundMsg.PRODUCTS_OPENED.value]
        self.assertEqual(len(opened), 1)
        self.assertEqual(len(opened[0]["items"]), 10)

        # Every generated card belongs to SWSH8's card scripts
        from spirit.game.scripts.cards import loader as card_loader
        for item in opened[0]["items"]:
            card = card_loader.cards_by_guid.get(item["archetypeID"].lower())
            self.assertIsNotNone(card)
            self.assertIn(card.key.lower(), ("swsh8", "free_energy"))

    def test_get_available_products_lists_eligible_packs(self):
        from spirit.shop import shop_manager
        shop = shop_manager.get_shop()
        sku = _pack_sku(shop, SWSH8_BOOSTER)
        guids = shop.get_available_guids()
        self.assertIn(sku, guids)
        self.assertNotIn(SWSH8_BOOSTER, guids)  # only the SKU is listed
        price_map = shop.get_price_map()
        self.assertEqual(price_map[sku]["value"][0]["value"], 200)


if __name__ == '__main__':
    unittest.main()
