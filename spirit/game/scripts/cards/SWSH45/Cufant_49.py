from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4f42e9a-74e0-5889-bd27-dad8b63814b1",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    display_name="Cufant",
    searchable_by=["Cufant", "Basic", "Cufant"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SWSH45",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=878,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)