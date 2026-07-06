from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a4e426d2-dff5-50c7-bf0b-902972890cf7",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic", "Turtwig"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=387,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)