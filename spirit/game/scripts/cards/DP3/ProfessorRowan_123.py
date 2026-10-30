"""STUB: effect not implemented — do not guess mechanics.
Professor Rowan (DP3 #123): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Choose 1 card in your hand and shuffle the rest of your cards into your deck. Then, draw 4 cards. (If this is the only card in your hand, you can't play this card.)
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8f3a7c42-53df-530b-b29f-fd96705a4b07",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorRowan.Name",
    display_name="Professor Rowan",
    searchable_by=["Professor Rowan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
