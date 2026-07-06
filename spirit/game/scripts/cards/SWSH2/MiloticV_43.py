from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f37a4da2-72c4-58cc-b785-2c07ebd3ffe7",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MiloticV.Name",
    display_name="Milotic V",
    searchable_by=["Milotic V", "Basic", "V", "MiloticV"],
    subtypes=["Basic", "V"],
    collector_number=43,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=350,
    abilities=[
        Attack(
            title="Aqua Impact",
            game_text="This attack does 50 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Hypno Splash",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)