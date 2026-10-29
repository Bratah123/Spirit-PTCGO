from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6a0d3a98-909d-51a9-976e-717f28817c9a",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="DM",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=147,
    abilities=[
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)