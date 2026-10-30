from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import collapse_asleep, rest_up_between_turns, toss_and_turn

card = PokemonCardDef(
    guid="e92c6410-ba3c-589c-a3cc-095a379a5ab8",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Rest Up",
            game_text="If Snorlax remains Asleep between turns, remove 2 damage counters from Snorlax (remove 1 if there is only 1).",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=rest_up_between_turns(),
        ),
        Attack(
            title="Collapse",
            game_text="Snorlax is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=collapse_asleep(),
        ),
        Attack(
            title="Toss and Turn",
            game_text="If Snorlax is Asleep, this attack does 30 damage plus 30 more damage. (This attack can be used even if Snorlax is Asleep.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=toss_and_turn(30, 30),
        ),
    ],
)