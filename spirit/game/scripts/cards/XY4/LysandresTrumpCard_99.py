"""STUB: effect not implemented — do not guess mechanics.
Lysandre's Trump Card (XY4 #99): trainer effect stubbed.

Card text:
  - Each player shuffles all cards in his or her discard pile into his or her deck (except for Lysandre's Trump Card).
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="fe27cfa7-6c7a-5e28-bdf2-0f75f19b006d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandresTrumpCard.Name",
    display_name="Lysandre's Trump Card",
    searchable_by=["Lysandre's Trump Card", "Supporter"],
    subtypes=["Supporter"],
    collector_number=99,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
