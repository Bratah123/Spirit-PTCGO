"""STUB: effect not implemented — do not guess mechanics.
Tentacruel (EX12 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack, flip_damage
from spirit.game.card_effects.ex import (
    reactive_shield_vs_ex_passive,
)

card = PokemonCardDef(guid='846c8961-dc63-52e6-80b9-aae91e6ac4d2', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name', display_name='Tentacruel', searchable_by=['Tentacruel', 'Stage 1', 'Tentacruel'], subtypes=['Stage 1'], collector_number=45, set_code='EX12', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name', family_id=72, abilities=[Ability(title='Reactive Shield', game_text="As long as Tentacruel has any React Energy cards attached to it, prevent all effects, including damage, done to any of your Tentacruel in play by attacks from your opponent's Pokémon-ex.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=reactive_shield_vs_ex_passive()), Attack(title='Water Arrow', game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1}, effect=snipe_attack(20, pool='any', count=1)), Attack(title='Fury Strikes', game_text='Flip 3 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=flip_damage(coins=3, per_heads=20))])
