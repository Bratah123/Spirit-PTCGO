"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_sentret_104_grope,
)

card = PokemonCardDef(guid='0b183e69-2c27-5f6b-ba91-b885a5e5c3bc', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name', display_name='Sentret', searchable_by=['Sentret', 'Basic', 'Sentret'], subtypes=['Basic'], collector_number=104, set_code='DP3', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=161, abilities=[Attack(title='Grope', game_text='Look at the top 2 cards of your deck, choose 1 of them, and put it into your hand. Put the other card on the bottom of your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_sentret_104_grope()), Attack(title='Scratch', cost={PokemonTypes.COLORLESS: 1}, damage=10)])
