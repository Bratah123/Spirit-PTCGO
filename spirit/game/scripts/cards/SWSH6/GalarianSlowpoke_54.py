from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c3540b7-bf02-5197-99ce-730776d67ccf",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    display_name="Galarian Slowpoke",
    searchable_by=["Galarian Slowpoke", "Basic", "GalarianSlowpoke"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=79,
    abilities=[
        Attack(
            title="Sharpness",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)