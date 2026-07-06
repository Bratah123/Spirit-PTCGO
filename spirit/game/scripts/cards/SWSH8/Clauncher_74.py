from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ea06ff8-b9d7-57f2-ad9e-2330de2a1449",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    display_name="Clauncher",
    searchable_by=["Clauncher", "Basic", "Clauncher"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=692,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)