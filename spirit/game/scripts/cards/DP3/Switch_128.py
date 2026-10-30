"""STUB: effect not implemented — do not guess mechanics.
Switch (DP3 #128): trainer effect stubbed.

Card text:
  - Switch 1 of your Active Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c0e0c660-e40c-5af4-995e-7dd82aec53df",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="DP3",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
