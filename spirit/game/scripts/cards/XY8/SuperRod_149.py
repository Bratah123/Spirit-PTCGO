"""STUB: effect not implemented — do not guess mechanics.
Super Rod (XY8 #149): trainer effect stubbed.

Card text:
  - Shuffle 3 in any combination of Pokémon and basic Energy cards from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="dffbeedc-023d-5e43-ae2a-3db735d2e307",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=149,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
