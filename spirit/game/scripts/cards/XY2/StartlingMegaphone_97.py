"""STUB: effect not implemented — do not guess mechanics.
Startling Megaphone (XY2 #97): trainer effect stubbed.

Card text:
  - Discard all Pokémon Tool cards attached to each of your opponent's Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6c240695-897c-5aab-8df8-f67f879df73b",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StartlingMegaphone.Name",
    display_name="Startling Megaphone",
    searchable_by=["Startling Megaphone", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
