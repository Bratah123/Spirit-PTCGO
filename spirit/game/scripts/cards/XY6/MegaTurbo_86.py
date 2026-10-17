"""STUB: effect not implemented — do not guess mechanics.
Mega Turbo (XY6 #86): trainer effect stubbed.

Card text:
  - Attach a basic Energy card from your discard pile to 1 of your Mega Evolution Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="93d6b5c7-727b-5ba2-9c76-86b3b5e33917",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaTurbo.Name",
    display_name="Mega Turbo",
    searchable_by=["Mega Turbo", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
