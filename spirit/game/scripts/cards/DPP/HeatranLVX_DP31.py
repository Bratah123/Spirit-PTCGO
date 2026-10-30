"""STUB: effect not implemented — do not guess mechanics.
Heatran LV.X (DP7 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_heatranlvx_97_heat_metal,
    dp7_heatranlvx_97_heat_wave,
)

card = PokemonCardDef(guid='d5683ca6-d5c6-5c93-9cdf-e9e97f9e64b6', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.HeatranLVX.Name', display_name='Heatran LV.X', searchable_by=['Heatran LV.X', 'Level-Up', 'HeatranLVX'], subtypes=['Level-Up'], collector_number=31, set_code='DP7', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.FIRE], stage=PokemonStage.LEVELUP, retreat_cost=4, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name', family_id=485, abilities=[Ability(title='Heat Metal', game_text="Your opponent can't remove the Special Condition Burned by evolving or devolving his or her Burned Pokémon. (This also includes putting a Pokémon Level-Up card onto the Burned Pokémon.) Whenever your opponent flips a coin for the Special Condition Burned between turns, treat it as tails.", ability_type=AbilityTypes.POKE_BODY, effect=dp7_heatranlvx_97_heat_metal(), activation=Activations.ONCE_PER_TURN), Ability(title='Heat Wave', game_text="Once at the end of your turn, if Heatran is on your Bench, you may use this power. If you discarded basic Energy cards attached to your Fire or Metal Active Pokémon by using that Pokémon's attack this turn, attach up to 2 of those Energy cards to that Pokémon.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_heatranlvx_97_heat_wave(), activation=Activations.ONCE_PER_TURN)])
