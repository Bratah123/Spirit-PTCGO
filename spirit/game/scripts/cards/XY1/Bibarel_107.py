"""STUB: effect not implemented — do not guess mechanics.
Bibarel (XY1 #107): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f0e703b-e730-595d-97a6-e82c46e11947",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hypno Headbutt",
            game_text="You may do 30 more damage. If you do, this Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)