"""STUB: effect not implemented — do not guess mechanics.
Steven (XY7 #95): trainer effect stubbed.

Card text:
  - Search your deck for a Supporter card and a basic Energy card, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2222e444-ca70-5b8a-9ba8-c8990419db06",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Steven.Name",
    display_name="Steven",
    searchable_by=["Steven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
