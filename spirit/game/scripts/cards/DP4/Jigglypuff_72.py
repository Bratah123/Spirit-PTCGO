"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp4_jigglypuff_72_expand,
)

card = PokemonCardDef(guid='6fdae969-8377-5208-8e87-54425558a777', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name', display_name='Jigglypuff', searchable_by=['Jigglypuff', 'Basic', 'Jigglypuff'], subtypes=['Basic'], collector_number=72, set_code='DP4', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=39, abilities=[Attack(title='Hypnotic Gaze', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Expand', game_text="During your opponent's next turn, any damage done to Jigglypuff by attacks is reduced by 20 (after applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=dp4_jigglypuff_72_expand())])
