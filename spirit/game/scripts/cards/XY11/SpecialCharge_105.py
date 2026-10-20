"""STUB: effect not implemented — do not guess mechanics.
Special Charge (XY11 #105): trainer effect stubbed.

Card text:
  - Shuffle 2 Special Energy cards from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ee453dd2-a4f6-5919-b5bd-83cf7435124b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialCharge.Name",
    display_name="Special Charge",
    searchable_by=["Special Charge", "Item"],
    subtypes=["Item"],
    collector_number=105,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
