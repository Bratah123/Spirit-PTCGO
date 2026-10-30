"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_venusaur_20_giant_bloom,
    dp3_venusaur_20_miracle_aroma,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='91229150-a581-591e-9514-caab2316a0f8', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name', display_name='Venusaur', searchable_by=['Venusaur', 'Stage 2', 'Venusaur'], subtypes=['Stage 2'], collector_number=20, set_code='DP3', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name', family_id=1, abilities=[Ability(title='Miracle Aroma', game_text="Once during your turn (before your attack), you may flip a coin. If heads, choose either Asleep, Burned, or Poisoned. The Defending Pokémon is now affected by that Special Condition. This power can't be used if Venusaur is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_venusaur_20_miracle_aroma(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Giant Bloom', game_text='Flip a coin. If heads, remove 4 damage counters from Venusaur.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp3_venusaur_20_giant_bloom())])
