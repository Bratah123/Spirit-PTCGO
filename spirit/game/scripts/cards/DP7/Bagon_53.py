"""STUB: effect not implemented — do not guess mechanics.
Bagon (DP7 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a406e4eb-0556-538b-b395-d084e5258f35",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon",
    searchable_by=["Bagon", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=371,
    abilities=[
        Attack(
            title="Scary Face",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack or retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)