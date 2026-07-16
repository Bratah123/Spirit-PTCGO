import asyncio
import unittest
from types import SimpleNamespace

from spirit.game.session.constants import (
    ACTION_COUNTDOWN_DURATION_MS,
    ACTION_INACTIVITY_DURATION_MS,
    ACTION_TIMEOUT_MS,
    GamePhase,
)
from spirit.game.session.game_session import GameSession
from spirit.game.session.network_player import NetworkPlayer
from spirit.network.message_names import OutboundMsg


class RecordingNetworkPlayer(NetworkPlayer):
    def __init__(self, account_id):
        self.account_id = account_id
        self.username = account_id
        self.deck_data = {}
        self.entity_id = ""
        self.client_handler = SimpleNamespace(running=True)
        self.pending_choice_future = None
        self._pending_offer = None
        self.packets = []

    async def send_packet(self, name, value, flags=0):
        self.packets.append((name, value, flags))


class ActionTimerTests(unittest.IsolatedAsyncioTestCase):
    def make_session(self):
        session = object.__new__(GameSession)
        session.game_id = "game-1"
        session.game_phase = GamePhase.TURN_LOOP
        session._connection_resumed = asyncio.Event()
        session._connection_resumed.set()
        session._connection_pause_event = asyncio.Event()
        session._disconnected = set()
        session._reconnecting = set()
        session._offers_to_restore = set()
        session._restoring_offers = set()
        session._wire_lock = asyncio.Lock()
        session._state_checkpoint = asyncio.Event()
        session._state_checkpoint.set()
        session._state_unit_tasks = {}
        session._prompt_checkpoint_tasks = set()
        session.choreography_pauses = False
        return session

    async def wait_for_packets(self, player, count):
        async def wait_until_ready():
            while len(player.packets) < count:
                await asyncio.sleep(0)

        await asyncio.wait_for(wait_until_ready(), timeout=1)

    def test_payload_hides_the_first_fifteen_seconds(self):
        payload = GameSession._idle_timer_payload("player-1", ACTION_TIMEOUT_MS)
        session = self.make_session()
        session._selection_counters = {}
        offer = session._main_offer_value("player-1", [])

        self.assertEqual(
            payload,
            {
                "playerID": "player-1",
                "inactivityDuration": ACTION_INACTIVITY_DURATION_MS,
                "endTurnDuration": ACTION_COUNTDOWN_DURATION_MS,
                "forced": False,
            },
        )
        self.assertEqual(offer["offerLength"], ACTION_TIMEOUT_MS)
        self.assertEqual(
            GameSession._idle_timer_payload("player-1", 0),
            {
                "playerID": "player-1",
                "inactivityDuration": 0,
                "endTurnDuration": 0,
                "forced": False,
            },
        )

    async def test_reply_stops_the_timer(self):
        session = self.make_session()
        player = RecordingNetworkPlayer("player-1")
        session.players = {player.account_id: player}
        prompt = asyncio.create_task(
            session.prompt_selection_message(
                player,
                OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                {"counter": 7},
                expected_counter=7,
                idle_timeout_ms=ACTION_TIMEOUT_MS,
            )
        )
        await self.wait_for_packets(player, 2)

        await session.receive_player_action(
            player.account_id, {"selection": None, "counter": 7}
        )
        reply = await asyncio.wait_for(prompt, timeout=1)

        self.assertEqual(reply, {"selection": None, "counter": 7})
        self.assertEqual(
            [name for name, _, _ in player.packets],
            [
                OutboundMsg.SEQUENCE_MESSAGE.value,
                OutboundMsg.SET_IDLE_TIMER.value,
                OutboundMsg.SET_IDLE_TIMER.value,
            ],
        )
        self.assertEqual(player.packets[-1][1]["inactivityDuration"], 0)
        self.assertEqual(player.packets[-1][1]["endTurnDuration"], 0)

    async def test_timeout_force_finishes_the_offer(self):
        session = self.make_session()
        player = RecordingNetworkPlayer("player-1")
        session.players = {player.account_id: player}

        reply = await session.prompt_selection_message(
            player,
            OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
            {"counter": 9},
            expected_counter=9,
            idle_timeout_ms=10,
        )

        self.assertTrue(reply["_timed_out"])
        self.assertIsNone(reply["selection"])
        self.assertEqual(
            [name for name, _, _ in player.packets],
            [
                OutboundMsg.SEQUENCE_MESSAGE.value,
                OutboundMsg.SET_IDLE_TIMER.value,
                OutboundMsg.SET_IDLE_TIMER.value,
                OutboundMsg.FORCE_SELECTION_FINISHED.value,
            ],
        )
        self.assertIsNone(player.pending_choice_future)
        self.assertIsNone(player._pending_offer)

    async def test_disconnect_pauses_the_authoritative_timeout(self):
        session = self.make_session()
        player = RecordingNetworkPlayer("player-1")
        session.players = {player.account_id: player}
        prompt = asyncio.create_task(
            session.prompt_selection_message(
                player,
                OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                {"counter": 11},
                expected_counter=11,
                idle_timeout_ms=200,
            )
        )
        await self.wait_for_packets(player, 2)

        session._connection_resumed.clear()
        session._connection_pause_event.set()
        await self.wait_for_packets(player, 3)
        await asyncio.sleep(0.25)
        self.assertFalse(prompt.done())
        self.assertFalse(session._offers_to_restore)

        session._connection_pause_event = asyncio.Event()
        session._connection_resumed.set()
        await self.wait_for_packets(player, 4)
        await session.receive_player_action(
            player.account_id, {"selection": None, "counter": 11}
        )
        reply = await asyncio.wait_for(prompt, timeout=1)

        self.assertEqual(reply, {"selection": None, "counter": 11})
        timer_packets = [
            value for name, value, _ in player.packets
            if name == OutboundMsg.SET_IDLE_TIMER.value
        ]
        self.assertEqual(len(timer_packets), 4)
        self.assertEqual(timer_packets[1]["endTurnDuration"], 0)
        self.assertGreater(timer_packets[2]["endTurnDuration"], 0)
        self.assertEqual(timer_packets[3]["endTurnDuration"], 0)


if __name__ == "__main__":
    unittest.main()
