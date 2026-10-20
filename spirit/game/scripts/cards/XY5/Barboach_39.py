from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3eb03ebe-23d3-56e8-a8f5-6c4faeacd4d7",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    display_name="Barboach",
    searchable_by=["Barboach", "Basic", "Barboach"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=339,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)