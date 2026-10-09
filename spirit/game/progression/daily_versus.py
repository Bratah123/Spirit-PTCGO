"""Daily versus reward track (wins-based, resets each UTC day).

Server-side config + wire payload for CurrentDailyRewardTrack. The client
derives the displayed win requirement from each tier's ARRAY INDEX + 1, so
tiers must stay contiguous (1..N) in file order — the `wins` field is kept in
sync for validation and is what the server matches daily_wins against.
"""
import datetime
import json
import logging
import os
from typing import Dict, List, Optional

from spirit.game.models.versus import Reward

REWARDS_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'database', 'json_data',
    'daily_versus_rewards.json'
))

# Same set the daily-login loader accepts (A.w.parsePrizeData renders anything
# else as an UnSet slot with amount -1).
VALID_REWARD_TYPES = {"Tokens", "TournamentTicket", "RandomBooster", "Archetype"}

DEFAULT_TIERS_JSON = [
    {"wins": 1,
     "rewards": [{"name": "250 Tokens", "rewardType": "Tokens", "rewardAmount": 250}]},
    {"wins": 2,
     "rewards": [{"name": "500 Tokens", "rewardType": "Tokens", "rewardAmount": 500}]},
    {"wins": 3,
     "rewards": [{"name": "750 Tokens", "rewardType": "Tokens", "rewardAmount": 750}]},
    {"wins": 4,
     "rewards": [{"name": "1000 Tokens", "rewardType": "Tokens", "rewardAmount": 1000}]},
    {"wins": 5, "isSpecial": True,
     "rewards": [{"name": "Booster Pack", "rewardType": "RandomBooster",
                  "rewardAmount": 1}]},
]


def parse_tiers(data) -> List[Dict]:
    """Validates a wins-track list into [{wins, rewards: [Reward], is_special}]."""
    if not isinstance(data, list) or not data:
        raise ValueError("daily versus track must be a non-empty list")
    tiers = []
    for i, entry in enumerate(data):
        wins = int(entry.get("wins", 0))
        if wins != i + 1:
            raise ValueError(
                f"daily versus tier {i}: wins must be contiguous 1..N (got {wins})")
        raw = entry.get("rewards")
        if not isinstance(raw, list) or not raw:
            raise ValueError(f"daily versus tier {wins}: rewards must be non-empty")
        rewards = [Reward.from_dict(r) for r in raw]
        for r in rewards:
            if r.reward_type not in VALID_REWARD_TYPES:
                raise ValueError(
                    f"daily versus tier {wins}: invalid rewardType '{r.reward_type}'")
            if r.reward_type == "Archetype" and not r.reward_product_id:
                raise ValueError(
                    f"daily versus tier {wins}: Archetype reward needs rewardProductID")
        tiers.append({
            "wins": wins,
            "rewards": rewards,
            "is_special": bool(entry.get(
                "isSpecial", wins == int(data[-1].get("wins", 0)))),
        })
    return tiers


class DailyVersusTrack:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DailyVersusTrack, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.tiers: List[Dict] = parse_tiers(DEFAULT_TIERS_JSON)
        self.load_tiers()

    def load_tiers(self, path: str = REWARDS_PATH):
        if not os.path.exists(path):
            logging.info("[DailyVersus] %s not found; using built-in default track",
                         path)
            self.tiers = parse_tiers(DEFAULT_TIERS_JSON)
            return
        try:
            with open(path, 'r') as f:
                self.tiers = parse_tiers(json.load(f))
            logging.info("[DailyVersus] Loaded daily versus track from %s", path)
        except Exception as e:
            logging.error("[DailyVersus] Invalid daily_versus_rewards.json, "
                          f"using defaults: {e}")
            self.tiers = parse_tiers(DEFAULT_TIERS_JSON)

    def tier_for_wins(self, wins: int) -> Optional[Dict]:
        for tier in self.tiers:
            if tier["wins"] == wins:
                return tier
        return None

    @staticmethod
    def next_expiry_ms(now: Optional[datetime.datetime] = None) -> int:
        """Next UTC midnight in epoch ms (client countdown WargTime.FromMilliseconds)."""
        now = now or datetime.datetime.now(datetime.timezone.utc)
        today = now.astimezone(datetime.timezone.utc).date()
        midnight = datetime.datetime.combine(
            today + datetime.timedelta(days=1), datetime.time.min,
            tzinfo=datetime.timezone.utc)
        return int(midnight.timestamp() * 1000)

    def payload(self, now: Optional[datetime.datetime] = None) -> Dict:
        """CurrentDailyRewardTrack message body (wire keys per DailyRewardTier)."""
        return {
            "dailyRewardTrack": {
                "name": "Standard Track",
                "rewardTiers": [
                    {
                        "wins": tier["wins"],
                        "rewards": [r.to_dict(index=i)
                                    for i, r in enumerate(tier["rewards"])],
                        "isDefaultReward": not tier["is_special"],
                        "isSpecialReward": tier["is_special"],
                    }
                    for tier in self.tiers
                ],
                "isDefault": True,
            },
            "nextExpiry": self.next_expiry_ms(now),
        }
