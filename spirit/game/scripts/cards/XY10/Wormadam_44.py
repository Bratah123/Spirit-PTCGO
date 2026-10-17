"""STUB: effect not implemented — do not guess mechanics.
Wormadam (XY10 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3205659b-83e7-5705-b1f2-74c4ea2eea27",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wormadam.Name",
    display_name="Wormadam",
    searchable_by=["Wormadam", "Stage 1", "Wormadam"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Twin Bursts",
            game_text="If Mothim is on your Bench, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)