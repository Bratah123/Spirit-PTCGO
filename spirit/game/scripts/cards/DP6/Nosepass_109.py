"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_nosepass_109_nose_poke,
)

card = PokemonCardDef(guid='f4177c5d-b8f7-53f5-91bd-67084a2465fd', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name', display_name='Nosepass', searchable_by=['Nosepass', 'Basic', 'Nosepass'], subtypes=['Basic'], collector_number=109, set_code='DP6', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=299, abilities=[Attack(title='Sharpen', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Nose Poke', game_text='If Probopass is on your Bench, this attack does 20 damage plus 20 more damage.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp6_nosepass_109_nose_poke())])
