from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b06df0b4-70a2-5d5b-b741-1951bd2cfbca",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic", "Karrablast"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Attack(
            title="Continuous Headbutt",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)