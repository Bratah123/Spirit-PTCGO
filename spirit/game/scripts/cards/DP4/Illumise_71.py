"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_illumise_71_scent_conduct,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='c35b5801-925b-5157-a5dd-6ff1e1894588', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name', display_name='Illumise', searchable_by=['Illumise', 'Basic', 'Illumise'], subtypes=['Basic'], collector_number=71, set_code='DP4', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=314, abilities=[Ability(title='Scent Conduct', game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a Grass Basic Pokémon and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Illumise is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_illumise_71_scent_conduct(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Firefly Scent', game_text='If the Defending Pokémon has any Poké-Bodies, that Pokémon is now Asleep.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.ASLEEP))])
