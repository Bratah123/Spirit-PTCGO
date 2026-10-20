"""STUB: effect not implemented — do not guess mechanics.
Mega Catcher (XY10 #104): trainer effect stubbed.

Card text:
  - Switch 1 of your opponent's Benched Mega Evolution Pokémon with his or her Active Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c102cb21-1255-5094-95c7-7525ec80e694",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaCatcher.Name",
    display_name="Mega Catcher",
    searchable_by=["Mega Catcher", "Item"],
    subtypes=["Item"],
    collector_number=104,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
