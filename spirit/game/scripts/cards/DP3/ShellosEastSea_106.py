"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_shelloseastsea_106_shell_hunting,
)

card = PokemonCardDef(guid='adfb3397-2f68-5590-acda-0c442c67043f', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.ShellosEastSea.Name', display_name='Shellos East Sea', searchable_by=['Shellos East Sea', 'Basic', 'ShellosEastSea'], subtypes=['Basic'], collector_number=106, set_code='DP3', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, family_id=422, abilities=[Attack(title='Shell Hunting', game_text='Search your deck for up to 2 in any combination of Shellos West Sea and Shellos East Sea and put them on your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_shelloseastsea_106_shell_hunting()), Attack(title='Sprinkle Water', cost={PokemonTypes.WATER: 1}, damage=10)])
