"""STUB: effect not implemented — do not guess mechanics.
Bubble Coat (DP6 #129): trainer effect stubbed.

Card text:
  - Attach Bubble Coat to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - As long as Bubble Coat is attached to a Pokémon, that Pokémon has no Weakness. If that Pokémon is damaged by an opponent's attack, discard this card at the end of the turn.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="44f3496a-7286-530d-b131-a494f9bc8393",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BubbleCoat.Name",
    display_name="Bubble Coat",
    searchable_by=["Bubble Coat", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=129,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
