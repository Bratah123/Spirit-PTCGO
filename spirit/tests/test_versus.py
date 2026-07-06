import unittest
import os
import tempfile
import json
from spirit.game.models.versus import Reward, VersusTier, VersusSeason
from spirit.game.season_manager import VersusSeasonManager

class TestVersusModels(unittest.TestCase):
    def test_reward_serialization(self):
        data = {
            "name": "5 Tokens",
            "rewardType": "Tokens",
            "rewardAmount": 5,
            "rewardCurrency": "prizeTrainerCoin"
        }
        reward = Reward.from_dict(data)
        self.assertEqual(reward.name, "5 Tokens")
        self.assertEqual(reward.reward_type, "Tokens")
        self.assertEqual(reward.reward_amount, 5)
        self.assertEqual(reward.reward_currency, "prizeTrainerCoin")
        
        serialized = reward.to_dict()
        self.assertEqual(serialized["name"], "5 Tokens")
        self.assertEqual(serialized["rewardType"], "Tokens")
        self.assertEqual(serialized["rewardAmount"], 5)
        self.assertEqual(serialized["rewardCurrency"], "prizeTrainerCoin")

    def test_tier_serialization(self):
        data = {
            "rewards": {
                "10": [
                    {
                        "name": "5 Tokens",
                        "rewardType": "Tokens",
                        "rewardAmount": 5
                    }
                ]
            }
        }
        tier = VersusTier.from_dict(data)
        self.assertIn(10, tier.rewards)
        self.assertEqual(len(tier.rewards[10]), 1)
        self.assertEqual(tier.rewards[10][0].name, "5 Tokens")

        serialized = tier.to_dict()
        self.assertIn("10", serialized["rewards"])
        self.assertEqual(serialized["rewards"]["10"][0]["name"], "5 Tokens")

    def test_season_serialization(self):
        data = {
            "seasonID": "Season1",
            "startTime": 1000,
            "endTime": 5000,
            "description": {"id": "SpiritPTCGO Season"},
            "tiers": [
                {
                    "rewards": {
                        "10": [
                            {
                                "name": "5 Tokens",
                                "rewardType": "Tokens",
                                "rewardAmount": 5
                            }
                        ]
                    }
                }
            ],
            "resetRewardID": "Reset1"
        }
        season = VersusSeason.from_dict(data)
        self.assertEqual(season.season_id, "Season1")
        self.assertEqual(season.start_time, 1000)
        self.assertEqual(season.end_time, 5000)
        self.assertEqual(season.reset_reward_id, "Reset1")
        self.assertEqual(len(season.tiers), 1)

        serialized = season.to_dict()
        self.assertEqual(serialized["seasonID"], "Season1")
        self.assertEqual(serialized["tiers"][0]["rewards"]["10"][0]["name"], "5 Tokens")


class TestVersusSeasonManager(unittest.TestCase):
    def test_manager_singleton_and_loading(self):
        # Trigger initialization of singleton
        manager = VersusSeasonManager()
        self.assertIsNotNone(manager)
        
        # Verify active season returns either a season or None, without raising exceptions
        active = manager.get_active_season()
        # Since we just added versus_seasons.json with start_time=0 and end_time=4102444800000,
        # it should load and active should be Season1.
        if active is not None:
            self.assertEqual(active.season_id, "Season1")

if __name__ == "__main__":
    unittest.main()
