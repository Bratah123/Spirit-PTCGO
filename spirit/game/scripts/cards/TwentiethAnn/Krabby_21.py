from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="52bd8d14-a9e1-5f67-a93b-8c57ff4c7fd6",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    display_name="Krabby",
    searchable_by=["Krabby", "Basic", "Krabby"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=98,
    abilities=[
        Attack(
            title="Vice Grip",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 3},
            damage=50,
        ),
    ],
)