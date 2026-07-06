from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ba79e90-b9bb-5851-baa2-d08544f2b7bb",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Single Strike", "Weedle"],
    subtypes=["Basic", "Single Strike"],
    collector_number=1,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)