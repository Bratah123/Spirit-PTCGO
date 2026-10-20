"""STUB: effect not implemented — do not guess mechanics.
Energy Pouch (XY10 #97): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put all basic Energy attached to that Pokémon into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="8067bf07-1cd5-588d-b3b2-dfd6ab99c2ff",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyPouch.Name",
    display_name="Energy Pouch",
    searchable_by=["Energy Pouch", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=97,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
