from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.support_common import _is_damaged


async def counter_press(ctx):
    """90. During your opponent's next turn, a hit on this Pokemon reflects
    as damage counters on the attacker (even if this Pokemon is KO'd)."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, CounterPressPassive())


class CounterPressPassive(Passive):
    """Reflects the damage this Pokemon takes onto the attacker as counters."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(calc.amount, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


card = PokemonCardDef(
    guid="36742245-10fc-5a40-97d9-00513d066b6a",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 1", "Bastiodon"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Attack(
            title="Counter Head",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=counter_press,
        ),
        Attack(
            title="Fortress of Rage",
            game_text="This attack does 10 more damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=damage_per(lambda ctx: sum(1 for p in ctx.my_bench() if _is_damaged(ctx.board, p)), 10, base=100),
        ),
    ],
)