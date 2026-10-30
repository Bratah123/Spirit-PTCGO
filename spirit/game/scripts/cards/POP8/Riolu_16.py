"""Riolu (POP8 #16)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import condition_immunity_passive


card = PokemonCardDef(
    guid="eb0e29dd-1bf8-5560-9624-9f399ca2d58e",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name="Riolu",
    searchable_by=["Riolu", "Basic", "Riolu"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="POP8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=447,
    abilities=[
        Ability(
            title="Inner Focus",
            game_text="Riolu can't be Paralyzed.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=condition_immunity_passive(SpecialConditions.PARALYZED),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)
