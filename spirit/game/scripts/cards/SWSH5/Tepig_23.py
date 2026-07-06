from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5749e809-2c0e-57e4-8f15-eadd8020b8b4",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    display_name="Tepig",
    searchable_by=["Tepig", "Basic", "Single Strike", "Tepig"],
    subtypes=["Basic", "Single Strike"],
    collector_number=23,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=498,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)