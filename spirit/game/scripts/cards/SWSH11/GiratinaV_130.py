from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="397ea489-34cc-5382-bad4-2122797e32bf",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaV.Name",
    display_name="Giratina V",
    searchable_by=["Giratina V", "Basic", "V", "GiratinaV"],
    subtypes=["Basic", "V"],
    collector_number=130,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=487,
    abilities=[
        Attack(
            title="Abyss Seeking",
            game_text="Look at the top 4 cards of your deck and put 2 of them into your hand. Put the other cards in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)