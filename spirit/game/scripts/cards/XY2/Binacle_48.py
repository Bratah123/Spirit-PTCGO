"""STUB: effect not implemented — do not guess mechanics.
Binacle (XY2 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d3a655d5-b6cb-5ad2-8e60-8f5884a60995",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    display_name="Binacle",
    searchable_by=["Binacle", "Basic", "Binacle"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=688,
    abilities=[
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)