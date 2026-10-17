"""STUB: effect not implemented — do not guess mechanics.
Professor Birch's Observations (XY5 #159): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck and flip a coin. If heads, draw 7 cards. If tails, draw 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="cc26edad-ecc7-55b9-b7c5-ff405493cea1",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirchsObservations.Name",
    display_name="Professor Birch's Observations",
    searchable_by=["Professor Birch's Observations", "Supporter"],
    subtypes=["Supporter"],
    collector_number=159,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
