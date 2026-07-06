import datetime
import os
import tempfile
import unittest
from unittest.mock import patch

from spirit.game.daily_rewards import (
    DailyRewardManager, parse_tracks, VALID_REWARD_TYPES
)

TEST_TRACKS = {
    "newbie": [
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 100}],
        [{"name": "Card", "rewardType": "Archetype", "rewardAmount": 2,
          "rewardProductID": "aaaa-cccc"}],
        [{"name": "Ticket", "rewardType": "TournamentTicket", "rewardAmount": 1}],
    ],
    "standard": [
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 7}],
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 7}],
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 7}],
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 7}],
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 7}],
    ],
}


class TestDailyRewardTracks(unittest.TestCase):
    def setUp(self):
        self.manager = DailyRewardManager()
        self.manager.tracks = parse_tracks(TEST_TRACKS)

    def tearDown(self):
        self.manager.load_tracks()

    def test_wire_shape(self):
        newbie = self.manager.weeks_rewards(1)
        self.assertEqual(len(newbie), 3)
        standard = self.manager.weeks_rewards(4)
        self.assertEqual(len(standard), 5)
        for day in newbie + standard:
            self.assertTrue(day)
            for i, reward in enumerate(day):
                self.assertIn(reward["rewardType"], VALID_REWARD_TYPES)
                self.assertEqual(reward["index"], i)
                if reward["rewardType"] != "Archetype":
                    self.assertIsNone(reward["rewardProductID"])

    def test_reward_day_wraps_per_track(self):
        self.assertEqual(self.manager.reward_day(1, 1), 1)
        self.assertEqual(self.manager.reward_day(3, 3), 3)
        self.assertEqual(self.manager.reward_day(4, 3), 1)   # newbie track wraps at 3
        self.assertEqual(self.manager.reward_day(4, 4), 4)   # standard track
        self.assertEqual(self.manager.reward_day(6, 6), 1)   # standard wraps at 5

    def test_invalid_reward_type_rejected(self):
        bad = {**TEST_TRACKS, "newbie": [
            [{"name": "x", "rewardType": "Currency", "rewardAmount": 5}]] * 3}
        with self.assertRaises(ValueError):
            parse_tracks(bad)

    def test_wrong_day_count_rejected(self):
        bad = {**TEST_TRACKS, "standard": TEST_TRACKS["standard"][:4]}
        with self.assertRaises(ValueError):
            parse_tracks(bad)

    def test_archetype_requires_product_id(self):
        bad = {**TEST_TRACKS, "newbie": [
            [{"name": "x", "rewardType": "Archetype", "rewardAmount": 1}]] * 3}
        with self.assertRaises(ValueError):
            parse_tracks(bad)

    def test_multi_reward_day_must_be_all_archetype(self):
        bad = {**TEST_TRACKS, "newbie": [
            [{"name": "a", "rewardType": "Archetype", "rewardAmount": 1,
              "rewardProductID": "aaaa-cccc"},
             {"name": "t", "rewardType": "Tokens", "rewardAmount": 5}]] * 3}
        with self.assertRaises(ValueError):
            parse_tracks(bad)

    def test_bad_config_file_falls_back_to_defaults(self):
        fd, path = tempfile.mkstemp(suffix=".json")
        try:
            with os.fdopen(fd, "w") as f:
                f.write("{not json")
            self.manager.load_tracks(path)
            self.assertEqual(len(self.manager.tracks["newbie"]), 3)
            self.assertEqual(len(self.manager.tracks["standard"]), 5)
        finally:
            os.unlink(path)


class TestDailyLoginProgress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        cls.db_patcher = patch('spirit.database.connection.DB_PATH', cls.db_path)
        cls.db_patcher.start()
        from spirit.database.setup_db import setup_database
        setup_database()
        cls.manager = DailyRewardManager()
        cls.manager.tracks = parse_tracks(TEST_TRACKS)

    @classmethod
    def tearDownClass(cls):
        cls.manager.load_tracks()
        cls.db_patcher.stop()
        try:
            os.close(cls.db_fd)
            os.unlink(cls.db_path)
        except OSError:
            pass

    def _new_account(self, name):
        from spirit.database.accounts import create_account
        return create_account(name, "pw123")["account_id"]

    def _rewind_last_claim(self, account_id, days):
        from spirit.database import db_session
        from spirit.database.models.economy import DailyLoginProgress
        with db_session() as session:
            p = session.query(DailyLoginProgress).filter_by(account_id=account_id).first()
            p.last_claim_date = p.last_claim_date - datetime.timedelta(days=days)

    def test_claims_once_per_day(self):
        from spirit.database.daily_rewards import process_daily_login
        from spirit.database.player_data import get_wallet_by_account_id

        account_id = self._new_account("daily_tester")
        coins_before = get_wallet_by_account_id(account_id)["coins"]

        r = process_daily_login(account_id)
        self.assertTrue(r["firstDailyLogin"])
        self.assertEqual(r["activations"], 1)
        self.assertEqual(r["rewardDay"], 1)
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], coins_before + 100)

        r2 = process_daily_login(account_id)
        self.assertFalse(r2["firstDailyLogin"])
        self.assertEqual(r2["activations"], 1)
        self.assertEqual(get_wallet_by_account_id(account_id)["coins"], coins_before + 100)

    def test_streak_grants_and_newbie_transition(self):
        from spirit.database.daily_rewards import process_daily_login
        from spirit.database.player_data import (
            get_wallet_by_account_id, get_collection_by_account_id)

        account_id = self._new_account("daily_streaker")
        wallet = get_wallet_by_account_id(account_id)
        coins_before, tickets_before = wallet["coins"], wallet["tickets"]

        process_daily_login(account_id)                      # day 1: 100 tokens
        self._rewind_last_claim(account_id, 1)
        process_daily_login(account_id)                      # day 2: 2x archetype
        collection = {c["archetype_id"]: c for c in get_collection_by_account_id(account_id)}
        self.assertEqual(collection["aaaa-cccc"]["nontradable_count"], 2)

        self._rewind_last_claim(account_id, 1)
        r = process_daily_login(account_id)                  # day 3: ticket
        self.assertEqual(r["activations"], 3)
        self.assertEqual(
            get_wallet_by_account_id(account_id)["tickets"], tickets_before + 1)

        self._rewind_last_claim(account_id, 1)
        r = process_daily_login(account_id)                  # day 4: standard track
        self.assertEqual(r["activations"], 4)
        self.assertEqual(r["rewardDay"], 4)
        self.assertFalse(self.manager.is_newbie(r["activations"]))
        self.assertEqual(len(self.manager.weeks_rewards(r["activations"])), 5)
        self.assertEqual(
            get_wallet_by_account_id(account_id)["coins"], coins_before + 100 + 7)

    def test_streak_resets_after_gap(self):
        from spirit.database.daily_rewards import process_daily_login

        account_id = self._new_account("daily_lapser")
        process_daily_login(account_id)
        self._rewind_last_claim(account_id, 1)
        r = process_daily_login(account_id)
        self.assertEqual(r["rewardDay"], 2)

        self._rewind_last_claim(account_id, 3)
        r = process_daily_login(account_id)
        self.assertEqual(r["rewardDay"], 1)                  # streak reset
        self.assertEqual(r["activations"], 3)                # lifetime count kept

    def test_next_reward_timestamp_is_future_ms(self):
        from spirit.database.daily_rewards import process_daily_login
        import time

        account_id = self._new_account("daily_timer")
        r = process_daily_login(account_id)
        now_ms = time.time() * 1000
        self.assertGreater(r["nextRewardTimestampMs"], now_ms)
        self.assertLessEqual(r["nextRewardTimestampMs"], now_ms + 24 * 3600 * 1000)
