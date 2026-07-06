import asyncio
import os
import tempfile
import unittest
import uuid
from unittest.mock import patch

DAY_MS = 86400000
FAR = 4102444800000


def make_definition(**overrides):
    d = {
        "name": "Test Cup", "title": "Test Cup", "description": "A test tournament",
        "previewTime": 1, "startTime": 2, "entryClosingTime": FAR,
        "resolutionTime": FAR + 1, "disappearTime": FAR + 2,
        "maxRuns": 2, "prizeBy": "wins",
        "run": {
            "entryFee": [{"currency": "Tokens", "amount": 100}],
            "allowDeckSwitching": True,
            "maxWins": 3, "maxLosses": 2, "maxGames": 0,
            "prizeTable": [
                {"start": 0, "end": 2, "rewards": [
                    {"rewardType": "Tokens", "rewardAmount": 50}]},
                {"start": 3, "end": 3, "rewards": [
                    {"rewardType": "Tokens", "rewardAmount": 500},
                    {"rewardType": "Archetype", "rewardAmount": 1,
                     "rewardProductID": "aaaa-bbbb-cccc"}]},
            ],
        },
        "leaderboard": {
            "runs": 0, "winValue": 3, "lossValue": 1,
            "prizeTable": [
                {"start": 1, "end": 1, "rewards": [
                    {"rewardType": "Tokens", "rewardAmount": 1000}]},
            ],
        },
    }
    d.update(overrides)
    return d


class TournamentDBTestCase(unittest.TestCase):
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

    def _new_account(self, name=None):
        from spirit.database.accounts import create_account
        name = name or f"tour_{uuid.uuid4().hex[:10]}"
        return create_account(name, "pw123")["account_id"]

    def _new_tournament(self, **overrides):
        from spirit.database import tournament_data
        return tournament_data.upsert_tournament(make_definition(**overrides))


class TestTournamentData(TournamentDBTestCase):
    def test_join_deducts_fee_and_enforces_limits(self):
        from spirit.database import tournament_data
        from spirit.database.player_data import get_wallet_by_account_id

        t = self._new_tournament()
        account_id = self._new_account()
        coins_before = get_wallet_by_account_id(account_id)["coins"]

        entry, err = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        self.assertIsNone(err)
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], coins_before - 100)

        # one active run at a time
        _, err = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        self.assertIn("active run", err)

        # bad currency rejected
        other = self._new_account()
        _, err = tournament_data.create_entry(
            other, t["tournament_id"], t["definition"], "Gems", {})
        self.assertIn("currency", err.lower())

    def test_join_rejects_insufficient_funds(self):
        from spirit.database import tournament_data
        from spirit.database.player_data import get_wallet_by_account_id, update_wallet

        t = self._new_tournament()
        account_id = self._new_account()
        update_wallet(account_id, 5, 0, 0)
        _, err = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        self.assertIn("afford", err)
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], 5)

    def test_max_runs_enforced(self):
        from spirit.database import tournament_data

        t = self._new_tournament()
        account_id = self._new_account()
        for _ in range(2):  # maxRuns = 2
            entry, err = tournament_data.create_entry(
                account_id, t["tournament_id"], t["definition"], "Tokens", {})
            self.assertIsNone(err)
            tournament_data.finish_entry(
                entry["entry_id"], account_id, t["definition"], resigned=True)
        _, err = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        self.assertIn("runs remaining", err)

    def test_run_completion_and_prize_grant(self):
        from spirit.database import tournament_data
        from spirit.database.player_data import get_wallet_by_account_id, get_collection_by_account_id

        t = self._new_tournament()
        run = t["definition"]["run"]
        account_id = self._new_account()
        entry, _ = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        entry_id = entry["entry_id"]

        # two wins: not complete yet
        for _ in range(2):
            result = tournament_data.record_game_result(
                entry_id, True, "opp-1", "Opponent", run)
            self.assertFalse(result["run_complete"])
        # third win caps the run (maxWins=3)
        result = tournament_data.record_game_result(
            entry_id, True, "opp-1", "Opponent", run)
        self.assertTrue(result["run_complete"])
        self.assertEqual(len(result["history"]), 3)
        self.assertEqual(result["history"][0]["gameResult"], "Win")

        coins_before = get_wallet_by_account_id(account_id)["coins"]
        finished, granted = tournament_data.finish_entry(
            entry_id, account_id, t["definition"])
        self.assertEqual(finished["status"], "complete")
        self.assertEqual(len(granted), 2)  # 3-wins row: 500 tokens + card
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], coins_before + 500)
        collection = {c["archetype_id"]: c for c in get_collection_by_account_id(account_id)}
        self.assertEqual(collection["aaaa-bbbb-cccc"]["nontradable_count"], 1)

        # idempotent: second finish grants nothing
        _, granted = tournament_data.finish_entry(
            entry_id, account_id, t["definition"])
        self.assertEqual(granted, [])
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], coins_before + 500)

    def test_resign_grants_current_row(self):
        from spirit.database import tournament_data
        from spirit.database.player_data import get_wallet_by_account_id

        t = self._new_tournament()
        account_id = self._new_account()
        entry, _ = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        tournament_data.record_game_result(
            entry["entry_id"], True, "opp", "Opp", t["definition"]["run"])

        coins_before = get_wallet_by_account_id(account_id)["coins"]
        finished, granted = tournament_data.finish_entry(
            entry["entry_id"], account_id, t["definition"], resigned=True)
        self.assertEqual(finished["status"], "resigned")
        self.assertEqual(granted[0]["rewardAmount"], 50)  # 0-2 wins row
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], coins_before + 50)

    def test_standings_and_leaderboard_claim(self):
        from spirit.database import tournament_data

        t = self._new_tournament()
        run = t["definition"]["run"]
        winner = self._new_account()
        loser = self._new_account()
        e1, _ = tournament_data.create_entry(winner, t["tournament_id"], t["definition"], "Tokens", {})
        e2, _ = tournament_data.create_entry(loser, t["tournament_id"], t["definition"], "Tokens", {})
        tournament_data.record_game_result(e1["entry_id"], True, loser, "Loser", run)
        tournament_data.record_game_result(e2["entry_id"], False, winner, "Winner", run)

        standings = tournament_data.leaderboard_standings(
            t["tournament_id"], t["definition"])
        self.assertEqual(standings[0]["accountID"], winner)
        self.assertEqual(standings[0]["points"], 3.0)  # 1 win * winValue 3
        self.assertEqual(standings[0]["rank"], 1)
        self.assertEqual(standings[1]["accountID"], loser)
        self.assertEqual(standings[1]["points"], 1.0)  # 1 loss * lossValue 1

        rank, granted = tournament_data.claim_leaderboard_reward(
            winner, t["tournament_id"], t["definition"], standings)
        self.assertEqual(rank, 1)
        self.assertEqual(granted[0]["rewardAmount"], 1000)
        self.assertTrue(tournament_data.has_claimed_leaderboard(winner, t["tournament_id"]))

        # second claim rejected
        rank, err = tournament_data.claim_leaderboard_reward(
            winner, t["tournament_id"], t["definition"], standings)
        self.assertIsNone(rank)
        self.assertIn("already claimed", err)

        # rank 2 has no prize row -> empty grant but claim recorded
        rank, granted = tournament_data.claim_leaderboard_reward(
            loser, t["tournament_id"], t["definition"], standings)
        self.assertEqual(rank, 2)
        self.assertEqual(granted, [])


class TestTournamentManager(TournamentDBTestCase):
    def test_wire_shape_and_states(self):
        from spirit.game.tournament_manager import (
            TournamentDef, STATE_OPEN, STATE_PREVIEW, STATE_ENTRY_CLOSED,
            STATE_RESOLVED, STATE_HIDDEN,
        )
        now = 1000000
        d = TournamentDef("tid-1", make_definition(
            previewTime=now - 10, startTime=now - 5,
            entryClosingTime=now + 10, resolutionTime=now + 20,
            disappearTime=now + 30), True)
        self.assertEqual(d.state(now), STATE_OPEN)
        self.assertEqual(d.state(now - 7), STATE_PREVIEW)
        self.assertEqual(d.state(now + 15), STATE_ENTRY_CLOSED)
        self.assertEqual(d.state(now + 25), STATE_RESOLVED)
        self.assertEqual(d.state(now + 35), STATE_HIDDEN)

        wire = d.to_client_dict()
        self.assertEqual(wire["id"], "tid-1")
        self.assertEqual(wire["title"], {"id": "Test Cup"})
        self.assertEqual(wire["run"]["maxWins"], 3)
        self.assertEqual(wire["run"]["entryFee"], [{"currency": "Tokens", "amount": 100}])
        # every reward must hint the only registered RewardDefinition subclass
        for prize in wire["run"]["prizeTable"] + wire["leaderboard"]["prizeTable"]:
            for reward in prize["rewards"]:
                self.assertEqual(reward["name"], "NoReward")
                self.assertIn("rewardType", reward)
                self.assertIn("rewardAmount", reward)
                self.assertIn("flavor", reward)
                self.assertNotIn("rewardProductID", reward)
        self.assertIsNone(wire["limited"])
        self.assertIsNone(wire["league"])

    def test_validate_definition(self):
        from spirit.game.tournament_manager import validate_definition
        self.assertIsNone(validate_definition(make_definition()))
        self.assertIsNotNone(validate_definition({"name": ""}))
        bad = make_definition()
        bad["run"] = {"maxWins": 0, "maxLosses": 0, "maxGames": 0}
        self.assertIsNotNone(validate_definition(bad))
        bad = make_definition()
        bad["run"]["entryFee"] = [{"currency": "Doubloons", "amount": 5}]
        self.assertIsNotNone(validate_definition(bad))
        bad = make_definition()
        bad["run"]["prizeTable"][0]["rewards"] = [{"rewardType": "Archetype"}]
        self.assertIsNotNone(validate_definition(bad))
        self.assertIsNotNone(validate_definition(make_definition(maxSize=5)))
        self.assertIsNotNone(
            validate_definition(make_definition(matchStructure="Swiss")))
        self.assertIsNone(validate_definition(make_definition(maxSize=8)))

    def test_manager_reload_and_visibility(self):
        from spirit.database import tournament_data
        from spirit.game.tournament_manager import TournamentManager

        t = self._new_tournament()
        manager = TournamentManager()
        manager.reload_from_db()
        self.assertIsNotNone(manager.get(t["tournament_id"]))
        self.assertIn(t["tournament_id"],
                      [x.tournament_id for x in manager.visible_tournaments()])

        tournament_data.upsert_tournament(
            definition=None, tournament_id=t["tournament_id"], enabled=False)
        manager.reload_from_db()
        self.assertNotIn(t["tournament_id"],
                         [x.tournament_id for x in manager.visible_tournaments()])


class MockPlayer:
    def __init__(self, account_id, username):
        self.account_id = account_id
        self.username = username
        self.decks = []

    def get_wallet_data(self):
        from spirit.database.player_data import get_wallet_by_account_id
        return dict(get_wallet_by_account_id(self.account_id) or {})


class MockServer:
    def __init__(self):
        self.clients = []


class MockClientHandler:
    def __init__(self, account_id, username):
        self.player = MockPlayer(account_id, username)
        self.sent_packets = []
        self.addr = ("127.0.0.1", 4242)
        self.server = MockServer()
        self.server.clients.append(self)

    async def send_packet(self, response_body, request_id, flags=0):
        self.sent_packets.append(response_body)


class TestTournamentHandler(TournamentDBTestCase, unittest.IsolatedAsyncioTestCase):
    def _handler(self, account_id):
        from spirit.packets.handlers.tournaments import TournamentHandler
        client = MockClientHandler(account_id, "tester")
        return TournamentHandler(client), client

    def _sync_manager(self):
        from spirit.game.tournament_manager import TournamentManager
        TournamentManager().reload_from_db()

    async def test_get_active_async_tournaments(self):
        t = self._new_tournament()
        self._sync_manager()
        account_id = self._new_account()
        handler, client = self._handler(account_id)

        await handler.handle_get_active_async_tournaments({}, 7, 0)
        msg = client.sent_packets[-1]
        self.assertEqual(msg["messageName"], "ActiveAsyncTournaments")
        ids = [d["id"] for d in msg["tournamentDefinitions"]]
        self.assertIn(t["tournament_id"], ids)
        self.assertEqual(msg["tournamentProgress"], [])
        self.assertEqual(msg["claimedLeaderboard"], {})

    async def test_legacy_events_scene_list(self):
        t = self._new_tournament()
        self._sync_manager()
        handler, client = self._handler(self._new_account())
        await handler.handle_get_active_tournaments_legacy({}, 3, 0)
        msg = client.sent_packets[-1]
        self.assertEqual(msg["messageName"], "AvailableTournamentList")
        # null tournamentQueues NREs the client handler — must be a dict
        self.assertIsInstance(msg["tournamentQueues"], dict)
        entry = next(e for e in msg["tournamentList"]
                     if e["tournamentID"] == t["tournament_id"])
        # entryFee/prizes must be non-null arrays (three renderers deref them)
        self.assertEqual(entry["entryFee"], [{"feeType": "Tokens", "feeAmount": 100}])
        self.assertTrue(entry["active"])
        self.assertEqual(entry["maxSize"], 8)
        self.assertEqual(entry["matchStructure"], "SingleElimination")
        prize_types = {p["prizeType"]["type"] for p in entry["prizes"]}
        self.assertEqual(prize_types, {"Tokens", "Archetype"})
        for p in entry["prizes"]:
            self.assertIn("startPlace", p)
            self.assertIn("endPlace", p)

        await handler.handle_subscribe_to_tournament_channel({}, 4, 0)
        msg = client.sent_packets[-1]
        self.assertEqual(msg["messageName"], "SubscribeToTournamentChannelSuccessful")
        self.assertIn(t["tournament_id"].lower(), msg["tournamentQueues"])

    async def test_join_flow_and_errors(self):
        t = self._new_tournament()
        self._sync_manager()
        account_id = self._new_account()
        handler, client = self._handler(account_id)
        deck_id = str(uuid.uuid4())
        client.player.decks = [{
            "id": deck_id, "name": "My Deck",
            "deck_data": {"cards": [{"guid": "g-1", "count": 2}]}
        }]

        await handler.handle_join_async_tournament(
            {"tournamentID": t["tournament_id"], "currency": "Tokens",
             "deckID": deck_id}, 5, 0)
        joined = client.sent_packets[0]
        self.assertEqual(joined["messageName"], "AsyncTournamentJoined")
        self.assertEqual(joined["tournamentID"], t["tournament_id"])
        self.assertEqual(joined["deck"]["piles"]["deck"], ["g-1", "g-1"])
        self.assertEqual(joined["progress"]["wins"], 0)
        # wallet push follows the join
        self.assertEqual(client.sent_packets[1]["messageName"], "CurrentWallet")

        # progress now rides the listing
        await handler.handle_get_active_async_tournaments({}, 8, 0)
        listing = client.sent_packets[-1]
        self.assertEqual(len(listing["tournamentProgress"]), 1)
        self.assertEqual(listing["tournamentProgress"][0]["entryID"], joined["entryID"])

        # double-join rejected
        await handler.handle_join_async_tournament(
            {"tournamentID": t["tournament_id"], "currency": "Tokens"}, 6, 0)
        error = client.sent_packets[-1]
        self.assertEqual(error["messageName"], "JoinAsyncTournamentError")
        self.assertIn("active run", error["error"]["id"])

        # unknown tournament rejected
        await handler.handle_join_async_tournament(
            {"tournamentID": str(uuid.uuid4()), "currency": "Tokens"}, 7, 0)
        self.assertEqual(client.sent_packets[-1]["messageName"], "JoinAsyncTournamentError")

    async def test_join_rejected_before_open(self):
        t = self._new_tournament(startTime=FAR - 10, entryClosingTime=FAR - 5)
        self._sync_manager()
        handler, client = self._handler(self._new_account())
        await handler.handle_join_async_tournament(
            {"tournamentID": t["tournament_id"], "currency": "Tokens"}, 1, 0)
        error = client.sent_packets[-1]
        self.assertEqual(error["messageName"], "JoinAsyncTournamentError")
        self.assertIn("not open", error["error"]["id"])

    async def test_number_of_runs_and_history(self):
        from spirit.database import tournament_data
        t = self._new_tournament()
        self._sync_manager()
        account_id = self._new_account()
        entry, _ = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        tournament_data.record_game_result(
            entry["entry_id"], True, "opp", "Rival", t["definition"]["run"])
        handler, client = self._handler(account_id)

        await handler.handle_get_number_of_player_runs(
            {"tournamentID": t["tournament_id"]}, 2, 0)
        self.assertEqual(client.sent_packets[-1]["runs"], 1)

        await handler.handle_get_async_tournament_game_history(
            {"tournamentID": t["tournament_id"], "entryID": entry["entry_id"]}, 3, 0)
        history = client.sent_packets[-1]
        self.assertEqual(history["messageName"], "AsyncTournamentGameHistoryList")
        self.assertEqual(history["games"][0]["gameResult"], "Win")
        self.assertEqual(history["games"][0]["opponentName"], "Rival")

    async def test_start_game_queues_with_tournament_context(self):
        from spirit.database import tournament_data
        from spirit.game.session.manager import GameSessionManager
        t = self._new_tournament()
        self._sync_manager()
        account_id = self._new_account()
        deck_json = {"deckID": "d", "deckName": "D", "piles": {"deck": ["g-1"] * 60},
                     "attributes": []}
        entry, _ = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", deck_json)
        handler, client = self._handler(account_id)

        manager = GameSessionManager()
        manager.queues = {}
        manager.pending_pairings = {}
        manager.active_sessions = {}

        await handler.handle_start_async_tournament_game(
            {"entryID": entry["entry_id"]}, 9, 0)
        queue_name = f"AsyncTournament_{t['tournament_id']}"
        self.assertIn(queue_name, manager.queues)
        queued = manager.queues[queue_name][0]
        self.assertEqual(queued["tournament_context"]["entry_id"], entry["entry_id"])
        self.assertEqual(
            client.sent_packets[-1]["messageName"], "MatchQueueEntered")
        manager.queues = {}

    async def test_start_game_rejects_finished_run(self):
        from spirit.database import tournament_data
        t = self._new_tournament()
        self._sync_manager()
        account_id = self._new_account()
        entry, _ = tournament_data.create_entry(
            account_id, t["tournament_id"], t["definition"], "Tokens", {})
        tournament_data.finish_entry(
            entry["entry_id"], account_id, t["definition"], resigned=True)
        handler, client = self._handler(account_id)
        await handler.handle_start_async_tournament_game(
            {"entryID": entry["entry_id"]}, 1, 0)
        error = client.sent_packets[-1]
        self.assertEqual(error["messageName"], "StartAsyncTournamentGameError")

    async def test_tournament_pairing_carries_context(self):
        from spirit.game.session.manager import GameSessionManager
        manager = GameSessionManager()
        manager.queues = {}
        manager.pending_pairings = {}
        manager.auto_confirm_ready = False

        c1 = MockClientHandler("acc-1", "P1")
        c2 = MockClientHandler("acc-2", "P2")
        await manager.add_to_queue(
            c1, "AsyncTournament_t1", {"piles": {"deck": []}}, {}, 0,
            tournament_context={"tournament_id": "t1", "entry_id": "e1"})
        await manager.add_to_queue(
            c2, "AsyncTournament_t1", {"piles": {"deck": []}}, {}, 0,
            tournament_context={"tournament_id": "t1", "entry_id": "e2"})
        pairing = list(manager.pending_pairings.values())[0]
        self.assertEqual(pairing["tournament"]["tournament_id"], "t1")
        self.assertEqual(pairing["tournament"]["entries"],
                         {"acc-2": "e2", "acc-1": "e1"})
        manager.pending_pairings = {}
        manager.auto_confirm_ready = True


class TestLiveTournament(TournamentDBTestCase, unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        super().setUp()
        from spirit.game.live_tournament import LiveTournamentManager
        LiveTournamentManager._instance = None

    def _sync_manager(self):
        from spirit.game.tournament_manager import TournamentManager
        TournamentManager().reload_from_db()

    def _handler_for(self, username):
        from spirit.packets.handlers.tournaments import TournamentHandler
        account_id = self._new_account()
        client = MockClientHandler(account_id, username)
        deck_id = str(uuid.uuid4())
        client.player.decks = [{"id": deck_id, "name": "Deck",
                                "deck_data": {"piles": {"deck": ["g-1"] * 60}}}]
        return TournamentHandler(client), client, deck_id

    async def test_join_insufficient_funds(self):
        from spirit.database.player_data import update_wallet
        t = self._new_tournament()
        self._sync_manager()
        handler, client, deck_id = self._handler_for("Poor")
        update_wallet(client.player.account_id, 5, 0, 0)
        await handler.handle_join_tournament(
            {"tournamentID": t["tournament_id"], "deck": deck_id}, 1, 0)
        failed = next(p for p in client.sent_packets
                      if p["messageName"] == "JoinTournamentFailed")
        # WalletFailed drives the client's local refund; wallet push resyncs
        self.assertEqual(failed["reason"]["id"], "event.join.error.WalletFailed")
        self.assertEqual(client.sent_packets[-1]["messageName"], "CurrentWallet")

    async def test_leave_queue_refunds_fee(self):
        from spirit.database.player_data import get_wallet_by_account_id
        t = self._new_tournament()
        self._sync_manager()
        handler, client, deck_id = self._handler_for("Leaver")
        account_id = client.player.account_id
        start_coins = get_wallet_by_account_id(account_id)["coins"]

        await handler.handle_join_tournament(
            {"tournamentID": t["tournament_id"], "deck": deck_id}, 1, 0)
        names = [p["messageName"] for p in client.sent_packets]
        self.assertIn("TournamentQueueJoined", names)
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"],
                         start_coins - 100)

        await handler.handle_leave_tournament_queue(
            {"tournamentID": t["tournament_id"]}, 2, 0)
        names = [p["messageName"] for p in client.sent_packets]
        self.assertIn("TournamentQueueLeft", names)
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], start_coins)

        # leaving again fails
        await handler.handle_leave_tournament_queue(
            {"tournamentID": t["tournament_id"]}, 3, 0)
        self.assertEqual(client.sent_packets[-1]["messageName"],
                         "TournamentQueueLeftFailed")

    async def test_two_player_bracket_end_to_end(self):
        from spirit.game.session.manager import GameSessionManager
        from spirit.game.live_tournament import LiveTournamentManager
        from spirit.database.player_data import get_wallet_by_account_id

        run = {
            "entryFee": [{"currency": "Tokens", "amount": 100}],
            "allowDeckSwitching": True,
            "maxWins": 3, "maxLosses": 2, "maxGames": 0,
            "prizeTable": [
                {"start": 1, "end": 1, "rewards": [
                    {"rewardType": "Tokens", "rewardAmount": 500}]},
                {"start": 2, "end": 2, "rewards": [
                    {"rewardType": "Tokens", "rewardAmount": 50}]},
            ],
        }
        t = self._new_tournament(maxSize=2, run=run)
        self._sync_manager()
        h1, c1, d1 = self._handler_for("Alice")
        h2, c2, d2 = self._handler_for("Bob")

        manager = GameSessionManager()
        manager.queues = {}
        dispatched = []
        with patch.object(GameSessionManager, "_dispatch_ready_check",
                          lambda self, gid, qn, clients, delay=1.5: dispatched.append(gid)):
            await h1.handle_join_tournament(
                {"tournamentID": t["tournament_id"], "deck": d1}, 1, 0)
            await h2.handle_join_tournament(
                {"tournamentID": t["tournament_id"], "deck": d2}, 2, 0)

        for client in (c1, c2):
            names = [p["messageName"] for p in client.sent_packets]
            self.assertIn("TournamentQueueJoined", names)
            self.assertIn("TournamentStarted", names)
            self.assertIn("TournamentRoundUpdated", names)

        started = next(p for p in c1.sent_packets
                       if p["messageName"] == "TournamentStarted")
        self.assertEqual(started["size"], 2)

        round_upd = next(p for p in c1.sent_packets
                         if p["messageName"] == "TournamentRoundUpdated")
        progress = round_upd["tournamentData"]
        self.assertIsNotNone(progress["tournamentData"])  # nested G.g NRE trap
        matchup = progress["matchups"][0]
        self.assertEqual(len(matchup["players"]), 2)  # G.j NRE trap
        self.assertIsNone(matchup["winner"])
        self.assertEqual(matchup["round"], 1)
        self.assertEqual(matchup["table"], 0)

        # the bracket game rides the normal pairing pipeline with legacy context
        game_id = matchup["gameID"]
        self.assertIn(game_id, dispatched)
        pairing = manager.pending_pairings.pop(game_id)
        self.assertEqual(pairing["legacy_tournament"]["tournament_id"],
                         t["tournament_id"])
        active_id = pairing["legacy_tournament"]["active_id"]
        self.assertEqual(active_id, round_upd["activeTournamentID"])

        # reconnect answer while the bracket runs
        await h1.handle_is_user_in_active_tournament({}, 5, 0)
        self.assertEqual(c1.sent_packets[-1]["activeTournamentID"], active_id)
        await h1.handle_get_tournament_in_progress(
            {"activeTournamentID": active_id}, 6, 0)
        in_progress = c1.sent_packets[-1]
        self.assertEqual(in_progress["messageName"], "TournamentsInProgressData")
        self.assertEqual(len(in_progress["tournamentData"]), 1)

        live = LiveTournamentManager()
        winner_id = c1.player.account_id
        loser_id = c2.player.account_id
        coins_before = get_wallet_by_account_id(winner_id)["coins"]
        await live.record_game_result(active_id, game_id, winner_id)

        completed = next(p for p in c1.sent_packets
                         if p["messageName"] == "TournamentCompleted")
        self.assertEqual(completed["finalStandings"][0]["accountID"], winner_id)
        self.assertEqual(completed["finalStandings"][1]["accountID"], loser_id)
        self.assertEqual(completed["prizes"][0]["rewardAmount"], 500)
        self.assertIsNone(completed["prizes"][0]["rewardProductID"])
        self.assertEqual(
            completed["tournamentData"]["matchups"][0]["winner"]["accountID"],
            winner_id)
        loser_completed = next(p for p in c2.sent_packets
                               if p["messageName"] == "TournamentCompleted")
        self.assertEqual(loser_completed["prizes"][0]["rewardAmount"], 50)
        self.assertEqual(get_wallet_by_account_id(winner_id)["coins"],
                         coins_before + 500)
        self.assertEqual(live.active, {})

    async def test_four_player_bracket_advances_rounds(self):
        from spirit.game.session.manager import GameSessionManager
        from spirit.game.live_tournament import LiveTournamentManager
        import spirit.game.live_tournament as lt_module

        t = self._new_tournament(maxSize=4, delayBetweenRounds=3)
        self._sync_manager()
        players = [self._handler_for(f"P{i}") for i in range(4)]

        manager = GameSessionManager()
        manager.queues = {}
        real_sleep = asyncio.sleep
        async def _no_sleep(_secs):
            await real_sleep(0)
        with patch.object(GameSessionManager, "_dispatch_ready_check",
                          lambda self, gid, qn, clients, delay=1.5: None), \
             patch.object(lt_module.asyncio, "sleep", _no_sleep):
            for i, (handler, _, deck_id) in enumerate(players):
                await handler.handle_join_tournament(
                    {"tournamentID": t["tournament_id"], "deck": deck_id}, i, 0)

            live = LiveTournamentManager()
            self.assertEqual(len(live.active), 1)
            tournament = list(live.active.values())[0]
            round1 = [m for m in tournament.matchups if m.round == 1]
            self.assertEqual(len(round1), 2)
            self.assertEqual([m.table for m in round1], [0, 1])

            # resolve round 1: table winners advance
            w1 = round1[0].players[0]
            w2 = round1[1].players[1]
            await live.record_game_result(
                tournament.active_id, round1[0].game_id, w1.account_id)
            names = [p["messageName"] for p in players[0][1].sent_packets]
            self.assertNotIn("TournamentNextRoundStarting", names)
            await live.record_game_result(
                tournament.active_id, round1[1].game_id, w2.account_id)
            for _ in range(3):  # let the spawned next-round task run
                await asyncio.sleep(0)

            # next round paired from the table-ordered winners (sleep patched out)
            round2 = [m for m in tournament.matchups if m.round == 2]
            self.assertEqual(len(round2), 1)
            self.assertEqual({p.account_id for p in round2[0].players},
                             {w1.account_id, w2.account_id})
            names = [p["messageName"] for p in players[0][1].sent_packets]
            self.assertIn("TournamentNextRoundStarting", names)

            await live.record_game_result(
                tournament.active_id, round2[0].game_id, w2.account_id)
            self.assertTrue(tournament.completed)
            standings = tournament.final_standings()
            self.assertEqual(standings[0].account_id, w2.account_id)
            self.assertEqual(standings[1].account_id, w1.account_id)

    async def test_withdraw_forfeits_pending_matchup(self):
        from spirit.game.session.manager import GameSessionManager
        from spirit.game.live_tournament import LiveTournamentManager

        t = self._new_tournament(maxSize=2)
        self._sync_manager()
        h1, c1, d1 = self._handler_for("Stay")
        h2, c2, d2 = self._handler_for("Quit")
        manager = GameSessionManager()
        manager.queues = {}
        with patch.object(GameSessionManager, "_dispatch_ready_check",
                          lambda self, gid, qn, clients, delay=1.5: None):
            await h1.handle_join_tournament(
                {"tournamentID": t["tournament_id"], "deck": d1}, 1, 0)
            await h2.handle_join_tournament(
                {"tournamentID": t["tournament_id"], "deck": d2}, 2, 0)
            live = LiveTournamentManager()
            tournament = list(live.active.values())[0]
            await h2.handle_leave_active_tournament(
                {"activeTournamentID": tournament.active_id,
                 "tournamentID": t["tournament_id"]}, 3, 0)
        self.assertEqual(c2.sent_packets[-1]["messageName"], "TournamentLeft")
        completed = next(p for p in c1.sent_packets
                         if p["messageName"] == "TournamentCompleted")
        self.assertEqual(completed["finalStandings"][0]["accountID"],
                         c1.player.account_id)


if __name__ == "__main__":
    unittest.main()
