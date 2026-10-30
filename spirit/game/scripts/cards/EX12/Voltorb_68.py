"""STUB: effect not implemented — do not guess mechanics.
Voltorb (EX12 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    bouncing_ball,
)

card = PokemonCardDef(guid='d4e9a102-4195-5aa5-938a-379940105c47', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name', display_name='Voltorb', searchable_by=['Voltorb', 'Basic', 'Voltorb'], subtypes=['Basic'], collector_number=68, set_code='EX12', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=100, abilities=[Attack(title='Thunder Wave', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Bouncing Ball', game_text='Voltorb does 10 damage to itself.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=bouncing_ball(10))])
