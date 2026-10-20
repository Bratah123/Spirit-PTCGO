from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76d4dc43-e286-5bd4-96d1-5c0b33028bc9",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Attack(
            title="Raging Pecks",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads. This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)