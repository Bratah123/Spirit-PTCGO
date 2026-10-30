"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_palkialvx_106_hydro_reflect,
    dp4_palkialvx_106_restructure,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='a51de647-f90e-5fa8-a30a-285ea24ef61a', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaLVX.Name', display_name='Palkia LV.X', searchable_by=['Palkia LV.X', 'Level-Up', 'PalkiaLVX'], subtypes=['Level-Up'], collector_number=18, set_code='DP4', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.LEVELUP, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name', family_id=484, abilities=[Ability(title='Restructure', game_text="Once during your turn (before your attack), you may have your opponent switch 1 of your Active Pokémon with 1 of your Benched Pokémon. Then, you switch 1 of the Defending Pokémon with 1 of your opponent's Benched Pokémon. This power can't be used if Palkia is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_palkialvx_106_restructure(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Hydro Reflect', game_text="You may move all Energy cards attached to Palkia to your Benched Pokémon in any way you like. (Ignore this effect if you don't have any Benched Pokémon.)", cost={PokemonTypes.WATER: 3}, damage=60, effect=dp4_palkialvx_106_hydro_reflect())])
