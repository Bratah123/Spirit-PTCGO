"""STUB: effect not implemented — do not guess mechanics.
Paint Roller (XY7 #79): trainer effect stubbed.

Card text:
  - Discard any Stadium card in play. Then, draw a card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b15e2067-8360-58c1-b37c-ffea09f3bcd5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PaintRoller.Name",
    display_name="Paint Roller",
    searchable_by=["Paint Roller", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
