"""STUB: effect not implemented — do not guess mechanics.
Professor Sycamore (XY1 #122): trainer effect stubbed.

Card text:
  - Discard your hand and draw 7 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0eec28a7-2241-57ec-87ca-469cac9aa9db",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSycamore.Name",
    display_name="Professor Sycamore",
    searchable_by=["Professor Sycamore", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
