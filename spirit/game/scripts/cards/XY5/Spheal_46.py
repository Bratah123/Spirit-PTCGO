from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="719cb916-5999-5267-ac2c-14a02e577e86",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    display_name="Spheal",
    searchable_by=["Spheal", "Basic", "Spheal"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Ice Ball",
            cost={PokemonTypes.WATER: 2},
            damage=20,
        ),
    ],
)