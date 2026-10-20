"""STUB: effect not implemented — do not guess mechanics.
Sail Fossil (XY3 #98): trainer effect stubbed.

Card text:
  - Look at the bottom 7 cards of your deck. You may reveal an Amaura you find there and put it onto your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="878bdf8b-e25d-5433-8d07-3715f4cdedf5",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SailFossil.Name",
    display_name="Sail Fossil",
    searchable_by=["Sail Fossil", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
