"""STUB: effect not implemented — do not guess mechanics.
Team Rocket's Handiwork (XY10 #124): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, discard 2 cards from the top of your opponent's deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b0a3f91f-e4d7-5357-9f5a-00e623edd536",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHandiwork.Name",
    display_name="Team Rocket's Handiwork",
    searchable_by=["Team Rocket's Handiwork", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
