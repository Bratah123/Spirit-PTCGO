from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fbc82ddd-95b0-519a-8096-e41e71549c7d",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik", "Basic", "Joltik"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)