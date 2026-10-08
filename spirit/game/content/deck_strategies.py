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

    def energy_of_type(self, pokemon, type_name: str) -> int:
        """Attached energies providing `type_name` ("Fire"/"Lightning"...):
        typed costs like Rayquaza's F+L need this, a bare count lies."""
        if pokemon is None:
            return 0
        wanted = getattr(PokemonTypes, type_name.upper(), None)
        if wanted is None:
            return 0
        value = wanted.value if hasattr(wanted, "value") else wanted
        total = 0
        for child in pokemon.children:
            if not isinstance(child, EnergyEntity):
                continue
            if value in (child.get_attribute(AttrID.POKEMON_TYPES) or []):
                total += 1
        return total

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


# ----------------------------------------------------------------------
# Rayquaza VMAX / Flaaffy  (deck key: 'Rayquaza V')
#
# Main plan: Rayquaza V -> VMAX is the puncher; Max Burst costs Fire +
# Lightning and dumps EVERY attached F/L for +80 each (the engine's picker
# always takes them all), so a loaded Rayquaza swings for 180-340.  The
# discard pile is the reservoir: Flaaffy's Dynamotor re-attaches Lightning
# to the bench (once per Flaaffy per turn), Rose reloads 2 from discard on
# a small hand, and Quick Ball/Research dumping Lightning is *good*.  Fire
# is the scarce type: never feed it to the engine bodies, only to a
# Rayquaza that still needs its Fire slot.  Stormy Mountains benches the
# missing piece (Rayquaza V first, then Mareep); Ordinary Rod / Pal Pad
# recover a lost line.  Keep a benched attacker developing: the active
# dumps its energy every swing, so Switch/retreat rotate to the Flaaffy-fed
# backup instead of rebuilding from zero.

RY_ATTACKERS = {"Rayquaza VMAX", "Rayquaza V"}
RY_BENCH_ORDER = ["Rayquaza V", "Mareep", "Kricketune V"]
RY_EVOLVE_ORDER = ["Rayquaza VMAX", "Flaaffy"]
RY_UTILITY = {"Mareep", "Flaaffy", "Kricketune V"}
_RY_KEY_SUPPORTERS = {"Boss's Orders", "Rose", "Professor's Research"}
_RY_ENERGY = {"Lightning Energy", "Fire Energy"}
_RY_LINE = {"Rayquaza V", "Rayquaza VMAX", "Mareep", "Flaaffy"}
_RY_REPEATABLE = {
    "Professor's Research", "Marnie", "Quick Ball", "Level Ball", "Switch",
    "Evolution Incense",
}


def _ry_ready(ctx: StrategyContext, pokemon) -> bool:
    """Attack-ready means the TYPED cost is met; two Lightning is not a
    Max Burst (needs one of each)."""
    if pokemon is None:
        return False
    name = ctx.name(pokemon)
    if name == "Rayquaza VMAX":
        return (ctx.energy_of_type(pokemon, "Fire") >= 1
                and ctx.energy_of_type(pokemon, "Lightning") >= 1)
    if name == "Rayquaza V":
        return ctx.energy_of_type(pokemon, "Lightning") >= 1
    return False


def _ry_output(ctx: StrategyContext, pokemon) -> int:
    """Damage `pokemon` deals from the Active slot right now.  Max Burst
    always dumps all attached F/L (engine picks the full count); the V
    prefers Spiral Burst (choice button picks the Fire pool) over Dragon
    Pulse's self-mill."""
    if pokemon is None:
        return 0
    name = ctx.name(pokemon)
    if name == "Rayquaza VMAX":
        if not _ry_ready(ctx, pokemon):
            return 0
        pools = (ctx.energy_of_type(pokemon, "Fire")
                 + ctx.energy_of_type(pokemon, "Lightning"))
        return 20 + 80 * pools
    if name == "Rayquaza V":
        lightning = ctx.energy_of_type(pokemon, "Lightning")
        if lightning < 1:
            return 0
        fire = ctx.energy_of_type(pokemon, "Fire")
        if fire >= 1:
            return 20 + 80 * min(2, fire)   # Spiral Burst dumps Fire first
        return 40                            # Dragon Pulse
    return 0                                 # engine bodies never attack


def _ry_strike_damage(ctx: StrategyContext) -> int:
    return _ry_output(ctx, ctx.active())


def _ry_energy_hungry(ctx: StrategyContext) -> bool:
    return any(ctx.name(p) in RY_ATTACKERS and ctx.energy_attached(p) < 3
               for p in ctx.in_play())


def _ry_gust_window(ctx: StrategyContext) -> List:
    damage = _ry_strike_damage(ctx)
    if damage <= 0:
        return []
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= damage]


def _ry_gust(ctx: StrategyContext, pokemon) -> float:
    damage = _ry_strike_damage(ctx)
    left = ctx.hp_left(pokemon)
    if damage > 0 and 0 < left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    return 500.0 + dealt if dealt > 0 else 0.0


def _ry_promote(ctx: StrategyContext, pokemon) -> float:
    """Rank bodies for the Active slot by TYPED readiness, not energy
    count: a VMAX holding two Lightning still can't Max Burst."""
    if ctx.name(pokemon) not in RY_ATTACKERS:
        return 0.0
    score = 2000.0 if _ry_ready(ctx, pokemon) else 1000.0
    score += ctx.energy_attached(pokemon) * 10.0
    if ctx.name(pokemon).endswith("VMAX"):
        score += 2.0
    return score


def _ry_bench_can_attack(ctx: StrategyContext) -> bool:
    return any(_ry_output(ctx, p) > 0 for p in ctx.bench())


def _ry_switch_ok(ctx: StrategyContext) -> bool:
    """Switch: unsticks a body that can't swing, or rotates away from a
    heavily damaged VMAX the moment a backup is loaded."""
    active = ctx.active()
    if active is None:
        return False
    if _ry_strike_damage(ctx) <= 0:
        return _ry_bench_can_attack(ctx)
    if ctx.damage_on(active) >= 150:
        return _ry_bench_can_attack(ctx)
    return False


def _ry_retreat_ok(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None:
        return False
    active_dmg = _ry_strike_damage(ctx)
    bench_best = max((_ry_output(ctx, p) for p in ctx.bench()), default=0)
    if bench_best <= 0:
        return False
    if active_dmg <= 0:
        return True                        # empty after a dump: rotate
    if ctx.damage_on(active) >= 150:
        return True                        # preserve the VMAX
    return bench_best >= active_dmg + 60


def _ry_stormy_ok(ctx: StrategyContext) -> bool:
    """Stormy Mountains benches the missing piece: attacker first, else
    another body for the Flaaffy engine (cap the Mareep glut)."""
    names = ctx.in_play_names()
    if "Rayquaza V" not in names and "Rayquaza VMAX" not in names:
        return True
    return (names.count("Mareep") + names.count("Flaaffy")) < 3


def _ry_rod_ok(ctx: StrategyContext) -> bool:
    """Ordinary Rod only when a line piece is gone or the deck runs dry."""
    play = ctx.in_play_names()
    discard = ctx.discard_names()
    rays = sum(1 for n in play if n in ("Rayquaza V", "Rayquaza VMAX"))
    line = sum(1 for n in play if n in ("Mareep", "Flaaffy"))
    if rays == 0 and any(n in ("Rayquaza V", "Rayquaza VMAX")
                         for n in discard):
        return True
    if line < 2 and any(n in ("Mareep", "Flaaffy") for n in discard):
        return True
    if ctx.deck_size() <= 15 and any(n in _RY_ENERGY for n in discard):
        return True
    return False


def _ry_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    deck = ctx.deck_size()
    hand = set(ctx.hand_names())
    if name == "Professor's Research":
        return ctx.hand_size() <= 5 and deck > 10
    if name == "Marnie":
        return (ctx.hand_size() <= 5 or ctx.hand_size(ctx.opp) >= 6) \
            and deck > 5
    if name in ("Quick Ball", "Level Ball", "Evolution Incense"):
        return deck > 5
    if name == "Boss's Orders":
        if _ry_strike_damage(ctx) <= 0:
            return False                   # can't swing this turn anyway
        if _ry_gust_window(ctx):
            return True
        return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
    if name == "Rose":
        # Rose discards the whole hand afterward: only a small hand plus
        # energy in the reservoir make the reload worth it.
        if ctx.hand_size() > 3:
            return False
        return any(n in _RY_ENERGY for n in ctx.discard_names())
    if name == "Switch":
        return _ry_switch_ok(ctx)
    if name == "Pal Pad":
        discard = ctx.discard_names()
        return any(s in discard for s in _RY_KEY_SUPPORTERS)
    if name == "Ordinary Rod":
        return _ry_rod_ok(ctx)
    if description == "DefaultStadiumPlayAbility" and name == "Stormy Mountains":
        return not ctx.opponent_stadium_is("Stormy Mountains")
    if description == "UsePokemonAbility":
        if name == "Stormy Mountains":
            return _ry_stormy_ok(ctx)
        if name == "Azure Pulse":
            # discard-hand-draw-3 (auto-yes): only with a small hand and
            # no live Supporter -- abilities fire before trainers.
            if ctx.hand_size() > 3:
                return False
            return not any(s in hand for s in _RY_KEY_SUPPORTERS)
        return True                        # Dynamotor / Exciting Stage
    if description == "UsePokemonAttack":
        if name == "Rayquaza V":
            return deck > 14               # Dragon Pulse mills our own deck
        if name in RY_UTILITY:
            return False                   # engine bodies never swing
        return True
    if description == "BaseRetreat":
        return _ry_retreat_ok(ctx)
    return True


def _ry_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational value of a card: attacker gap first, then the engine."""
    hand = set(ctx.hand_names())
    play = set(ctx.in_play_names())
    seen = hand | play
    board = ctx.in_play()
    rays = sum(1 for p in board if ctx.name(p) in
               ("Rayquaza V", "Rayquaza VMAX"))
    mareep = sum(1 for p in board if ctx.name(p) == "Mareep")
    flaaffy = sum(1 for p in board if ctx.name(p) == "Flaaffy")
    discard = set(ctx.discard_names())

    # -- Pokemon gap pieces (searches + hand planning) --------------------
    if name == "Rayquaza V":
        v = 35.0 if rays == 0 else (25.0 if rays < 3 else 8.0)
    elif name == "Rayquaza VMAX":
        if "Rayquaza VMAX" in seen:
            v = 10.0
        elif "Rayquaza V" in seen:
            v = 35.0
        else:
            v = 6.0
    elif name == "Mareep":
        if mareep == 0:
            v = 32.0
        elif mareep + flaaffy < 4:
            v = 20.0                       # room for another Flaaffy
        else:
            v = 7.0
    elif name == "Flaaffy":
        if mareep > 0 and flaaffy == 0:
            v = 34.0                       # first engine evolution
        elif mareep > flaaffy:
            v = 24.0
        else:
            v = 7.0
    elif name == "Kricketune V":
        if "Kricketune V" in seen:
            v = 5.0
        else:
            v = 18.0 if ctx.hand_size() < 4 else 8.0
    elif name == "Lightning Energy":
        v = 6.0                            # dump-first: Flaaffy reservoir
    elif name == "Fire Energy":
        v = 30.0                           # scarce: never a free discard

    # -- Supporters / items ------------------------------------------------
    elif name == "Professor's Research":
        v = 30.0 if ctx.hand_size() <= 4 else 12.0
    elif name == "Marnie":
        v = 24.0 if ctx.hand_size(ctx.opp) > ctx.hand_size() else 18.0
    elif name == "Boss's Orders":
        if _ry_gust_window(ctx):
            v = 40.0
        elif any(ctx.damage_on(p) for p in ctx.in_play(ctx.opp)):
            v = 18.0
        else:
            v = 12.0
    elif name == "Rose":
        active = ctx.active()
        if active is not None \
                and ctx.name(active) == "Rayquaza VMAX" \
                and _ry_strike_damage(ctx) <= 0:
            v = 38.0                       # immediate reload into a swing
        elif discard & _RY_ENERGY:
            v = 20.0
        else:
            v = 8.0
    elif name == "Quick Ball":
        if rays == 0:
            v = 30.0
        elif mareep == 0:
            v = 26.0
        elif mareep + flaaffy < 4:
            v = 18.0
        elif rays < 2:
            v = 14.0
        else:
            v = 8.0
    elif name == "Level Ball":
        if mareep == 0:
            v = 30.0
        elif mareep > flaaffy:
            v = 26.0                       # evolve what is already out
        elif mareep + flaaffy < 4:
            v = 16.0
        else:
            v = 8.0
    elif name == "Evolution Incense":
        if "Rayquaza V" in seen and "Rayquaza VMAX" not in seen:
            v = 34.0
        elif mareep > flaaffy:
            v = 30.0
        else:
            v = 8.0
    elif name == "Switch":
        active = ctx.active()
        if active is None:
            v = 4.0
        elif _ry_strike_damage(ctx) <= 0:
            v = 25.0                       # rotate into the loaded backup
        elif ctx.damage_on(active) >= 150 and _ry_bench_can_attack(ctx):
            v = 22.0                       # preserve the VMAX
        else:
            v = 4.0
    elif name == "Stormy Mountains":
        v = 15.0 if _ry_stormy_ok(ctx) else 3.0
    elif name == "Air Balloon":
        v = 16.0
    elif name == "Ordinary Rod":
        v = 14.0 if _ry_rod_ok(ctx) else 4.0
    elif name == "Pal Pad":
        v = 12.0 if discard & _RY_KEY_SUPPORTERS else 4.0
    else:
        v = 6.0

    if in_hand and name in hand and name not in _RY_REPEATABLE:
        v -= 40.0                          # a second copy adds little
    return v


def _ry_energy_value(name: str, ctx: StrategyContext) -> float:
    """Which energy card to spend the turn's manual attach on."""
    if name == "Fire Energy":
        # reserved for the Rayquaza line: attach only when a ray still
        # lacks its Fire slot; otherwise hold it in hand.
        needs_fire = any(ctx.name(p) in RY_ATTACKERS
                         and ctx.energy_of_type(p, "Fire") == 0
                         for p in ctx.in_play())
        return 42.0 if needs_fire else 6.0
    if name == "Lightning Energy":
        held = ctx.hand_names().count("Lightning Energy")
        return 30.0 if held <= 1 else (26.0 if held == 2 else 20.0)
    return 6.0


def _ry_bench_score(name: str, ctx: StrategyContext) -> float:
    score = order_score(RY_BENCH_ORDER, name)
    names = [ctx.name(p) for p in ctx.in_play()]
    if name == "Rayquaza V":
        count = names.count("Rayquaza V") + names.count("Rayquaza VMAX")
        score += 25.0 if count == 0 else (10.0 if count < 3 else -15.0)
    elif name == "Mareep":
        count = names.count("Mareep")
        line = count + names.count("Flaaffy")
        if count == 0:
            score += 30.0                  # the engine is missing entirely
        elif line < 4:
            score += 15.0                  # another Flaaffy in waiting
        else:
            score -= 15.0
    elif name == "Kricketune V":
        if "Kricketune V" in names:
            score -= 15.0
        elif ctx.hand_size() < 4:
            score += 10.0                  # worth a slot when digging
        else:
            score -= 10.0
    return score


def _ry_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "EvolvePokemonPlayAbility":
        return order_score(RY_EVOLVE_ORDER, name)
    if description == "DefaultEnergyPlayAbility":
        return _ry_energy_value(name, ctx)
    if description == "DefaultPokemonPlayAbility":
        return _ry_bench_score(name, ctx)
    if description == "UsePokemonAbility":
        if name == "Dynamotor":
            return 100.0 if _ry_energy_hungry(ctx) else 70.0
        if name == "Stormy Mountains":
            return 85.0 if _ry_stormy_ok(ctx) else 0.0
        if name == "Exciting Stage":
            return 70.0
        if name == "Azure Pulse":
            return 55.0
        return 0.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility",
                       "DefaultToolPlayAbility"):
        return _ry_value(name, ctx, in_hand=True)
    return 0.0


def _ry_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0         # take the KO
        return score

    active = ctx.active()
    if title == "Max Burst":
        damage = _ry_strike_damage(ctx)
        return _ko(700.0 + damage, damage)
    if title == "Spiral Burst":
        fire = ctx.energy_of_type(active, "Fire") if active else 0
        lightning = ctx.energy_of_type(active, "Lightning") if active else 0
        if fire >= 1:
            damage = 20 + 80 * min(2, fire)   # the choice button picks Fire
        else:
            damage = 20 + 80 * min(2, lightning)
        return _ko(450.0 + damage, damage)
    if title == "Dragon Pulse":
        return _ko(320.0 + 40, 40)
    return base


def _ry_energy_target_score(ctx: StrategyContext, target,
                            energy_name: str) -> float:
    """Where an attach lands: typed slot on the Rayquaza line only, with an
    overcommit cap so the next attacker keeps room to grow into."""
    if ctx.name(target) not in RY_ATTACKERS:
        return 55.0                        # never feed the engine bodies
    is_active = target is ctx.active()
    if energy_name == "Fire Energy":
        if ctx.energy_of_type(target, "Fire") >= 1:
            return 60.0                    # slot filled: hold the spare
        return 460.0 if is_active else 360.0
    score = 500.0 if is_active else 380.0
    if ctx.energy_attached(target) >= 3:
        score -= 200.0                     # overcommit cap: feed the next
    return score


def _ry_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _ry_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            return 200.0                   # dump it all: Flaaffy refills
        if target.owning_player_id == ctx.me:
            return _ry_promote(ctx, target)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return _ry_energy_target_score(ctx, target, name)
    if description == "EvolvePokemonPlayAbility":
        if name == "Rayquaza VMAX":
            if target is ctx.active():
                return 10.0
            return 8.0 if ctx.energy_attached(target) >= 2 else 6.0
        if name == "Flaaffy":
            return 8.0
        return 0.0
    if description == "DefaultToolPlayAbility":        # Air Balloon
        target_name = ctx.name(target)
        score = 4.0
        if target is ctx.active():
            score += 10.0                  # free pivot up front
        if target_name in RY_ATTACKERS:
            score += 8.0
        return score
    return 0.0


def _ry_search_score(card, ctx: StrategyContext) -> float:
    return _ry_value(ctx.name(card), ctx, in_hand=False)


def _ry_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote by TYPED readiness;
    - Rose's "Pok\u00e9mon VMAX" target -> reload the active puncher
      (unless it is already loaded);
    - Flaaffy Dynamotor targets -> the Lightning ladder;
    - Max Burst discard -> positive (the engine takes them all anyway);
    - hand discards -> dump Lightning Energy first (the reservoir).
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return _ry_promote(ctx, card)
    if not mine and "new Active" in text:
        return _ry_gust(ctx, card)
    if mine and "VMAX" in text:
        # Rose: "Choose your Pok\u00e9mon VMAX"
        score = 1000.0 if card is ctx.active() else 800.0
        if ctx.energy_attached(card) >= 4:
            score -= 400.0                 # already loaded: feed the other
        return score
    if mine and ("Discard any amount" in text):
        return 100.0                       # Max Burst: all of them go
    if mine and ("attach it to" in text or "attach the Energy to" in text):
        return _ry_energy_target_score(ctx, card, "Lightning Energy")
    if mine and "attach" in text:
        return 100.0                       # pick the energy itself
    if mine and "into your hand" in text:
        return _ry_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        return -_ry_value(name, ctx, in_hand=True)
    return 0.0


RAYQUAZA_VMAX_FLAFFY = {
    "allow_action": _ry_allow,
    "action_score": _ry_action_score,
    "attack_score": _ry_attack_score,
    "target_score": _ry_target_score,
    "search_score": _ry_search_score,
    "pick_score": _ry_pick,
}


# ----------------------------------------------------------------------
# Suicune V / Ludicolo  (deck key: 'Sobble (suicune-ludicolo)')
#
# Main plan: Suicune V is the puncher and the first meaningful Water Energy
# investment; Blizzard Rondo costs Water + Colorless and hits 20 + 20 for
# every Benched Pokemon on BOTH sides, so filling our own bench is offense.
# The Sobble -> Drizzile -> Inteleon line is the consistency engine (Shady
# Dealings searches); searches are spent on real gaps, never wasted.
# Ludicolo's on-evolve Enthusiastic Dance adds +100 to a Basic attacker
# THIS turn only, so the Lombre -> Ludicolo evolve is gated on a window:
# the active Suicune is ready to swing and (ideally) the boost unlocks a
# KO.  Lotad is NOT auto-benched: bench space is kept for the backup
# attacker and, when the line pieces are held, for the single Ludicolo.
# Melony/Raihan reload a dead attacker after losses; Boss/Escape Rope
# move KO-range bodies into Rondo's reach; Scoop Up Net reuses search
# bodies (Pokemon V can't be netted).  Cape of Toughness hardens the
# active attacker.

SU_ATTACKERS = {"Suicune V"}
_SU_ENERGY = {"Water Energy", "Capture Energy"}
_SU_ATTACKER = "Suicune V"
_SU_ATTACK = "Blizzard Rondo"
_SU_LINE = {"Suicune V", "Sobble", "Drizzile", "Inteleon",
            "Lotad", "Lombre", "Ludicolo"}
_SU_REPEATABLE = {
    "Professor's Research", "Marnie", "Quick Ball", "Level Ball",
    "Evolution Incense", "Boss's Orders", "Melony", "Raihan",
    "Capacious Bucket", "Scoop Up Net", "Rare Candy", "Escape Rope",
    "Cape of Toughness", "Water Energy", "Capture Energy",
}


def _su_attackers(ctx: StrategyContext) -> List:
    return [p for p in ctx.in_play() if ctx.name(p) == "Suicune V"]


def _su_ready(ctx: StrategyContext, pokemon) -> bool:
    """Blizzard Rondo typed cost: one Water plus a second unit."""
    if pokemon is None or ctx.name(pokemon) != "Suicune V":
        return False
    return (ctx.energy_of_type(pokemon, "Water") >= 1
            and ctx.energy_attached(pokemon) >= 2)


def _su_dance_bonus(ctx: StrategyContext, pokemon) -> int:
    """Enthusiastic Dance rider: +100 this turn for a Basic attacker vs the
    opponent's Active (read from turn_state; expires at begin_turn)."""
    try:
        state = ctx.session.turn_state
        mods = state.damage_modifiers
        turn = state.turn_number
    except Exception:
        return 0
    total = 0
    for mod in mods:
        if getattr(mod, "player_id", None) != ctx.me:
            continue
        expires = getattr(mod, "expires_after_turn", None)
        if expires is not None and expires < turn:
            continue
        if getattr(mod, "source_entity_id", None) is not None:
            if mod.source_entity_id != getattr(pokemon, "entity_id", None):
                continue
        if getattr(mod, "attack_title", None):
            continue                      # title-gated: not ours to count
        if getattr(mod, "source_predicate", None) is not None:
            continue                      # opaque gate: don't assume it
        subtype = getattr(mod, "requires_subtype", None)
        if subtype and pokemon is not None:
            from spirit.game.data_utils import subtypes_for
            arch = getattr(pokemon, "archetype_id", None)
            if arch is not None and subtype not in subtypes_for(arch):
                continue
        total += int(getattr(mod, "amount", 0) or 0)
    return total


def _su_rondo_base(ctx: StrategyContext) -> int:
    """20 + 20 per Benched Pokemon on both sides, ready attacker only."""
    active = ctx.active()
    if not _su_ready(ctx, active):
        return 0
    return 20 + 20 * (len(ctx.bench()) + len(ctx.bench(ctx.opp)))


def _su_output(ctx: StrategyContext, pokemon) -> int:
    """Damage `pokemon`'s Blizzard Rondo deals from the Active right now."""
    if not _su_ready(ctx, pokemon):
        return 0
    return (20 + 20 * (len(ctx.bench()) + len(ctx.bench(ctx.opp)))
            + _su_dance_bonus(ctx, pokemon))


def _su_strike_damage(ctx: StrategyContext) -> int:
    return _su_output(ctx, ctx.active())


def _su_energy_hungry(ctx: StrategyContext) -> bool:
    attackers = _su_attackers(ctx)
    if not attackers:
        return True
    return any(ctx.energy_attached(p) < 2 or ctx.energy_of_type(p, "Water") < 1
               for p in attackers)


def _su_water_left(ctx: StrategyContext) -> int:
    """6 Water Energy minus the copies we can already see (hand, discard,
    attached): what a Capacious Bucket can still dig out of the deck."""
    used = (ctx.hand_names().count("Water Energy")
            + ctx.discard_names().count("Water Energy")
            + sum(ctx.energy_of_type(p, "Water") for p in ctx.in_play()))
    return max(0, 6 - used)


def _su_water_in_discard(ctx: StrategyContext) -> bool:
    return "Water Energy" in ctx.discard_names()


def _su_tool_free(ctx: StrategyContext, pokemon) -> bool:
    if pokemon is None:
        return False
    return not any(
        c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
        for c in (getattr(pokemon, "children", None) or [])
    )


def _su_dance_window(ctx: StrategyContext) -> bool:
    """A Basic puncher is attack-ready in the Active right now: evolving
    Ludicolo this turn actually spends the on-evolve boost."""
    return _su_ready(ctx, ctx.active())


def _su_dance_unlocks(ctx: StrategyContext) -> bool:
    """+100 turns a surviving active into a KO (base < hp <= base + 100)."""
    if not _su_dance_window(ctx):
        return False
    opp = ctx.active(ctx.opp)
    if opp is None:
        return False
    base = _su_rondo_base(ctx)
    left = ctx.hp_left(opp)
    return 0 < base < left <= base + 100


def _su_gust_window(ctx: StrategyContext) -> List:
    damage = _su_strike_damage(ctx)
    if damage <= 0:
        return []
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= damage]


def _su_gust(ctx: StrategyContext, pokemon) -> float:
    damage = _su_strike_damage(ctx)
    left = ctx.hp_left(pokemon)
    if damage > 0 and 0 < left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    return 500.0 + dealt if dealt > 0 else 0.0


def _su_snipe(ctx: StrategyContext, pokemon) -> float:
    """Quick Shooting counters / Aqua Bullet bench pick: finish first."""
    left = ctx.hp_left(pokemon)
    if 0 < left <= 20:
        return 1000.0                      # 2 counters close the KO
    dealt = ctx.damage_on(pokemon)
    if dealt > 0:
        return 600.0 + dealt
    return 300.0 + ctx.prize_value(pokemon) * 50.0


def _su_promote(ctx: StrategyContext, pokemon) -> float:
    """New-Active ranking: the ready puncher first, then the developing one."""
    name = ctx.name(pokemon)
    if name == "Suicune V":
        score = 2000.0 if _su_ready(ctx, pokemon) else 1200.0
        return score + ctx.energy_attached(pokemon) * 10.0
    if name == "Ludicolo":
        return 900.0
    if name == "Inteleon":
        return 700.0
    if name == "Drizzile":
        return 500.0
    if name == "Sobble":
        return 300.0
    if name in ("Lotad", "Lombre"):
        return 200.0
    return 0.0


def _su_scoop(ctx: StrategyContext, pokemon) -> float:
    """Scoop Up Net target: heal the wounded, reuse a used search body."""
    if pokemon is None:
        return 0.0
    if ctx.name(pokemon) == "Suicune V":
        return 0.0                         # engine excludes Pokemon V anyway
    dealt = ctx.damage_on(pokemon)
    if pokemon is ctx.active():
        return 600.0 if ctx.bench() else -999.0  # empty bench = we lose
    if dealt >= 60:
        return 1200.0                      # nearly dead: bounce and replay
    if ctx.name(pokemon) in ("Drizzile", "Inteleon"):
        return 500.0 if dealt == 0 else 700.0    # fire Shady Dealings again
    if dealt > 0:
        return 400.0 + dealt
    return 100.0


def _su_scoop_ok(ctx: StrategyContext) -> bool:
    if not ctx.bench():
        return False                       # netting the active would lose
    hand = set(ctx.hand_names())
    for p in ctx.in_play():
        if ctx.name(p) == "Suicune V":
            continue
        if ctx.damage_on(p) >= 40:
            return True
    if len(ctx.bench()) >= 5 and hand & {"Drizzile", "Inteleon"}:
        return True                        # free a slot to replay a search
    return False


def _su_rope_ok(ctx: StrategyContext) -> bool:
    """Escape Rope: rotate into a ready puncher, or gust a KO the active
    itself denies."""
    active = ctx.active()
    if active is None:
        return False
    damage = _su_strike_damage(ctx)
    if damage <= 0:
        return any(_su_ready(ctx, p) for p in ctx.bench())
    if 0 < ctx.hp_left(active) <= damage:
        return False                       # current target already dies
    opp_left = ctx.hp_left(ctx.active(ctx.opp)) \
        if ctx.active(ctx.opp) is not None else 0
    if 0 < opp_left <= damage:
        return False                       # no reason to trade it away
    return any(0 < ctx.hp_left(p) <= damage for p in ctx.bench(ctx.opp))


def _su_retreat_ok(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None:
        return False
    bench_ready = any(_su_ready(ctx, p) for p in ctx.bench())
    if not bench_ready:
        return False
    if _su_strike_damage(ctx) <= 0:
        return True                        # the active can't swing: rotate
    if ctx.damage_on(active) >= 120:
        return True                        # preserve the wounded puncher
    return False


def _su_lotad_ok(ctx: StrategyContext) -> bool:
    """Bench Lotad only when the line can actually be walked, and never
    out of slots for the backup attacker."""
    hand = set(ctx.hand_names())
    if not (hand & {"Lombre", "Ludicolo", "Evolution Incense"}):
        return False
    names = ctx.in_play_names()
    if names.count("Lotad") + names.count("Lombre") + names.count("Ludicolo"):
        return False                       # one Ludicolo line is enough
    free = 5 - len(ctx.bench())
    if names.count("Suicune V") < 2:
        return free >= 2                   # keep a slot for the backup
    return free >= 1


def _su_candy_pairs(ctx: StrategyContext) -> List:
    """(basic in play, Stage 2 in hand) couples Rare Candy can join."""
    hand = set(ctx.hand_names())
    names = set(ctx.in_play_names())
    pairs = []
    if "Sobble" in names and "Inteleon" in hand:
        pairs.append(("Sobble", "Inteleon"))
    if "Lotad" in names and "Ludicolo" in hand:
        pairs.append(("Lotad", "Ludicolo"))
    return pairs


def _su_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    deck = ctx.deck_size()
    if description == "DefaultPokemonPlayAbility":
        if name == "Lotad":
            return _su_lotad_ok(ctx)
        return True
    if description == "EvolvePokemonPlayAbility":
        if name == "Ludicolo":
            # never spend the on-evolve boost while the puncher can't swing
            if _su_dance_window(ctx):
                return True
            active = ctx.active()
            return active is not None and ctx.name(active) == "Lombre"
        return True
    if description == "UsePokemonAbility":
        return name in ("Fleet-Footed", "Quick Shooting")
    if description == "UseTrainerCard":
        if name == "Professor's Research":
            return ctx.hand_size() <= 5 and deck > 10
        if name == "Marnie":
            return (ctx.hand_size() <= 5
                    or ctx.hand_size(ctx.opp) >= 6) and deck > 5
        if name in ("Quick Ball", "Level Ball", "Evolution Incense"):
            return deck > 5
        if name == "Capacious Bucket":
            return _su_energy_hungry(ctx) and _su_water_left(ctx) > 0
        if name == "Boss's Orders":
            if _su_strike_damage(ctx) <= 0:
                return False               # no swing this turn, no gust
            if _su_gust_window(ctx):
                return True
            return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
        if name == "Melony":
            if not _su_water_in_discard(ctx):
                return False
            return _su_energy_hungry(ctx) or ctx.hand_size() <= 4
        if name == "Rare Candy":
            return bool(_su_candy_pairs(ctx))
        if name == "Scoop Up Net":
            return _su_scoop_ok(ctx)
        if name == "Escape Rope":
            return _su_rope_ok(ctx)
        if name == "Cape of Toughness":
            return any(ctx.name(p) == "Suicune V" and _su_tool_free(ctx, p)
                       for p in ctx.in_play())
        return True
    if description == "UsePokemonAttack":
        active = ctx.active()
        # rotating into a ready puncher beats weak chip; retreat can pay
        # because the body sits on exactly one energy (its retreat cost)
        can_rotate = (active is not None
                      and ctx.energy_attached(active) >= 1
                      and _su_retreat_ok(ctx))
        if name in ("Sobble", "Lotad"):
            if len(ctx.bench()) >= 5:
                return False               # bench full: nothing to fill
            if can_rotate:
                return False               # rotate into the ready puncher
            return True
        if name in ("Drizzile", "Lombre"):
            return not can_rotate          # weak chip only when stuck
        return True                        # Suicune V / Inteleon / Ludicolo
    if description == "BaseRetreat":
        return _su_retreat_ok(ctx)
    return True


def _su_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational worth: attacker first, then the engine, then the plays
    that solve a real problem (mirrors the strategy priority chain)."""
    hand = ctx.hand_names()
    handset = set(hand)
    play = ctx.in_play_names()
    attackers = len(_su_attackers(ctx))
    unevolved = play.count("Sobble")

    # -- Pokemon gap pieces ------------------------------------------------
    if name == "Suicune V":
        v = 95.0 if attackers == 0 else (55.0 if attackers < 3 else 10.0)
    elif name == "Sobble":
        depth = unevolved + play.count("Drizzile") + play.count("Inteleon")
        v = 45.0 if depth < 2 else (25.0 if depth < 4 else 6.0)
    elif name == "Drizzile":
        if unevolved == 0:
            v = 6.0
        elif "Drizzile" in handset:
            v = 12.0                       # already holding the search
        else:
            v = 80.0 if unevolved > play.count("Drizzile") else 40.0
    elif name == "Inteleon":
        v = 60.0 if play.count("Drizzile") > play.count("Inteleon") else 6.0
    elif name == "Lotad":
        v = 40.0 if handset & {"Lombre", "Ludicolo"} else 8.0
    elif name == "Lombre":
        v = 55.0 if "Lotad" in play else 6.0
    elif name == "Ludicolo":
        v = 60.0 if ("Lotad" in play or "Lombre" in play) else 6.0

    # -- Energy ------------------------------------------------------------
    elif name == "Water Energy":
        v = 85.0 if _su_energy_hungry(ctx) else 40.0
    elif name == "Capture Energy":
        v = 35.0                           # setup filler, never a plan

    # -- Supporters / items ------------------------------------------------
    elif name == "Melony":
        if _su_energy_hungry(ctx):
            v = 90.0                       # attach + draw 3 into the gap
        elif ctx.hand_size() <= 4:
            v = 60.0                       # the draw alone
        else:
            v = 45.0                       # save the Supporter slot
    elif name == "Raihan":
        v = 75.0                           # attach + search, post-KO only
    elif name == "Boss's Orders":
        if _su_gust_window(ctx):
            v = 95.0                       # a KO walks into Rondo's range
        elif any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp)):
            v = 45.0
        else:
            v = 15.0
    elif name == "Professor's Research":
        v = 80.0 if ctx.hand_size() <= 4 else (
            55.0 if ctx.hand_size() <= 6 else 20.0)
    elif name == "Marnie":
        v = 70.0 if ctx.hand_size(ctx.opp) >= 6 else (
            50.0 if ctx.hand_size() <= 4 else 30.0)
    elif name == "Evolution Incense":
        if unevolved > play.count("Drizzile") and "Drizzile" not in handset:
            v = 75.0
        elif play.count("Drizzile") > play.count("Inteleon") \
                and "Inteleon" not in handset:
            v = 70.0
        elif "Lotad" in play and "Ludicolo" not in handset:
            v = 65.0
        elif "Lotad" in play and "Lombre" not in handset:
            v = 60.0
        else:
            v = 12.0
    elif name == "Level Ball":
        if unevolved > play.count("Drizzile") and "Drizzile" not in handset:
            v = 80.0                       # the engine's first search
        elif (unevolved + play.count("Drizzile")) < 4 \
                and "Sobble" not in handset:
            v = 65.0
        elif "Lotad" in play and "Lombre" not in handset:
            v = 55.0
        else:
            v = 10.0
    elif name == "Quick Ball":
        if attackers == 0 and "Suicune V" not in handset:
            v = 85.0                       # fetch the puncher
        elif unevolved == 0 and "Sobble" not in handset:
            v = 60.0
        else:
            v = 15.0
    elif name == "Capacious Bucket":
        v = 85.0 if (_su_energy_hungry(ctx) and _su_water_left(ctx) > 0) \
            else 20.0
    elif name == "Rare Candy":
        v = 70.0 if _su_candy_pairs(ctx) else 8.0
    elif name == "Scoop Up Net":
        v = 68.0 if _su_scoop_ok(ctx) else 15.0
    elif name == "Escape Rope":
        v = 68.0 if _su_rope_ok(ctx) else 18.0
    elif name == "Cape of Toughness":
        active = ctx.active()
        v = 60.0 if (active is not None and ctx.name(active) == "Suicune V"
                     and _su_tool_free(ctx, active)) else 15.0
    else:
        v = 6.0

    if in_hand and name in handset and name not in _SU_REPEATABLE:
        v -= 40.0                          # a second copy adds little
    return v


def _su_energy_value(name: str, ctx: StrategyContext) -> float:
    """Which energy card to spend the turn's manual attach on."""
    if name == "Water Energy":
        return 120.0 if _su_energy_hungry(ctx) else 60.0
    if name == "Capture Energy":
        if "Water Energy" in ctx.hand_names():
            return 40.0                    # the real slot waits for Water
        if _su_energy_hungry(ctx):
            return 90.0                    # it is the only unit we have
        return 40.0
    return 6.0


def _su_energy_target_score(ctx: StrategyContext, target,
                            energy_name: str) -> float:
    """Where an attach lands: the puncher's slots first, engine never."""
    if ctx.name(target) not in SU_ATTACKERS:
        if not _su_attackers(ctx):
            return 300.0 if target is ctx.active() else 150.0
        return 50.0                        # never feed the engine bodies
    score = 500.0 if target is ctx.active() else 350.0
    water = ctx.energy_of_type(target, "Water")
    have = ctx.energy_attached(target)
    if water < 1:
        score += 250.0                     # the typed slot comes first
    elif have < 2:
        score += 120.0                     # second unit completes the cost
    else:
        score -= 260.0                     # loaded: the backup grows instead
    return score


def _su_bench_score(name: str, ctx: StrategyContext) -> float:
    names = ctx.in_play_names()
    free = 5 - len(ctx.bench())
    attackers = names.count("Suicune V")
    lotad_line = names.count("Lotad") + names.count("Lombre") \
        + names.count("Ludicolo")
    hand = set(ctx.hand_names())
    want_lotad = lotad_line == 0 and bool(
        hand & {"Lombre", "Ludicolo", "Evolution Incense"})
    if name == "Suicune V":
        if attackers == 0:
            return 700.0                   # the puncher takes the bench
        if attackers < 3:
            return 450.0
        return 40.0
    if name == "Sobble":
        depth = names.count("Sobble") + names.count("Drizzile") \
            + names.count("Inteleon")
        if depth == 0:
            score = 600.0
        elif depth < 3:
            score = 420.0
        elif depth < 4:
            score = 300.0
        else:
            score = 60.0
        # slot discipline: keep room for the backup attacker / the line
        if attackers < 2 and free <= 1:
            score = min(score, 120.0)
        elif want_lotad and free <= 2:
            score = min(score, 200.0)
        return score
    if name == "Lotad":
        if lotad_line > 0 or not want_lotad:
            return 0.0
        if attackers < 2 and free <= 1:
            return 0.0
        return 280.0
    return 0.0


def _su_evolve_score(name: str, ctx: StrategyContext) -> float:
    if name == "Drizzile":
        return 800.0                       # Shady Dealings consistency
    if name == "Inteleon":
        return 650.0                       # search-2 or Quick Shooting
    if name == "Lombre":
        return 500.0                       # prep step, no same-turn payoff
    if name == "Ludicolo":
        return 950.0 if _su_dance_unlocks(ctx) else 700.0
    return 0.0


def _su_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "DefaultPokemonPlayAbility":
        return _su_bench_score(name, ctx)
    if description == "DefaultEnergyPlayAbility":
        return _su_energy_value(name, ctx)
    if description == "EvolvePokemonPlayAbility":
        return _su_evolve_score(name, ctx)
    if description == "UsePokemonAbility":
        if name == "Fleet-Footed":
            return 75.0                    # free draw, always live
        if name == "Quick Shooting":
            opp = ctx.in_play(ctx.opp)
            if any(0 < ctx.hp_left(p) <= 20 for p in opp):
                return 90.0                # a counter closes a KO
            if any(ctx.damage_on(p) > 0 for p in opp):
                return 65.0
            return 45.0
        return 0.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility",
                       "DefaultToolPlayAbility"):
        return _su_value(name, ctx, in_hand=True)
    return 0.0


def _su_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0         # take the KO
        return score

    if title == "Blizzard Rondo":
        damage = _su_strike_damage(ctx)
        if damage <= 0:
            return 0.0
        return _ko(800.0 + damage, damage)
    if title == "Wave Splash":
        return _ko(450.0 + 120, 120)
    if title == "Aqua Bullet":
        return _ko(420.0 + 120, 120)
    if title == "Keep Calling":
        return 350.0 if len(ctx.bench()) < 5 else 0.0
    if title == "Call for Family":
        return 400.0 if len(ctx.bench()) < 5 else 0.0
    if title == "Waterfall":
        return _ko(350.0 + 70, 70)
    if title == "Water Drip":
        return 150.0
    if title == "Rain Splash":
        return 120.0
    if title == "Double Spin":
        return 100.0
    return base


def _su_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _su_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            # dump the redundant unit first: setup filler dies before the
            # Water Energy that feeds the puncher
            return 200.0 if ctx.name(target) == "Capture Energy" else 150.0
        if target.owning_player_id == ctx.me:
            return _su_promote(ctx, target)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return _su_energy_target_score(ctx, target, name)
    if description == "DefaultToolPlayAbility":     # Cape of Toughness
        if ctx.name(target) != "Suicune V":
            return 0.0
        score = 500.0
        if target is ctx.active():
            score += 150.0
        if _su_tool_free(ctx, target):
            score += 50.0
        return score
    if description == "EvolvePokemonPlayAbility":
        if name == "Ludicolo":
            return 10.0 if target is ctx.active() else 6.0
        return 4.0 if target is ctx.active() else 2.0
    return 0.0


def _su_search_score(card, ctx: StrategyContext) -> float:
    return _su_value(ctx.name(card), ctx, in_hand=False)


def _su_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote the ready puncher;
    - opponent switch/snipe picks -> KO window, then scratch value;
    - Melony/Raihan attach targets -> the Suicune energy ladder;
    - Rare Candy's Basic/Stage 2 picks -> the candy pair worth taking;
    - Scoop Up Net -> wound first, used search bodies next;
    - hand discards -> dump the least valuable card.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return _su_promote(ctx, card)
    if not mine and "new Active" in text:
        return _su_gust(ctx, card)
    if not mine and ("opponent's" in text or "take" in text):
        return _su_snipe(ctx, card)        # Quick Shooting / Aqua Bullet
    if mine and ("attach it to" in text or "attach the Energy to" in text):
        return _su_energy_target_score(ctx, card, "")
    if mine and "attach" in text:
        return 100.0                       # pick the energy itself
    if mine and "evolve into" in text:
        # Rare Candy: "Choose a Stage 2 Pokemon to evolve into"
        if name == "Inteleon":
            return 800.0
        if name == "Ludicolo":
            if _su_dance_unlocks(ctx):
                return 950.0
            return 700.0 if _su_dance_window(ctx) else 400.0
        return 100.0
    if mine and "in play" in text:
        # Rare Candy: "Choose a Basic Pokemon in play"
        if name == "Lotad" and "Ludicolo" in ctx.hand_names():
            return 900.0                   # Lotad -> Ludicolo skips Lombre
        if name == "Sobble" and "Inteleon" in ctx.hand_names():
            return 700.0
        return 100.0
    if mine and "put into your hand" in text:
        return _su_scoop(ctx, card)        # Scoop Up Net
    if mine and "into your hand" in text:
        return _su_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        return -_su_value(name, ctx, in_hand=True)
    return 0.0


SUICUNE_LUDICOLO = {
    "allow_action": _su_allow,
    "action_score": _su_action_score,
    "attack_score": _su_attack_score,
    "target_score": _su_target_score,
    "search_score": _su_search_score,
    "pick_score": _su_pick,
}


# Charizard VSTAR / Magma Basin  (deck key: 'Charizard (charizard-vmax)')
#
# Charizard VSTAR is the boss attacker: Explosive Fire costs Fire + Fire +
# Colorless for 130, or 230 once any damage counter sits on Charizard --
# Magma Basin's self-inflicted counters and ordinary wear both feed it.
# Star Blaze is the one-per-game VSTAR Power (320): spent ONLY where the
# 230 line cannot answer (231..320 hp bodies -- VSTAR/VMAX prizes), never
# on a target Explosive Fire already handles.  Magma Basin accelerates a
# Fire Energy from the discard onto a Benched Fire Pokemon every turn
# (2 damage counters as the price, which later powers Explosive Fire);
# Raihan reloads after a loss.  One Charizard V is benched as the backup
# body; support Pokemon are benched only for their effect -- Crobat V to
# fill a small hand, Mew to dig Items, Lumineon V to fetch a missing
# Supporter -- because extra 2-prize bodies are liabilities.  Moltres is
# the emergency 1-prize attacker while the line develops.  When the
# Active Charizard is about to fall, energy and the promote slot go to
# the NEXT Charizard instead of the doomed one.

CZ_FIRE = {"Fire Energy", "Heat Fire Energy"}
CZ_SUPPORTERS = {"Professor's Research", "Marnie", "Boss's Orders",
                 "Zinnia's Resolve", "Raihan"}
CZ_LINE = {"Charizard V", "Charizard VSTAR"}
CZ_REPEATABLE = {
    "Professor's Research", "Marnie", "Boss's Orders", "Raihan",
    "Zinnia's Resolve", "Quick Ball", "Ultra Ball", "Switch",
    "Air Balloon", "Magma Basin", "Fire Energy", "Heat Fire Energy",
}


def _cz_zards(ctx: StrategyContext) -> int:
    names = ctx.in_play_names()
    return names.count("Charizard V") + names.count("Charizard VSTAR")


def _cz_ready(ctx: StrategyContext, pokemon) -> bool:
    """Explosive Fire typed cost: two Fire plus one more unit."""
    if pokemon is None or ctx.name(pokemon) != "Charizard VSTAR":
        return False
    return (ctx.energy_of_type(pokemon, "Fire") >= 2
            and ctx.energy_attached(pokemon) >= 3)


def _cz_output(ctx: StrategyContext, pokemon) -> int:
    """Explosive Fire damage: 130, or 230 with any damage counters on."""
    if not _cz_ready(ctx, pokemon):
        return 0
    return 130 + (100 if ctx.damage_on(pokemon) > 0 else 0)


def _cz_v_ready(ctx: StrategyContext, pokemon) -> bool:
    """Charizard V's Incinerate cost: two Fire plus one more unit."""
    if pokemon is None or ctx.name(pokemon) != "Charizard V":
        return False
    return (ctx.energy_of_type(pokemon, "Fire") >= 2
            and ctx.energy_attached(pokemon) >= 3)


def _cz_strike_damage(ctx: StrategyContext) -> int:
    """What our Active can put into the opposing Active right now."""
    active = ctx.active()
    if active is None:
        return 0
    return max(_cz_output(ctx, active), _cz_v_ready(ctx, active) * 90)


def _cz_energy_hungry(ctx: StrategyContext) -> bool:
    """Any attacker body still has an open Explosive Fire / Incinerate slot."""
    bodies = [p for p in ctx.in_play() if ctx.name(p) in (CZ_LINE | {"Moltres"})]
    if not bodies:
        return True
    for p in bodies:
        if ctx.name(p) == "Moltres":
            if ctx.energy_of_type(p, "Fire") < 1:
                return True
            continue
        if (ctx.energy_attached(p) < 3
                or ctx.energy_of_type(p, "Fire") < 2):
            return True
    return False


def _cz_vstar_used(ctx: StrategyContext) -> bool:
    try:
        return ctx.me in ctx.session.turn_state.vstar_used
    except Exception:
        return False


def _cz_star_blaze_window(ctx: StrategyContext) -> bool:
    """Spend the one-per-game 320 only where the 230 line can't answer."""
    if _cz_vstar_used(ctx):
        return False
    opp = ctx.active(ctx.opp)
    if opp is None:
        return False
    left = ctx.hp_left(opp)
    return 230 < left <= 320


def _cz_threatened(ctx: StrategyContext) -> bool:
    """The Active Charizard is facing a likely KO next swing."""
    active = ctx.active()
    if active is None or ctx.name(active) not in CZ_LINE:
        return False
    return ctx.damage_on(active) >= 120


def _cz_tool_free(ctx: StrategyContext, pokemon) -> bool:
    if pokemon is None:
        return False
    return not any(
        c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
        for c in (getattr(pokemon, "children", None) or [])
    )


def _cz_basin_ok(ctx: StrategyContext) -> bool:
    """Magma Basin is playable and useful: a Fire Energy to move onto a
    Benched Fire body, and no Basin already occupying the stadium slot."""
    if ctx.opponent_stadium_is("Magma Basin"):
        return False
    if not (CZ_FIRE & set(ctx.discard_names())):
        return False
    return any(ctx.name(p) in (CZ_LINE | {"Moltres"}) for p in ctx.bench())


def _cz_gust_window(ctx: StrategyContext) -> List:
    damage = _cz_strike_damage(ctx)
    if damage <= 0:
        return []
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= damage]


def _cz_gust(ctx: StrategyContext, pokemon) -> float:
    damage = _cz_strike_damage(ctx)
    left = ctx.hp_left(pokemon)
    if damage > 0 and 0 < left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    return 500.0 + dealt if dealt > 0 else 0.0


def _cz_promote(ctx: StrategyContext, pokemon) -> float:
    """New-Active ranking: ready swingers first, the big developing wall
    next, then the utility diggers."""
    name = ctx.name(pokemon)
    if name == "Charizard VSTAR":
        if _cz_ready(ctx, pokemon):
            return 2000.0 + ctx.energy_attached(pokemon) * 10.0
        return 900.0
    if name == "Charizard V":
        if _cz_v_ready(ctx, pokemon):
            return 1200.0
        return 600.0
    if name == "Moltres":
        return 800.0 if ctx.energy_of_type(pokemon, "Fire") >= 1 else 400.0
    if name == "Mew":
        return 350.0                      # Mysterious Tail digs Items
    if name in ("Crobat V", "Lumineon V"):
        return 100.0
    return 0.0


def _cz_retreat_ok(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None:
        return False
    can_switch = any(
        _cz_ready(ctx, p) or _cz_v_ready(ctx, p)
        or (ctx.name(p) == "Moltres" and ctx.energy_of_type(p, "Fire") >= 1)
        for p in ctx.bench()
    )
    if not can_switch:
        return False
    if _cz_strike_damage(ctx) <= 0:
        return True                        # the active can't swing: rotate
    if ctx.damage_on(active) >= 120:
        return True                        # doomed Charizard: keep the body
    return False


def _cz_basin_target_score(ctx: StrategyContext, target) -> float:
    """Magma Basin's bench target: fill the next attacker's energy gap."""
    name = ctx.name(target)
    if name == "Charizard VSTAR":
        score = 400.0
    elif name == "Charizard V":
        score = 380.0                      # energy carries into evolution
    elif name == "Moltres":
        score = 300.0
    else:
        return 0.0
    have = ctx.energy_attached(target)
    fire = ctx.energy_of_type(target, "Fire")
    if fire < 2:
        score += 200.0
    elif have < 3:
        score += 100.0
    else:
        score -= 150.0                     # loaded: the counters land anyway
    if name == "Moltres" and fire >= 1:
        score -= 120.0
    return score


def _cz_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    deck = ctx.deck_size()
    if description == "DefaultPokemonPlayAbility":
        if name == "Crobat V":
            return ctx.hand_size() <= 5    # Dark Asset draws only to 6
        if name == "Lumineon V":
            hand = set(ctx.hand_names())
            if not (hand & CZ_SUPPORTERS):
                return True
            return _cz_gust_window(ctx) and "Boss's Orders" not in hand
        return True                        # Charizard V / Moltres / Mew
    if description == "UseTrainerCard":
        if name == "Professor's Research":
            return ctx.hand_size() <= 5 and deck > 10
        if name == "Marnie":
            return (ctx.hand_size() <= 5
                    or ctx.hand_size(ctx.opp) >= 6) and deck > 5
        if name == "Zinnia's Resolve":
            return (ctx.hand_size() >= 5 and len(ctx.in_play(ctx.opp)) >= 3
                    and deck > 6)
        if name == "Raihan":
            return True                    # engine gate: the KO already fell
        if name == "Boss's Orders":
            if _cz_strike_damage(ctx) <= 0:
                return False
            if _cz_gust_window(ctx):
                return True
            return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
        if name in ("Quick Ball", "Ultra Ball"):
            return deck > 5
        if name == "Magma Basin":
            return _cz_basin_ok(ctx)
        if name == "Switch":
            return _cz_retreat_ok(ctx)
        if name == "Air Balloon":
            return any(ctx.name(p) in CZ_LINE and _cz_tool_free(ctx, p)
                       for p in ctx.in_play())
        return True
    if description == "DefaultStadiumPlayAbility" and name == "Magma Basin":
        return _cz_basin_ok(ctx)
    if description == "DefaultToolPlayAbility" and name == "Air Balloon":
        return any(ctx.name(p) in CZ_LINE and _cz_tool_free(ctx, p)
                   for p in ctx.in_play())
    if description == "UsePokemonAbility":
        if name == "Mysterious Tail":
            return True                    # engine gate: Mew Active, once
        if name == "Dark Asset":
            return ctx.hand_size() <= 5
        if name == "Luminous Sign":
            hand = set(ctx.hand_names())
            if not (hand & CZ_SUPPORTERS):
                return True
            return _cz_gust_window(ctx) and "Boss's Orders" not in hand
        return True
    if description == "UsePokemonAttack":
        if name == "Star Blaze":
            return _cz_star_blaze_window(ctx)
        return True                        # Explosive Fire / Incinerate / ...
    if description == "BaseRetreat":
        return _cz_retreat_ok(ctx)
    return True


def _cz_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational worth: the attacker line first, then the plays that
    solve a real problem, then the support bodies for their effect."""
    hand = ctx.hand_names()
    handset = set(hand)
    play = ctx.in_play_names()
    zards = play.count("Charizard V") + play.count("Charizard VSTAR")
    active = ctx.active()
    hs = ctx.hand_size()

    # -- Pokemon gap pieces ------------------------------------------------
    if name == "Charizard VSTAR":
        waiting = play.count("Charizard V") > play.count("Charizard VSTAR")
        if waiting:
            v = 90.0                       # a V body is waiting to evolve
        elif zards == 0 and "Charizard V" in handset:
            v = 55.0                       # the line arrives together
        elif zards == 0:
            v = 15.0                       # nothing to evolve into it
        else:
            v = 40.0                       # the second line's end state
    elif name == "Charizard V":
        if zards == 0:
            v = 95.0                       # the line must exist
        elif zards == 1:
            v = 55.0                       # the backup body
        else:
            v = 12.0
    elif name == "Moltres":
        if zards == 0 and play.count("Moltres") == 0:
            v = 70.0                       # emergency attacker, early only
        elif zards == 0:
            v = 45.0
        else:
            v = 10.0
    elif name == "Crobat V":
        v = 75.0 if hs <= 4 else (45.0 if hs == 5 else 10.0)
    elif name == "Mew":
        v = 60.0 if not (handset & {"Quick Ball", "Ultra Ball"}) else 25.0
    elif name == "Lumineon V":
        if not (handset & CZ_SUPPORTERS):
            v = 70.0
        elif _cz_gust_window(ctx) and "Boss's Orders" not in handset:
            v = 85.0                       # fetch the missing gust
        else:
            v = 8.0

    # -- Energy ------------------------------------------------------------
    elif name == "Fire Energy":
        v = 85.0 if _cz_energy_hungry(ctx) else 45.0
    elif name == "Heat Fire Energy":
        if active is not None and ctx.name(active) == "Charizard VSTAR" \
                and ctx.energy_attached(active) < 3:
            v = 80.0                       # typed slot + the +20 HP rider
        else:
            v = 55.0

    # -- Supporters / items ------------------------------------------------
    elif name == "Professor's Research":
        v = 80.0 if hs <= 4 else (55.0 if hs <= 6 else 20.0)
    elif name == "Marnie":
        v = 70.0 if ctx.hand_size(ctx.opp) >= 6 else (
            50.0 if hs <= 4 else 30.0)
    elif name == "Raihan":
        v = 85.0                           # attach + search, post-KO only
    elif name == "Zinnia's Resolve":
        opp_n = len(ctx.in_play(ctx.opp))
        if hs >= 5 and opp_n >= 4:
            v = 65.0
        elif hs >= 5 and opp_n >= 3:
            v = 55.0
        else:
            v = 25.0
    elif name == "Boss's Orders":
        if _cz_gust_window(ctx):
            v = 95.0                       # a KO walks into the 230 line
        elif any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp)):
            v = 45.0
        else:
            v = 15.0
    elif name == "Quick Ball":
        if zards == 0 and "Charizard V" not in handset:
            v = 85.0                       # fetch the line
        elif zards == 1 and "Charizard V" not in handset:
            v = 70.0                       # fetch the backup body
        else:
            v = 15.0
    elif name == "Ultra Ball":
        if zards == 0 and "Charizard V" not in handset:
            v = 80.0
        elif zards == 1 and "Charizard V" not in handset:
            v = 65.0
        else:
            v = 20.0
    elif name == "Magma Basin":
        v = 75.0 if _cz_basin_ok(ctx) else 10.0
    elif name == "Air Balloon":
        v = 65.0 if (active is not None and ctx.name(active) in CZ_LINE
                     and _cz_tool_free(ctx, active)) else 20.0
    elif name == "Switch":
        if _cz_retreat_ok(ctx) and _cz_strike_damage(ctx) <= 0:
            v = 70.0                       # rotate into a swinger
        elif _cz_threatened(ctx):
            v = 65.0                       # save the loaded Charizard
        else:
            v = 20.0
    else:
        v = 6.0

    if in_hand and name in handset and name not in CZ_REPEATABLE:
        v -= 40.0                          # a second copy adds little
    return v


def _cz_energy_value(name: str, ctx: StrategyContext) -> float:
    """Which energy card to spend the turn's manual attach on."""
    if name == "Fire Energy":
        return 125.0 if _cz_energy_hungry(ctx) else 60.0
    if name == "Heat Fire Energy":
        active = ctx.active()
        if active is not None and ctx.name(active) == "Charizard VSTAR" \
                and ctx.energy_attached(active) < 3:
            return 140.0                   # typed slot + the +20 HP rider
        return 95.0 if _cz_energy_hungry(ctx) else 55.0
    return 6.0


def _cz_energy_target_score(ctx: StrategyContext, target,
                            energy_name: str) -> float:
    """Where an attach lands: open slots on the Charizard line first; the
    doomed Active loses its claim once the next body grows."""
    name = ctx.name(target)
    if name == "Charizard VSTAR":
        score = 520.0 if target is ctx.active() else 400.0
        if _cz_threatened(ctx) and target is not ctx.active():
            score += 200.0                 # next attacker grows first
        fire = ctx.energy_of_type(target, "Fire")
        have = ctx.energy_attached(target)
        if fire < 2:
            score += 250.0                 # the typed slots come first
        elif have < 3:
            score += 130.0                 # third unit completes Explosive
        else:
            score -= 260.0                 # loaded: the backup grows instead
        if energy_name == "Heat Fire Energy" and target is ctx.active():
            score += 60.0
        return score
    if name == "Charizard V":
        score = 430.0
        if _cz_threatened(ctx):
            score += 150.0
        fire = ctx.energy_of_type(target, "Fire")
        have = ctx.energy_attached(target)
        if fire < 2:
            score += 200.0
        elif have < 3:
            score += 110.0
        else:
            score -= 140.0
        return score
    if name == "Moltres":
        fire = ctx.energy_of_type(target, "Fire")
        if _cz_zards(ctx) == 0:
            score = 400.0 if fire < 1 else 280.0
            if ctx.in_play_names().count("Moltres") == 0:
                score += 40.0
            return score
        return 120.0 if fire < 1 else 40.0
    return 40.0                            # support bodies never get fed


def _cz_bench_score(name: str, ctx: StrategyContext) -> float:
    names = ctx.in_play_names()
    free = 5 - len(ctx.bench())
    zards = names.count("Charizard V") + names.count("Charizard VSTAR")
    hand = set(ctx.hand_names())
    hs = ctx.hand_size()
    if name == "Charizard V":
        if zards == 0:
            return 700.0                   # the line takes the bench
        if zards == 1:
            return 450.0                   # one backup body is enough
        return 40.0
    if name == "Moltres":
        if zards == 0 and names.count("Moltres") == 0:
            return 420.0                   # emergency attacker, early only
        if zards == 0:
            return 0.0 if free <= 1 else 300.0
        return 0.0 if free <= 1 else 90.0
    if name == "Crobat V":
        if hs <= 4 and free >= 2:
            return 500.0
        if hs <= 4:
            return 380.0
        if hs == 5 and free >= 3:
            return 220.0
        return 0.0                         # full hand: no draw, no liability
    if name == "Mew":
        if free == 0:
            return 0.0
        if not (hand & {"Quick Ball", "Ultra Ball"}):
            return 300.0                   # the Item dig matters now
        return 110.0
    if name == "Lumineon V":
        if not (hand & CZ_SUPPORTERS):
            return 450.0 if free >= 2 else 380.0
        if _cz_gust_window(ctx) and "Boss's Orders" not in hand:
            return 480.0
        return 0.0                         # 2-prize body with no job
    return 0.0


def _cz_evolve_score(name: str, ctx: StrategyContext) -> float:
    if name == "Charizard VSTAR":
        return 900.0                       # strictly the better attacker
    return 0.0


def _cz_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "DefaultPokemonPlayAbility":
        return _cz_bench_score(name, ctx)
    if description == "DefaultEnergyPlayAbility":
        return _cz_energy_value(name, ctx)
    if description == "EvolvePokemonPlayAbility":
        return _cz_evolve_score(name, ctx)
    if description == "UsePokemonAbility":
        if name == "Dark Asset":
            return 85.0                    # fill a small hand
        if name == "Luminous Sign":
            return 80.0                    # fetch the missing Supporter
        if name == "Mysterious Tail":
            return 70.0                    # free Item dig while Active
        return 0.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility",
                       "DefaultToolPlayAbility"):
        return _cz_value(name, ctx, in_hand=True)
    return 0.0


def _cz_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0         # take the KO
        return score

    if title == "Explosive Fire":
        damage = _cz_output(ctx, ctx.active())
        if damage <= 0:
            return 0.0
        return _ko(800.0 + damage, damage)
    if title == "Star Blaze":
        if not _cz_star_blaze_window(ctx):
            return 0.0                     # never waste the VSTAR Power
        return 3000.0
    if title == "Heat Blast":
        active = ctx.active()
        if active is None or ctx.name(active) != "Charizard V":
            return 0.0
        if not (ctx.energy_of_type(active, "Fire") >= 3
                and ctx.energy_attached(active) >= 4):
            return 0.0
        return _ko(620.0 + 180, 180)
    if title == "Incinerate":
        active = ctx.active()
        if not _cz_v_ready(ctx, active):
            return 0.0
        score = 560.0 + 90.0
        if ctx.opponent_tools():
            score += 60.0                  # the tool strip rides along
        return _ko(score, 90)
    if title == "Inferno Wings":
        active = ctx.active()
        if active is None or ctx.name(active) != "Moltres":
            return 0.0
        if ctx.energy_of_type(active, "Fire") < 1:
            return 0.0
        damage = 90 if ctx.damage_on(active) > 0 else 20
        return _ko(430.0 + damage, damage)
    if title == "Psyshot":
        return _ko(320.0 + 30, 30)         # Mew is Active only when stuck
    return base


def _cz_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _cz_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            # the expendable basic copies pay retreat before special energy
            return 160.0 if ctx.name(target) == "Fire Energy" else 90.0
        if target.owning_player_id == ctx.me:
            return _cz_promote(ctx, target)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return _cz_energy_target_score(ctx, target, name)
    if description == "DefaultToolPlayAbility":     # Air Balloon
        if ctx.name(target) not in CZ_LINE:
            return 0.0
        if not _cz_tool_free(ctx, target):
            return 0.0
        score = 500.0
        if target is ctx.active():
            score += 150.0                 # the pivot hangs on the Active
        return score
    if description == "EvolvePokemonPlayAbility":   # Charizard VSTAR
        score = 8.0 + ctx.energy_attached(target) * 2.0
        if target is ctx.active():
            score += 6.0                   # evolve where the energy is
        return score
    return 0.0


def _cz_search_score(card, ctx: StrategyContext) -> float:
    return _cz_value(ctx.name(card), ctx, in_hand=False)


def _cz_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote the ready swinger;
    - opponent switch picks -> KO window, then scratch value;
    - Magma Basin's bench target -> fill the next attacker's gap;
    - Raihan/Magma Basin attaches -> the Charizard energy ladder;
    - Star Blaze energy self-dump -> expendable basics first;
    - hand discards -> dump the least valuable card.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return _cz_promote(ctx, card)
    if not mine and "new Active" in text:
        return _cz_gust(ctx, card)
    if not mine and ("opponent's" in text or "take" in text):
        left = ctx.hp_left(card)
        if 0 < left <= _cz_strike_damage(ctx):
            return 1000.0
        return 600.0 + ctx.damage_on(card) if ctx.damage_on(card) > 0 else 0.0
    if mine and "Benched Fire" in text:
        return _cz_basin_target_score(ctx, card)
    if mine and "Item card" in text:
        return _cz_value(name, ctx, in_hand=False)   # Mew's Mysterious Tail
    if mine and ("attach it to" in text or "attach the Energy to" in text):
        return _cz_energy_target_score(ctx, card, "")
    if mine and "attach" in text:
        return 100.0                       # pick the energy card itself
    if mine and "evolve into" in text:
        return 900.0 if name == "Charizard VSTAR" else 100.0
    if mine and "in play" in text:
        return 100.0
    if mine and "put into your hand" in text:
        return _cz_value(name, ctx, in_hand=False)
    if mine and "into your hand" in text:
        return _cz_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        if isinstance(card, EnergyEntity):  # Star Blaze self-dump
            return 50.0 if name == "Fire Energy" else 10.0
        return -_cz_value(name, ctx, in_hand=True)
    return 0.0


CHARIZARD_VSTAR = {
    "allow_action": _cz_allow,
    "action_score": _cz_action_score,
    "attack_score": _cz_attack_score,
    "target_score": _cz_target_score,
    "search_score": _cz_search_score,
    "pick_score": _cz_pick,
}


# ----------------------------------------------------------------------
# Origin Forme Palkia VSTAR  (deck key: 'Origin Forme Palkia VSTAR')
#
# Fill the board -> throw Energy into discard -> Star Portal -> Palkia
# SMASH.  Palkia VSTAR is the main attacker: Subspace Swell costs two
# Water for 60 + 20 per Benched Pokemon on BOTH sides, so a developed
# board (ours AND theirs) is the attack's fuel -- don't clear our own
# bench.  Star Portal is the one-per-game VSTAR Power: up to 3 Water
# Energy from the discard onto Water Pokemon, used the moment it powers
# an attacker (the Active's gap first, the backup body next).  Radiant
# Greninja's Concealed Cards discards Water Energy on purpose -- the
# discard is fuel, not loss -- and Moonlight Shuriken picks off two
# valuable targets.  The Inteleon engine (Sobble -> Drizzile/Inteleon)
# is the toolbox: Shady Dealings finds the exact Trainer, Quick Shooting
# finishes 20-hp leftovers; Irida is the top setup Supporter (Water
# Pokemon + Item in one).  Keep a second Palkia V developing, bench
# support bodies for their effect only (Lumineon V for a missing
# Supporter, Manaphy when their bench spreads), and when the Active is
# about to fall, energy and the promote slot go to the NEXT Palkia.

PK_ATTACKER = "Origin Forme Palkia VSTAR"
PK_V = "Origin Forme Palkia V"
PK_LINE = {PK_V, PK_ATTACKER}
PK_WATER = {"Water Energy"}
PK_SUPPORTERS = {"Irida", "Boss's Orders", "Melony", "Nessa", "Raihan",
                 "Roxanne"}
PK_REPEATABLE = {
    "Irida", "Boss's Orders", "Melony", "Nessa", "Raihan", "Roxanne",
    "Quick Ball", "Level Ball", "Ultra Ball", "Evolution Incense",
    "Capacious Bucket", "Scoop Up Net", "Water Energy",
}
_PK_BASICS = {f"{e} Energy" for e in (
    "Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting",
    "Darkness", "Metal", "Fairy")}


def _pk_palkias(ctx: StrategyContext) -> int:
    names = ctx.in_play_names()
    return names.count(PK_V) + names.count(PK_ATTACKER)


def _pk_ready(ctx: StrategyContext, pokemon) -> bool:
    """Subspace Swell typed cost: two Water."""
    if pokemon is None or ctx.name(pokemon) != PK_ATTACKER:
        return False
    return ctx.energy_of_type(pokemon, "Water") >= 2


def _pk_tool_named(pokemon, tool: str) -> bool:
    if pokemon is None:
        return False
    for c in (getattr(pokemon, "children", None) or []):
        if c.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.POKEMON_TOOL.value:
            continue
        if getattr(c, "display_name", None) == tool:
            return True
        definition = def_for(getattr(c, "archetype_id", None))
        if getattr(definition, "display_name", None) == tool:
            return True
    return False


def _pk_output(ctx: StrategyContext, pokemon) -> int:
    """Subspace Swell: 60 + 20 per Benched Pokemon (both sides), with the
    Choice Belt rider when the opponent's Active is a V."""
    if not _pk_ready(ctx, pokemon):
        return 0
    damage = 60 + 20 * (len(ctx.bench()) + len(ctx.bench(ctx.opp)))
    if _pk_tool_named(pokemon, "Choice Belt"):
        opp = ctx.active(ctx.opp)
        if opp is not None:
            try:
                if has_rule_box(getattr(opp, "archetype_id", None)):
                    damage += 30
            except Exception:
                pass
    return damage


def _pk_strike_damage(ctx: StrategyContext) -> int:
    return _pk_output(ctx, ctx.active())


def _pk_v_hydro(ctx: StrategyContext, pokemon) -> bool:
    """Palkia V's Hydro Break cost: two Water plus one more unit."""
    if pokemon is None or ctx.name(pokemon) != PK_V:
        return False
    return (ctx.energy_of_type(pokemon, "Water") >= 2
            and ctx.energy_attached(pokemon) >= 3)


def _pk_energy_hungry(ctx: StrategyContext) -> bool:
    bodies = [p for p in ctx.in_play() if ctx.name(p) in PK_LINE]
    if not bodies:
        return True
    return any(ctx.energy_of_type(p, "Water") < 2 for p in bodies)


def _pk_water_in_discard(ctx: StrategyContext) -> bool:
    return "Water Energy" in ctx.discard_names()


def _pk_water_left(ctx: StrategyContext) -> int:
    """8 Water Energy minus the copies already visible: what a Capacious
    Bucket can still dig out of the deck."""
    used = (ctx.hand_names().count("Water Energy")
            + ctx.discard_names().count("Water Energy")
            + sum(ctx.energy_of_type(p, "Water") for p in ctx.in_play()))
    return max(0, 8 - used)


def _pk_opp_energy(ctx: StrategyContext) -> int:
    return sum(ctx.energy_attached(p) for p in ctx.in_play(ctx.opp))


def _pk_threatened(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None or ctx.name(active) not in PK_LINE:
        return False
    return ctx.damage_on(active) >= 120


def _pk_portal_ok(ctx: StrategyContext) -> bool:
    """Star Portal only when it powers an attacker: the Active's gap, or
    the backup Palkia growing while the Active is about to fall."""
    if not _pk_water_in_discard(ctx):
        return False
    if not any(ctx.name(p) != "" for p in ctx.in_play()):
        return False
    active = ctx.active()
    if active is not None and ctx.name(active) in PK_LINE \
            and ctx.energy_of_type(active, "Water") < 2:
        return True
    return any(ctx.name(p) in PK_LINE and ctx.energy_of_type(p, "Water") < 2
               for p in ctx.bench())


def _pk_concealed_ok(ctx: StrategyContext) -> bool:
    if "Water Energy" not in ctx.hand_names():
        return False                       # engine condition: energy in hand
    play = ctx.in_play_names()
    return ctx.hand_size() <= 6 or PK_ATTACKER in play


def _pk_gust_window(ctx: StrategyContext) -> List:
    damage = _pk_strike_damage(ctx)
    if damage <= 0:
        return []
    return [p for p in ctx.in_play(ctx.opp) if 0 < ctx.hp_left(p) <= damage]


def _pk_gust(ctx: StrategyContext, pokemon) -> float:
    damage = _pk_strike_damage(ctx)
    left = ctx.hp_left(pokemon)
    if damage > 0 and 0 < left <= damage:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    return 500.0 + dealt if dealt > 0 else 0.0


def _pk_snipe(ctx: StrategyContext, pokemon, hit: int = 90) -> float:
    """Moonlight Shuriken (90) / Quick Shooting (2) target value."""
    left = ctx.hp_left(pokemon)
    if 0 < left <= hit:
        return 1000.0 + ctx.prize_value(pokemon) * 100.0 - left
    dealt = ctx.damage_on(pokemon)
    if dealt > 0:
        return 600.0 + dealt
    return 300.0 + ctx.prize_value(pokemon) * 50.0


def _pk_shuriken_ok(ctx: StrategyContext) -> bool:
    """Moonlight Shuriken only when at least one target falls to 90."""
    active = ctx.active()
    if active is None or ctx.name(active) != "Radiant Greninja":
        return False
    return any(0 < ctx.hp_left(p) <= 90 for p in ctx.in_play(ctx.opp))


def _pk_manaphy_ok(ctx: StrategyContext) -> bool:
    """Bench protection only against a developed (spread-damage) bench."""
    return len(ctx.bench(ctx.opp)) >= 3


def _pk_temple_ok(ctx: StrategyContext) -> bool:
    """Temple of Sinnoh: answers Path (it blocks Star Portal) or a board
    leaning on Special Energy."""
    if ctx.opponent_stadium_is("Path to the Peak"):
        return True
    for p in ctx.in_play(ctx.opp):
        for c in (getattr(p, "children", None) or []):
            if not isinstance(c, EnergyEntity):
                continue
            if ctx.name(c) and ctx.name(c) not in _PK_BASICS:
                return True
    return False


def _pk_nessa_ok(ctx: StrategyContext) -> bool:
    disc = set(ctx.discard_names())
    names = ctx.in_play_names()
    depth = (names.count("Sobble") + names.count("Drizzile")
             + names.count("Inteleon"))
    if (PK_LINE & disc) and _pk_palkias(ctx) < 2:
        return True
    if "Sobble" in disc and depth < 3:
        return True
    return False


def _pk_promote(ctx: StrategyContext, pokemon) -> float:
    """New-Active ranking: the ready Palkia first, the developing one
    next, the emergency punchers, then the toolbox bodies."""
    name = ctx.name(pokemon)
    if name == PK_ATTACKER:
        if _pk_ready(ctx, pokemon):
            return 2000.0 + ctx.energy_attached(pokemon) * 10.0
        return 1100.0
    if name == PK_V:
        if _pk_v_hydro(ctx, pokemon):
            return 1200.0
        return 700.0
    if name == "Starmie V":
        if ctx.energy_of_type(pokemon, "Water") >= 2:
            return 850.0
        return 350.0
    if name == "Radiant Greninja":
        if ctx.energy_attached(pokemon) >= 3 and _pk_shuriken_ok(ctx):
            return 800.0
        return 350.0
    if name == "Inteleon":
        return 600.0
    if name == "Drizzile":
        return 500.0
    if name == "Sobble":
        return 300.0
    if name == "Lumineon V":
        return 100.0
    if name == "Manaphy":
        return 50.0
    return 0.0


def _pk_scoop(ctx: StrategyContext, pokemon) -> float:
    """Scoop Up Net target: heal the wounded, reuse a used search body."""
    if pokemon is None:
        return 0.0
    if ctx.name(pokemon) in PK_LINE or ctx.name(pokemon) == "Starmie V":
        return 0.0                         # engine excludes Pokemon V anyway
    dealt = ctx.damage_on(pokemon)
    if pokemon is ctx.active():
        return 600.0 if ctx.bench() else -999.0  # empty bench = we lose
    if dealt >= 60:
        return 1200.0                      # nearly dead: bounce and replay
    if ctx.name(pokemon) in ("Drizzile", "Inteleon"):
        return 500.0 if dealt == 0 else 700.0    # fire Shady Dealings again
    if dealt > 0:
        return 400.0 + dealt
    return 100.0


def _pk_scoop_ok(ctx: StrategyContext) -> bool:
    if not ctx.bench():
        return False                       # netting the active would lose
    hand = set(ctx.hand_names())
    for p in ctx.in_play():
        if ctx.name(p) in PK_LINE or ctx.name(p) == "Starmie V":
            continue
        if ctx.damage_on(p) >= 40:
            return True
    if len(ctx.bench()) >= 5 and hand & {"Drizzile", "Inteleon"}:
        return True                        # free a slot to replay a search
    return False


def _pk_retreat_ok(ctx: StrategyContext) -> bool:
    active = ctx.active()
    if active is None:
        return False
    can_rotate = any(
        _pk_ready(ctx, p) or _pk_v_hydro(ctx, p)
        or (ctx.name(p) == "Starmie V"
            and ctx.energy_of_type(p, "Water") >= 2)
        for p in ctx.bench()
    )
    if not can_rotate:
        return False
    if _pk_strike_damage(ctx) <= 0:
        return True                        # the active can't swing: rotate
    if ctx.damage_on(active) >= 120:
        return True                        # doomed Palkia: keep the body
    return False


def _pk_allow(description: str, name: str, ctx: StrategyContext) -> bool:
    deck = ctx.deck_size()
    if description == "DefaultPokemonPlayAbility":
        if name == "Lumineon V":
            hand = set(ctx.hand_names())
            if not (hand & PK_SUPPORTERS):
                return True
            return _pk_gust_window(ctx) and "Boss's Orders" not in hand
        if name == "Manaphy":
            return _pk_manaphy_ok(ctx)
        return True                        # Palkia V / Greninja / Starmie / Sobble
    if description == "EvolvePokemonPlayAbility":
        return True                        # the engine line always advances
    if description == "UseTrainerCard":
        if name == "Irida":
            return deck > 5
        if name == "Melony":
            if not _pk_water_in_discard(ctx):
                return False
            return _pk_energy_hungry(ctx) or ctx.hand_size() <= 4
        if name == "Nessa":
            return _pk_nessa_ok(ctx)
        if name == "Raihan":
            return ctx.prizes_lost() >= 1  # come back after a KO fell
        if name == "Roxanne":
            return ctx.prizes_lost() >= 3  # behind: reshuffle to 6 vs 2
        if name == "Boss's Orders":
            if _pk_strike_damage(ctx) <= 0:
                return False
            if _pk_gust_window(ctx):
                return True
            return any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp))
        if name in ("Quick Ball", "Level Ball", "Ultra Ball",
                    "Evolution Incense"):
            return deck > 5
        if name == "Capacious Bucket":
            return _pk_energy_hungry(ctx) and _pk_water_left(ctx) > 0
        if name == "Scoop Up Net":
            return _pk_scoop_ok(ctx)
        if name == "Choice Belt":
            return ctx.opponent_rule_box()
        if name == "Tool Jammer":
            return ctx.opponent_tools()
        if name == "Temple of Sinnoh":
            return _pk_temple_ok(ctx)
        if name == "Pal Pad":
            return any(s in ctx.discard_names() for s in PK_SUPPORTERS)
        return True                        # VIP Pass / Heavy Ball / ...
    if description == "DefaultStadiumPlayAbility" and name == "Temple of Sinnoh":
        return _pk_temple_ok(ctx)
    if description == "DefaultToolPlayAbility":
        if name == "Choice Belt":
            return ctx.opponent_rule_box()
        if name == "Tool Jammer":
            return ctx.opponent_tools()
        return True
    if description == "UsePokemonAbility":
        if name == "Star Portal":
            return _pk_portal_ok(ctx)
        if name == "Concealed Cards":
            return _pk_concealed_ok(ctx)
        if name == "Luminous Sign":
            hand = set(ctx.hand_names())
            if not (hand & PK_SUPPORTERS):
                return True
            return _pk_gust_window(ctx) and "Boss's Orders" not in hand
        if name == "Quick Shooting":
            return True                    # engine gate: Inteleon in play
        return True                        # Wave Veil is a passive
    if description == "UsePokemonAttack":
        if name == "Moonlight Shuriken":
            return _pk_shuriken_ok(ctx)
        if name == "Rule the Region":
            # rotate into a ready swinger instead when one exists
            return not _pk_retreat_ok(ctx)
        return True                        # Subspace Swell / Hydro Break / ...
    if description == "BaseRetreat":
        return _pk_retreat_ok(ctx)
    return True


def _pk_value(name: str, ctx: StrategyContext, in_hand: bool = False) -> float:
    """Situational worth: the Palkia line first, then the engine, then the
    plays that solve a real problem (mirrors the strategy priority chain)."""
    hand = ctx.hand_names()
    handset = set(hand)
    play = ctx.in_play_names()
    palkias = play.count(PK_V) + play.count(PK_ATTACKER)
    v_waiting = play.count(PK_V) > play.count(PK_ATTACKER)
    unevolved = play.count("Sobble")
    drizziles = play.count("Drizzile")
    inteles = play.count("Inteleon")
    depth = unevolved + drizziles + inteles
    hs = ctx.hand_size()

    # -- Pokemon gap pieces ------------------------------------------------
    if name == PK_ATTACKER:
        if v_waiting:
            v = 90.0                       # a V body is waiting to evolve
        elif palkias == 0 and PK_V in handset:
            v = 55.0                       # the line arrives together
        elif palkias == 0:
            v = 15.0                       # nothing to evolve into it
        else:
            v = 40.0                       # the second line's end state
    elif name == PK_V:
        v = 95.0 if palkias == 0 else (55.0 if palkias == 1 else 12.0)
    elif name == "Sobble":
        v = 45.0 if depth < 2 else (25.0 if depth < 4 else 6.0)
    elif name == "Drizzile":
        if unevolved == 0:
            v = 6.0
        elif "Drizzile" in handset:
            v = 12.0                       # already holding the search
        else:
            v = 80.0 if unevolved > drizziles else 40.0
    elif name == "Inteleon":
        v = 60.0 if drizziles > inteles else 6.0
    elif name == "Radiant Greninja":
        v = 55.0 if "Radiant Greninja" not in play else 8.0
    elif name == "Starmie V":
        v = 55.0 if ("Starmie V" not in play
                     and _pk_opp_energy(ctx) >= 4) else 10.0
    elif name == "Manaphy":
        v = 55.0 if ("Manaphy" not in play and _pk_manaphy_ok(ctx)) else 8.0
    elif name == "Lumineon V":
        if not (handset & PK_SUPPORTERS):
            v = 70.0
        elif _pk_gust_window(ctx) and "Boss's Orders" not in handset:
            v = 85.0                       # fetch the missing gust
        else:
            v = 8.0

    # -- Energy ------------------------------------------------------------
    elif name == "Water Energy":
        v = 85.0 if _pk_energy_hungry(ctx) else 45.0

    # -- Supporters --------------------------------------------------------
    elif name == "Irida":
        if depth < 4 or palkias < 2 or _pk_energy_hungry(ctx):
            v = 85.0                       # setup gaps: she solves them
        else:
            v = 60.0
    elif name == "Boss's Orders":
        if _pk_gust_window(ctx):
            v = 95.0                       # a KO walks into Swell's range
        elif any(ctx.damage_on(p) > 0 for p in ctx.in_play(ctx.opp)):
            v = 45.0
        else:
            v = 15.0
    elif name == "Melony":
        if _pk_energy_hungry(ctx) and _pk_water_in_discard(ctx):
            v = 90.0                       # attach + draw 3 into the gap
        elif hs <= 4:
            v = 60.0
        else:
            v = 45.0
    elif name == "Nessa":
        disc = set(ctx.discard_names())
        if (PK_LINE & disc) and palkias < 2:
            v = 85.0                       # the lost Palkia comes back
        elif "Sobble" in disc and depth < 3:
            v = 60.0
        else:
            v = 15.0
    elif name == "Raihan":
        v = 85.0                           # attach + search, post-KO only
    elif name == "Roxanne":
        v = 80.0 if ctx.prizes_lost() >= 3 else 10.0

    # -- Items -------------------------------------------------------------
    elif name == "Quick Ball":
        if palkias == 0 and PK_V not in handset:
            v = 85.0                       # fetch the line
        elif unevolved == 0 and "Sobble" not in handset:
            v = 60.0
        else:
            v = 15.0
    elif name == "Ultra Ball":
        if palkias == 0 and PK_V not in handset:
            v = 80.0
        elif v_waiting and PK_ATTACKER not in handset:
            v = 75.0
        else:
            v = 20.0
    elif name == "Level Ball":
        if unevolved > drizziles and "Drizzile" not in handset:
            v = 80.0                       # the engine's first search
        elif depth < 4 and "Sobble" not in handset:
            v = 65.0
        else:
            v = 10.0
    elif name == "Evolution Incense":
        if v_waiting and PK_ATTACKER not in handset:
            v = 85.0                       # evolve the waiting V
        elif unevolved > drizziles and "Drizzile" not in handset:
            v = 75.0
        elif drizziles > inteles and "Inteleon" not in handset:
            v = 70.0
        else:
            v = 12.0
    elif name == "Capacious Bucket":
        v = 85.0 if (_pk_energy_hungry(ctx) and _pk_water_left(ctx) > 0) \
            else 20.0
    elif name == "Scoop Up Net":
        v = 68.0 if _pk_scoop_ok(ctx) else 15.0
    elif name == "Choice Belt":
        v = 65.0 if ctx.opponent_rule_box() else 15.0
    elif name == "Tool Jammer":
        v = 65.0 if ctx.opponent_tools() else 15.0
    elif name == "Temple of Sinnoh":
        v = 70.0 if _pk_temple_ok(ctx) else 12.0
    elif name == "Pal Pad":
        v = 35.0 if any(s in ctx.discard_names()
                        for s in PK_SUPPORTERS) else 10.0
    elif name == "Battle VIP Pass":
        v = 70.0                           # engine: turn 1 only
    elif name == "Hisuian Heavy Ball":
        v = 35.0 if (palkias < 2 or depth < 2) else 10.0
    else:
        v = 6.0

    if in_hand and name in handset and name not in PK_REPEATABLE:
        v -= 40.0                          # a second copy adds little
    return v


def _pk_energy_value(name: str, ctx: StrategyContext) -> float:
    """Which energy card to spend the turn's manual attach on."""
    if name == "Water Energy":
        return 120.0 if _pk_energy_hungry(ctx) else 60.0
    return 6.0


def _pk_energy_target_score(ctx: StrategyContext, target,
                            energy_name: str) -> float:
    """Where an attach (manual or Star Portal) lands: the Palkia gap
    first, the developing V next, the emergency punchers, engine never."""
    name = ctx.name(target)
    if name == PK_ATTACKER:
        score = 520.0 if target is ctx.active() else 400.0
        if _pk_threatened(ctx) and target is not ctx.active():
            score += 200.0                 # next attacker grows first
        water = ctx.energy_of_type(target, "Water")
        if water < 2:
            score += 250.0                 # the typed slots come first
        else:
            score -= 260.0                 # loaded: the backup grows instead
        return score
    if name == PK_V:
        score = 430.0
        if _pk_threatened(ctx):
            score += 150.0
        water = ctx.energy_of_type(target, "Water")
        have = ctx.energy_attached(target)
        if water < 2:
            score += 200.0
        elif have < 3:
            score += 110.0                 # Hydro Break's third unit
        else:
            score -= 140.0
        return score
    if name == "Radiant Greninja":
        water = ctx.energy_of_type(target, "Water")
        if water < 2:
            return 320.0
        if water < 3:
            return 240.0                   # Moonlight's colorless unit
        return -100.0                      # loaded: leave it alone
    if name == "Starmie V":
        water = ctx.energy_of_type(target, "Water")
        return 300.0 if water < 2 else -100.0
    return 40.0                            # engine / support never get fed


def _pk_bench_score(name: str, ctx: StrategyContext) -> float:
    names = ctx.in_play_names()
    free = 5 - len(ctx.bench())
    palkias = names.count(PK_V) + names.count(PK_ATTACKER)
    depth = (names.count("Sobble") + names.count("Drizzile")
             + names.count("Inteleon"))
    hand = set(ctx.hand_names())
    if name == PK_V:
        if palkias == 0:
            return 700.0                   # the line takes the bench
        if palkias == 1:
            return 450.0                   # one backup body is enough
        return 40.0
    if name == "Sobble":
        if depth == 0:
            score = 600.0
        elif depth < 3:
            score = 420.0
        elif depth < 4:
            score = 300.0
        else:
            score = 60.0
        # slot discipline: keep room for the backup Palkia
        if palkias < 2 and free <= 1:
            score = min(score, 120.0)
        return score
    if name == "Radiant Greninja":
        if "Radiant Greninja" in names:
            return 0.0
        if free <= 0:
            return 0.0
        if "Water Energy" in hand:
            return 400.0                   # the fuel is ready to dump
        return 340.0
    if name == "Lumineon V":
        if not (hand & PK_SUPPORTERS):
            return 450.0 if free >= 2 else 380.0
        if _pk_gust_window(ctx) and "Boss's Orders" not in hand:
            return 480.0
        return 0.0                         # 2-prize body with no job
    if name == "Manaphy":
        if "Manaphy" in names or not _pk_manaphy_ok(ctx):
            return 0.0
        return 320.0 if free >= 2 else 240.0
    if name == "Starmie V":
        if "Starmie V" in names or free <= 0:
            return 0.0
        if _pk_opp_energy(ctx) >= 4:
            return 280.0                   # Energy Spiral's window
        return 120.0                       # 0-retreat starter
    return 0.0


def _pk_evolve_score(name: str, ctx: StrategyContext) -> float:
    if name == PK_ATTACKER:
        return 900.0                       # strictly the better attacker
    if name == "Drizzile":
        return 800.0                       # Shady Dealings consistency
    if name == "Inteleon":
        return 650.0                       # search-2 or Quick Shooting
    return 0.0


def _pk_action_score(description: str, name: str,
                     ctx: StrategyContext) -> float:
    if description == "DefaultPokemonPlayAbility":
        return _pk_bench_score(name, ctx)
    if description == "DefaultEnergyPlayAbility":
        return _pk_energy_value(name, ctx)
    if description == "EvolvePokemonPlayAbility":
        return _pk_evolve_score(name, ctx)
    if description == "UsePokemonAbility":
        if name == "Star Portal":
            if not _pk_portal_ok(ctx):
                return 0.0
            active = ctx.active()
            if active is not None and ctx.name(active) in PK_LINE \
                    and ctx.energy_of_type(active, "Water") < 2:
                return 95.0                # swings THIS turn
            return 75.0                    # powers the backup body
        if name == "Concealed Cards":
            hs = ctx.hand_size()
            return 75.0 if hs <= 4 else (60.0 if hs <= 6 else 40.0)
        if name == "Luminous Sign":
            return 80.0                    # fetch the missing Supporter
        if name == "Quick Shooting":
            opp = ctx.in_play(ctx.opp)
            if any(0 < ctx.hp_left(p) <= 20 for p in opp):
                return 90.0                # a counter closes a KO
            if any(ctx.damage_on(p) > 0 for p in opp):
                return 65.0
            return 45.0
        return 0.0
    if description in ("UseTrainerCard", "DefaultStadiumPlayAbility",
                       "DefaultToolPlayAbility"):
        return _pk_value(name, ctx, in_hand=True)
    return 0.0


def _pk_attack_score(title: str, base: float,
                     ctx: StrategyContext) -> float:
    opp_active = ctx.active(ctx.opp)
    opp_left = ctx.hp_left(opp_active) if opp_active is not None else None
    active = ctx.active()

    def _ko(score, damage):
        if opp_left is not None and 0 < opp_left <= damage:
            return score + 1000.0         # take the KO
        return score

    if title == "Subspace Swell":
        damage = _pk_output(ctx, active)
        if damage <= 0:
            return 0.0
        return _ko(800.0 + damage, damage)
    if title == "Hydro Break":
        if not _pk_v_hydro(ctx, active):
            return 0.0
        return _ko(700.0 + 200, 200)
    if title == "Rule the Region":
        if active is None or ctx.name(active) != PK_V:
            return 0.0
        if ctx.energy_of_type(active, "Water") < 1:
            return 0.0
        return 250.0                       # utility: search the Stadium
    if title == "Moonlight Shuriken":
        if not _pk_shuriken_ok(ctx):
            return 0.0
        targets = [p for p in ctx.in_play(ctx.opp)
                   if 0 < ctx.hp_left(p) <= 90][:2]
        score = 400.0 + 500.0 * len(targets)
        for t in targets:
            score += ctx.prize_value(t) * 100.0
        if opp_left is not None and 0 < opp_left <= 90:
            score += 1000.0
        return score
    if title == "Energy Spiral":
        if active is None or ctx.name(active) != "Starmie V":
            return 0.0
        if ctx.energy_of_type(active, "Water") < 2:
            return 0.0
        damage = 50 * _pk_opp_energy(ctx)
        if damage <= 0:
            return 0.0
        return _ko(400.0 + damage, damage)
    if title == "Swift":
        if active is None or ctx.name(active) != "Starmie V":
            return 0.0
        if ctx.energy_attached(active) < 2:
            return 0.0
        return _ko(200.0 + 50, 50)
    return base


def _pk_target_score(description: str, name: str,
                     ctx: StrategyContext, target_id: str) -> float:
    target = ctx.board.get_entity(target_id)
    if target is None:
        return 0.0
    if description == "UseTrainerCard" and name == "Boss's Orders":
        return _pk_gust(ctx, target)
    if description == "BaseRetreat":
        if isinstance(target, EnergyEntity):
            # we run basic Water only: expendable over anything else
            return 160.0
        if target.owning_player_id == ctx.me:
            return _pk_promote(ctx, target)
        return 0.0
    if description == "DefaultEnergyPlayAbility":
        return _pk_energy_target_score(ctx, target, name)
    if description in ("DefaultToolPlayAbility",):     # Choice Belt / Jammer
        if ctx.name(target) not in PK_LINE:
            return 0.0
        score = 500.0
        if target is ctx.active():
            score += 150.0                 # the tool hangs on the Active
        return score
    if description == "EvolvePokemonPlayAbility":
        if name == PK_ATTACKER:
            score = 8.0 + ctx.energy_attached(target) * 2.0
            if target is ctx.active():
                score += 6.0               # evolve where the energy is
            return score
        return 4.0 if target is ctx.active() else 2.0
    return 0.0


def _pk_search_score(card, ctx: StrategyContext) -> float:
    return _pk_value(ctx.name(card), ctx, in_hand=False)


def _pk_pick(prompt: str, ctx: StrategyContext, card) -> float:
    """Ranks in-place picker prompts:

    - own "new Active" choices -> promote the ready Palkia;
    - opponent switch/snipe picks -> KO window (90 for Shuriken, 20 for
      Quick Shooting), then scratch value;
    - Star Portal / Melony attach targets -> the Palkia energy ladder;
    - Star Portal / Melony energy cards -> any fuel card is fine;
    - Scoop Up Net -> wounded first, used search bodies next;
    - Concealed Cards discard -> dump the recoverable Water Energy.
    """
    text = prompt or ""
    name = ctx.name(card)
    mine = card.owning_player_id == ctx.me
    if mine and "new Active" in text:
        return _pk_promote(ctx, card)
    if not mine and "new Active" in text:
        return _pk_gust(ctx, card)
    if not mine and ("opponent's" in text or "take" in text):
        hit = 90 if "90" in text else 20   # Moonlight vs Quick Shooting
        return _pk_snipe(ctx, card, hit)
    if mine and "put into your hand" in text:
        return _pk_scoop(ctx, card)        # Scoop Up Net
    if mine and "attach" in text:
        if "mon to attach" in text or "attach the Energy to" in text \
                or "attach it to" in text:
            return _pk_energy_target_score(ctx, card, name)
        return 100.0                       # the energy card itself
    if mine and "evolve into" in text:
        if name == PK_ATTACKER:
            return 900.0
        if name == "Inteleon":
            return 750.0
        if name == "Drizzile":
            return 700.0
        return 100.0
    if mine and "in play" in text:
        return 100.0
    if mine and "into your hand" in text:
        return _pk_value(name, ctx, in_hand=False)
    if mine and "discard" in text.lower():
        if isinstance(card, EnergyEntity):  # Concealed Cards fuel
            return 50.0
        return -_pk_value(name, ctx, in_hand=True)
    return 0.0


PALKIA_VSTAR = {
    "allow_action": _pk_allow,
    "action_score": _pk_action_score,
    "attack_score": _pk_attack_score,
    "target_score": _pk_target_score,
    "search_score": _pk_search_score,
    "pick_score": _pk_pick,
}


DECK_STRATEGIES = {
    "Dragapult Inteleon": DRAGAPULT_INTELEON,
    "Rapid Strike Urshifu V": RAPID_STRIKE_URSHIFU,
    "Shadow Rider Calyrex V": SHADOW_RIDER,
    "Bronzor": CORVIKNIGHT_BRONZONG,
    "Eternatus V": ETERNATUS_VMAX,
    "Rayquaza V": RAYQUAZA_VMAX_FLAFFY,
    "Sobble (suicune-ludicolo)": SUICUNE_LUDICOLO,
    "Charizard (charizard-vmax)": CHARIZARD_VSTAR,
    "Origin Forme Palkia VSTAR": PALKIA_VSTAR,
}


def strategy_for(deck_name: Optional[str]) -> Optional[dict]:
    """The brain for a bot deck name, or None (generic AI)."""
    if not deck_name:
        return None
    return DECK_STRATEGIES.get(deck_name)


def make_context(session, player_id: str) -> StrategyContext:
    return StrategyContext(session, player_id)
