"""STUB: effect not implemented — do not guess mechanics.
Acro Bike (XY5 #122): trainer effect stubbed.

Card text:
  - Look at the top 2 cards of your deck and put 1 of them into your hand. Discard the other card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="09c2a182-8a5a-5c10-acac-589fd1281f95",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
