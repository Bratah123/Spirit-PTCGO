from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6fb33170-b187-5a53-b3d2-11f22e6f3241",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    display_name="Shellos",
    searchable_by=["Shellos", "Basic", "Shellos"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=422,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)