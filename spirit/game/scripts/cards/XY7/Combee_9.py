from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a17c6eb6-e891-5e12-88c4-579102fed3e3",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    display_name="Combee",
    searchable_by=["Combee", "Basic", "Combee"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=415,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)