from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    synchronized_lift_passive, may_move_own_energy, snipe_own_bench,
)


card = PokemonCardDef(
    guid="84c33a50-efc4-5c0d-8ea7-f7f2356a41d9",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name",
    display_name="Zapdos ex",
    searchable_by=["Zapdos ex", "Basic", "ex", "Zapdosex"],
    subtypes=["Basic", "ex"],
    collector_number=33,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=145,
    abilities=[
        Ability(
            title="Synchronized Lift",
            game_text="As long as you have Articuno ex and Moltres ex in play, the Retreat Cost for Zapdos ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=synchronized_lift_passive("Articuno ex", "Moltres ex"),
        ),
        Attack(
            title="Thunder Gift",
            game_text="You may move a Lightning Energy card attached to Zapdos ex to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=may_move_own_energy(PokemonTypes.LIGHTNING),
        ),
        Attack(
            title="Lightning Wing",
            game_text="Does 10 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=snipe_own_bench(10),
        ),
    ],
)
