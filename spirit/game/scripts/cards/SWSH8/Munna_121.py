from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd694bcd-5805-5f5d-8e2a-c2a4e6535f6b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic", "Munna"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=517,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)