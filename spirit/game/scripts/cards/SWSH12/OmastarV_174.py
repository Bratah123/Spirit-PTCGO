from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="09a33f5c-f76f-5f55-8475-5ae5fe5318c8",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OmastarV.Name",
    display_name="Omastar V",
    searchable_by=["Omastar V", "Basic", "V", "OmastarV"],
    subtypes=["Basic", "V"],
    collector_number=174,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=139,
    abilities=[
        Attack(
            title="Primal Guidance",
            game_text="Search your deck for up to 2 Pok\u00e9mon that evolve from an Item card that has \"Fossil\" in its name and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tentacle Lock",
            game_text="If the Defending Pok\u00e9mon is an Evolution Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=unimplemented,
        ),
    ],
)