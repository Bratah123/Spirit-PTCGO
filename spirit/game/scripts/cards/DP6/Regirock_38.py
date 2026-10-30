"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_regirock_38_regi_cycle,
)
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='e97f5769-6c0e-5095-9520-5e78e4e18cd5', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name', display_name='Regirock', searchable_by=['Regirock', 'Basic', 'Regirock'], subtypes=['Basic'], collector_number=38, set_code='DP6', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.WATER, family_id=377, abilities=[Ability(title='Regi Cycle', game_text="Once during your turn (before your attack), if you have a Fighting Energy card in your discard pile, you may discard 2 cards from your hand. Then, attach a Fighting Energy card from your discard pile to Regirock. This power can't be used if Regirock is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_regirock_38_regi_cycle(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Stone Edge', game_text='Flip a coin. If heads, this attack does 40 damage plus 30 more damage.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=flip_bonus(30))])
