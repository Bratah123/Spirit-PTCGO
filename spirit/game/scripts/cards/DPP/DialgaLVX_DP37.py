"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_dialgalvx_105_metal_flash,
    dp4_dialgalvx_105_time_skip,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='c2a9d832-e51b-5cd2-befc-b1e349f78604', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.DialgaLVX.Name', display_name='Dialga LV.X', searchable_by=['Dialga LV.X', 'Level-Up', 'DialgaLVX'], subtypes=['Level-Up'], collector_number=37, set_code='DP4', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.METAL], stage=PokemonStage.LEVELUP, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name', family_id=483, abilities=[Ability(title='Time Skip', game_text="Once during your turn (before your attack), you may have your opponent flip 2 coins. If both of them are heads, your turn ends. If both of them are tails, after your opponent draws a card at the beginning of his or her next turn, his or her turn ends. This power can't be used if Dialga is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_dialgalvx_105_time_skip(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Metal Flash', game_text="During your next turn, Dialga can't use Metal Flash.", cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2}, damage=80, effect=dp4_dialgalvx_105_metal_flash())])
