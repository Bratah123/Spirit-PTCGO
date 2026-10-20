"""STUB: effect not implemented — do not guess mechanics.
Old Amber Aerodactyl (XY10 #106): trainer effect stubbed.

Card text:
  - Look at the bottom 7 cards of your deck. You may reveal an Aerodactyl you find there and put it onto your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c6afbafe-eec4-5ff8-a20d-f0e3401dac8b",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldAmberAerodactyl.Name",
    display_name="Old Amber Aerodactyl",
    searchable_by=["Old Amber Aerodactyl", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
