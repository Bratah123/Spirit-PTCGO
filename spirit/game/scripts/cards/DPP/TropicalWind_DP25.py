"""STUB: effect not implemented — do not guess mechanics.
Tropical Wind (DPP #DP25): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, remove 2 damage counters from each Active Pokémon (remove 1 damage counter if a Pokémon has only 1). If tails, each Active Pokémon is now Asleep.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8420000c-d47f-5caf-a3f1-73fd7547a6c9",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=25,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
