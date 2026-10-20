from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1949e6db-f07a-57a6-af87-a7a425c7f9c8",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    display_name="Machop",
    searchable_by=["Machop", "Basic", "Machop"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=66,
    abilities=[
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)