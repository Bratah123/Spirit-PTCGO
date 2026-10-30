"""STUB: effect not implemented — do not guess mechanics.
Lanturn (EX12 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    dual_armor_if_energy,
    water_gun_extra,
)

card = PokemonCardDef(guid='32dabc1a-6a0c-5eb9-9535-7a138fc581a9', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name', display_name='Lanturn', searchable_by=['Lanturn', 'Stage 1', 'Lanturn'], subtypes=['Stage 1'], collector_number=19, set_code='EX12', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name', family_id=170, abilities=[Ability(title='Dual Armor', game_text='As long as Lanturn has any Water Energy attached to it, Lanturn is both Water and Lightning type.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=dual_armor_if_energy(PokemonTypes.WATER, PokemonTypes.WATER, PokemonTypes.LIGHTNING)), Attack(title='Razor Fin', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30), Attack(title='Water Gun', game_text="Does 40 damage plus 20 more damage for each Water Energy attached to Lanturn but not used to pay for this attack's Energy cost. You can't add more then 40 damage in this way.", cost={PokemonTypes.COLORLESS: 3}, damage=40, damage_operator='+', effect=water_gun_extra(40, 20, PokemonTypes.WATER))])
