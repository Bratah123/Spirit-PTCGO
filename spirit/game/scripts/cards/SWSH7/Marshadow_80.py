from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="61197dd1-389f-59da-b240-7015c62b6188",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic", "Rapid Strike", "Marshadow"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=80,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=802,
    abilities=[
        Attack(
            title="Rapid Hunt",
            game_text="Search your deck for up to 2 Rapid Strike cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Flicker",
            game_text="If the Defending Pok\u00e9mon is Knocked Out during your next turn, take 1 more Prize card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)