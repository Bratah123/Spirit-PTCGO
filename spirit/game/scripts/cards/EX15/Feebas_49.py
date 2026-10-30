"""STUB: effect not implemented — do not guess mechanics.
Feebas δ (EX15 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import flail_damage
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59e09db2-d639-5dba-841d-6e1e9a7518d3",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas δ",
    searchable_by=["Feebas \u03b4", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Feebas.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flail_damage(10),
        ),
    ],
)