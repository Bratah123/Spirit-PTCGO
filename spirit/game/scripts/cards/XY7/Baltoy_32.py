"""STUB: effect not implemented — do not guess mechanics.
Baltoy (XY7 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df3c3948-bbbe-5a99-851a-48364afb9c49",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    display_name="Baltoy",
    searchable_by=["Baltoy", "Basic", "Baltoy"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=343,
    abilities=[
        Attack(
            title="Future Spin",
            game_text="Look at the top 3 cards of either player's deck and put them back on top of that player's deck in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)