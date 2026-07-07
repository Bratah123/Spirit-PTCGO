from spirit.game.attributes import AttrID
from spirit.database import versus_data
from spirit.database.player_data import get_account_settings, get_screen_name, merge_account_settings
from spirit.game.season_manager import VersusSeasonManager

# Client setting numbers inside the account-settings dict (attr 10230, K.L.GetSetting)
VERSUS_LAST_SEEN_POINTS_SETTING = 109  # LastKnownSeasonPointTotal (ladder animation anchor)


def anchor_versus_animation(account_id):
    """LOGIN-ONLY: set the client's LastKnownSeasonPointTotal (setting 109) to the
    player's current season points so the versus ladder never replays its
    points/reward animation on relog. In-session gains still animate because the
    mid-game AccountUpdated leaves 109 stale (it never re-runs this)."""
    season = VersusSeasonManager().get_active_season()
    points, _ = versus_data.get_progress(
        account_id, season.season_id if season else "")
    merge_account_settings(account_id, {VERSUS_LAST_SEEN_POINTS_SETTING: points})
    return points


def build_account_attributes(account_id):
    """Full SerializableAccount attribute list (AccountUpdated ReplaceWith
    swaps the whole set, so every sender must include everything)."""

    season = VersusSeasonManager().get_active_season()
    points, all_time = versus_data.get_progress(
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
    ]
