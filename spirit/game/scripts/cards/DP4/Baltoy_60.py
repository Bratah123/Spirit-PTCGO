"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp3_mew_15_psychic_balance
from spirit.game.card_effects.dp import (
    dp4_baltoy_60_spin_turn,
)

card = PokemonCardDef(guid='f9afea4a-5b83-52d6-a81a-2476a3d4dda8', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name', display_name='Baltoy', searchable_by=['Baltoy', 'Basic', 'Baltoy'], subtypes=['Basic'], collector_number=60, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=343, abilities=[Attack(title='Psychic Balance', game_text='If you have less cards in your hand than your opponent, draw cards until you have the same number of cards as your opponent. (If you have more or the same number of cards in your hand as your opponent, this attack does nothing.)', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_mew_15_psychic_balance()), Attack(title='Spin Turn', game_text='Switch Baltoy with 1 of your Benched Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=dp4_baltoy_60_spin_turn())])
