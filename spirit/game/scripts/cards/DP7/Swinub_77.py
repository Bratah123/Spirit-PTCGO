"""STUB: effect not implemented — do not guess mechanics.
Swinub (DP7 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c8d2a556-67a4-5041-b8d2-840368e08b98",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    display_name="Swinub",
    searchable_by=["Swinub", "Basic", "Swinub"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=220,
    abilities=[
        Attack(
            title="Freezing Breath",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Take Down",
            game_text="Flip a coin. If tails, Swinub does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)