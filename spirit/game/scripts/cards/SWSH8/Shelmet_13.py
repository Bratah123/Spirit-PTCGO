from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8366b56c-5049-5dd6-8530-e1faabb04c39",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name="Shelmet",
    searchable_by=["Shelmet", "Basic", "Fusion Strike", "Shelmet"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=13,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=616,
    abilities=[
        Attack(
            title="Spit Beam",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)