from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c475920f-518c-5434-9448-1e6e6565c897",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic", "Rapid Strike", "Inkay"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=69,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=686,
    abilities=[
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)