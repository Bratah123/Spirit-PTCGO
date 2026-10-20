from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="27725213-5b5a-54a3-bb00-1290c9a78c44",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    display_name="Finneon",
    searchable_by=["Finneon", "Basic", "Finneon"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=456,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)