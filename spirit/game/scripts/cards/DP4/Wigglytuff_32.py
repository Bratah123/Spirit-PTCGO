"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_wigglytuff_32_ballon_attack,
    dp4_wigglytuff_32_good_night_melody,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='a5ff22e7-03d5-5f82-b284-fd9c94df26b2', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name', display_name='Wigglytuff', searchable_by=['Wigglytuff', 'Stage 1', 'Wigglytuff'], subtypes=['Stage 1'], collector_number=32, set_code='DP4', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name', family_id=39, abilities=[Ability(title='Good Night Melody', game_text="Once during your turn (before your attack), you may use this power. Each Active Pokémon (both yours and your opponent's) is now Asleep. This power can't be used if Wigglytuff is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_wigglytuff_32_good_night_melody(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Ballon Attack', game_text='If Igglybuff is anywhere under Wigglytuff, this attack does 40 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=dp4_wigglytuff_32_ballon_attack())])
