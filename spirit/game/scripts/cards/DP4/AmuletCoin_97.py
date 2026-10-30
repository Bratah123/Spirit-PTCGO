"""STUB: effect not implemented — do not guess mechanics.
Amulet Coin (DP4 #97): trainer effect stubbed.

Card text:
  - Attach Amulet Coin to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - If the Pokémon Amulet Coin is attached to is your Active Pokémon at the end of your turn, draw a card.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="b0151dd5-68b4-5509-8def-0c9415905bae",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmuletCoin.Name",
    display_name="Amulet Coin",
    searchable_by=["Amulet Coin", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
