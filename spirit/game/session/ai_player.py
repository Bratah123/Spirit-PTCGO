import logging
from typing import Dict, Any
from .player_abstract import GamePlayer

class AIPlayer(GamePlayer):
    def __init__(self, bot_id: str, bot_name: str, deck_data: Dict[str, Any], session: Any):
        super().__init__(account_id=bot_id, username=bot_name, deck_data=deck_data)
        self.session = session

    async def send_packet(self, name: str, value: Dict[str, Any], flags: int = 0):
        # AI ignores visual animations but updates its internal model
        if name == "SequenceMessage":
            self._update_internal_board_model(value)

    async def prompt_selection(self, prompt_packet: Dict[str, Any]):
        logging.info(f"[Session] AI Player {self.username} evaluating selection prompt.")
        # Minimal AI decision making: Select first valid target
        valid_targets = prompt_packet.get("validTargets", [])
        selected = [valid_targets[0]] if valid_targets else []
        
        response = {
            "selectedTargets": selected,
            "action": "Select"
        }
        
        # Schedule response processing in session
        await self.session.receive_player_action(self.account_id, response)

    def _update_internal_board_model(self, sequence_payload: Dict[str, Any]):
        # Keep track of damage, prizes, and attachments if we need a smart AI later
        pass
