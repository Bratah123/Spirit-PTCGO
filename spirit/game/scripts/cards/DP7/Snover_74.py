"""STUB: effect not implemented — do not guess mechanics.
Snover (DP7 #74): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1401526e-fbac-5a5b-aeb5-5cd60fb1ab93",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic", "Snover"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=459,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Snover during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Powder Snow",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)