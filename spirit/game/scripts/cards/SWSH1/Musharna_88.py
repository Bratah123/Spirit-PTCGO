from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb1f1731-14bd-59fd-8657-a7fb347b2b2b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna", "Stage 1", "Musharna"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    family_id=517,
    abilities=[
        Attack(
            title="Sleepy Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. During Pok\u00e9mon Checkup, your opponent flips 2 coins instead of 1. If either of them is tails, that Pok\u00e9mon is still Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Super Hypnoblast",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)