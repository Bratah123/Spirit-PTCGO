"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    electromagnetic_jam,
)

card = PokemonCardDef(guid='b4bd108c-b411-54dd-a01a-efceee8362f7', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name', display_name='Electrike', searchable_by=['Electrike', 'Basic', 'Electrike'], subtypes=['Basic'], collector_number=81, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=309, abilities=[Attack(title='Electromagnetic Jam', game_text="Flip a coin. If heads, your opponent can't attach any Energy cards from his or her hand to the Active Pokémon during his or her next turn.", cost={PokemonTypes.LIGHTNING: 1}, damage=10, effect=electromagnetic_jam(10))])
