from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53087943-2cbd-5b6f-9d36-318a0d663014",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    display_name="Barboach",
    searchable_by=["Barboach", "Basic", "Barboach"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=339,
    abilities=[
        Attack(
            title="Splash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)