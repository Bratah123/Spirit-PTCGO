from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a91f8d6e-3f77-55b2-8075-5552d169054f",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    display_name="Hippopotas",
    searchable_by=["Hippopotas", "Basic", "Hippopotas"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=449,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)