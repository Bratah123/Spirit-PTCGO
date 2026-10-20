"""STUB: effect not implemented — do not guess mechanics.
Binacle (XY10 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b695338-e2ec-5b9b-90ea-d9fd1ef87057",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    display_name="Binacle",
    searchable_by=["Binacle", "Basic", "Binacle"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=688,
    abilities=[
        Attack(
            title="Swing Around",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)