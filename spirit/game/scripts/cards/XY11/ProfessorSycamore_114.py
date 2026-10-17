"""STUB: effect not implemented — do not guess mechanics.
Professor Sycamore (XY11 #114): trainer effect stubbed.

Card text:
  - Discard your hand and draw 7 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="07ae5c3a-de5d-574f-8da6-9e492628c50e",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSycamore.Name",
    display_name="Professor Sycamore",
    searchable_by=["Professor Sycamore", "Supporter"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="XY11",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
