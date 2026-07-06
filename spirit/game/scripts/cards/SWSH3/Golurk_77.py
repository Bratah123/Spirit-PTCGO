from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7de197e3-7c45-5363-a08b-604ca6df84f3",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Dynamic Chop",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Golurk Hammer",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 4},
            damage=180,
        ),
    ],
)