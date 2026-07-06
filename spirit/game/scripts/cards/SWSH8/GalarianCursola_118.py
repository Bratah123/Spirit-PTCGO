from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1bc64ee-e196-54e6-aa94-fa891e449f7a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCursola.Name",
    display_name="Galarian Cursola",
    searchable_by=["Galarian Cursola", "Stage 1", "GalarianCursola"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCorsola.Name",
    family_id=222,
    abilities=[
        Attack(
            title="Force Regeneration",
            game_text="Put a Basic Pok\u00e9mon V from your opponent's discard pile onto their Bench. If you do, put damage counters on that Pok\u00e9mon until its remaining HP is 30.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)