from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30d21668-3a17-5b2d-96ef-d70f332f1446",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    display_name="Snom",
    searchable_by=["Snom", "Basic", "Snom"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=872,
    abilities=[
        Attack(
            title="Find Ice",
            game_text="Search your deck for up to 2 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)