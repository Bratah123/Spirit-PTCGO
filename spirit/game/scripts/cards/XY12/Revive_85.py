"""STUB: effect not implemented — do not guess mechanics.
Revive (XY12 #85): trainer effect stubbed.

Card text:
  - Put a Basic Pokémon from your discard pile onto your Bench.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b5ed74e1-7938-5542-83a5-ec04d5bf4aa0",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
