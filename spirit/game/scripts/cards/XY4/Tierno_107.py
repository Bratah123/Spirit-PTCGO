"""STUB: effect not implemented — do not guess mechanics.
Tierno (XY4 #107): trainer effect stubbed.

Card text:
  - Draw 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="29b0a32c-164d-51bc-9f42-b674e850bcee",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tierno.Name",
    display_name="Tierno",
    searchable_by=["Tierno", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
