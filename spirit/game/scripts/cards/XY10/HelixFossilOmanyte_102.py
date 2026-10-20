"""STUB: effect not implemented — do not guess mechanics.
Helix Fossil Omanyte (XY10 #102): trainer effect stubbed.

Card text:
  - Look at the bottom 7 cards of your deck. You may reveal an Omanyte you find there and put it onto your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="40fa2b61-b005-5839-8432-f96e46f5ceeb",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HelixFossilOmanyte.Name",
    display_name="Helix Fossil Omanyte",
    searchable_by=["Helix Fossil Omanyte", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
