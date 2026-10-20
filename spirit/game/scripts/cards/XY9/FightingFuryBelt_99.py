"""STUB: effect not implemented — do not guess mechanics.
Fighting Fury Belt (XY9 #99): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Basic Pokémon this card is attached to gets +40 HP and its attacks do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a1bc0828-b71f-596d-8e12-a06ef6ba2838",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingFuryBelt.Name",
    display_name="Fighting Fury Belt",
    searchable_by=["Fighting Fury Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=99,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
