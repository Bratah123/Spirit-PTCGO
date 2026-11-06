from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f038181e-7d3c-5715-b079-f33c03490855",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    display_name="Sewaddle",
    searchable_by=["Sewaddle", "Basic", "Sewaddle"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=540,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)