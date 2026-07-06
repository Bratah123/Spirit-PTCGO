from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ed7d816-be6f-5243-a22b-d601beeb0ed2",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    display_name="Hattrem",
    searchable_by=["Hattrem", "Stage 1", "Hattrem"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    family_id=856,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)