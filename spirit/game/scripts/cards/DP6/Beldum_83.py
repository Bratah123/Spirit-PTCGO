"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_beldum_83_metal_chain,
    dp6_beldum_83_take_down,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='4a509e4c-90cb-59ca-9d14-f77157b8842a', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name', display_name='Beldum', searchable_by=['Beldum', 'Basic', 'Beldum'], subtypes=['Basic'], collector_number=83, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=374, abilities=[Ability(title='Metal Chain', game_text="Once during your turn (before your attack), when you attach a Metal Energy card from your hand to Beldum (excluding effects of attacks or Poké-Powers), you may search your deck for Beldum and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Beldum is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_beldum_83_metal_chain(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Take Down', game_text='Beldum does 10 damage to itself.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=dp6_beldum_83_take_down())])
