"""Daily challenge definitions and recovered client payloads."""

import json
from functools import lru_cache
from pathlib import Path

CATALOG_PATH = Path(__file__).resolve().parents[1] / "database/json_data/daily_challenges.json"
MAX_ACTIVE = 3
XP_LEVELS = {1: 5, 2: 10, 3: 20, 4: 35, 5: 50}
AFFINITIES = "Colorless Darkness Dragon Fairy Fighting Fire Grass Lightning Metal Psychic Water".split()
STATS = {"wins", "damagedealt", "energyplayed", "trainersplayed", "prizecardstaken"}


@lru_cache(maxsize=1)
def load_catalog():
    """Loads validated challenge templates; restart the server after editing."""
    rows = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    keys = set()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("key"), str) or not row["key"]:
            raise ValueError("Each daily challenge needs a nonempty key")
        if row["key"] in keys or row.get("stat") not in STATS:
            raise ValueError(f"Duplicate key or unsupported stat: {row['key']}")
        keys.add(row["key"])
        for name in ("title", "description"):
            if not isinstance(row.get(name), str) or not row[name]:
                raise ValueError(f"Challenge {row['key']} needs {name}")
        for name, minimum in (("target", 1), ("coins", 1), ("xp", 0)):
            if type(row.get(name)) is not int or not minimum <= row[name] <= 100000:
                raise ValueError(f"Invalid {name} for challenge {row['key']}")
    if len(rows) < 2:
        raise ValueError("Daily challenges need at least two templates")
    return rows


def coin_reward(amount, source=""):
    return {
        "name": "DailyChallengeReward", "rewardType": "Tokens", "rewardAmount": amount,
        "rewardProductID": None, "rewardCurrency": "Tokens",
        "rewardDescription": {"id": "QuestCompleted"}, "rewardReason": "QuestCompleted",
        "selectedFrom": [], "selectedIndex": 0, "rewardSource": source,
        "index": 0, "openedReward": None,
    }


def quest_payload(row):
    template = row.definition
    return {
        "questDefinition": {
            "questID": row.quest_id, "name": f"SpiritDaily_{row.quest_id}",
            "title": {"id": template["title"]}, "description": {"id": template["description"]},
            "rewards": [coin_reward(template["coins"], row.quest_id)],
            "affinity": "Colorless", "xp": template["xp"], "tier": 1,
            "startTime": None, "endTime": None, "priority": "Bronze", "abandonable": True,
            "gameModes": ["PvPMatch", "TournamentMatch"],
            "questInformation": {"id": "Progress counts in multiplayer matches started after accepting. Unfinished challenges carry over; choose one new challenge per UTC day."},
        },
        "currentProgress": {
            "questID": row.quest_id, "activations": row.activations,
            "requiredActivations": template["target"],
        },
    }


def configuration(next_available_ms):
    return {
        "xpLevelMap": {str(k): v for k, v in XP_LEVELS.items()},
        "levelTierMap": {"0": 1, "3": 1, "5": 1, "8": 1, "10": 1},
        "affinityToAffinityLevelRewardsMap": {
            affinity: {str(level): [coin_reward(25)] for level in XP_LEVELS}
            for affinity in AFFINITIES
        },
        "nextQuestAvailableTime": next_available_ms,
        "levelActiveQuestsMap": {"1": -1, "2": -1, "3": 2147483647},
    }
