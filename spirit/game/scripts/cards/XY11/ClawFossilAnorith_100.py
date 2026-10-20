"""STUB: effect not implemented — do not guess mechanics.
Claw Fossil Anorith (XY11 #100): trainer effect stubbed.

Card text:
  - Look at the bottom 7 cards of your deck. You may reveal an Anorith you find there and put it onto your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="06959e7b-0e76-59f4-b155-9834bb527048",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClawFossilAnorith.Name",
    display_name="Claw Fossil Anorith",
    searchable_by=["Claw Fossil Anorith", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
