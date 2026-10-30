"""STUB: effect not implemented — do not guess mechanics.
Tropical Wind (DPP #DP05): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, remove 2 damage counters from each Active Pokémon (remove 1 damage counter if a Pokémon has only 1). If tails, each Active Pokémon is now Asleep.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8fd4b34b-663b-5669-9f7a-f95f857f150f",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=5,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
