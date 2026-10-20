"""STUB: effect not implemented — do not guess mechanics.
Regigigas (XY4 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be1a842b-b1cb-569a-8a8c-f959ae89788d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Daunt",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 40 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
        ),
    ],
)