"""STUB: effect not implemented — do not guess mechanics.
Roller Skates (XY1 #125): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, draw 3 cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="762c8466-bfbb-5e0b-ab40-00861f03ed81",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkates.Name",
    display_name="Roller Skates",
    searchable_by=["Roller Skates", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
