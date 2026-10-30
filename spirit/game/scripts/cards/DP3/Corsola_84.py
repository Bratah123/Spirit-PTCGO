"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_corsola_84_rally,
)

card = PokemonCardDef(guid='5f7e6dab-18f8-5c18-af1f-699fa0cd0cd8', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name', display_name='Corsola', searchable_by=['Corsola', 'Basic', 'Corsola'], subtypes=['Basic'], collector_number=84, set_code='DP3', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=222, abilities=[Attack(title='Rally', game_text='Search your deck for up to 3 different types of Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_corsola_84_rally()), Attack(title='Hook', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30)])
