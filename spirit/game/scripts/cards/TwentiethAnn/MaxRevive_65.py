"""STUB: effect not implemented — do not guess mechanics.
Max Revive (TwentiethAnn #65): trainer effect stubbed.

Card text:
  - Put a Pokémon from your discard pile on top of your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4ebc61ca-7af4-5584-b2af-df4d580918d5",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item"],
    subtypes=["Item"],
    collector_number=65,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
