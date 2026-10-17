"""STUB: effect not implemented — do not guess mechanics.
Lysandre (XY2 #104): trainer effect stubbed.

Card text:
  - Switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6e2ee7b2-2b80-5617-ab6f-e8de5d58a8a9",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre",
    searchable_by=["Lysandre", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY2",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
