"""Reusable Passive factories and temporary-shield effect factories.

GROUP A builds configured Passive instances for Ability(passive=)/Tool/
Stadium/Energy definitions. GROUP B builds complete attack effects (printed
damage first, then the rider) around expiring temp passives; the apply_*
helpers are the damage-free riders for composition inside bespoke effects.

Predicate conventions: `protects` is 'carrier' | 'team' | callable(target,
carrier). Side/holder gates are built into each factory, so refining preds
(attacker_pred / target_pred / holder_pred) take just the entity; block-hook
preds (no_retreat / ability_lock / healing_block / retreat_free) take
(target, carrier).
"""

from typing import Any, Callable, Optional

from spirit.game.attributes import AttrID
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    carrier_pokemon,
)


# ----------------------------------------------------------------------
# Shared predicate plumbing
# ----------------------------------------------------------------------

def _protects_pred(protects) -> Callable[[Any, Any], bool]:
    """Resolves the 'carrier' | 'team' | callable(target, carrier) tri-form."""
    if callable(protects):
        return protects
    if protects == "team":
        return lambda target, carrier: (
            target.owning_player_id == carrier.owning_player_id
        )
    if protects in (None, "carrier"):
        return lambda target, carrier: carrier_pokemon(carrier) is target
    raise ValueError(f"protects must be 'carrier', 'team' or a callable: {protects!r}")


def is_in_active_spot(pokemon) -> bool:
    """Whether a top-level Pokemon sits in its owner's Active spot."""
    parent = getattr(pokemon, "parent", None)
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


def opposing_pokemon(target, carrier) -> bool:
    """(target, carrier) pred: target belongs to the other player."""
    return target.owning_player_id != carrier.owning_player_id


def opposing_active(target, carrier) -> bool:
    """(target, carrier) pred: target is the opposing Active Pokemon."""
    return opposing_pokemon(target, carrier) and is_in_active_spot(target)


# ======================================================================
# GROUP A -- continuous Passive factories
# ======================================================================

class TakesLessPassive(Passive):
    """Protected Pokemon take N less damage from opposing attacks (after W/R)."""

    def __init__(self, amount, protects="carrier", attacker_pred=None,
                 stack_key=None):
        self.amount = amount
        self.protects = _protects_pred(protects)
        self.attacker_pred = attacker_pred
        self.stack_key = stack_key

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if not self.protects(calc.target, carrier):
            return
        if self.attacker_pred is not None and (
                calc.attacker is None or not self.attacker_pred(calc.attacker)):
            return
        if self.stack_key:
            if self.stack_key in calc.applied_once:
                return
            calc.applied_once.add(self.stack_key)
        calc.amount = max(0, calc.amount - self.amount)


def takes_less_passive(amount, protects="carrier", attacker_pred=None,
                       stack_key=None) -> Passive:
    """"Takes N less damage from attacks" (Lesson in Zeal shape); a stack_key
    dedups multiple copies within one damage calc."""
    return TakesLessPassive(amount, protects, attacker_pred, stack_key)


class TeamDamageBoostPassive(Passive):
    """Matching friendly attackers' attacks do +N (before W/R)."""

    def __init__(self, amount, attacker_pred=None, target_pred=None,
                 once_key=None, to_active_only=True):
        self.amount = amount
        self.attacker_pred = attacker_pred
        self.target_pred = target_pred
        self.once_key = once_key
        self.to_active_only = to_active_only

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if attacker.owning_player_id != carrier.owning_player_id:
            return
        if self.attacker_pred is not None and not self.attacker_pred(attacker):
            return
        if self.to_active_only and not calc.to_active:
            return
        if self.target_pred is not None and not self.target_pred(calc.target):
            return
        if self.once_key:
            if self.once_key in calc.applied_once:
                return
            calc.applied_once.add(self.once_key)
        calc.amount += self.amount


def team_damage_boost_passive(amount, attacker_pred=None, target_pred=None,
                              once_key=None, to_active_only=True) -> Passive:
    """"Your <matching> Pokemon's attacks do +N to the opponent's Active"
    (pass to_active_only=False for boosts with no Active clause)."""
    return TeamDamageBoostPassive(amount, attacker_pred, target_pred,
                                  once_key, to_active_only)


class PredicatePreventionPassive(Passive):
    """prevents_damage generic: pred(calc, carrier) decides the block."""

    def __init__(self, pred, attacks_only=True):
        self.pred = pred
        self.attacks_only = attacks_only

    def prevents_damage(self, calc, carrier):
        if self.attacks_only and not (calc.is_attack and calc.is_opposing):
            return False
        return bool(self.pred(calc, carrier))


def prevent_damage_when(pred, attacks_only=True) -> Passive:
    """Full damage prevention whenever pred(calc, carrier) holds; by default
    only versus opposing attacks (Wave Veil discipline)."""
    return PredicatePreventionPassive(pred, attacks_only)


class TypedDamageBoostPassive(Passive):
    """The holder's attacks do +N to opposing targets matching a type/pred."""

    def __init__(self, type_or_pred, amount, to_active_only=True):
        if callable(type_or_pred):
            self.target_match = type_or_pred
        else:
            type_value = getattr(type_or_pred, "value", type_or_pred)
            self.target_match = lambda target: type_value in (
                target.get_attribute(AttrID.POKEMON_TYPES) or []
            )
        self.amount = amount
        self.to_active_only = to_active_only

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.attacker:
            return
        if self.to_active_only and not calc.to_active:
            return
        if self.target_match(calc.target):
            calc.amount += self.amount


def typed_damage_boost_tool(type_or_pred, amount, to_active_only=True) -> Passive:
    """Gloves shape: the holder's attacks do +N versus opposing Active
    targets of the given PokemonTypes (or matching target_pred(target))."""
    return TypedDamageBoostPassive(type_or_pred, amount, to_active_only)


class HpBonusPassive(Passive):
    """The holder gets +N max HP (Cape of Toughness shape)."""

    def __init__(self, amount, holder_pred=None):
        self.amount = amount
        self.holder_pred = holder_pred

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        if self.holder_pred is not None and not self.holder_pred(pokemon):
            return 0
        return self.amount


def hp_bonus_tool(amount, holder_pred=None) -> Passive:
    """+N max HP on the holder; holder_pred gates eligibility (e.g. Basic
    only for Cape of Toughness). Engine keeps damage-taken constant."""
    return HpBonusPassive(amount, holder_pred)


class RetreatDiscountPassive(Passive):
    """Matching Pokemon's retreat cost is N less."""

    def __init__(self, amount, target_pred=None):
        self.amount = amount
        self.protects = _protects_pred(target_pred)

    def modify_retreat_cost(self, cost, pokemon, carrier):
        if not self.protects(pokemon, carrier):
            return cost
        return max(0, cost - self.amount)


def retreat_discount(amount, target_pred=None) -> Passive:
    """Retreat cost -N (Air Balloon shape); target_pred defaults to the
    carrier's holder, or 'team' / callable(pokemon, carrier)."""
    return RetreatDiscountPassive(amount, target_pred)


class RetreatFreeWhenPassive(Passive):
    """Retreat cost becomes 0 whenever pred(pokemon, carrier) holds."""

    def __init__(self, pred):
        self.pred = pred

    def modify_retreat_cost(self, cost, pokemon, carrier):
        return 0 if self.pred(pokemon, carrier) else cost


def retreat_free_when(pred) -> Passive:
    """Free retreat while pred(pokemon, carrier) holds."""
    return RetreatFreeWhenPassive(pred)


class OpponentAttackTaxPassive(Passive):
    """Opposing Pokemon's attacks cost [C] N more."""

    def __init__(self, extra, target_pred=None):
        self.extra = extra
        self.target_pred = target_pred

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return cost
        if self.target_pred is not None and not self.target_pred(pokemon):
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + self.extra
        return cost


def opponent_attack_tax(extra_cost_count, target_pred=None) -> Passive:
    """Opposing (vs the carrier's owner) Pokemon's attacks cost [C] N more;
    target_pred(pokemon) refines which opposing Pokemon are taxed."""
    return OpponentAttackTaxPassive(extra_cost_count, target_pred)


class AttackDiscountPassive(Passive):
    """Attacks cost [C] N less (Colorless removed first, Excited Heart shape)."""

    def __init__(self, count, self_only=True, pred=None):
        self.count = count
        self.self_only = self_only
        self.pred = pred

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if self.self_only:
            if carrier_pokemon(carrier) is not pokemon:
                return cost
        elif pokemon.owning_player_id != carrier.owning_player_id:
            return cost
        if self.pred is not None and not self.pred(pokemon):
            return cost
        if "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - self.count
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


def attack_discount_passive(count, self_only=True, pred=None) -> Passive:
    """Attacks cost [C] N less; self_only=False widens to the carrier
    owner's whole team, pred(pokemon) refines further."""
    return AttackDiscountPassive(count, self_only, pred)


class NoWeaknessPassive(Passive):
    """Protected Pokemon have no Weakness."""

    def __init__(self, protects="carrier"):
        self.protects = _protects_pred(protects)

    def modify_weakness(self, calc, carrier):
        if self.protects(calc.target, carrier):
            calc.weakness_applies = False


def no_weakness_passive(protects="carrier") -> Passive:
    """"... has no Weakness" (Mysterious Nest shape via a protects pred)."""
    return NoWeaknessPassive(protects)


class WeaknessMultiplierPassive(Passive):
    """Weakness applies xN instead of x2 (Supereffective Glasses shape)."""

    def __init__(self, mult, when=None):
        self.mult = mult
        self.when = when

    def modify_weakness(self, calc, carrier):
        if self.when is not None:
            if not self.when(calc, carrier):
                return
        elif carrier_pokemon(carrier) is not calc.attacker:
            return
        calc.weakness_multiplier = self.mult


def weakness_multiplier_passive(mult, when=None) -> Passive:
    """Rewrites the Weakness multiplier; defaults to the holder attacking,
    or gate with when(calc, carrier)."""
    return WeaknessMultiplierPassive(mult, when)


class NoResistancePassive(Passive):
    """Attacks from the carrier's side aren't affected by Resistance."""

    def __init__(self, when=None):
        self.when = when

    def modify_resistance(self, calc, carrier):
        if self.when is not None:
            if not self.when(calc, carrier):
                return
        elif not (calc.attacker is not None
                  and calc.attacker.owning_player_id == carrier.owning_player_id):
            return
        calc.resistance_applies = False


def no_resistance_passive(when=None) -> Passive:
    """"... isn't affected by Resistance" (Pinsir team shape); defaults to
    the carrier owner's attackers, or gate with when(calc, carrier)."""
    return NoResistancePassive(when)


class ConditionImmunityPassive(Passive):
    """Protected Pokemon can't be affected by the given Special Conditions."""

    def __init__(self, conditions=None, protects="carrier"):
        if conditions is None:
            self.conditions = None  # None = immune to ALL conditions
        elif isinstance(conditions, (list, tuple, set, frozenset)):
            self.conditions = set(conditions)
        else:
            self.conditions = {conditions}
        self.protects = _protects_pred(protects)

    def blocks_special_conditions(self, target, condition, carrier):
        if self.conditions is not None and condition not in self.conditions:
            return False
        return bool(self.protects(target, carrier))


def condition_immunity_passive(conditions=None, protects="carrier") -> Passive:
    """Condition immunity (Galarian Rapidash shape); conditions=None means
    ALL, else a SpecialConditions member or iterable of them."""
    return ConditionImmunityPassive(conditions, protects)


class NoRetreatPassive(Passive):
    """Matching Pokemon can't retreat."""

    def __init__(self, target_pred):
        self.target_pred = target_pred

    def blocks_retreat(self, pokemon, carrier):
        return bool(self.target_pred(pokemon, carrier))


def no_retreat_passive(target_pred) -> Passive:
    """Blocks retreat while target_pred(pokemon, carrier) holds (Flygon:
    `lambda p, c: opposing_active(p, c) and is_in_active_spot(c)`)."""
    return NoRetreatPassive(target_pred)


class AbilityLockPassive(Passive):
    """Matching Pokemon have no Abilities."""

    def __init__(self, target_pred):
        self.target_pred = target_pred

    def blocks_abilities(self, pokemon, carrier):
        return bool(self.target_pred(pokemon, carrier))


def ability_lock_passive(target_pred) -> Passive:
    """Turns off Abilities while target_pred(pokemon, carrier) holds (Path
    to the Peak: `lambda p, c: has_rule_box(p.archetype_id)`)."""
    return AbilityLockPassive(target_pred)


class HealingBlockPassive(Passive):
    """Matching Pokemon can't have damage healed."""

    def __init__(self, target_pred):
        self.target_pred = target_pred

    def prevents_healing(self, target, carrier):
        return bool(self.target_pred(target, carrier))


def healing_block_passive(target_pred) -> Passive:
    """Blocks healing while target_pred(target, carrier) holds (Mimikyu)."""
    return HealingBlockPassive(target_pred)


class AttackEffectShieldPassive(Passive):
    """Protected Pokemon are shielded from opposing attack EFFECTS."""

    def __init__(self, protects="carrier"):
        self.protects = _protects_pred(protects)

    def blocks_attack_effects(self, target, carrier):
        return bool(self.protects(target, carrier))


def attack_effect_shield_passive(protects="carrier") -> Passive:
    """Unfazed Fat generalized: shields from attack effects, not damage
    (the engine already scopes the check to opposing attacks)."""
    return AttackEffectShieldPassive(protects)


# ======================================================================
# GROUP B -- temporary-shield effect factories (expiring temp passives)
# ======================================================================
# Factory forms are COMPLETE attack effects: printed damage first (a no-op
# at damage 0), then the rider. The apply_* helpers are riders only.

class TempShieldPassive(Passive):
    """reduce-N / prevent / effects_too shield on its carrier vs opposing attacks."""

    def __init__(self, reduce=None, prevent=False, effects_too=False):
        self.reduce = reduce
        self.prevent = prevent
        self.effects_too = effects_too

    def modify_damage_taken(self, calc, carrier):
        if (self.reduce and calc.is_attack and calc.is_opposing
                and carrier_pokemon(carrier) is calc.target):
            calc.amount = max(0, calc.amount - self.reduce)

    def prevents_damage(self, calc, carrier):
        return bool(self.prevent and calc.is_attack and calc.is_opposing
                    and carrier_pokemon(carrier) is calc.target)

    def blocks_attack_effects(self, target, carrier):
        return bool(self.effects_too and carrier_pokemon(carrier) is target)


async def apply_protection(ctx, target=None, reduce=None, prevent=False,
                           effects_too=False, through_own_next_turn=False):
    """Rider: shield `target` (default the attack's user) through the
    opponent's next turn; the shield ends early if the carrier leaves the
    Active spot / play (clear_pokemon_effects)."""
    target = target if target is not None else ctx.attacker
    if target is None:
        return False
    shield = TempShieldPassive(reduce=reduce, prevent=prevent,
                               effects_too=effects_too)
    if through_own_next_turn:
        ctx.add_passive_through_own_next_turn(target, shield)
    else:
        ctx.add_passive_through_opponents_turn(target, shield)
    return True


def protect_next_turn(reduce=None, prevent=False, effects_too=False,
                      self_target=True):
    """Complete attack effect: printed damage, then shield the user (or the
    Defending Pokemon when self_target=False) during the opponent's next
    turn -- reduce=N takes-less, prevent=True full prevention, effects_too
    adds the attack-effect shield ("all effects ... including damage")."""
    async def effect(ctx):
        await ctx.deal_damage()
        target = ctx.attacker if self_target else ctx.defender
        await apply_protection(ctx, target=target, reduce=reduce,
                               prevent=prevent, effects_too=effects_too)
    return effect


def flip_protection(prevent=True, reduce=None, effects_too=False, title=None):
    """Complete attack effect: printed damage, then flip a coin -- heads
    shields the user during the opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        flip_title = title if title is not None else (
            ctx.ability.title if ctx.ability else "")
        results = await ctx.flip_coins(1, flip_title)
        if results and results[0]:
            await apply_protection(ctx, reduce=reduce, prevent=prevent,
                                   effects_too=effects_too)
    return effect


class AttackDebuffPassive(Passive):
    """The carrier's attacks do N less damage (dealt-side, before W/R)."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing
                and carrier_pokemon(carrier) is calc.attacker):
            calc.amount -= self.amount


async def apply_defender_debuff(ctx, amount, target=None):
    """Rider: `target`'s (default the Defending Pokemon) attacks do N less
    during the opponent's next turn; fizzles vs attack-effect shields."""
    target = target if target is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    ctx.add_passive_through_opponents_turn(target, AttackDebuffPassive(amount))
    return True


def debuff_defender_attacks(amount):
    """Complete attack effect: printed damage, then "during your opponent's
    next turn, the Defending Pokemon's attacks do N less damage"."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_defender_debuff(ctx, amount)
    return effect


async def apply_own_next_turn_boost(ctx, amount, attack_title=None,
                                    opposing_active_only=True):
    """Rider: during your next turn this Pokemon's attacks (optionally only
    `attack_title`) do +N; a turn guard keeps it off the current attack."""
    state = ctx.session.turn_state
    start = state.turn_number
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        amount, ctx.player_id,
        opposing_active_only=opposing_active_only,
        expires_after_turn=start + 2,
        source_entity_id=ctx.attacker.entity_id,
        attack_title=attack_title,
        source_predicate=lambda _e: state.turn_number > start,
    ))


def boost_own_next_turn(amount, attack_title=None):
    """Complete attack effect: printed damage, then "during your next turn,
    this Pokemon's attacks do +N" (Fullmetal Impact rider when titled)."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_own_next_turn_boost(ctx, amount, attack_title)
    return effect


class SelfAttackCostRaisePassive(Passive):
    """The carrier's attacks cost [C] N more."""

    def __init__(self, extra):
        self.extra = extra

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + self.extra
        return cost


async def apply_defender_attack_cost_raise(ctx, extra=1, target=None):
    """Rider: `target`'s (default the Defending Pokemon) attacks cost [C]
    N more during the opponent's next turn; fizzles vs effect shields."""
    target = target if target is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    ctx.add_passive_through_opponents_turn(
        target, SelfAttackCostRaisePassive(extra))
    return True


def raise_defender_attack_cost_next_turn(extra=1):
    """Complete attack effect: printed damage, then the Defending Pokemon's
    attacks cost [C] N more during your opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_defender_attack_cost_raise(ctx, extra)
    return effect


class SelfRetreatCostRaisePassive(Passive):
    """The carrier's retreat cost is [C] N more."""

    def __init__(self, extra):
        self.extra = extra

    def modify_retreat_cost(self, cost, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        return cost + self.extra


async def apply_defender_retreat_cost_raise(ctx, extra=1, target=None):
    """Rider: `target`'s (default the Defending Pokemon) retreat cost is N
    more during the opponent's next turn; fizzles vs effect shields."""
    target = target if target is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    ctx.add_passive_through_opponents_turn(
        target, SelfRetreatCostRaisePassive(extra))
    return True


def raise_defender_retreat_cost_next_turn(extra=1):
    """Complete attack effect: printed damage, then the Defending Pokemon's
    retreat cost is [C] N more during your opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_defender_retreat_cost_raise(ctx, extra)
    return effect
