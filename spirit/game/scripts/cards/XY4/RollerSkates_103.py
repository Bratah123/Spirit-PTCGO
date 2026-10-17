"""STUB: effect not implemented — do not guess mechanics.
Roller Skates (XY4 #103): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, draw 3 cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f8f1569d-092a-56a8-8bdc-83f0902acc95",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkates.Name",
    display_name="Roller Skates",
    searchable_by=["Roller Skates", "Item"],
    subtypes=["Item"],
    collector_number=103,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
