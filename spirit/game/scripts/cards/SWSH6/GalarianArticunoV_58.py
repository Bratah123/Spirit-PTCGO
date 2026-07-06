from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="599da55f-31bb-5804-832f-57611541a50d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianArticunoV.Name",
    display_name="Galarian Articuno V",
    searchable_by=["Galarian Articuno V", "Basic", "V", "GalarianArticunoV"],
    subtypes=["Basic", "V"],
    collector_number=58,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Reconstitute",
            game_text="You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyray",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=unimplemented,
        ),
    ],
)