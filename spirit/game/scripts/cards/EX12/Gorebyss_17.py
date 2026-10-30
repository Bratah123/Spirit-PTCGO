"""STUB: effect not implemented — do not guess mechanics.
Gorebyss (EX12 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    hydro_pump_capped_attack,
    reactive_booster_passive,
)

card = PokemonCardDef(guid='3553aad4-3086-5ea6-b514-9453071eb0fa', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name', display_name='Gorebyss', searchable_by=['Gorebyss', 'Stage 1', 'Gorebyss'], subtypes=['Stage 1'], collector_number=17, set_code='EX12', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name', family_id=366, abilities=[Ability(title='Reactive Booster', game_text='Each React Energy card attached to all of your Huntail and Gorebyss provides 2 Energy of every type but has no effect other than providing Energy.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=reactive_booster_passive()), Attack(title='Hydro Pump', game_text="Does 30 damage plus 20 more damage for each Water Energy attached to Gorebyss but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=hydro_pump_capped_attack(30, 20, 40, PokemonTypes.WATER))])
