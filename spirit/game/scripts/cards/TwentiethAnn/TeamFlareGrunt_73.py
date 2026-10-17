"""STUB: effect not implemented — do not guess mechanics.
Team Flare Grunt (TwentiethAnn #73): trainer effect stubbed.

Card text:
  - Discard an Energy attached to your opponent's Active Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="44b0ed40-5fb4-500d-9ba8-be00d2f93023",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name",
    display_name="Team Flare Grunt",
    searchable_by=["Team Flare Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
