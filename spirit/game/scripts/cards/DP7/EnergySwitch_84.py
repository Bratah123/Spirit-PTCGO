"""STUB: effect not implemented — do not guess mechanics.
Energy Switch (DP7 #84): trainer effect stubbed.

Card text:
  - Move a basic Energy card attached to 1 of your Pokémon to another of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="69ab3162-be0e-5a32-afb0-59a1ad2d76fa",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
