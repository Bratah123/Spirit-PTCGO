from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da6f9a68-b24e-5f99-bb87-f882605f99f6",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    display_name="Glaceon V",
    searchable_by=["Glaceon V", "Basic", "V", "GlaceonV"],
    subtypes=["Basic", "V"],
    collector_number=40,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=471,
    abilities=[
        Attack(
            title="Frozen Awakening",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Snow",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)