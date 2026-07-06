from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b11b08e-094c-5914-8f47-f27f811d17dc",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    display_name="Clobbopus",
    searchable_by=["Clobbopus", "Basic", "Clobbopus"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=852,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)