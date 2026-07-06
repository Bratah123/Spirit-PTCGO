from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a0f3b1c3-5168-5a50-807c-318e3dda08b6",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    display_name="Unown V",
    searchable_by=["Unown V", "Basic", "V", "UnownV"],
    subtypes=["Basic", "V"],
    collector_number=65,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=201,
    abilities=[
        Attack(
            title="Shady Stamp",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Victory Symbol",
            game_text="If you use this attack when you have only 1 Prize card remaining, you win this game.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)