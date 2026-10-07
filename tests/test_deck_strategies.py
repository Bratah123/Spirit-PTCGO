"""Unit tests for the deck strategic-brain system (content.deck_strategies),
the AIPlayer wiring, and a headless end-to-end sim smoke run."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from spirit.game.content import bot_decks  # noqa: E402
from spirit.game.content.deck_strategies import (  # noqa: E402
    CORVIKNIGHT_BRONZONG,
    DRAGAPULT_INTELEON,
    ETERNATUS_VMAX,
    RAPID_STRIKE_URSHIFU,
    RS_ATTACKERS,
    SHADOW_RIDER,
    SR_ATTACKERS,
    StrategyContext,
    _cv_allow,
    _cv_action_score,
    _cv_attack_score,
    _cv_bench_score,
    _cv_energy_target_score,
    _cv_output,
    _cv_pick,
    _cv_retreat_ok,
    _cv_search_score,
    _cv_switch_ok,
    _cv_target_score,
    _cv_transfer_ok,
    _cv_value,
    _dragapult_allow,
    _dragapult_pick,
    _dragapult_value,
    _et_allow,
    _et_attack_score,
    _et_bench_score,
    _et_dread_end,
    _et_energy_target_score,
    _et_gust,
    _et_gust_window,
    _et_output,
    _et_pick,
    _et_promote,
    _et_retreat_ok,
    _et_search_score,
    _et_strike_damage,
    _et_switch_ok,
    _et_target_score,
    _et_value,
    _rs_allow,
    _rs_attack_score,
    _rs_grf_score,
    _rs_pick,
    _rs_search_score,
    _rs_switch_ok,
    _sr_allow,
    _sr_attack_score,
    _sr_energy_target_score,
    _sr_pick,
    _sr_retreat_ok,
    _sr_search_score,
    _sr_value,
    gust_score,
    ko_threshold_counters,
    order_score,
    promotion_score,
    rs_energy_value,
    strategy_for,
)


class FakeMon:
    def __init__(self, name, owner="p1", hp=0, max_hp=None, energy=0,
                 cost=0, eid=None, prize=1):
        self.name_ = name
        self.owning_player_id = owner
        self.hp = hp
        self.max_hp = hp if max_hp is None else max_hp
        self.energy = energy
        self.cost = cost
        self.entity_id = eid or name
        self.prize = prize
        self.children = []


class _FakeBoard:
    """Minimal board surface: entity lookup by id across the fake pools."""

    def __init__(self, ctx):
        self._ctx = ctx

    def get_entity(self, entity_id):
        pools = (self._ctx.play, self._ctx.opp_play,
                 self._ctx.bench_pokes, self._ctx.opp_bench_pokes)
        if self._ctx._active is not None:
            pools = pools + ((self._ctx._active,),)
        if self._ctx._opp_active is not None:
            pools = pools + ((self._ctx._opp_active,),)
        for pool in pools:
            for entity in pool:
                if getattr(entity, "entity_id", None) == entity_id:
                    return entity
        return None


class FakeCtx:
    """Duck-typed stand-in for StrategyContext (surface used by the brain)."""

    me = "p1"
    opp = "p2"

    def __init__(self, hand=(), play=(), opp_play=(), active=None,
                 opp_active=None, bench=(), opp_bench=(),
                 active_damage=130, stadium=None, opp_rule_box=False,
                 opp_tools=False, prizes_lost=0, entered=(), discard=(),
                 deck=40, locked=()):
        self.hand = list(hand)
        self.play = list(play)
        self.opp_play = list(opp_play)
        self._active = active
        self._opp_active = opp_active
        self.bench_pokes = list(bench)
        self.opp_bench_pokes = list(opp_bench)
        self._active_damage = active_damage
        self.stadium = stadium
        self._opp_rule_box = opp_rule_box
        self._opp_tools = opp_tools
        self._prizes_lost = prizes_lost
        self.entered_ids = set(entered)
        self.discard_pile = list(discard)
        self.deck_cards = list(deck) if isinstance(deck, (list, tuple)) \
            else list(range(deck))
        self.locked_titles = set(locked)
        self.board = _FakeBoard(self)

    def attack_locked(self, pokemon, title):
        if pokemon is None:
            return False
        return title in self.locked_titles

    # -- names ---------------------------------------------------------
    @staticmethod
    def name(entity):
        if isinstance(entity, str):
            return entity
        return getattr(entity, "name_", "") or ""

    # -- zones ---------------------------------------------------------
    def hand_names(self, pid=None):
        return list(self.hand)

    def hand_size(self, pid=None):
        return len(self.hand)

    def discard_names(self, pid=None):
        return list(self.discard_pile)

    def deck_size(self, pid=None):
        return len(self.deck_cards)

    def in_play(self, pid=None):
        if pid == self.opp:
            return list(self.opp_play)
        return list(self.play)

    def in_play_names(self, pid=None):
        return [self.name(p) for p in self.in_play(pid)]

    def active(self, pid=None):
        if pid == self.opp:
            return self._opp_active
        return self._active

    def bench(self, pid=None):
        if pid == self.opp:
            return list(self.opp_bench_pokes)
        return list(self.bench_pokes)

    # -- damage --------------------------------------------------------
    def max_hp(self, pokemon):
        return pokemon.max_hp

    def hp_left(self, pokemon):
        return max(0, pokemon.hp)

    def damage_on(self, pokemon):
        return pokemon.max_hp - pokemon.hp

    def prize_value(self, pokemon):
        return pokemon.prize

    def energy_attached(self, pokemon):
        return pokemon.energy

    def min_attack_cost(self, pokemon):
        return pokemon.cost

    def active_ready(self, pid=None):
        active = self.active(pid)
        if active is None:
            return False
        return active.energy >= max(1, active.cost)

    def active_attack_damage(self):
        return self._active_damage

    def ko_window(self, damage=None):
        if damage is None:
            damage = self._active_damage
        if damage <= 0:
            return []
        return [p for p in self.opp_play if p.hp <= damage]

    def opponent_rule_box(self):
        return self._opp_rule_box

    def opponent_tools(self):
        return self._opp_tools

    def opponent_stadium_is(self, card_name):
        return self.stadium == card_name

    def prizes_lost(self):
        return self._prizes_lost

    def entered_active(self, pokemon):
        if pokemon is None:
            return False
        return getattr(pokemon, "entity_id", None) in self.entered_ids


class RegistryTests(unittest.TestCase):
    def test_dragapult_brain_registered(self):
        spec = strategy_for("Dragapult Inteleon")
        self.assertIs(spec, DRAGAPULT_INTELEON)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score",
                     "counter_plan"):
            self.assertTrue(callable(spec[hook]), hook)

    def test_unknown_or_missing_name_has_no_brain(self):
        self.assertIsNone(strategy_for("Some Other Deck"))
        self.assertIsNone(strategy_for(None))
        self.assertIsNone(strategy_for(""))

    def test_active_pool_is_brained_decks_only(self):
        names = {name for name, _ in bot_decks.BOT_DECKS}
        self.assertEqual(names, {"Dragapult Inteleon", "Rapid Strike Urshifu V",
                                 "Shadow Rider Calyrex V", "Bronzor",
                                 "Eternatus V"})
        self.assertEqual(
            set(bot_decks.ACTIVE_BOT_DECKS),
            {"Dragapult Inteleon", "Rapid Strike Urshifu V",
             "Shadow Rider Calyrex V", "Bronzor", "Eternatus V"},
        )


class HelperTests(unittest.TestCase):
    def test_order_score_prefers_listed_order(self):
        order = ["A", "B", "C"]
        self.assertGreater(order_score(order, "A"), order_score(order, "B"))
        self.assertGreater(order_score(order, "B"), order_score(order, "C"))
        self.assertLess(order_score(order, "Zzz"), order_score(order, "C"))

    def test_counter_plan_finishes_cheapest_ko_first(self):
        ctx = FakeCtx()
        almost_dead = FakeMon("Sobble", owner="p2", hp=20, max_hp=60, prize=1)
        fresh = FakeMon("Zigzagoon", owner="p2", hp=110, max_hp=110, prize=1)
        plan = ko_threshold_counters(ctx, [fresh, almost_dead], 2)
        self.assertEqual(plan, {almost_dead.entity_id: 2})

    def test_counter_plan_splits_toward_second_ko(self):
        ctx = FakeCtx()
        one_left = FakeMon("Zigzagoon", owner="p2", hp=10, max_hp=110)
        five_left = FakeMon("Sobble", owner="p2", hp=50, max_hp=60)
        plan = ko_threshold_counters(ctx, [five_left, one_left], 5)
        self.assertEqual(plan, {one_left.entity_id: 1, five_left.entity_id: 4})

    def test_counter_plan_prefers_prizes_on_ties(self):
        ctx = FakeCtx()
        basic = FakeMon("Sobble", owner="p2", hp=30, max_hp=60, prize=1)
        vstar = FakeMon("VSTAR", owner="p2", hp=30, max_hp=280, prize=2)
        plan = ko_threshold_counters(ctx, [basic, vstar], 3)
        self.assertEqual(plan[vstar.entity_id], 3)

    def test_counter_plan_never_overspends_a_dead_body(self):
        ctx = FakeCtx()
        target = FakeMon("Sobble", owner="p2", hp=10, max_hp=60)
        plan = ko_threshold_counters(ctx, [target], 5)
        self.assertEqual(plan, {target.entity_id: 1})

    def test_promotion_prefers_ready_vmax(self):
        ctx = FakeCtx()
        ready_vmax = FakeMon("Dragapult VMAX", energy=2, cost=1)
        unready_vmax = FakeMon("Dragapult VMAX", energy=0, cost=2, eid="v2")
        sobble = FakeMon("Sobble", energy=0, cost=1, eid="s1")
        scores = [promotion_score(ctx, m)
                  for m in (sobble, unready_vmax, ready_vmax)]
        self.assertEqual(scores, sorted(scores))
        self.assertGreater(promotion_score(ctx, ready_vmax),
                           promotion_score(ctx, unready_vmax))

    def test_gust_prefers_ko_window_then_damaged(self):
        ctx = FakeCtx(active_damage=130)
        in_range = FakeMon("Zigzagoon", owner="p2", hp=110, max_hp=110)
        fresh_big = FakeMon("VMAX", owner="p2", hp=300, max_hp=320, prize=3)
        self.assertGreater(gust_score(ctx, in_range), gust_score(ctx, fresh_big))
        dented = FakeMon("VMAX", owner="p2", hp=300, max_hp=320, eid="d2")
        pristine = FakeMon("VMAX", owner="p2", hp=320, max_hp=320, eid="s2")
        self.assertGreater(gust_score(ctx, dented), gust_score(ctx, pristine))


class GateTests(unittest.TestCase):
    def test_research_gated_by_hand_size(self):
        small = FakeCtx(hand=["a", "b", "c", "d", "e"])
        big = FakeCtx(hand=["a", "b", "c", "d", "e", "f", "g"])
        self.assertTrue(_dragapult_allow("UseTrainerCard", "Professor's Research", small))
        self.assertFalse(_dragapult_allow("UseTrainerCard", "Professor's Research", big))

    def test_path_requires_opponent_rule_box_and_no_own_stadium(self):
        self.assertTrue(_dragapult_allow(
            "DefaultStadiumPlayAbility", "Path to the Peak",
            FakeCtx(opp_rule_box=True)))
        self.assertFalse(_dragapult_allow(
            "DefaultStadiumPlayAbility", "Path to the Peak",
            FakeCtx(opp_rule_box=False)))
        self.assertFalse(_dragapult_allow(
            "DefaultStadiumPlayAbility", "Path to the Peak",
            FakeCtx(opp_rule_box=True, stadium="Path to the Peak")))

    def test_raihan_needs_a_prize_lost(self):
        self.assertFalse(_dragapult_allow("UseTrainerCard", "Raihan", FakeCtx()))
        self.assertTrue(_dragapult_allow(
            "UseTrainerCard", "Raihan", FakeCtx(prizes_lost=1)))

    def test_switch_only_when_active_not_ready(self):
        ready = FakeCtx(active=FakeMon("Dragapult VMAX", energy=2, cost=1))
        stuck = FakeCtx(active=FakeMon("Dragapult VMAX", energy=0, cost=2))
        self.assertFalse(_dragapult_allow("UseTrainerCard", "Switch", ready))
        self.assertTrue(_dragapult_allow("UseTrainerCard", "Switch", stuck))

    def test_manual_retreat_rules(self):
        ready = FakeCtx(active=FakeMon("Dragapult VMAX", energy=2, cost=1),
                        bench=[FakeMon("Dragapult VMAX", energy=2, cost=1)])
        self.assertFalse(_dragapult_allow("BaseRetreat", "Dragapult VMAX", ready))

        stuck_with_energy = FakeCtx(
            active=FakeMon("Drizzile", energy=1, cost=3),
            bench=[FakeMon("Dragapult VMAX", energy=2, cost=1)])
        self.assertTrue(_dragapult_allow("BaseRetreat", "Drizzile", stuck_with_energy))

        useless_bench = FakeCtx(
            active=FakeMon("Drizzile", energy=1, cost=3),
            bench=[FakeMon("Sobble", energy=0, cost=1)])
        self.assertFalse(_dragapult_allow("BaseRetreat", "Drizzile", useless_bench))

    def test_ability_allowlist(self):
        self.assertTrue(_dragapult_allow(
            "UsePokemonAbility", "Quick Shooting", FakeCtx()))
        self.assertFalse(_dragapult_allow(
            "UsePokemonAbility", "Intrepid Sword", FakeCtx()))


class CardValueTests(unittest.TestCase):
    def test_incense_valued_when_vmax_missing(self):
        with_v_no_vmax = FakeCtx(
            hand=["Marnie"], play=["Dragapult V"])
        self.assertGreater(
            _dragapult_value("Evolution Incense", with_v_no_vmax, False), 30)

        complete = FakeCtx(hand=["Marnie"], play=["Dragapult V", "Dragapult VMAX"])
        self.assertLess(
            _dragapult_value("Evolution Incense", complete, False), 15)

    def test_marnie_bonus_when_opponent_hand_bigger(self):
        # hand_size(opp) reads the same canned list in FakeCtx, so patch it.
        ctx = FakeCtx(hand=["a"] * 4)
        base = _dragapult_value("Marnie", ctx, False)
        ctx.hand_size = lambda pid=None: 9 if pid == ctx.opp else 4
        self.assertGreater(_dragapult_value("Marnie", ctx, False), base)

    def test_duplicate_penalty_applies_to_hand_cards(self):
        already_hold = FakeCtx(hand=["Drizzile"], play=[])
        fresh_hand = FakeCtx(hand=["Marnie"], play=[])
        self.assertLess(_dragapult_value("Drizzile", already_hold, True),
                        _dragapult_value("Drizzile", fresh_hand, True))


class PickTests(unittest.TestCase):
    def test_new_active_pick_promotes_ready_attacker(self):
        ctx = FakeCtx(
            bench=[FakeMon("Sobble", energy=0, cost=1),
                   FakeMon("Dragapult VMAX", energy=2, cost=1, eid="v")])
        chosen = max(
            ctx.bench(),
            key=lambda c: _dragapult_pick("Choose your new Active Pok\u00e9mon", ctx, c),
        )
        self.assertEqual(chosen.name_, "Dragapult VMAX")

    def test_new_active_pick_ranks_opp_body_by_gust_value(self):
        ctx = FakeCtx(active_damage=130)
        ko_range = FakeMon("Zigzagoon", owner="p2", hp=90, max_hp=110)
        full = FakeMon("Dragapult VMAX", owner="p2", hp=300, max_hp=320, prize=3)
        prompt = "Choose the opponent's new Active Pok\u00e9mon"
        self.assertGreater(_dragapult_pick(prompt, ctx, ko_range),
                           _dragapult_pick(prompt, ctx, full))

    def test_discard_pick_dumps_least_valuable(self):
        ctx = FakeCtx(hand=["Professor's Research", "Quick Ball"],
                      play=["Dragapult V"])
        junk = FakeMon("Galarian Zigzagoon")
        key_card = FakeMon("Dragapult VMAX")
        prompt = "Discard a card for Quick Ball"
        self.assertGreater(_dragapult_pick(prompt, ctx, junk),
                           _dragapult_pick(prompt, ctx, key_card))

    def test_net_pick_prefers_stuck_utility_active(self):
        ctx = FakeCtx()
        stuck = FakeMon("Galarian Zigzagoon", hp=110, max_hp=110)
        ctx._active = stuck
        other = FakeMon("Sobble", eid="s2")
        prompt = "Choose 1 of your Pok\u00e9mon to put into your hand"
        self.assertGreater(_dragapult_pick(prompt, ctx, stuck),
                           _dragapult_pick(prompt, ctx, other))


class UrshifuBrainTests(unittest.TestCase):
    """Rapid Strike Urshifu VMAX brain (key = the scraped Gabriel list)."""

    def test_registry(self):
        spec = strategy_for("Rapid Strike Urshifu V")
        self.assertIs(spec, RAPID_STRIKE_URSHIFU)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score"):
            self.assertTrue(callable(spec[hook]), hook)

    def test_grf_score_scenarios(self):
        fold_a = FakeMon("Basic", owner="p2", hp=100, max_hp=110, eid="a")
        fold_b = FakeMon("Basic2", owner="p2", hp=110, max_hp=110, eid="b")
        dented = FakeMon("VMAX", owner="p2", hp=200, max_hp=330, eid="d")
        fresh = FakeMon("VMAX2", owner="p2", hp=300, max_hp=330, eid="f")

        ctx = FakeCtx(opp_play=[fold_a, fold_b], opp_active=fold_a)
        self.assertEqual(_rs_grf_score(ctx), 2100.0)      # double fold

        ctx = FakeCtx(opp_play=[fold_a, dented], opp_active=dented)
        self.assertEqual(_rs_grf_score(ctx), 1600.0)      # fold + wrecked

        ctx = FakeCtx(opp_play=[fold_a, fresh], opp_active=fresh)
        self.assertEqual(_rs_grf_score(ctx), 1300.0)      # lone fold

        ctx = FakeCtx(opp_play=[dented, fresh], opp_active=fresh)
        self.assertEqual(_rs_grf_score(ctx), 100.0)       # save the energy

    def test_cheryl_gated_by_vmax_damage(self):
        hurt = FakeMon("Rapid Strike Urshifu VMAX", hp=200, max_hp=330)
        healthy = FakeMon("Rapid Strike Urshifu VMAX", hp=330, max_hp=330,
                          eid="v2")
        self.assertTrue(_rs_allow(
            "UseTrainerCard", "Cheryl", FakeCtx(active=hurt, play=[hurt])))
        self.assertFalse(_rs_allow(
            "UseTrainerCard", "Cheryl", FakeCtx(active=healthy, play=[healthy])))

    def test_switch_gate(self):
        active = FakeMon("Rapid Strike Urshifu VMAX", energy=2, cost=1,
                         eid="v")
        active.children = ["Fighting Energy", "Fighting Energy"]
        bench_vmax = FakeMon("Rapid Strike Urshifu VMAX", energy=2, cost=1,
                             eid="b")
        bench_vmax.children = ["Fighting Energy", "Fighting Energy"]
        opp = [FakeMon("Basic", owner="p2", hp=60, max_hp=110, eid="o1")]

        # ready, not entered, powered bench -> swap for Gale Thrust 150
        ctx = FakeCtx(active=active, bench=[bench_vmax],
                      opp_play=opp, opp_active=opp[0])
        self.assertTrue(_rs_switch_ok(ctx))

        # entered this turn: Gale Thrust is already live -> hold position
        ctx = FakeCtx(active=active, bench=[bench_vmax], entered={"v"},
                      opp_play=opp, opp_active=opp[0])
        self.assertFalse(_rs_switch_ok(ctx))

        # GRF ready with real double-KO targets -> swing instead of swapping
        grf_body = FakeMon("Rapid Strike Urshifu VMAX", energy=3, cost=1,
                           eid="g")
        grf_body.children = ["Rapid Strike Energy", "Fighting Energy",
                             "Fighting Energy"]
        doubles = [FakeMon("Basic", owner="p2", hp=90, max_hp=110, eid="o1"),
                   FakeMon("Basic2", owner="p2", hp=100, max_hp=110, eid="o2")]
        ctx = FakeCtx(active=grf_body, bench=[bench_vmax],
                      opp_play=doubles, opp_active=doubles[0])
        self.assertFalse(_rs_switch_ok(ctx))

    def test_rs_energy_value_counts_double_provider(self):
        ctx = FakeCtx()
        body = FakeMon("Rapid Strike Urshifu VMAX")
        body.children = ["Rapid Strike Energy", "Fighting Energy",
                         "Vitality Band"]
        self.assertEqual(rs_energy_value(ctx, body), 3)

    def test_gale_thrust_scores_the_bonus_window(self):
        active = FakeMon("Rapid Strike Urshifu VMAX", eid="a")
        opp = FakeMon("Target", owner="p2", hp=140, max_hp=330, eid="o")
        ctx = FakeCtx(active=active, opp_play=[opp], opp_active=opp,
                      entered={"a"})
        self.assertEqual(_rs_attack_score("Gale Thrust", 30.0, ctx), 2150.0)
        ctx = FakeCtx(active=active, opp_play=[opp], opp_active=opp)
        self.assertEqual(_rs_attack_score("Gale Thrust", 30.0, ctx), 330.0)

    def test_grf_attack_only_fires_for_real_value(self):
        active = FakeMon("Rapid Strike Urshifu VMAX", eid="a")
        fresh = FakeMon("Big", owner="p2", hp=300, max_hp=330, eid="o")
        ctx = FakeCtx(active=active, opp_play=[fresh], opp_active=fresh)
        self.assertEqual(_rs_attack_score("G-Max Rapid Flow", 0.0, ctx), 100.0)

        fold = FakeMon("Basic", owner="p2", hp=110, max_hp=110, eid="o2")
        ctx = FakeCtx(active=active, opp_play=[fold], opp_active=fold)
        self.assertGreater(_rs_attack_score("G-Max Rapid Flow", 0.0, ctx),
                           1000.0)

    def test_snipe_pick_prefers_fold(self):
        fold = FakeMon("Basic", owner="p2", hp=100, max_hp=110, eid="f")
        fresh = FakeMon("Big", owner="p2", hp=300, max_hp=330, eid="n")
        ctx = FakeCtx(opp_play=[fold, fresh], opp_active=fresh)
        prompt = "Choose 2 PokAcmon to take 120 damage"
        self.assertGreater(_rs_pick(prompt, ctx, fold),
                           _rs_pick(prompt, ctx, fresh))

    def test_hammer_pick_strips_powered_active(self):
        powered = FakeMon("Attacker", owner="p2", hp=300, max_hp=330,
                          energy=2, eid="pa")
        idle = FakeMon("Sitter", owner="p2", hp=300, max_hp=330,
                       energy=0, eid="ib")
        ctx = FakeCtx(opp_play=[powered, idle], opp_active=powered)
        prompt = "Choose 1 of your opponent's Pok\u00e9mon"
        self.assertGreater(_rs_pick(prompt, ctx, powered),
                           _rs_pick(prompt, ctx, idle))

    def test_discard_pick_dumps_hammer_keeps_korrina(self):
        ctx = FakeCtx(hand=["Crushing Hammer", "Korrina's Focus"])
        prompt = "Discard a card for Quick Ball"
        hammer = FakeMon("Crushing Hammer")
        korrina = FakeMon("Korrina's Focus", eid="kf")
        self.assertGreater(_rs_pick(prompt, ctx, hammer),
                           _rs_pick(prompt, ctx, korrina))

    def test_search_prefers_energy_when_attacker_unpowered(self):
        v = FakeMon("Rapid Strike Urshifu V", eid="v")
        v.children = ["Fighting Energy"]           # value 1 < 3
        ctx = FakeCtx(play=[v])
        energy = FakeMon("Rapid Strike Energy", eid="e")
        octillery = FakeMon("Octillery", eid="o")
        self.assertGreater(_rs_search_score(energy, ctx),
                           _rs_search_score(octillery, ctx))

    def test_search_prefers_gap_vmax(self):
        v = FakeMon("Rapid Strike Urshifu V", eid="v")
        ctx = FakeCtx(play=[v], hand=["Crushing Hammer"])
        vmax = FakeMon("Rapid Strike Urshifu VMAX", eid="vm")
        energy = FakeMon("Rapid Strike Energy", eid="e")
        self.assertGreater(_rs_search_score(vmax, ctx),
                           _rs_search_score(energy, ctx))

    def test_promotion_uses_rs_attackers(self):
        ctx = FakeCtx()
        vmax = FakeMon("Rapid Strike Urshifu VMAX", energy=2, cost=1, eid="v")
        crobat = FakeMon("Crobat V", energy=0, cost=1, eid="c")
        self.assertGreater(
            promotion_score(ctx, vmax, attackers=RS_ATTACKERS),
            promotion_score(ctx, crobat, attackers=RS_ATTACKERS))


class ShadowRiderBrainTests(unittest.TestCase):
    def test_registry(self):
        spec = strategy_for("Shadow Rider Calyrex V")
        self.assertIs(spec, SHADOW_RIDER)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score"):
            self.assertTrue(callable(spec[hook]), hook)

    def test_max_geist_scales_with_board_energy(self):
        weak = FakeCtx(
            play=[FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3,
                          eid="a")],
            opp_active=FakeMon("Body", owner="p2", hp=310, max_hp=320))
        strong = FakeCtx(
            play=[FakeMon("Shadow Rider Calyrex VMAX", energy=6, cost=3,
                          eid="a")],
            opp_active=FakeMon("Body", owner="p2", hp=310, max_hp=320))
        self.assertGreater(_sr_attack_score("Max Geist", 10, strong),
                           _sr_attack_score("Max Geist", 10, weak))
        self.assertEqual(_sr_attack_score("Max Geist", 10, weak), 600.0 + 100)

    def test_max_geist_takes_the_ko(self):
        ctx = FakeCtx(
            play=[FakeMon("Shadow Rider Calyrex VMAX", energy=6, cost=3)],
            opp_active=FakeMon("Body", owner="p2", hp=180, max_hp=320,
                               prize=3))
        # 10 + 30*6 = 190 >= 180 -> +1000 KO bonus
        self.assertEqual(_sr_attack_score("Max Geist", 10, ctx), 1790.0)

    def test_astral_barrage_folds_multiple_bodies(self):
        def ctx(*hp):
            bodies = [FakeMon("Body", owner="p2", hp=h, max_hp=320,
                              eid=f"b{i}") for i, h in enumerate(hp)]
            return FakeCtx(opp_play=bodies, opp_active=bodies[0])
        self.assertEqual(_sr_attack_score("Astral Barrage", 0, ctx(40, 50)),
                         1500.0)
        self.assertEqual(_sr_attack_score("Astral Barrage", 0, ctx(40, 300)),
                         1100.0)
        self.assertEqual(_sr_attack_score("Astral Barrage", 0, ctx(300, 310)),
                         300.0)

    def test_crescent_glow_prefers_acceleration_early(self):
        empty = FakeCtx(active=FakeMon("Cresselia", energy=1, cost=1),
                        play=[FakeMon("Cresselia", energy=1, cost=1)])
        self.assertEqual(_sr_attack_score("Crescent Glow", 0, empty), 700.0)
        powered = FakeCtx(
            active=FakeMon("Cresselia", energy=1, cost=1, eid="c"),
            play=[FakeMon("Cresselia", energy=1, cost=1, eid="c"),
                  FakeMon("Shadow Rider Calyrex V", energy=1, cost=3,
                          eid="v")],
            bench=[FakeMon("Shadow Rider Calyrex V", energy=1, cost=3,
                           eid="v")])
        self.assertEqual(_sr_attack_score("Crescent Glow", 0, powered), 250.0)

    def test_g_max_whisk_only_strips_for_the_ko(self):
        def ctx(energy, hp=320):
            return FakeCtx(
                play=[FakeMon("Alcremie VMAX", energy=energy, cost=1)],
                opp_active=FakeMon("Body", owner="p2", hp=hp, max_hp=320))
        # never strips for mere damage -- Adornment (650) stays preferred
        self.assertEqual(_sr_attack_score("G-Max Whisk", 0, ctx(3)), 300.0)
        self.assertEqual(_sr_attack_score("G-Max Whisk", 0, ctx(6, hp=400)),
                         300.0)
        self.assertGreater(_sr_attack_score("Adornment", 0, ctx(6, hp=400)),
                           _sr_attack_score("G-Max Whisk", 0,
                                            ctx(6, hp=400)))
        # folds the Active outright -> then the strip is worth it
        self.assertEqual(_sr_attack_score("G-Max Whisk", 0, ctx(5, hp=250)),
                         1800.0)

    def test_energy_target_ladder_spreads_hungry_first(self):
        active = FakeMon("Shadow Rider Calyrex VMAX", energy=0, cost=3,
                         eid="a")
        bench_v = FakeMon("Shadow Rider Calyrex V", energy=0, cost=3,
                          eid="b")
        ctx = FakeCtx(active=active, play=[active, bench_v],
                      bench=[bench_v])
        self.assertGreater(_sr_energy_target_score(ctx, active),
                           _sr_energy_target_score(ctx, bench_v))
        # satisfied active loses to a hungry bench body
        fed = FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3, eid="a")
        hungry = FakeMon("Shadow Rider Calyrex V", energy=0, cost=3, eid="b")
        ctx2 = FakeCtx(active=fed, play=[fed, hungry], bench=[hungry])
        self.assertGreater(_sr_energy_target_score(ctx2, hungry),
                           _sr_energy_target_score(ctx2, fed))
        # Crobat never gets the energy
        crobat = FakeMon("Crobat V", energy=0, cost=1, eid="c")
        ctx3 = FakeCtx(play=[hungry, crobat])
        self.assertGreater(_sr_energy_target_score(ctx3, hungry),
                           _sr_energy_target_score(ctx3, crobat))

    def test_retreat_gate_compares_output(self):
        # utility Active, powered VMAX on the bench -> get out of the way
        cress = FakeMon("Cresselia", energy=1, cost=1, eid="c")
        vmax = FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3,
                       eid="v")
        self.assertTrue(_sr_retreat_ok(
            FakeCtx(active=cress, play=[cress, vmax], bench=[vmax])))
        # two equal VMAXes -> keep the Active (no free churn)
        a = FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3, eid="a")
        b = FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3, eid="b")
        self.assertFalse(_sr_retreat_ok(
            FakeCtx(active=a, play=[a, b], bench=[b])))
        # bench must be clearly better before dumping a ready attacker
        v = FakeMon("Shadow Rider Calyrex V", energy=1, cost=1, eid="v1")
        vm = FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3,
                     eid="vm")
        self.assertTrue(_sr_retreat_ok(
            FakeCtx(active=v, play=[v, vm], bench=[vm])))
        # nobody ready -> stay put
        dead = FakeMon("Crobat V", energy=0, cost=1, eid="c")
        cress = FakeMon("Cresselia", energy=0, cost=1, eid="c2")
        self.assertFalse(_sr_retreat_ok(
            FakeCtx(active=dead, play=[dead, cress], bench=[cress])))

    def test_alcremie_yields_to_ready_vmax_unless_it_can_close(self):
        # Alcremie active (no KO available) + powered VMAX -> swap to Max Geist
        alcremie = FakeMon("Alcremie VMAX", energy=3, cost=1, eid="al")
        vmax = FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3,
                       eid="vm")
        self.assertTrue(_sr_retreat_ok(FakeCtx(
            active=alcremie, play=[alcremie, vmax], bench=[vmax],
            opp_active=FakeMon("Body", owner="p2", hp=400, max_hp=400))))
        # ... but she stays when Whisk folds the Active right now
        self.assertFalse(_sr_retreat_ok(FakeCtx(
            active=alcremie, play=[alcremie, vmax], bench=[vmax],
            opp_active=FakeMon("Body", owner="p2", hp=150, max_hp=320))))

    def test_research_and_marnie_gates(self):
        self.assertTrue(_sr_allow("UseTrainerCard", "Professor's Research",
                                  FakeCtx(hand=["x"] * 5)))
        self.assertFalse(_sr_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 6)))
        ctx = FakeCtx(hand=["x"] * 6)
        ctx.hand_size = lambda pid=None: 4 if pid == "p2" else 6
        self.assertFalse(_sr_allow("UseTrainerCard", "Marnie", ctx))
        ctx.hand_size = lambda pid=None: 6 if pid == "p2" else 6
        self.assertTrue(_sr_allow("UseTrainerCard", "Marnie", ctx))

    def test_deck_runway_gates_stop_self_mill(self):
        # Research can mill 7: need real runway
        self.assertTrue(_sr_allow("UseTrainerCard", "Professor's Research",
                                  FakeCtx(hand=["x"] * 5, deck=20)))
        self.assertFalse(_sr_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 5, deck=10)))
        # Underworld Door's draw 2 is the biggest burner
        self.assertTrue(_sr_allow("UsePokemonAbility", "Underworld Door",
                                  FakeCtx(deck=20)))
        self.assertFalse(_sr_allow("UsePokemonAbility", "Underworld Door",
                                   FakeCtx(deck=8)))
        # searches can be the last card out
        for card in ("Fog Crystal", "Quick Ball", "Evolution Incense"):
            self.assertTrue(_sr_allow("UseTrainerCard", card,
                                      FakeCtx(deck=6)), card)
            self.assertFalse(_sr_allow("UseTrainerCard", card,
                                       FakeCtx(deck=5)), card)
        # Marnie's hand goes to the deck bottom -- only the draw needs room
        self.assertTrue(_sr_allow("UseTrainerCard", "Marnie",
                                  FakeCtx(hand=["x"], deck=6)))
        self.assertFalse(_sr_allow("UseTrainerCard", "Marnie",
                                   FakeCtx(hand=["x"], deck=5)))

    def test_boss_gate_needs_a_window_or_scratch(self):
        def boss_ctx(hp):
            body = FakeMon("Body", owner="p2", hp=hp, max_hp=320)
            return FakeCtx(
                active=FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3),
                play=[FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3)],
                opp_active=body, opp_play=[body])
        self.assertFalse(_sr_allow("UseTrainerCard", "Boss's Orders",
                                   boss_ctx(320)))
        self.assertTrue(_sr_allow("UseTrainerCard", "Boss's Orders",
                                  boss_ctx(90)))
        self.assertTrue(_sr_allow("UseTrainerCard", "Boss's Orders",
                                  boss_ctx(300)))

    def test_training_court_gates(self):
        self.assertTrue(_sr_allow(
            "DefaultStadiumPlayAbility", "Training Court",
            FakeCtx(stadium="Path to the Peak",
                    discard=["Psychic Energy"])))
        self.assertFalse(_sr_allow(
            "DefaultStadiumPlayAbility", "Training Court",
            FakeCtx(stadium="Training Court",
                    discard=["Psychic Energy"])))
        self.assertFalse(_sr_allow(
            "DefaultStadiumPlayAbility", "Training Court",
            FakeCtx(stadium="Path to the Peak", discard=[])))

    def test_ability_allowlist(self):
        for ability in ("Underworld Door", "Cruel Charge", "Training Court"):
            self.assertTrue(_sr_allow("UsePokemonAbility", ability,
                                      FakeCtx()), ability)
        self.assertFalse(_sr_allow("UsePokemonAbility", "Intrepid Sword",
                                   FakeCtx()))

    def test_value_prefers_gap_vmax_and_starved_energy(self):
        gap = FakeCtx(play=["Shadow Rider Calyrex V"])
        self.assertGreater(_sr_value("Shadow Rider Calyrex VMAX", gap), 30)
        full = FakeCtx(play=["Shadow Rider Calyrex V", "Shadow Rider Calyrex VMAX"])
        self.assertLess(_sr_value("Shadow Rider Calyrex VMAX", full), 15)
        starved = FakeCtx(hand=[])
        stocked = FakeCtx(hand=["Psychic Energy"] * 3)
        self.assertGreater(_sr_value("Psychic Energy", starved),
                           _sr_value("Psychic Energy", stocked))
        self.assertEqual(_sr_value("Psychic Energy", starved), 28.0)

    def test_search_uses_value(self):
        ctx = FakeCtx(play=["Shadow Rider Calyrex V"])
        vmax = FakeMon("Shadow Rider Calyrex VMAX", eid="vm")
        energy = FakeMon("Psychic Energy", eid="e")
        self.assertGreater(_sr_search_score(vmax, ctx),
                           _sr_search_score(energy, ctx))

    def test_search_prefers_gap_v_over_energy_when_starved(self):
        ctx = FakeCtx(play=[])
        v = FakeMon("Shadow Rider Calyrex V", eid="v")
        energy = FakeMon("Psychic Energy", eid="e")
        self.assertGreater(_sr_search_score(v, ctx),
                           _sr_search_score(energy, ctx))

    def test_pick_promotes_and_gusts(self):
        ready = FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3,
                        eid="a")
        crobat = FakeMon("Crobat V", energy=0, cost=1, eid="c")
        ctx = FakeCtx()
        self.assertGreater(
            promotion_score(ctx, ready, attackers=SR_ATTACKERS),
            promotion_score(ctx, crobat, attackers=SR_ATTACKERS))
        in_range = FakeMon("Body", owner="p2", hp=90, max_hp=320, eid="g1")
        fresh = FakeMon("Body", owner="p2", hp=320, max_hp=320, eid="g2")
        gust_ctx = FakeCtx(
            active=FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3),
            play=[FakeMon("Shadow Rider Calyrex VMAX", energy=3, cost=3)])
        self.assertGreater(
            _sr_pick("Choose your opponent's new Active Pokémon",
                     gust_ctx, in_range),
            _sr_pick("Choose your opponent's new Active Pokémon",
                     gust_ctx, fresh))

    def test_pick_snipes_fold_before_dent(self):
        ctx = FakeCtx()
        fold = FakeMon("Body", owner="p2", hp=100, max_hp=320, eid="s1")
        fresh = FakeMon("Body", owner="p2", hp=320, max_hp=320, eid="s2")
        psylaser = "Choose 1 of your opponent's Pokémon to take 120 damage"
        self.assertGreater(_sr_pick(psylaser, ctx, fold),
                           _sr_pick(psylaser, ctx, fresh))
        barrage_fold = FakeMon("Body", owner="p2", hp=40, max_hp=320,
                               eid="b1")
        self.assertGreater(
            _sr_pick("Choose 2 of your opponent's Pokémon", ctx,
                     barrage_fold),
            _sr_pick("Choose 2 of your opponent's Pokémon", ctx, fresh))

    def test_pick_energy_attaches_via_ladder(self):
        active = FakeMon("Shadow Rider Calyrex VMAX", energy=0, cost=3,
                         eid="a")
        bench_v = FakeMon("Shadow Rider Calyrex V", energy=0, cost=3,
                          eid="b")
        ctx = FakeCtx(active=active, play=[active, bench_v],
                      bench=[bench_v])
        self.assertEqual(
            _sr_pick("Choose the Benched Psychic Pokémon to attach it to",
                     ctx, bench_v),
            _sr_energy_target_score(ctx, bench_v))
        energy = FakeMon("Psychic Energy", eid="e")
        self.assertEqual(
            _sr_pick("Choose a Psychic Energy card to attach", ctx, energy),
            100.0)

    def test_pick_discard_dumps_least_valuable(self):
        ctx = FakeCtx(hand=["Professor's Research", "Pal Pad"])
        research = FakeMon("Professor's Research", eid="r")
        palpad = FakeMon("Pal Pad", eid="p")
        prompt = "Choose a card to discard."
        self.assertLess(_sr_pick(prompt, ctx, research),
                        _sr_pick(prompt, ctx, palpad))

    def test_pick_promotes_ready_body_over_utility(self):
        ready = FakeMon("Shadow Rider Calyrex V", energy=3, cost=3, owner="p1",
                        eid="p1v")
        utility = FakeMon("Crobat V", energy=0, cost=1, owner="p1", eid="p1c")
        ctx = FakeCtx()
        self.assertGreater(
            _sr_pick("Choose your new Active Pokémon", ctx, ready),
            _sr_pick("Choose your new Active Pokémon", ctx, utility))


class CorviknightBrainTests(unittest.TestCase):
    def test_registry(self):
        spec = strategy_for("Bronzor")
        self.assertIs(spec, CORVIKNIGHT_BRONZONG)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score"):
            self.assertTrue(callable(spec[hook]), hook)

    # -- output / self-lock math ----------------------------------------
    def test_hurricane_output_and_lock(self):
        ready = FakeMon("Corviknight VMAX", energy=3, cost=3)
        hungry = FakeMon("Corviknight VMAX", energy=2, cost=3)
        self.assertEqual(_cv_output(FakeCtx(), ready), 240)
        self.assertEqual(_cv_output(FakeCtx(), hungry), 0)
        locked = FakeCtx(locked=("G-Max Hurricane",))
        self.assertEqual(_cv_output(locked, ready), 0)

    def test_v_falls_back_to_clutch_when_locked(self):
        body = FakeMon("Corviknight V", energy=3, cost=1)
        locked = FakeCtx(locked=("Sky Hurricane",))
        self.assertEqual(_cv_output(FakeCtx(), body), 190)
        self.assertEqual(_cv_output(locked, body), 30)
        # one energy is enough to Clutch; zero is stuck
        self.assertEqual(_cv_output(FakeCtx(), FakeMon("Corviknight V",
                                                       energy=1, cost=1)), 30)
        self.assertEqual(_cv_output(FakeCtx(), FakeMon("Corviknight V",
                                                       energy=0, cost=1)), 0)

    def test_zacian_needs_three_and_locks_out(self):
        ready = FakeMon("Zacian V", energy=3, cost=3)
        self.assertEqual(_cv_output(FakeCtx(), ready), 230)
        self.assertEqual(_cv_output(FakeCtx(), FakeMon("Zacian V", energy=2,
                                                       cost=3)), 0)
        locked = FakeCtx(locked=("Brave Blade",))
        self.assertEqual(_cv_output(locked, ready), 0)

    def test_utility_bodies_score_zero_unless_fully_fed(self):
        self.assertEqual(_cv_output(FakeCtx(), FakeMon("Bronzor",
                                                       energy=3, cost=1)), 0)
        self.assertEqual(_cv_output(FakeCtx(), FakeMon("Bronzong",
                                                       energy=3, cost=3)), 70)
        self.assertEqual(_cv_output(FakeCtx(), FakeMon("Bronzong",
                                                       energy=2, cost=3)), 0)

    # -- attack bucket ----------------------------------------------------
    def test_hurricane_is_the_default_swing(self):
        # Hurricane (940) outranks Brave Blade (780) and Sky Hurricane (640)
        self.assertEqual(_cv_attack_score("G-Max Hurricane", 0, FakeCtx()),
                         940.0)
        self.assertEqual(_cv_attack_score("Brave Blade", 0, FakeCtx()), 780.0)
        self.assertEqual(_cv_attack_score("Sky Hurricane", 0, FakeCtx()), 640.0)

    def test_attacks_take_the_ko(self):
        ctx = FakeCtx(opp_active=FakeMon("Body", owner="p2", hp=200,
                                         max_hp=320, prize=3))
        self.assertEqual(_cv_attack_score("G-Max Hurricane", 0, ctx),
                         700.0 + 240 + 1000)
        poke = FakeCtx(opp_active=FakeMon("Body", owner="p2", hp=30,
                                          max_hp=320, prize=1))
        self.assertEqual(_cv_attack_score("Clutch", 0, poke), 180.0 + 1000)
        no_window = FakeCtx(opp_active=FakeMon("Body", owner="p2", hp=500,
                                               max_hp=500, prize=1))
        self.assertEqual(_cv_attack_score("Clutch", 0, no_window), 180.0)

    # -- energy ladder -----------------------------------------------------
    def test_energy_ladder_feeds_active_then_hungry(self):
        active = FakeMon("Corviknight VMAX", energy=0, cost=3, eid="a")
        bench_v = FakeMon("Corviknight V", energy=0, cost=1, eid="b")
        ctx = FakeCtx(active=active, play=[active, bench_v],
                      bench=[bench_v])
        self.assertGreater(_cv_energy_target_score(ctx, active),
                           _cv_energy_target_score(ctx, bench_v))
        # satisfied active yields to a hungry bench attacker
        fed = FakeMon("Corviknight VMAX", energy=3, cost=3, eid="a")
        hungry = FakeMon("Corviknight V", energy=0, cost=1, eid="b")
        ctx2 = FakeCtx(active=fed, play=[fed, hungry], bench=[hungry])
        self.assertGreater(_cv_energy_target_score(ctx2, hungry),
                           _cv_energy_target_score(ctx2, fed))
        # utility bodies never get the attach
        bronzor = FakeMon("Bronzor", energy=0, cost=1, eid="z")
        ctx3 = FakeCtx(active=bronzor, play=[bronzor, bench_v],
                       bench=[bench_v])
        self.assertGreater(_cv_energy_target_score(ctx3, bench_v),
                           _cv_energy_target_score(ctx3, bronzor))

    # -- Metal Transfer ----------------------------------------------------
    def test_transfer_gate_feeds_empty_active_only(self):
        active = FakeMon("Corviknight VMAX", energy=0, cost=3, eid="a")
        fed_bench = FakeMon("Corviknight V", energy=2, cost=1, eid="b")
        self.assertTrue(_cv_transfer_ok(FakeCtx(
            active=active, play=[active, fed_bench], bench=[fed_bench])))
        # active already holds energy: source pool starts there -> no ping-pong
        active1 = FakeMon("Corviknight VMAX", energy=1, cost=3, eid="a")
        self.assertFalse(_cv_transfer_ok(FakeCtx(
            active=active1, play=[active1, fed_bench], bench=[fed_bench])))
        # utility Active never gets fed by the ability
        bronzong = FakeMon("Bronzong", energy=0, cost=3, eid="z")
        self.assertFalse(_cv_transfer_ok(FakeCtx(
            active=bronzong, play=[bronzong, fed_bench], bench=[fed_bench])))
        # bench has nothing to give
        empty = FakeMon("Corviknight V", energy=0, cost=1, eid="b")
        self.assertFalse(_cv_transfer_ok(FakeCtx(
            active=active, play=[active, empty], bench=[empty])))

    # -- retreat / switch gates ------------------------------------------
    def test_retreat_swaps_locked_or_stuck_active(self):
        locked = FakeCtx(locked=("G-Max Hurricane",))
        vmax = FakeMon("Corviknight VMAX", energy=3, cost=3, eid="vm")
        v = FakeMon("Corviknight V", energy=3, cost=1, eid="v")
        self.assertTrue(_cv_retreat_ok(FakeCtx(
            locked=locked.locked_titles, active=vmax, play=[vmax, v],
            bench=[v])))
        # two comparable bodies -> keep the Active (no free churn)
        a = FakeMon("Corviknight VMAX", energy=3, cost=3, eid="a")
        b = FakeMon("Corviknight VMAX", energy=3, cost=3, eid="b")
        self.assertFalse(_cv_retreat_ok(
            FakeCtx(active=a, play=[a, b], bench=[b])))
        # heavily damaged attacker yields to a fresh one
        hurt = FakeMon("Corviknight VMAX", energy=3, cost=3, hp=190,
                       max_hp=320, eid="h")
        self.assertTrue(_cv_retreat_ok(FakeCtx(
            active=hurt, play=[hurt, v], bench=[v])))
        # nobody ready -> stay put
        dead = FakeMon("Corviknight VMAX", energy=0, cost=3, eid="d")
        bronzor = FakeMon("Bronzor", energy=0, cost=1, eid="z")
        self.assertFalse(_cv_retreat_ok(
            FakeCtx(active=dead, play=[dead, bronzor], bench=[bronzor])))

    def test_switch_gate_unsticks_or_preserves(self):
        locked = FakeCtx(locked=("G-Max Hurricane",))
        vmax = FakeMon("Corviknight VMAX", energy=3, cost=3, eid="vm")
        v = FakeMon("Corviknight V", energy=3, cost=1, eid="v")
        self.assertTrue(_cv_switch_ok(FakeCtx(
            locked=locked.locked_titles, active=vmax, play=[vmax, v],
            bench=[v])))
        # fresh, unstuck attacker -> save the Switch
        self.assertFalse(_cv_switch_ok(
            FakeCtx(active=vmax, play=[vmax, v], bench=[v])))
        # damaged attacker + ready backup -> swap before it dies
        hurt = FakeMon("Corviknight VMAX", energy=3, cost=3, hp=190,
                       max_hp=320, eid="h")
        self.assertTrue(_cv_switch_ok(FakeCtx(
            active=hurt, play=[hurt, v], bench=[v])))

    # -- action gates ------------------------------------------------------
    def test_research_gates(self):
        self.assertTrue(_cv_allow("UseTrainerCard", "Professor's Research",
                                  FakeCtx(hand=["x"] * 5)))
        self.assertFalse(_cv_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 6)))
        self.assertFalse(_cv_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 5, deck=10)))
        self.assertTrue(_cv_allow("UseTrainerCard", "Professor's Research",
                                  FakeCtx(hand=["x"] * 5, deck=11)))

    def test_marnie_needs_full_hand_or_disruption(self):
        ctx = FakeCtx(hand=["x"] * 6)
        ctx.hand_size = lambda pid=None: 4 if pid == "p2" else 6
        self.assertFalse(_cv_allow("UseTrainerCard", "Marnie", ctx))
        ctx.hand_size = lambda pid=None: 6 if pid == "p2" else 6
        self.assertTrue(_cv_allow("UseTrainerCard", "Marnie", ctx))
        # hand goes to the deck bottom: small hand needs no runway
        self.assertTrue(_cv_allow("UseTrainerCard", "Marnie",
                                  FakeCtx(hand=["x"], deck=4)))

    def test_zinnia_gates(self):
        four = [FakeMon("Body", owner="p2", eid=f"o{i}") for i in range(4)]
        three = four[:3]
        self.assertTrue(_cv_allow("UseTrainerCard", "Zinnia's Resolve",
                                  FakeCtx(opp_play=four, deck=40)))
        self.assertFalse(_cv_allow("UseTrainerCard", "Zinnia's Resolve",
                                   FakeCtx(opp_play=three, deck=40)))
        self.assertFalse(_cv_allow("UseTrainerCard", "Zinnia's Resolve",
                                   FakeCtx(opp_play=four, deck=7)))

    def test_search_deck_runway_gates(self):
        for card in ("Quick Ball", "Great Ball", "Evolution Incense"):
            self.assertTrue(_cv_allow("UseTrainerCard", card,
                                      FakeCtx(deck=6)), card)
            self.assertFalse(_cv_allow("UseTrainerCard", card,
                                       FakeCtx(deck=5)), card)

    def test_cheryl_gate_waits_for_real_damage(self):
        hurt = FakeMon("Corviknight VMAX", hp=190, max_hp=320, eid="h")
        fresh = FakeMon("Corviknight VMAX", hp=320, max_hp=320, eid="f")
        self.assertTrue(_cv_allow("UseTrainerCard", "Cheryl",
                                  FakeCtx(play=[hurt])))
        self.assertFalse(_cv_allow("UseTrainerCard", "Cheryl",
                                   FakeCtx(play=[fresh])))

    def test_boss_gate_needs_window_or_scratch(self):
        def boss_ctx(hp, energy=3):
            body = FakeMon("Body", owner="p2", hp=hp, max_hp=320, eid="b")
            return FakeCtx(
                active=FakeMon("Corviknight VMAX", energy=energy, cost=3,
                               eid="a"),
                opp_active=body, opp_play=[body])
        self.assertTrue(_cv_allow("UseTrainerCard", "Boss's Orders",
                                  boss_ctx(200)))      # in Hurricane range
        self.assertTrue(_cv_allow("UseTrainerCard", "Boss's Orders",
                                  boss_ctx(300)))      # already scratched
        self.assertFalse(_cv_allow("UseTrainerCard", "Boss's Orders",
                                   boss_ctx(320)))     # nothing to gain
        self.assertFalse(_cv_allow("UseTrainerCard", "Boss's Orders",
                                   boss_ctx(200, energy=0)))  # can't swing

    def test_switch_and_tool_gates(self):
        ready = FakeMon("Corviknight VMAX", energy=3, cost=3, eid="v")
        self.assertFalse(_cv_allow("UseTrainerCard", "Switch",
                                   FakeCtx(active=ready, play=[ready],
                                           bench=[ready])))
        self.assertTrue(_cv_allow("UseTrainerCard", "Big Charm",
                                  FakeCtx(play=[ready])))
        self.assertFalse(_cv_allow("UseTrainerCard", "Big Charm",
                                   FakeCtx(play=[FakeMon("Bronzor",
                                                         eid="z")])))

    def test_crystal_cave_stadium_gate(self):
        self.assertTrue(_cv_allow(
            "DefaultStadiumPlayAbility", "Crystal Cave",
            FakeCtx(stadium="Path to the Peak")))
        self.assertFalse(_cv_allow(
            "DefaultStadiumPlayAbility", "Crystal Cave",
            FakeCtx(stadium="Crystal Cave")))

    def test_ability_allowlist(self):
        active = FakeMon("Corviknight VMAX", energy=0, cost=3, eid="a")
        bench_v = FakeMon("Corviknight V", energy=2, cost=1, eid="b")
        good = FakeCtx(active=active, play=[active, bench_v],
                       bench=[bench_v])
        self.assertTrue(_cv_allow("UsePokemonAbility", "Metal Transfer",
                                  good))
        self.assertFalse(_cv_allow("UsePokemonAbility", "Metal Transfer",
                                   FakeCtx(active=active, play=[active],
                                           bench=[FakeMon("Corviknight V",
                                                          energy=0, eid="b")])))
        self.assertTrue(_cv_allow("UsePokemonAbility", "Crystal Cave",
                                  FakeCtx()))
        self.assertFalse(_cv_allow("UsePokemonAbility", "Intrepid Sword",
                                   FakeCtx()))

    # -- value / search ----------------------------------------------------
    def test_value_prefers_gap_piece(self):
        gap = FakeCtx(play=["Corviknight V"])
        self.assertGreater(_cv_value("Corviknight VMAX", gap), 30)
        full = FakeCtx(play=["Corviknight V", "Corviknight VMAX"])
        self.assertLess(_cv_value("Corviknight VMAX", full), 15)
        engine_gap = FakeCtx(play=["Corviknight V"])
        self.assertGreater(_cv_value("Bronzor", engine_gap), 25)
        engine_full = FakeCtx(play=["Bronzor", "Bronzong"])
        self.assertLess(_cv_value("Bronzor", engine_full), 10)

    def test_value_prefers_starved_metal_energy(self):
        starved = FakeCtx(hand=[])
        stocked = FakeCtx(hand=["Metal Energy", "Metal Energy",
                                "Metal Energy"])
        self.assertGreater(_cv_value("Metal Energy", starved),
                           _cv_value("Metal Energy", stocked))
        self.assertEqual(_cv_value("Metal Energy", starved), 26.0)

    def test_value_scales_cheryl_with_damage(self):
        hurt = FakeCtx(play=[FakeMon("Corviknight VMAX", hp=220,
                                     max_hp=320, eid="h")])
        fresh = FakeCtx(play=[FakeMon("Corviknight VMAX", hp=320,
                                      max_hp=320, eid="f")])
        self.assertGreater(_cv_value("Cheryl", hurt),
                           _cv_value("Cheryl", fresh))

    def test_search_score_uses_value(self):
        ctx = FakeCtx(play=["Corviknight V"])
        vmax = FakeMon("Corviknight VMAX", eid="vm")
        tool = FakeMon("Big Charm", eid="t")
        self.assertGreater(_cv_search_score(vmax, ctx),
                           _cv_search_score(tool, ctx))

    def test_bench_score_orders_setup(self):
        # first Bronzor before a second Zacian, utility last once evolved
        self.assertGreater(_cv_bench_score("Bronzor", FakeCtx(play=[])),
                           _cv_bench_score("Zacian V", FakeCtx(play=[])))
        full = FakeCtx(play=["Bronzor", "Bronzong"])
        self.assertGreater(_cv_bench_score("Zacian V", full),
                           _cv_bench_score("Bronzor", full))
        # evolve VMAX ahead of Bronzong
        self.assertGreater(
            _cv_action_score("EvolvePokemonPlayAbility",
                             "Corviknight VMAX", FakeCtx()),
            _cv_action_score("EvolvePokemonPlayAbility", "Bronzong",
                             FakeCtx()))

    # -- target / pick -----------------------------------------------------
    def test_tool_and_evolve_targets(self):
        active = FakeMon("Corviknight VMAX", energy=0, cost=3, eid="a")
        ctx = FakeCtx(active=active, play=[active])
        tool_on_active = _cv_target_score("DefaultToolPlayAbility",
                                          "Big Charm", ctx, active.entity_id)
        bench_v = FakeMon("Corviknight V", energy=0, cost=1, eid="b")
        ctx2 = FakeCtx(active=active, play=[active, bench_v],
                       bench=[bench_v])
        tool_on_bench = _cv_target_score("DefaultToolPlayAbility",
                                         "Big Charm", ctx2,
                                         bench_v.entity_id)
        self.assertGreater(tool_on_active, tool_on_bench)

    def test_pick_promotes_over_locked_body(self):
        locked = FakeCtx(locked=("G-Max Hurricane",))
        vmax = FakeMon("Corviknight VMAX", energy=3, cost=3, eid="vm")
        v = FakeMon("Corviknight V", energy=2, cost=1, owner="p1", eid="pv")
        prompt = "Choose your new Active Pok\u00e9mon"
        self.assertGreater(_cv_pick(prompt, locked, v),
                           _cv_pick(prompt, locked, vmax))

    def test_pick_gusts_into_hurricane_range(self):
        ctx = FakeCtx(
            active=FakeMon("Corviknight VMAX", energy=3, cost=3, eid="a"),
            play=[FakeMon("Corviknight VMAX", energy=3, cost=3, eid="a")])
        in_range = FakeMon("Body", owner="p2", hp=200, max_hp=320, eid="g1")
        fresh = FakeMon("Body", owner="p2", hp=320, max_hp=320, eid="g2")
        prompt = "Choose your opponent's new Active Pok\u00e9mon"
        self.assertGreater(_cv_pick(prompt, ctx, in_range),
                           _cv_pick(prompt, ctx, fresh))

    def test_pick_energy_targets_use_ladder(self):
        active = FakeMon("Corviknight VMAX", energy=0, cost=3, eid="a")
        bench_v = FakeMon("Corviknight V", energy=0, cost=1, eid="b")
        ctx = FakeCtx(active=active, play=[active, bench_v],
                      bench=[bench_v])
        saucer = "Choose a Benched Metal Pok\u00e9mon to attach it to"
        self.assertEqual(_cv_pick(saucer, ctx, bench_v),
                         _cv_energy_target_score(ctx, bench_v))
        transfer = "Choose a Pok\u00e9mon to move the Energy to"
        self.assertEqual(_cv_pick(transfer, ctx, active),
                         _cv_energy_target_score(ctx, active))
        energy = FakeMon("Metal Energy", eid="e")
        self.assertEqual(
            _cv_pick("Choose a Metal Energy card to attach", ctx, energy),
            100.0)

    def test_pick_discard_dumps_least_valuable(self):
        ctx = FakeCtx(hand=["Professor's Research", "Pal Pad"])
        research = FakeMon("Professor's Research", eid="r")
        palpad = FakeMon("Pal Pad", eid="p")
        prompt = "Choose a card to discard."
        self.assertLess(_cv_pick(prompt, ctx, research),
                        _cv_pick(prompt, ctx, palpad))


class EternatusBrainTests(unittest.TestCase):
    def test_eternatus_brain_registered(self):
        spec = strategy_for("Eternatus V")
        self.assertIs(spec, ETERNATUS_VMAX)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score",
                     "counter_plan"):
            self.assertTrue(callable(spec[hook]), hook)

    # -- Dread End math --------------------------------------------------
    def test_dread_end_scales_with_dark_bodies(self):
        vmax = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="vm")
        self.assertEqual(
            _et_dread_end(FakeCtx(active=vmax, play=[vmax])), 30)
        nine = [vmax] + [FakeMon("Galarian Zigzagoon", eid=f"z{i}")
                         for i in range(8)]
        self.assertEqual(_et_dread_end(FakeCtx(active=vmax, play=nine)), 270)
        # non-Darkness bodies don't count
        mixed = [vmax, "Radiant Greninja"]
        self.assertEqual(_et_dread_end(FakeCtx(active=vmax, play=mixed)), 30)

    def test_dread_end_attack_scores_and_ko_bonus(self):
        vmax = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="vm")
        opp = FakeMon("Body", owner="p2", hp=250, max_hp=320, eid="o")
        nine = [vmax] + [FakeMon("Galarian Zigzagoon", eid=f"z{i}")
                         for i in range(8)]
        ctx = FakeCtx(active=vmax, play=nine, opp_active=opp,
                      opp_play=[opp])
        self.assertGreaterEqual(_et_attack_score("Dread End", 0, ctx),
                                1700)     # 700 + 270 + KO bonus
        five = [vmax] + [FakeMon("Galarian Zigzagoon", eid=f"z{i}")
                         for i in range(4)]
        ctx2 = FakeCtx(active=vmax, play=five, opp_active=opp,
                       opp_play=[opp])
        self.assertEqual(_et_attack_score("Dread End", 0, ctx2), 850.0)

    def test_utility_bodies_have_no_output(self):
        crobat = FakeMon("Crobat V", energy=2, cost=1, eid="c")
        ctx = FakeCtx(active=crobat, play=[crobat])
        self.assertEqual(_et_output(ctx, crobat), 0)
        self.assertEqual(_et_strike_damage(ctx), 0)

    def test_power_accelerator_prefers_accel_when_hungry(self):
        v = FakeMon("Eternatus V", energy=1, cost=1, eid="v")
        bench_v = FakeMon("Eternatus V", energy=0, cost=1, eid="bv")
        opp = FakeMon("Body", owner="p2", hp=300, max_hp=320, eid="o")
        hungry = FakeCtx(active=v, play=[v, bench_v], bench=[bench_v],
                         opp_active=opp, opp_play=[opp],
                         hand=["Darkness Energy"])
        stocked = FakeCtx(active=v, play=[v, bench_v], bench=[bench_v],
                          opp_active=opp, opp_play=[opp], hand=[])
        self.assertGreater(_et_attack_score("Power Accelerator", 0, hungry),
                           _et_attack_score("Power Accelerator", 0, stocked))

    def test_dynamax_cannon_bonus_vs_vmax(self):
        v = FakeMon("Eternatus V", energy=4, cost=4, eid="v")
        big = FakeMon("Opp VMAX", owner="p2", hp=300, max_hp=340, eid="o1")
        plain = FakeMon("Body", owner="p2", hp=300, max_hp=320, eid="o2")
        vs_vmax = _et_attack_score(
            "Dynamax Cannon", 0,
            FakeCtx(active=v, play=[v], opp_active=big, opp_play=[big]))
        vs_plain = _et_attack_score(
            "Dynamax Cannon", 0,
            FakeCtx(active=v, play=[v], opp_active=plain, opp_play=[plain]))
        self.assertGreater(vs_vmax, vs_plain)

    def test_assault_gate_only_scores_after_entry(self):
        hoopa = FakeMon("Hoopa", energy=1, cost=1, eid="h")
        opp = FakeMon("Body", owner="p2", hp=80, max_hp=120, eid="o")
        on_entry = FakeCtx(active=hoopa, play=[hoopa], opp_active=opp,
                           opp_play=[opp], entered={"h"})
        self.assertGreaterEqual(_et_attack_score("Assault Gate", 0,
                                                 on_entry), 1440)
        off = FakeCtx(active=hoopa, play=[hoopa], opp_active=opp,
                      opp_play=[opp])
        self.assertEqual(_et_attack_score("Assault Gate", 0, off), 0.0)

    # -- action gates ------------------------------------------------------
    def test_research_gates(self):
        self.assertTrue(_et_allow("UseTrainerCard", "Professor's Research",
                                  FakeCtx(hand=["x"] * 5, deck=40)))
        self.assertFalse(_et_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 6, deck=40)))
        self.assertFalse(_et_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 5, deck=10)))

    def test_marnie_needs_soft_hand_disruption_and_runway(self):
        self.assertTrue(_et_allow("UseTrainerCard", "Marnie",
                                  FakeCtx(hand=["x"] * 2, deck=40)))
        ctx = FakeCtx(hand=["x"] * 7)
        ctx.hand_size = lambda pid=None: 4 if pid == "p2" else 7
        self.assertFalse(_et_allow("UseTrainerCard", "Marnie", ctx))
        ctx.hand_size = lambda pid=None: 6 if pid == "p2" else 7
        self.assertTrue(_et_allow("UseTrainerCard", "Marnie", ctx))
        self.assertFalse(_et_allow("UseTrainerCard", "Marnie",
                                   FakeCtx(hand=["x"] * 2, deck=4)))

    def test_search_deck_runway_gates(self):
        for card in ("Quick Ball", "Great Ball", "Evolution Incense"):
            self.assertTrue(_et_allow("UseTrainerCard", card,
                                      FakeCtx(deck=6)), card)
            self.assertFalse(_et_allow("UseTrainerCard", card,
                                       FakeCtx(deck=5)), card)

    def test_boss_gate_needs_current_dread_end(self):
        def boss_ctx(hp, energy=2, bodies=1):
            body = FakeMon("Body", owner="p2", hp=hp, max_hp=320, eid="b")
            vmax = FakeMon("Eternatus VMAX", energy=energy, cost=2,
                           eid="a")
            darks = [vmax] + [FakeMon("Galarian Zigzagoon", eid=f"z{i}")
                              for i in range(bodies - 1)]
            return FakeCtx(active=vmax, play=darks, opp_active=body,
                           opp_play=[body])
        # 1 body -> Dread End 30: a 30 hp body is in the window
        self.assertTrue(_et_allow("UseTrainerCard", "Boss's Orders",
                                  boss_ctx(30)))
        # scratched body (outside the window) still has gusted value
        self.assertTrue(_et_allow("UseTrainerCard", "Boss's Orders",
                                  boss_ctx(200)))
        # fresh body outside the window and unscratched -> nothing to gain
        self.assertFalse(_et_allow("UseTrainerCard", "Boss's Orders",
                                   boss_ctx(320)))
        # can't swing this turn
        self.assertFalse(_et_allow("UseTrainerCard", "Boss's Orders",
                                   boss_ctx(30, energy=0)))

    def test_switch_and_bird_keeper_gates(self):
        ready = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="r")
        dead = FakeMon("Eternatus VMAX", energy=0, cost=2, eid="d")
        hurt = FakeMon("Eternatus VMAX", energy=2, cost=2, hp=190,
                       max_hp=340, eid="h")
        # healthy powered active -> save the switch
        self.assertFalse(_et_allow("UseTrainerCard", "Switch",
                                   FakeCtx(active=ready, play=[ready],
                                           bench=[ready])))
        for card in ("Switch", "Bird Keeper"):
            self.assertTrue(_et_allow("UseTrainerCard", card,
                                      FakeCtx(active=dead, play=[dead,
                                              ready], bench=[ready])), card)
            self.assertTrue(_et_allow("UseTrainerCard", card,
                                      FakeCtx(active=hurt, play=[hurt,
                                              ready], bench=[ready])), card)

    def test_galar_mine_stadium_gate(self):
        self.assertTrue(_et_allow("DefaultStadiumPlayAbility", "Galar Mine",
                                  FakeCtx()))
        self.assertFalse(_et_allow("DefaultStadiumPlayAbility", "Galar Mine",
                                   FakeCtx(stadium="Galar Mine")))

    def test_retreat_gate_is_last_resort(self):
        vmax = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="v")
        ready = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="r")
        dead = FakeMon("Eternatus VMAX", energy=0, cost=2, eid="d")
        self.assertFalse(_et_retreat_ok(FakeCtx(
            active=vmax, play=[vmax, ready], bench=[ready])))
        self.assertTrue(_et_retreat_ok(FakeCtx(
            active=dead, play=[dead, ready], bench=[ready])))
        self.assertFalse(_et_retreat_ok(FakeCtx(
            active=dead, play=[dead], bench=[])))

    def test_hoopa_assault_gate_allow(self):
        hoopa = FakeMon("Hoopa", energy=1, cost=1, eid="h")
        self.assertTrue(_et_allow("UsePokemonAttack", "Hoopa",
                                  FakeCtx(active=hoopa, play=[hoopa],
                                          entered={"h"})))
        self.assertFalse(_et_allow("UsePokemonAttack", "Hoopa",
                                   FakeCtx(active=hoopa, play=[hoopa])))
        # default: everything else stays allowed
        self.assertTrue(_et_allow("UseTrainerCard", "Marnie",
                                  FakeCtx(hand=["x"] * 2, deck=40)))

    # -- value / bench / energy --------------------------------------------
    def test_value_prefers_gap_pieces(self):
        gap = FakeCtx(play=[])
        self.assertGreater(_et_value("Eternatus V", gap), 30)
        seen = FakeCtx(play=[FakeMon("Eternatus V", eid="v")])
        self.assertGreater(_et_value("Eternatus VMAX", seen), 30)
        full = FakeCtx(play=[FakeMon("Eternatus V", eid="v"),
                             FakeMon("Eternatus VMAX", eid="vm")])
        self.assertLess(_et_value("Eternatus VMAX", full), 15)
        self.assertGreater(_et_value("Crobat V", FakeCtx(hand=["x"] * 3)),
                           _et_value("Crobat V", FakeCtx(hand=["x"] * 7)))

    def test_value_starved_darkness_energy(self):
        self.assertEqual(_et_value("Darkness Energy", FakeCtx(hand=[])),
                         26.0)
        stocked = FakeCtx(hand=["Darkness Energy", "Darkness Energy",
                                "Darkness Energy"])
        self.assertGreater(_et_value("Darkness Energy", FakeCtx(hand=[])),
                           _et_value("Darkness Energy", stocked))

    def test_bench_score_fills_and_preserves_crobat(self):
        self.assertGreater(_et_bench_score("Eternatus V", FakeCtx()),
                           _et_bench_score("Galarian Zigzagoon",
                                           FakeCtx()))
        low = FakeCtx(hand=["x"] * 3)
        full = FakeCtx(hand=["x"] * 7)
        self.assertGreater(_et_bench_score("Crobat V", low),
                           _et_bench_score("Crobat V", full))
        # already two Crobats in play with a full hand: keep one back
        two = FakeCtx(hand=["x"] * 7,
                      play=[FakeMon("Crobat V", eid="c1"),
                            FakeMon("Crobat V", eid="c2")])
        self.assertLess(_et_bench_score("Crobat V", two),
                        _et_bench_score("Crobat V", full))

    def test_energy_target_ladder(self):
        vmax = FakeMon("Eternatus VMAX", energy=0, cost=2, eid="vm")
        bench_v = FakeMon("Eternatus V", energy=0, cost=1, eid="bv")
        crobat = FakeMon("Crobat V", energy=0, cost=1, eid="c")
        ctx = FakeCtx(active=vmax, play=[vmax, bench_v, crobat],
                      bench=[bench_v, crobat])
        active_score = _et_energy_target_score(ctx, vmax)
        bench_score = _et_energy_target_score(ctx, bench_v)
        utility = _et_energy_target_score(ctx, crobat)
        self.assertGreater(active_score, bench_score)
        self.assertEqual(utility, 55.0)
        # satisfied active yields to a hungry bench body
        fed = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="vm2")
        ctx2 = FakeCtx(active=fed, play=[fed, bench_v], bench=[bench_v])
        self.assertLess(_et_energy_target_score(ctx2, fed),
                        _et_energy_target_score(ctx2, bench_v))

    # -- gust / promote / pick ----------------------------------------------
    def test_gust_window_tracks_current_dread_end(self):
        vmax = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="vm")
        five = [vmax] + [FakeMon("Galarian Zigzagoon", eid=f"z{i}")
                         for i in range(4)]        # 5 bodies -> 150
        in_range = FakeMon("Body", owner="p2", hp=140, max_hp=320,
                           eid="g1")
        out = FakeMon("Body", owner="p2", hp=200, max_hp=320, eid="g2")
        ctx = FakeCtx(active=vmax, play=five,
                      opp_play=[in_range, out], opp_active=in_range)
        self.assertEqual(_et_gust_window(ctx), [in_range])
        self.assertGreater(_et_gust(ctx, in_range), _et_gust(ctx, out))

    def test_promote_prefers_ready_vmax_and_gated_hoopa(self):
        vmax = FakeMon("Eternatus VMAX", energy=2, cost=2, eid="vm")
        hoopa = FakeMon("Hoopa", energy=1, cost=1, eid="h")
        opp = FakeMon("Body", owner="p2", hp=80, max_hp=120, eid="o")
        ctx = FakeCtx(active=vmax, play=[vmax], opp_active=opp,
                      opp_play=[opp])
        window = _et_promote(ctx, hoopa)
        self.assertGreater(window, 1500)          # the 90 finishes
        self.assertGreater(_et_promote(ctx, vmax), window)
        opp.hp = 300                              # no window -> sink
        self.assertGreater(_et_promote(ctx, vmax), _et_promote(ctx, hoopa))

    def test_pick_promotes_and_gusts(self):
        vmax = FakeMon("Eternatus VMAX", energy=2, cost=2, owner="p1",
                       eid="vm")
        hoopa = FakeMon("Hoopa", energy=1, cost=1, owner="p1", eid="h")
        ctx = FakeCtx(active=vmax, play=[vmax])
        mine = "Choose your new Active Pok\u00e9mon"
        self.assertGreater(_et_pick(mine, ctx, vmax), _et_pick(mine, ctx,
                                                               hoopa))
        in_range = FakeMon("Body", owner="p2", hp=30, max_hp=320,
                           eid="g1")
        fresh = FakeMon("Body", owner="p2", hp=300, max_hp=320, eid="g2")
        opp_prompt = "Choose your opponent's new Active Pok\u00e9mon"
        self.assertGreater(_et_pick(opp_prompt, ctx, in_range),
                           _et_pick(opp_prompt, ctx, fresh))

    def test_search_score_uses_value(self):
        ctx = FakeCtx(play=["Eternatus V"])
        vmax = FakeMon("Eternatus VMAX", eid="vm")
        zig = FakeMon("Galarian Zigzagoon", eid="z")
        self.assertGreater(_et_search_score(vmax, ctx),
                           _et_search_score(zig, ctx))

    def test_counter_plan_finishes_cheapest_ko(self):
        ctx = FakeCtx()
        almost = FakeMon("Body", owner="p2", hp=10, max_hp=120, eid="a")
        fresh = FakeMon("Body", owner="p2", hp=110, max_hp=120, eid="f")
        plan = ETERNATUS_VMAX["counter_plan"]([fresh, almost], 1, ctx)
        self.assertEqual(plan, {"a": 1})


class WiringTests(unittest.TestCase):
    def test_ai_player_attaches_brain_from_deck_name(self):
        from spirit.game.session.ai_player import AIPlayer
        player = AIPlayer("bot-1", "Bot", {"deckName": "Dragapult Inteleon"}, None)
        self.assertIs(player.deck_strategy, DRAGAPULT_INTELEON)
        generic = AIPlayer("bot-2", "Bot", {"deckName": "Nope"}, None)
        self.assertIsNone(generic.deck_strategy)
        empty = AIPlayer("bot-3", "Bot", {}, None)
        self.assertIsNone(empty.deck_strategy)

    def test_ai_priority_includes_ability_bucket(self):
        from spirit.game.session.game_session import GameSession
        from spirit.game.session.legal_actions import ACTION_USE_ABILITY
        self.assertIn(ACTION_USE_ABILITY, GameSession.AI_ACTION_PRIORITY)


class HeadlessSimTests(unittest.TestCase):
    def test_one_full_ai_vs_ai_game(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "sim_bot_match.py"),
             "--games", "1"],
            cwd=str(ROOT), capture_output=True, text=True, timeout=180,
        )
        output = (proc.stdout or "") + (proc.stderr or "")
        self.assertEqual(proc.returncode, 0, output[-4000:])
        self.assertIn("crash-fallback results: 0/1", output)
        # mirror outcome is random (coin toss / draws): only completion matters
        self.assertIn("winner=ai", output)
        self.assertNotIn("Error in gameplay sequence", output)


if __name__ == "__main__":
    unittest.main()
