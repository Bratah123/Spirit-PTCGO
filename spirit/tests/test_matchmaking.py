import unittest
import asyncio
from spirit.game.session.manager import GameSessionManager
from spirit.network.message_names import OutboundMsg

class MockPlayer:
    def __init__(self, account_id: str, username: str):
        self.account_id = account_id
        self.username = username

class MockServer:
    def __init__(self):
        self.clients = []


class MockClientHandler:
    def __init__(self, account_id: str, username: str, server=None):
        self.player = MockPlayer(account_id, username)
        self.sent_packets = []
        self.addr = ("127.0.0.1", 12345)
        self.server = server or MockServer()
        self.server.clients.append(self)

    async def send_packet(self, response_body, request_id, flags=0):
        self.sent_packets.append(response_body)


class TestMatchmakingFlows(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # Reset the GameSessionManager singleton state before each test
        self.manager = GameSessionManager()
        self.manager.queues = {}
        self.manager.pending_pairings = {}
        self.manager.active_sessions = {}
        self.manager.auto_confirm_ready = False

    def test_singleton_behavior(self):
        manager2 = GameSessionManager()
        self.assertIs(self.manager, manager2)

    async def test_multiplayer_queue_matchmaking(self):
        client1 = MockClientHandler("player-1", "Ash")
        client2 = MockClientHandler("player-2", "Gary")

        deck1 = {"deckID": "deck-1", "deckName": "Charizard Fire"}
        deck2 = {"deckID": "deck-2", "deckName": "Blastoise Water"}

        # 1. Player 1 enters standard queue
        await self.manager.add_to_queue(client1, "Standard", deck1, {})
        
        # Verify Player 1 received MatchQueueEntered
        self.assertEqual(len(client1.sent_packets), 1)
        self.assertEqual(client1.sent_packets[0]["messageName"], OutboundMsg.MATCH_QUEUE_ENTERED.value)
        self.assertIn("Standard", self.manager.queues)
        self.assertEqual(len(self.manager.queues["Standard"]), 1)

        # 2. Player 2 enters standard queue (triggers pair matching)
        await self.manager.add_to_queue(client2, "Standard", deck2, {})

        # Wait for the ConfirmReadyForMatch 1.5s delay timer to fire
        await asyncio.sleep(1.6)

        # Queue should now be empty
        self.assertEqual(len(self.manager.queues["Standard"]), 0)
        # Should have created 1 pending pairing
        self.assertEqual(len(self.manager.pending_pairings), 1)
        
        game_id = list(self.manager.pending_pairings.keys())[0]
        pairing = self.manager.pending_pairings[game_id]
        
        self.assertFalse(pairing["is_solo"])
        self.assertEqual(pairing["queue_name"], "Standard")

        # Verify MatchQueueEntered and ConfirmReadyForMatch sent
        self.assertEqual(len(client1.sent_packets), 2)
        self.assertEqual(len(client2.sent_packets), 2)

        p1_confirm = client1.sent_packets[1]
        p2_confirm = client2.sent_packets[1]

        self.assertEqual(client2.sent_packets[0]["messageName"], OutboundMsg.MATCH_QUEUE_ENTERED.value)
        self.assertEqual(p1_confirm["messageName"], OutboundMsg.CONFIRM_READY_FOR_MATCH.value)
        self.assertEqual(p1_confirm["gameID"], game_id)
        self.assertEqual(p2_confirm["messageName"], OutboundMsg.CONFIRM_READY_FOR_MATCH.value)
        self.assertEqual(p2_confirm["gameID"], game_id)

        # 3. Ready check confirmation
        await self.manager.confirm_ready(client1, game_id)
        # Game should not start yet as Player 2 is not ready
        self.assertEqual(len(self.manager.active_sessions), 0)
        self.assertTrue(self.manager.pending_pairings[game_id]["players"]["player-1"]["ready"])
        self.assertFalse(self.manager.pending_pairings[game_id]["players"]["player-2"]["ready"])

        await self.manager.confirm_ready(client2, game_id)
        # Both ready! Should clear pending and move to active sessions
        self.assertEqual(len(self.manager.pending_pairings), 0)
        self.assertEqual(len(self.manager.active_sessions), 1)

        # Yield to event loop to allow asyncio.create_task(session.start()) to run
        await asyncio.sleep(0.05)

        # Verify MatchFound sent to both
        self.assertEqual(len(client1.sent_packets), 3)
        self.assertEqual(len(client2.sent_packets), 3)

        self.assertEqual(client1.sent_packets[2]["messageName"], OutboundMsg.MATCH_FOUND.value)
        self.assertEqual(client2.sent_packets[2]["messageName"], OutboundMsg.MATCH_FOUND.value)

    async def test_single_player_ai_matchmaking(self):
        client = MockClientHandler("player-1", "Ash")
        deck = {"deckID": "deck-1", "deckName": "Charizard Fire"}

        # 1. Start solo match against AI
        await self.manager.start_solo_match(client, deck, "easy_ai_bot", {})

        # Should be a pending pairing
        self.assertEqual(len(self.manager.pending_pairings), 1)
        game_id = list(self.manager.pending_pairings.keys())[0]
        pairing = self.manager.pending_pairings[game_id]

        self.assertTrue(pairing["is_solo"])
        self.assertEqual(pairing["solitaire_id"], "easy_ai_bot")
        
        # Player 1 is not ready, AI is instantly ready
        self.assertFalse(pairing["players"]["player-1"]["ready"])
        self.assertTrue(pairing["players"]["mock_ai_bot"]["ready"])

        # Verify ConfirmReadyForMatch sent
        self.assertEqual(len(client.sent_packets), 1)
        self.assertEqual(client.sent_packets[0]["messageName"], OutboundMsg.CONFIRM_READY_FOR_MATCH.value)

        # 2. Confirm ready from player 1
        await self.manager.confirm_ready(client, game_id)

        # Since AI was already ready, this should start the session immediately
        self.assertEqual(len(self.manager.pending_pairings), 0)
        self.assertEqual(len(self.manager.active_sessions), 1)

        # Yield to event loop to allow asyncio.create_task(session.start()) to run
        await asyncio.sleep(0.05)

        # Verify MatchFound is sent
        self.assertEqual(len(client.sent_packets), 2)
        self.assertEqual(client.sent_packets[1]["messageName"], OutboundMsg.MATCH_FOUND.value)

    async def test_cancel_match_request(self):
        client = MockClientHandler("player-1", "Ash")
        deck = {"deckID": "deck-1"}

        # 1. Enter queue
        await self.manager.add_to_queue(client, "Standard", deck, {})
        self.assertEqual(len(self.manager.queues["Standard"]), 1)

        # 2. Cancel match request
        await self.manager.remove_from_queue(client, send_left_packet=True)
        self.assertEqual(len(self.manager.queues["Standard"]), 0)

        # Verify MatchQueueLeft is sent
        self.assertEqual(len(client.sent_packets), 2)
        self.assertEqual(client.sent_packets[1]["messageName"], OutboundMsg.MATCH_QUEUE_LEFT.value)

    async def test_matchmaking_deck_cosmetic_resolution(self):
        from unittest.mock import MagicMock
        from spirit.game.models.player import Player
        from spirit.packets.handlers.matchmaking import MatchmakingHandler
        from spirit.game.attributes import AttrID

        # Create mock client and player
        client = MockClientHandler("player-cosmetic-1", "Satoshi")
        player = Player({
            "account_id": "player-cosmetic-1",
            "username": "satoshi",
            "screen_name": "Satoshi"
        })
        client.player = player

        # Save a customized deck into player's local list
        custom_deck_id = "custom-deck-123"
        custom_deck = {
            "deckID": custom_deck_id,
            "deckName": "Cosmetic Test Deck",
            "attributes": [
                {"name": AttrID.SELECTED_COIN.value, "value": "custom-coin-guid"},
                {"name": AttrID.SELECTED_SLEEVE.value, "value": ["custom-sleeve-guid"]},
                {"name": AttrID.SELECTED_DECK_BOX.value, "value": "custom-deckbox-guid"}
            ],
            "piles": {"deck": []}
        }
        player.save_deck_data(custom_deck)

        # Instantiate matchmaking handler
        handler = MatchmakingHandler(client)

        # 1. Verify resolution of full deck data with string and list cosmetic values
        resolved_deck = handler._resolve_full_deck({"deckID": custom_deck_id})
        self.assertEqual(resolved_deck["deckName"], "Cosmetic Test Deck")
        
        # Test cosmetic values on NetworkPlayer instantiated with resolved deck
        from spirit.game.session.network_player import NetworkPlayer
        np = NetworkPlayer(
            client_handler=client,
            deck_data=resolved_deck
        )
        self.assertEqual(np.coin_id, "custom-coin-guid")     # String value resolution
        self.assertEqual(np.sleeve_id, "custom-sleeve-guid") # List value resolution
        self.assertEqual(np.deckbox_id, "custom-deckbox-guid")

        # 2. Verify fallback default cosmetic values when they are missing or empty
        empty_deck = {
            "deckID": "empty-deck",
            "deckName": "Empty Cosmetic Deck",
            "attributes": [],
            "piles": {"deck": []}
        }
        np_empty = NetworkPlayer(
            client_handler=client,
            deck_data=empty_deck
        )
        # Verify fallback deckbox GUID is the safe Basic Deck Box GUID
        self.assertEqual(np_empty.deckbox_id, "e129b0d3-b934-4fbd-b021-545106c75694")
        self.assertEqual(np_empty.coin_id, "B9A4EA96-949E-11E1-890F-EFB676C7909C")
        self.assertEqual(np_empty.sleeve_id, "e079c0d3-b934-4fbd-b021-545106c75693")

    async def test_active_session_cleanup_on_matchmaking(self):
        client = MockClientHandler("player-cleanup-1", "Satoshi")
        deck = {"deckID": "deck-1"}

        # 1. Start a solo match to populate an active session
        await self.manager.start_solo_match(client, deck, "easy_ai_bot", {})
        # Confirm ready to move to active sessions
        game_id = list(self.manager.pending_pairings.keys())[0]
        await self.manager.confirm_ready(client, game_id)
        
        # Verify session is active
        self.assertEqual(len(self.manager.active_sessions), 1)

        # 2. Add to queue should automatically trigger removal and cleanup of the old session
        await self.manager.add_to_queue(client, "Standard", deck, {})
        self.assertEqual(len(self.manager.active_sessions), 0)


class TestFriendChallenges(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.manager = GameSessionManager()
        self.manager.queues = {}
        self.manager.pending_pairings = {}
        self.manager.active_sessions = {}
        self.manager.pending_challenges = {}
        self.manager.auto_confirm_ready = False

        self.server = MockServer()
        self.challenger = MockClientHandler("player-1", "Ash", server=self.server)
        self.opponent = MockClientHandler("player-2", "Gary", server=self.server)

    def _last(self, client):
        return client.sent_packets[-1]

    async def test_challenge_accept_starts_game(self):
        deck1 = {"deckID": "deck-1"}
        deck2 = {"deckID": "deck-2"}
        options = {"QueueType": "Standard", "TimersEnabled": "True"}

        await self.manager.create_challenge(self.challenger, "player-2", deck1, options)

        sent = self._last(self.challenger)
        self.assertEqual(sent["messageName"], OutboundMsg.MATCH_REQUEST_SENT.value)
        self.assertEqual(sent["opponentID"], "player-2")
        path = sent["path"]
        self.assertIn(path, self.manager.pending_challenges)

        requested = self._last(self.opponent)
        self.assertEqual(requested["messageName"], OutboundMsg.MATCH_REQUESTED.value)
        self.assertEqual(requested["path"], path)
        self.assertEqual(requested["opponentID"], "player-1")
        self.assertEqual(requested["matchOptions"], options)

        await self.manager.accept_challenge(self.opponent, path, deck2)

        accepted = self._last(self.opponent)
        self.assertEqual(accepted["messageName"], OutboundMsg.MATCH_REQUEST_SENT.value)
        self.assertEqual(accepted["opponentID"], "player-1")

        self.assertEqual(len(self.manager.pending_challenges), 0)
        self.assertEqual(len(self.manager.pending_pairings), 1)
        game_id, pairing = next(iter(self.manager.pending_pairings.items()))
        self.assertEqual(pairing["queue_name"], "Friend")
        self.assertEqual(pairing["players"]["player-1"]["deck"], deck1)
        self.assertEqual(pairing["players"]["player-2"]["deck"], deck2)

        # Ready check fires after the 1.5s settle delay
        await asyncio.sleep(1.6)
        self.assertEqual(self._last(self.challenger)["messageName"], OutboundMsg.CONFIRM_READY_FOR_MATCH.value)
        self.assertEqual(self._last(self.opponent)["messageName"], OutboundMsg.CONFIRM_READY_FOR_MATCH.value)

        await self.manager.confirm_ready(self.challenger, game_id)
        await self.manager.confirm_ready(self.opponent, game_id)
        await asyncio.sleep(0.05)

        self.assertEqual(len(self.manager.active_sessions), 1)
        self.assertEqual(self._last(self.challenger)["messageName"], OutboundMsg.MATCH_FOUND.value)
        self.assertEqual(self._last(self.opponent)["messageName"], OutboundMsg.MATCH_FOUND.value)

    async def test_challenge_offline_opponent_fails(self):
        await self.manager.create_challenge(self.challenger, "player-offline", {}, {})

        failed = self._last(self.challenger)
        self.assertEqual(failed["messageName"], OutboundMsg.MATCH_REQUEST_WITH_SPECIFIC_CLIENT_FAILED.value)
        self.assertIn("id", failed["failureType"])
        self.assertEqual(len(self.manager.pending_challenges), 0)

    async def test_challenge_reject_notifies_challenger(self):
        await self.manager.create_challenge(self.challenger, "player-2", {}, {})
        path = self._last(self.challenger)["path"]

        await self.manager.reject_challenge(self.opponent, path)

        rejected = self._last(self.challenger)
        self.assertEqual(rejected["messageName"], OutboundMsg.MATCH_REQUEST_REJECTED.value)
        self.assertEqual(rejected["path"], path)
        self.assertEqual(rejected["failureType"], "Rejected")
        self.assertEqual(len(self.manager.pending_challenges), 0)

    async def test_challenge_cancel_notifies_both(self):
        await self.manager.create_challenge(self.challenger, "player-2", {}, {})
        path = self._last(self.challenger)["path"]

        await self.manager.cancel_challenge(self.challenger, path)

        self.assertEqual(self._last(self.challenger)["messageName"], OutboundMsg.MATCH_REQUEST_CANCELLED.value)
        cancelled = self._last(self.opponent)
        self.assertEqual(cancelled["messageName"], OutboundMsg.MATCH_REQUEST_CANCELLED.value)
        self.assertEqual(cancelled["path"], path)
        self.assertEqual(len(self.manager.pending_challenges), 0)

    async def test_accept_stale_path_fails(self):
        await self.manager.accept_challenge(self.opponent, "challenge_gone", {})
        failed = self._last(self.opponent)
        self.assertEqual(failed["messageName"], OutboundMsg.MATCH_REQUEST_WITH_SPECIFIC_CLIENT_FAILED.value)

    async def test_disconnect_cancels_pending_challenge(self):
        await self.manager.create_challenge(self.challenger, "player-2", {}, {})
        path = self._last(self.challenger)["path"]

        await self.manager.remove_challenges_for_client(self.challenger, notify_self=False)

        cancelled = self._last(self.opponent)
        self.assertEqual(cancelled["messageName"], OutboundMsg.MATCH_REQUEST_CANCELLED.value)
        self.assertEqual(cancelled["path"], path)
        self.assertEqual(len(self.manager.pending_challenges), 0)

    async def test_new_challenge_replaces_previous(self):
        third = MockClientHandler("player-3", "Misty", server=self.server)
        await self.manager.create_challenge(self.challenger, "player-2", {}, {})
        first_path = self._last(self.challenger)["path"]

        await self.manager.create_challenge(self.challenger, "player-3", {}, {})

        self.assertEqual(len(self.manager.pending_challenges), 1)
        self.assertNotIn(first_path, self.manager.pending_challenges)
        # The first opponent's dialog is unwound with a cancellation
        cancelled = self.opponent.sent_packets[-1]
        self.assertEqual(cancelled["messageName"], OutboundMsg.MATCH_REQUEST_CANCELLED.value)
        self.assertEqual(cancelled["path"], first_path)
        self.assertEqual(self._last(third)["messageName"], OutboundMsg.MATCH_REQUESTED.value)


if __name__ == "__main__":
    unittest.main()
