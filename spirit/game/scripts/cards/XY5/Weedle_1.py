"""STUB: effect not implemented — do not guess mechanics.
Weedle (XY5 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="046aa0b1-69ff-5b36-adb2-12d328132300",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Multiply",
            game_text="Search your deck for Weedle and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)