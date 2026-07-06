import unittest
import os
import tempfile
from unittest.mock import MagicMock, AsyncMock, patch

from spirit.database import db_manager


class TestCodeRedemption(unittest.IsolatedAsyncioTestCase):
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

    def _make_handler(self, account_id):
        from spirit.packets.handlers.redemption import RedemptionHandler
        from spirit.game.models.player import Player

        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 5555)
        mock_client.player = Player({
            "account_id": account_id,
            "username": "redeemer",
            "screen_name": "Redeemer"
        })
        return RedemptionHandler(mock_client), mock_client

    def _sent_by_name(self, mock_client, name):
        return [c.args[0] for c in mock_client.send_packet.call_args_list
                if isinstance(c.args[0], dict) and c.args[0].get("messageName") == name]

    async def test_validate_code_valid_and_invalid(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        code = economy_data.create_code(reward={"coins": 100}, max_uses=1)["code_string"]
        handler, client = self._make_handler("acc-validate-1")

        await handler.handle_validate_code({"code": code}, 10, 0)
        valid = self._sent_by_name(client, OutboundMsg.CODE_IS_VALID.value)
        self.assertEqual(len(valid), 1)
        self.assertEqual(valid[0]["code"], code)

        await handler.handle_validate_code({"code": "SPIRIT-FAKE-FAKE-FAKE"}, 11, 0)
        invalid = self._sent_by_name(client, OutboundMsg.INVALID_CODE.value)
        self.assertEqual(len(invalid), 1)
        self.assertIn("id", invalid[0]["reason"])

    async def test_redeem_code_grants_rewards(self):
        from spirit.database import economy_data
        from spirit.database.player_data import get_wallet_by_account_id, get_collection_by_account_id
        from spirit.network.message_names import OutboundMsg

        account_id = "acc-redeem-1"
        # Seed wallet
        get_wallet_by_account_id(account_id)
        before = get_wallet_by_account_id(account_id)

        pack_guid = "d017c195-83c5-c74e-0638-25128b3116c4"
        code = economy_data.create_code(
            reward={"coins": 250, "gems": 5, "products": {pack_guid: 3}}, max_uses=1
        )["code_string"]

        handler, client = self._make_handler(account_id)
        await handler.handle_redeem_codes({"codes": [code]}, 20, 0)

        success = self._sent_by_name(client, OutboundMsg.CODE_SUCCESSFULLY_REDEEMED.value)
        self.assertEqual(len(success), 1)
        self.assertEqual(success[0]["code"], code)

        # Wallet credited
        after = get_wallet_by_account_id(account_id)
        self.assertEqual(after["coins"], before["coins"] + 250)
        self.assertEqual(after["gems"], before["gems"] + 5)

        # Collection credited
        col = {c["archetype_id"]: c for c in get_collection_by_account_id(account_id)}
        self.assertEqual(col[pack_guid]["nontradable_count"], 3)

        # Collection + wallet syncs were pushed
        self.assertTrue(self._sent_by_name(client, OutboundMsg.COLLECTION_COUNT_FOUND.value))
        self.assertTrue(self._sent_by_name(client, OutboundMsg.CURRENT_WALLET.value))

    async def test_redeem_twice_fails(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        code = economy_data.create_code(reward={"coins": 10}, max_uses=0)["code_string"]
        handler, client = self._make_handler("acc-redeem-twice")

        await handler.handle_redeem_codes({"codes": [code]}, 30, 0)
        await handler.handle_redeem_codes({"codes": [code]}, 31, 0)

        self.assertEqual(len(self._sent_by_name(client, OutboundMsg.CODE_SUCCESSFULLY_REDEEMED.value)), 1)
        failures = self._sent_by_name(client, OutboundMsg.CODE_REDEMPTION_FAILURE.value)
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0]["reason"]["id"], "shop.redeemcodes.error.codealreadyused")

    async def test_max_uses_exhaustion(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        code = economy_data.create_code(reward={"coins": 10}, max_uses=1)["code_string"]

        handler1, client1 = self._make_handler("acc-uses-1")
        await handler1.handle_redeem_codes({"codes": [code]}, 40, 0)
        self.assertEqual(len(self._sent_by_name(client1, OutboundMsg.CODE_SUCCESSFULLY_REDEEMED.value)), 1)

        handler2, client2 = self._make_handler("acc-uses-2")
        await handler2.handle_redeem_codes({"codes": [code]}, 41, 0)
        failures = self._sent_by_name(client2, OutboundMsg.CODE_REDEMPTION_FAILURE.value)
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0]["reason"]["id"], "shop.redeemcodes.error.codeexpired")

    async def test_disabled_code_rejected(self):
        from spirit.database import economy_data
        from spirit.network.message_names import OutboundMsg

        code = economy_data.create_code(reward={"coins": 10}, enabled=False)["code_string"]
        handler, client = self._make_handler("acc-disabled")

        await handler.handle_validate_code({"code": code}, 50, 0)
        invalid = self._sent_by_name(client, OutboundMsg.INVALID_CODE.value)
        self.assertEqual(len(invalid), 1)

    def test_handler_registered_in_router(self):
        from spirit.packets.handlers.redemption import RedemptionHandler
        from spirit.network.message_names import InboundMsg

        handler = RedemptionHandler(MagicMock())
        handlers = handler.get_handlers()
        self.assertIn(InboundMsg.VALIDATE_CODE.value, handlers)
        self.assertIn(InboundMsg.REDEEM_CODES.value, handlers)


if __name__ == '__main__':
    unittest.main()
