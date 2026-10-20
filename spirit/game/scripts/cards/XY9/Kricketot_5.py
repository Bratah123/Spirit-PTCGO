"""STUB: effect not implemented — do not guess mechanics.
Kricketot (XY9 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b4a1275-bc5b-5b76-9929-ebdac0110cd1",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    display_name="Kricketot",
    searchable_by=["Kricketot", "Basic", "Kricketot"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=401,
    abilities=[
        Attack(
            title="Bug Hunch",
            game_text="Search your deck for up to 3 Grass Pok\u00e9mon, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)