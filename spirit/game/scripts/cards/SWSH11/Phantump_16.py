from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="82c12c6a-d84d-5d1d-a71a-f0c07a5b7dd4",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    display_name="Phantump",
    searchable_by=["Phantump", "Basic", "Phantump"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=708,
    abilities=[
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)