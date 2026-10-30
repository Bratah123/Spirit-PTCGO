"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp4_togepi_88_find_a_friend,
)

card = PokemonCardDef(guid='23fa92c7-51c2-51ec-95a0-b0714222c983', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name', display_name='Togepi', searchable_by=['Togepi', 'Basic', 'Togepi'], subtypes=['Basic'], collector_number=88, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=175, abilities=[Attack(title='Yawn', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Find a Friend', game_text='Flip a coin. If heads, search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp4_togepi_88_find_a_friend())])
