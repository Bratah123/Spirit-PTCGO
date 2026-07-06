from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="218b52a5-8630-5c60-b5b4-4509d859dbcc",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    display_name="Goomy",
    searchable_by=["Goomy", "Basic", "Goomy"],
    subtypes=["Basic"],
    collector_number=195,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=704,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Melt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)