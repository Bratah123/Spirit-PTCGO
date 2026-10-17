"""STUB: effect not implemented — do not guess mechanics.
Floral Crown (TwentiethAnn #RC26): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - At the end of your opponent's turn, heal 20 damage from the Basic Pokémon this card is attached to.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="9ab49a52-5b8a-5019-9d63-c5e6a7855dd3",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloralCrown.Name",
    display_name="Floral Crown",
    searchable_by=["Floral Crown", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=26,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
