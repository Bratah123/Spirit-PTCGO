"""STUB: effect not implemented — do not guess mechanics.
Sewaddle (XY4 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5dfc6b84-d5cb-52d0-88dd-8a444ee8620a",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    display_name="Sewaddle",
    searchable_by=["Sewaddle", "Basic", "Sewaddle"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=540,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)