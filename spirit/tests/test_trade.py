import unittest
import os
import tempfile
from unittest.mock import MagicMock, AsyncMock, patch

from spirit.database import db_manager

CARD_A = "aaaaaaaa-1111-2222-3333-444444444444"
CARD_B = "bbbbbbbb-1111-2222-3333-444444444444"


class TestTradeSystem(unittest.IsolatedAsyncioTestCase):
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
        from spirit.database import db_session, TradeOffer, Collection
        with db_session() as session:
            session.query(TradeOffer).delete()
            session.query(Collection).filter(
                Collection.archetype_id.in_([CARD_A, CARD_B])).delete(synchronize_session=False)

    def _give(self, account_id, guid, count):
        from spirit.database.player_data import add_to_collection
        add_to_collection(account_id, guid, count=count, is_tradable=True)

    def _tradable_count(self, account_id, guid):
        from spirit.database.player_data import get_collection_by_account_id
        for c in get_collection_by_account_id(account_id):
            if c["archetype_id"] == guid:
                return c["tradable_count"]
        return 0

    def _make_handler(self, account_id, server=None):
        from spirit.packets.handlers.trade import TradeHandler
        from spirit.game.models.player import Player

        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 9999)
        mock_client.server = server or MagicMock(clients=[])
        mock_client.player = Player({
            "account_id": account_id,
            "username": f"user_{account_id[:6]}",
            "screen_name": f"User {account_id[:6]}"
        })
        return TradeHandler(mock_client), mock_client

    def _sent_by_name(self, mock_client, name):
        return [c.args[0] for c in mock_client.send_packet.call_args_list
                if isinstance(c.args[0], dict) and c.args[0].get("messageName") == name]

    # ------------------------------------------------------------- data layer

    def test_create_offer_requires_ownership(self):
        from spirit.database import economy_data

        offer, error = economy_data.create_trade_offer(
            "acc-t-poor", {CARD_A: 1}, {CARD_B: 1})
        self.assertIsNone(offer)
        self.assertEqual(error, "trade.createLot.notEnoughCards.body")

        self._give("acc-t-rich", CARD_A, 2)
        offer, error = economy_data.create_trade_offer(
            "acc-t-rich", {CARD_A: 2}, {CARD_B: 1})
        self.assertIsNone(error)
        self.assertEqual(offer["status"], "open")

    def test_accept_swaps_items_atomically(self):
        from spirit.database import economy_data

        seller, buyer = "acc-t-seller", "acc-t-buyer"
        self._give(seller, CARD_A, 3)
        self._give(buyer, CARD_B, 2)

        offer, _ = economy_data.create_trade_offer(seller, {CARD_A: 3}, {CARD_B: 2})
        accepted, error = economy_data.accept_trade_offer(offer["offer_id"], buyer)

        self.assertIsNone(error)
        self.assertEqual(accepted["status"], "accepted")
        self.assertEqual(accepted["accepted_by"], buyer)

        self.assertEqual(self._tradable_count(seller, CARD_A), 0)
        self.assertEqual(self._tradable_count(seller, CARD_B), 2)
        self.assertEqual(self._tradable_count(buyer, CARD_A), 3)
        self.assertEqual(self._tradable_count(buyer, CARD_B), 0)

    def test_accept_fails_without_requested_items_and_rolls_back(self):
        from spirit.database import economy_data

        seller, buyer = "acc-t-seller2", "acc-t-buyer2"
        self._give(seller, CARD_A, 1)
        # Buyer owns nothing

        offer, _ = economy_data.create_trade_offer(seller, {CARD_A: 1}, {CARD_B: 1})
        accepted, error = economy_data.accept_trade_offer(offer["offer_id"], buyer)

        self.assertIsNone(accepted)
        self.assertEqual(error, "trade.createLot.notEnoughCards.body")
        # Nothing moved, offer still open
        self.assertEqual(self._tradable_count(seller, CARD_A), 1)
        self.assertEqual(economy_data.get_trade_offer(offer["offer_id"])["status"], "open")

    def test_accept_cancels_stale_offer_when_seller_spent_items(self):
        from spirit.database import economy_data
        from spirit.database.player_data import remove_from_collection

        seller, buyer = "acc-t-seller3", "acc-t-buyer3"
        self._give(seller, CARD_A, 1)
        self._give(buyer, CARD_B, 1)

        offer, _ = economy_data.create_trade_offer(seller, {CARD_A: 1}, {CARD_B: 1})
        remove_from_collection(seller, CARD_A, count=1, is_tradable=True)

        accepted, error = economy_data.accept_trade_offer(offer["offer_id"], buyer)
        self.assertIsNone(accepted)
        self.assertIsNotNone(error)
        self.assertEqual(economy_data.get_trade_offer(offer["offer_id"])["status"], "cancelled")

    def test_private_offer_only_acceptable_by_recipient(self):
        from spirit.database import economy_data

        seller, friend, stranger = "acc-t-s4", "acc-t-f4", "acc-t-x4"
        self._give(seller, CARD_A, 1)
        self._give(friend, CARD_B, 1)
        self._give(stranger, CARD_B, 1)

        offer, _ = economy_data.create_trade_offer(
            seller, {CARD_A: 1}, {CARD_B: 1}, recipient_id=friend)

        _, error = economy_data.accept_trade_offer(offer["offer_id"], stranger)
        self.assertIsNotNone(error)

        accepted, error = economy_data.accept_trade_offer(offer["offer_id"], friend)
        self.assertIsNone(error)
        self.assertEqual(accepted["accepted_by"], friend)

    # ------------------------------------------------------------- handlers

    async def test_create_and_view_public_board(self):
        from spirit.network.message_names import OutboundMsg

        seller_id = "acc-t-h-seller"
        self._give(seller_id, CARD_A, 2)

        seller, seller_client = self._make_handler(seller_id)
        await seller.handle_create_lot({
            "forTrade": {CARD_A: 2}, "toReceive": {CARD_B: 1},
            "privateTo": None, "message": "", "expirationType": 0
        }, 70, 0)

        created = self._sent_by_name(seller_client, OutboundMsg.LOT_CREATED.value)
        self.assertEqual(len(created), 1)
        lot_id = created[0]["lotID"]

        # Another player sees it on the public board
        viewer, viewer_client = self._make_handler("acc-t-h-viewer")
        await viewer.handle_view_public_trades({"offset": 0, "limit": 50}, 71, 0)

        lots = self._sent_by_name(viewer_client, OutboundMsg.LOTS_RETRIEVED.value)[0]["lots"]
        self.assertEqual(len(lots), 1)
        lot = lots[0]
        self.assertEqual(lot["id"], lot_id)
        self.assertEqual(len(lot["items"]), 2)
        self.assertEqual(lot["cardPrice"], {CARD_B: 1})

        # The seller does NOT see their own lot on the public board
        seller_client.send_packet.reset_mock()
        await seller.handle_view_public_trades({"offset": 0, "limit": 50}, 72, 0)
        lots = self._sent_by_name(seller_client, OutboundMsg.LOTS_RETRIEVED.value)[0]["lots"]
        self.assertEqual(len(lots), 0)

        # But sees it under My Lots
        seller_client.send_packet.reset_mock()
        await seller.handle_view_my_lots({"offset": 0, "limit": 50}, 73, 0)
        lots = self._sent_by_name(seller_client, OutboundMsg.MY_LOTS_RETRIEVED.value)[0]["lots"]
        self.assertEqual(len(lots), 1)

    async def test_accept_trade_handler_swaps_and_notifies(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        seller_id, buyer_id = "acc-t-h-s2", "acc-t-h-b2"
        self._give(seller_id, CARD_A, 1)
        self._give(buyer_id, CARD_B, 1)

        offer, _ = economy_data.create_trade_offer(seller_id, {CARD_A: 1}, {CARD_B: 1})

        # Seller is online on a mock server
        server = MagicMock()
        seller_handler, seller_client = self._make_handler(seller_id, server)
        server.clients = [seller_client]

        buyer_handler, buyer_client = self._make_handler(buyer_id, server)
        await buyer_handler.handle_accept_trade({"lotID": offer["offer_id"]}, 80, 0)

        sold = self._sent_by_name(buyer_client, OutboundMsg.LOT_SOLD.value)
        self.assertEqual(len(sold), 1)
        self.assertTrue(self._sent_by_name(buyer_client, OutboundMsg.COLLECTION_COUNT_FOUND.value))

        # Owner notified too
        self.assertTrue(self._sent_by_name(seller_client, OutboundMsg.LOT_SOLD.value))

        self.assertEqual(self._tradable_count(buyer_id, CARD_A), 1)
        self.assertEqual(self._tradable_count(seller_id, CARD_B), 1)

    async def test_remove_lot(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        seller_id = "acc-t-h-s3"
        self._give(seller_id, CARD_A, 1)
        offer, _ = economy_data.create_trade_offer(seller_id, {CARD_A: 1}, {CARD_B: 1})

        handler, client = self._make_handler(seller_id)
        await handler.handle_remove_lot({"lotID": offer["offer_id"]}, 90, 0)

        removed = self._sent_by_name(client, OutboundMsg.LOT_REMOVED.value)
        self.assertEqual(len(removed), 1)
        self.assertEqual(economy_data.get_trade_offer(offer["offer_id"])["status"], "cancelled")

    async def test_count_handshake_precedes_pagination(self):
        """The client asks for a count first; the reply must carry the true total."""
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        seller_id = "acc-t-count-s"
        self._give(seller_id, CARD_A, 3)
        economy_data.create_trade_offer(seller_id, {CARD_A: 1}, {CARD_B: 1})
        economy_data.create_trade_offer(seller_id, {CARD_A: 2}, {CARD_B: 2})

        # Owner: My Lots count
        seller, seller_client = self._make_handler(seller_id)
        await seller.handle_view_my_lots_count({}, 200, 0)
        counts = self._sent_by_name(seller_client, OutboundMsg.MY_LOTS_RETRIEVED_COUNT.value)
        self.assertEqual(len(counts), 1)
        self.assertEqual(counts[0]["count"], 2)

        # Public count from another viewer sees both (not their own)
        viewer, viewer_client = self._make_handler("acc-t-count-v")
        await viewer.handle_view_public_trades_count({}, 201, 0)
        pub = self._sent_by_name(viewer_client, OutboundMsg.LOTS_RETRIEVED_COUNT.value)
        self.assertEqual(pub[0]["count"], 2)

        # The seller's own public count excludes their own lots
        seller_client.send_packet.reset_mock()
        await seller.handle_view_public_trades_count({}, 202, 0)
        pub = self._sent_by_name(seller_client, OutboundMsg.LOTS_RETRIEVED_COUNT.value)
        self.assertEqual(pub[0]["count"], 0)

    async def test_public_count_matches_paginated_results(self):
        """Count and page must agree so the client paginates to completion."""
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        # Two sellers post public lots; viewer is a third party
        for i, sid in enumerate(["acc-t-pc-1", "acc-t-pc-2"]):
            self._give(sid, CARD_A, 1)
            economy_data.create_trade_offer(sid, {CARD_A: 1}, {CARD_B: 1})

        viewer, client = self._make_handler("acc-t-pc-viewer")
        await viewer.handle_view_public_trades_count({}, 210, 0)
        count = self._sent_by_name(client, OutboundMsg.LOTS_RETRIEVED_COUNT.value)[0]["count"]

        client.send_packet.reset_mock()
        await viewer.handle_view_public_trades({"offset": 0, "limit": count}, 211, 0)
        lots = self._sent_by_name(client, OutboundMsg.LOTS_RETRIEVED.value)[0]["lots"]
        self.assertEqual(len(lots), count)

    async def test_private_count_and_view(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        seller_id, friend_id = "acc-t-pv-s", "acc-t-pv-f"
        self._give(seller_id, CARD_A, 1)
        economy_data.create_trade_offer(
            seller_id, {CARD_A: 1}, {CARD_B: 1}, recipient_id=friend_id)

        friend, client = self._make_handler(friend_id)
        await friend.handle_view_private_trades_count({}, 220, 0)
        count = self._sent_by_name(client, OutboundMsg.PRIVATE_LOTS_RETRIEVED_COUNT.value)
        self.assertEqual(count[0]["count"], 1)

        client.send_packet.reset_mock()
        await friend.handle_view_private_trades({"offset": 0, "limit": 1}, 221, 0)
        lots = self._sent_by_name(client, OutboundMsg.PRIVATE_LOTS_RETRIEVED.value)[0]["lots"]
        self.assertEqual(len(lots), 1)

    async def test_trade_history_count_and_view(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        seller_id, buyer_id = "acc-t-hist-s", "acc-t-hist-b"
        self._give(seller_id, CARD_A, 1)
        self._give(buyer_id, CARD_B, 1)
        offer, _ = economy_data.create_trade_offer(seller_id, {CARD_A: 1}, {CARD_B: 1})
        economy_data.accept_trade_offer(offer["offer_id"], buyer_id)

        buyer, client = self._make_handler(buyer_id)
        await buyer.handle_view_trade_history_count({"accountID": buyer_id}, 230, 0)
        count = self._sent_by_name(client, OutboundMsg.TRADE_HISTORY_RETRIEVED_COUNT.value)
        self.assertEqual(count[0]["count"], 1)

        client.send_packet.reset_mock()
        await buyer.handle_view_trade_history(
            {"accountID": buyer_id, "offset": 0, "limit": 50}, 231, 0)
        res = self._sent_by_name(client, OutboundMsg.TRADE_HISTORY_RETRIEVED.value)[0]
        self.assertEqual(res["offset"], 0)
        self.assertEqual(len(res["history"]), 1)

    def test_count_handlers_registered(self):
        from spirit.packets.handlers.trade import TradeHandler
        from spirit.network.message_names import InboundMsg
        from unittest.mock import MagicMock

        handlers = TradeHandler(MagicMock()).get_handlers()
        for name in (InboundMsg.VIEW_MY_LOTS_COUNT, InboundMsg.VIEW_ALL_PRIVATE_TRADES_COUNT,
                     InboundMsg.VIEW_ALL_PUBLIC_TRADES_COUNT, InboundMsg.VIEW_TRADE_HISTORY_2_COUNT,
                     InboundMsg.VIEW_TRADE_HISTORY_2):
            self.assertIn(name.value, handlers)

    async def test_search_for_lots(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        seller_id = "acc-t-h-s5"
        self._give(seller_id, CARD_A, 1)
        economy_data.create_trade_offer(seller_id, {CARD_A: 1}, {CARD_B: 1})

        viewer, client = self._make_handler("acc-t-h-v5")
        await viewer.handle_search_for_lots({"archetypes": [CARD_A]}, 91, 0)
        lots = self._sent_by_name(client, OutboundMsg.LOTS_RETRIEVED.value)[0]["lots"]
        self.assertEqual(len(lots), 1)

        client.send_packet.reset_mock()
        await viewer.handle_search_for_lots({"archetypes": [CARD_B]}, 92, 0)
        lots = self._sent_by_name(client, OutboundMsg.LOTS_RETRIEVED.value)[0]["lots"]
        self.assertEqual(len(lots), 0)

    async def test_archetype_flags_handlers(self):
        from spirit.database.player_data import get_archetype_flags
        from spirit.network.message_names import OutboundMsg

        user_id = "acc-flags-test"
        handler, client = self._make_handler(user_id)

        # Test SetArchetypeForTradeCount
        await handler.handle_set_archetype_for_trade_count({
            "archetypeID": CARD_A,
            "forTrade": 5
        }, 123, 0)

        # Verify Outbound Msg
        res = self._sent_by_name(client, OutboundMsg.ARCHETYPE_FOR_TRADE_SET.value)[0]
        self.assertEqual(res["archetypeID"], CARD_A)
        self.assertEqual(res["forTrade"], 5)

        # Test SetArchetypeReview
        await handler.handle_set_archetype_review({
            "archetypeID": CARD_A,
            "review": 1
        }, 124, 0)

        # Verify Outbound Msg
        res = self._sent_by_name(client, OutboundMsg.ARCHETYPE_REVIEW_SET.value)[0]
        self.assertEqual(res["archetypeID"], CARD_A)
        self.assertEqual(res["review"], 1)

        # Retrieve flags via player_data helper
        flags = get_archetype_flags(user_id)
        self.assertEqual(len(flags), 1)
        self.assertEqual(flags[0]["archetypeID"], CARD_A)
        self.assertEqual(flags[0]["forTrade"], 5)
        self.assertEqual(flags[0]["review"], 1)

    async def test_get_create_lot_prices_handler(self):
        from spirit.network.message_names import OutboundMsg
        from spirit.game.attributes import AttrID

        handler, client = self._make_handler("acc-prices-test")
        await handler.handle_get_create_lot_prices({}, 125, 0)

        # Verify Outbound Msg
        res = self._sent_by_name(client, OutboundMsg.CREATE_LOT_PRICES.value)[0]
        prices = res["prices"]
        self.assertEqual(prices[0]["name"], AttrID.TRAINER_TOKENS.value)
        self.assertEqual(prices[0]["value"], 8)
        self.assertEqual(prices[1]["name"], AttrID.TRAINER_TOKENS.value)
        self.assertEqual(prices[1]["value"], 24)
        self.assertEqual(prices[2]["name"], AttrID.TRAINER_TOKENS.value)
        self.assertEqual(prices[2]["value"], 48)


if __name__ == '__main__':
    unittest.main()
