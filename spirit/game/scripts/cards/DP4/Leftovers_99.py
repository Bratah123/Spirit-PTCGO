"""STUB: effect not implemented — do not guess mechanics.
Leftovers (DP4 #99): trainer effect stubbed.

Card text:
  - Attach Leftovers to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - If the Pokémon Leftovers is attached to is your Active Pokémon at the end of your turn, remove 1 damage counter from the Pokémon.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="94540bcd-b129-552a-8c67-7f0f0116b303",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Leftovers.Name",
    display_name="Leftovers",
    searchable_by=["Leftovers", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
