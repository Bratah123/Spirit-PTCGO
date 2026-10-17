"""STUB: effect not implemented — do not guess mechanics.
Lysandre (XY7 #78): trainer effect stubbed.

Card text:
  - Switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a1dcc4ec-3463-5c03-a295-68f0dada2c25",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre",
    searchable_by=["Lysandre", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
