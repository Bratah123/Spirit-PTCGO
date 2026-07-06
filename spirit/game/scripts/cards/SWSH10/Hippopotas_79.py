from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dd5968d5-89e4-51aa-b535-9503666dd0bd",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    display_name="Hippopotas",
    searchable_by=["Hippopotas", "Basic", "Hippopotas"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=449,
    abilities=[
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)