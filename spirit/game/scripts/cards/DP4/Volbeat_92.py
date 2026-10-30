"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp4_volbeat_92_light_conduct,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='0f050192-548c-5e86-b8d8-200d9f6d69bf', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name', display_name='Volbeat', searchable_by=['Volbeat', 'Basic', 'Volbeat'], subtypes=['Basic'], collector_number=92, set_code='DP4', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=313, abilities=[Ability(title='Light Conduct', game_text="Once during your turn (before your attack), if you have Illumise in play, you may search your discard pile for a Supporter card, show it to your opponent, and put it on top of your deck. This power can't be used if Volbeat is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_volbeat_92_light_conduct(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Firefly Light', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.', cost={PokemonTypes.GRASS: 2}, damage=20, effect=condition_attack(SpecialConditions.CONFUSED, flip=True))])
