"""STUB: effect not implemented — do not guess mechanics.
Regigigas (DPP #DP40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    cant_attack_next_turn,
    dpp_regigigas_dp40_drag_off,
)

card = PokemonCardDef(guid='f1009d9d-610b-50df-a011-73457eba2eaa', key='DPP', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name', display_name='Regigigas', searchable_by=['Regigigas', 'Basic', 'Regigigas'], subtypes=['Basic'], collector_number=40, set_code='DPP', rarity=Rarities.RarePromo, hp=100, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, family_id=486, abilities=[Attack(title='Drag Off', game_text="Before doing damage, you may choose 1 of your opponent's Benched Pokémon and switch it with the Defending Pokémon.", cost={PokemonTypes.COLORLESS: 3}, damage=30, effect=dpp_regigigas_dp40_drag_off()), Attack(title='Giga Hammer', game_text="Regigigas can't use Giga Hammer during your next turn.", cost={PokemonTypes.COLORLESS: 4}, damage=80, effect=cant_attack_next_turn())])
