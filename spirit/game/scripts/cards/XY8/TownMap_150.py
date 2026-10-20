"""STUB: effect not implemented — do not guess mechanics.
Town Map (XY8 #150): trainer effect stubbed.

Card text:
  - Turn all of your Prize cards face up. (Those Prize cards remain face up for the rest of the game.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c8904062-e8ac-5c98-8b22-e1548f1a257e",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownMap.Name",
    display_name="Town Map",
    searchable_by=["Town Map", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
