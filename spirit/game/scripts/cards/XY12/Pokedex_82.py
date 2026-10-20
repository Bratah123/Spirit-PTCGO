"""STUB: effect not implemented — do not guess mechanics.
Pokédex (XY12 #82): trainer effect stubbed.

Card text:
  - Look at the top 5 cards of your deck and put them back in any order.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6dea3f2c-dac3-5b88-ab90-b6d0ad542c16",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokedex.Name",
    display_name="Pok\u00e9dex",
    searchable_by=["Pokédex", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
