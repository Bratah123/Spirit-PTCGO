"""STUB: effect not implemented — do not guess mechanics.
Lass's Special (XY10 #103): trainer effect stubbed.

Card text:
  - Draw a card for each of your opponent's Benched Basic Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1a44fea6-e882-53b6-be66-799e0c629b48",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LasssSpecial.Name",
    display_name="Lass's Special",
    searchable_by=["Lass's Special", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
