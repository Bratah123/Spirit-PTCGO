from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4303d5d8-01a7-5661-84d7-d44f293c7cc4",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=["Piplup", "Basic", "Piplup"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=393,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)