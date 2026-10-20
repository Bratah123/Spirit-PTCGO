"""STUB: effect not implemented — do not guess mechanics.
Elgyem (XY8 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="efd8c7aa-05b8-5bd4-be06-03bb2b2724a1",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem", "Basic", "Elgyem"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=605,
    abilities=[
        Attack(
            title="Psych Up",
            game_text="During your next turn, this Pok\u00e9mon's Psych Up attack does 20 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)