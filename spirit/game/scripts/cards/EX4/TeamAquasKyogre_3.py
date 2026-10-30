"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Kyogre (EX4 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import bonus_if_special_condition, power_saver_condition


card = PokemonCardDef(
    guid="f3593dea-70bb-58c5-8fd5-b51a9cd21817",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasKyogre.Name",
    display_name="Team Aqua's Kyogre",
    searchable_by=["Team Aqua's Kyogre", "Basic", "TeamAquasKyogre"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER, PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="As long as the number of Pok\u00e9mon in play (both yours and your opponent's) that has Team Aqua in its name is 3 or less, Team Aqua's Kyogre can't attack.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=None,
        ),
        Attack(
            title="Aqua Trip",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            condition=power_saver_condition("Team Aqua"),
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True, tails_conditions=(SpecialConditions.ASLEEP,)),
        ),
        Attack(
            title="Aqua Smash",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            condition=power_saver_condition("Team Aqua"),
            effect=bonus_if_special_condition(20),
        ),
    ],
)