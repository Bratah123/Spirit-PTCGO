from spirit.game.attributes import AttrID
from spirit.database.versus_data import get_progress
from spirit.database.quests import account_quest_attributes
from spirit.database.player_data import get_account_settings, get_screen_name, merge_account_settings
from spirit.game.progression.seasons import VersusSeasonManager

# Client setting numbers inside the account-settings dict (attr 10230, K.L.GetSetting)
VERSUS_LAST_SEEN_POINTS_SETTING = 109  # LastKnownSeasonPointTotal (ladder animation anchor)
VERSUS_SEEN_SEASON_SETTINGS = (111, 112, 113, 114)  # start hi/lo, end hi/lo
FALLBACK_SEASON = {
    "seasonID": "Season1",
    "startTime": 1,
    "endTime": 4102444800000,
    "description": {"id": "SpiritPTCGO Season"},
    "tiers": [],
    "resetRewardID": "",
}


def client_season_payload():
    """CurrentVersusSeason payload for the active season."""
    season = VersusSeasonManager().get_active_season()
    return season.client_dict() if season else dict(FALLBACK_SEASON)


def _split_long(value):
    low = ((value & 0xFFFFFFFF) ^ 0x80000000) - 0x80000000
    return value >> 32, low


def acknowledge_versus_season(account_id):
    """LOGIN-ONLY, after attributes are built: store the season the new-season dialog compares against."""
    payload = client_season_payload()
    start_hi, start_lo = _split_long(payload["startTime"])
    end_hi, end_lo = _split_long(payload["endTime"])
    seen = dict(zip(VERSUS_SEEN_SEASON_SETTINGS, (start_hi, start_lo, end_hi, end_lo)))
    stored = get_account_settings(account_id)
    if any(stored.get(str(key)) != value for key, value in seen.items()):
        merge_account_settings(account_id, seen)


def anchor_versus_animation(account_id):
    """LOGIN-ONLY: set the client's LastKnownSeasonPointTotal (setting 109) to the
    player's current season points so the versus ladder never replays its
    points/reward animation on relog. In-session gains still animate because the
    mid-game AccountUpdated leaves 109 stale (it never re-runs this)."""
    season = VersusSeasonManager().get_active_season()
    points, _ = get_progress(
        account_id, season.season_id if season else "")
    merge_account_settings(account_id, {VERSUS_LAST_SEEN_POINTS_SETTING: points})
    return points


def build_account_attributes(account_id):
    """Full SerializableAccount attribute list (AccountUpdated ReplaceWith
    swaps the whole set, so every sender must include everything)."""

    quest_state = account_quest_attributes(account_id)
    season = VersusSeasonManager().get_active_season()
    points, all_time = get_progress(
        account_id, season.season_id if season else "")
    return [
        {"name": AttrID.ACCOUNT_SETTINGS.value, "value": get_account_settings(account_id)},
        {"name": AttrID.SCREEN_NAME.value, "value": get_screen_name(account_id)},
        {"name": AttrID.FRIEND_CHAT_MODE.value, "value": "OpenChat"},
        {"name": AttrID.FRIEND_MODE.value, "value": "Open"},
        {"name": AttrID.FRIEND_TRADE_MODE.value, "value": "Free"},
        {"name": AttrID.GAME_CHAT_MODE.value, "value": "OpenChat"},
        {"name": AttrID.PUBLIC_CHAT_MODE.value, "value": "OpenChat"},
        {"name": AttrID.SHOPPING_MODE.value, "value": "Open"},
        {"name": AttrID.TRADE_MODE.value, "value": "Free"},
        {"name": AttrID.PRIVATE_MESSAGING_MODE.value, "value": "OpenChat"},
        {"name": AttrID.DECK_SHARE_MODE.value, "value": "Everybody"},
        {"name": AttrID.SEASON_POINTS.value, "value": points},
        {"name": AttrID.ALL_TIME_SEASON_POINTS.value, "value": all_time},
        {"name": AttrID.QUESTS_ENABLED.value, "value": quest_state["enabled"]},
        {"name": AttrID.QUEST_AFFINITY_XP.value, "value": quest_state["xp"]},
    ]
