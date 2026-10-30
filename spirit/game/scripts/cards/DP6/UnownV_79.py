"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import dp5_torterra_30_earthquake
from spirit.game.card_effects.dp import (
    dp6_unownv_79_vacation,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='61039d44-3ae7-591d-a294-715f4f711a92', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name', display_name='Unown [V]', searchable_by=['Unown [V]', 'Basic', 'UnownV'], subtypes=['Basic'], collector_number=79, set_code='DP6', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='VACATION', game_text="Once during your turn (before your attack), you may remove 2 damage counters from each of your Pokémon. If you do, your turn ends. This power can't be used if Unown V is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_unownv_79_vacation(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Hidden Power', game_text="Does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.PSYCHIC: 1}, damage=30, effect=dp5_torterra_30_earthquake())])
