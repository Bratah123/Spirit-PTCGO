"""STUB: effect not implemented — do not guess mechanics.
Switch (DP7 #93): trainer effect stubbed.

Card text:
  - Switch 1 of your Active Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="91b4b59b-8532-5f3d-b6b7-6f0e9c44e949",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="DP7",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
