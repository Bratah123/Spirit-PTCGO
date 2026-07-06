from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="621b6d89-2340-5408-8f0a-cdf91886d2e6",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    display_name="Clobbopus",
    searchable_by=["Clobbopus", "Basic", "Clobbopus"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SWSH4",
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
            damage=20,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)