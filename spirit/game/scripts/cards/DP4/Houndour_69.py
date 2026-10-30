"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_houndour_69_ember,
)

card = PokemonCardDef(guid='a98031f8-325b-5dad-b8d5-a301f0d453df', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name', display_name='Houndour', searchable_by=['Houndour', 'Basic', 'Houndour'], subtypes=['Basic'], collector_number=69, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=228, abilities=[Attack(title='Ember', game_text='Flip a coin. If tails, discard a Fire Energy attached to Houndour.', cost={PokemonTypes.FIRE: 1}, damage=20, effect=dp4_houndour_69_ember()), Attack(title='Smash Kick', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
