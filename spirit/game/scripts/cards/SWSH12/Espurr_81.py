from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="49bb60d6-1b31-5ffc-9227-ef898b696762",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic", "Espurr"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=677,
    abilities=[
        Attack(
            title="Mumble",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)