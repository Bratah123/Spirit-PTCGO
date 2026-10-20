"""STUB: effect not implemented — do not guess mechanics.
Team Magma Admin (TATM #29): trainer effect stubbed.

Card text:
  - Put up to 3 Team Magma Pokémon from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0a9d9923-ad43-56ca-9b2b-e2ffc812c8bc",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaAdmin.Name",
    display_name="Team Magma Admin",
    searchable_by=["Team Magma Admin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=29,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
