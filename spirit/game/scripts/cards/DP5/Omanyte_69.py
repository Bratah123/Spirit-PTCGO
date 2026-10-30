"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_omanyte_69_call_up,
    dp5_omanyte_69_wash_over,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='7dc73369-fe36-5c67-a2f7-2965d1adc721', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name', display_name='Omanyte', searchable_by=['Omanyte', 'Stage 1', 'Omanyte'], subtypes=['Stage 1'], collector_number=69, set_code='DP5', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.HelixFossil.Name', family_id=138, abilities=[Ability(title='Call Up', game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your discard pile for Helix Fossil, Dome Fossil, or Old Amber and put it onto your Bench. This power can't be used if Omanyte is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp5_omanyte_69_call_up(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Wash Over', game_text="Does 10 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=dp5_omanyte_69_wash_over())])
