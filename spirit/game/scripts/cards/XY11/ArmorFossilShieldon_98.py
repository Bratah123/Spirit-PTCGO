"""STUB: effect not implemented — do not guess mechanics.
Armor Fossil Shieldon (XY11 #98): trainer effect stubbed.

Card text:
  - Look at the bottom 7 cards of your deck. You may reveal a Shieldon you find there and put it onto your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="59cde074-a448-5463-ab52-40a51cb0c9c3",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArmorFossilShieldon.Name",
    display_name="Armor Fossil Shieldon",
    searchable_by=["Armor Fossil Shieldon", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
