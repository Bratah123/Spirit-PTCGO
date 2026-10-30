"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_corphish_89_knock_off,
)

card = PokemonCardDef(guid='ad29d7f6-eed5-5d1d-a381-a9edc72f9cf4', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name', display_name='Corphish', searchable_by=['Corphish', 'Basic', 'Corphish'], subtypes=['Basic'], collector_number=89, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=341, abilities=[Attack(title='Knock Off', game_text="Flip a coin. If heads, choose 1 card from your opponent's hand without looking and discard it.", cost={PokemonTypes.COLORLESS: 1}, effect=dp6_corphish_89_knock_off()), Attack(title='Irongrip', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
