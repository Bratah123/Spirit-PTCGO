"""STUB: effect not implemented — do not guess mechanics.
Minccino (XY10 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba9bd381-05db-5a6a-b366-4c494d7887cd",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino", "Basic", "Minccino"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=572,
    abilities=[
        Attack(
            title="Cleaning Up",
            game_text="Discard a Pok\u00e9mon Tool card attached to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)