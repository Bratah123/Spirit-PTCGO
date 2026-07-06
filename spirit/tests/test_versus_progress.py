import os
import tempfile
import unittest
from unittest.mock import patch

from spirit.game.models.versus import VersusSeason


def _season(season_id="TestSeason"):
    return VersusSeason.from_dict({
        "seasonID": season_id,
        "startTime": 0,
        "endTime": 4102444800000,
        "description": {"id": "Test"},
        "tiers": [
            {"rewards": {
                "10": [
                    {"name": "5 Tokens", "rewardType": "Tokens",
                     "rewardAmount": 5, "rewardCurrency": "prizeTrainerCoin"},
                    {"name": "Reward Card", "rewardType": "Archetype",
                     "rewardAmount": 2, "rewardProductID": "aaaa-bbbb"}
                ],
                "50": [
                    {"name": "20 Tokens", "rewardType": "Tokens",
                     "rewardAmount": 20, "rewardCurrency": "prizeTrainerCoin"}
                ]
            }},
        ],
        "resetRewardID": ""
    })


class TestVersusProgress(unittest.TestCase):
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

    def _new_account(self, name):
        from spirit.database.accounts import create_account
        return create_account(name, "pw123")["account_id"]

    def test_threshold_grants_once(self):
        from spirit.database import versus_data
        from spirit.database.player_data import get_wallet_by_account_id, get_collection_by_account_id

        account_id = self._new_account("versus_tester")
        season = _season()
        coins_before = get_wallet_by_account_id(account_id)["coins"]

        r = versus_data.award_match_points(account_id, True, season=season)
        self.assertEqual(r["points"], versus_data.VERSUS_POINTS_PER_WIN)
        self.assertEqual(r["granted"], [])

        # cross the 10-point tier
        while r["points"] < 10:
            r = versus_data.award_match_points(account_id, True, season=season)
        self.assertEqual(len(r["granted"]), 2)

        wallet = get_wallet_by_account_id(account_id)
        self.assertEqual(wallet["coins"], coins_before + 5)
        collection = {c["archetype_id"]: c for c in get_collection_by_account_id(account_id)}
        self.assertEqual(collection["aaaa-bbbb"]["nontradable_count"], 2)

        # further matches do not re-grant the crossed tier
        r = versus_data.award_match_points(account_id, False, season=season)
        self.assertEqual(r["granted"], [])
        wallet = get_wallet_by_account_id(account_id)
        self.assertEqual(wallet["coins"], coins_before + 5)

    def test_season_change_resets_points_keeps_all_time(self):
        from spirit.database import versus_data

        account_id = self._new_account("versus_resetter")
        r = versus_data.award_match_points(account_id, True, season=_season("SeasonA"))
        self.assertEqual(r["points"], 5)
        r = versus_data.award_match_points(account_id, True, season=_season("SeasonB"))
        self.assertEqual(r["points"], 5)  # reset by the new season
        self.assertEqual(r["all_time_points"], 10)

        points, all_time = versus_data.get_progress(account_id, "SeasonB")
        self.assertEqual((points, all_time), (5, 10))
        points, _ = versus_data.get_progress(account_id, "SeasonC")
        self.assertEqual(points, 0)

    def test_account_attributes_carry_season_points(self):
        from spirit.database import versus_data
        from spirit.game.account_attributes import build_account_attributes
        from spirit.game.attributes import AttrID
        from spirit.game.season_manager import VersusSeasonManager

        account_id = self._new_account("versus_attrs")
        active = VersusSeasonManager().get_active_season()
        self.assertIsNotNone(active)
        versus_data.award_match_points(account_id, True, season=active)

        attrs = {a["name"]: a["value"] for a in build_account_attributes(account_id)}
        self.assertEqual(attrs[AttrID.SEASON_POINTS.value], versus_data.VERSUS_POINTS_PER_WIN)
        self.assertEqual(attrs[AttrID.ALL_TIME_SEASON_POINTS.value], versus_data.VERSUS_POINTS_PER_WIN)
        self.assertIn(AttrID.FRIEND_CHAT_MODE.value, attrs)


class TestVersusSeasonWireShape(unittest.TestCase):
    """The client chevron renderers get_Item reward[0]'s ArchetypeID unguarded
    and sort rewards by the "index" field — the wire must order cards first,
    products next, tokens (null product) last."""

    def test_reward_ordering_null_tokens_and_indexes(self):
        from spirit.game.scripts.cards import loader as card_loader
        card_guid = card_loader.load_all()[0].guid
        season = VersusSeason.from_dict({
            "seasonID": "Wire", "startTime": 0, "endTime": 1, "description": {"id": "x"},
            "tiers": [{"rewards": {"10": [
                {"name": "5 Tokens", "rewardType": "Tokens", "rewardAmount": 5,
                 "rewardProductID": "00000000-0000-0000-0000-000000000000"},
                {"name": "A Pack", "rewardType": "Archetype", "rewardAmount": 1,
                 "rewardProductID": "d017c195-0000-0000-0000-000000000001"},
                {"name": "A Card", "rewardType": "Archetype", "rewardAmount": 1,
                 "rewardProductID": card_guid},
            ]}}]
        })
        rewards = season.to_dict()["tiers"][0]["rewards"]["10"]
        self.assertEqual([r["index"] for r in rewards], [0, 1, 2])
        self.assertEqual(rewards[0]["rewardProductID"].lower(), card_guid.lower())
        self.assertEqual(rewards[1]["rewardProductID"],
                         "d017c195-0000-0000-0000-000000000001")
        self.assertEqual(rewards[2]["rewardType"], "Tokens")
        # zero GUID must become null: ArchetypeID(Guid.Empty) is non-null
        # client-side and misses the archetype cache (KeyNotFoundException)
        self.assertIsNone(rewards[2]["rewardProductID"])

    def test_tokens_without_product_id_serialize_null(self):
        from spirit.game.models.versus import Reward
        r = Reward(name="5 Tokens", reward_type="Tokens", reward_amount=5)
        self.assertIsNone(r.to_dict()["rewardProductID"])


if __name__ == "__main__":
    unittest.main()
