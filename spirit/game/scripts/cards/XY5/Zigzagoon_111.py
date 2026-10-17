"""STUB: effect not implemented — do not guess mechanics.
Zigzagoon (XY5 #111): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8881824a-f161-5579-9993-ad817c8d145e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    display_name="Zigzagoon",
    searchable_by=["Zigzagoon", "Basic", "Zigzagoon"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=263,
    abilities=[
        Attack(
            title="Sand Attack",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)