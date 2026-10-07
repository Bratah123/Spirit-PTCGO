"""Strategic brains for the queue AI.

A brain is a plain dict registered in DECK_STRATEGIES under the same name the
deck has in bot_decks.BOT_DECK_LISTS.  The GameSession consults it through
five hooks while an AIPlayer is acting -- each optional; a missing hook means
"keep the generic behavior":

    allow_action(description, name, ctx) -> bool
        hard gate per legal action (Path timing, Boss windows, ...).
    action_score(description, name, ctx) -> float
        ranking inside one action category (which trainer/evolve/energy
        to spend first).  Higher wins.
    attack_score(title, base_damage, ctx) -> float
        replaces the plain printed-damage attack ranking.
    target_score(description, name, ctx, target_id) -> float
        ranking among one action's valid targets (where the energy goes,
        which Pokemon Boss gusts, who Quick Shooting pings).
    search_score(card, ctx) -> float
        deck-search picks (Shady Dealings, Level Ball, ...).
    counter_plan(pool, count, ctx) -> {entity_id: counters}
        Max-Phantom style damage-counter distributions.

`ctx` is a StrategyContext: a duck-typed view over the GameSession (board,
hands, prizes) with helper queries.  Brains only import content/attributes
level modules so ai_player -> deck_strategies never cycles through the
session package.
"""

from typing import Dict, List, Optional

from spirit.game.attributes import AttrID, PokemonTypes, TrainerType
from spirit.game.content.definitions import def_for, has_rule_box, prize_value
from spirit.game.models.board import EnergyEntity


# ----------------------------------------------------------------------
# shared context helpers (duck-typed over GameSession)


class StrategyContext:
    """Board/hand queries a brain can rely on."""

    def __init__(self, session, player_id: str):
        self.session = session
        self.board = session.board_state
        self.me = player_id
        self.opp = session._opponent_id(player_id)

    # -- names ------------------------------------------------------------

    @staticmethod
    def name(entity) -> str:
        if entity is None:
            return ""
        definition = def_for(getattr(entity, "archetype_id", None))
        display = getattr(definition, "display_name", None)
        if display:
            return display
        raw = entity.get_attribute(AttrID.NAME)
        return raw.get("id", "") if isinstance(raw, dict) else (raw or "")

    # -- zones ------------------------------------------------------------

    def hand_cards(self, pid: Optional[str] = None):
        area = self.board.find_player_area(pid or self.me, "hand")
        return list(area.children) if area else []

    def hand_names(self, pid: Optional[str] = None) -> List[str]:
        return [self.name(c) for c in self.hand_cards(pid)]

    def hand_size(self, pid: Optional[str] = None) -> int:
        return len(self.hand_cards(pid))

    def in_play(self, pid: Optional[str] = None):
        return list(self.board.pokemon_in_play(pid or self.me))

    def in_play_names(self, pid: Optional[str] = None) -> List[str]:
        return [self.name(p) for p in self.in_play(pid)]

    def active(self, pid: Optional[str] = None):
        return self.board.active_pokemon(pid or self.me)

    def bench(self, pid: Optional[str] = None):
        area = self.board.find_player_area(pid or self.me, "bench")
        return [c for c in (list(area.children) if area else [])] 

    # -- damage / HP ------------------------------------------------------

    def max_hp(self, pokemon) -> int:
        from spirit.game.session.passives import effective_max_hp
        return effective_max_hp(self.board, pokemon)

    def hp_left(self, pokemon) -> int:
        return max(0, int(pokemon.get_attribute(AttrID.HP) or 0))

    def damage_on(self, pokemon) -> int:
        return self.max_hp(pokemon) - self.hp_left(pokemon)

    def prize_value(self, entity) -> int:
        try:
            return prize_value(getattr(entity, "archetype_id", None))
        except Exception:
            return 1

    # -- energy / readiness ----------------------------------------------

    def energy_attached(self, pokemon) -> int:
        return sum(1 for child in pokemon.children if isinstance(child, EnergyEntity))

    def min_attack_cost(self, pokemon) -> int:
        definition = def_for(getattr(pokemon, "archetype_id", None))
        best = None
        for ability in getattr(definition, "abilities", None) or []:
            cost = getattr(ability, "cost", None)
            if not isinstance(cost, dict):
                continue
            total = sum(v for v in cost.values() if isinstance(v, int))
            best = total if best is None else min(best, total)
        return best if best is not None else 0

    def active_ready(self, pid: Optional[str] = None) -> bool:
        """Active can fire its cheapest attack right now."""
        active = self.active(pid)
        if active is None:
            return False
        return self.energy_attached(active) >= self.min_attack_cost(active)

    def active_attack_damage(self) -> int:
        """Largest printed damage our Active could attack for right now."""
        from spirit.game.data_utils import ABILITIES_BY_ID
        active = self.active()
        if active is None:
            return 0
        best = 0
        for ability_id in getattr(active, "ability_ids", None) or []:
            ability = ABILITIES_BY_ID.get(ability_id)
            damage = getattr(ability, "damage", 0) or 0
            if not isinstance(damage, (int, float)):
                damage = 0
            if getattr(ability, "damage_operator", "") == "x":
                damage *= 3
            best = max(best, damage)
        if best:
            return int(best)
        # Fallback: read the archetype's attacks directly.
        definition = def_for(getattr(active, "archetype_id", None))
        for ability in getattr(definition, "abilities", None) or []:
            damage = getattr(ability, "damage", 0) or 0
            if not isinstance(damage, (int, float)):
                damage = 0
            if getattr(ability, "damage_operator", "") == "x":
                damage *= 3
            best = max(best, damage)
        return int(best)

    # -- opponent windows -------------------------------------------------

    def opponent_rule_box(self) -> bool:
        return any(has_rule_box(getattr(p, "archetype_id", None))
                   for p in self.in_play(self.opp))

    def opponent_tools(self) -> bool:
        for pokemon in self.in_play(self.opp):
            for child in pokemon.children:
                if child.get_attribute(AttrID.TRAINER_TYPE) \
                        == TrainerType.POKEMON_TOOL.value:
                    return True
        return False

    def opponent_stadium_is(self, card_name: str) -> bool:
        area = self.board.find_global_area("activeStadium")
        if not area:
            return False
        return any(self.name(child) == card_name for child in area.children)

    def ko_window(self, damage: Optional[int] = None) -> List:
        """Opponent Pokemon our Active (or the strategy's finisher) can KO."""
        if damage is None:
            damage = self.active_attack_damage()
        if damage <= 0:
            return []
        return [p for p in self.in_play(self.opp) if self.hp_left(p) <= damage]

    def prizes_lost(self) -> int:
        try:
            dealt = self.board.prizes_dealt.get(self.me, 6)
            return dealt - self.board.prizes_taken(self.me)
        except Exception:
            return 0

    def entered_active(self, pokemon) -> bool:
        """True when `pokemon` moved Bench -> Active during the current turn
        (Gale Thrust's 120-damage bonus window)."""
        if pokemon is None:
            return False
        try:
            state = self.session.turn_state
            return state.became_active_turn.get(pokemon.entity_id) == state.turn_number
        except Exception:
            return False

    def discard_names(self, pid: Optional[str] = None) -> List[str]:
        area = self.board.find_player_area(pid or self.me, "discard")
        return [self.name(c) for c in area.children] if area else []

    def deck_size(self, pid: Optional[str] = None) -> int:
        area = self.board.find_player_area(pid or self.me, "deck")
        return len(area.children) if area else 0

    def attack_locked(self, pokemon, title: str) -> bool:
        """True when `pokemon` is under a "can't use <title> next turn" lock
        (G-Max Hurricane / Brave Blade / Sky Hurricane self-locks)."""
        if pokemon is None:
            return False
        from spirit.game.data_utils import ABILITIES_BY_ID
        try:
            state = self.session.turn_state
        except Exception:
            return False
        ids = [e.get("abilityID") for e in
               (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
               if e.get("abilityID")]
        if not ids:
            definition = def_for(getattr(pokemon, "archetype_id", None))
            ids = [getattr(a, "ability_id", None)
                   for a in (getattr(definition, "abilities", None) or [])]
        for ability_id in ids:
            if not ability_id:
                continue
            definition = ABILITIES_BY_ID.get(ability_id)
            if definition is None:
                continue
            if getattr(definition, "title", "") == title:
                return bool(state.attack_locked(pokemon.entity_id, ability_id))
        return False


# ----------------------------------------------------------------------
# shared ranking helpers

_NEUTRAL = -50.0


def order_score(order, name: str) -> float:
    """Higher for names earlier in a priority list; neutral otherwise."""
    try:
        return 1000.0 - 10.0 * list(order).index(name)
    except ValueError:
        return _NEUTRAL


def _ko_need(ctx: StrategyContext, pokemon) -> int:
    """Damage counters required to KO `pokemon` right now."""
    left = ctx.hp_left(pokemon)
    return (left + 9) // 10


def ko_threshold_counters(ctx: StrategyContext, pool, count: int) -> Dict[str, int]:
    """Spend counters on the cheapest KOs first, then push the next-nearest
    target toward its threshold.  Ties prefer multi-prize bodies."""
    if count <= 0 or not pool:
        return {}
    ordered = sorted(
        pool,
        key=lambda p: (_ko_need(ctx, p), -ctx.prize_value(p), ctx.hp_left(p)),
    )
    plan: Dict[str, int] = {}
    remaining = count
    for pokemon in ordered:
        if remaining <= 0:
            break
        need = _ko_need(ctx, pokemon)
        if need <= 0:
            continue
        take = min(remaining, need)
        plan[pokemon.entity_id] = take
        remaining -= take
    return plan


def promotion_score(ctx: StrategyContext, pokemon,
                    attackers=None) -> float:
    """Rank bodies for the Active slot: attack-ready VMAXes first,
    powered-but-unready next, everything else last (stable order)."""
    if attackers is None:
        attackers = ATTACKERS
    name = ctx.name(pokemon)
    if name not in attackers:
        return 0.0
    ready = ctx.energy_attached(pokemon) >= max(1, ctx.min_attack_cost(pokemon))
    score = 2000.0 if ready else 1000.0
    score += ctx.energy_attached(pokemon) * 10.0
    if name.endswith("VMAX"):
        score += 2.0
    return score


def gust_score(ctx: StrategyContext, pokemon) -> float:
    """Boss-style gust value: a KO-range body now, else anything scratched."""
    damage = ctx.active_attack_damage()
    left = ctx.hp_left(pokemon)
    if damage and left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    if dealt > 0:
        return 500.0 + dealt
    return 0.0


# ----------------------------------------------------------------------
# gates shared by brains


def gate_path_to_the_peak(ctx: StrategyContext) -> bool:
    """Path is a strategic switch: only when the opponent leans on Rule Box
    Pokemon and we don't already control the stadium."""
    if ctx.opponent_stadium_is("Path to the Peak"):
        return False
    return ctx.opponent_rule_box()


def gate_tool_jammer(ctx: StrategyContext) -> bool:
    return ctx.opponent_tools()


def gate_food_tin(ctx: StrategyContext, min_damage: int = 100) -> bool:
    """Heal only when the damage is heavy enough to matter."""
    active = ctx.active()
    return active is not None and ctx.damage_on(active) >= min_damage


def gate_switch_or_rope(ctx: StrategyContext) -> bool:
    """Swap only when the Active can't attack (or is pure setup fodder)."""
    return not ctx.active_ready()


def gate_raihan(ctx: StrategyContext) -> bool:
    """Comeback tool: only after we lost a Pokemon."""
    return ctx.prizes_lost() >= 1


# ----------------------------------------------------------------------
# DRAGAPULT VMAX / INTELEON
#
# Main plan: Dragapult V -> VMAX, Max Phantom every turn; Drizzile/Shady
# Dealings is the trainer toolbox; bench damage lands toward KO thresholds
# (Quick Shooting / Zigzagoon / Horror Energy finish them); Boss gusts the
# already-damaged; keep a second attacker developing.

BENCH_ORDER = ["Dragapult V", "Sobble", "Galarian Zigzagoon"]
ATTACH_ORDER = ["Dragapult VMAX", "Dragapult V", "Drizzile", "Inteleon"]
ENERGY_ORDER = ["Horror Psychic Energy", "Psychic Energy"]
EVOLVE_ORDER = ["Dragapult VMAX", "Drizzile", "Inteleon"]
ABILITY_ORDER = ["Quick Shooting"]
ATTACKERS = {"Dragapult VMAX", "Dragapult V"}


def _dragapult_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    if description == "DefaultStadiumPlayAbility" and name == "Path to the Peak":
        return gate_path_to_the_peak(ctx)
    if name == "Tool Jammer":
        return gate_tool_jammer(ctx)
    if name == "Suspicious Food Tin":
        return gate_food_tin(ctx)
    if name in ("Switch", "Escape Rope"):
        return gate_switch_or_rope(ctx)
    if name == "Scoop Up Net":
        # Free a stuck utility Active (promotion follows), or recycle a
        # battered non-attacker; never bounce a workable attacker.
        active = ctx.active()
        if active is None:
            return False
        if ctx.name(active) not in ATTACKERS and not ctx.active_ready():
            return True
        return any(
            p is not active and ctx.name(p) not in ATTACKERS
            and ctx.damage_on(p) >= 60
            for p in ctx.in_play()
        )
    if name == "Raihan":
        return gate_raihan(ctx)
    if name == "Boss's Orders":
        # Gust only something we can actually finish: an KO-range body now,
        # or anything already scratched by a previous Max Phantom.
        window = ctx.ko_window()
        if window:
            return True
        return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
    if name == "Professor's Research":
        # Discarding is acceptable only when the hand really needs a refresh.
        return ctx.hand_size() <= 5
    if description == "BaseRetreat":
        # Manual retreat discards energy: never dump the Active's attach unless
        # the body is energy-less, or a benched Dragapult is already attack-ready
        # while the Active can't fire (Switch/Escape Rope handle the rest).
        active = ctx.active()
        if active is None:
            return False
        if ctx.energy_attached(active) == 0:
            return True
        if ctx.active_ready():
            return False
        return any(
            ctx.name(p) in ATTACKERS
            and ctx.energy_attached(p) >= ctx.min_attack_cost(p)
            for p in ctx.bench()
        )
    if description == "UsePokemonAbility":
        return name in ABILITY_ORDER
    return True


def _dragapult_value(name: str, ctx: StrategyContext, in_hand: bool) -> float:
    """Situational value of a card: fills the missing setup piece first."""
    hand = set(ctx.hand_names())
    play = set(ctx.in_play_names())
    all_seen = hand | play
    v = 0.0

    if name == "Evolution Incense":
        if "Dragapult V" in all_seen and "Dragapult VMAX" not in all_seen:
            v += 35
        if any(p in play for p in ("Sobble",)) and "Drizzile" not in hand:
            v += 30
        if "Drizzile" in play and "Inteleon" not in hand:
            v += 15
        v += 5
    elif name == "Level Ball":
        if "Sobble" in play and "Drizzile" not in hand:
            v += 30
        if "Sobble" not in all_seen:
            v += 25
        if "Galarian Zigzagoon" not in all_seen:
            v += 8
    elif name == "Fog Crystal":
        if "Dragapult V" not in all_seen:
            v += 30
        if "Psychic Energy" not in hand:
            v += 22
        v += 3
    elif name == "Quick Ball":
        if "Dragapult V" not in all_seen:
            v += 30
        v -= 5  # discards a card
    elif name == "Boss's Orders":
        v += 40 if ctx.ko_window() else 12
    elif name in ("Switch", "Escape Rope"):
        v += 25 if not ctx.active_ready() else 4
    elif name == "Professor's Research":
        v += 30
    elif name == "Marnie":
        v += 12
        if ctx.hand_size(ctx.opp) > ctx.hand_size():
            v += 8  # disruption is live
    elif name == "Raihan":
        v += 30 if ctx.prizes_lost() else 0
    elif name == "Path to the Peak":
        v += 30 if ctx.opponent_rule_box() else 0
    elif name == "Tool Jammer":
        v += 20 if ctx.opponent_tools() else 0
    elif name == "Suspicious Food Tin":
        v += 25 if gate_food_tin(ctx) else 0
    elif name == "Scoop Up Net":
        v += 12 if "Galarian Zigzagoon" in play else 5
    elif name == "Dragapult V":
        v += 35 if "Dragapult V" not in all_seen else 10
    elif name == "Sobble":
        v += 30 if "Sobble" not in play else 8
    elif name == "Dragapult VMAX":
        v += 35 if "Dragapult V" in all_seen and "Dragapult VMAX" not in all_seen else 5
    elif name == "Drizzile":
        v += 30 if "Sobble" in play and "Drizzile" not in hand else 5
    elif name == "Inteleon":
        v += 18 if "Drizzile" in play else 4
    elif name == "Galarian Zigzagoon":
        v += 10 if name not in all_seen else 3
    elif name.endswith("Energy"):
        v += 22 if "Psychic Energy" not in hand and name == "Psychic Energy" else 8

    if in_hand and name in hand and name not in (
            "Path to the Peak", "Marnie", "Professor's Research", "Level Ball"):
        v -= 40  # a second copy adds little; let other needs surface first
    return v


def _dragapult_action_score(description: str, name: str,
                            ctx: StrategyContext) -> float:
    if description == "EvolvePokemonPlayAbility":
        return order_score(EVOLVE_ORDER, name)
    if description == "DefaultEnergyPlayAbility":
        return order_score(ENERGY_ORDER, name)
    if description == "DefaultPokemonPlayAbility":
        return order_score(BENCH_ORDER, name)
    if description == "UsePokemonAbility":
        return order_score(ABILITY_ORDER, name) + 5.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility"):
        return _dragapult_value(name, ctx, in_hand=True)
    return 0.0


def _dragapult_attack_score(title: str, base: float,
                            ctx: StrategyContext) -> float:
    score = base
    active = ctx.active()
    if active is not None and ctx.hp_left(ctx.active(ctx.opp)) <= base:
        score += 1000.0  # take the KO
    if title == "Max Phantom":
        # 5 counters (50 damage) to spend on the bench: value every body
        # they can finish, plus 10 each toward a future threshold.
        for pokemon in ctx.bench(ctx.opp):
            left = ctx.hp_left(pokemon)
            if 0 < left <= 50:
                score += 40.0
            elif left > 50:
                score += 8.0
    return score


def _dragapult_target_score(description: str, name: str,
                            ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return gust_score(ctx, target)
    if description == "UsePokemonAbility" and name == "Quick Shooting":
        left = ctx.hp_left(target)
        if 0 < left <= 20:
            return 1000.0 - left
        return 300.0 - left
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            # Pay with the basic; Horror Psychic stays attached for recoil.
            return 200.0 if ctx.name(target) == "Psychic Energy" else 100.0
        if target.owning_player_id == ctx.me:
            return promotion_score(ctx, target)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        score = order_score(ATTACH_ORDER, ctx.name(target))
        return score + (5.0 if target is ctx.active() else 0.0)
    if description == "EvolvePokemonPlayAbility":
        return 5.0 if target is not ctx.active() else 8.0
    if description == "DefaultToolPlayAbility":
        return 5.0 if target is ctx.active() else 0.0
    return 0.0


def _dragapult_search_score(card, ctx: StrategyContext) -> float:
    return _dragapult_value(ctx.name(card), ctx, in_hand=False)


def _dragapult_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts (prompt_entity_picker):

    - "new Active" choices -> promote the ready attacker (or gust value when
      picking the OPPONENT's body, e.g. Boss's Orders / Escape Rope).
    - Scoop Up Net ("put into your hand") -> bounce a stuck utility Active.
    - hand discards ("Discard a card ...") -> dump the least valuable card.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return promotion_score(ctx, card)
    if not mine and "new Active" in text:
        return gust_score(ctx, card)
    if not mine and ("opponent's" in text or "opponent\u2019s" in text):
        return gust_score(ctx, card)
    if mine and "put into your hand" in text:
        active = ctx.active()
        if card is active:
            return 700.0 if name not in ATTACKERS else -100.0
        if name not in ATTACKERS and ctx.damage_on(card) >= 60:
            return 300.0
        return 50.0
    if mine and "discard" in text.lower():
        return -_dragapult_value(name, ctx, in_hand=True)
    if mine and "heal" in text.lower():
        return float(ctx.damage_on(card))
    return 0.0


def _dragapult_counter_plan(pool, count: int, ctx: StrategyContext):
    return ko_threshold_counters(ctx, pool, count)


DRAGAPULT_INTELEON = {
    "allow_action": _dragapult_allow,
    "action_score": _dragapult_action_score,
    "attack_score": _dragapult_attack_score,
    "target_score": _dragapult_target_score,
    "search_score": _dragapult_search_score,
    "pick_score": _dragapult_pick,
    "counter_plan": _dragapult_counter_plan,
}


# ----------------------------------------------------------------------
# RAPID STRIKE URSHIFU VMAX (Octillery toolbox, Cheryl, hammer disruption)
#
# Plan: bench Urshifu V + Remoraid, evolve to VMAX, unlock Gale Thrust 150
# with Switch / Escape Rope / Tower of Waters free retreats, fire G-Max
# Rapid Flow only when two bodies fall (or one folds and another is wrecked),
# Cheryl heals a battered VMAX, Crushing Hammer / Fan of Waves strip the
# opponent's attacker, rebuild the next Urshifu after a GRF discard turn.

RS_ATTACKERS = {"Rapid Strike Urshifu VMAX", "Rapid Strike Urshifu V"}
RS_BENCH_ORDER = ["Rapid Strike Urshifu V", "Remoraid", "Crobat V"]
RS_ENERGY_ORDER = ["Rapid Strike Energy", "Fighting Energy", "Stone Fighting Energy"]
RS_EVOLVE_ORDER = ["Rapid Strike Urshifu VMAX", "Octillery"]
RS_ABILITY_ORDER = ["Rapid Strike Search"]
RS_GALE = 150
RS_SNIPER = 120
_RS_REPEATABLE = {
    "Professor's Research", "Marnie", "Korrina's Focus",
    "Crushing Hammer", "Fan of Waves",
}


def rs_energy_value(ctx: StrategyContext, pokemon) -> int:
    """Attached energy in pay-units: Rapid Strike Energy provides 2,
    every other energy in this deck provides 1."""
    total = 0
    for child in getattr(pokemon, "children", None) or []:
        child_name = ctx.name(child)
        if not child_name.endswith("Energy"):
            continue
        total += 2 if child_name == "Rapid Strike Energy" else 1
    return total


def _rs_gust_window(ctx: StrategyContext) -> List:
    """Opponent bodies a Gale Thrust / Hundred Furious Blows (150) can KO."""
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= RS_GALE]


def _rs_gust(ctx: StrategyContext, pokemon) -> float:
    """Boss value: a 150-window body first, else anything already scratched."""
    left = ctx.hp_left(pokemon)
    if 0 < left <= RS_GALE:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    if dealt > 0:
        return 500.0 + dealt
    return 0.0


def _rs_snipe(ctx: StrategyContext, pokemon) -> float:
    """G-Max Rapid Flow target value: fold it (120, or 240 on a Fighting-
    weak Active), else dent it toward a later threshold."""
    left = ctx.hp_left(pokemon)
    if left <= 0:
        return 0.0
    hit = RS_SNIPER
    if pokemon is ctx.active(ctx.opp):
        try:
            weakness = getattr(
                def_for(getattr(pokemon, "archetype_id", None)),
                "weakness_type", None,
            )
        except Exception:
            weakness = None
        if weakness == PokemonTypes.FIGHTING:
            hit = 2 * RS_SNIPER
    if left <= hit:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    if dealt > 0:
        return 500.0 + dealt
    if ctx.prize_value(pokemon) >= 3:
        return 300.0
    return 100.0


def _rs_grf_score(ctx: StrategyContext) -> float:
    """How good G-Max Rapid Flow is right now: double folds = 2100,
    fold + wrecked second body = 1600, lone fold = 1300, otherwise skip
    (100) and keep the energy attached."""
    bodies = [p for p in ctx.in_play(ctx.opp) if ctx.hp_left(p) > 0]
    if not bodies:
        return 100.0
    kos = 0
    for pokemon in bodies:
        left = ctx.hp_left(pokemon)
        hit = RS_SNIPER
        if pokemon is ctx.active(ctx.opp):
            try:
                weakness = getattr(
                    def_for(getattr(pokemon, "archetype_id", None)),
                    "weakness_type", None,
                )
            except Exception:
                weakness = None
            if weakness == PokemonTypes.FIGHTING:
                hit = 2 * RS_SNIPER
        if left <= hit:
            kos += 1
    if kos >= 2:
        return 2100.0
    if kos == 1:
        wrecked = any(
            ctx.hp_left(p) <= 2 * RS_SNIPER
            for p in bodies if ctx.hp_left(p) > RS_SNIPER
        )
        return 1600.0 if wrecked else 1300.0
    return 100.0


def _rs_bench_ready(ctx: StrategyContext) -> bool:
    return any(
        ctx.name(p) in RS_ATTACKERS and rs_energy_value(ctx, p) >= 1
        for p in ctx.bench()
    )


def _rs_switch_ok(ctx: StrategyContext) -> bool:
    """Switch / Escape Rope: unsticks a utility Active, or swaps in a
    powered body for Gale Thrust 150 -- but never breaks a live GRF."""
    active = ctx.active()
    if active is None:
        return False
    if rs_energy_value(ctx, active) >= 3 and _rs_grf_score(ctx) >= 1600:
        return False
    if not ctx.active_ready():
        return True
    # Ready attacker: only swap to unlock a fresh Gale Thrust.
    return (not ctx.entered_active(active)) and _rs_bench_ready(ctx)


def _rs_retreat_ok(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None:
        return False
    if rs_energy_value(ctx, active) == 0:
        return True                      # dead body out of the way
    if ctx.entered_active(active):
        return False                     # Gale Thrust 150 is live
    if rs_energy_value(ctx, active) >= 3 and _rs_grf_score(ctx) >= 1600:
        return False                     # swing the GRF first
    if ctx.active_ready():
        # Free swap under Tower of Waters -> next body enters for 150.
        return (ctx.opponent_stadium_is("Tower of Waters")
                and _rs_bench_ready(ctx))
    return _rs_bench_ready(ctx)


def _rs_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    if name in ("Switch", "Escape Rope"):
        return _rs_switch_ok(ctx)
    if name == "Cheryl":
        # Heal only when a VMAX's damage actually matters (>= 100 on board).
        return any(
            ctx.name(p) == "Rapid Strike Urshifu VMAX" and ctx.damage_on(p) >= 100
            for p in ctx.in_play()
        )
    if name == "Professor's Research":
        return ctx.hand_size() <= 4       # discard only for a real refresh
    if name in ("Korrina's Focus", "Marnie"):
        return ctx.hand_size() <= 5
    if name == "Boss's Orders":
        if _rs_gust_window(ctx):
            return True
        return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
    if description == "DefaultStadiumPlayAbility" and name == "Tower of Waters":
        return not ctx.opponent_stadium_is("Tower of Waters")
    if description == "DefaultToolPlayAbility" and name == "Vitality Band":
        return any(ctx.name(p) in RS_ATTACKERS for p in ctx.in_play())
    if description == "BaseRetreat":
        return _rs_retreat_ok(ctx)
    if description == "UsePokemonAbility":
        return name in RS_ABILITY_ORDER
    return True


def _rs_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational value of a card: fills the missing setup piece first."""
    hand = set(ctx.hand_names())
    play = set(ctx.in_play_names())
    seen = hand | play
    board = ctx.in_play()
    attackers = [p for p in board if ctx.name(p) in RS_ATTACKERS]
    best_energy = max((rs_energy_value(ctx, p) for p in attackers), default=0)
    need_energy = bool(attackers) and best_energy < 3
    v_count = sum(1 for p in board if ctx.name(p) == "Rapid Strike Urshifu V")

    # -- Pokemon gap pieces (searches + hand planning) --------------------
    if name == "Rapid Strike Urshifu V":
        v = 30.0 if v_count == 0 else (18.0 if v_count < 2 else 8.0)
    elif name == "Rapid Strike Urshifu VMAX":
        if "Rapid Strike Urshifu VMAX" in seen:
            v = 10.0
        elif "Rapid Strike Urshifu V" in seen:
            v = 35.0
        else:
            v = 6.0
    elif name == "Remoraid":
        setup = any(ctx.name(p) in ("Remoraid", "Octillery") for p in board)
        v = 28.0 if not setup and "Remoraid" not in hand else 7.0
    elif name == "Octillery":
        can_evolve = any(ctx.name(p) == "Remoraid" for p in board)
        v = 30.0 if can_evolve and "Octillery" not in seen else 7.0
    elif name == "Crobat V":
        v = 22.0 if "Crobat V" not in seen and ctx.hand_size() <= 4 else 6.0
    elif name == "Rapid Strike Energy":
        v = 30.0 if need_energy and name not in hand else (
            14.0 if need_energy else 8.0)
    elif name == "Fighting Energy":
        v = 24.0 if need_energy and name not in hand else (
            12.0 if need_energy else 8.0)
    elif name == "Stone Fighting Energy":
        v = 18.0 if need_energy else 7.0

    # -- Supporters / items ------------------------------------------------
    elif name == "Cheryl":
        v = 50.0
    elif name == "Boss's Orders":
        if _rs_gust_window(ctx):
            v = 40.0
        elif any(ctx.damage_on(p) for p in ctx.in_play(ctx.opp)):
            v = 18.0
        else:
            v = 12.0
    elif name == "Professor's Research":
        v = 30.0
    elif name == "Korrina's Focus":
        v = 25.0
    elif name == "Evolution Incense":
        v = 6.0
        if "Rapid Strike Urshifu V" in seen and "Rapid Strike Urshifu VMAX" not in seen:
            v = 32.0
        elif (any(ctx.name(p) == "Remoraid" for p in board)
                and "Octillery" not in seen):
            v = 26.0
    elif name == "Quick Ball":
        if "Rapid Strike Urshifu V" not in seen:
            v = 30.0
        elif v_count < 2:
            v = 18.0
        elif "Crobat V" not in seen and ctx.hand_size() <= 4:
            v = 16.0
        else:
            v = 7.0
    elif name == "Great Ball":
        if "Rapid Strike Urshifu V" in seen and "Rapid Strike Urshifu VMAX" not in seen:
            v = 26.0
        elif "Rapid Strike Urshifu V" not in seen:
            v = 24.0
        elif v_count < 2:
            v = 20.0
        elif (not any(ctx.name(p) in ("Remoraid", "Octillery") for p in board)
                and "Remoraid" not in hand):
            v = 16.0
        elif "Crobat V" not in seen and ctx.hand_size() <= 4:
            v = 14.0
        else:
            v = 9.0
    elif name in ("Switch", "Escape Rope"):
        active = ctx.active()
        if active is None:
            v = 4.0
        elif not ctx.active_ready():
            v = 25.0
        elif (not ctx.entered_active(active)) and _rs_bench_ready(ctx):
            v = 22.0                     # unlocks Gale Thrust 150
        else:
            v = 4.0
    elif name == "Tower of Waters":
        v = 20.0
    elif name == "Marnie":
        v = 18.0 if ctx.hand_size(ctx.opp) > ctx.hand_size() else 10.0
    elif name == "Vitality Band":
        v = 15.0 if attackers else 6.0
    elif name == "Fan of Waves":
        v = 14.0
    elif name == "Crushing Hammer":
        v = 12.0
    else:
        v = 6.0

    if in_hand and name in hand and name not in _RS_REPEATABLE:
        v -= 40.0                         # a second copy adds little
    return v


def _rs_bench_score(name: str, ctx: StrategyContext) -> float:
    score = order_score(RS_BENCH_ORDER, name)
    if name == "Crobat V":
        score += 40.0 if ctx.hand_size() <= 5 else -30.0
    elif name == "Rapid Strike Urshifu V":
        v_count = sum(1 for p in ctx.in_play() if ctx.name(p) == name)
        score += 15.0 if v_count < 2 else -10.0
    elif name == "Remoraid":
        setup = any(ctx.name(p) in ("Remoraid", "Octillery")
                    for p in ctx.in_play())
        score += 20.0 if not setup else -20.0
    return score


def _rs_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "EvolvePokemonPlayAbility":
        return order_score(RS_EVOLVE_ORDER, name)
    if description == "DefaultEnergyPlayAbility":
        return order_score(RS_ENERGY_ORDER, name)
    if description == "DefaultPokemonPlayAbility":
        return _rs_bench_score(name, ctx)
    if description == "UsePokemonAbility":
        return order_score(RS_ABILITY_ORDER, name) + 5.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility",
                       "DefaultToolPlayAbility"):
        return _rs_value(name, ctx, in_hand=True)
    return 0.0


def _rs_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0        # take the KO
        return score

    if title == "Gale Thrust":
        entered = ctx.entered_active(ctx.active())
        if entered:
            return _ko(1000.0 + RS_GALE, RS_GALE)   # Bench -> Active: 150
        return _ko(300.0 + 30, 30)
    if title == "G-Max Rapid Flow":
        return _rs_grf_score(ctx)        # 100 = save the energy
    if title == "Hundred Furious Blows":
        return _ko(750.0 + RS_GALE, RS_GALE)
    if title == "Strafe":
        return 150.0
    if title == "Waterfall":
        return 100.0
    return base


def _rs_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _rs_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            # Drop the cheapest unit: a basic pays 1, RS Energy pays 2.
            target_name = ctx.name(target)
            if target_name == "Rapid Strike Energy":
                return 50.0
            if target_name == "Stone Fighting Energy":
                return 150.0
            return 200.0
        if target.owning_player_id == ctx.me:
            return promotion_score(ctx, target, attackers=RS_ATTACKERS)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        if ctx.name(target) in RS_ATTACKERS:
            score = 500.0 if target is ctx.active() else 300.0
            if rs_energy_value(ctx, target) < 3:
                score += 100.0           # hungry for Gale / GRF
            return score
        return 5.0
    if description == "EvolvePokemonPlayAbility":
        if name == "Rapid Strike Urshifu VMAX":
            return 10.0 if target is ctx.active() else 6.0
        if name == "Octillery":
            return 8.0
        return 0.0
    if description == "DefaultToolPlayAbility":
        target_name = ctx.name(target)
        if target_name in RS_ATTACKERS:
            if target is ctx.active():
                return 10.0
            return 8.0 if target_name == "Rapid Strike Urshifu VMAX" else 6.0
        return 0.0
    return 0.0


def _rs_search_score(card, ctx: StrategyContext) -> float:
    return _rs_value(ctx.name(card), ctx, in_hand=False)


def _rs_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote the ready attacker;
    - opponent "new Active" (Boss / Rope) -> gust value;
    - G-Max Rapid Flow snipe targets -> fold first, dent second;
    - Crushing Hammer -> strip the opponent's most-powered body;
    - Fan of Waves -> the Active's special energy;
    - hand discards -> dump the least valuable card.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return promotion_score(ctx, card, attackers=RS_ATTACKERS)
    if not mine and "new Active" in text:
        return _rs_gust(ctx, card)
    if not mine and ("take" in text or "damage" in text):
        return _rs_snipe(ctx, card)
    if not mine and "opponent's" in text:
        # Crushing Hammer: the powered attacker hurts most.
        score = 150.0 * ctx.energy_attached(card)
        if card is ctx.active(ctx.opp):
            score += 100.0
        return score
    if not mine and "Special Energy" in text:
        parent = getattr(card, "parent", None)
        return 500.0 if (parent is not None
                         and parent is ctx.active(ctx.opp)) else 200.0
    if mine and "into your hand" in text:
        return _rs_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        return -_rs_value(name, ctx, in_hand=True)
    return 0.0


RAPID_STRIKE_URSHIFU = {
    "allow_action": _rs_allow,
    "action_score": _rs_action_score,
    "attack_score": _rs_attack_score,
    "target_score": _rs_target_score,
    "search_score": _rs_search_score,
    "pick_score": _rs_pick,
}


# ----------------------------------------------------------------------
# Shadow Rider Calyrex V
#
# Engine: Calyrex VMAX's Underworld Door (attach a Psychic Energy to a
# benched Psychic Pokemon + draw 2) chained with Cresselia's Crescent
# Glow and Alcremie's Adornment.  Max Geist scales at 30 per Psychic
# Energy attached across our whole board, so the brain spreads energy
# wide (never piles it on one body) and leans on the ability chains.

SR_ATTACKERS = {"Shadow Rider Calyrex VMAX", "Shadow Rider Calyrex V",
                "Alcremie VMAX", "Alcremie V", "Cresselia",
                "Galarian Articuno"}
SR_BENCH_ORDER = ["Shadow Rider Calyrex V", "Alcremie V", "Crobat V",
                  "Cresselia", "Galarian Articuno"]
SR_EVOLVE_ORDER = ["Shadow Rider Calyrex VMAX", "Alcremie VMAX"]
SR_ABILITY_ORDER = ["Underworld Door", "Cruel Charge", "Training Court"]
SR_NEED = {"Shadow Rider Calyrex VMAX": 3, "Shadow Rider Calyrex V": 3,
           "Alcremie VMAX": 2, "Alcremie V": 3, "Cresselia": 1,
           "Galarian Articuno": 3}
_SR_SUPPORT = {"Cresselia", "Crobat V", "Galarian Articuno"}
_SR_REPEATABLE = {
    "Professor's Research", "Marnie", "Quick Ball", "Fog Crystal",
    "Evolution Incense", "Air Balloon", "Training Court", "Psychic Energy",
}


def _sr_energy_total(ctx: StrategyContext) -> int:
    """Psychic Energy attached across our board (this deck runs nothing
    else; Max Geist scales on it)."""
    return sum(ctx.energy_attached(p) for p in ctx.in_play())


def _sr_stadium_up(ctx: StrategyContext) -> bool:
    board = getattr(ctx, "board", None)
    if board is None:
        return False
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


def _sr_turn2(ctx: StrategyContext) -> bool:
    """We are the second player on turn 2 (Crescent Glow's 3-energy burst)."""
    session = getattr(ctx, "session", None)
    if session is None:
        return False
    try:
        first = session.first_player_id
        return (session.turn_state.turn_number == 2
                and first is not None and first != ctx.me)
    except Exception:
        return False


def _sr_output(ctx: StrategyContext, pokemon) -> int:
    """Best damage `pokemon` could deal as our Active right now (0 for
    utility bodies and attackers that are not powered up yet)."""
    if pokemon is None:
        return 0
    name = ctx.name(pokemon)
    have = ctx.energy_attached(pokemon)
    energy = _sr_energy_total(ctx)
    if name == "Shadow Rider Calyrex VMAX":
        return 10 + 30 * energy if have >= 3 else 0
    if name == "Shadow Rider Calyrex V":
        if have >= 3:
            return 50           # Astral Barrage per-body ceiling
        return 10 if have >= 1 else 0
    if name == "Alcremie VMAX":
        if have >= 2:
            damage = 60 * energy          # G-Max Whisk
            opp = ctx.active(ctx.opp)
            if opp is not None and 0 < ctx.hp_left(opp) <= damage:
                return damage              # she closes a KO right now
        return 0                # else she is the accel body, not the puncher
    if name == "Alcremie V":
        return 100 if have >= 3 else 0
    if name == "Cresselia":
        if have >= 2:
            return 120 if energy >= 5 else 30
        return 0                # Crescent Glow accelerates, not damage
    if name == "Galarian Articuno":
        return 120 if have >= 3 else 0
    return 0                    # Crobat V never swings


def _sr_strike_damage(ctx: StrategyContext) -> int:
    return _sr_output(ctx, ctx.active())


def _sr_gust_window(ctx: StrategyContext) -> List:
    damage = _sr_strike_damage(ctx)
    if damage <= 0:
        return []
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= damage]


def _sr_gust(ctx: StrategyContext, pokemon) -> float:
    damage = _sr_strike_damage(ctx)
    left = ctx.hp_left(pokemon)
    if damage > 0 and 0 < left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    return 500.0 + dealt if dealt > 0 else 0.0


def _sr_snipe(ctx: StrategyContext, pokemon, hit: int) -> float:
    """Remote target value: fold it with `hit`, else dent it toward
    a later threshold."""
    left = ctx.hp_left(pokemon)
    if left <= 0:
        return 0.0
    if left <= hit:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    if dealt > 0:
        return 500.0 + dealt
    return 300.0 if ctx.prize_value(pokemon) >= 3 else 100.0


def _sr_lock_worth(ctx: StrategyContext) -> bool:
    """Shadow Mist's special-energy / stadium lock only matters when the
    opponent actually has something to lock."""
    for pokemon in ctx.in_play(ctx.opp):
        for child in getattr(pokemon, "children", None) or []:
            definition = def_for(getattr(child, "archetype_id", None))
            if getattr(definition, "is_special", False):
                return True
    return _sr_stadium_up(ctx)


def _sr_retreat_ok(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None:
        return False
    active_dmg = _sr_output(ctx, active)
    bench_best = max((_sr_output(ctx, p) for p in ctx.bench()), default=0)
    if bench_best <= 0:
        return False
    if active_dmg <= 0:
        return True                       # utility body, someone can swing
    return bench_best >= active_dmg + 60   # only when clearly better


def _sr_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    deck = ctx.deck_size()
    if name == "Professor's Research":
        # hand: ... and leave deck runway -- Research alone can mill 7.
        return ctx.hand_size() <= 5 and deck > 12
    if name == "Marnie":
        # hand returns to the deck bottom, so only the draw itself needs room
        return (ctx.hand_size() <= 5 or ctx.hand_size(ctx.opp) >= 6) \
            and deck > 5
    if name in ("Fog Crystal", "Quick Ball", "Evolution Incense"):
        return deck > 5                    # a search can be the last card
    if name == "Boss's Orders":
        if _sr_gust_window(ctx):
            return True
        return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
    if name == "Phoebe":
        return True                     # engine gate: our VMAX in play
    if description == "DefaultStadiumPlayAbility" and name == "Training Court":
        return (not ctx.opponent_stadium_is("Training Court")
                and any(n == "Psychic Energy" for n in ctx.discard_names()))
    if description == "DefaultToolPlayAbility" and name == "Air Balloon":
        return True
    if description == "BaseRetreat":
        return _sr_retreat_ok(ctx)
    if description == "UsePokemonAbility":
        if name == "Underworld Door":
            return deck > 8              # the draw 2 is our biggest mill
        return name in SR_ABILITY_ORDER
    return True


def _sr_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational value of a card: fills the missing setup piece first."""
    hand = set(ctx.hand_names())
    play = set(ctx.in_play_names())
    seen = hand | play
    board = ctx.in_play()
    v_count = sum(1 for p in board if ctx.name(p) == "Shadow Rider Calyrex V")
    energy_in_hand = sum(1 for n in ctx.hand_names() if n == "Psychic Energy")
    alcremie_v = "Alcremie V" in seen
    alcremie_vmax = "Alcremie VMAX" in seen
    vmax_seen = "Shadow Rider Calyrex VMAX" in seen

    # -- Pokemon gap pieces (searches + hand planning) --------------------
    if name == "Shadow Rider Calyrex V":
        v = 35.0 if v_count == 0 else (25.0 if v_count < 3 else 8.0)
    elif name == "Shadow Rider Calyrex VMAX":
        if vmax_seen:
            v = 10.0
        elif "Shadow Rider Calyrex V" in seen:
            v = 35.0
        else:
            v = 6.0
    elif name == "Alcremie V":
        v = 20.0 if not alcremie_v else 6.0
    elif name == "Alcremie VMAX":
        if alcremie_vmax:
            v = 8.0
        elif alcremie_v:
            v = 25.0 if vmax_seen else 14.0
        else:
            v = 5.0
    elif name == "Crobat V":
        v = 24.0 if "Crobat V" not in seen and ctx.hand_size() <= 4 else 6.0
    elif name == "Cresselia":
        v = 18.0 if "Cresselia" not in play else 4.0
    elif name == "Galarian Articuno":
        v = 16.0 if ("Galarian Articuno" not in seen
                      and energy_in_hand >= 2) else 5.0
    elif name == "Psychic Energy":
        if energy_in_hand == 0:
            v = 28.0               # Underworld Door needs one in hand
        elif energy_in_hand == 1:
            v = 22.0
        else:
            v = 12.0

    # -- Supporters / items ------------------------------------------------
    elif name == "Professor's Research":
        v = 30.0
    elif name == "Marnie":
        v = 24.0 if ctx.hand_size(ctx.opp) > ctx.hand_size() else 18.0
    elif name == "Boss's Orders":
        if _sr_gust_window(ctx):
            v = 40.0
        elif any(ctx.damage_on(p) for p in ctx.in_play(ctx.opp)):
            v = 18.0
        else:
            v = 12.0
    elif name == "Phoebe":
        v = 14.0
    elif name == "Fog Crystal":
        if v_count == 0:
            v = 24.0
        elif energy_in_hand == 0:
            v = 22.0
        else:
            v = 14.0
    elif name == "Quick Ball":
        if v_count == 0:
            v = 30.0
        elif v_count < 2:
            v = 24.0
        elif "Crobat V" not in seen and ctx.hand_size() <= 4:
            v = 16.0
        elif alcremie_v and not alcremie_vmax:
            v = 12.0
        else:
            v = 8.0
    elif name == "Evolution Incense":
        if "Shadow Rider Calyrex V" in seen and not vmax_seen:
            v = 32.0
        elif alcremie_v and not alcremie_vmax and vmax_seen:
            v = 16.0
        else:
            v = 8.0
    elif name == "Pal Pad":
        v = 12.0
    elif name == "Air Balloon":
        v = 15.0
    elif name == "Training Court":
        v = 20.0
    else:
        v = 6.0

    if in_hand and name in hand and name not in _SR_REPEATABLE:
        v -= 40.0                         # a second copy adds little
    return v


def _sr_bench_score(name: str, ctx: StrategyContext) -> float:
    score = order_score(SR_BENCH_ORDER, name)
    if name == "Shadow Rider Calyrex V":
        v_count = sum(1 for p in ctx.in_play() if ctx.name(p) == name)
        score += 20.0 if v_count < 3 else -20.0
    elif name == "Crobat V":
        score += 40.0 if ctx.hand_size() <= 5 else -30.0
    elif name == "Cresselia":
        score += 25.0 if _sr_energy_total(ctx) < 6 else -15.0
    elif name == "Galarian Articuno":
        energy_in_hand = sum(1 for n in ctx.hand_names()
                             if n == "Psychic Energy")
        score += 20.0 if energy_in_hand >= 2 else -15.0
    elif name == "Alcremie V":
        score += 10.0 if "Shadow Rider Calyrex VMAX" in ctx.in_play_names() else 0.0
    return score




def _sr_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "EvolvePokemonPlayAbility":
        if name == "Shadow Rider Calyrex VMAX":
            return 1000.0                 # the engine, always first
        if name == "Alcremie VMAX":
            # second line only once the primary engine is online
            return 600.0 if "Shadow Rider Calyrex VMAX" in ctx.in_play_names() \
                else 200.0
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return 50.0                       # Psychic Energy is the only kind
    if description == "DefaultPokemonPlayAbility":
        return _sr_bench_score(name, ctx)
    if description == "UsePokemonAbility":
        return order_score(SR_ABILITY_ORDER, name) + 5.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility",
                       "DefaultToolPlayAbility"):
        return _sr_value(name, ctx, in_hand=True)
    return 0.0


def _sr_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0        # take the KO
        return score

    energy = _sr_energy_total(ctx)
    if title == "Max Geist":
        damage = 10 + 30 * energy
        return _ko(600.0 + damage, damage)
    if title == "Shadow Mist":
        return 10.0 + (450.0 if _sr_lock_worth(ctx) else 0.0)
    if title == "Astral Barrage":
        bodies = [p for p in ctx.in_play(ctx.opp) if ctx.hp_left(p) > 0]
        finishes = sum(1 for p in bodies if ctx.hp_left(p) <= 50)
        if finishes >= 2:
            return 1500.0
        if finishes == 1:
            return 1100.0
        dented = sum(1 for p in bodies if 0 < ctx.hp_left(p) <= 100)
        return 300.0 + 25.0 * min(2, dented)
    if title == "Crescent Glow":
        bench_ready = any(_sr_output(ctx, p) > 0 for p in ctx.bench())
        score = 700.0 if not bench_ready else 250.0
        if _sr_turn2(ctx):
            score += 400.0                # second-player turn-2 burst
        return score
    if title == "Photon Laser":
        damage = 120 if energy >= 5 else 30
        return _ko(400.0 + damage, damage)
    if title == "Sugary Sprinkles":
        return 100.0                      # fallback heal; Splash is better
    if title == "Sweet Splash":
        return _ko(500.0 + 100, 100)
    if title == "Adornment":
        return 650.0                      # mass bench acceleration
    if title == "G-Max Whisk":
        damage = 60 * energy
        if opp_left is not None and 0 < opp_left <= damage:
            return 1500.0 + damage         # fold the Active and strip
        return 300.0                       # never strip for mere damage
    if title == "Psylaser":
        foldable = any(0 < ctx.hp_left(p) <= 120
                       for p in ctx.in_play(ctx.opp))
        return 1100.0 if foldable else 350.0
    return base


def _sr_energy_target_score(ctx: StrategyContext, target) -> float:
    """Where a Psychic Energy attach lands: power the hungriest body, keep
    the Active fed first, spread away from anyone already satisfied."""
    name = ctx.name(target)
    need = SR_NEED.get(name)
    if need is None:
        return 60.0                       # Crobat V: don't waste it
    have = ctx.energy_attached(target)
    score = 500.0 if target is ctx.active() else 380.0
    if have >= need:
        score -= 250.0                    # satisfied: spread to someone else
    else:
        score += 20.0 * (need - have)
    return score


def _sr_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _sr_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            return 150.0                   # Psychic Energy only, all equal
        if target.owning_player_id == ctx.me:
            return promotion_score(ctx, target, attackers=SR_ATTACKERS)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return _sr_energy_target_score(ctx, target)
    if description == "EvolvePokemonPlayAbility":
        if name == "Shadow Rider Calyrex VMAX":
            if target is ctx.active():
                return 10.0
            return 8.0 if ctx.energy_attached(target) >= 2 else 6.0
        if name == "Alcremie VMAX":
            return 8.0 if target is ctx.active() else 6.0
        return 0.0
    if description == "DefaultToolPlayAbility":       # Air Balloon
        target_name = ctx.name(target)
        score = 8.0 if target_name in _SR_SUPPORT else 6.0
        if target is ctx.active():
            score += 10.0
        if target_name.endswith("VMAX"):
            score += 2.0
        return score
    return 0.0


def _sr_search_score(card, ctx: StrategyContext) -> float:
    return _sr_value(ctx.name(card), ctx, in_hand=False)


def _sr_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote the ready attacker;
    - opponent "new Active" (Boss) -> gust value;
    - Psylaser / Astral Barrage targets -> fold first, dent second;
    - energy attaches -> the ladder, then the energy itself;
    - hand discards -> dump the least valuable card.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return promotion_score(ctx, card, attackers=SR_ATTACKERS)
    if not mine and "new Active" in text:
        return _sr_gust(ctx, card)
    if not mine and ("take" in text or "damage" in text):
        return _sr_snipe(ctx, card, 120)          # Psylaser
    if not mine and "opponent's" in text:
        return _sr_snipe(ctx, card, 50)           # Astral Barrage
    if mine and ("attach it to" in text or "attach the Energy to" in text):
        return _sr_energy_target_score(ctx, card)
    if mine and "attach" in text:
        return 100.0                             # pick the energy itself
    if mine and "into your hand" in text:
        return _sr_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        return -_sr_value(name, ctx, in_hand=True)
    return 0.0


SHADOW_RIDER = {
    "allow_action": _sr_allow,
    "action_score": _sr_action_score,
    "attack_score": _sr_attack_score,
    "target_score": _sr_target_score,
    "search_score": _sr_search_score,
    "pick_score": _sr_pick,
}


# ----------------------------------------------------------------------
# Corviknight VMAX / Bronzong  (deck key: 'Bronzor')
#
# Corviknight VMAX is the primary attacker (flat 240, free retreat, but
# G-Max Hurricane self-locks the following turn -- so the brain swaps to a
# second attacker on locked turns).  The discard pile is the energy bank:
# Metal Saucer loads the bench, Metal Transfer feeds the empty Active,
# Cheryl dumps energy back into the bank.  Zacian V is the backup puncher.

CV_ATTACKERS = {"Corviknight VMAX", "Corviknight V", "Zacian V"}
CV_BENCH_ORDER = ["Corviknight V", "Bronzor", "Zacian V"]
CV_EVOLVE_ORDER = ["Corviknight VMAX", "Bronzong"]
CV_ABILITY_ORDER = ["Metal Transfer", "Crystal Cave"]
CV_NEED = {"Corviknight VMAX": 3, "Corviknight V": 3, "Zacian V": 3}
_CV_LOCK_TITLES = {"Corviknight VMAX": "G-Max Hurricane",
                   "Corviknight V": "Sky Hurricane",
                   "Zacian V": "Brave Blade"}
_CV_EVOLUTIONS = ("Corviknight VMAX", "Bronzong")
_CV_REPEATABLE = {
    "Professor's Research", "Marnie", "Quick Ball", "Great Ball", "Switch",
    "Metal Saucer", "Evolution Incense", "Big Charm",
}


def _cv_output(ctx: StrategyContext, pokemon) -> int:
    """Best damage `pokemon` could deal right now; 0 when it is locked or
    unpowered (self-locks make a full-energy body dead weight for a turn)."""
    if pokemon is None:
        return 0
    name = ctx.name(pokemon)
    have = ctx.energy_attached(pokemon)
    if name == "Corviknight VMAX":
        if have < 3 or ctx.attack_locked(pokemon, "G-Max Hurricane"):
            return 0
        return 240
    if name == "Corviknight V":
        if have >= 3 and not ctx.attack_locked(pokemon, "Sky Hurricane"):
            return 190
        return 30 if have >= 1 else 0        # Clutch never locks
    if name == "Zacian V":
        if have >= 3 and not ctx.attack_locked(pokemon, "Brave Blade"):
            return 230
        return 0
    if name == "Bronzong":
        return 70 if have >= 3 else 0
    return 0                                # Bronzor is setup, not a puncher


def _cv_strike_damage(ctx: StrategyContext) -> int:
    return _cv_output(ctx, ctx.active())


def _cv_gust_window(ctx: StrategyContext) -> List:
    damage = _cv_strike_damage(ctx)
    if damage <= 0:
        return []
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= damage]


def _cv_gust(ctx: StrategyContext, pokemon) -> float:
    damage = _cv_strike_damage(ctx)
    left = ctx.hp_left(pokemon)
    if damage > 0 and 0 < left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    return 500.0 + dealt if dealt > 0 else 0.0


def _cv_locked(ctx: StrategyContext, pokemon) -> bool:
    """A body whose only real attack is self-locked right now."""
    title = _CV_LOCK_TITLES.get(ctx.name(pokemon))
    if title is None:
        return False
    if ctx.name(pokemon) == "Corviknight V":
        return False                        # Clutch (1 energy) never locks
    return ctx.attack_locked(pokemon, title)


def _cv_promote(ctx: StrategyContext, pokemon) -> float:
    if _cv_locked(ctx, pokemon):
        return 0.0                         # locked body can't swing this turn
    return promotion_score(ctx, pokemon, attackers=CV_ATTACKERS)


def _cv_bench_can_attack(ctx: StrategyContext) -> bool:
    return any(_cv_output(ctx, p) > 0 for p in ctx.bench())


def _cv_switch_ok(ctx: StrategyContext) -> bool:
    """Switch: unsticks a body that can't attack, or preserves a heavily
    damaged attacker when a fresh one can swing.  Never waste it early."""
    active = ctx.active()
    if active is None:
        return False
    if _cv_output(ctx, active) <= 0:
        return _cv_bench_can_attack(ctx)
    if ctx.damage_on(active) >= 120:
        return _cv_bench_can_attack(ctx)
    return False


def _cv_retreat_ok(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None:
        return False
    active_dmg = _cv_output(ctx, active)
    bench_best = max((_cv_output(ctx, p) for p in ctx.bench()), default=0)
    if bench_best <= 0:
        return False
    if active_dmg <= 0:
        return True                        # locked / unpowered: swap in a puncher
    if ctx.damage_on(active) >= 120:
        return True                        # preserve the attacker
    return bench_best >= active_dmg + 60   # only when clearly better


def _cv_transfer_ok(ctx: StrategyContext) -> bool:
    """Metal Transfer: the engine's source pick is Active-first, so only
    fire it when the Active holds nothing and a real attacker wants energy
    (one bench -> Active move, then the gate closes: no ping-pong)."""
    active = ctx.active()
    if active is None:
        return False
    if ctx.name(active) not in CV_NEED:
        return False                       # don't feed utility bodies
    if ctx.energy_attached(active) > 0:
        return False                       # source would drain the Active
    return sum(ctx.energy_attached(p) for p in ctx.bench()) > 0


def _cv_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    deck = ctx.deck_size()
    if name == "Professor's Research":
        return ctx.hand_size() <= 5 and deck > 10
    if name == "Marnie":
        # hand returns to the deck bottom, so no deck runway needed
        return ctx.hand_size() <= 5 or ctx.hand_size(ctx.opp) >= 6
    if name == "Zinnia's Resolve":
        return len(ctx.in_play(ctx.opp)) >= 4 and deck > 7
    if name in ("Quick Ball", "Great Ball", "Evolution Incense"):
        return deck > 5
    if name == "Cheryl":
        # heal only when a big chunk of damage actually matters
        return any(ctx.damage_on(p) >= 100 for p in ctx.in_play()
                   if ctx.name(p) in _CV_EVOLUTIONS)
    if name == "Boss's Orders":
        if _cv_strike_damage(ctx) <= 0:
            return False                   # can't swing this turn anyway
        if _cv_gust_window(ctx):
            return True
        return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
    if name == "Switch":
        return _cv_switch_ok(ctx)
    if name == "Big Charm":
        return any(ctx.name(p) in CV_ATTACKERS for p in ctx.in_play())
    if description == "DefaultStadiumPlayAbility" and name == "Crystal Cave":
        return not ctx.opponent_stadium_is("Crystal Cave")
    if description == "BaseRetreat":
        return _cv_retreat_ok(ctx)
    if description == "UsePokemonAbility":
        if name == "Metal Transfer":
            return _cv_transfer_ok(ctx)
        if name == "Crystal Cave":
            return True                    # engine gate: one of ours is hurt
        if name == "Intrepid Sword":
            return False                   # turn-ender: never over real plays
        return False
    return True


def _cv_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational value of a card: fills the missing setup piece first."""
    hand = set(ctx.hand_names())
    play = set(ctx.in_play_names())
    seen = hand | play
    board = ctx.in_play()
    v_count = sum(1 for p in board if ctx.name(p) == "Corviknight V")
    metal_in_hand = sum(1 for n in ctx.hand_names()
                        if n in ("Metal Energy", "Coating Metal Energy"))
    metal_in_discard = sum(1 for n in ctx.discard_names()
                           if n in ("Metal Energy", "Coating Metal Energy"))
    bronze = any(n in ("Bronzor", "Bronzong") for n in seen)

    # -- Pokemon gap pieces (searches + hand planning) --------------------
    if name == "Corviknight V":
        v = 35.0 if v_count == 0 else (25.0 if v_count < 3 else 8.0)
    elif name == "Corviknight VMAX":
        if "Corviknight VMAX" in seen:
            v = 10.0
        elif "Corviknight V" in seen:
            v = 35.0
        else:
            v = 6.0
    elif name == "Bronzor":
        if not bronze:
            v = 30.0
        elif "Bronzong" not in seen:
            v = 15.0
        else:
            v = 7.0
    elif name == "Bronzong":
        can_evolve = any(ctx.name(p) == "Bronzor" for p in board)
        v = 30.0 if can_evolve and "Bronzong" not in seen else 7.0
    elif name == "Zacian V":
        v = 18.0 if "Zacian V" not in seen else 6.0
    elif name == "Metal Energy":
        if metal_in_hand == 0:
            v = 26.0
        elif metal_in_hand == 1:
            v = 20.0
        else:
            v = 12.0
    elif name == "Coating Metal Energy":
        v = 22.0 if metal_in_hand == 0 else 14.0

    # -- Supporters / items ------------------------------------------------
    elif name == "Professor's Research":
        v = 30.0
    elif name == "Marnie":
        v = 24.0 if ctx.hand_size(ctx.opp) > ctx.hand_size() else 18.0
    elif name == "Zinnia's Resolve":
        v = 26.0
    elif name == "Cheryl":
        worst = max((ctx.damage_on(p) for p in ctx.in_play()
                     if ctx.name(p) in _CV_EVOLUTIONS), default=0)
        v = min(50.0, 30.0 + worst / 10.0)
    elif name == "Boss's Orders":
        if _cv_gust_window(ctx):
            v = 40.0
        elif any(ctx.damage_on(p) for p in ctx.in_play(ctx.opp)):
            v = 18.0
        else:
            v = 12.0
    elif name == "Quick Ball":
        if v_count == 0:
            v = 30.0
        elif not bronze:
            v = 26.0
        elif v_count < 2:
            v = 20.0
        elif "Zacian V" not in seen:
            v = 14.0
        else:
            v = 8.0
    elif name == "Great Ball":
        if v_count == 0 or not bronze:
            v = 18.0
        elif v_count < 2:
            v = 14.0
        else:
            v = 9.0
    elif name == "Evolution Incense":
        if "Corviknight V" in seen and "Corviknight VMAX" not in seen:
            v = 32.0
        elif any(ctx.name(p) == "Bronzor" for p in board) \
                and "Bronzong" not in seen:
            v = 26.0
        else:
            v = 8.0
    elif name == "Metal Saucer":
        v = 26.0 if metal_in_discard else 8.0
    elif name == "Switch":
        active = ctx.active()
        if active is None:
            v = 4.0
        elif _cv_output(ctx, active) <= 0:
            v = 25.0                       # unlock the bench attacker
        elif ctx.damage_on(active) >= 120 and _cv_bench_can_attack(ctx):
            v = 22.0                       # preserve the attacker
        else:
            v = 4.0
    elif name == "Crystal Cave":
        v = 18.0
    elif name == "Big Charm":
        v = 15.0
    elif name == "Ordinary Rod":
        v = 12.0
    else:
        v = 6.0

    if in_hand and name in hand and name not in _CV_REPEATABLE:
        v -= 40.0                         # a second copy adds little
    return v


def _cv_bench_score(name: str, ctx: StrategyContext) -> float:
    score = order_score(CV_BENCH_ORDER, name)
    names = set(ctx.in_play_names())
    if name == "Corviknight V":
        count = sum(1 for p in ctx.in_play() if ctx.name(p) == name)
        if count == 0:
            score += 25.0
        elif count < 3:
            score += 15.0                 # keep a replacement lined up
        else:
            score -= 15.0
        if "Corviknight VMAX" in names:
            score += 10.0                 # backup attacker behind the wall
    elif name == "Bronzor":
        if "Bronzor" not in names and "Bronzong" not in names:
            score += 30.0                 # the engine is missing entirely
        elif "Bronzong" not in names:
            score += 10.0                 # waiting to evolve
        else:
            score -= 15.0
    elif name == "Zacian V":
        score += 10.0 if "Zacian V" not in names else -15.0
    return score


def _cv_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "EvolvePokemonPlayAbility":
        return order_score(CV_EVOLVE_ORDER, name)
    if description == "DefaultEnergyPlayAbility":
        return 50.0                       # Metal / Coating: both fine
    if description == "DefaultPokemonPlayAbility":
        return _cv_bench_score(name, ctx)
    if description == "UsePokemonAbility":
        return order_score(CV_ABILITY_ORDER, name) + 5.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility",
                       "DefaultToolPlayAbility"):
        return _cv_value(name, ctx, in_hand=True)
    return 0.0


def _cv_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0        # take the KO
        return score

    if title == "G-Max Hurricane":
        return _ko(700.0 + 240, 240)
    if title == "Sky Hurricane":
        return _ko(450.0 + 190, 190)
    if title == "Clutch":
        return _ko(150.0 + 30, 30)       # poke + opp-retreat lock
    if title == "Brave Blade":
        return _ko(550.0 + 230, 230)
    if title == "Zen Headbutt":
        return _ko(120.0 + 70, 70)
    return base


def _cv_energy_target_score(ctx: StrategyContext, target) -> float:
    """Where an energy attach lands: feed the hungriest main attacker,
    keep the Active fed first, never waste energy on utility bodies."""
    name = ctx.name(target)
    need = CV_NEED.get(name)
    if need is None:
        return 55.0                       # Bronzor / Bronzong: don't waste it
    have = ctx.energy_attached(target)
    score = 500.0 if target is ctx.active() else 380.0
    if have >= need:
        score -= 250.0                    # satisfied: spread to someone else
    else:
        score += 20.0 * (need - have)
    return score


def _cv_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _cv_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            # dump the plain energy; keep Coating for its defensive text
            return 80.0 if ctx.name(target) == "Coating Metal Energy" \
                else 200.0
        if target.owning_player_id == ctx.me:
            return _cv_promote(ctx, target)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return _cv_energy_target_score(ctx, target)
    if description == "EvolvePokemonPlayAbility":
        if name == "Corviknight VMAX":
            if target is ctx.active():
                return 10.0
            return 8.0 if ctx.energy_attached(target) >= 2 else 6.0
        if name == "Bronzong":
            return 8.0
        return 0.0
    if description == "DefaultToolPlayAbility":       # Big Charm
        target_name = ctx.name(target)
        if target_name not in CV_ATTACKERS:
            return 1.0
        score = 6.0
        if target is ctx.active():
            score += 10.0
        if target_name == "Corviknight VMAX":
            score += 8.0
        elif target_name == "Corviknight V":
            score += 4.0
        return score
    return 0.0


def _cv_search_score(card, ctx: StrategyContext) -> float:
    return _cv_value(ctx.name(card), ctx, in_hand=False)


def _cv_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote an unlocked attacker;
    - opponent "new Active" (Boss) -> gust value;
    - Saucer / Metal Transfer targets -> the energy ladder;
    - hand discards -> dump the least valuable card.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return _cv_promote(ctx, card)
    if not mine and "new Active" in text:
        return _cv_gust(ctx, card)
    if mine and ("attach it to" in text or "attach the Energy to" in text
                 or "Benched Metal" in text or "move the Energy to" in text):
        return _cv_energy_target_score(ctx, card)
    if mine and "attach" in text:
        return 100.0                             # pick the energy itself
    if mine and "into your hand" in text:
        return _cv_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        return -_cv_value(name, ctx, in_hand=True)
    return 0.0


CORVIKNIGHT_BRONZONG = {
    "allow_action": _cv_allow,
    "action_score": _cv_action_score,
    "attack_score": _cv_attack_score,
    "target_score": _cv_target_score,
    "search_score": _cv_search_score,
    "pick_score": _cv_pick,
}


# ----------------------------------------------------------------------
# Eternatus VMAX  (deck key: 'Eternatus V')
#
# Main plan: fill the bench with Darkness bodies (Eternal Zone opens 8
# slots, and Dread End = 30 x darkness in play: 8 bodies = 240, 9 = 270).
# Eternatus V pokes with Power Accelerator to feed the bench, then evolves.
# Crobat V draws with Dark Asset (never waste the once-per-turn draw when
# the hand is already full).  Galarian Zigzagoon's on-play counter lands on
# the cheapest KO (counter_plan).  Boss gusts whatever current Dread End
# finishes; Switch / Bird Keeper keep the VMAX attacking; Galar Mine makes
# the opponent pay to retreat.  Hoopa (Assault Gate 90) and Sableye V
# (Crazy Claws) are threshold finishers -- Hoopa only after a Bench->Active
# move or the attack does nothing.

ET_ATTACKERS = {"Eternatus VMAX", "Eternatus V", "Sableye V", "Hoopa"}
ET_BENCH_ORDER = ["Eternatus V", "Crobat V", "Galarian Zigzagoon",
                  "Sableye V", "Hoopa"]
ET_EVOLVE_ORDER = ["Eternatus VMAX"]
# Every deck Pokemon is Darkness: the dark-only bench rule holds by itself.
ET_DARKS = {"Eternatus V", "Eternatus VMAX", "Crobat V",
            "Galarian Zigzagoon", "Sableye V", "Hoopa"}
ET_NEED = {"Eternatus VMAX": 2, "Eternatus V": 1, "Hoopa": 1,
           "Sableye V": 1}
_ET_REPEATABLE = {
    "Professor's Research", "Marnie", "Quick Ball", "Great Ball", "Switch",
    "Bird Keeper",
}


def _et_dread_end(ctx: StrategyContext) -> int:
    """Damage Dread End deals right now: 30 per Darkness body in play
    (Active included), matching the engine's count_in_play scaling."""
    return 30 * sum(1 for p in ctx.in_play() if ctx.name(p) in ET_DARKS)


def _et_output(ctx: StrategyContext, pokemon) -> int:
    """Damage `pokemon` could deal from the Active slot right now; 0 when
    unpowered (or off-entry Hoopa, whose Assault Gate fizzles)."""
    if pokemon is None:
        return 0
    name = ctx.name(pokemon)
    if name not in ET_ATTACKERS:
        return 0
    have = ctx.energy_attached(pokemon)
    if have < ctx.min_attack_cost(pokemon):
        return 0
    if name == "Eternatus VMAX":
        return _et_dread_end(ctx)
    if name == "Eternatus V":
        return 30                        # Power Accelerator poke
    if name == "Sableye V":
        if have < 2:
            return 0                      # Lode Search: utility, no damage
        opp = ctx.active(ctx.opp)
        counters = (ctx.damage_on(opp) // 10) if opp is not None else 0
        return 10 + 60 * counters         # Crazy Claws
    if name == "Hoopa":
        return 90 if ctx.entered_active(pokemon) else 0
    return 0                              # Crobat / Zigzagoon: setup


def _et_strike_damage(ctx: StrategyContext) -> int:
    return _et_output(ctx, ctx.active())


def _et_energy_hungry(ctx: StrategyContext) -> bool:
    for p in ctx.in_play():
        need = ET_NEED.get(ctx.name(p))
        if need is not None and ctx.energy_attached(p) < need:
            return True
    return False


def _et_gust_window(ctx: StrategyContext) -> List:
    damage = _et_strike_damage(ctx)
    if damage <= 0:
        return []
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= damage]


def _et_gust(ctx: StrategyContext, pokemon) -> float:
    damage = _et_strike_damage(ctx)
    left = ctx.hp_left(pokemon)
    if damage > 0 and 0 < left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    return 500.0 + dealt if dealt > 0 else 0.0


def _et_promote(ctx: StrategyContext, pokemon) -> float:
    score = promotion_score(ctx, pokemon, attackers=ET_ATTACKERS)
    if ctx.name(pokemon) == "Hoopa":
        if score <= 0 or ctx.energy_attached(pokemon) < 1:
            return 0.0
        # Entry this turn enables the 90 -- but only keep Hoopa's slot
        # when that 90 actually finishes something.
        opp = ctx.active(ctx.opp)
        if opp is None or not (0 < ctx.hp_left(opp) <= 90):
            score -= 800.0
    return score


def _et_bench_can_attack(ctx: StrategyContext) -> bool:
    for p in ctx.bench():
        if _et_output(ctx, p) > 0:
            return True
        if ctx.name(p) == "Hoopa" and ctx.energy_attached(p) >= 1:
            return True                   # a Switch this turn gives entry
    return False


def _et_switch_ok(ctx: StrategyContext) -> bool:
    """Switch: unsticks a body that can't swing, or preserves a heavily
    damaged VMAX when a fresh attacker is ready."""
    active = ctx.active()
    if active is None:
        return False
    if _et_strike_damage(ctx) <= 0:
        return _et_bench_can_attack(ctx)
    if ctx.damage_on(active) >= 150:
        return _et_bench_can_attack(ctx)
    return False


def _et_retreat_ok(ctx: StrategyContext) -> bool:
    """Last resort only: VMAX retreat is expensive (+2 under Galar Mine),
    so Retreat only fires when nothing else moves us."""
    active = ctx.active()
    if active is None:
        return False
    active_dmg = _et_strike_damage(ctx)
    bench_best = 0
    for p in ctx.bench():
        out = _et_output(ctx, p)
        if ctx.name(p) == "Hoopa" and ctx.energy_attached(p) >= 1:
            out = max(out, 90)
        bench_best = max(bench_best, out)
    if bench_best <= 0:
        return False
    if active_dmg <= 0:
        return True                       # unpowered / off-entry: swap
    if ctx.damage_on(active) >= 150:
        return True                       # preserve the VMAX
    return bench_best >= active_dmg + 60


def _et_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    deck = ctx.deck_size()
    if name == "Professor's Research":
        return ctx.hand_size() <= 5 and deck > 10
    if name == "Marnie":
        return (ctx.hand_size() <= 5 or ctx.hand_size(ctx.opp) >= 6) \
            and deck > 5
    if name in ("Quick Ball", "Great Ball", "Evolution Incense"):
        return deck > 5
    if name == "Boss's Orders":
        if _et_strike_damage(ctx) <= 0:
            return False                  # can't swing this turn anyway
        if _et_gust_window(ctx):
            return True
        return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
    if name in ("Switch", "Bird Keeper"):
        return _et_switch_ok(ctx)
    if description == "DefaultStadiumPlayAbility" and name == "Galar Mine":
        return not ctx.opponent_stadium_is("Galar Mine")
    if description == "BaseRetreat":
        return _et_retreat_ok(ctx)
    if description == "UsePokemonAttack" and name == "Hoopa":
        # entry (Bench -> Active) this turn; otherwise Assault Gate
        # fizzles and the turn passes for nothing -- fall through to
        # the retreat/switch buckets instead.
        return ctx.entered_active(ctx.active())
    return True


def _et_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational value of a card: fills the missing setup piece first."""
    hand = set(ctx.hand_names())
    play = set(ctx.in_play_names())
    seen = hand | play
    board = ctx.in_play()
    ev_count = sum(1 for p in board if ctx.name(p) == "Eternatus V")
    crobat_count = sum(1 for p in board if ctx.name(p) == "Crobat V")
    dark_in_hand = sum(1 for n in ctx.hand_names()
                       if n == "Darkness Energy")

    # -- Pokemon gap pieces (searches + hand planning) --------------------
    if name == "Eternatus V":
        v = 35.0 if ev_count == 0 else (25.0 if ev_count < 3 else 8.0)
    elif name == "Eternatus VMAX":
        if "Eternatus VMAX" in seen:
            v = 10.0
        elif "Eternatus V" in seen:
            v = 35.0
        else:
            v = 6.0
    elif name == "Crobat V":
        if "Crobat V" not in seen:
            # the draw is wasted on a full hand -- search it later
            v = 30.0 if ctx.hand_size() < 6 else 18.0
        elif ctx.hand_size() < 6 and crobat_count < 3:
            v = 24.0                      # another draw while the hand is low
        else:
            v = 8.0                       # preserve it for post-Marnie recovery
    elif name == "Galarian Zigzagoon":
        v = 22.0 if "Galarian Zigzagoon" not in seen else 9.0
    elif name == "Sableye V":
        v = 16.0 if "Sableye V" not in seen else 7.0
    elif name == "Hoopa":
        v = 15.0 if "Hoopa" not in seen else 7.0
    elif name == "Darkness Energy":
        if dark_in_hand == 0:
            v = 26.0
        elif dark_in_hand == 1:
            v = 20.0
        else:
            v = 12.0

    # -- Supporters / items ------------------------------------------------
    elif name == "Professor's Research":
        v = 30.0 if ctx.hand_size() <= 4 else 12.0
    elif name == "Marnie":
        v = 24.0 if ctx.hand_size(ctx.opp) > ctx.hand_size() else 18.0
    elif name == "Boss's Orders":
        if _et_gust_window(ctx):
            v = 40.0
        elif any(ctx.damage_on(p) for p in ctx.in_play(ctx.opp)):
            v = 18.0
        else:
            v = 12.0
    elif name == "Bird Keeper":
        if _et_strike_damage(ctx) <= 0 and _et_bench_can_attack(ctx):
            v = 30.0                      # rotate into the VMAX
        elif ctx.hand_size() <= 4:
            v = 18.0                      # supporter that draws 3
        else:
            v = 6.0
    elif name == "Switch":
        active = ctx.active()
        if active is None:
            v = 4.0
        elif _et_strike_damage(ctx) <= 0:
            v = 25.0                      # unstick the bench attacker
        elif ctx.damage_on(active) >= 150 and _et_bench_can_attack(ctx):
            v = 22.0                      # preserve the VMAX
        else:
            v = 4.0
    elif name == "Quick Ball":
        if ev_count == 0:
            v = 30.0
        elif "Crobat V" not in seen:
            v = 24.0
        elif "Galarian Zigzagoon" not in seen:
            v = 18.0
        elif ev_count < 2:
            v = 14.0
        else:
            v = 8.0
    elif name == "Great Ball":
        if "Eternatus V" in seen and "Eternatus VMAX" not in seen:
            v = 20.0
        elif "Sableye V" not in seen or "Hoopa" not in seen:
            v = 14.0
        else:
            v = 9.0
    elif name == "Evolution Incense":
        v = 32.0 if "Eternatus V" in seen and "Eternatus VMAX" not in seen \
            else 8.0
    elif name == "Galar Mine":
        v = 15.0 if not ctx.opponent_stadium_is("Galar Mine") else 0.0
    else:
        v = 6.0

    if in_hand and name in hand and name not in _ET_REPEATABLE:
        v -= 40.0                         # a second copy adds little
    return v


def _et_bench_score(name: str, ctx: StrategyContext) -> float:
    score = order_score(ET_BENCH_ORDER, name)
    names = [ctx.name(p) for p in ctx.in_play()]
    if name == "Eternatus V":
        count = names.count("Eternatus V")
        score += 25.0 if count == 0 else (15.0 if count < 3 else -15.0)
    elif name == "Crobat V":
        count = names.count("Crobat V")
        if count == 0:
            score += 30.0 if ctx.hand_size() < 6 else 12.0
        elif count < 3 and ctx.hand_size() < 6:
            score += 15.0                 # still draws (once per turn)
        else:
            score -= 20.0                 # preserve the Dark Asset recovery
    elif name == "Galarian Zigzagoon":
        # every dark body is +30 Dread End; the engine caps the bench
        score += 15.0 if names.count("Galarian Zigzagoon") == 0 else 5.0
    elif name == "Sableye V":
        score += 8.0 if "Sableye V" not in names else -15.0
    elif name == "Hoopa":
        score += 6.0 if "Hoopa" not in names else -15.0
    return score


def _et_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "EvolvePokemonPlayAbility":
        return order_score(ET_EVOLVE_ORDER, name)
    if description == "DefaultEnergyPlayAbility":
        return 50.0
    if description == "DefaultPokemonPlayAbility":
        return _et_bench_score(name, ctx)
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility"):
        return _et_value(name, ctx, in_hand=True)
    return 0.0


def _et_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0        # take the KO
        return score

    if title == "Dread End":
        damage = _et_dread_end(ctx)
        return _ko(700.0 + damage, damage)
    if title == "Power Accelerator":
        score = _ko(350.0 + 30, 30)
        if _et_energy_hungry(ctx) and \
                any(n == "Darkness Energy" for n in ctx.hand_names()):
            score += 160.0                # benching energy beats raw poke
        return score
    if title == "Dynamax Cannon":
        damage = 120
        if opp_active is not None and ctx.name(opp_active).endswith("VMAX"):
            damage = 240
        return _ko(400.0 + damage, damage)
    if title == "Crazy Claws":
        counters = (ctx.damage_on(opp_active) // 10) \
            if opp_active is not None else 0
        damage = 10 + 60 * counters
        return _ko(350.0 + damage, damage)
    if title == "Assault Gate":
        if _et_strike_damage(ctx) > 0:
            return _ko(450.0 + 90, 90)
        return 0.0
    if title == "Lode Search":
        return 30.0                       # recursion when stuck
    if title == "Venomous Fang":
        return _ko(300.0 + 70, 70)
    if title == "Surprise Attack":
        return _ko(120.0 + 30, 30)        # coin flip: last-resort poke
    return base


def _et_energy_target_score(ctx: StrategyContext, target) -> float:
    """Where an energy attach lands: feed the hungriest main attacker,
    keep the Active fed first, never waste energy on utility bodies."""
    name = ctx.name(target)
    need = ET_NEED.get(name)
    if need is None:
        return 55.0                       # Crobat / Zigzagoon: don't waste it
    have = ctx.energy_attached(target)
    score = 500.0 if target is ctx.active() else 380.0
    if have >= need:
        score -= 250.0                    # satisfied: spread to someone else
    else:
        score += 20.0 * (need - have)
    return score


def _et_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _et_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            return 200.0                  # plain dark energy: nothing to keep
        if target.owning_player_id == ctx.me:
            return _et_promote(ctx, target)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return _et_energy_target_score(ctx, target)
    if description == "EvolvePokemonPlayAbility":
        if name == "Eternatus VMAX":
            if target is ctx.active():
                return 10.0
            return 8.0 if ctx.energy_attached(target) >= 2 else 6.0
        return 0.0
    return 0.0


def _et_search_score(card, ctx: StrategyContext) -> float:
    return _et_value(ctx.name(card), ctx, in_hand=False)


def _et_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote a ready attacker (Hoopa only
      when its 90 finishes);
    - opponent "new Active" (Boss) -> current Dread End gust value;
    - Power Accelerator attach targets -> the energy ladder;
    - hand discards -> dump the least valuable card.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return _et_promote(ctx, card)
    if not mine and "new Active" in text:
        return _et_gust(ctx, card)
    if mine and ("attach it to" in text or "attach the Energy to" in text):
        return _et_energy_target_score(ctx, card)
    if mine and "attach" in text:
        return 100.0                             # pick the energy itself
    if mine and "into your hand" in text:
        return _et_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        return -_et_value(name, ctx, in_hand=True)
    return 0.0


def _et_counter_plan(candidates, count: int,
                     ctx: StrategyContext) -> Dict[str, int]:
    """Headbutt Tantrum's on-play counter: cheapest KO first, then push a
    target toward its threshold (ko_threshold_counters handles both)."""
    return ko_threshold_counters(ctx, candidates, count)


ETERNATUS_VMAX = {
    "allow_action": _et_allow,
    "action_score": _et_action_score,
    "attack_score": _et_attack_score,
    "target_score": _et_target_score,
    "search_score": _et_search_score,
    "pick_score": _et_pick,
    "counter_plan": _et_counter_plan,
}


DECK_STRATEGIES = {
    "Dragapult Inteleon": DRAGAPULT_INTELEON,
    "Rapid Strike Urshifu V": RAPID_STRIKE_URSHIFU,
    "Shadow Rider Calyrex V": SHADOW_RIDER,
    "Bronzor": CORVIKNIGHT_BRONZONG,
    "Eternatus V": ETERNATUS_VMAX,
}


def strategy_for(deck_name: Optional[str]) -> Optional[dict]:
    """The brain for a bot deck name, or None (generic AI)."""
    if not deck_name:
        return None
    return DECK_STRATEGIES.get(deck_name)


def make_context(session, player_id: str) -> StrategyContext:
    return StrategyContext(session, player_id)
