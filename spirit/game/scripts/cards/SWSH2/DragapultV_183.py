from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _entered_active_this_turn(ctx):
    return ctx.entered_active_this_turn(ctx.attacker)


card = PokemonCardDef(
    guid="31afd2eb-00ff-56a6-a31a-58bda27e11b3",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragapultV.Name",
    display_name="Dragapult V",
    searchable_by=["Dragapult V", "Basic", "V", "DragapultV"],
    subtypes=["Basic", "V"],
    collector_number=183,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=887,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Jet Assault",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_entered_active_this_turn, 80),
        ),
    ],
)