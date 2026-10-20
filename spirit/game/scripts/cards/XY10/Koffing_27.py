"""STUB: effect not implemented — do not guess mechanics.
Koffing (XY10 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7c72b4d6-f1c8-5f43-8bfe-09e44922fde9",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic", "Koffing"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Attack(
            title="Division",
            game_text="Search your deck for up to 2 Koffing and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)