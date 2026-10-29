from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus

from spirit.game.card_effects.sm8 import (
    molting,
    molting_condition,
)

card = PokemonCardDef(
    guid="dac17095-31e2-5371-971a-8c5801de5928",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Molting",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put a Shedinja from your discard pile onto your Bench.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=molting,
            trigger=Triggers.ON_EVOLVE,
            condition=molting_condition,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
    ],
)