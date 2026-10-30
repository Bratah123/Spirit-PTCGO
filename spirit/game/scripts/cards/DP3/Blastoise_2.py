"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    bonus_energy_water_50_20,
    dp3_blastoise_2_waterlog,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='a6303097-4017-5795-81c5-961917eb2b70', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name', display_name='Blastoise', searchable_by=['Blastoise', 'Stage 2', 'Blastoise'], subtypes=['Stage 2'], collector_number=2, set_code='DP3', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name', family_id=7, abilities=[Ability(title='Waterlog', game_text="Once during your turn (before your attack), you may attach as many basic Water Energy cards from your hand to any of your Pokémon in any way you like. If you do, your turn ends. This power can't be used if Blastoise is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_blastoise_2_waterlog(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Hydro Pump', game_text="Does 50 damage plus 20 more damage for each Water Energy attached to Blastoise but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=50, damage_operator='+', effect=bonus_energy_water_50_20())])
