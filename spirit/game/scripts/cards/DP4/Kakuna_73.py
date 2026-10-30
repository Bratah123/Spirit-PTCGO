"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp4_kakuna_73_stiffen,
)

card = PokemonCardDef(guid='28de44c2-7419-5751-8150-f2c155880adf', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name', display_name='Kakuna', searchable_by=['Kakuna', 'Stage 1', 'Kakuna'], subtypes=['Stage 1'], collector_number=73, set_code='DP4', rarity=Rarities.Common, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name', family_id=13, abilities=[Attack(title='Stiffen', game_text="During your opponent's next turn, any damage done to Kakuna by attacks is reduced by 30 (after applying Weakness and Resistance).", cost={}, effect=dp4_kakuna_73_stiffen()), Attack(title='Spit Poison', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.GRASS: 1}, damage=10, effect=condition_attack(SpecialConditions.POISONED))])
