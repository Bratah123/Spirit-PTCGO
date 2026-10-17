"""STUB: effect not implemented — do not guess mechanics.
Max Revive (XY1 #120): trainer effect stubbed.

Card text:
  - Put a Pokémon from your discard pile on top of your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bdfab0b2-e405-5f82-9a79-2dcf3987e2ed",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
