from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c210b715-c9dc-5218-bdf3-0e6eebf33c86",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2", "Walrein"],
    subtypes=["Stage 2"],
    collector_number=39,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Hail Prison",
            game_text="Discard 2 Energy from this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)