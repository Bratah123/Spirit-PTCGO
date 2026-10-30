"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_delibird_36_present,
)

card = PokemonCardDef(guid='88b4ed4d-017c-5628-b4ea-97d81b5138a5', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name', display_name='Delibird', searchable_by=['Delibird', 'Basic', 'Delibird'], subtypes=['Basic'], collector_number=36, set_code='DP4', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.METAL, family_id=225, abilities=[Attack(title='Present', game_text='Flip a coin. If heads, search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.', cost={}, effect=dp4_delibird_36_present()), Attack(title='Ice Ball', cost={PokemonTypes.WATER: 1}, damage=20)])
