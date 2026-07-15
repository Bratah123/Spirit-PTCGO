import logging
from spirit.network.message_names import InboundMsg, OutboundMsg
from spirit.game.session.manager import GameSessionManager
from .base import BaseHandler, handle

class GameplayHandler(BaseHandler):
    async def _forward_action(self, message, label):
        """Routes a player game action into their active GameSession."""
        account_id = self.client.player.account_id
        logging.info(f"[Gameplay] Player {self.client.player.username} made {label}: {message}")
        session = GameSessionManager().get_session_by_player_id(account_id)
        if session:
            await session.receive_player_action(
                account_id, message, client_handler=self.client
            )

    @handle(InboundMsg.PLAYER_READY)
    async def handle_player_ready(self, message, request_id, flags):
        account_id = self.client.player.account_id
        logging.info(f"[Gameplay] Player {self.client.player.username} ({account_id}) sends PlayerReady")

        session = GameSessionManager().get_session_by_player_id(account_id)
        if session:
            await session.mark_player_ready(account_id, client_handler=self.client)
        else:
            logging.warning(f"[Gameplay] PlayerReady received but player {account_id} has no active GameSession")

    @handle(InboundMsg.GAME_CUSTOM_CHOICE)
    async def handle_game_custom_choice(self, message, request_id, flags):
        await self._forward_action(message, "CustomChoice")

    @handle(InboundMsg.GAME_MULLIGAN_CHOICE)
    async def handle_game_mulligan_choice(self, message, request_id, flags):
        await self._forward_action(message, "MulliganChoice")

    @handle(InboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS)
    async def handle_selection_with_targets_and_actions(self, message, request_id, flags):
        await self._forward_action(message, "TargetSelection")

    @handle(InboundMsg.SELECTION_WITH_TARGETS)
    async def handle_selection_with_targets(self, message, request_id, flags):
        await self._forward_action(message, "TargetSelection")

    @handle(InboundMsg.RECONNECT_TO_GAME)
    async def handle_reconnect_to_game(self, message, request_id, flags):
        account_id = self.client.player.account_id
        game_id = message.get("gameID")
        logging.info(f"[Gameplay] Player {self.client.player.username} requests ReconnectToGame: {message}")

        session = GameSessionManager().get_session_by_player_id(account_id)
        if session is None or (game_id and session.game_id != game_id):
            logging.warning(f"[Gameplay] ReconnectToGame for {account_id}: no matching active session")
            await self.send({"messageName": OutboundMsg.PLAYER_NOT_IN_GAME.value})
            return

        await session.reconnect_player(self.client, account_id)

    @handle(InboundMsg.RESIGN_GAME)
    async def handle_resign_game(self, message, request_id, flags):
        account_id = self.client.player.account_id
        logging.info(f"[Gameplay] Player {self.client.player.username} Conceded/Resigned Match: {message}")
        session = GameSessionManager().get_session_by_player_id(account_id)
        if session:
            # Full EOG flow (GameCompletedMessage to both viewers, rewards,
            # ladder points); the session self-removes when the loop unwinds.
            await session.concede(account_id)
        else:
            GameSessionManager().remove_session_by_player_id(account_id)

    @handle(InboundMsg.GAME_CHAT)
    async def handle_game_chat(self, message, request_id, flags):
        account_id = self.client.player.account_id
        game_id = message.get("gameID")
        chat_msg = message.get("message")

        logging.info(f"[Gameplay] Player {self.client.player.username} sent GameChat in {game_id}: {chat_msg}")

        manager = GameSessionManager()
        session = manager.get_session_by_player_id(account_id)
        if session and session.game_id == game_id:
            payload = {
                "gameID": game_id,
                "userInfo": {
                    "accountID": account_id,
                    "displayName": self.client.player.screen_name
                },
                "message": chat_msg
            }
            await session.broadcast_packet(OutboundMsg.NOTIFY_GAME_CHAT.value, payload)

    @handle(InboundMsg.UPDATE_USER_TIMEOUT_STATUS)
    async def handle_update_user_timeout_status(self, message, request_id, flags):
        account_id = self.client.player.account_id
        logging.debug(f"[Gameplay] Player {self.client.player.username} updated user timeout status: {message}")
