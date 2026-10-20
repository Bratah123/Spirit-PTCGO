"""STUB: effect not implemented — do not guess mechanics.
Reserved Ticket (XY8 #147): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for a card, shuffle your deck, then put that card on top of it.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b3f7ca8f-d81a-5893-b7e7-c9e7bc56799a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReservedTicket.Name",
    display_name="Reserved Ticket",
    searchable_by=["Reserved Ticket", "Item"],
    subtypes=["Item"],
    collector_number=147,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
