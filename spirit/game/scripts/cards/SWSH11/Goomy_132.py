from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ddb9504d-02ee-578d-bad3-d9c8ac5b6d71",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    display_name="Goomy",
    searchable_by=["Goomy", "Basic", "Goomy"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=704,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Melt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=30,
        ),
    ],
)