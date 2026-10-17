"""STUB: effect not implemented — do not guess mechanics.
Steven (XY6 #90): trainer effect stubbed.

Card text:
  - Search your deck for a Supporter card and a basic Energy card, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1d911495-bac3-5000-b31b-4be666caca7e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Steven.Name",
    display_name="Steven",
    searchable_by=["Steven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
