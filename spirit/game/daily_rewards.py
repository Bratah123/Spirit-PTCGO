import os
import json
import logging
from typing import Dict, List

from spirit.game.models.versus import Reward

REWARDS_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'database', 'json_data', 'daily_rewards.json'
))

# Client shows the 3-slot newbie dialog while activations <= 3, the 5-slot one after.
NEWBIE_MAX_ACTIVATIONS = 3
TRACK_DAYS = {"newbie": 3, "standard": 5}

# Any other rewardType renders an UnSet slot with amount -1 (A.w.parsePrizeData).
VALID_REWARD_TYPES = {"Tokens", "TournamentTicket", "RandomBooster", "Archetype"}

DEFAULT_TRACKS_JSON = {
    "newbie": [
        [{"name": "Welcome Tokens", "rewardType": "Tokens", "rewardAmount": 100}],
        [{"name": "Booster Pack", "rewardType": "RandomBooster", "rewardAmount": 1}],
        [{"name": "Event Ticket", "rewardType": "TournamentTicket", "rewardAmount": 1}],
    ],
    "standard": [
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 50}],
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 75}],
        [{"name": "Event Ticket", "rewardType": "TournamentTicket", "rewardAmount": 1}],
        [{"name": "Tokens", "rewardType": "Tokens", "rewardAmount": 100}],
        [{"name": "Booster Pack", "rewardType": "RandomBooster", "rewardAmount": 1}],
    ],
}


def parse_tracks(data: Dict) -> Dict[str, List[List[Reward]]]:
    """Validates a {track: [day: [reward, ...]]} config into Reward objects."""
    tracks = {}
    for track_name, day_count in TRACK_DAYS.items():
        days = data.get(track_name)
        if not isinstance(days, list) or len(days) != day_count:
            raise ValueError(f"track '{track_name}' must have exactly {day_count} days")
        parsed_days = []
        for i, day in enumerate(days):
            if not isinstance(day, list) or not day:
                raise ValueError(f"track '{track_name}' day {i + 1} must be a non-empty list")
            rewards = [Reward.from_dict(r) for r in day]
            for r in rewards:
                if r.reward_type not in VALID_REWARD_TYPES:
                    raise ValueError(
                        f"track '{track_name}' day {i + 1}: invalid rewardType '{r.reward_type}'")
                if r.reward_type == "Archetype" and not r.reward_product_id:
                    raise ValueError(
                        f"track '{track_name}' day {i + 1}: Archetype reward needs rewardProductID")
            # client sums a multi-reward day only when every entry is an Archetype
            if len(rewards) > 1 and any(r.reward_type != "Archetype" for r in rewards):
                raise ValueError(
                    f"track '{track_name}' day {i + 1}: multi-reward days must be all-Archetype")
            parsed_days.append(rewards)
        tracks[track_name] = parsed_days
    return tracks


class DailyRewardManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DailyRewardManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.tracks: Dict[str, List[List[Reward]]] = parse_tracks(DEFAULT_TRACKS_JSON)
        self.load_tracks()

    def load_tracks(self, path: str = REWARDS_PATH):
        if not os.path.exists(path):
            logging.info(f"[DailyRewards] {path} not found; using built-in default tracks")
            self.tracks = parse_tracks(DEFAULT_TRACKS_JSON)
            return
        try:
            with open(path, 'r') as f:
                self.tracks = parse_tracks(json.load(f))
            logging.info(f"[DailyRewards] Loaded daily reward tracks from {path}")
        except Exception as e:
            logging.error(f"[DailyRewards] Invalid daily_rewards.json, using defaults: {e}")
            self.tracks = parse_tracks(DEFAULT_TRACKS_JSON)

    def is_newbie(self, activations: int) -> bool:
        return activations <= NEWBIE_MAX_ACTIVATIONS

    def track_for(self, activations: int) -> List[List[Reward]]:
        return self.tracks["newbie" if self.is_newbie(activations) else "standard"]

    def reward_day(self, streak: int, activations: int) -> int:
        """1-indexed slot in the displayed track; wraps weekly."""
        return (max(streak, 1) - 1) % len(self.track_for(activations)) + 1

    def rewards_for(self, streak: int, activations: int) -> List[Reward]:
        return self.track_for(activations)[self.reward_day(streak, activations) - 1]

    def weeks_rewards(self, activations: int) -> List[List[Dict]]:
        """DailyLogin.weeksRewards wire shape: outer array = days, inner = that day's rewards."""
        return [[r.to_dict(index=i) for i, r in enumerate(day)]
                for day in self.track_for(activations)]
