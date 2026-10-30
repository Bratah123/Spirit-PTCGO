"""STUB: effect not implemented — do not guess mechanics.
Energy Pickup (DP6 #132): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your discard pile for a basic Energy card and attach it to 1 of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fc33059c-0ec5-5d9c-bd5f-6c827a7fe105",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyPickup.Name",
    display_name="Energy Pickup",
    searchable_by=["Energy Pickup", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
