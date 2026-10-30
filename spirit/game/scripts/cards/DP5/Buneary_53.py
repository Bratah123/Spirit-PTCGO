"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp4_darkrai_3_reach_over
from spirit.game.card_effects.dp import (
    dp5_buneary_53_extend_ears,
)

card = PokemonCardDef(guid='23d7d52f-5943-5444-bb8d-5df04bd0069e', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name', display_name='Buneary', searchable_by=['Buneary', 'Basic', 'Buneary'], subtypes=['Basic'], collector_number=53, set_code='DP5', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=427, abilities=[Attack(title='Drawup Power', game_text='Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={}, effect=dp4_darkrai_3_reach_over()), Attack(title='Extend Ears', game_text='Remove 1 damage counter from each of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=dp5_buneary_53_extend_ears())])
