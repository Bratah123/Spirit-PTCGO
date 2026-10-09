"""Win streaks + daily versus rewards: counters, tiers, wire payloads, gates."""
import asyncio
import datetime
import unittest
import uuid
from types import SimpleNamespace

DAY1 = datetime.datetime(2026, 10, 9, 10, 0, tzinfo=datetime.timezone.utc)
DAY2 = datetime.datetime(2026, 10, 10, 12, 0, tzinfo=datetime.timezone.utc)
NEXT_MIDNIGHT = int(datetime.datetime(
    2026, 10, 10, tzinfo=datetime.timezone.utc).timestamp() * 1000)


def _outcome(**overrides):
    base = {"updated": True, "streak": 3, "daily_wins": 3,
            "daily_last_win_ms": 123, "crossed": 3,
            "granted": [{"name": "750 Tokens", "rewardType": "Tokens",
                         "rewardAmount": 750}]}
    base.update(overrides)
    return base


class StreakDailyDbTests(unittest.TestCase):
    def setUp(self):
        from spirit.database import Base, engine, db_session, Wallet, VersusProgress
        Base.metadata.create_all(engine)
        self.db_session = db_session
        self.Wallet = Wallet
        self.VersusProgress = VersusProgress
        self.account = str(uuid.uuid4())

    def tearDown(self):
        with self.db_session() as session:
            for model in (self.VersusProgress, self.Wallet):
                session.query(model).filter_by(account_id=self.account).delete()
            from spirit.database import Collection
            session.query(Collection).filter_by(account_id=self.account).delete()

    def _state(self, now=None):
        from spirit.database.versus_data import get_streak_state
        return get_streak_state(self.account, now=now)

    def _coins(self):
        with self.db_session() as session:
            wallet = session.query(self.Wallet).filter_by(
                account_id=self.account).first()
            return wallet.coins if wallet else 0

    def test_win_loss_streak_and_daily_counters(self):
        from spirit.database.versus_data import record_match_outcome
        r = record_match_outcome(self.account, True, True, now=DAY1)
        self.assertTrue(r["updated"])
        self.assertEqual((r["streak"], r["daily_wins"]), (1, 1))
        self.assertGreater(r["daily_last_win_ms"], 0)
        self.assertEqual(r["crossed"], 1, "win 1 crosses the first track tier")

        r = record_match_outcome(self.account, True, True, now=DAY1)
        self.assertEqual((r["streak"], r["daily_wins"]), (2, 2))

        r = record_match_outcome(self.account, False, True, now=DAY1)
        self.assertEqual(r["streak"], 0, "a counted loss resets the streak")
        self.assertEqual(r["daily_wins"], 2, "a loss never rolls daily wins back")

    def test_non_counting_match_never_touches_state(self):
        from spirit.database.versus_data import record_match_outcome
        record_match_outcome(self.account, True, True, now=DAY1)
        for won in (False, False, True):
            r = record_match_outcome(self.account, won, False, now=DAY1)
            self.assertFalse(r["updated"])
        state = self._state(DAY1)
        self.assertEqual((state["streak"], state["daily_wins"]), (1, 1),
                         "practice/tournament matches leave streaks untouched")

    def test_daily_wins_roll_on_utc_day_change(self):
        from spirit.database.versus_data import record_match_outcome
        record_match_outcome(self.account, True, True, now=DAY1)
        display = self._state(DAY2)
        self.assertEqual(display["daily_wins"], 0,
                         "display rolls to 0 after midnight without a write")
        self.assertEqual(display["streak"], 1, "streak survives the day roll")

        r = record_match_outcome(self.account, True, True, now=DAY2)
        self.assertEqual((r["streak"], r["daily_wins"]), (2, 1),
                         "the counted match persists the rolled day")

    def test_daily_tiers_grant_in_sequence(self):
        from spirit.database.versus_data import record_match_outcome
        crossed = []
        for i in range(6):
            r = record_match_outcome(self.account, True, True, now=DAY1)
            crossed.append(r["crossed"])
            if i < 4:
                # 250 / 750 / 1500 / 2500 cumulative token milestones
                self.assertEqual(self._coins(), sum((250, 500, 750, 1000)[:i + 1]))
            else:
                self.assertEqual(self._coins(), 2500,
                                 "the tier-5 booster adds no tokens")
        self.assertEqual(crossed, [1, 2, 3, 4, 5, None])
        from spirit.database import db_session, Collection
        with db_session() as session:
            granted = session.query(Collection).filter_by(
                account_id=self.account).count()
        self.assertEqual(granted, 1, "the special booster is granted exactly once")

    def test_loss_between_wins_does_not_regrant_a_tier(self):
        from spirit.database.versus_data import record_match_outcome
        record_match_outcome(self.account, True, True, now=DAY1)   # tier 1
        record_match_outcome(self.account, False, True, now=DAY1)  # streak reset
        r = record_match_outcome(self.account, True, True, now=DAY1)
        self.assertEqual(r["crossed"], 2, "daily wins continue after a loss")
        self.assertEqual(self._coins(), 750)

    def test_get_streak_state_defaults_for_unknown_account(self):
        state = self._state()
        self.assertEqual(state, {"streak": 0, "daily_wins": 0,
                                 "daily_last_win_ms": 0})


class StreakAttributeTests(unittest.TestCase):
    def test_build_account_attributes_includes_streak_entries(self):
        from spirit.game.attributes import AttrID
        from spirit.game.progression.account import build_account_attributes
        account_id = str(uuid.uuid4())
        attrs = {a["name"]: a["value"]
                 for a in build_account_attributes(account_id)}
        self.assertEqual(attrs[AttrID.WIN_STREAK.value],
                         {"winStreak": False, "streakLength": 0})
        self.assertEqual(attrs[AttrID.DAILY_TRACK_PROGRESS.value],
                         {"wins": 0, "mostRecentWin": 0})

    def test_streak_attribute_values_helper_shapes(self):
        from spirit.game.attributes import AttrID
        from spirit.game.session.game_session import _streak_attribute_values
        attrs = {a["name"]: a["value"]
                 for a in _streak_attribute_values(_outcome())}
        self.assertEqual(attrs[AttrID.WIN_STREAK.value],
                         {"winStreak": True, "streakLength": 3})
        self.assertEqual(attrs[AttrID.DAILY_TRACK_PROGRESS.value],
                         {"wins": 3, "mostRecentWin": 123})

    def test_zero_streak_is_not_a_win_streak(self):
        from spirit.game.session.game_session import _streak_attribute_values
        attrs = {a["name"]: a["value"]
                 for a in _streak_attribute_values(_outcome(streak=0))}
        self.assertFalse(attrs[202010]["winStreak"])


class DailyTrackPayloadTests(unittest.TestCase):
    def test_payload_wire_shape_and_expiry(self):
        from spirit.game.progression.daily_versus import DailyVersusTrack
        payload = DailyVersusTrack().payload(DAY1)
        self.assertEqual(payload["nextExpiry"], NEXT_MIDNIGHT,
                         "expiry is the next UTC midnight in epoch ms")
        track = payload["dailyRewardTrack"]
        self.assertTrue(track["isDefault"])
        tiers = track["rewardTiers"]
        self.assertEqual([t["wins"] for t in tiers], [1, 2, 3, 4, 5])
        for i, tier in enumerate(tiers):
            self.assertEqual(
                set(tier), {"wins", "rewards", "isDefaultReward",
                           "isSpecialReward"},
                "wire keys are isDefaultReward/isSpecialReward (JsonName)")
            self.assertEqual(tier["isSpecialReward"], i == len(tiers) - 1)
            self.assertEqual(tier["isDefaultReward"], i != len(tiers) - 1)
            reward = tier["rewards"][0]
            self.assertIn("rewardType", reward)
            self.assertIn("rewardAmount", reward)

    def test_special_default_tier_amounts(self):
        from spirit.game.progression.daily_versus import DailyVersusTrack
        tiers = DailyVersusTrack().payload()["dailyRewardTrack"]["rewardTiers"]
        self.assertEqual([t["rewards"][0]["rewardAmount"] for t in tiers],
                         [250, 500, 750, 1000, 1])
        self.assertEqual(tiers[4]["rewards"][0]["rewardType"], "RandomBooster")

    def test_parse_tiers_rejects_noncontiguous_wins(self):
        from spirit.game.progression.daily_versus import parse_tiers
        with self.assertRaises(ValueError):
            parse_tiers([{"wins": 2, "rewards": [
                {"name": "x", "rewardType": "Tokens", "rewardAmount": 1}]}])

    def test_tier_for_wins_lookup(self):
        from spirit.game.progression.daily_versus import DailyVersusTrack
        track = DailyVersusTrack()
        self.assertIsNotNone(track.tier_for_wins(1))
        self.assertIsNotNone(track.tier_for_wins(5))
        self.assertIsNone(track.tier_for_wins(6))


class CountsGateTests(unittest.TestCase):
    def _counts(self, pairing, reason="winner conceded", turn=5):
        from spirit.game.session.game_session import GameSession
        session = GameSession.__new__(GameSession)
        session.pairing = pairing
        session.turn_state = SimpleNamespace(turn_number=turn)
        return session._streak_counts(reason)

    def test_queue_and_friend_matches_count(self):
        self.assertTrue(self._counts({}))
        self.assertTrue(self._counts({"queue_name": "Standard"}))
        self.assertTrue(self._counts({"queue_name": "Friend"}))
        self.assertTrue(self._counts({"is_solo": True,
                                      "solitaire_id": "queue_ai",
                                      "queue_name": "Standard"}))

    def test_practice_and_tournaments_never_count(self):
        self.assertFalse(self._counts({"queue_name": "SinglePlayer"}))
        self.assertFalse(self._counts({"tournament": {"tournament_id": "t"}}))
        self.assertFalse(self._counts({"legacy_tournament": {"tournament_id": "t"}}))

    def test_game_error_and_turn_zero_never_count(self):
        self.assertFalse(self._counts({}, reason="A game error occurred."))
        self.assertFalse(self._counts({}, turn=0))


class GameOptionsStreakTests(unittest.TestCase):
    def test_emits_game_extras_win_streak_keys(self):
        from spirit.game.session.game_session import GameSession
        from spirit.game.session.network_player import NetworkPlayer

        class _Client:
            def __init__(self, account_id):
                self.player = SimpleNamespace(
                    account_id=account_id, username="Tester",
                    screen_name="Tester", avatar_decks=None)
                self.running = True

        network_player = NetworkPlayer(_Client("acct-1"), {})
        bot = SimpleNamespace(screen_name="Spirit AI Bot", avatar_items=[],
                              sleeve_id="s", coin_id="c", deckbox_id="d")
        session = GameSession.__new__(GameSession)
        session.players = {"acct-1": network_player, "bot": bot}
        session.board_state = SimpleNamespace(
            find_player_entity=lambda pid: None)
        session.pairing = {}
        session._rating_cache = {"acct-1": 1400}
        session._streak_cache = {"acct-1": 3}

        options = session._build_game_options()
        self.assertEqual(options["gameExtrasWinStreak_acct-1"], "3")
        self.assertEqual(options["gameExtrasWinStreak_bot"], "0",
                         "bots emit the key as '0' so ContainsKey reads work")
        self.assertEqual(options["eloRating_acct-1"], "1400")


class EogFlagEntryTests(unittest.TestCase):
    def test_flag_entry_wire_shape(self):
        from spirit.game.session.game_session import _daily_track_reward_entry
        entry = _daily_track_reward_entry(_outcome())
        self.assertEqual(entry["name"], "DailyRewardTrackReward")
        self.assertEqual(entry["rewardReason"], "DailyRewardTrackReward")
        self.assertEqual(entry["rewardType"], "DailyRewardTrack")
        self.assertEqual(entry["rewardAmount"], 750)
        self.assertIsNotNone(entry["rewardDescription"])

    def test_flag_amount_sums_only_token_rewards(self):
        from spirit.game.session.game_session import _daily_track_reward_entry
        granted = [{"rewardType": "Tokens", "rewardAmount": 250},
                   {"rewardType": "RandomBooster", "rewardAmount": 1}]
        entry = _daily_track_reward_entry(_outcome(granted=granted))
        self.assertEqual(entry["rewardAmount"], 250)


class DailyTrackHandlerTests(unittest.TestCase):
    def test_sends_track_refresh_plus_attribute_delta(self):
        from spirit.packets.handlers.versus import VersusHandler

        class _Client:
            def __init__(self):
                self.player = SimpleNamespace(account_id=str(uuid.uuid4()),
                                              username="u")
                self.sent = []

            async def send_packet(self, packet, request_id=0, flags=None):
                self.sent.append(packet)

        client = _Client()
        handler = VersusHandler(client)
        asyncio.get_event_loop_policy().new_event_loop().run_until_complete(
            handler.handle_request_daily_track(None, 7, None))

        self.assertEqual(len(client.sent), 2,
                         "track refresh AND the attribute delta are required")
        track, delta = client.sent
        self.assertEqual(track["messageName"], "CurrentDailyRewardTrack")
        self.assertIn("dailyRewardTrack", track)
        self.assertIn("nextExpiry", track)
        self.assertEqual(delta["messageName"], "AccountPropertiesUpdated")
        self.assertEqual(delta["accountID"], client.player.account_id)
        names = {a["name"] for a in delta["attributes"]}
        self.assertEqual(names, {202010, 202190})

    def test_requires_login(self):
        from spirit.packets.handlers.versus import VersusHandler

        class _Client:
            player = None

            async def send_packet(self, packet, request_id=0, flags=None):
                raise AssertionError("must not reply when logged out")

        handler = VersusHandler(_Client())
        asyncio.get_event_loop_policy().new_event_loop().run_until_complete(
            handler.handle_request_daily_track(None, 7, None))


if __name__ == "__main__":
    unittest.main()
