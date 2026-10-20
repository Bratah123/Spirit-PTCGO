"""STUB: effect not implemented — do not guess mechanics.
Feebas (XY5 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca9a3c10-43fa-5213-99b1-0e76362c6ee3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=349,
    abilities=[
        Attack(
            title="Float On",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)