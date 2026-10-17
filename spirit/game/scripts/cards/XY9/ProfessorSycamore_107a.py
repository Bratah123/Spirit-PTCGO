"""STUB: effect not implemented — do not guess mechanics.
Professor Sycamore (XY9 #107a): trainer effect stubbed.

Card text:
  - Discard your hand and draw 7 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="952ae9ea-85e3-5416-8c54-ffe0568cea65",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSycamore.Name",
    display_name="Professor Sycamore",
    searchable_by=["Professor Sycamore", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
