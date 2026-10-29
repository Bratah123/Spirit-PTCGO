from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4605161e-cccb-5a41-a6e1-b10ac8353d2b",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    display_name="Fennekin",
    searchable_by=["Fennekin", "Basic", "Fennekin"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=653,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)