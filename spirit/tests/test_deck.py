import unittest
import os
import tempfile
import uuid
import json
from unittest.mock import MagicMock, AsyncMock, patch

# Ensure the database paths are mocked to a temporary file BEFORE importing anything that might initialize connection pools
from spirit.database import db_manager

class TestDeckOperations(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        cls.db_patcher = patch('spirit.database.connection.DB_PATH', cls.db_path)
        cls.db_patcher.start()

        # Initialize the test database tables
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
        # We also need to mock or clear any global caches if necessary
        pass

    def test_database_deck_lifecycle(self):
        """Verifies player_data save_deck, get_decks_by_account_id, and delete_deck flow."""
        from spirit.database.player_data import save_deck, get_decks_by_account_id, delete_deck

        account_id = "test-acc-123"
        deck_id = str(uuid.uuid4())
        deck_name = "Lightning Strike"
        deck_data = {
            "deckID": deck_id,
            "deckName": deck_name,
            "cards": []
        }

        # 1. Save the deck
        success = save_deck(account_id, deck_id, deck_name, deck_data, is_avatar=False)
        self.assertTrue(success)

        # 2. Get the decks and verify it exists
        decks = get_decks_by_account_id(account_id, is_avatar=False)
        self.assertEqual(len(decks), 1)
        self.assertEqual(decks[0]["id"], deck_id)
        self.assertEqual(decks[0]["name"], deck_name)
        self.assertEqual(decks[0]["deck_data"]["deckID"], deck_id)

        # 3. Delete the deck
        del_success = delete_deck(account_id, deck_id)
        self.assertTrue(del_success)

        # 4. Get the decks and verify it is gone
        decks_after = get_decks_by_account_id(account_id, is_avatar=False)
        self.assertEqual(len(decks_after), 0)

    def test_player_model_deck_deletion(self):
        """Verifies Player model's local state synchronization after deck deletion."""
        from spirit.game.models.player import Player

        account_data = {
            "account_id": "player-acc-456",
            "username": "tester",
            "screen_name": "Tester"
        }

        # We construct player after DB has been set up
        player = Player(account_data)

        deck_id = str(uuid.uuid4())
        deck_dict = {
            "deckID": deck_id,
            "deckName": "Water Splash"
        }

        # Save deck through player
        player.save_deck_data(deck_dict, is_avatar=False)
        self.assertEqual(len(player.decks), 1)
        self.assertEqual(player.decks[0]["id"], deck_id)

        # Delete deck through player
        player.delete_deck_data(deck_id, is_avatar=False)
        self.assertEqual(len(player.decks), 0)

    async def test_handler_cake_delete_deck(self):
        """Verifies handle_cake_delete_deck correctly deletes a deck and sends DeckDeleted response."""
        from spirit.packets.handlers.data_sync import DataSyncHandler
        from spirit.game.models.player import Player
        from spirit.network.message_names import OutboundMsg, InboundMsg
        from spirit.network.protocol import WargFlags

        # Setup mock client
        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 12345)
        
        # Setup player on client
        account_data = {
            "account_id": "player-acc-789",
            "username": "handler_tester",
            "screen_name": "HandlerTester"
        }
        player = Player(account_data)
        mock_client.player = player

        # Save a deck to ensure we can delete it
        deck_id = str(uuid.uuid4())
        deck_dict = {
            "deckID": deck_id,
            "deckName": "Fire Blast"
        }
        player.save_deck_data(deck_dict, is_avatar=False)
        self.assertEqual(len(player.decks), 1)

        # Instantiate handler
        handler = DataSyncHandler(mock_client)

        # Invoke handle_cake_delete_deck
        message = {
            "deckID": deck_id
        }
        await handler.handle_cake_delete_deck(message, request_id=101, flags=WargFlags.CLEAR)

        # Verify database / local state deletion
        self.assertEqual(len(player.decks), 0)

        # Verify response packet was sent
        mock_client.send_packet.assert_called_once()
        sent_args = mock_client.send_packet.call_args[0]
        sent_res = sent_args[0]
        sent_rid = sent_args[1]
        sent_flags = mock_client.send_packet.call_args[1].get("flags")

        self.assertEqual(sent_res["messageName"], OutboundMsg.DECK_DELETED.value)
        self.assertEqual(sent_res["deckID"], deck_id)
        self.assertEqual(sent_rid, 101)
        self.assertEqual(sent_flags, WargFlags.CLEAR)

    async def test_handler_cake_save_deck(self):
        """Verifies handle_cake_save_deck correctly saves a deck, populates validationResults, and sends DeckSaved response."""
        from spirit.packets.handlers.data_sync import DataSyncHandler
        from spirit.game.models.player import Player
        from spirit.network.message_names import OutboundMsg, InboundMsg
        from spirit.network.protocol import WargFlags

        # Setup mock client
        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 12345)
        
        # Setup player on client
        account_data = {
            "account_id": "player-acc-save-999",
            "username": "save_tester",
            "screen_name": "SaveTester"
        }
        player = Player(account_data)
        mock_client.player = player

        # Instantiate handler
        handler = DataSyncHandler(mock_client)

        # Incoming save request with attributes
        deck_id = str(uuid.uuid4())
        message = {
            "deck": {
                "deckID": deck_id,
                "deckName": "Leaf Storm",
                "attributes": [
                    {"name": 200670, "value": "some-coin-guid"}
                ],
                "piles": {
                    "deck": []
                }
            }
        }

        # Invoke handle_cake_save_deck
        await handler.handle_cake_save_deck(message, request_id=102, flags=WargFlags.CLEAR)

        # Verify DB / local state updated
        self.assertEqual(len(player.decks), 1)
        self.assertEqual(player.decks[0]["id"], deck_id)
        self.assertEqual(player.decks[0]["name"], "Leaf Storm")

        # Verify response packet was sent
        mock_client.send_packet.assert_called_once()
        sent_args = mock_client.send_packet.call_args[0]
        sent_res = sent_args[0]
        sent_rid = sent_args[1]
        sent_flags = mock_client.send_packet.call_args[1].get("flags")

        self.assertEqual(sent_res["messageName"], OutboundMsg.DECK_SAVED.value)
        self.assertEqual(sent_res["deckID"], deck_id)
        self.assertEqual(sent_res["deck"]["deckName"], "Leaf Storm")
        
        # Core checks for validationResults
        self.assertIn("validationResults", sent_res)
        self.assertEqual(len(sent_res["validationResults"]), 3)
        self.assertEqual(sent_res["validationResults"][0]["formatName"], "Modified")
        self.assertTrue(sent_res["validationResults"][0]["valid"])

        self.assertEqual(sent_rid, 102)
        self.assertEqual(sent_flags, WargFlags.CLEAR)

    async def test_handler_validate_all_decks(self):
        """Verifies handle_validate_all_decks returns correctly structured validation results for player's decks."""
        from spirit.packets.handlers.data_sync import DataSyncHandler
        from spirit.game.models.player import Player
        from spirit.network.message_names import OutboundMsg, InboundMsg
        from spirit.network.protocol import WargFlags

        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 12345)
        
        player = Player({
            "account_id": "val-all-acc-111",
            "username": "val_all_tester",
            "screen_name": "ValAllTester"
        })
        mock_client.player = player

        # Pre-populate a deck
        deck_id = str(uuid.uuid4())
        player.save_deck_data({"deckID": deck_id, "deckName": "Val Deck"}, is_avatar=False)

        handler = DataSyncHandler(mock_client)
        
        # Invoke ValidateAllDecks
        formats = ["6402e830-7fed-4cd1-b172-2a320047c2bb", "98c83df9-ec82-4193-84a8-104115ce4e25"]
        message = {"formats": formats}
        await handler.handle_validate_all_decks(message, request_id=103, flags=WargFlags.CLEAR)

        mock_client.send_packet.assert_called_once()
        sent_res = mock_client.send_packet.call_args[0][0]
        self.assertEqual(sent_res["messageName"], OutboundMsg.DECKS_VALIDATED.value)
        self.assertIn("results", sent_res)
        self.assertEqual(len(sent_res["results"]), 2) # 1 deck * 2 formats
        self.assertEqual(sent_res["results"][0]["deckID"], deck_id)
        self.assertEqual(sent_res["results"][0]["formatName"], "Modified")
        self.assertTrue(sent_res["results"][0]["valid"])

    async def test_handler_validate_decks(self):
        """Verifies handle_validate_decks returns correctly structured validation results for specified decks."""
        from spirit.packets.handlers.data_sync import DataSyncHandler
        from spirit.network.message_names import OutboundMsg, InboundMsg
        from spirit.network.protocol import WargFlags

        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 12345)

        handler = DataSyncHandler(mock_client)
        
        # Invoke ValidateDecks
        deck_id = str(uuid.uuid4())
        message = {
            "decks": [{"deckID": deck_id}],
            "formats": ["6a1dec5a-34db-4cee-a503-4ee759304135"]
        }
        await handler.handle_validate_decks(message, request_id=104, flags=WargFlags.CLEAR)

        mock_client.send_packet.assert_called_once()
        sent_res = mock_client.send_packet.call_args[0][0]
        self.assertEqual(sent_res["messageName"], OutboundMsg.DECKS_VALIDATED.value)
        self.assertEqual(len(sent_res["results"]), 1)
        self.assertEqual(sent_res["results"][0]["deckID"], deck_id)
        self.assertEqual(sent_res["results"][0]["formatName"], "Unlimited")
        self.assertTrue(sent_res["results"][0]["valid"])

    def test_dynamic_validation_attribute_injection(self):
        """Verifies that player deck retrieval dynamically injects the VALID_FORMATS attribute (10860) with standard format names."""
        from spirit.game.models.player import Player
        from spirit.game.attributes import AttrID

        player = Player({
            "account_id": "val-inject-acc-321",
            "username": "inject_tester",
            "screen_name": "InjectTester"
        })

        deck_id = str(uuid.uuid4())
        deck_dict = {
            "deckID": deck_id,
            "deckName": "Lightning Speed",
            "attributes": [
                {"name": AttrID.SELECTED_COIN.value, "value": "some-coin-id"}
            ],
            "piles": {"deck": []}
        }

        # Save to player
        player.save_deck_data(deck_dict, is_avatar=False)

        # Retrieve player's deck data
        decks_data = player.get_decks_data()
        self.assertEqual(len(decks_data["decks"]), 1)

        retrieved_deck = decks_data["decks"][0]
        attributes = retrieved_deck.get("attributes", [])
        
        # Verify the VALID_FORMATS (10860) attribute was injected and contains standard format names
        format_attr = next((attr for attr in attributes if attr.get("name") == AttrID.VALID_FORMATS.value), None)
        self.assertIsNotNone(format_attr)
        self.assertEqual(format_attr["value"], ["Modified", "Expanded", "Unlimited", "Legacy"])

        # Ensure other attributes are preserved
        coin_attr = next((attr for attr in attributes if attr.get("name") == AttrID.SELECTED_COIN.value), None)
        self.assertIsNotNone(coin_attr)
        self.assertEqual(coin_attr["value"], "some-coin-id")

if __name__ == '__main__':
    unittest.main()
