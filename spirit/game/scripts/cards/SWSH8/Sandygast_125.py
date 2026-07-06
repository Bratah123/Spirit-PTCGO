from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="634f8e0c-27f6-5dda-a34a-5182bf151173",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    display_name="Sandygast",
    searchable_by=["Sandygast", "Basic", "Sandygast"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=769,
    abilities=[
        Attack(
            title="Vibration",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)