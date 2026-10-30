"""STUB: effect not implemented — do not guess mechanics.
Abomasnow (DP7 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_abomasnow_12_below_zero,
    dp7_abomasnow_12_snow_play,
    dp7_abomasnow_12_snow_veil_passive,
)

card = PokemonCardDef(guid='5f227a4b-19cf-5552-8ff8-1a193278c8cf', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name', display_name='Abomasnow', searchable_by=['Abomasnow', 'Stage 1', 'Abomasnow'], subtypes=['Stage 1'], collector_number=12, set_code='DP7', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name', family_id=459, abilities=[Ability(title='Snow Veil', game_text="As long as Abomasnow is your Active Pokémon, any damage done to your Pokémon by an opponent's attack is reduced by 20 (after applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, passive=dp7_abomasnow_12_snow_veil_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Snow Play', game_text="Does 20 damage to each of your opponent's Benched Pokémon, excluding Grass Pokémon and Water Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=dp7_abomasnow_12_snow_play()), Attack(title='Below Zero', game_text='If Abomasnow evolved from Snover during this turn, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp7_abomasnow_12_below_zero())])
