"""STUB: effect not implemented — do not guess mechanics.
Raichu LV.X (DP7 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_raichulvx_99_link_lightning,
    dp7_raichulvx_99_voltage_shoot,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='866b537f-abec-592f-b906-db261fc5a6a1', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.RaichuLVX.Name', display_name='Raichu LV.X', searchable_by=['Raichu LV.X', 'Level-Up', 'RaichuLVX'], subtypes=['Level-Up'], collector_number=99, set_code='DP7', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.LEVELUP, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name', family_id=25, abilities=[Ability(title='Link Lightning', game_text="Once during your turn, when you put Raichu LV.X onto Raichu and use Voltage Shoot, you may use another attack of Raichu afterward. This power can't be used if Raichu is affected by a Special Condition.", ability_type=AbilityTypes.POKE_BODY, effect=dp7_raichulvx_99_link_lightning(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Voltage Shoot', game_text="Discard 2 Lightning Energy cards from your hand and choose 1 of your opponent's Pokémon. This attack does 80 to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, effect=dp7_raichulvx_99_voltage_shoot())])
