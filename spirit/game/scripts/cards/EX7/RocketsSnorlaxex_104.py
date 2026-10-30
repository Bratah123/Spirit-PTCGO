from spirit.game.card_effects.ex import collapse_asleep_ex7, dark_healer_between_turns
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Snorlax ex (EX7 #104): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="87923f87-a14e-5168-8513-c3658f1a214d",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsSnorlaxex.Name",
    display_name="Rocket's Snorlax ex",
    searchable_by=["Rocket's Snorlax ex", "Basic", "ex", "RocketsSnorlaxex"],
    subtypes=["Basic", "ex"],
    collector_number=104,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Dark Healer",
            trigger=Triggers.BETWEEN_TURNS,
            game_text="As long as Rocket's Snorlax ex has any Darkness Energy attached to it, remove 1 damage counter from Rocket's Snorlax ex between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=dark_healer_between_turns(),
        ),
        Attack(
            title="Poison Claws",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Collapse",
            game_text="Rocket's Snorlax ex is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            # STUB: attack effect not implemented
            effect=collapse_asleep_ex7(),
        ),
    ],
)