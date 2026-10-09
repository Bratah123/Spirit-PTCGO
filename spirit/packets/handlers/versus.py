"""Daily versus reward track request handlers."""

from spirit.database.async_utils import run_db
from spirit.database.versus_data import get_streak_state
from spirit.game.attributes import AttrID
from spirit.game.progression.daily_versus import DailyVersusTrack
from spirit.network.message_names import InboundMsg, OutboundMsg
from .base import BaseHandler, handle


class VersusHandler(BaseHandler):
    @handle(InboundMsg.REQUEST_CURRENT_DAILY_REWARD_TRACK)
    async def handle_request_daily_track(self, message, request_id, flags):
        """Day-rollover refresh: the client only sends this when its cached
        nextExpiry <= server now, then waits for BOTH a fresh
        CurrentDailyRewardTrack AND an AccountPropertiesUpdated containing the
        daily-wins attribute before restarting the daily timer."""
        if self.client.player is None:
            return
        account_id = self.client.player.account_id
        state = await run_db(get_streak_state, account_id)
        await self.send({
            "messageName": OutboundMsg.CURRENT_DAILY_REWARD_TRACK.value,
            **DailyVersusTrack().payload(),
        }, request_id)
        await self.send({
            "messageName": OutboundMsg.ACCOUNT_PROPERTIES_UPDATED.value,
            "accountID": account_id,
            "attributes": [
                {"name": AttrID.WIN_STREAK.value,
                 "value": {"winStreak": state["streak"] > 0,
                           "streakLength": state["streak"]}},
                {"name": AttrID.DAILY_TRACK_PROGRESS.value,
                 "value": {"wins": state["daily_wins"],
                           "mostRecentWin": state["daily_last_win_ms"]}},
            ],
        })
