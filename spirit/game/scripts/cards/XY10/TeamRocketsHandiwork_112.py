"""STUB: effect not implemented — do not guess mechanics.
Team Rocket's Handiwork (XY10 #112): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, discard 2 cards from the top of your opponent's deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7117ef04-9e42-5aa4-a20e-39951495e458",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHandiwork.Name",
    display_name="Team Rocket's Handiwork",
    searchable_by=["Team Rocket's Handiwork", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
