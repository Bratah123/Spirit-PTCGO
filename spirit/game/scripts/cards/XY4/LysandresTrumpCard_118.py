"""STUB: effect not implemented — do not guess mechanics.
Lysandre's Trump Card (XY4 #118): trainer effect stubbed.

Card text:
  - Each player shuffles all cards in his or her discard pile into his or her deck (except for Lysandre's Trump Card).
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="dafac91a-ca68-5667-8a1f-f518503823e8",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandresTrumpCard.Name",
    display_name="Lysandre's Trump Card",
    searchable_by=["Lysandre's Trump Card", "Supporter"],
    subtypes=["Supporter"],
    collector_number=118,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
