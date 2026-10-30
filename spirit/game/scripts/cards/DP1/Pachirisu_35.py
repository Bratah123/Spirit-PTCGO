from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import minor_errand_running, thunder_jolt_self


card = PokemonCardDef(
    guid="04cf449a-582b-5a45-8f59-13dababe9738",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=417,
    abilities=[
        Attack(
            title="Minor Errand-Running",
            game_text="Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=minor_errand_running(1),
        ),
        Attack(
            title="Thunder Jolt",
            game_text="Flip a coin. If tails, Pachirisu does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=thunder_jolt_self(10),
        ),
    ],
)
