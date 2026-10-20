"""STUB: effect not implemented — do not guess mechanics.
Dome Fossil Kabuto (XY10 #96): trainer effect stubbed.

Card text:
  - Look at the bottom 7 cards of your deck. You may reveal a Kabuto you find there and put it onto your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8d39e07c-2ead-54f4-9f11-c6a2f6e6c6a9",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DomeFossilKabuto.Name",
    display_name="Dome Fossil Kabuto",
    searchable_by=["Dome Fossil Kabuto", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
