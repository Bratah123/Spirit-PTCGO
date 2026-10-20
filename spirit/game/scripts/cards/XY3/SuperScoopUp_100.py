"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (XY3 #100): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put 1 of your Pokémon and all cards attached to it into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="46a98064-f2bf-5c1a-bdaa-1f4a7b184474",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
