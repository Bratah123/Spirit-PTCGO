"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Admin (TATM #25): trainer effect stubbed.

Card text:
  - Attach a basic Energy card from your discard pile to your Active Team Aqua Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6d4713e6-8061-5b33-b82b-7c09ba157c49",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaAdmin.Name",
    display_name="Team Aqua Admin",
    searchable_by=["Team Aqua Admin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=25,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
