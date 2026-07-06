from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8da673b4-dbf9-5585-b21e-84e5ff94a019",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBraviary.Name",
    display_name="Hisuian Braviary",
    searchable_by=["Hisuian Braviary", "Stage 1", "HisuianBraviary"],
    subtypes=["Stage 1"],
    collector_number=149,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Eerie Cry",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon that has any damage counters on it.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
    ],
)