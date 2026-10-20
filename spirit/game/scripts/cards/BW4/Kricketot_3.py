from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54783ec1-fdcb-5081-9a37-2fa956630b30",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    display_name="Kricketot",
    searchable_by=["Kricketot", "Basic", "Kricketot"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=401,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 10 more damage for each heads.",
            cost={PokemonTypes.GRASS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)