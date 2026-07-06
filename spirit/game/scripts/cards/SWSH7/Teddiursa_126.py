from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9b85b78b-3b60-5c7d-b112-a6ac75bdb842",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    display_name="Teddiursa",
    searchable_by=["Teddiursa", "Basic", "Teddiursa"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=216,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)