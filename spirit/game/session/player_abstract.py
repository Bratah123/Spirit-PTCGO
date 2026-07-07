import abc
import asyncio
from typing import Dict, Any, List, Optional
from spirit.game.attributes import AttrID
from spirit.game.models.avatar import get_default_avatar_items_list

class GamePlayer(abc.ABC):
    def __init__(self, account_id: str, username: str, deck_data: Dict[str, Any]):
        self.account_id: str = account_id
        self.username: str = username
        self.deck_data: Dict[str, Any] = deck_data
        self.entity_id: str = ""  # assigned by server upon board setup
        self.pending_choice_future: Optional[asyncio.Future] = None
        # (name, value, flags) of the offer currently awaiting a reply, replayed
        # verbatim on reconnect since the client never re-requests it.
        self._pending_offer: Optional[tuple] = None

    @property
    def active_deck(self) -> Dict[str, Any]:
        """Returns the player's active deck."""
        return self.deck_data

    @property
    def screen_name(self) -> str:
        """Returns the display or screen name for this player."""
        return self.username

    @property
    def avatar_items(self) -> List[str]:
        """Returns the list of avatar customization item GUIDs."""
        return get_default_avatar_items_list()

    def _get_cosmetic_id(self, attr_id: int, default: str) -> str:
        attrs = self.deck_data.get("attributes", []) if isinstance(self.deck_data, dict) else []
        for attr in attrs:
            if isinstance(attr, dict) and attr.get("name") == attr_id:
                val = attr.get("value")
                if val and isinstance(val, list) and len(val) > 0:
                    item = val[0]
                    if item and item != "00000000-0000-0000-0000-000000000000":
                        return item
                elif isinstance(val, str) and val and val != "00000000-0000-0000-0000-000000000000":
                    return val
        return default

    @property
    def sleeve_id(self) -> str:
        """Returns the selected card sleeve GUID."""
        return self._get_cosmetic_id(AttrID.SELECTED_SLEEVE.value, "e079c0d3-b934-4fbd-b021-545106c75693")

    @property
    def coin_id(self) -> str:
        """Returns the selected coin GUID."""
        return self._get_cosmetic_id(AttrID.SELECTED_COIN.value, "B9A4EA96-949E-11E1-890F-EFB676C7909C")

    @property
    def deckbox_id(self) -> str:
        """Returns the selected deck box GUID."""
        return self._get_cosmetic_id(AttrID.SELECTED_DECK_BOX.value, "e129b0d3-b934-4fbd-b021-545106c75694")

    @abc.abstractmethod
    async def send_packet(self, name: str, value: Dict[str, Any], flags: int = 0):
        """Sends a message or sequence effect down to this specific participant."""
        pass

    @abc.abstractmethod
    async def prompt_selection(self, prompt_packet: Dict[str, Any]) -> Any:
        """Prompts this player for choices or targets (Blocking or Async)."""
        pass

    async def prompt_custom_choice(self, name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Prompts the player with a custom choice and waits for their action in-line."""
        loop = asyncio.get_running_loop()
        self.pending_choice_future = loop.create_future()

        # Send prompt packet to player
        self._pending_offer = (name, payload, 0)
        await self.send_packet(name, payload)

        try:
            return await self.pending_choice_future
        finally:
            self.pending_choice_future = None
            self._pending_offer = None
