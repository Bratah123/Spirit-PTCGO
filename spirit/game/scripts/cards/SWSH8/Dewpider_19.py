from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1495517-9400-510d-87e5-7ab8be2adb52",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    display_name="Dewpider",
    searchable_by=["Dewpider", "Basic", "Dewpider"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=751,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)