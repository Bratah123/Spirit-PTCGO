"""STUB: effect not implemented — do not guess mechanics.
Lysandre (XY2 #90): trainer effect stubbed.

Card text:
  - Switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="dde7530d-fc38-57a1-bd17-db10eb2c458f",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre",
    searchable_by=["Lysandre", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
