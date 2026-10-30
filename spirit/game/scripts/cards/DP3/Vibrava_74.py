"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import breaking_sound
from spirit.game.card_effects.dp import (
    dp3_vibrava_74_hyper_beam,
)

card = PokemonCardDef(guid='9c9f3737-2277-5dca-a8f3-9f22a3b787e0', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name', display_name='Vibrava', searchable_by=['Vibrava', 'Stage 1', 'Vibrava'], subtypes=['Stage 1'], collector_number=74, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name', family_id=328, abilities=[Attack(title='Sand Wind', game_text="Does 10 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1}, effect=breaking_sound(10)), Attack(title='Hyper Beam', game_text='Flip a coin. If heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=40, effect=dp3_vibrava_74_hyper_beam())])
