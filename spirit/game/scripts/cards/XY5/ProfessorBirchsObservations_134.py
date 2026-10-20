"""STUB: effect not implemented — do not guess mechanics.
Professor Birch's Observations (XY5 #134): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck and flip a coin. If heads, draw 7 cards. If tails, draw 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="96ce1699-6cd9-5e75-8112-fd1d12abe42a",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirchsObservations.Name",
    display_name="Professor Birch's Observations",
    searchable_by=["Professor Birch's Observations", "Supporter"],
    subtypes=["Supporter"],
    collector_number=134,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
