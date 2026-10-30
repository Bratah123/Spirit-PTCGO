"""STUB: effect not implemented — do not guess mechanics.
Potion (DP3 #127): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6a9588c0-0cd1-554c-ab63-c1cebf799f38",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="DP3",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
