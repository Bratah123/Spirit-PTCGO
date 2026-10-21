from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack, bonus_if


def _has_condition(ctx):
    d = ctx.opponent_active()
    return d is not None and bool(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="41a3579d-5239-501a-8834-cbc90d33f6d5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SceptileEX.Name",
    display_name="Sceptile-EX",
    searchable_by=["Sceptile-EX", "Basic", "EX", "SceptileEX"],
    subtypes=["Basic", "EX"],
    collector_number=7,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=254,
    abilities=[
        Attack(
            title="Sleep Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Unseen Claw",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 70 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_has_condition, 70),
        ),
    ],
)