"""STUB: effect not implemented — do not guess mechanics.
Tierno (XY0 #39): trainer effect stubbed.

Card text:
  - Draw 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7a08de01-1838-54b5-9af3-1231a99e11b2",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tierno.Name",
    display_name="Tierno",
    searchable_by=["Tierno", "Supporter"],
    subtypes=["Supporter"],
    collector_number=39,
    set_code="XY0",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
