"""STUB: effect not implemented — do not guess mechanics.
AZ (XY4 #117): trainer effect stubbed.

Card text:
  - Put 1 Pokémon into your hand. (Discard all cards attached to that Pokémon.)
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="bb3855cc-0a1e-5265-adc3-428851559235",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZ.Name",
    display_name="AZ",
    searchable_by=["AZ", "Supporter"],
    subtypes=["Supporter"],
    collector_number=117,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
