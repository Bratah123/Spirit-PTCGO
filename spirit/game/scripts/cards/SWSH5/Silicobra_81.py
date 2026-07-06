from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14ba7341-0a36-547e-bea8-d69a4a89143d",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    display_name="Silicobra",
    searchable_by=["Silicobra", "Basic", "Silicobra"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=843,
    abilities=[
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)