"""Bot fill for Events-bracket tournaments: validation, timer, matchups, prizes."""
import asyncio
import unittest
import uuid

from unittest.mock import AsyncMock, patch

from spirit.game.session.manager import GameSessionManager
from spirit.game.tournaments.live import (
    LiveTournament, LiveTournamentManager, Matchup, Participant,
)
from spirit.game.tournaments.manager import (
    TournamentDef, _legacy_prizes, validate_definition,
)


def base_definition(**overrides):
    d = {
        "name": "Bot Fill Test",
        "title": "Bot Fill Test",
        "maxSize": 2,
        "matchStructure": "SingleElimination",
        "format": "Unlimited",
        "run": {
            "maxWins": 1, "maxLosses": 0, "maxGames": 0,
            "entryFee": [],
            "prizeTable": [
                {"start": 1, "end": 2,
                 "rewards": [{"rewardType": "Tokens", "rewardAmount": 10}]},
            ],
        },
    }
    d.update(overrides)
    return d


def make_tdef(definition=None, enabled=True, tid=None):
    return TournamentDef(tid or str(uuid.uuid4()), definition or base_definition(),
                         enabled)


def stub_tm(tdef):
    class _Stub:
        def get(self, tid):
            return tdef
    return _Stub()


class FakePlayer:
    def __init__(self, username="Tester"):
        self.account_id = str(uuid.uuid4())
        self.username = username
        self.screen_name = username
        self.wallet = None

    def get_wallet_data(self):
        return {}


class FakeClient:
    def __init__(self):
        self.player = FakePlayer()
        self.running = True
        self.sent = []

    async def send_packet(self, packet, request_id=0):
        self.sent.append(packet)


class LiveCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        m = LiveTournamentManager()
        tasks = list(m._background_tasks)
        for t in tasks:
            t.cancel()
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        m.queues.clear()
        m.active.clear()
        m._fill_tasks.clear()
        m.subscribers.clear()
        gsm = GameSessionManager()
        gsm.pending_pairings.clear()
        self.m = m
        self.gsm = gsm

    async def asyncTearDown(self):
        tasks = list(self.m._background_tasks)
        for t in tasks:
            t.cancel()
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)


class ValidateDefinitionTests(unittest.TestCase):
    def test_accepts_bot_fill_fields(self):
        d = base_definition(botFill=True, botFillDelay=45)
        self.assertIsNone(validate_definition(d))

    def test_accepts_zero_delay(self):
        d = base_definition(botFill=True, botFillDelay=0)
        self.assertIsNone(validate_definition(d))

    def test_rejects_non_bool_bot_fill(self):
        error = validate_definition(base_definition(botFill="yes"))
        self.assertIn("botFill", error)

    def test_rejects_negative_delay(self):
        error = validate_definition(base_definition(botFillDelay=-1))
        self.assertIn("botFillDelay", error)

    def test_rejects_non_numeric_delay(self):
        error = validate_definition(base_definition(botFillDelay="soon"))
        self.assertIn("botFillDelay", error)

    def test_rejects_delay_over_cap(self):
        error = validate_definition(base_definition(botFillDelay=3601))
        self.assertIn("botFillDelay", error)


class TournamentDefPropertyTests(unittest.TestCase):
    def test_bot_fill_defaults_off(self):
        self.assertFalse(make_tdef().bot_fill)

    def test_bot_fill_reads_definition(self):
        self.assertTrue(make_tdef(base_definition(botFill=True)).bot_fill)

    def test_delay_defaults_to_30(self):
        self.assertEqual(make_tdef().bot_fill_delay, 30)

    def test_zero_delay_is_kept(self):
        tdef = make_tdef(base_definition(botFillDelay=0))
        self.assertEqual(tdef.bot_fill_delay, 0)

    def test_garbage_delay_falls_back(self):
        tdef = make_tdef(base_definition(botFillDelay="soon"))
        self.assertEqual(tdef.bot_fill_delay, 30)


class BotParticipantTests(unittest.TestCase):
    def test_bot_participant_shape(self):
        deck = {"deckName": "Charizard (charizard-vmax)",
                "piles": {"deck": ["guid-1"]}}
        p = Participant(None, deck, bot=True)
        self.assertTrue(p.bot)
        self.assertIsNone(p.client)
        uuid.UUID(p.account_id)  # GUID-shaped for the client deserializer
        self.assertEqual(p.username, "Bot (Charizard (charizard-vmax))")
        self.assertFalse(p.withdrawn)
        self.assertEqual(p.wins, 0)
        self.assertEqual(p.identity(),
                         {"accountID": p.account_id, "username": p.username})

    def test_human_participant_unchanged(self):
        client = FakeClient()
        p = Participant(client, {"piles": {"deck": []}})
        self.assertFalse(p.bot)
        self.assertIs(p.client, client)
        self.assertEqual(p.account_id, client.player.account_id)
        self.assertEqual(p.username, "Tester")

    def test_resolve_client_returns_none_for_bot(self):
        m = LiveTournamentManager()
        bot = Participant(None, {"piles": {"deck": []}}, bot=True)
        self.assertIsNone(m.resolve_client(bot))


class MakeBotTests(unittest.TestCase):
    def test_make_bot_draws_pool_deck(self):
        tdef = make_tdef()
        bot = LiveTournamentManager()._make_bot(tdef)
        self.assertTrue(bot.bot)
        self.assertTrue(bot.deck.get("piles", {}).get("deck"),
                        "bot deck must resolve to a non-empty pile")
        self.assertTrue(bot.username.startswith("Bot ("))


class FillAfterTests(LiveCase):
    async def test_pads_and_starts_bracket(self):
        tdef = make_tdef(base_definition(maxSize=2, botFill=True, botFillDelay=0))
        tid = tdef.tournament_id.lower()
        client = FakeClient()
        self.m.queues[tid] = [Participant(client, {"piles": {"deck": []}})]
        self.m.subscribers.append(client)  # queued clients sit on the Events scene
        with patch("spirit.game.tournaments.live.TournamentManager",
                   lambda: stub_tm(tdef)), \
             patch.object(GameSessionManager, "_dispatch_ready_check") as dc:
            await asyncio.wait_for(self.m._fill_after(tid), 5)

        self.assertEqual(self.m.queues[tid], [], "humans must leave the queue")
        self.assertEqual(len(self.m.active), 1)
        live = next(iter(self.m.active.values()))
        self.assertEqual(len(live.participants), 2)
        bots = [p for p in live.participants if p.bot]
        humans = [p for p in live.participants if not p.bot]
        self.assertEqual(len(bots), 1)
        self.assertEqual(len(humans), 1)
        self.assertIs(humans[0].client, client)

        matchup = live.matchups[0]
        pairing = self.gsm.pending_pairings[matchup.game_id]
        self.assertIsNone(pairing["players"][bots[0].account_id]["client"])
        self.assertTrue(pairing["players"][bots[0].account_id]["ready"])
        self.assertFalse(pairing["players"][humans[0].account_id]["ready"])
        # ready check must only be dispatched to real clients
        dc.assert_called_once()
        self.assertEqual(dc.call_args[0][2], [client],
                         "None clients must be filtered out of the ready check")
        # bots never sit in the queue: the status broadcast after padding is 0
        self.assertTrue(any(p.get("size") == 0 for p in client.sent))
        for packet in client.sent:
            self.assertNotIn("Bot (", str(packet.get("usernames", "")))

    async def test_bails_on_empty_queue(self):
        tdef = make_tdef(base_definition(botFill=True, botFillDelay=0))
        tid = tdef.tournament_id.lower()
        with patch("spirit.game.tournaments.live.TournamentManager",
                   lambda: stub_tm(tdef)):
            await asyncio.wait_for(self.m._fill_after(tid), 5)
        self.assertEqual(len(self.m.active), 0)

    async def test_bails_when_tournament_gone(self):
        tdef = make_tdef(base_definition(botFill=True, botFillDelay=0))
        tid = tdef.tournament_id.lower()
        self.m.queues[tid] = [Participant(FakeClient(), {"piles": {"deck": []}})]
        with patch("spirit.game.tournaments.live.TournamentManager",
                   lambda: stub_tm(None)):
            await asyncio.wait_for(self.m._fill_after(tid), 5)
        self.assertEqual(len(self.m.active), 0)
        self.assertEqual(len(self.m.queues[tid]), 1)

    async def test_bails_when_tournament_disabled(self):
        tdef = make_tdef(base_definition(botFill=True, botFillDelay=0),
                         enabled=False)
        tid = tdef.tournament_id.lower()
        self.m.queues[tid] = [Participant(FakeClient(), {"piles": {"deck": []}})]
        with patch("spirit.game.tournaments.live.TournamentManager",
                   lambda: stub_tm(tdef)):
            await asyncio.wait_for(self.m._fill_after(tid), 5)
        self.assertEqual(len(self.m.active), 0)

    async def test_waits_for_the_delay(self):
        tdef = make_tdef(base_definition(botFill=True, botFillDelay=3600))
        tid = tdef.tournament_id.lower()
        self.m.queues[tid] = [Participant(FakeClient(), {"piles": {"deck": []}})]
        with patch("spirit.game.tournaments.live.TournamentManager",
                   lambda: stub_tm(tdef)):
            task = asyncio.create_task(self.m._fill_after(tid))
            await asyncio.sleep(0.05)
            self.assertFalse(task.done(), "must still be sleeping before the delay")
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)
        self.assertEqual(len(self.m.active), 0)


class JoinQueueTests(LiveCase):
    async def test_join_starts_fill_timer_when_enabled(self):
        tdef = make_tdef(base_definition(botFill=True, botFillDelay=60))
        tid = tdef.tournament_id.lower()
        await self.m.join_queue(FakeClient(), tdef, {"piles": {"deck": []}})
        self.assertEqual(len(self.m.queues[tid]), 1)
        self.assertIn(tid, self.m._fill_tasks)
        self.assertFalse(self.m._fill_tasks[tid].done())

    async def test_join_no_timer_when_disabled(self):
        tdef = make_tdef()
        tid = tdef.tournament_id.lower()
        await self.m.join_queue(FakeClient(), tdef, {"piles": {"deck": []}})
        self.assertEqual(len(self.m.queues[tid]), 1)
        self.assertNotIn(tid, self.m._fill_tasks)

    async def test_natural_full_starts_without_bots(self):
        tdef = make_tdef(base_definition(maxSize=2, botFill=True, botFillDelay=60))
        tid = tdef.tournament_id.lower()
        with patch.object(GameSessionManager, "_dispatch_ready_check"):
            await self.m.join_queue(FakeClient(), tdef, {"piles": {"deck": []}})
            await self.m.join_queue(FakeClient(), tdef, {"piles": {"deck": []}})
        self.assertEqual(self.m.queues[tid], [])
        self.assertEqual(len(self.m.active), 1)
        live = next(iter(self.m.active.values()))
        self.assertEqual(len(live.participants), 2)
        self.assertTrue(all(not p.bot for p in live.participants))


class HumanVsBotStartTests(LiveCase):
    async def test_pairing_shapes_and_ready_check_filtering(self):
        tdef = make_tdef()
        client = FakeClient()
        human = Participant(client, {"piles": {"deck": []}})
        bot = Participant(None, {"piles": {"deck": ["g"]}}, bot=True)
        t = LiveTournament(self.m, tdef, [human, bot])
        matchup = Matchup(1, 0, [human, bot])
        with patch.object(GameSessionManager, "_dispatch_ready_check") as dc:
            await t._start_or_forfeit(matchup)

        pairing = self.gsm.pending_pairings[matchup.game_id]
        self.assertIs(pairing["players"][human.account_id]["client"], client)
        self.assertFalse(pairing["players"][human.account_id]["ready"])
        self.assertIsNone(pairing["players"][bot.account_id]["client"])
        self.assertTrue(pairing["players"][bot.account_id]["ready"])
        dc.assert_called_once()
        self.assertEqual(dc.call_args[0][2], [client],
                         "None clients must be filtered out of the ready check")

    async def test_offline_human_forfeits_to_bot(self):
        tdef = make_tdef()
        client = FakeClient()
        client.running = False
        human = Participant(client, {"piles": {"deck": []}})
        bot = Participant(None, {"piles": {"deck": ["g"]}}, bot=True)
        t = LiveTournament(self.m, tdef, [human, bot])
        matchup = Matchup(1, 0, [human, bot])
        t.matchups.append(matchup)
        with patch.object(GameSessionManager, "_dispatch_ready_check") as dc, \
             patch("spirit.game.tournaments.live.run_db", new=AsyncMock()):
            # completion retries TournamentCompleted delivery ~8s for the
            # offline human before giving up
            await asyncio.wait_for(t._start_or_forfeit(matchup), 20)
        self.assertIs(matchup.winner, bot)
        self.assertNotIn(matchup.game_id, self.gsm.pending_pairings)
        dc.assert_not_called()


class BotVsBotTests(LiveCase):
    async def test_instant_resolve_without_session(self):
        tdef = make_tdef(base_definition(maxSize=2))
        bot_a = Participant(None, {"piles": {"deck": ["a"]}}, bot=True)
        bot_b = Participant(None, {"piles": {"deck": ["b"]}}, bot=True)
        t = LiveTournament(self.m, tdef, [bot_a, bot_b])
        self.m.active[t.active_id] = t
        matchup = Matchup(1, 0, [bot_a, bot_b])
        t.matchups.append(matchup)
        with patch("spirit.game.tournaments.live.run_db", new=AsyncMock()):
            await asyncio.wait_for(
                t._start_or_forfeit(matchup), 5)

        self.assertIsNotNone(matchup.winner, "bot-vs-bot must resolve instantly")
        self.assertIn(matchup.winner, (bot_a, bot_b))
        self.assertEqual(matchup.winner.wins, 1)
        loser = bot_b if matchup.winner is bot_a else bot_a
        self.assertEqual(loser.eliminated_round, 1)
        self.assertNotIn(matchup.game_id, self.gsm.pending_pairings,
                         "no GameSession pairing may be created")
        self.assertTrue(t.completed, "sole winner ends the tournament")


class PrizeTests(LiveCase):
    async def test_bots_win_no_prizes(self):
        tdef = make_tdef()
        client = FakeClient()
        human = Participant(client, {"piles": {"deck": []}})
        bot = Participant(None, {"piles": {"deck": ["g"]}}, bot=True)
        t = LiveTournament(self.m, tdef, [human, bot])
        with patch("spirit.game.tournaments.live.run_db",
                   new=AsyncMock()) as db:
            await asyncio.wait_for(t._complete(human), 5)

        self.assertEqual(db.await_count, 2,
                         "prize grant + history persist are the only DB calls")
        self.assertEqual(db.await_args_list[0].args[1], human.account_id)
        completed = [p for p in client.sent
                     if p.get("messageName") == "TournamentCompleted"]
        self.assertEqual(len(completed), 1)
        # champion prize actually granted
        self.assertEqual(len(completed[0]["prizes"]), 1)

    async def test_grant_failure_still_sends_completed(self):
        tdef = make_tdef()
        client = FakeClient()
        human = Participant(client, {"piles": {"deck": []}})
        t = LiveTournament(self.m, tdef, [human])
        with patch("spirit.game.tournaments.live.run_db",
                   new=AsyncMock(side_effect=RuntimeError("db down"))):
            await asyncio.wait_for(t._complete(human), 5)

        completed = [p for p in client.sent
                     if p.get("messageName") == "TournamentCompleted"]
        self.assertEqual(len(completed), 1,
                         "results packet must survive a grant failure")
        self.assertEqual(completed[0]["prizes"], [],
                         "ungranted prizes must not be advertised")

    def test_legacy_prize_types_match_client(self):
        table = [
            {"start": 1, "end": 1,
             "rewards": [
                 {"rewardType": "Archetype", "rewardProductID": "card-1",
                  "rewardAmount": 1},
                 {"rewardType": "Tokens", "rewardAmount": 5000,
                  "rewardCurrency": "prizeTrainerCoin"},
                 {"rewardType": "Tokens", "rewardAmount": 1,
                  "rewardCurrency": "prizeTournamentTicket"},
             ]},
        ]
        prizes = _legacy_prizes(table)
        self.assertEqual([p["prizeType"]["type"] for p in prizes],
                         ["Archetype", "Token", "TournamentTicket"],
                         "client only accepts Token/TournamentTicket (not Tokens)")
        self.assertEqual(prizes[0]["prizeType"]["archetypeID"], "card-1")
        self.assertIsNone(prizes[1]["prizeType"]["archetypeID"])


class HistoryPersistTests(LiveCase):
    async def test_completion_persists_history_row(self):
        tdef = make_tdef()
        client = FakeClient()
        human = Participant(client, {"piles": {"deck": []}})
        bot = Participant(None, {"piles": {"deck": ["g"]}}, bot=True)
        t = LiveTournament(self.m, tdef, [human, bot])
        with patch("spirit.game.tournaments.live.run_db",
                   new=AsyncMock()) as db:
            await asyncio.wait_for(t._complete(human), 5)

        calls = [c for c in db.await_args_list
                 if getattr(c.args[0], "__name__", "") == "save_tournament_history"]
        self.assertEqual(len(calls), 1, "completion must persist one history row")
        _, tid, active_id, account_ids, ended_ms, payload = calls[0].args
        self.assertEqual(tid, tdef.tournament_id)
        self.assertEqual(active_id, t.active_id)
        self.assertCountEqual(account_ids, [human.account_id, bot.account_id])
        self.assertIsInstance(ended_ms, int)
        self.assertGreaterEqual(ended_ms, t.started_ms)

        self.assertEqual(payload["activeTournamentID"], t.active_id)
        self.assertEqual(payload["tournamentData"]["tournamentID"],
                         tdef.tournament_id)
        self.assertIsInstance(payload["rounds"], int)
        self.assertEqual(payload["roundLength"], 30)
        # J.G.L sorts by tournamentEnded (ms); renderer formats it as a date.
        self.assertEqual(payload["tournamentStarted"], t.started_ms)
        self.assertEqual(payload["tournamentEnded"], ended_ms)
        # players = final-standings order (champion first) as J.G+k identities.
        self.assertEqual(payload["players"][0]["accountID"], human.account_id)
        self.assertTrue(all(set(p) == {"accountID", "username"}
                            for p in payload["players"]))
        # prizeList must cover every participant: the client picks the
        # requester's entry by accountID and NREs on a missing Prizes.
        self.assertCountEqual(
            [e["accountIDUsername"]["accountID"] for e in payload["prizeList"]],
            [human.account_id, bot.account_id])
        human_entry = next(e for e in payload["prizeList"]
                           if e["accountIDUsername"]["accountID"] == human.account_id)
        self.assertEqual(len(human_entry["prizes"]), 1)
        self.assertEqual(human_entry["prizes"][0]["rewardType"], "Tokens")
        bot_entry = next(e for e in payload["prizeList"]
                         if e["accountIDUsername"]["accountID"] == bot.account_id)
        self.assertEqual(bot_entry["prizes"], [], "bots never win prizes")
        # Bracket rows stay J.G.j shaped (winner/round/table/players[2]).
        for m in payload["matchups"]:
            self.assertIn("gameID", m)
            self.assertEqual(len(m["players"]), 2)
            self.assertIsNotNone(m["winner"])

    async def test_history_persist_failure_does_not_break_completion(self):
        tdef = make_tdef()
        client = FakeClient()
        human = Participant(client, {"piles": {"deck": []}})
        t = LiveTournament(self.m, tdef, [human])
        calls = {"n": 0}

        async def failing_run_db(fn, *args):
            calls["n"] += 1
            raise RuntimeError("db down")

        with patch("spirit.game.tournaments.live.run_db",
                   new=failing_run_db):
            await asyncio.wait_for(t._complete(human), 5)

        completed = [p for p in client.sent
                     if p.get("messageName") == "TournamentCompleted"]
        self.assertEqual(len(completed), 1,
                         "a history failure must not swallow the results packet")


class HistoryDbTests(unittest.TestCase):
    def setUp(self):
        from spirit.database import Base, engine, db_session, TournamentHistory
        Base.metadata.create_all(engine)
        self.db_session = db_session
        self.TournamentHistory = TournamentHistory
        self.active_id = str(uuid.uuid4())
        self.account = str(uuid.uuid4())
        self.other = str(uuid.uuid4())

    def tearDown(self):
        with self.db_session() as session:
            session.query(self.TournamentHistory).filter_by(
                active_id=self.active_id).delete()

    def test_save_and_filter_by_account(self):
        from spirit.database.tournament_data import (
            save_tournament_history, get_tournament_history,
        )
        payload = {"activeTournamentID": self.active_id, "players": [],
                   "tournamentEnded": 123}
        save_tournament_history("tid-hist", self.active_id,
                                [self.account], 123, payload)
        # Same-shape row for someone else's bracket must never surface.
        other_active = str(uuid.uuid4())
        try:
            save_tournament_history("tid-hist", other_active,
                                    [self.other], 456,
                                    {"activeTournamentID": other_active})
            mine = get_tournament_history(self.account)
            self.assertEqual([p["activeTournamentID"] for p in mine],
                             [self.active_id])
            self.assertEqual(get_tournament_history(str(uuid.uuid4())), [])
        finally:
            with self.db_session() as session:
                session.query(self.TournamentHistory).filter_by(
                    active_id=other_active).delete()

    def test_upsert_by_run_id(self):
        from spirit.database.tournament_data import (
            save_tournament_history, get_tournament_history,
        )
        save_tournament_history("tid-hist", self.active_id,
                                [self.account], 1,
                                {"activeTournamentID": self.active_id, "v": 1})
        save_tournament_history("tid-hist", self.active_id,
                                [self.account, self.other], 2,
                                {"activeTournamentID": self.active_id, "v": 2})
        rows = get_tournament_history(self.account)
        matching = [p for p in rows
                    if p.get("activeTournamentID") == self.active_id]
        self.assertEqual(len(matching), 1, "same run id must upsert, not duplicate")
        with self.db_session() as session:
            count = (session.query(self.TournamentHistory).filter_by(
                active_id=self.active_id).count())
        self.assertEqual(count, 1)


class HistoryHandlerTests(unittest.TestCase):
    def test_sends_tournament_history_list(self):
        import asyncio
        from unittest.mock import patch
        from spirit.packets.handlers.tournaments import TournamentHandler

        class _Client:
            def __init__(self):
                self.player = type("P", (), {
                    "account_id": "acc-1", "username": "u",
                    "screen_name": "u", "wallet": None})()
                self.sent = []

            async def send_packet(self, packet, request_id=0, flags=None):
                self.sent.append(packet)

        client = _Client()
        handler = TournamentHandler(client)
        rows = [{"activeTournamentID": "x"}]
        with patch("spirit.packets.handlers.tournaments.run_db",
                   new=AsyncMock(return_value=rows)):
            asyncio.get_event_loop_policy().new_event_loop().run_until_complete(
                handler.handle_get_tournament_history_for_user(None, 7, None))

        self.assertEqual(len(client.sent), 1)
        packet = client.sent[0]
        self.assertEqual(packet["messageName"], "TournamentHistoryList")
        self.assertEqual(packet["tournamentHistoryList"], rows)


if __name__ == "__main__":
    unittest.main()
