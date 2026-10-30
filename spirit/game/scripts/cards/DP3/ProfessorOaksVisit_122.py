"""STUB: effect not implemented — do not guess mechanics.
Professor Oak's Visit (DP3 #122): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw 3 cards. Then, choose a card from your hand and put it on the bottom of your deck.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="91023469-6138-59fd-ad9f-ad70b3aa872d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksVisit.Name",
    display_name="Professor Oak's Visit",
    searchable_by=["Professor Oak's Visit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
