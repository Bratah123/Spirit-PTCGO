"""STUB: effect not implemented — do not guess mechanics.
Poké Drawer + (DP7 #89): trainer effect stubbed.

Card text:
  - You may play 2 Poké Drawer + at the same time. If you play 1 Poké Drawer +, draw a card. If you play 2 Poké Drawer +, search your deck for up to 2 cards, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f1a46bc0-2d62-57ca-9d89-3dfde732b8d0",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeDrawer.Name",
    display_name="Poké Drawer +",
    searchable_by=["Pok\u00e9 Drawer +", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
