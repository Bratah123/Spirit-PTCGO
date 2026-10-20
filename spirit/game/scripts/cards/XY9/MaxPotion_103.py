"""STUB: effect not implemented — do not guess mechanics.
Max Potion (XY9 #103): trainer effect stubbed.

Card text:
  - Heal all damage from 1 of your Pokémon. If you do, discard all Energy attached to that Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="baf7d106-d4f8-5fa8-b328-dbe3a444c0ee",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=103,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
