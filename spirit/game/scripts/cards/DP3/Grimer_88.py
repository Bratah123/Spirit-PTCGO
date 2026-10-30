"""STUB: effect not implemented — do not guess mechanics.
Grimer (DP3 #88): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="78e0145a-6cc3-539a-af5a-29db42daf895",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic", "Grimer"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Mud Bomb",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Gunky",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)