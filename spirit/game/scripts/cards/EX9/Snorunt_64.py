from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16ffa82c-b770-56eb-bce9-63f1be18c777",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    display_name="Snorunt",
    searchable_by=["Snorunt", "Basic", "Snorunt"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=361,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)