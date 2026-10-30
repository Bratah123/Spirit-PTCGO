"""STUB: effect not implemented — do not guess mechanics.
Aggron (EX12 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    bound_crush,
    heavy_blow_react_or_minus,
)

card = PokemonCardDef(guid='dc01c2d9-7198-53b2-b79e-c4d630973bc9', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name', display_name='Aggron', searchable_by=['Aggron', 'Stage 2', 'Aggron'], subtypes=['Stage 2'], collector_number=2, set_code='EX12', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name', family_id=304, abilities=[Attack(title='Heavy Blow', game_text='Does 70 damage minus 10 damage for each damage counter on Aggron. If Aggron has any React Energy cards attached to it, this attack does 70 damage instead.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=70, damage_operator='-', effect=heavy_blow_react_or_minus(70, 10)), Attack(title='Bound Crush', game_text="Choose 1 of your opponent's Pokémon. This attack does 60 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) During your next turn, Aggron can't use Bound Crush.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, effect=bound_crush(60), locks_next_turn=True)])
