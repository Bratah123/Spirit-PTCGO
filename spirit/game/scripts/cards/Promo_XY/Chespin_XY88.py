from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="44bdbcfa-0936-55e2-ae3d-769c6471d563",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    display_name="Chespin",
    searchable_by=["Chespin", "Basic", "Chespin"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=650,
    abilities=[
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)