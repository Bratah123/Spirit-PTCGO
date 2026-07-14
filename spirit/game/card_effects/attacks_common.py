"""Reusable attack-effect factories: flips, scaling, snipes, conditions,
energy-discard costs, locks, counter placement.

Every factory returns an `async def effect(ctx)` for Attack(effect=...);
damage/base None = the attack's printed damage; `also=` chains a follow-up
coroutine run after the factory's own work.
"""

import random
from typing import Optional

from spirit.game.attributes import (
    AbilityTypes,
    AttrID,
    CLIENT_SPECIAL_CONDITION_NAMES,
    TrainerType,
)
from spirit.game.data_utils import Attack, def_for, has_rule_box, is_pokemon_v, subtypes_for
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_special_energy
from spirit.game.session.legal_actions import energy_provided_count

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)
_ENERGY_SCOPES = ("self", "attacker", "defender", "opponent_active", "my_active",
                  "mine", "opponent", "both")


# ----------------------------------------------------------------------
# Shared internals
# ----------------------------------------------------------------------

def _printed(ctx) -> int:
    return getattr(ctx.ability, "damage", 0) or 0


def _title(ctx) -> str:
    return ctx.ability.title if ctx.ability else ""


def _resolve_count(ctx, count_or_fn) -> int:
    return count_or_fn(ctx) if callable(count_or_fn) else int(count_or_fn)


def _in_play(ctx, side: str) -> list:
    if side == "both":
        return ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    if side in ("opponent", "theirs"):
        return ctx.opponent_pokemon_in_play()
    return ctx.my_pokemon_in_play()


def _bench_of(ctx, side: str) -> list:
    if side == "both":
        return ctx.my_bench() + ctx.opponent_bench()
    return ctx.opponent_bench() if side in ("opponent", "theirs") else ctx.my_bench()


def _side_pid(ctx, side: str) -> str:
    return ctx.opponent_id if side in ("opponent", "theirs") else ctx.player_id


def _resolve_target(ctx, target_fn):
    if callable(target_fn):
        return target_fn(ctx)
    return ctx.attacker if target_fn == "self" else ctx.defender


async def _finish(ctx, self_damage: int, also):
    if self_damage:
        await ctx.deal_damage(self_damage, target=ctx.attacker, apply_modifiers=False)
    if also is not None:
        await also(ctx)


def _attack_ability_entries(pokemon) -> list:
    return [e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
            if isinstance(e, dict) and e.get("abilityType") == "Attack"
            and e.get("abilityID")]


def _provided_of_type(energy, type_value: int) -> int:
    info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
    best = max((option.count(type_value)
                for option in info.get("options", [])), default=0)
    return best or 1


# ----------------------------------------------------------------------
# Count helpers (each returns count_fn(ctx) -> int, or a card predicate)
# ----------------------------------------------------------------------

def count_energy(scope: str = "self", energy_type=None, cards: bool = False):
    """Attached Energy on a scope; counts PROVIDED amounts (Double Turbo = 2)
    unless cards=True. energy_type filters/counts one type (Aurora matches)."""
    if scope not in _ENERGY_SCOPES:
        raise ValueError(f"count_energy: unknown scope '{scope}'")
    type_value = getattr(energy_type, "value", energy_type)

    def count(ctx) -> int:
        if scope in ("self", "attacker"):
            pool = [ctx.attacker]
        elif scope in ("defender", "opponent_active"):
            pool = [ctx.opponent_active()]
        elif scope == "my_active":
            pool = [ctx.my_active()]
        else:
            pool = _in_play(ctx, scope)
        total = 0
        for pokemon in pool:
            if pokemon is None:
                continue
            for energy in ctx.attached_energies(pokemon):
                if type_value is None:
                    total += 1 if cards else energy_provided_count(energy)
                elif energy_provides_type(energy, type_value):
                    total += 1 if cards else _provided_of_type(energy, type_value)
        return total
    return count


def count_bench(side: str = "mine", pred=None):
    """Benched Pokemon on a side ('mine'|'opponent'|'both'), optionally filtered."""
    def count(ctx) -> int:
        return sum(1 for p in _bench_of(ctx, side) if pred is None or pred(p))
    return count


def count_discard(side: str = "mine", pred=None):
    """Cards in a discard pile ('mine'|'opponent'|'both'), optionally filtered."""
    def count(ctx) -> int:
        piles = [ctx.player_id, ctx.opponent_id] if side == "both" \
            else [_side_pid(ctx, side)]
        return sum(1 for pid in piles for c in ctx.discard_pile(pid)
                   if pred is None or pred(c))
    return count


def count_prizes_taken(side: str = "mine"):
    def count(ctx) -> int:
        return ctx.prizes_taken(_side_pid(ctx, side))
    return count


def count_prizes_remaining(side: str = "mine"):
    def count(ctx) -> int:
        area = ctx.board.find_player_area(_side_pid(ctx, side), "prizePile")
        return len(area.children) if area else 0
    return count


def damage_counters_on(target_fn="self"):
    """Damage counters on a Pokemon ('self'|'defender'|callable(ctx)->pokemon)."""
    def count(ctx) -> int:
        target = _resolve_target(ctx, target_fn)
        if target is None:
            return 0
        return max(0, (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10)
    return count


def count_hand(side: str = "mine"):
    def count(ctx) -> int:
        return ctx.hand_size(_side_pid(ctx, side))
    return count


def count_in_play(side: str = "mine", pred=None):
    """In-play Pokemon (Active + Bench) on a side, optionally filtered."""
    def count(ctx) -> int:
        return sum(1 for p in _in_play(ctx, side) if pred is None or pred(p))
    return count


def has_attack_titled(title: str):
    """Card predicate: the card's definition carries an attack named `title`
    (Mad Party / Let's All Rollout counting)."""
    def pred(card) -> bool:
        definition = def_for(getattr(card, "archetype_id", None) or "")
        for ability in getattr(definition, "abilities", None) or []:
            if getattr(ability, "title", None) != title:
                continue
            if isinstance(ability, Attack) or getattr(ability, "ability_type", None) \
                    in (AbilityTypes.ATTACK, AbilityTypes.NON_DAMAGING_ATTACK):
                return True
        return False
    return pred


# ----------------------------------------------------------------------
# Flip family
# ----------------------------------------------------------------------

def flip_damage(coins: int = 1, per_heads: int = 0, base: Optional[int] = None,
                bonus: int = 0, bonus_per_heads: int = 0,
                until_tails: bool = False, coins_from=None,
                require_all: bool = False, tails_self_damage: int = 0,
                self_damage: int = 0, also=None):
    """Coin-flip damage: heads*per_heads (base defaults 0), or printed base +
    heads*bonus_per_heads, or base+bonus gated on ALL heads (require_all;
    without a bonus the whole base needs all heads). coins_from=count_fn
    flips one coin per counted thing; until_tails uses one coin screen.
    tails_self_damage hits the attacker once when any coin lands tails."""
    async def effect(ctx):
        if until_tails:
            heads = await ctx.flip_until_tails(_title(ctx))
            total, tails = heads + 1, 1
        else:
            total = _resolve_count(ctx, coins_from) if coins_from is not None else coins
            results = await ctx.flip_coins(total, _title(ctx)) if total > 0 else []
            heads = sum(1 for r in results if r)
            tails = total - heads
        base_val = (base or 0) if per_heads \
            else (base if base is not None else _printed(ctx))
        if require_all:
            success = total > 0 and tails == 0
            amount = base_val + bonus if success else (base_val if bonus else 0)
        else:
            amount = base_val + heads * (per_heads + bonus_per_heads) \
                + (bonus if heads else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if tails_self_damage and tails > 0:
            await ctx.deal_damage(tails_self_damage, target=ctx.attacker,
                                  apply_modifiers=False)
        await _finish(ctx, self_damage, also)
    return effect


def flip_or_nothing(coins: int = 1, then=None):
    """"Flip a coin. If tails, this attack does nothing." — any tails is an
    early return; all heads runs `then(ctx)` (default: printed damage)."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, _title(ctx))
        if not results or not all(results):
            return
        if then is None:
            await ctx.deal_damage()
        else:
            await then(ctx)
    return effect


def flip_bonus(bonus: int, coins: int = 1):
    """Printed damage, +bonus when every flipped coin is heads."""
    return flip_damage(coins=coins, bonus=bonus, require_all=True)


# ----------------------------------------------------------------------
# Scaling damage
# ----------------------------------------------------------------------

def damage_per(count_fn, per: int, base: int = 0, cap: Optional[int] = None,
               self_damage: int = 0, also=None):
    """base + per * count_fn(ctx) damage to the opponent's Active (cap optional)."""
    async def effect(ctx):
        amount = base + per * max(0, count_fn(ctx))
        if cap is not None:
            amount = min(amount, cap)
        if amount > 0:
            await ctx.deal_damage(amount)
        await _finish(ctx, self_damage, also)
    return effect


# ----------------------------------------------------------------------
# Snipe / spread
# ----------------------------------------------------------------------

def snipe_attack(amount: int, pool="bench", count: int = 1,
                 side: str = "opponent", also_base: bool = False,
                 apply_modifiers: Optional[bool] = None, optional: bool = False,
                 self_damage: int = 0, also=None, prompt: Optional[str] = None):
    """Deal `amount` to `count` chosen Pokemon (pool 'bench'|'any'|predicate).
    apply_modifiers None = engine auto (W/R only when the target is the
    opponent's Active); also_base deals printed damage to the Active first."""
    async def effect(ctx):
        if also_base:
            await ctx.deal_damage()
        if pool == "any":
            candidates = _in_play(ctx, side)
        elif pool == "bench":
            candidates = _bench_of(ctx, side)
        else:
            candidates = [p for p in _in_play(ctx, side) if pool(p)]
        if candidates:
            text = prompt or (f"Choose a Pokémon to take {amount} damage"
                              if count == 1 else
                              f"Choose {count} Pokémon to take {amount} damage")
            picks = await ctx.choose_cards(
                candidates, count, minimum=0 if optional else None, prompt=text)
            for target in picks:
                await ctx.deal_damage(amount, target=target,
                                      apply_modifiers=apply_modifiers)
        await _finish(ctx, self_damage, also)
    return effect


def spread_damage(amount: int, side: str = "opponent",
                  include_active: bool = False, own_bench: bool = False,
                  also_base: bool = False, also=None):
    """Deal `amount` to every Benched Pokemon on `side` ('opponent'|'mine'|
    'both'); include_active adds that side's Active(s), own_bench adds your
    bench to an opponent-side spread. Bench damage takes no W/R (engine auto)."""
    async def effect(ctx):
        if also_base:
            await ctx.deal_damage()
        targets = {p.entity_id: p for p in _bench_of(ctx, side)}
        if own_bench and side != "mine":
            targets.update((p.entity_id, p) for p in ctx.my_bench())
        if include_active:
            actives = []
            if side in ("opponent", "theirs", "both"):
                actives.append(ctx.opponent_active())
            if side in ("mine", "both"):
                actives.append(ctx.my_active())
            targets.update((p.entity_id, p) for p in actives if p is not None)
        for target in targets.values():
            await ctx.deal_damage(amount, target=target, apply_modifiers=None)
        if also is not None:
            await also(ctx)
    return effect


def damage_all_opponents(amount: int, also=None):
    """Deal `amount` to each of the opponent's Pokemon (Active included)."""
    return spread_damage(amount, side="opponent", include_active=True, also=also)


# ----------------------------------------------------------------------
# Conditional bonus + predicates
# ----------------------------------------------------------------------

def bonus_if(cond_fn, bonus: int, base: Optional[int] = None,
             else_nothing: bool = False, self_damage: int = 0, also=None):
    """Printed (or base) damage, +bonus when cond_fn(ctx) holds; else_nothing
    makes the whole attack deal 0 when the condition fails."""
    async def effect(ctx):
        base_val = base if base is not None else _printed(ctx)
        met = bool(cond_fn(ctx))
        amount = base_val + bonus if met else (0 if else_nothing else base_val)
        if amount > 0:
            await ctx.deal_damage(amount)
        await _finish(ctx, self_damage, also)
    return effect


def active_is(pred):
    """cond_fn: the opponent's Active exists and matches `pred(pokemon)`."""
    def cond(ctx) -> bool:
        active = ctx.opponent_active()
        return active is not None and bool(pred(active))
    return cond


def defender_is_v(ctx) -> bool:
    d = ctx.defender
    return d is not None and is_pokemon_v(d.archetype_id)


def defender_is_gx(ctx) -> bool:
    d = ctx.defender
    return d is not None and "GX" in subtypes_for(d.archetype_id)


def defender_is_vmax(ctx) -> bool:
    d = ctx.defender
    return d is not None and "VMAX" in subtypes_for(d.archetype_id)


def defender_has_rule_box(ctx) -> bool:
    d = ctx.defender
    return d is not None and has_rule_box(d.archetype_id)


def defender_has_condition(condition):
    """cond_fn: the opponent's Active already has the Special Condition."""
    name = CLIENT_SPECIAL_CONDITION_NAMES[condition]

    def cond(ctx) -> bool:
        d = ctx.defender
        return d is not None and \
            name in (d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    return cond


def named_in_play(*names, side: str = "mine", require_all: bool = False):
    """cond_fn: Pokemon with these names (EVOLUTION_LOGIC_NAME) are in play."""
    def cond(ctx) -> bool:
        present = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                   for p in _in_play(ctx, side)}
        wanted = set(names)
        return wanted <= present if require_all else bool(wanted & present)
    return cond


def has_tool(pokemon) -> bool:
    """Card predicate: a Tool is attached (compose: active_is(has_tool))."""
    return any(c.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES
               for c in pokemon.children)


def has_damage(target_fn="defender"):
    """cond_fn: the target ('self'|'defender'|callable) has damage on it."""
    def cond(ctx) -> bool:
        target = _resolve_target(ctx, target_fn)
        return target is not None and \
            target.get_attribute(AttrID.HP, 0) < ctx.max_hp(target)
    return cond


def opponent_prizes_taken_at_least(n: int):
    def cond(ctx) -> bool:
        return ctx.prizes_taken(ctx.opponent_id) >= n
    return cond


# ----------------------------------------------------------------------
# Energy-discard costs
# ----------------------------------------------------------------------

def self_energy_discard_attack(count: Optional[int] = None,
                               all_energy: bool = False, energy_type=None,
                               before_damage: bool = False,
                               then_damage: Optional[int] = None, also=None):
    """Discard own attached Energy (count, or all_energy=True) around the
    printed (or then_damage) damage; before_damage follows the printed order."""
    if count is None and not all_energy:
        raise ValueError("self_energy_discard_attack: pass count= or all_energy=True")
    type_value = getattr(energy_type, "value", energy_type)
    pred = (lambda c: energy_provides_type(c, type_value)) \
        if type_value is not None else None

    async def _discard(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, 99 if all_energy else count, predicate=pred,
            prompt="Choose Energy to discard from this Pokémon")

    async def effect(ctx):
        if before_damage:
            await _discard(ctx)
            await ctx.deal_damage(then_damage)
        else:
            await ctx.deal_damage(then_damage)
            await _discard(ctx)
        if also is not None:
            await also(ctx)
    return effect


def discard_opponent_energy_attack(count: int = 1, special_only: bool = False,
                                   after_damage: bool = True,
                                   damage: Optional[int] = None, also=None):
    """Printed (or damage) damage + discard Energy from the opponent's Active;
    the discard no-ops when the target is shielded from attack effects."""
    pred = is_special_energy if special_only else None

    async def _discard(ctx):
        target = ctx.opponent_active()
        if target is None or ctx.effects_blocked(target):
            return
        await ctx.discard_energy_from(
            target, count, predicate=pred,
            prompt="Choose Energy to discard from the Defending Pokémon")

    async def effect(ctx):
        if after_damage:
            await ctx.deal_damage(damage)
            await _discard(ctx)
        else:
            await _discard(ctx)
            await ctx.deal_damage(damage)
        if also is not None:
            await also(ctx)
    return effect


# ----------------------------------------------------------------------
# Special-condition attacks (supersedes card_effects.pokemon.condition_attack)
# ----------------------------------------------------------------------

def condition_attack(*conditions, flip: bool = False, coins: int = 1,
                     min_heads: int = 1, tails_conditions=(),
                     always_conditions=(), heads_bonus_damage: int = 0,
                     self_conditions=(), both_actives: bool = False,
                     no_retreat: bool = False, counters: int = 1,
                     checkup_coins: int = 1, damage: Optional[int] = None,
                     also=None):
    """Printed damage + Special Conditions on the Defending Pokemon; flip=True
    gates `conditions`/self_conditions/no_retreat/heads_bonus_damage on
    min_heads heads (tails_conditions on failure, always_conditions always)."""
    async def effect(ctx):
        success = True
        if flip:
            results = await ctx.flip_coins(coins, _title(ctx))
            success = sum(1 for r in results if r) >= min_heads
        base_val = damage if damage is not None else _printed(ctx)
        amount = base_val + (heads_bonus_damage if success else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        applied = list(always_conditions) + \
            (list(conditions) if success else list(tails_conditions))
        for condition in applied:
            await ctx.apply_special_condition(
                ctx.defender, condition,
                checkup_coins=checkup_coins, poison_counters=counters)
            if both_actives:
                await ctx.apply_special_condition(
                    ctx.attacker, condition,
                    checkup_coins=checkup_coins, poison_counters=counters)
        if success:
            for condition in self_conditions:
                await ctx.apply_special_condition(
                    ctx.attacker, condition,
                    checkup_coins=checkup_coins, poison_counters=counters)
            if no_retreat:
                defender = ctx.defender
                if defender is not None and not ctx.effects_blocked(defender):
                    ctx.lock_retreat(defender)
        if also is not None:
            await also(ctx)
    return effect


def condition_bonus_attack(bonus: int, *required_conditions,
                           base: Optional[int] = None, also=None):
    """"If the Defending Pokemon is already <condition>, this attack does
    `bonus` more damage." Checks before the hit; applies nothing itself."""
    names = [CLIENT_SPECIAL_CONDITION_NAMES[c] for c in required_conditions]

    async def effect(ctx):
        base_val = base if base is not None else _printed(ctx)
        defender = ctx.defender
        current = (defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) \
            if defender is not None else []
        met = bool(names) and all(n in current for n in names)
        amount = base_val + (bonus if met else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if also is not None:
            await also(ctx)
    return effect


# ----------------------------------------------------------------------
# Recoil / mill
# ----------------------------------------------------------------------

def recoil_attack(self_damage: int, damage: Optional[int] = None, also=None):
    """Printed (or damage) damage; the attacker then damages itself (no W/R)."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        await ctx.deal_damage(self_damage, target=ctx.attacker,
                              apply_modifiers=False)
        if also is not None:
            await also(ctx)
    return effect


def mill_attack(count: int, opponent: bool = True,
                then_damage: Optional[int] = None, also=None):
    """Printed (or then_damage) damage, then discard the top `count` cards of
    a deck (opponent's by default)."""
    async def effect(ctx):
        await ctx.deal_damage(then_damage)
        pid = ctx.opponent_id if opponent else ctx.player_id
        await ctx.discard_cards(ctx.deck_top(count, player_id=pid))
        if also is not None:
            await also(ctx)
    return effect


def mill_scaled_damage(mill_count: int, per: int, pred=None, base: int = 0,
                       also=None):
    """Discard the top `mill_count` of YOUR deck; damage = base + per for each
    discarded card matching `pred`."""
    async def effect(ctx):
        cards = ctx.deck_top(mill_count)
        await ctx.discard_cards(cards)
        matched = sum(1 for c in cards if pred is None or pred(c))
        amount = base + per * matched
        if amount > 0:
            await ctx.deal_damage(amount)
        if also is not None:
            await also(ctx)
    return effect


# ----------------------------------------------------------------------
# Attack-lock helpers (runtime helpers, not factories)
# ----------------------------------------------------------------------

def lock_all_attacks(ctx, pokemon):
    """Locks every printed attack on own `pokemon` through its user's next
    turn (Cross Fusion Strike's blanket self-lock)."""
    for entry in _attack_ability_entries(pokemon):
        ctx.session.turn_state.lock_attack(pokemon.entity_id, entry["abilityID"])


def lock_defender_attacks(ctx, defender=None) -> bool:
    """"The Defending Pokemon can't attack during your opponent's next turn";
    no-ops (False) on an effect-shielded target."""
    target = defender if defender is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    state = ctx.session.turn_state
    for entry in _attack_ability_entries(target):
        state.attack_locks[(target.entity_id, entry["abilityID"])] = \
            state.turn_number + 1
    return True


# ----------------------------------------------------------------------
# Damage-counter placement
# ----------------------------------------------------------------------

def place_counters(count_or_fn, target: str = "opponent_active", also=None):
    """Put damage counters (raw, no W/R; effect-shield gated by the engine):
    target 'opponent_active'|'choose_any_opponent'|'each_opponent'|'self'|
    'choose_own'; count_or_fn is an int or count_fn(ctx)."""
    if target not in ("opponent_active", "choose_any_opponent", "each_opponent",
                      "self", "choose_own"):
        raise ValueError(f"place_counters: unknown target '{target}'")

    async def effect(ctx):
        count = _resolve_count(ctx, count_or_fn)
        if count > 0:
            if target == "opponent_active":
                if ctx.defender is not None:
                    await ctx.deal_damage(count * 10, target=ctx.defender,
                                          as_counters=True)
            elif target == "choose_any_opponent":
                await ctx.place_damage_counters(count, ctx.opponent_pokemon_in_play())
            elif target == "each_opponent":
                for pokemon in ctx.opponent_pokemon_in_play():
                    await ctx.deal_damage(count * 10, target=pokemon,
                                          as_counters=True)
            elif target == "self":
                await ctx.deal_damage(count * 10, target=ctx.attacker,
                                      as_counters=True)
            else:  # choose_own
                await ctx.place_damage_counters(count, ctx.my_pokemon_in_play())
        if also is not None:
            await also(ctx)
    return effect


# ----------------------------------------------------------------------
# Discard-for-bonus + misc
# ----------------------------------------------------------------------

def discard_for_bonus(source: str = "hand", predicate=None, max_count: int = 1,
                      per: int = 0, flat: int = 0, optional: bool = True,
                      base: Optional[int] = None, also=None,
                      prompt: Optional[str] = None):
    """Discard up to `max_count` cards (from 'hand' or 'self-energy'), then
    deal printed (or base) + per*discarded + (flat if any discarded)."""
    if source not in ("hand", "self-energy"):
        raise ValueError(f"discard_for_bonus: unknown source '{source}'")

    async def effect(ctx):
        if source == "hand":
            pool = [c for c in ctx.hand() if predicate is None or predicate(c)]
        else:
            pool = [c for c in ctx.attached_energies(ctx.attacker)
                    if predicate is None or predicate(c)]
        picked = await ctx.choose_cards(
            pool, max_count, minimum=0 if optional else None,
            prompt=prompt or "Choose cards to discard") if pool else []
        await ctx.discard_cards(picked)
        base_val = base if base is not None else _printed(ctx)
        amount = base_val + per * len(picked) + (flat if picked else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if also is not None:
            await also(ctx)
    return effect


def smokescreen_attack(damage: Optional[int] = None, also=None):
    """Printed (or damage) damage; "during your opponent's next turn, if the
    Defending Pokemon tries to attack, your opponent flips a coin. If tails,
    that attack doesn't happen" (Smokescreen / Sand Attack / Blinding Beam).
    The rider no-ops versus an attack-effect-shielded target."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            ctx.require_attack_flip(defender)
        if also is not None:
            await also(ctx)
    return effect


async def discard_random_from_hand(ctx, player_id: Optional[str] = None,
                                   count: int = 1) -> list:
    """Discards `count` random cards from a player's hand (reveals via the
    public-pile discard bracket); returns the discarded cards."""
    pid = player_id or ctx.player_id
    hand = ctx.hand(pid)
    if not hand or count <= 0:
        return []
    picks = random.sample(hand, min(count, len(hand)))
    await ctx.discard_cards(picks)
    return picks
