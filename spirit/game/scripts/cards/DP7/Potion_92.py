"""STUB: effect not implemented — do not guess mechanics.
Potion (DP7 #92): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b4f031af-021c-55f2-b952-0223a54becbb",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="DP7",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
