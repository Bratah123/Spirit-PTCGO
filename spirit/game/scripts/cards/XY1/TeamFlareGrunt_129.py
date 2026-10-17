"""STUB: effect not implemented — do not guess mechanics.
Team Flare Grunt (XY1 #129): trainer effect stubbed.

Card text:
  - Discard an Energy attached to your opponent's Active Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c91261c9-93cc-515f-990f-575006157dfc",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name",
    display_name="Team Flare Grunt",
    searchable_by=["Team Flare Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
