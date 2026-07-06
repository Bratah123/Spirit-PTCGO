from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e3f2f24-e06f-57b0-b235-a69a33a36a01",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    display_name="Shellos",
    searchable_by=["Shellos", "Basic", "Shellos"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=422,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)