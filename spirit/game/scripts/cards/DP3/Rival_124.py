"""STUB: effect not implemented — do not guess mechanics.
Rival (DP3 #124): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Reveal the top 5 cards of your deck. Your opponent chooses 3 of those cards. Put those cards into your hand and put other 2 cards on top of your deck. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7469ca89-93f5-564b-9dc6-e2edd08045ca",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rival.Name",
    display_name="Rival",
    searchable_by=["Rival", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
