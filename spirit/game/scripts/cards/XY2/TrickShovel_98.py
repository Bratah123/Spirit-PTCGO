"""STUB: effect not implemented — do not guess mechanics.
Trick Shovel (XY2 #98): trainer effect stubbed.

Card text:
  - Look at the top card of either player's deck. You may discard that card or return it to the top of the deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="19baa988-4599-57a9-a76f-6c7d9fd87212",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrickShovel.Name",
    display_name="Trick Shovel",
    searchable_by=["Trick Shovel", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
