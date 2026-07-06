from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1429d89e-bb69-5127-a059-69dc1ad7c3cc",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    display_name="Cufant",
    searchable_by=["Cufant", "Basic", "Cufant"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SWSH3",
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