"""STUB: effect not implemented — do not guess mechanics.
Regigigas (DP7 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_regigigas_9_giga_power,
    dp7_regigigas_9_regi_form,
)

card = PokemonCardDef(guid='8d54ca93-b09a-5354-ba08-42ae0ab87293', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name', display_name='Regigigas', searchable_by=['Regigigas', 'Basic', 'Regigigas'], subtypes=['Basic'], collector_number=9, set_code='DP7', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, family_id=486, abilities=[Ability(title='Regi Form', game_text="If you have Regirock, Regice, and Registeel in play, the attack cost of Regigigas's attacks is Colorless less.", ability_type=AbilityTypes.POKE_BODY, effect=dp7_regigigas_9_regi_form(), activation=Activations.ONCE_PER_TURN), Attack(title='Mega Punch', cost={PokemonTypes.COLORLESS: 2}, damage=30), Attack(title='Giga Power', game_text='You may do 60 damage plus 40 more damage. If you do, Regigigas does 40 damage to itself.', cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=60, damage_operator='+', effect=dp7_regigigas_9_giga_power())])
