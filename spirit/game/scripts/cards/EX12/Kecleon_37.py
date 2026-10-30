"""STUB: effect not implemented — do not guess mechanics.
Kecleon (EX12 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack, flip_bonus
from spirit.game.card_effects.ex import (
    reactive_colors_passive,
)

card = PokemonCardDef(guid='74abad32-4b73-5f5f-b04e-0be535fc8ae8', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name', display_name='Kecleon', searchable_by=['Kecleon', 'Basic', 'Kecleon'], subtypes=['Basic'], collector_number=37, set_code='EX12', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=352, abilities=[Ability(title='Reactive Colors', game_text='If Kecleon has any React Energy cards attached to it, Kecleon is Grass, Fire, Water, Lightning, Psychic, and Fighting type.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=reactive_colors_passive(PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING)), Attack(title='Tongue Whip', game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 1}, effect=snipe_attack(10, pool='any')), Attack(title='Quick Attack', game_text='Flip a coin. If heads, this attack does 10 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='+', effect=flip_bonus(20))])
