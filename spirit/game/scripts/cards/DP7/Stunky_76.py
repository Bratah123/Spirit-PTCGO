"""STUB: effect not implemented — do not guess mechanics.
Stunky (DP7 #76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    switch_self_attack,
)

card = PokemonCardDef(guid='823cc3b4-1fe4-56c3-85a7-f3f653f6a4b0', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name', display_name='Stunky', searchable_by=['Stunky', 'Basic', 'Stunky'], subtypes=['Basic'], collector_number=76, set_code='DP7', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=434, abilities=[Attack(title='Gnaw and Run', game_text='Switch Stunky with 1 of your Benched Pokémon.', cost={PokemonTypes.DARKNESS: 1}, damage=10, effect=switch_self_attack(damage=10)), Attack(title='Double Scratch', game_text='Flip 2 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=flip_damage(2, per_heads=20))])
