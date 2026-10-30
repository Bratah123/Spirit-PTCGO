"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_porygon_81_calculate,
)

card = PokemonCardDef(guid='16dcfab9-1878-5985-bcaf-856ed93eb9a3', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name', display_name='Porygon', searchable_by=['Porygon', 'Basic', 'Porygon'], subtypes=['Basic'], collector_number=81, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=137, abilities=[Attack(title='Calculate', game_text='Look at the top 3 cards of your deck and put them back on top of your deck in any order.', cost={PokemonTypes.COLORLESS: 1}, effect=dp4_porygon_81_calculate()), Attack(title='Sharpen', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
