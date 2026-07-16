import asyncio
import unittest
from types import SimpleNamespace

from spirit.game.session.constants import (
    GamePhase,
    FORCE_SELECTION_SETTLE_SECONDS,
    RECONNECT_GRACE_SECONDS,
)
from spirit.game.session.game_session import GameSession
from spirit.game.session.network_player import NetworkPlayer
from spirit.network.message_names import OutboundMsg


class RecordingNetworkPlayer(NetworkPlayer):
    def __init__(self, account_id, connected=True):
        self.account_id = account_id
        self.username = account_id
        self.deck_data = {}
        self.entity_id = ""
        self.client_handler = SimpleNamespace(running=True) if connected else None
        self.pending_choice_future = None
        self._pending_offer = None
        self.packets = []

    async def send_packet(self, name, value, flags=0):
        self.packets.append((name, value, flags))


class DelayedSequencePlayer(RecordingNetworkPlayer):
    def __init__(self, account_id):
        super().__init__(account_id)
        self.sequence_started = asyncio.Event()
        self.release_sequence = asyncio.Event()

    async def send_packet(self, name, value, flags=0):
        self.packets.append((name, value, flags))
        nested_name = value.get("msg", {}).get("name") if isinstance(value, dict) else None
        if (name == OutboundMsg.SEQUENCE_MESSAGE.value
                and nested_name == OutboundMsg.START_SEQUENCE.value
                and not self.sequence_started.is_set()):
            self.sequence_started.set()
            await self.release_sequence.wait()


class ConnectionNoticeTests(unittest.IsolatedAsyncioTestCase):
    def make_session(self):
        session = object.__new__(GameSession)
        session.game_id = "game-1"
        session.game_phase = GamePhase.TURN_LOOP
        session._reconnecting = set()
        session._disconnected = set()
        session._connection_resumed = asyncio.Event()
        session._connection_resumed.set()
        session._connection_pause_event = asyncio.Event()
        session._resync_epoch = 0
        session._resync_players = set()
        session._resync_ready = set()
        session._resync_inflight = {}
        session._offers_to_restore = set()
        session._restoring_offers = set()
        session._pause_prompts = {}
        session._wire_lock = asyncio.Lock()
        session._last_sequence_sent_at = 0.0
        session._state_checkpoint = asyncio.Event()
        session._state_checkpoint.set()
        session._state_unit_tasks = {}
        session._prompt_checkpoint_tasks = set()
        session._grace_tasks = {}
        session._background_tasks = set()
        session.ready_players = set()
        session._state_dispatched = True
        session.choreography_pauses = False
        session._build_match_found_payload = lambda reconnecting=False: {
            "gameID": session.game_id,
            "players": list(session.players),
            "gameOptions": {"Reconnecting": "true"} if reconnecting else {},
        }
        return session

    async def settle_notices(self, session):
        grace = set(session._grace_tasks.values())
        notices = [
            task for task in session._background_tasks
            if task not in grace and not task.done()
        ]
        if notices:
            await asyncio.gather(*notices)

    async def cleanup_session(self, session):
        for task in list(session._background_tasks):
            if not task.done():
                task.cancel()
        if session._background_tasks:
            await asyncio.gather(*session._background_tasks, return_exceptions=True)

    async def test_disconnect_force_ends_only_a_live_offer(self):
        session = self.make_session()
        dropped = RecordingNetworkPlayer("dropped")
        opponent = RecordingNetworkPlayer("opponent")
        future = asyncio.get_running_loop().create_future()
        opponent.pending_choice_future = future
        opponent._pending_offer = (
            OutboundMsg.SEQUENCE_MESSAGE.value,
            {"saved": "real-offer"},
            0,
        )
        session.players = {"dropped": dropped, "opponent": opponent}
        dropped_handler = dropped.client_handler

        await session.on_player_disconnect(
            "dropped", client_handler=dropped_handler
        )
        try:
            await self.settle_notices(session)
            self.assertEqual(
                opponent.packets[0],
                (OutboundMsg.FORCE_SELECTION_FINISHED.value, {}, 0),
            )
            pause_name, pause_payload, pause_flags = opponent.packets[1]
            self.assertEqual(pause_name, OutboundMsg.SEQUENCE_MESSAGE.value)
            self.assertEqual(
                pause_payload["msg"]["name"],
                OutboundMsg.PAUSE_ON_PROMPT_EFFECT.value,
            )
            self.assertEqual(
                pause_payload["msg"]["value"]["prompt"]["id"],
                f"Opponent disconnected. Waiting up to {RECONNECT_GRACE_SECONDS} seconds for them to reconnect.",
            )
            self.assertFalse(pause_payload["msg"]["value"]["doPause"])
            self.assertEqual(pause_flags, 0)
            self.assertFalse(session._connection_resumed.is_set())
            self.assertEqual(session._offers_to_restore, {"opponent"})

            await session.receive_player_action("opponent", {"selection": None})
            self.assertFalse(future.done())
            nested_names = [
                value.get("msg", {}).get("name")
                for name, value, _ in opponent.packets
                if name == OutboundMsg.SEQUENCE_MESSAGE.value
            ]
            self.assertNotIn(
                OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                nested_names,
            )
            self.assertNotIn(
                OutboundMsg.PLAYER_DISCONNECTED.value,
                [name for name, _, _ in opponent.packets],
            )
        finally:
            await self.cleanup_session(session)

    async def test_banner_waits_out_force_selection_and_skips_after_fast_return(self):
        session = self.make_session()
        dropped = RecordingNetworkPlayer("dropped")
        opponent = RecordingNetworkPlayer("opponent")
        future = asyncio.get_running_loop().create_future()
        opponent.pending_choice_future = future
        opponent._pending_offer = (
            OutboundMsg.SEQUENCE_MESSAGE.value,
            {"saved": "real-offer"},
            0,
        )
        session.players = {"dropped": dropped, "opponent": opponent}
        settle_calls = []

        async def fake_settle(seconds):
            settle_calls.append(seconds)
            # Simulate the player returning during the m.d settle window.
            session._disconnected.discard("dropped")

        session.choreo_pause = fake_settle
        await session.on_player_disconnect(
            "dropped", client_handler=dropped.client_handler
        )
        try:
            await self.settle_notices(session)
            self.assertEqual(settle_calls, [FORCE_SELECTION_SETTLE_SECONDS])
            self.assertEqual(
                [name for name, _, _ in opponent.packets],
                [OutboundMsg.FORCE_SELECTION_FINISHED.value],
            )
            self.assertEqual(session._offers_to_restore, {"opponent"})
        finally:
            await self.cleanup_session(session)

    async def test_disconnect_notice_waits_for_authoritative_checkpoint(self):
        session = self.make_session()
        dropped = RecordingNetworkPlayer("dropped")
        opponent = RecordingNetworkPlayer("opponent")
        session.players = {"dropped": dropped, "opponent": opponent}
        session._state_checkpoint.clear()

        await session.on_player_disconnect(
            "dropped", client_handler=dropped.client_handler
        )
        await asyncio.sleep(0)
        try:
            self.assertFalse(opponent.packets)
            session._state_checkpoint.set()
            await self.settle_notices(session)
            self.assertEqual(
                opponent.packets[0][1]["msg"]["name"],
                OutboundMsg.PAUSE_ON_PROMPT_EFFECT.value,
            )
        finally:
            await self.cleanup_session(session)

    async def test_checkpoint_waits_for_every_concurrent_state_branch(self):
        session = self.make_session()
        waiting_ready = asyncio.Event()
        mutating_ready = asyncio.Event()
        finish_waiting = asyncio.Event()
        finish_mutating = asyncio.Event()

        async def waiting_branch():
            session._mark_prompt_checkpoint()
            waiting_ready.set()
            try:
                await finish_waiting.wait()
            finally:
                session._leave_prompt_checkpoint()

        async def mutating_branch():
            mutating_ready.set()
            await finish_mutating.wait()

        waiting_task = asyncio.create_task(
            session._run_state_unit(waiting_branch())
        )
        mutating_task = asyncio.create_task(
            session._run_state_unit(mutating_branch())
        )
        await asyncio.gather(waiting_ready.wait(), mutating_ready.wait())
        try:
            self.assertFalse(session._state_checkpoint.is_set())
            finish_mutating.set()
            await mutating_task
            self.assertTrue(session._state_checkpoint.is_set())
            finish_waiting.set()
            await waiting_task
            self.assertTrue(session._state_checkpoint.is_set())
        finally:
            finish_mutating.set()
            finish_waiting.set()
            await asyncio.gather(
                waiting_task, mutating_task, return_exceptions=True
            )

    async def test_inactive_viewer_gets_banner_without_force_command(self):
        session = self.make_session()
        dropped = RecordingNetworkPlayer("dropped")
        opponent = RecordingNetworkPlayer("opponent")
        session.players = {"dropped": dropped, "opponent": opponent}

        await session.on_player_disconnect(
            "dropped", client_handler=dropped.client_handler
        )
        try:
            await self.settle_notices(session)
            self.assertEqual(len(opponent.packets), 1)
            self.assertEqual(
                opponent.packets[0][1]["msg"]["name"],
                OutboundMsg.PAUSE_ON_PROMPT_EFFECT.value,
            )
        finally:
            await self.cleanup_session(session)

    async def test_disconnect_before_initial_snapshot_rejoins_shared_ready_barrier(self):
        session = self.make_session()
        session._state_dispatched = False
        returning = RecordingNetworkPlayer("returning")
        opponent = RecordingNetworkPlayer("opponent")
        session.players = {"returning": returning, "opponent": opponent}
        gameplay_release = asyncio.Event()

        async def fake_gameplay():
            await gameplay_release.wait()

        async def fake_initial_state(only_player_id=None):
            self.assertIsNone(only_player_id)
            for player in session.players.values():
                await player.send_packet(
                    OutboundMsg.SEQUENCE_MESSAGE.value,
                    {
                        "gameID": session.game_id,
                        "msg": {
                            "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                            "value": {"viewer": player.account_id},
                        },
                    },
                )

        session.run_gameplay_sequence = fake_gameplay
        session.send_serialized_game_state = fake_initial_state
        await session.mark_player_ready(
            "returning", client_handler=returning.client_handler
        )
        self.assertIn("returning", session.ready_players)

        await session.on_player_disconnect(
            "returning", client_handler=returning.client_handler
        )
        await self.settle_notices(session)
        self.assertNotIn("returning", session.ready_players)
        self.assertFalse(opponent.packets)

        await session.mark_player_ready(
            "opponent", client_handler=opponent.client_handler
        )
        handler = SimpleNamespace(running=True)
        await session.reconnect_player(handler, "returning")
        try:
            await session.mark_player_ready("returning", client_handler=handler)
            self.assertTrue(session._state_dispatched)
            self.assertTrue(session._connection_resumed.is_set())
            for player in (returning, opponent):
                snapshots = [
                    value for name, value, _ in player.packets
                    if (name == OutboundMsg.SEQUENCE_MESSAGE.value
                        and value.get("msg", {}).get("name")
                        == OutboundMsg.SERIALIZED_GAME_STATE.value)
                ]
                self.assertEqual(len(snapshots), 1)
            self.assertNotIn(
                OutboundMsg.PAUSE_ON_PROMPT_EFFECT.value,
                [
                    value.get("msg", {}).get("name")
                    for name, value, _ in opponent.packets
                    if name == OutboundMsg.SEQUENCE_MESSAGE.value
                ],
            )
        finally:
            gameplay_release.set()
            await self.cleanup_session(session)

    async def test_disconnect_control_waits_for_complete_reveal_bracket(self):
        session = self.make_session()
        dropped = RecordingNetworkPlayer("dropped")
        opponent = DelayedSequencePlayer("opponent")
        session.players = {"dropped": dropped, "opponent": opponent}
        reveal = session._build_msg(
            OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value,
            {"gameID": session.game_id, "entityID": "supporter", "return": True},
        )
        move = session._build_msg(
            OutboundMsg.ENTITY_MOVED.value,
            {
                "gameID": session.game_id,
                "entityID": "supporter",
                "destinationID": "active-trainer",
                "positionInParent": 0,
            },
        )

        sequence_task = asyncio.create_task(
            session.send_game_sequence([opponent], "PlayCard", [reveal, move])
        )
        await opponent.sequence_started.wait()
        await session.on_player_disconnect(
            "dropped", client_handler=dropped.client_handler
        )
        opponent.release_sequence.set()
        await sequence_task
        try:
            await self.settle_notices(session)
            nested_names = [
                value.get("msg", {}).get("name")
                for name, value, _ in opponent.packets
                if name == OutboundMsg.SEQUENCE_MESSAGE.value
            ]
            self.assertEqual(
                nested_names,
                [
                    OutboundMsg.START_SEQUENCE.value,
                    OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value,
                    OutboundMsg.ENTITY_MOVED.value,
                    OutboundMsg.STOP_SEQUENCE.value,
                    OutboundMsg.PAUSE_ON_PROMPT_EFFECT.value,
                ],
            )
        finally:
            await self.cleanup_session(session)

    async def test_stale_socket_cannot_detach_rebound_player(self):
        session = self.make_session()
        player = RecordingNetworkPlayer("player")
        opponent = RecordingNetworkPlayer("opponent")
        old_handler = player.client_handler
        new_handler = SimpleNamespace(running=True)
        player.client_handler = new_handler
        session.players = {"player": player, "opponent": opponent}

        await session.on_player_disconnect("player", client_handler=old_handler)

        self.assertIs(player.client_handler, new_handler)
        self.assertTrue(session._connection_resumed.is_set())
        self.assertFalse(session._grace_tasks)

    async def test_stale_socket_cannot_answer_current_offer(self):
        session = self.make_session()
        player = RecordingNetworkPlayer("player")
        opponent = RecordingNetworkPlayer("opponent")
        old_handler = player.client_handler
        new_handler = SimpleNamespace(running=True)
        player.client_handler = new_handler
        player.pending_choice_future = asyncio.get_running_loop().create_future()
        session.players = {"player": player, "opponent": opponent}

        await session.receive_player_action(
            "player", {"selection": "stale"}, client_handler=old_handler
        )
        self.assertFalse(player.pending_choice_future.done())

        await session.receive_player_action(
            "player", {"selection": "current"}, client_handler=new_handler
        )
        self.assertEqual(
            player.pending_choice_future.result(), {"selection": "current"}
        )

    async def test_reconnect_rebuilds_only_returning_scene_and_restores_offer(self):
        session = self.make_session()
        returning = RecordingNetworkPlayer("returning")
        opponent = RecordingNetworkPlayer("opponent")
        future = asyncio.get_running_loop().create_future()
        saved_offer = {
            "sequenceID": "00000000-0000-0000-0000-000000000000",
            "gameID": session.game_id,
            "msg": {
                "name": OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                "value": {"gameID": session.game_id, "counter": 9, "forced": False},
            },
        }
        opponent.pending_choice_future = future
        opponent._pending_offer = (
            OutboundMsg.SEQUENCE_MESSAGE.value,
            saved_offer,
            0,
        )
        session.players = {"returning": returning, "opponent": opponent}

        async def fake_state_resync(only_player_id=None):
            player = session.players[only_player_id]
            await player.send_packet(
                OutboundMsg.SEQUENCE_MESSAGE.value,
                {
                    "gameID": session.game_id,
                    "msg": {
                        "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                        "value": {"viewer": only_player_id},
                    },
                },
            )

        session.send_serialized_game_state = fake_state_resync
        old_handler = returning.client_handler
        await session.on_player_disconnect(
            "returning", client_handler=old_handler
        )
        await self.settle_notices(session)
        returning.packets.clear()
        opponent.packets.clear()

        new_handler = SimpleNamespace(running=True)
        await session.reconnect_player(new_handler, "returning")
        try:
            self.assertEqual(session._reconnecting, {"returning"})
            self.assertEqual(returning.packets[0][0], OutboundMsg.MATCH_FOUND.value)
            self.assertEqual(
                returning.packets[0][1]["gameOptions"]["Reconnecting"], "true"
            )
            self.assertFalse(opponent.packets)

            await session.mark_player_ready("returning")

            self.assertTrue(session._connection_resumed.is_set())
            self.assertFalse(session._reconnecting)
            self.assertFalse(session._resync_players)
            self.assertFalse(session._grace_tasks)
            self.assertFalse(future.done())

            returning_nested = [
                value.get("msg", {}).get("name")
                for name, value, _ in returning.packets
                if name == OutboundMsg.SEQUENCE_MESSAGE.value
            ]
            opponent_nested = [
                value.get("msg", {}).get("name")
                for name, value, _ in opponent.packets
                if name == OutboundMsg.SEQUENCE_MESSAGE.value
            ]
            self.assertEqual(
                returning_nested,
                [
                    OutboundMsg.SERIALIZED_GAME_STATE.value,
                    OutboundMsg.CLOSE_PAUSE_ON_PROMPT_EFFECT.value,
                ],
            )
            self.assertEqual(
                opponent_nested,
                [
                    OutboundMsg.CLOSE_PAUSE_ON_PROMPT_EFFECT.value,
                    OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                ],
            )
            self.assertEqual(opponent.packets[-1][1], saved_offer)
            self.assertNotIn(
                OutboundMsg.MATCH_FOUND.value,
                [name for name, _, _ in opponent.packets],
            )
            for player in (returning, opponent):
                packet_names = [name for name, _, _ in player.packets]
                self.assertNotIn(OutboundMsg.PLAYER_RECONNECTED.value, packet_names)
        finally:
            await self.cleanup_session(session)

    async def test_returning_player_receives_its_lost_pending_offer(self):
        session = self.make_session()
        returning = RecordingNetworkPlayer("returning")
        opponent = RecordingNetworkPlayer("opponent")
        future = asyncio.get_running_loop().create_future()
        saved_offer = {
            "gameID": session.game_id,
            "msg": {
                "name": OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                "value": {
                    "gameID": session.game_id,
                    "counter": 12,
                    "startingTimestamp": 1,
                },
            },
        }
        returning.pending_choice_future = future
        returning._pending_offer = (
            OutboundMsg.SEQUENCE_MESSAGE.value,
            saved_offer,
            0,
        )
        session.players = {"returning": returning, "opponent": opponent}

        async def fake_state_resync(only_player_id=None):
            await session.players[only_player_id].send_packet(
                OutboundMsg.SEQUENCE_MESSAGE.value,
                {
                    "gameID": session.game_id,
                    "msg": {
                        "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                        "value": {"viewer": only_player_id},
                    },
                },
            )

        session.send_serialized_game_state = fake_state_resync
        await session.on_player_disconnect(
            "returning", client_handler=returning.client_handler
        )
        await self.settle_notices(session)
        returning.packets.clear()

        handler = SimpleNamespace(running=True)
        await session.reconnect_player(handler, "returning")
        try:
            await session.mark_player_ready("returning", client_handler=handler)
            nested = [
                value.get("msg", {}).get("name")
                for name, value, _ in returning.packets
                if name == OutboundMsg.SEQUENCE_MESSAGE.value
            ]
            self.assertEqual(
                nested,
                [
                    OutboundMsg.SERIALIZED_GAME_STATE.value,
                    OutboundMsg.CLOSE_PAUSE_ON_PROMPT_EFFECT.value,
                    OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                ],
            )
            replayed_offer = returning.packets[-1][1]
            self.assertEqual(replayed_offer["msg"]["value"]["counter"], 12)
            self.assertGreater(
                replayed_offer["msg"]["value"]["startingTimestamp"], 1
            )
            self.assertEqual(saved_offer["msg"]["value"]["startingTimestamp"], 1)
            self.assertFalse(future.done())
        finally:
            await self.cleanup_session(session)

    async def test_fast_reconnect_does_not_duplicate_uncancelled_offer(self):
        session = self.make_session()
        returning = RecordingNetworkPlayer("returning")
        opponent = RecordingNetworkPlayer("opponent")
        future = asyncio.get_running_loop().create_future()
        opponent.pending_choice_future = future
        opponent._pending_offer = (
            OutboundMsg.SEQUENCE_MESSAGE.value,
            {"gameID": session.game_id, "saved": "still-live"},
            0,
        )
        session.players = {"returning": returning, "opponent": opponent}

        async def fake_state_resync(only_player_id=None):
            await session.players[only_player_id].send_packet(
                OutboundMsg.SEQUENCE_MESSAGE.value,
                {
                    "gameID": session.game_id,
                    "msg": {
                        "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                        "value": {"viewer": only_player_id},
                    },
                },
            )

        session.send_serialized_game_state = fake_state_resync
        session._state_checkpoint.clear()
        await session.on_player_disconnect(
            "returning", client_handler=returning.client_handler
        )
        await asyncio.sleep(0)
        handler = SimpleNamespace(running=True)
        await session.reconnect_player(handler, "returning")
        session._state_checkpoint.set()
        try:
            await session.mark_player_ready("returning", client_handler=handler)
            self.assertFalse(session._offers_to_restore)
            self.assertEqual(
                sum(name == OutboundMsg.FORCE_SELECTION_FINISHED.value
                    for name, _, _ in opponent.packets),
                0,
            )
            self.assertEqual(
                sum(value.get("saved") == "still-live"
                    for _, value, _ in opponent.packets),
                0,
            )
            self.assertFalse(future.done())
        finally:
            await self.cleanup_session(session)

    async def test_reconnect_restores_underlying_opponent_wait_prompt(self):
        session = self.make_session()
        returning = RecordingNetworkPlayer("returning")
        opponent = RecordingNetworkPlayer("opponent")
        session.players = {"returning": returning, "opponent": opponent}

        async def fake_state_resync(only_player_id=None):
            await session.players[only_player_id].send_packet(
                OutboundMsg.SEQUENCE_MESSAGE.value,
                {
                    "gameID": session.game_id,
                    "msg": {
                        "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                        "value": {"viewer": only_player_id},
                    },
                },
            )

        session.send_serialized_game_state = fake_state_resync
        underlying = "Opponent is choosing a card."
        await session._send_pause_prompt(opponent, underlying)
        opponent.packets.clear()
        await session.on_player_disconnect(
            "returning", client_handler=returning.client_handler
        )
        await self.settle_notices(session)

        handler = SimpleNamespace(running=True)
        await session.reconnect_player(handler, "returning")
        try:
            await session.mark_player_ready("returning", client_handler=handler)
            nested = [
                value.get("msg", {})
                for name, value, _ in opponent.packets
                if name == OutboundMsg.SEQUENCE_MESSAGE.value
            ]
            self.assertEqual(
                [msg.get("name") for msg in nested[-2:]],
                [
                    OutboundMsg.CLOSE_PAUSE_ON_PROMPT_EFFECT.value,
                    OutboundMsg.PAUSE_ON_PROMPT_EFFECT.value,
                ],
            )
            self.assertEqual(nested[-1]["value"]["prompt"]["id"], underlying)
        finally:
            await self.cleanup_session(session)

    async def test_second_return_does_not_reload_an_already_clean_scene(self):
        session = self.make_session()
        first = RecordingNetworkPlayer("first")
        second = RecordingNetworkPlayer("second")
        session.players = {"first": first, "second": second}

        async def fake_state_resync(only_player_id=None):
            await session.players[only_player_id].send_packet(
                OutboundMsg.SEQUENCE_MESSAGE.value,
                {
                    "gameID": session.game_id,
                    "msg": {
                        "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                        "value": {"viewer": only_player_id},
                    },
                },
            )

        session.send_serialized_game_state = fake_state_resync
        await session.on_player_disconnect(
            "first", client_handler=first.client_handler
        )
        await session.on_player_disconnect(
            "second", client_handler=second.client_handler
        )
        await self.settle_notices(session)

        await session.reconnect_player(SimpleNamespace(running=True), "first")
        await session.mark_player_ready("first")
        first_match_found_count = sum(
            name == OutboundMsg.MATCH_FOUND.value for name, _, _ in first.packets
        )
        self.assertIn("first", session._resync_ready)
        self.assertFalse(session._connection_resumed.is_set())

        await session.reconnect_player(SimpleNamespace(running=True), "second")
        try:
            self.assertEqual(
                sum(name == OutboundMsg.MATCH_FOUND.value for name, _, _ in first.packets),
                first_match_found_count,
            )
            self.assertEqual(
                sum(name == OutboundMsg.MATCH_FOUND.value for name, _, _ in second.packets),
                1,
            )
            await session.mark_player_ready("second")
            self.assertTrue(session._connection_resumed.is_set())
            self.assertFalse(session._resync_ready)
            self.assertFalse(session._offers_to_restore)
        finally:
            await self.cleanup_session(session)

    async def test_new_reconnect_socket_supersedes_inflight_snapshot(self):
        session = self.make_session()
        returning = RecordingNetworkPlayer("returning")
        opponent = RecordingNetworkPlayer("opponent")
        session.players = {"returning": returning, "opponent": opponent}

        async def fake_state_resync(only_player_id=None):
            await session.players[only_player_id].send_packet(
                OutboundMsg.SEQUENCE_MESSAGE.value,
                {
                    "gameID": session.game_id,
                    "msg": {
                        "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                        "value": {"viewer": only_player_id},
                    },
                },
            )

        session.send_serialized_game_state = fake_state_resync
        await session.on_player_disconnect(
            "returning", client_handler=returning.client_handler
        )
        await self.settle_notices(session)

        first_handler = SimpleNamespace(running=True)
        await session.reconnect_player(first_handler, "returning")
        session._state_checkpoint.clear()
        first_ready = asyncio.create_task(
            session.mark_player_ready("returning", client_handler=first_handler)
        )
        await asyncio.sleep(0)

        second_handler = SimpleNamespace(running=True)
        await session.reconnect_player(second_handler, "returning")
        second_ready = asyncio.create_task(
            session.mark_player_ready("returning", client_handler=second_handler)
        )
        await asyncio.sleep(0)
        session._state_checkpoint.set()
        try:
            await asyncio.gather(first_ready, second_ready)
            snapshots = [
                value for name, value, _ in returning.packets
                if (name == OutboundMsg.SEQUENCE_MESSAGE.value
                    and value.get("msg", {}).get("name")
                    == OutboundMsg.SERIALIZED_GAME_STATE.value)
            ]
            self.assertEqual(len(snapshots), 1)
            self.assertTrue(session._connection_resumed.is_set())
            self.assertFalse(session._resync_inflight)
        finally:
            await self.cleanup_session(session)


if __name__ == "__main__":
    unittest.main()
