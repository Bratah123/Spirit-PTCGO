from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c54dd90-8429-5459-960f-ca1e4711ad38",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    display_name="Chewtle",
    searchable_by=["Chewtle", "Basic", "Chewtle"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SWSH45",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=833,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)