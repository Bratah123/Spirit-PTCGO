from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5a17640-709d-5667-9a3e-7092b29b1d8a",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    display_name="Baltoy",
    searchable_by=["Baltoy", "Basic", "Baltoy"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=343,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)