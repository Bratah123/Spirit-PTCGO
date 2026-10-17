"""STUB: effect not implemented — do not guess mechanics.
Professor Oak's Hint (XY12 #84): trainer effect stubbed.

Card text:
  - Draw cards until you have 7 cards in your hand. Your turn ends.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="50303223-e9c7-5a18-bb74-27048380401a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksHint.Name",
    display_name="Professor Oak's Hint",
    searchable_by=["Professor Oak's Hint", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
