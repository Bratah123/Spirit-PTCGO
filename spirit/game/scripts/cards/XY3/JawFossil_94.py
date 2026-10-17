"""STUB: effect not implemented — do not guess mechanics.
Jaw Fossil (XY3 #94): trainer effect stubbed.

Card text:
  - Look at the bottom 7 cards of your deck. You may reveal a Tyrunt you find there and put it onto your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="98f9f9d7-d9ab-5369-af62-c82c5b553100",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JawFossil.Name",
    display_name="Jaw Fossil",
    searchable_by=["Jaw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
