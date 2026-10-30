"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_heatran_30_heavy_metal,
    dp6_heatran_30_smelt,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='ab58a6bf-8261-5d01-8bcd-67eeeb760fbc', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name', display_name='Heatran', searchable_by=['Heatran', 'Basic', 'Heatran'], subtypes=['Basic'], collector_number=30, set_code='DP6', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.WATER, family_id=485, abilities=[Ability(title='Smelt', game_text="Once during your turn (before your attack), you may move a Metal Energy attached to 1 of your Pokémon to Heatran. This power can't be used if Heatran is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_heatran_30_smelt(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Heavy Metal', game_text='Flip a coin for each Metal Energy attached to Heatran. This attack does 40 damage plus 20 more damage for each heads.', cost={PokemonTypes.COLORLESS: 3}, damage=40, damage_operator='+', effect=dp6_heatran_30_heavy_metal())])
