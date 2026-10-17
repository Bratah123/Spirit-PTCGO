import abc
import asyncio
from typing import Dict, Any, List, Optional, Tuple
from spirit.game.attributes import AttrID, DefaultCosmetic, DeckBoxShape
from spirit.game.models.product import DeckBox
from spirit.game.models.avatar import get_default_avatar_items_list
from spirit.game.scripts.products import loader as product_loader
from spirit.server.auto_bundle_cosmetics import deckbox_flat_names

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
        return self._get_cosmetic_id(AttrID.SELECTED_SLEEVE.value, DefaultCosmetic.SLEEVE.value)

    @property
    def coin_id(self) -> str:
        """Returns the selected coin GUID."""
        return self._get_cosmetic_id(AttrID.SELECTED_COIN.value, DefaultCosmetic.COIN.value)

    @property
    def deckbox_id(self) -> str:
        """Returns the selected deck box GUID."""
        return self._get_cosmetic_id(AttrID.SELECTED_DECK_BOX.value, DefaultCosmetic.DECK_BOX.value)

    @property
    def playmat_deck_box(self) -> Tuple[str, DeckBoxShape]:
        """(image name, shape) of the selected deck box; ("", TWO_TONE) when it has no playmat flat."""
        product = product_loader.products_by_guid.get(self.deckbox_id.lower())
        if not isinstance(product, DeckBox) or product.shape not in (DeckBoxShape.THEME_DECK, DeckBoxShape.KEEPER):
            return "", DeckBoxShape.TWO_TONE
        image = str(product.get_attribute_value(AttrID.IMAGE_NAME, "") or "").lower()
        if image not in deckbox_flat_names():
            return "", DeckBoxShape.TWO_TONE
        return image, product.shape

    @abc.abstractmethod
    async def send_packet(self, name: str, value: Dict[str, Any], flags: int = 0):
        """Sends a message or sequence effect down to this specific participant."""
        pass

    @abc.abstractmethod
    async def prompt_selection(self, prompt_packet: Dict[str, Any]) -> Any:
        """Prompts this player for choices or targets (Blocking or Async)."""
        pass

    async def send_packets(self, packets):
        """Send an ordered batch; network players override this with atomic enqueue."""
        for name, value, flags in packets:
            await self.send_packet(name, value, flags)

    async def flush_outbound(self):
        """Non-network players have no socket backlog."""
        return True

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
