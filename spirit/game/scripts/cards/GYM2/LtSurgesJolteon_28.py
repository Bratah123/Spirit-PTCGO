from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import high_voltage, thunder_flare


card = PokemonCardDef(
    guid="182f9fb9-7519-5117-baf6-9ce743df6989",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesJolteon.Name",
    display_name="Lt. Surge's Jolteon",
    searchable_by=["Lt. Surge's Jolteon", "Stage 1", "LtSurgesJolteon"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesEevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="High Voltage",
            game_text="Flip a coin. If heads, your opponent can't play Trainer cards during his or her next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=high_voltage,
        ),
        Attack(
            title="Thunder Flare",
            game_text="Does 30 damage plus 10 damage times the number of damage counters on Lt. Surge's Jolteon, then flip a coin. If tails, Lt. Surge's Jolteon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            damage_operator="+",
            effect=thunder_flare,
        ),
    ],
)
