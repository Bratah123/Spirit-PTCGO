from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7896df0b-fc2d-5142-a595-0de266d1bbbb",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic", "Voltorb"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Speed Ball",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)