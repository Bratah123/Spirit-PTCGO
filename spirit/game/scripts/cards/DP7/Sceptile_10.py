"""STUB: effect not implemented — do not guess mechanics.
Sceptile (DP7 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp7_sceptile_10_energy_trans,
    dp7_sceptile_10_slice_drain,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='669e91c1-0b1c-592f-a160-34afe3b1fbaa', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name', display_name='Sceptile', searchable_by=['Sceptile', 'Stage 2', 'Sceptile'], subtypes=['Stage 2'], collector_number=10, set_code='DP7', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name', family_id=252, abilities=[Ability(title='Energy Trans', game_text="As often as you like during your turn (before your attack), move a Grass Energy card attached to 1 of your Pokémon to another of your Pokémon. This power can't be used if Sceptile is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_sceptile_10_energy_trans(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Poison Leaf', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.COLORLESS: 2}, damage=40, effect=condition_attack(SpecialConditions.POISONED)), Attack(title='Slice Drain', game_text='Remove 2 damage counters from Sceptile.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp7_sceptile_10_slice_drain())])
