from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ab717cd-88f9-5a76-b8c6-e794e0a2d72c",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    display_name="Timburr",
    searchable_by=["Timburr", "Basic", "Timburr"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=532,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)