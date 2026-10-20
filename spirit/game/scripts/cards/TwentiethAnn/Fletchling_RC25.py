"""STUB: effect not implemented — do not guess mechanics.
Fletchling (TwentiethAnn #RC25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c49eb161-61c7-5d7c-85ab-eb6f552cb1b3",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    display_name="Fletchling",
    searchable_by=["Fletchling", "Basic", "Fletchling"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=661,
    abilities=[
        Attack(
            title="Warble",
            game_text="Search your deck for up to 2 Fletchling, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)