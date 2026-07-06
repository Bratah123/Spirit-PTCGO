from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9e261b40-58e3-5ab6-a26f-0bc3c07a885e",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    display_name="Sobble",
    searchable_by=["Sobble", "Basic", "Sobble"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=816,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)