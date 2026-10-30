"""STUB: effect not implemented — do not guess mechanics.
Vibrava (EX12 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    bi_blast,
)

card = PokemonCardDef(guid='0ebf0441-b48e-5c78-81bc-db1fb1c8a1e0', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name', display_name='Vibrava', searchable_by=['Vibrava', 'Stage 1', 'Vibrava'], subtypes=['Stage 1'], collector_number=46, set_code='EX12', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name', family_id=328, abilities=[Attack(title='Supersonic', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.CONFUSED, flip=True)), Attack(title='Bi-Blast', game_text='If Vibrava has any React Energy cards attached to it, this attack does 20 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='+', effect=bi_blast(20, 20))])
