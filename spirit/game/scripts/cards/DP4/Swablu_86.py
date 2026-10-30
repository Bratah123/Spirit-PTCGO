"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.dp import (
    dp4_swablu_86_super_speed,
)

card = PokemonCardDef(guid='c6d4c1ca-5e66-5fb4-acf4-e4a9e0167f93', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name', display_name='Swablu', searchable_by=['Swablu', 'Basic', 'Swablu'], subtypes=['Basic'], collector_number=86, set_code='DP4', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=333, abilities=[Attack(title='Super Speed', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Swablu during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=dp4_swablu_86_super_speed()), Attack(title='Shoot Through', game_text="Does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 2}, damage=10, effect=snipe_attack(10, also_base=True))])
