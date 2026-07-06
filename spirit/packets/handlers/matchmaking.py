import logging
from spirit.network.message_names import InboundMsg
from spirit.game.session.manager import GameSessionManager
from .base import BaseHandler, handle

class MatchmakingHandler(BaseHandler):
    def _resolve_full_deck(self, client_deck: dict) -> dict:
        if not client_deck:
            return {}
        deck_id = client_deck.get("deckID") or client_deck.get("id")
        if self.client.player and deck_id:
            # Check normal decks
            for d in getattr(self.client.player, "decks", []):
                if d.get("id") == deck_id and d.get("deck_data"):
                    logging.info(f"[Matchmaking] Resolved full deck data '{d.get('name')}' ({deck_id}) from player profile.")
                    return d.get("deck_data")
            # Check avatar decks
            for d in getattr(self.client.player, "avatar_decks", []):
                if d.get("id") == deck_id and d.get("deck_data"):
                    logging.info(f"[Matchmaking] Resolved full avatar deck data '{d.get('name')}' ({deck_id}) from player profile.")
                    return d.get("deck_data")
        return client_deck

    @handle(InboundMsg.REQUEST_QUEUE_MATCH)
    async def handle_request_queue_match(self, message, request_id, flags):
        deck = self._resolve_full_deck(message.get("deck", {}))
        queue_name = message.get("queueName", "Standard")
        client_options = message.get("clientOptions", {})

        logging.info(f"[TCP] [{self.client.addr}] Player {self.client.player.username} requesting queue entry for '{queue_name}'")
        
        # Cleanly complete the RequestQueueMatch RPC first by returning an empty packet
        await self.client.send_packet({}, request_id)

        # Delegate to Matchmaking Manager with 0 as request_id so MatchQueueEntered is sent as an independent event
        manager = GameSessionManager()
        await manager.add_to_queue(self.client, queue_name, deck, client_options, 0)

    @handle(InboundMsg.REQUEST_SINGLE_PLAYER_MATCH)
    async def handle_request_single_player_match(self, message, request_id, flags):
        deck = self._resolve_full_deck(message.get("deck", {}))
        solitaire_id = str(message.get("solitaireID", "basic_bot_id"))
        match_options = message.get("matchOptions", {})

        logging.info(f"[TCP] [{self.client.addr}] Player {self.client.player.username} requesting solo match against AI {solitaire_id}")

        # Delegate to Matchmaking Manager
        manager = GameSessionManager()
        await manager.start_solo_match(self.client, deck, solitaire_id, match_options, request_id)

    @handle(InboundMsg.CANCEL_MATCH_REQUEST)
    async def handle_cancel_match_request(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Player {self.client.player.username} requesting matchmaking cancellation")

        # Delegate to Matchmaking Manager
        manager = GameSessionManager()
        await manager.remove_from_queue(self.client, send_left_packet=True)

    @handle(InboundMsg.REQUEST_MATCH_WITH_SPECIFIC_CLIENT)
    async def handle_request_match_with_specific_client(self, message, request_id, flags):
        deck = self._resolve_full_deck(message.get("deck", {}))
        opponent_id = str(message.get("opponentID", ""))
        match_options = message.get("matchOptions", {}) or {}

        logging.info(f"[TCP] [{self.client.addr}] Player {self.client.player.username} challenging {opponent_id}")
        await self.client.send_packet({}, request_id)
        await GameSessionManager().create_challenge(self.client, opponent_id, deck, match_options)

    @handle(InboundMsg.ACCEPT_MATCH_WITH_SPECIFIC_CLIENT)
    async def handle_accept_match_with_specific_client(self, message, request_id, flags):
        deck = self._resolve_full_deck(message.get("deck", {}))
        path = str(message.get("path", ""))

        logging.info(f"[TCP] [{self.client.addr}] Player {self.client.player.username} accepting challenge {path}")
        await self.client.send_packet({}, request_id)
        await GameSessionManager().accept_challenge(self.client, path, deck)

    @handle(InboundMsg.REJECT_MATCH_WITH_SPECIFIC_CLIENT)
    async def handle_reject_match_with_specific_client(self, message, request_id, flags):
        path = str(message.get("path", ""))
        logging.info(f"[TCP] [{self.client.addr}] Player {self.client.player.username} rejecting challenge {path}")
        await self.client.send_packet({}, request_id)
        await GameSessionManager().reject_challenge(self.client, path)

    @handle(InboundMsg.CANCEL_MATCH_REQUEST_WITH_SPECIFIC_CLIENT)
    async def handle_cancel_match_request_with_specific_client(self, message, request_id, flags):
        path = str(message.get("path", ""))
        logging.info(f"[TCP] [{self.client.addr}] Player {self.client.player.username} cancelling challenge {path}")
        await self.client.send_packet({}, request_id)
        await GameSessionManager().cancel_challenge(self.client, path)
