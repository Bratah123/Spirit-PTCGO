"""STUB: effect not implemented — do not guess mechanics.
Revive (XY6 #88): trainer effect stubbed.

Card text:
  - Put a Basic Pokémon from your discard pile onto your Bench.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="542cc576-c475-517e-bd7c-204db9742644",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
