from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import (
    bonus_if, condition_attack, defender_has_any_condition,
)
from spirit.game.card_effects.ex import partner_typed_takes_less


card = PokemonCardDef(
    guid="e9c61b38-8786-53e4-bba8-f248bd4cf761",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic", "Illumise"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Ability(
            title="Glowing Screen",
            game_text="As long as Volbeat is in play, any damage done to Illumise by attacks from Fighting Pok\u00e9mon and Darkness Pok\u00e9mon is reduced by 30. You can't reduce more than 30 damage even if there is more than 1 Volbeat in play.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=partner_typed_takes_less(
                30, "Volbeat",
                (PokemonTypes.FIGHTING, PokemonTypes.DARKNESS),
            ),
        ),
        Attack(
            title="Chaotic Noise",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(
                SpecialConditions.CONFUSED, flip=True,
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
