from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf4be9ee-5662-59e2-ac80-b03e2b9dd4ee",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name",
    display_name="Copperajah",
    searchable_by=["Copperajah", "Stage 1", "Single Strike", "Copperajah"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=192,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
        Attack(
            title="High Horsepower",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)