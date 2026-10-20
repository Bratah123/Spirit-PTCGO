"""STUB: effect not implemented — do not guess mechanics.
Magikarp (XY12 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="702b6b78-df21-5364-b24c-5032046d37a9",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="XY12",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)