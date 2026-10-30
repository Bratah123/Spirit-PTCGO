"""STUB: effect not implemented — do not guess mechanics.
Unown [L] (DP4 #91): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="815f7226-bc95-55e3-abcc-e901243cea7d",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownL.Name",
    display_name="Unown [L]",
    searchable_by=["Unown [L]", "Basic", "UnownL"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="DP4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="LINK",
            game_text="Unown L can use any attack from any Unown in play (both yours and your opponent's). (You still have to pay for that attack's Energy cost.)",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Search either player's discard pile for up to any 2 cards, show them to your opponent, and put them on top of that player's deck in any order you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)