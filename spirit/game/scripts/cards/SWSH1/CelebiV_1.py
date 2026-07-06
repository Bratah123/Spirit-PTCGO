from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93c4af72-ab2c-566a-871f-9834d9db7e9c",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiV.Name",
    display_name="Celebi V",
    searchable_by=["Celebi V", "Basic", "V", "CelebiV"],
    subtypes=["Basic", "V"],
    collector_number=1,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for up to 2 Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Line Force",
            game_text="This attack does 20 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)