"""STUB: effect not implemented — do not guess mechanics.
Gastly (XY8 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6bb5a2c0-5099-5da5-b593-95011d51bdd4",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Sleep Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)