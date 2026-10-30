from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import (
    bonus_if, condition_attack, defender_has_any_condition,
)
from spirit.game.card_effects.ex import partner_retreat_free


card = PokemonCardDef(
    guid="7a58926a-a45a-50a6-84bf-f692839063eb",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Ability(
            title="Uplifting Glow",
            game_text="As long as Illumise is in play, Volbeat's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=partner_retreat_free("Illumise"),
        ),
        Attack(
            title="Toxic Vibration",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(
                SpecialConditions.POISONED, flip=True,
                tails_conditions=(SpecialConditions.ASLEEP,),
            ),
        ),
        Attack(
            title="Pester",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(defender_has_any_condition, 20),
        ),
    ],
)
