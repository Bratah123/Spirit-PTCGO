"""Native daily challenge request handlers."""

from spirit.database import quests
from spirit.database.async_utils import run_db
from spirit.game.account_attributes import build_account_attributes
from spirit.network.message_names import InboundMsg, OutboundMsg
from .base import BaseHandler, handle


class QuestHandler(BaseHandler):
    async def _send_snapshot(self, snapshot, request_id):
        await self.send({"messageName": OutboundMsg.QUEST_CONFIGURATION_UPDATED.value,
                         "questConfiguration": snapshot["configuration"]})
        await self.send({"messageName": OutboundMsg.ALL_QUESTS.value,
                         **snapshot["quests"]}, request_id)

    @handle(InboundMsg.GET_QUESTS)
    async def handle_get_quests(self, message, request_id, flags):
        if self.client.player is None:
            return
        snapshot = await run_db(quests.get_quests, self.client.player.account_id)
        await self._send_snapshot(snapshot, request_id)

    @handle(InboundMsg.GET_QUEST_CONFIGURATION_DATA)
    async def handle_get_configuration(self, message, request_id, flags):
        if self.client.player is None:
            return
        snapshot = await run_db(quests.get_quests, self.client.player.account_id)
        await self.send({"messageName": OutboundMsg.QUEST_CONFIGURATION_UPDATED.value,
                         "questConfiguration": snapshot["configuration"]}, request_id)

    @handle(InboundMsg.QUESTS_ENABLED)
    async def handle_quests_enabled(self, message, request_id, flags):
        if self.client.player is None or not isinstance(message, dict):
            return
        enabled = message.get("enabled")
        if type(enabled) is not bool:
            return await self.handle_get_quests(message, request_id, flags)
        player = self.client.player

        def update_enabled():
            snapshot = quests.set_enabled(player.account_id, enabled)
            return snapshot, build_account_attributes(player.account_id)

        snapshot, attributes = await run_db(update_enabled)
        await self.send({"messageName": OutboundMsg.ACCOUNT_UPDATED.value, "account": {
            "username": player.username, "accountID": player.account_id, "attributes": attributes,
        }})
        await self._send_snapshot(snapshot, request_id)

    @staticmethod
    def _quest_ids(message):
        ids = message.get("quests") if isinstance(message, dict) else None
        return ids if isinstance(ids, list) and all(isinstance(i, str) for i in ids) else []

    @handle(InboundMsg.QUESTS_SELECTED)
    async def handle_selected(self, message, request_id, flags):
        if self.client.player is None:
            return
        snapshot = await run_db(quests.select_quest, self.client.player.account_id,
                                self._quest_ids(message))
        await self._send_snapshot(snapshot, request_id)

    @handle(InboundMsg.ABANDON_QUESTS)
    async def handle_abandoned(self, message, request_id, flags):
        if self.client.player is None:
            return
        snapshot = await run_db(quests.abandon_quests, self.client.player.account_id,
                                self._quest_ids(message))
        await self._send_snapshot(snapshot, request_id)
