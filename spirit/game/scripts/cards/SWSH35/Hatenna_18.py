from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="475a195f-8f48-557f-b30f-afdde1ad4ce6",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    display_name="Hatenna",
    searchable_by=["Hatenna", "Basic", "Hatenna"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SWSH35",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=856,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)