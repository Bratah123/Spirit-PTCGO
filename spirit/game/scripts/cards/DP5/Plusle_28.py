"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import call_for_family_basic
from spirit.game.card_effects.dp import (
    dp5_plusle_28_boost,
)

card = PokemonCardDef(guid='f0ea6328-ff06-5681-869d-d4758001aa2b', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name', display_name='Plusle', searchable_by=['Plusle', 'Basic', 'Plusle'], subtypes=['Basic'], collector_number=28, set_code='DP5', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=311, abilities=[Attack(title='Call for Family', game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=call_for_family_basic()), Attack(title='– Boost', game_text='If Minun is on your Bench, this attack does 20 damage plus 20 more damage.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp5_plusle_28_boost())])
