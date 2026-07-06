from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa0abf4f-e929-5212-a723-9ec6f00f7f65",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaV.Name",
    display_name="Giratina V",
    searchable_by=["Giratina V", "Basic", "V", "GiratinaV"],
    subtypes=["Basic", "V"],
    collector_number=186,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
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