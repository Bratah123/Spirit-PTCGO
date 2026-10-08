"""Unit tests for the deck strategic-brain system (content.deck_strategies),
the AIPlayer wiring, and a headless end-to-end sim smoke run."""

import subprocess
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from spirit.game.content import bot_decks  # noqa: E402
from spirit.game.content.deck_strategies import (  # noqa: E402
    CHARIZARD_VSTAR,
    CORVIKNIGHT_BRONZONG,
    DRAGAPULT_INTELEON,
    ETERNATUS_VMAX,
    RAPID_STRIKE_URSHIFU,
    RS_ATTACKERS,
    RAYQUAZA_VMAX_FLAFFY,
    SHADOW_RIDER,
    SR_ATTACKERS,
    StrategyContext,
    SUICUNE_LUDICOLO,
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
    _cz_allow,
    _cz_attack_score,
    _cz_basin_ok,
    _cz_basin_target_score,
    _cz_bench_score,
    _cz_energy_target_score,
    _cz_energy_value,
    _cz_gust,
    _cz_gust_window,
    _cz_output,
    _cz_pick,
    _cz_promote,
    _cz_ready,
    _cz_retreat_ok,
    _cz_search_score,
    _cz_star_blaze_window,
    _cz_strike_damage,
    _cz_target_score,
    _cz_value,
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
    _ry_action_score,
    _ry_allow,
    _ry_attack_score,
    _ry_bench_can_attack,
    _ry_bench_score,
    _ry_energy_target_score,
    _ry_energy_value,
    _ry_gust,
    _ry_gust_window,
    _ry_output,
    _ry_pick,
    _ry_promote,
    _ry_ready,
    _ry_retreat_ok,
    _ry_search_score,
    _ry_stormy_ok,
    _ry_strike_damage,
    _ry_switch_ok,
    _ry_target_score,
    _ry_value,
    _sr_allow,
    _sr_attack_score,
    _sr_energy_target_score,
    _sr_pick,
    _sr_retreat_ok,
    _sr_search_score,
    _sr_value,
    _su_action_score,
    _su_allow,
    _su_attack_score,
    _su_bench_score,
    _su_candy_pairs,
    _su_dance_bonus,
    _su_dance_unlocks,
    _su_dance_window,
    _su_energy_target_score,
    _su_energy_value,
    _su_evolve_score,
    _su_gust,
    _su_gust_window,
    _su_lotad_ok,
    _su_output,
    _su_pick,
    _su_promote,
    _su_ready,
    _su_retreat_ok,
    _su_rope_ok,
    _su_rondo_base,
    _su_scoop,
    _su_scoop_ok,
    _su_search_score,
    _su_snipe,
    _su_strike_damage,
    _su_target_score,
    _su_value,
    _su_water_left,
    gust_score,
    ko_threshold_counters,
    order_score,
    promotion_score,
    rs_energy_value,
    strategy_for,
)


class FakeMon:
    def __init__(self, name, owner="p1", hp=0, max_hp=None, energy=0,
                 cost=0, eid=None, prize=1, fire=0, lightning=0, water=0):
        self.name_ = name
        self.owning_player_id = owner
        self.hp = hp
        self.max_hp = hp if max_hp is None else max_hp
        self.energy = energy
        self.cost = cost
        self.entity_id = eid or name
        self.prize = prize
        self.fire = fire
        self.lightning = lightning
        self.water = water
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

    def energy_of_type(self, pokemon, type_name):
        if pokemon is None:
            return 0
        return getattr(pokemon, type_name.lower(), 0)

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
                                 "Eternatus V", "Rayquaza V",
                                 "Sobble (suicune-ludicolo)",
                                 "Charizard (charizard-vmax)"})
        self.assertEqual(
            set(bot_decks.ACTIVE_BOT_DECKS),
            {"Dragapult Inteleon", "Rapid Strike Urshifu V",
             "Shadow Rider Calyrex V", "Bronzor", "Eternatus V",
             "Rayquaza V", "Sobble (suicune-ludicolo)",
             "Charizard (charizard-vmax)"},
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


class RayquazaBrainTests(unittest.TestCase):
    def test_rayquaza_brain_registered(self):
        spec = strategy_for("Rayquaza V")
        self.assertIs(spec, RAYQUAZA_VMAX_FLAFFY)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score"):
            self.assertTrue(callable(spec[hook]), hook)
        self.assertNotIn("counter_plan", spec)

    # -- typed readiness / output -----------------------------------------
    @staticmethod
    def _vmax(fire=0, lightning=0, eid="vm", owner="p1", hp=320):
        return FakeMon("Rayquaza VMAX", owner=owner, hp=hp, max_hp=320,
                       energy=fire + lightning, cost=2, fire=fire,
                       lightning=lightning, eid=eid)

    @staticmethod
    def _v(fire=0, lightning=0, eid="v", owner="p1", hp=210):
        return FakeMon("Rayquaza V", owner=owner, hp=hp, max_hp=210,
                       energy=fire + lightning, cost=1, fire=fire,
                       lightning=lightning, eid=eid)

    def test_ready_needs_one_fire_and_one_lightning(self):
        both = self._vmax(fire=1, lightning=1)
        stacked = self._vmax(lightning=2)
        ctx = FakeCtx(active=both, play=[both, stacked])
        self.assertTrue(_ry_ready(ctx, both))
        self.assertFalse(_ry_ready(ctx, stacked))
        # the V only needs Lightning (Dragon Pulse path)
        self.assertTrue(_ry_ready(ctx, self._v(lightning=1)))
        self.assertFalse(_ry_ready(ctx, self._v(fire=1)))
        # engine bodies are never ready
        self.assertFalse(_ry_ready(ctx, FakeMon("Flaaffy", lightning=2)))

    def test_max_burst_dumps_every_attached_pool(self):
        small = self._vmax(fire=1, lightning=1)
        loaded = self._vmax(fire=2, lightning=2)
        self.assertEqual(
            _ry_output(FakeCtx(active=small, play=[small]), small), 180)
        self.assertEqual(
            _ry_strike_damage(FakeCtx(active=loaded, play=[loaded])), 340)
        # Lightning stacked without Fire cannot Max Burst at all
        stuck = self._vmax(lightning=3)
        self.assertEqual(
            _ry_output(FakeCtx(active=stuck, play=[stuck]), stuck), 0)

    def test_spiral_burst_prefers_fire_then_dragon_pulse(self):
        # fire attached -> the choice button picks the Fire pool
        dual = self._v(fire=1, lightning=1)
        stacked_fire = self._v(fire=2, lightning=1)
        lightning_only = self._v(lightning=2)
        self.assertEqual(
            _ry_output(FakeCtx(active=dual, play=[dual]), dual), 100)
        self.assertEqual(
            _ry_output(FakeCtx(active=stacked_fire, play=[stacked_fire]),
                       stacked_fire), 180)
        self.assertEqual(
            _ry_output(FakeCtx(active=lightning_only, play=[lightning_only]),
                       lightning_only), 40)

    def test_engine_bodies_never_strike(self):
        for title in ("Mareep", "Flaaffy", "Kricketune V"):
            body = FakeMon(title, energy=2, lightning=2, eid=title)
            ctx = FakeCtx(active=body, play=[body], deck=40)
            self.assertEqual(_ry_output(ctx, body), 0.0, title)
            self.assertFalse(
                _ry_allow("UsePokemonAttack", title, ctx), title)

    # -- allow gates --------------------------------------------------------
    def test_research_gates(self):
        self.assertTrue(_ry_allow("UseTrainerCard", "Professor's Research",
                                  FakeCtx(hand=["x"] * 5, deck=40)))
        self.assertFalse(_ry_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 6, deck=40)))
        self.assertFalse(_ry_allow("UseTrainerCard", "Professor's Research",
                                   FakeCtx(hand=["x"] * 5, deck=10)))

    def test_marnie_gates(self):
        self.assertTrue(_ry_allow("UseTrainerCard", "Marnie",
                                  FakeCtx(hand=["x"] * 2, deck=40)))
        ctx = FakeCtx(hand=["x"] * 7)
        ctx.hand_size = lambda pid=None: 4 if pid == "p2" else 7
        self.assertFalse(_ry_allow("UseTrainerCard", "Marnie", ctx))
        ctx.hand_size = lambda pid=None: 6 if pid == "p2" else 7
        self.assertTrue(_ry_allow("UseTrainerCard", "Marnie", ctx))
        self.assertFalse(_ry_allow("UseTrainerCard", "Marnie",
                                   FakeCtx(hand=["x"] * 2, deck=5)))

    def test_search_runway_gates(self):
        for card in ("Quick Ball", "Level Ball", "Evolution Incense"):
            self.assertTrue(_ry_allow("UseTrainerCard", card,
                                      FakeCtx(deck=6)), card)
            self.assertFalse(_ry_allow("UseTrainerCard", card,
                                       FakeCtx(deck=5)), card)

    def test_boss_gate_needs_a_swing_and_a_window(self):
        ready = self._vmax(fire=1, lightning=1)
        window = FakeMon("Body", owner="p2", hp=170, max_hp=320, eid="w1")
        fresh = FakeMon("Body", owner="p2", hp=500, max_hp=500, eid="w2")
        base = dict(active=ready, play=[ready])
        ctx = FakeCtx(opp_active=window, opp_play=[window], **base)
        self.assertTrue(_ry_allow("UseTrainerCard", "Boss's Orders", ctx))
        ctx2 = FakeCtx(opp_active=fresh, opp_play=[fresh], **base)
        self.assertFalse(_ry_allow("UseTrainerCard", "Boss's Orders", ctx2))
        fresh.hp = 480                      # scratched: still worth dragging
        self.assertTrue(_ry_allow("UseTrainerCard", "Boss's Orders", ctx2))
        # cannot swing this turn -> hold the Boss
        stuck = self._vmax(lightning=2)
        ctx3 = FakeCtx(active=stuck, play=[stuck], opp_active=window,
                       opp_play=[window])
        self.assertFalse(_ry_allow("UseTrainerCard", "Boss's Orders", ctx3))

    def test_rose_needs_small_hand_and_reservoir(self):
        discard = ["Lightning Energy", "Fire Energy"]
        self.assertTrue(_ry_allow("UseTrainerCard", "Rose",
                                  FakeCtx(hand=["x"] * 3, discard=discard)))
        self.assertFalse(_ry_allow("UseTrainerCard", "Rose",
                                   FakeCtx(hand=["x"] * 4, discard=discard)))
        self.assertFalse(_ry_allow("UseTrainerCard", "Rose",
                                   FakeCtx(hand=["x"] * 3, discard=[])))

    def test_switch_and_retreat_gate_rotation(self):
        empty = self._vmax()                # dumped its whole pool
        loaded = self._v(fire=1, lightning=1)
        ctx = FakeCtx(active=empty, play=[empty, loaded], bench=[loaded])
        self.assertTrue(_ry_switch_ok(ctx))
        self.assertTrue(_ry_retreat_ok(ctx))
        # healthy active with an unpowered backup: stay put
        ctx2 = FakeCtx(active=loaded, play=[loaded, empty], bench=[empty])
        self.assertFalse(_ry_switch_ok(ctx2))
        self.assertFalse(_ry_retreat_ok(ctx2))
        # heavily damaged active: bail even if the backup swings less
        hurt = self._vmax(fire=1, lightning=1, hp=170)
        ctx3 = FakeCtx(active=hurt, play=[hurt, loaded], bench=[loaded])
        self.assertTrue(_ry_switch_ok(ctx3))
        self.assertTrue(_ry_retreat_ok(ctx3))

    def test_azure_pulse_gate(self):
        self.assertFalse(_ry_allow("UsePokemonAbility", "Azure Pulse",
                                   FakeCtx(hand=["x"] * 4)))
        self.assertFalse(_ry_allow(
            "UsePokemonAbility", "Azure Pulse",
            FakeCtx(hand=["Boss's Orders", "x", "x"])))
        self.assertTrue(_ry_allow("UsePokemonAbility", "Azure Pulse",
                                  FakeCtx(hand=["x"] * 3)))

    def test_dynamotor_offered_stormy_gated(self):
        self.assertTrue(_ry_allow("UsePokemonAbility", "Dynamotor",
                                  FakeCtx()))
        ready = self._vmax(fire=1, lightning=1)
        line = [FakeMon("Mareep", eid="m1"), FakeMon("Flaaffy", eid="f1"),
                FakeMon("Mareep", eid="m2")]
        capped = FakeCtx(active=ready, play=[ready] + line)
        self.assertFalse(_ry_allow("UsePokemonAbility", "Stormy Mountains",
                                   capped))
        empty = FakeCtx(play=[FakeMon("Mareep", eid="m1")])
        self.assertTrue(_ry_allow("UsePokemonAbility", "Stormy Mountains",
                                  empty))
        self.assertTrue(_ry_allow("UsePokemonAbility", "Exciting Stage",
                                  FakeCtx()))

    def test_stadium_gate_only_blocks_opponent_stormy(self):
        self.assertTrue(_ry_allow("DefaultStadiumPlayAbility",
                                  "Stormy Mountains", FakeCtx()))
        self.assertFalse(_ry_allow(
            "DefaultStadiumPlayAbility", "Stormy Mountains",
            FakeCtx(stadium="Stormy Mountains")))

    def test_dragon_pulse_runway_and_utility_attack_block(self):
        self.assertTrue(_ry_allow("UsePokemonAttack", "Rayquaza V",
                                  FakeCtx(deck=15)))
        self.assertFalse(_ry_allow("UsePokemonAttack", "Rayquaza V",
                                   FakeCtx(deck=14)))
        self.assertTrue(_ry_allow("UsePokemonAttack", "Rayquaza VMAX",
                                  FakeCtx(deck=40)))

    def test_pal_pad_and_rod_gates(self):
        self.assertTrue(_ry_allow("UseTrainerCard", "Pal Pad",
                                  FakeCtx(discard=["Boss's Orders"])))
        self.assertFalse(_ry_allow("UseTrainerCard", "Pal Pad",
                                   FakeCtx(discard=["Switch"])))
        lost = FakeCtx(play=[], discard=["Rayquaza V", "Mareep"], deck=40)
        self.assertTrue(_ry_allow("UseTrainerCard", "Ordinary Rod", lost))
        vmax = self._vmax(fire=1, lightning=1)
        healthy = FakeCtx(
            active=vmax,
            play=[vmax, FakeMon("Mareep", eid="m"),
                  FakeMon("Flaaffy", eid="f")],
            discard=["Lightning Energy"], deck=40)
        self.assertFalse(_ry_allow("UseTrainerCard", "Ordinary Rod", healthy))

    # -- value / energy ------------------------------------------------------
    def test_value_prefers_gap_pieces(self):
        empty = FakeCtx(play=[])
        seen = FakeCtx(play=[FakeMon("Rayquaza V", eid="v")])
        self.assertGreater(_ry_value("Rayquaza V", empty), 30)
        self.assertGreater(_ry_value("Rayquaza VMAX", seen), 30)
        self.assertLess(_ry_value("Rayquaza VMAX", empty), 15)
        full = FakeCtx(play=[self._vmax(eid="a"), self._v(eid="b"),
                             self._v(eid="c")])
        self.assertLess(_ry_value("Rayquaza V", full), 15)
        no_mareep = FakeCtx(play=[])
        stocked = FakeCtx(play=[FakeMon("Mareep", eid="m1"),
                                FakeMon("Mareep", eid="m2"),
                                FakeMon("Flaaffy", eid="f1"),
                                FakeMon("Flaaffy", eid="f2")])
        self.assertGreater(_ry_value("Mareep", no_mareep),
                           _ry_value("Mareep", stocked))
        self.assertGreater(_ry_value("Flaaffy",
                                     FakeCtx(play=[FakeMon("Mareep",
                                                           eid="m")])), 30)
        self.assertLess(_ry_value("Flaaffy", stocked), 10)

    def test_fire_energy_is_protected_lightning_is_dump_fuel(self):
        self.assertEqual(_ry_value("Fire Energy", FakeCtx(hand=[])), 30.0)
        self.assertEqual(_ry_value("Lightning Energy", FakeCtx(hand=[])),
                         6.0)
        fire_card = FakeMon("Fire Energy", eid="fe")
        bolt_card = FakeMon("Lightning Energy", eid="le")
        ctx = FakeCtx(play=[])
        self.assertGreater(_ry_search_score(fire_card, ctx),
                           _ry_search_score(bolt_card, ctx))

    def test_energy_action_value(self):
        hungry = self._vmax(lightning=2)    # fire slot still open
        fed = self._vmax(fire=1, lightning=1)
        self.assertEqual(
            _ry_energy_value("Fire Energy",
                             FakeCtx(active=hungry, play=[hungry])), 42.0)
        self.assertEqual(
            _ry_energy_value("Fire Energy",
                             FakeCtx(active=fed, play=[fed])), 6.0)
        held1 = FakeCtx(hand=["Lightning Energy"])
        held3 = FakeCtx(hand=["Lightning Energy"] * 3)
        self.assertEqual(_ry_energy_value("Lightning Energy", held1), 30.0)
        self.assertEqual(_ry_energy_value("Lightning Energy", held3), 20.0)

    def test_supporter_values_and_dup_penalty(self):
        starved = FakeCtx(hand=["x"] * 3)
        stocked = FakeCtx(hand=["x"] * 7)
        self.assertGreater(
            _ry_value("Professor's Research", starved),
            _ry_value("Professor's Research", stocked))
        # a second Boss is a dead card this turn...
        dup = FakeCtx(hand=["Boss's Orders"])
        self.assertLess(
            _ry_value("Boss's Orders", dup, in_hand=True),
            _ry_value("Boss's Orders", starved, in_hand=True))
        # ...a second Research still plays next turn (repeatable)
        self.assertEqual(
            _ry_value("Professor's Research",
                      FakeCtx(hand=["Professor's Research"]),
                      in_hand=True), 30.0)

    def test_energy_target_ladder(self):
        active = self._vmax(lightning=2)    # fire slot open
        bench_ray = self._v(lightning=1, eid="br")
        body = FakeMon("Mareep", eid="m")
        ctx = FakeCtx(active=active, play=[active, bench_ray, body],
                      bench=[bench_ray, body])
        # Fire into the open slot: active over bench, engine never
        self.assertGreater(
            _ry_energy_target_score(ctx, active, "Fire Energy"),
            _ry_energy_target_score(ctx, bench_ray, "Fire Energy"))
        self.assertEqual(
            _ry_energy_target_score(ctx, body, "Fire Energy"), 55.0)
        fed = self._vmax(fire=1, lightning=1)
        ctxf = FakeCtx(active=fed, play=[fed])
        self.assertEqual(
            _ry_energy_target_score(ctxf, fed, "Fire Energy"), 60.0)
        # Lightning ladder: active first, engine bodies never
        self.assertGreater(
            _ry_energy_target_score(ctx, active, "Lightning Energy"),
            _ry_energy_target_score(ctx, bench_ray, "Lightning Energy"))
        self.assertEqual(
            _ry_energy_target_score(ctx, body, "Lightning Energy"), 55.0)
        # overcommit cap: four energy already -> feed the next attacker
        stuffed = self._vmax(fire=1, lightning=3)
        ctx2 = FakeCtx(active=stuffed, play=[stuffed, bench_ray],
                       bench=[bench_ray])
        self.assertLess(
            _ry_energy_target_score(ctx2, stuffed, "Lightning Energy"),
            _ry_energy_target_score(ctx, active, "Lightning Energy"))

    def test_bench_score_growth(self):
        empty = FakeCtx(play=[])
        self.assertGreater(_ry_bench_score("Rayquaza V", empty),
                           _ry_bench_score("Mareep", empty))
        self.assertGreater(_ry_bench_score("Mareep", empty),
                           _ry_bench_score("Kricketune V", empty))
        line_up = FakeCtx(play=[FakeMon("Mareep", eid="m1"),
                                FakeMon("Flaaffy", eid="f1"),
                                FakeMon("Mareep", eid="m2"),
                                FakeMon("Flaaffy", eid="f2")])
        self.assertGreater(_ry_bench_score("Mareep", empty),
                           _ry_bench_score("Mareep", line_up))
        # Kricketune only earns a slot while we are digging
        self.assertGreater(
            _ry_bench_score("Kricketune V", FakeCtx(hand=["x"] * 2)),
            _ry_bench_score("Kricketune V", FakeCtx(hand=["x"] * 7)))

    def test_action_score_priorities(self):
        ctx = FakeCtx(hand=["x"] * 2)
        self.assertGreater(
            _ry_action_score("EvolvePokemonPlayAbility", "Rayquaza VMAX",
                             ctx),
            _ry_action_score("EvolvePokemonPlayAbility", "Flaaffy", ctx))
        self.assertEqual(
            _ry_action_score("EvolvePokemonPlayAbility", "Unrelated", ctx),
            -50.0)
        empty_ray = self._vmax()
        hungry = FakeCtx(active=empty_ray, play=[empty_ray])
        fed_ray = self._vmax(fire=1, lightning=2)   # 3 energy: not starving
        fed = FakeCtx(active=fed_ray, play=[fed_ray])
        self.assertGreater(
            _ry_action_score("UsePokemonAbility", "Dynamotor", hungry),
            _ry_action_score("UsePokemonAbility", "Dynamotor", fed))
        self.assertEqual(
            _ry_action_score("UsePokemonAbility", "Azure Pulse", ctx), 55.0)
        capped = FakeCtx(play=[self._vmax(eid="a"),
                               FakeMon("Mareep", eid="m1"),
                               FakeMon("Flaaffy", eid="f1"),
                               FakeMon("Mareep", eid="m2")])
        self.assertEqual(
            _ry_action_score("UsePokemonAbility", "Stormy Mountains",
                             capped), 0.0)
        self.assertEqual(
            _ry_action_score("UseTrainerCard", "Professor's Research",
                             FakeCtx(hand=["x"] * 3)), 30.0)
        hungry_ray = self._vmax()
        self.assertEqual(
            _ry_action_score("DefaultEnergyPlayAbility", "Fire Energy",
                             FakeCtx(active=hungry_ray, play=[hungry_ray])),
            42.0)

    # -- attack / gust / promote ---------------------------------------------
    def test_max_burst_scores_kos(self):
        ready = self._vmax(fire=1, lightning=1)     # 180
        ko = FakeMon("Body", owner="p2", hp=170, max_hp=320, eid="o")
        tough = FakeMon("Body", owner="p2", hp=300, max_hp=320, eid="t")
        ctx_win = FakeCtx(active=ready, play=[ready], opp_active=ko,
                          opp_play=[ko])
        ctx_no = FakeCtx(active=ready, play=[ready], opp_active=tough,
                         opp_play=[tough])
        self.assertGreaterEqual(
            _ry_attack_score("Max Burst", 0, ctx_win), 1880)
        self.assertEqual(_ry_attack_score("Max Burst", 0, ctx_no), 880.0)
        loaded = self._vmax(fire=2, lightning=1)    # 260
        ctx_load = FakeCtx(active=loaded, play=[loaded], opp_active=tough,
                           opp_play=[tough])
        self.assertGreater(_ry_attack_score("Max Burst", 0, ctx_load), 880.0)

    def test_spiral_and_pulse_attack_scores(self):
        dual = self._v(fire=1, lightning=1)         # 100
        ctx = FakeCtx(active=dual, play=[dual])
        self.assertEqual(_ry_attack_score("Spiral Burst", 0, ctx), 550.0)
        bolt = self._v(lightning=2)
        ctx2 = FakeCtx(active=bolt, play=[bolt])
        self.assertEqual(_ry_attack_score("Dragon Pulse", 0, ctx2), 360.0)
        ko = FakeMon("Body", owner="p2", hp=40, max_hp=120, eid="o")
        ctx3 = FakeCtx(active=bolt, play=[bolt], opp_active=ko,
                       opp_play=[ko])
        self.assertGreaterEqual(
            _ry_attack_score("Dragon Pulse", 0, ctx3), 1360)

    def test_gust_window_follows_typed_output(self):
        ready = self._vmax(fire=1, lightning=1)      # 180
        in_range = FakeMon("Body", owner="p2", hp=170, max_hp=320, eid="g1")
        out = FakeMon("Body", owner="p2", hp=250, max_hp=320, eid="g2")
        ctx = FakeCtx(active=ready, play=[ready], opp_active=in_range,
                      opp_play=[in_range, out])
        self.assertEqual(_ry_gust_window(ctx), [in_range])
        self.assertGreater(_ry_gust(ctx, in_range), _ry_gust(ctx, out))
        stuck = self._vmax(lightning=2)
        ctx2 = FakeCtx(active=stuck, play=[stuck], opp_active=in_range,
                       opp_play=[in_range])
        self.assertEqual(_ry_gust_window(ctx2), [])

    def test_promote_prefers_typed_ready(self):
        ready = self._vmax(fire=1, lightning=1)
        stacked = self._vmax(lightning=3)
        self.assertGreater(
            _ry_promote(FakeCtx(active=ready, play=[ready]), ready),
            _ry_promote(FakeCtx(active=stacked, play=[stacked]), stacked))
        body = FakeMon("Flaaffy", energy=2)
        self.assertEqual(_ry_promote(FakeCtx(active=body), body), 0.0)

    def test_bench_can_attack(self):
        self.assertTrue(_ry_bench_can_attack(
            FakeCtx(bench=[self._v(lightning=1)])))
        self.assertFalse(_ry_bench_can_attack(FakeCtx(bench=[self._v()])))

    # -- target / pick ---------------------------------------------------------
    def test_target_score_boss_evolve_and_tool(self):
        ready = self._vmax(fire=1, lightning=1, owner="p1")
        ko = FakeMon("Body", owner="p2", hp=170, max_hp=320, eid="g1")
        fresh = FakeMon("Body", owner="p2", hp=300, max_hp=320, eid="g2")
        ctx = FakeCtx(active=ready, play=[ready, ko, fresh],
                      opp_active=ko, opp_play=[ko, fresh])
        self.assertGreater(
            _ry_target_score("UseTrainerCard", "Boss's Orders", ctx, "g1"),
            _ry_target_score("UseTrainerCard", "Boss's Orders", ctx, "g2"))
        active_v = self._v(lightning=1, owner="p1", eid="av")
        bench_v = self._v(owner="p1", eid="bv")
        ctx2 = FakeCtx(active=active_v, play=[active_v, bench_v],
                       bench=[bench_v])
        self.assertGreater(
            _ry_target_score("EvolvePokemonPlayAbility", "Rayquaza VMAX",
                             ctx2, "av"),
            _ry_target_score("EvolvePokemonPlayAbility", "Rayquaza VMAX",
                             ctx2, "bv"))
        body = FakeMon("Mareep", owner="p1", eid="m")
        ctx3 = FakeCtx(active=ready, play=[ready, body], bench=[body])
        self.assertGreater(
            _ry_target_score("DefaultToolPlayAbility", "Air Balloon", ctx3,
                             "vm"),
            _ry_target_score("DefaultToolPlayAbility", "Air Balloon", ctx3,
                             "m"))

    def test_target_score_energy_and_retreat(self):
        active = self._vmax(lightning=2, owner="p1")
        bench_ray = self._v(lightning=1, owner="p1", eid="br")
        opp = FakeMon("Body", owner="p2", hp=300, max_hp=320, eid="ob")
        ctx = FakeCtx(active=active, play=[active, bench_ray, opp],
                      bench=[bench_ray], opp_active=opp, opp_play=[opp])
        self.assertGreater(
            _ry_target_score("DefaultEnergyPlayAbility", "Fire Energy",
                             ctx, "vm"),
            _ry_target_score("DefaultEnergyPlayAbility", "Fire Energy",
                             ctx, "br"))
        self.assertGreater(_ry_target_score("BaseRetreat", "", ctx, "br"), 0)
        self.assertEqual(_ry_target_score("BaseRetreat", "", ctx, "ob"), 0)

    def test_pick_promotes_and_gusts(self):
        ready = self._vmax(fire=1, lightning=1, owner="p1")
        body = FakeMon("Flaaffy", owner="p1", eid="f")
        ctx = FakeCtx(active=ready, play=[ready, body], bench=[body])
        mine = "Choose your new Active Pok\u00e9mon"
        self.assertGreater(_ry_pick(mine, ctx, ready),
                           _ry_pick(mine, ctx, body))
        ko = FakeMon("Body", owner="p2", hp=170, max_hp=320, eid="g1")
        fresh = FakeMon("Body", owner="p2", hp=300, max_hp=320, eid="g2")
        opp_prompt = "Choose your opponent's new Active Pok\u00e9mon"
        self.assertGreater(_ry_pick(opp_prompt, ctx, ko),
                           _ry_pick(opp_prompt, ctx, fresh))

    def test_pick_rose_target_and_max_burst_dump(self):
        loaded = self._vmax(fire=1, lightning=1, owner="p1")
        spare = self._vmax(lightning=1, owner="p1", eid="spare")
        ctx = FakeCtx(active=loaded, play=[loaded, spare], bench=[spare])
        rose_prompt = "Choose your Pok\u00e9mon VMAX"
        self.assertGreater(_ry_pick(rose_prompt, ctx, loaded),
                           _ry_pick(rose_prompt, ctx, spare))
        stuffed = self._vmax(fire=2, lightning=2, owner="p1", eid="stuffed")
        ctx2 = FakeCtx(active=stuffed, play=[stuffed, spare], bench=[spare])
        self.assertLess(_ry_pick(rose_prompt, ctx2, stuffed),
                        _ry_pick(rose_prompt, ctx2, spare))
        dump = ("Discard any amount of basic Fire or Lightning Energy "
                "from this Pok\u00e9mon.")
        self.assertEqual(_ry_pick(dump, ctx, loaded), 100.0)

    def test_pick_attach_and_discard(self):
        active = self._vmax(lightning=2, owner="p1")
        bench_ray = self._v(lightning=1, owner="p1", eid="br")
        body = FakeMon("Mareep", owner="p1", eid="m")
        ctx = FakeCtx(active=active, play=[active, bench_ray, body],
                      bench=[bench_ray, body])
        attach_prompt = "Choose a Pok\u00e9mon to attach the Energy to"
        self.assertGreater(_ry_pick(attach_prompt, ctx, active),
                           _ry_pick(attach_prompt, ctx, bench_ray))
        self.assertGreater(_ry_pick(attach_prompt, ctx, bench_ray),
                           _ry_pick(attach_prompt, ctx, body))
        discard_prompt = "Choose a card to discard"
        bolt = FakeMon("Lightning Energy", owner="p1", eid="le")
        fire = FakeMon("Fire Energy", owner="p1", eid="fe")
        hand_ctx = FakeCtx(hand=["Lightning Energy", "Fire Energy", "x"])
        self.assertGreater(_ry_pick(discard_prompt, hand_ctx, bolt),
                           _ry_pick(discard_prompt, hand_ctx, fire))
        self.assertGreater(
            _ry_search_score(self._v(eid="sv"), FakeCtx(play=[])),
            _ry_search_score(bolt, FakeCtx(play=[])))


class SuicuneBrainTests(unittest.TestCase):
    def test_suicune_brain_registered(self):
        spec = strategy_for("Sobble (suicune-ludicolo)")
        self.assertIs(spec, SUICUNE_LUDICOLO)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score"):
            self.assertTrue(callable(spec[hook]), hook)
        self.assertNotIn("counter_plan", spec)

    # -- readiness / output ----------------------------------------------
    @staticmethod
    def _su(water=0, extra=0, eid="su", owner="p1", hp=210):
        return FakeMon("Suicune V", owner=owner, hp=hp, max_hp=210,
                       energy=water + extra, cost=2, water=water, eid=eid)

    @staticmethod
    def _dance_ctx(active, amount=100, player="p1", expires=None,
                   turn=1, **kw):
        ctx = FakeCtx(active=active, **kw)
        ctx.session = SimpleNamespace(
            turn_state=SimpleNamespace(
                damage_modifiers=[SimpleNamespace(
                    player_id=player, amount=amount,
                    expires_after_turn=expires, requires_subtype=None,
                    source_entity_id=None, attack_title=None,
                    source_predicate=None)],
                turn_number=turn))
        return ctx

    def test_ready_needs_typed_water_plus_second_unit(self):
        ready = self._su(water=1, extra=1)
        stacked = self._su(water=2)
        colorless = self._su(water=0, extra=2)
        short = self._su(water=1)
        ctx = FakeCtx(active=ready, play=[ready, stacked, colorless, short])
        self.assertTrue(_su_ready(ctx, ready))
        self.assertTrue(_su_ready(ctx, stacked))
        self.assertFalse(_su_ready(ctx, colorless))   # no Water slot filled
        self.assertFalse(_su_ready(ctx, short))       # only one unit
        self.assertFalse(_su_ready(ctx, FakeMon("Sobble", water=2)))

    def test_rondo_scales_with_both_benches(self):
        su = self._su(water=1, extra=1)
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        theirs = [FakeMon("Drizzile", owner="p2", eid=f"o{i}")
                  for i in range(4)]
        ctx = FakeCtx(active=su, play=[su] + mine, bench=mine,
                      opp_bench=theirs)
        self.assertEqual(_su_rondo_base(ctx), 20 + 20 * 8)
        self.assertEqual(_su_output(ctx, su), 180)
        small = FakeCtx(active=su, play=[su], bench=[], opp_bench=theirs[:1])
        self.assertEqual(_su_rondo_base(small), 20 + 20)
        unready = self._su(water=0, extra=1)
        ctx2 = FakeCtx(active=unready, play=[unready], bench=mine,
                       opp_bench=theirs)
        self.assertEqual(_su_rondo_base(ctx2), 0)
        self.assertEqual(_su_output(ctx2, unready), 0)

    def test_dance_bonus_reads_turn_state(self):
        su = self._su(water=1, extra=1)
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        theirs = [FakeMon("Drizzile", owner="p2", eid=f"o{i}")
                  for i in range(4)]
        ctx = self._dance_ctx(su, play=[su] + mine, bench=mine,
                              opp_bench=theirs)
        self.assertEqual(_su_dance_bonus(ctx, su), 100)
        self.assertEqual(_su_output(ctx, su), 280)      # 180 base + 100
        # only my modifiers count, and expired ones are pruned
        other = self._dance_ctx(su, player="p2", play=[su] + mine,
                                bench=mine, opp_bench=theirs)
        self.assertEqual(_su_dance_bonus(other, su), 0)
        stale = self._dance_ctx(su, expires=0, turn=1, play=[su] + mine,
                                bench=mine, opp_bench=theirs)
        self.assertEqual(_su_dance_bonus(stale, su), 0)
        # a FakeCtx without a session reads zero instead of raising
        bare = FakeCtx(active=su, play=[su] + mine, bench=mine,
                       opp_bench=theirs)
        self.assertEqual(_su_dance_bonus(bare, su), 0)

    # -- gust / promote ----------------------------------------------------
    def test_gust_window_uses_rondo_output(self):
        su = self._su(water=1, extra=1)
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        theirs = [FakeMon("Drizzile", owner="p2", hp=170, eid=f"o{i}")
                  for i in range(4)]
        ctx = FakeCtx(active=su, play=[su] + mine, bench=mine,
                      opp_play=theirs, opp_bench=theirs)
        window = _su_gust_window(ctx)
        self.assertEqual(len(window), 4)               # all 170 <= 180
        self.assertGreater(_su_gust(ctx, theirs[0]), 900.0)
        full_hp = FakeMon("Suicune V", owner="p2", hp=300, max_hp=300,
                          eid="tank")
        self.assertEqual(_su_gust(ctx, full_hp), 0.0)
        scratched = FakeMon("Suicune V", owner="p2", hp=300, max_hp=350,
                            eid="scratch")
        self.assertEqual(_su_gust(ctx, scratched), 550.0)
        unready = self._su(water=0, extra=1)
        ctx2 = FakeCtx(active=unready, play=[unready] + mine, bench=mine,
                       opp_bench=theirs)
        self.assertEqual(_su_gust_window(ctx2), [])

    def test_promote_prefers_the_ready_puncher(self):
        ready = self._su(water=1, extra=1, eid="r")
        bare = self._su(water=0, extra=0, eid="b")
        ctx = FakeCtx(active=ready, play=[ready, bare])
        ladder = [
            _su_promote(ctx, ready),
            _su_promote(ctx, bare),
            _su_promote(ctx, FakeMon("Ludicolo", eid="l")),
            _su_promote(ctx, FakeMon("Inteleon", eid="i")),
            _su_promote(ctx, FakeMon("Drizzile", eid="d")),
            _su_promote(ctx, FakeMon("Sobble", eid="s")),
            _su_promote(ctx, FakeMon("Lotad", eid="lo")),
        ]
        self.assertEqual(ladder, sorted(ladder, reverse=True))
        self.assertGreater(ladder[0], 2000.0)

    # -- energy ------------------------------------------------------------
    def test_energy_value_prefers_water_into_the_gap(self):
        hungry = self._su(water=0)
        hctx = FakeCtx(active=hungry, play=[hungry])
        self.assertEqual(_su_energy_value("Water Energy", hctx), 120.0)
        ready = self._su(water=1, extra=1)
        rctx = FakeCtx(active=ready, play=[ready])
        self.assertEqual(_su_energy_value("Water Energy", rctx), 60.0)
        # Capture only leads when no Water Energy is held at all
        self.assertEqual(_su_energy_value("Capture Energy", hctx), 90.0)
        held = FakeCtx(active=hungry, play=[hungry],
                       hand=["Water Energy", "x"])
        self.assertEqual(_su_energy_value("Capture Energy", held), 40.0)

    def test_energy_target_ladder_puncher_first(self):
        active_su = self._su(water=0, eid="a")
        bench_su = self._su(water=0, eid="b")
        engine = FakeMon("Sobble", eid="s")
        ctx = FakeCtx(active=active_su, play=[active_su, bench_su, engine],
                      bench=[bench_su, engine])
        score = lambda t, n="Water Energy": _su_energy_target_score(ctx, t, n)
        self.assertEqual(score(active_su), 750.0)      # 500 + typed slot
        self.assertEqual(score(bench_su), 600.0)
        self.assertEqual(score(engine), 50.0)          # engine never fed
        ready = self._su(water=1, extra=1, eid="a")
        rctx = FakeCtx(active=ready, play=[ready])
        self.assertEqual(_su_energy_target_score(rctx, ready, "Water Energy"),
                         240.0)                        # loaded: hold back
        mid = self._su(water=1, extra=0, eid="a")
        mctx = FakeCtx(active=mid, play=[mid])
        self.assertEqual(_su_energy_target_score(mctx, mid, "Water Energy"),
                         620.0)
        # no puncher out yet: the active body develops
        body = FakeMon("Sobble", eid="s")
        bctx = FakeCtx(active=body, play=[body])
        self.assertEqual(_su_energy_target_score(bctx, body, "Water Energy"),
                         300.0)

    # -- bench discipline ----------------------------------------------------
    def test_bench_attacker_first_then_engine(self):
        empty = FakeCtx(play=[], bench=[])
        self.assertEqual(_su_bench_score("Suicune V", empty), 700.0)
        self.assertEqual(_su_bench_score("Sobble", empty), 600.0)
        su = self._su(eid="a")
        one = FakeCtx(play=[su], bench=[su])
        self.assertEqual(_su_bench_score("Suicune V", one), 450.0)

    def test_bench_lotad_needs_line_pieces_and_slot(self):
        su = self._su(eid="s1")
        so1 = FakeMon("Sobble", eid="b1")
        so2 = FakeMon("Sobble", eid="b2")
        board = [su, so1, so2]
        # pieces in hand: Lotad outranks the next Sobble for the slot
        held = FakeCtx(hand=["Lombre"], play=board, bench=board)
        self.assertEqual(_su_bench_score("Lotad", held), 280.0)
        self.assertEqual(_su_bench_score("Sobble", held), 200.0)
        # no pieces: Lotad stays down
        bare = FakeCtx(hand=[], play=board, bench=board)
        self.assertEqual(_su_bench_score("Lotad", bare), 0.0)
        # one slot left and no backup puncher: both yield
        so3 = FakeMon("Sobble", eid="b3")
        full = FakeCtx(hand=["Lombre"], play=board + [so3],
                       bench=board + [so3])
        self.assertEqual(_su_bench_score("Sobble", full), 120.0)
        self.assertEqual(_su_bench_score("Lotad", full), 0.0)

    def test_lotad_ok_gates_pieces_and_slots(self):
        self.assertFalse(_su_lotad_ok(FakeCtx(hand=[], bench=[])))
        self.assertTrue(_su_lotad_ok(FakeCtx(hand=["Lombre"], bench=[])))
        su = self._su(eid="s")
        busy = FakeCtx(hand=["Ludicolo"], bench=[su] * 4)
        self.assertFalse(_su_lotad_ok(busy))            # no slot for backup
        out = FakeCtx(hand=["Lombre"], play=[FakeMon("Lotad")], bench=[])
        self.assertFalse(_su_lotad_ok(out))             # one line is enough
        two = FakeCtx(hand=["Lombre"], play=[self._su(eid="a"),
                                             self._su(eid="b")], bench=[])
        self.assertTrue(_su_lotad_ok(two))              # punchers secured

    # -- evolve / dance windows ---------------------------------------------
    def test_ludicolo_evolve_needs_the_window(self):
        ready = self._su(water=1, extra=1)
        ctx = FakeCtx(active=ready, play=[ready])
        self.assertTrue(
            _su_allow("EvolvePokemonPlayAbility", "Ludicolo", ctx))
        unready = self._su(water=0, extra=0)
        uctx = FakeCtx(active=unready, play=[unready])
        self.assertFalse(
            _su_allow("EvolvePokemonPlayAbility", "Ludicolo", uctx))
        lombre = FakeMon("Lombre", eid="l")
        lctx = FakeCtx(active=lombre, play=[lombre])
        self.assertTrue(
            _su_allow("EvolvePokemonPlayAbility", "Ludicolo", lctx))
        self.assertTrue(
            _su_allow("EvolvePokemonPlayAbility", "Drizzile", uctx))

    def test_dance_unlocks_only_in_the_100_window(self):
        su = self._su(water=1, extra=1)
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        opp_bench = [FakeMon("Drizzile", owner="p2", eid=f"o{i}")
                     for i in range(4)]

        def _with(hp):
            oa = FakeMon("Suicune V", owner="p2", hp=hp, max_hp=320,
                         eid="oa")
            return FakeCtx(active=su, play=[su] + mine, bench=mine,
                           opp_active=oa, opp_play=[oa] + opp_bench,
                           opp_bench=opp_bench)

        ctx = _with(250)
        self.assertTrue(_su_dance_window(ctx))
        self.assertEqual(_su_rondo_base(ctx), 180)       # 4 + 4 benched
        self.assertTrue(_su_dance_unlocks(ctx))         # 180 < 250 <= 280
        self.assertEqual(_su_evolve_score("Ludicolo", ctx), 950.0)
        low = _with(150)
        self.assertFalse(_su_dance_unlocks(low))        # already in range
        self.assertEqual(_su_evolve_score("Ludicolo", low), 700.0)
        high = _with(300)
        self.assertFalse(_su_dance_unlocks(high))       # 280 < 300

    def test_candy_pairs(self):
        self.assertEqual(
            _su_candy_pairs(FakeCtx(play=[FakeMon("Sobble")],
                                    hand=["Inteleon"])),
            [("Sobble", "Inteleon")])
        self.assertEqual(
            _su_candy_pairs(FakeCtx(play=[FakeMon("Lotad")],
                                    hand=["Ludicolo"])),
            [("Lotad", "Ludicolo")])
        self.assertEqual(_su_candy_pairs(FakeCtx(play=[], hand=[])), [])
        self.assertFalse(
            _su_allow("UseTrainerCard", "Rare Candy",
                      FakeCtx(play=[FakeMon("Sobble")], hand=[])))

    # -- values / searches ---------------------------------------------------
    def test_value_reflects_real_gaps(self):
        hungry = self._su(water=0)
        hctx = FakeCtx(active=hungry, play=[hungry])
        self.assertEqual(_su_value("Melony", hctx), 90.0)
        ready = self._su(water=1, extra=1)
        stocked = FakeCtx(active=ready, play=[ready], hand=["x"] * 7)
        self.assertEqual(_su_value("Melony", stocked), 45.0)
        self.assertEqual(_su_value("Water Energy", hctx), 85.0)
        self.assertEqual(_su_value("Water Energy", stocked), 40.0)
        self.assertEqual(
            _su_value("Professor's Research", FakeCtx(hand=["a"] * 4)), 80.0)
        self.assertEqual(
            _su_value("Professor's Research", FakeCtx(hand=["a"] * 7)), 20.0)
        marnie = FakeCtx(hand=["a"] * 3)
        marnie.hand_size = lambda pid=None: 6 if pid == marnie.opp else 3
        self.assertEqual(_su_value("Marnie", marnie), 70.0)

    def test_value_boss_tracks_the_gust_window(self):
        su = self._su(water=1, extra=1)
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        theirs = [FakeMon("Drizzile", owner="p2", hp=170, eid=f"o{i}")
                  for i in range(4)]
        window = FakeCtx(active=su, play=[su] + mine, bench=mine,
                         opp_play=theirs, opp_bench=theirs)
        self.assertEqual(_su_value("Boss's Orders", window), 95.0)
        tank = FakeMon("Suicune V", owner="p2", hp=320, max_hp=320,
                       eid="tank")
        scratched = FakeMon("Sobble", owner="p2", hp=30, max_hp=60,
                           eid="scr")
        clean = FakeCtx(active=su, play=[su], opp_play=[tank])
        self.assertEqual(_su_value("Boss's Orders", clean), 15.0)
        dirty = FakeCtx(active=su, play=[su], opp_play=[tank, scratched])
        self.assertEqual(_su_value("Boss's Orders", dirty), 45.0)

    def test_value_searchers_solve_gaps(self):
        # Drizzile fetch only matters when an un-evolved Sobble is out
        self.assertEqual(
            _su_value("Drizzile", FakeCtx(play=[FakeMon("Sobble")])), 80.0)
        self.assertEqual(_su_value("Drizzile", FakeCtx(play=[])), 6.0)
        # speculative Lotad stays cheap
        self.assertEqual(_su_value("Lotad", FakeCtx(hand=[])), 8.0)
        self.assertEqual(
            _su_value("Lotad", FakeCtx(hand=["Lombre"])), 40.0)
        # Level Ball first target: the missing Drizzile
        ball = FakeCtx(play=[FakeMon("Sobble")], hand=[])
        self.assertEqual(_su_value("Level Ball", ball), 80.0)
        self.assertEqual(_su_value("Level Ball", FakeCtx(play=[])), 65.0)
        full = FakeCtx(play=[FakeMon("Sobble"), FakeMon("Drizzile"),
                             FakeMon("Drizzile"), FakeMon("Drizzile")],
                       hand=[])
        self.assertEqual(_su_value("Level Ball", full), 10.0)
        # Quick Ball fetches the puncher when we have none
        self.assertEqual(_su_value("Quick Ball", FakeCtx(play=[])), 85.0)
        # Capacious Bucket stops digging once the puncher is loaded
        ready = self._su(water=1, extra=1)
        self.assertEqual(
            _su_value("Capacious Bucket", FakeCtx(active=ready,
                                                  play=[ready])), 20.0)

    def test_search_score_ranks_engine_over_dead_pieces(self):
        ctx = FakeCtx(play=[FakeMon("Sobble")])
        self.assertGreater(_su_search_score(FakeMon("Drizzile"), ctx),
                           _su_search_score(FakeMon("Lotad"), ctx))
        self.assertGreater(_su_search_score(FakeMon("Suicune V"),
                                            FakeCtx(play=[])),
                           _su_search_score(FakeMon("Lotad"),
                                            FakeCtx(play=[])))

    # -- actions -------------------------------------------------------------
    def test_action_score_routes_by_description(self):
        su = self._su(water=0)
        ctx = FakeCtx(active=su, play=[su])
        self.assertEqual(
            _su_action_score("DefaultPokemonPlayAbility", "Suicune V",
                             FakeCtx(play=[], bench=[])), 700.0)
        self.assertEqual(
            _su_action_score("UsePokemonAbility", "Fleet-Footed", ctx), 75.0)
        self.assertEqual(
            _su_action_score("UseTrainerCard", "Boss's Orders",
                             FakeCtx(active=su, play=[su])), 15.0)
        self.assertEqual(
            _su_action_score("DefaultEnergyPlayAbility", "Water Energy", ctx),
            120.0)
        self.assertEqual(_su_evolve_score("Drizzile", ctx), 800.0)
        self.assertEqual(_su_evolve_score("Inteleon", ctx), 650.0)

    def test_attack_scores_take_the_rondo_ko(self):
        su = self._su(water=1, extra=1)
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        theirs = [FakeMon("Sobble", owner="p2", eid=f"o{i}")
                  for i in range(4)]
        dying = FakeMon("Suicune V", owner="p2", hp=170, max_hp=210,
                        eid="die")
        tank = FakeMon("Suicune V", owner="p2", hp=300, max_hp=320,
                       eid="tank")
        ctx = FakeCtx(active=su, play=[su] + mine, bench=mine,
                      opp_active=dying, opp_play=[dying] + theirs,
                      opp_bench=theirs)
        self.assertEqual(_su_strike_damage(ctx), 180)
        self.assertEqual(_su_attack_score("Blizzard Rondo", 20, ctx),
                         800.0 + 180 + 1000.0)
        ctx_tank = FakeCtx(active=su, play=[su] + mine, bench=mine,
                           opp_active=tank, opp_play=[tank] + theirs,
                           opp_bench=theirs)
        self.assertEqual(_su_attack_score("Blizzard Rondo", 20, ctx_tank),
                         800.0 + 180)
        unready = self._su(water=0, extra=1)
        ctx_u = FakeCtx(active=unready, play=[unready])
        self.assertEqual(_su_attack_score("Blizzard Rondo", 20, ctx_u), 0.0)
        # ramp attacks only while the bench has room
        self.assertEqual(
            _su_attack_score("Keep Calling", 0, FakeCtx(bench=[])), 350.0)
        self.assertEqual(
            _su_attack_score("Keep Calling", 0, FakeCtx(bench=[mine] * 5)),
            0.0)
        self.assertEqual(
            _su_attack_score("Call for Family", 0, FakeCtx(bench=[])), 400.0)

    def test_allow_gates_boss_research_and_cape(self):
        su = self._su(water=0)
        uctx = FakeCtx(active=su, play=[su], hand=["a"] * 6)
        self.assertFalse(_su_allow("UseTrainerCard", "Boss's Orders", uctx))
        self.assertFalse(_su_allow("UseTrainerCard", "Professor's Research",
                                   uctx))
        self.assertTrue(_su_allow("UseTrainerCard", "Professor's Research",
                                  FakeCtx(hand=["a"] * 4)))
        # window: gust opens
        ready = self._su(water=1, extra=1)
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        targets = [FakeMon("Drizzile", owner="p2", hp=170, eid=f"o{i}")
                   for i in range(4)]
        wctx = FakeCtx(active=ready, play=[ready] + mine, bench=mine,
                       opp_play=targets, opp_bench=targets)
        self.assertTrue(_su_allow("UseTrainerCard", "Boss's Orders", wctx))
        # Cape only when the puncher has a free tool slot
        self.assertTrue(_su_allow("UseTrainerCard", "Cape of Toughness",
                                  FakeCtx(play=[self._su()])))
        self.assertFalse(_su_allow("UseTrainerCard", "Cape of Toughness",
                                   FakeCtx(play=[FakeMon("Sobble")])))

    def test_allow_bucket_never_mines_a_dry_deck(self):
        hungry = self._su(water=0)
        dry = FakeCtx(active=hungry, play=[hungry],
                      hand=["Water Energy"] * 6, discard=["Water Energy"] * 6)
        self.assertEqual(_su_water_left(dry), 0)
        self.assertFalse(_su_allow("UseTrainerCard", "Capacious Bucket", dry))
        wet = FakeCtx(active=hungry, play=[hungry])
        self.assertTrue(_su_allow("UseTrainerCard", "Capacious Bucket", wet))
        self.assertFalse(
            _su_allow("UseTrainerCard", "Capacious Bucket",
                      FakeCtx(active=self._su(water=1, extra=1),
                              play=[self._su(water=1, extra=1)])))

    def test_allow_attacks_rotate_into_the_puncher(self):
        su = self._su(water=1, extra=1)
        sobble = FakeMon("Sobble", energy=1, eid="s")
        rctx = FakeCtx(active=sobble, play=[sobble, su], bench=[su])
        self.assertFalse(_su_allow("UsePokemonAttack", "Sobble", rctx))
        broke = FakeMon("Sobble", energy=0, eid="s")
        bctx = FakeCtx(active=broke, play=[broke, su], bench=[su])
        self.assertTrue(_su_allow("UsePokemonAttack", "Sobble", bctx))
        full = FakeCtx(active=sobble,
                       play=[sobble] + [FakeMon("Sobble", eid=f"b{i}")
                                        for i in range(5)],
                       bench=[FakeMon("Sobble", eid=f"b{i}")
                              for i in range(5)])
        self.assertFalse(_su_allow("UsePokemonAttack", "Sobble", full))
        sctx = FakeCtx(active=su, play=[su], bench=[])
        self.assertTrue(_su_allow("UsePokemonAttack", "Suicune V", sctx))

    def test_retreat_and_rope_windows(self):
        ready = self._su(water=1, extra=1, eid="r")
        stuck = self._su(water=0, extra=0, eid="s")
        # stuck active, loaded bench: rotate
        self.assertTrue(_su_retreat_ok(
            FakeCtx(active=stuck, play=[stuck, ready], bench=[ready])))
        # loaded active, no damage: keep swinging
        self.assertFalse(_su_retreat_ok(
            FakeCtx(active=ready, play=[ready], bench=[stuck])))
        # loaded active, nearly dead: preserve it
        hurt = self._su(water=1, extra=1, eid="h", hp=210)
        hurt.hp = 80
        self.assertTrue(_su_retreat_ok(
            FakeCtx(active=hurt, play=[hurt, ready], bench=[ready])))
        # rope: rotate when the active can't swing ...
        self.assertTrue(_su_rope_ok(
            FakeCtx(active=stuck, play=[stuck, ready], bench=[ready])))
        # ... or when a bench body walks into Rondo's KO
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        target = FakeMon("Drizzile", owner="p2", hp=170, eid="o")
        opp_b = [target] + [FakeMon("Drizzile", owner="p2", hp=170,
                                    eid=f"w{i}") for i in range(3)]
        gctx = FakeCtx(active=ready, play=[ready] + mine, bench=mine,
                       opp_active=target, opp_play=[target],
                       opp_bench=opp_b)
        self.assertFalse(_su_rope_ok(gctx))   # active itself KOs it already
        tank = FakeMon("Suicune V", owner="p2", hp=300, max_hp=320,
                       eid="tank")
        hctx = FakeCtx(active=ready, play=[ready] + mine, bench=mine,
                       opp_active=tank, opp_play=[tank], opp_bench=opp_b)
        self.assertTrue(_su_rope_ok(hctx))

    # -- scooping / sniping ---------------------------------------------------
    def test_scoop_heals_wounded_bodies_only_with_a_bench(self):
        so = FakeMon("Sobble", hp=0, max_hp=60, eid="s")
        dry = FakeMon("Sobble", hp=60, max_hp=60, eid="d")
        active = FakeMon("Drizzile", hp=90, max_hp=90, eid="a")
        ctx = FakeCtx(active=active, play=[active, so, dry],
                      bench=[so, dry])
        self.assertEqual(_su_scoop(ctx, so), 1200.0)
        self.assertGreater(_su_scoop(ctx, active), _su_scoop(ctx, dry))
        self.assertEqual(_su_scoop(ctx, self._su()), 0.0)
        empty = FakeCtx(active=active, play=[active])
        self.assertLess(_su_scoop(empty, active), -900.0)
        self.assertFalse(_su_scoop_ok(empty))
        self.assertTrue(_su_scoop_ok(ctx))
        self.assertFalse(_su_scoop_ok(
            FakeCtx(active=dry, play=[dry], bench=[dry])))
        full = FakeCtx(play=[dry], bench=[dry] * 5, hand=["Drizzile"])
        self.assertTrue(_su_scoop_ok(full))

    def test_snipe_prefers_counter_kos(self):
        ctx = FakeCtx()
        dying = FakeMon("Sobble", owner="p2", hp=10, max_hp=60, eid="d")
        scratched = FakeMon("Suicune V", owner="p2", hp=260, max_hp=320,
                            eid="s")
        fresh = FakeMon("Sobble", owner="p2", hp=60, max_hp=60, eid="f")
        self.assertEqual(_su_snipe(ctx, dying), 1000.0)
        self.assertGreater(_su_snipe(ctx, scratched), _su_snipe(ctx, fresh))

    # -- pick branches ---------------------------------------------------------
    def test_pick_ranks_prompts(self):
        ready = self._su(water=1, extra=1, eid="r")
        stuck = self._su(water=0, extra=0, eid="s")
        ctx = FakeCtx(active=ready, play=[ready, stuck], bench=[stuck],
                      hand=["Ludicolo", "Inteleon"])
        promote = "Choose your new Active Pok\u00e9mon"
        self.assertGreater(_su_pick(promote, ctx, ready),
                           _su_pick(promote, ctx, stuck))
        snipe = "Choose 1 of your opponent's Pok\u00e9mon"
        dying = FakeMon("Sobble", owner="p2", hp=10, max_hp=60, eid="d")
        tank = FakeMon("Suicune V", owner="p2", hp=300, max_hp=320,
                       eid="t")
        self.assertGreater(_su_pick(snipe, ctx, dying),
                           _su_pick(snipe, ctx, tank))
        attach = "Choose a Pok\u00e9mon to attach the Energy to"
        self.assertEqual(_su_pick(attach, ctx, ready), 240.0)
        self.assertEqual(_su_pick(attach, ctx, stuck), 600.0)
        candy2 = "Choose a Stage 2 Pok\u00e9mon to evolve into"
        self.assertEqual(_su_pick(candy2, ctx, FakeMon("Inteleon")), 800.0)
        candy1 = "Choose a Basic Pok\u00e9mon in play"
        lotad = FakeMon("Lotad", eid="lo")
        lctx = FakeCtx(play=[lotad], hand=["Ludicolo"])
        self.assertEqual(_su_pick(candy1, lctx, lotad), 900.0)
        scooped = "Choose 1 of your Pok\u00e9mon to put into your hand"
        wounded = FakeMon("Sobble", hp=20, max_hp=60, eid="w")
        sctx = FakeCtx(active=wounded, play=[wounded], bench=[wounded])
        self.assertEqual(_su_pick(scooped, sctx, wounded), 600.0)
        discard = "Choose a card to discard"
        hctx = FakeCtx(hand=["Water Energy", "Capture Energy",
                             "Suicune V", "x"])
        self.assertGreater(_su_pick(discard, hctx,
                                    FakeMon("Capture Energy")),
                           _su_pick(discard, hctx, self._su()))

    def test_target_score_energy_boss_and_tool(self):
        su = self._su(water=0, eid="a")
        bench_su = self._su(water=1, extra=1, eid="b")
        ctx = FakeCtx(active=su, play=[su, bench_su], bench=[bench_su])
        self.assertEqual(
            _su_target_score("DefaultEnergyPlayAbility", "Water Energy",
                             ctx, "a"), 750.0)
        self.assertEqual(
            _su_target_score("DefaultToolPlayAbility", "Cape of Toughness",
                             ctx, "a"), 700.0)
        target = FakeMon("Drizzile", owner="p2", hp=170, eid="o")
        gctx = FakeCtx(active=su, play=[su], opp_play=[target])
        self.assertEqual(
            _su_target_score("UseTrainerCard", "Boss's Orders",
                             gctx, "o"), 0.0)   # unready: no gust value
        ready = self._su(water=1, extra=1, eid="r")
        mine = [FakeMon("Sobble", eid=f"m{i}") for i in range(4)]
        theirs = [FakeMon("Drizzile", owner="p2", hp=170, eid=f"t{i}")
                  for i in range(4)]
        wctx = FakeCtx(active=ready, play=[ready] + mine, bench=mine,
                       opp_play=theirs, opp_bench=theirs)
        self.assertGreater(
            _su_target_score("UseTrainerCard", "Boss's Orders",
                             wctx, "t0"), 900.0)


class CharizardBrainTests(unittest.TestCase):
    def test_registered_with_six_hooks(self):
        spec = strategy_for("Charizard (charizard-vmax)")
        self.assertIs(spec, CHARIZARD_VSTAR)
        for hook in ("allow_action", "action_score", "attack_score",
                     "target_score", "search_score", "pick_score"):
            self.assertTrue(callable(spec[hook]), hook)

    # -- Explosive Fire / readiness --------------------------------------
    def test_ready_requires_two_fire_and_three_total(self):
        z = FakeMon("Charizard VSTAR", fire=2, energy=3, hp=280, max_hp=280)
        self.assertTrue(_cz_ready(FakeCtx(active=z, play=[z]), z))
        thin = FakeMon("Charizard VSTAR", fire=1, energy=3, hp=280, max_hp=280)
        self.assertFalse(_cz_ready(FakeCtx(active=thin, play=[thin]), thin))
        self.assertFalse(
            _cz_ready(FakeCtx(), FakeMon("Charizard V", fire=3, energy=3)))

    def test_output_130_clean_230_damaged(self):
        clean = FakeMon("Charizard VSTAR", fire=2, energy=3,
                        hp=280, max_hp=280)
        self.assertEqual(_cz_output(FakeCtx(active=clean, play=[clean]), clean),
                         130)
        hurt = FakeMon("Charizard VSTAR", fire=2, energy=3,
                       hp=250, max_hp=280)
        self.assertEqual(_cz_output(FakeCtx(active=hurt, play=[hurt]), hurt),
                         230)

    # -- Star Blaze (VSTAR Power) ----------------------------------------
    def test_star_blaze_only_where_230_cannot_answer(self):
        big = FakeCtx(opp_active=FakeMon("Big VMAX", hp=300, max_hp=320,
                                         prize=3))
        self.assertTrue(_cz_star_blaze_window(big))
        small = FakeCtx(opp_active=FakeMon("Moltres", hp=200, max_hp=280,
                                           prize=1))
        self.assertFalse(_cz_star_blaze_window(small))
        exact = FakeCtx(opp_active=FakeMon("Zard", hp=230, max_hp=280))
        self.assertFalse(_cz_star_blaze_window(exact))
        too_big = FakeCtx(opp_active=FakeMon("Zard", hp=350, max_hp=380))
        self.assertFalse(_cz_star_blaze_window(too_big))
        self.assertFalse(_cz_star_blaze_window(FakeCtx()))

    def test_star_blaze_blocked_once_vstar_spent(self):
        ctx = FakeCtx(opp_active=FakeMon("Mew VMAX", hp=300, max_hp=320,
                                         prize=3))
        self.assertTrue(_cz_star_blaze_window(ctx))
        ctx.session = SimpleNamespace(
            turn_state=SimpleNamespace(vstar_used={"p1"}))
        self.assertFalse(_cz_star_blaze_window(ctx))

    # -- attack scores ----------------------------------------------------
    def test_explosive_fire_prefers_the_ko(self):
        z = FakeMon("Charizard VSTAR", fire=2, energy=3,
                    hp=250, max_hp=280)          # damaged -> 230
        victim = FakeMon("VMAX", hp=200, max_hp=320, prize=3, owner="p2")
        ctx = FakeCtx(active=z, opp_active=victim, play=[z])
        self.assertEqual(_cz_attack_score("Explosive Fire", 0, ctx), 2030.0)
        clean = FakeMon("Charizard VSTAR", fire=2, energy=3,
                        hp=280, max_hp=280)      # clean -> 130, still KOs 120
        victim2 = FakeMon("Moltres", hp=120, max_hp=120, owner="p2")
        ctx2 = FakeCtx(active=clean, opp_active=victim2, play=[clean])
        self.assertEqual(_cz_attack_score("Explosive Fire", 0, ctx2), 1930.0)
        unready = FakeCtx(
            active=FakeMon("Charizard VSTAR", hp=280, max_hp=280),
            opp_active=FakeMon("VMAX", hp=200, max_hp=320, owner="p2"))
        self.assertEqual(_cz_attack_score("Explosive Fire", 0, unready), 0.0)

    def test_star_blaze_score_gated_on_window(self):
        z = FakeMon("Charizard VSTAR", fire=3, energy=4,
                    hp=250, max_hp=280)
        window = FakeCtx(active=z, opp_active=FakeMon("VMAX", hp=300,
                                                      max_hp=320, prize=3,
                                                      owner="p2"),
                         play=[z])
        self.assertEqual(_cz_attack_score("Star Blaze", 0, window), 3000.0)
        no = FakeCtx(active=z, opp_active=FakeMon("VMAX", hp=200,
                                                  max_hp=320, owner="p2"),
                     play=[z])
        self.assertEqual(_cz_attack_score("Star Blaze", 0, no), 0.0)

    def test_charizard_v_and_moltres_attacks(self):
        v = FakeMon("Charizard V", fire=2, energy=3, hp=220, max_hp=220)
        ctx = FakeCtx(active=v, opp_active=FakeMon("Mew", hp=60, max_hp=60,
                                                   owner="p2"), play=[v])
        self.assertEqual(_cz_attack_score("Incinerate", 0, ctx), 1650.0)
        self.assertEqual(
            _cz_attack_score("Heat Blast", 0,
                             FakeCtx(active=v, play=[v],
                                     opp_active=FakeMon("x", hp=200,
                                                        max_hp=200,
                                                        owner="p2"))),
            0.0)                                     # 4-unit cost unpaid
        m = FakeMon("Moltres", fire=1, energy=1, hp=100, max_hp=120)
        mctx = FakeCtx(active=m, opp_active=FakeMon("x", hp=70, max_hp=70,
                                                    owner="p2"), play=[m])
        self.assertEqual(_cz_attack_score("Inferno Wings", 0, mctx), 1520.0)

    # -- bench / value / energy ------------------------------------------
    def test_bench_score_line_first_support_by_need(self):
        self.assertEqual(_cz_bench_score("Charizard V", FakeCtx()), 700.0)
        one = FakeCtx(play=[FakeMon("Charizard V", hp=220, max_hp=220)])
        self.assertEqual(_cz_bench_score("Charizard V", one), 450.0)
        three = FakeCtx(play=[FakeMon("Charizard V", hp=220, max_hp=220)] * 3)
        self.assertEqual(_cz_bench_score("Charizard V", three), 40.0)
        self.assertEqual(_cz_bench_score("Moltres", FakeCtx()), 420.0)
        loaded_hand = FakeCtx(hand=["Boss's Orders", "Research", "Marnie",
                                    "Switch", "Switch", "Quick Ball",
                                    "Ultra Ball"])
        self.assertEqual(_cz_bench_score("Crobat V", loaded_hand), 0.0)
        small_hand = FakeCtx(hand=["Quick Ball"] * 3)
        self.assertEqual(_cz_bench_score("Crobat V", small_hand), 500.0)
        with_sup = FakeCtx(hand=["Boss's Orders", "Marnie", "Switch",
                                 "Switch", "Air Balloon", "Quick Ball",
                                 "Ultra Ball"])
        self.assertEqual(_cz_bench_score("Lumineon V", with_sup), 0.0)
        no_sup = FakeCtx(hand=["Switch", "Switch", "Fire Energy",
                               "Fire Energy"])
        self.assertEqual(_cz_bench_score("Lumineon V", no_sup), 450.0)
        self.assertEqual(_cz_bench_score("Mew", FakeCtx(hand=["Fire Energy"])),
                         300.0)

    def test_value_ladder(self):
        z = FakeMon("Charizard VSTAR", fire=2, energy=3,
                    hp=250, max_hp=280)
        window = FakeCtx(active=z, play=[z],
                         opp_play=[FakeMon("Crobat V", hp=100, max_hp=180,
                                           prize=2, owner="p2")])
        self.assertEqual(_cz_value("Boss's Orders", window, in_hand=True),
                         95.0)
        no_window = FakeCtx(active=z, play=[z],
                            opp_play=[FakeMon("Big", hp=300, max_hp=300,
                                              owner="p2")])
        self.assertEqual(_cz_value("Boss's Orders", no_window, in_hand=True),
                         15.0)
        self.assertEqual(
            _cz_value("Professor's Research",
                      FakeCtx(hand=["a", "b", "c"]), in_hand=True), 80.0)
        self.assertEqual(
            _cz_value("Professor's Research",
                      FakeCtx(hand=list("abcdefg")), in_hand=True), 20.0)
        basin = FakeCtx(discard=("Fire Energy",),
                        bench=(FakeMon("Charizard V", hp=220, max_hp=220),))
        self.assertEqual(_cz_value("Magma Basin", basin, in_hand=True), 75.0)
        self.assertEqual(_cz_value("Magma Basin", FakeCtx(), in_hand=True),
                         10.0)

    def test_zinnia_needs_hand_and_opponent_board(self):
        ready = FakeCtx(hand=list("abcdef"),
                        opp_play=[FakeMon("a", owner="p2"),
                                  FakeMon("b", owner="p2"),
                                  FakeMon("c", owner="p2"),
                                  FakeMon("d", owner="p2")])
        self.assertEqual(_cz_value("Zinnia's Resolve", ready, in_hand=True),
                         65.0)
        thin = FakeCtx(hand=list("abc"),
                       opp_play=[FakeMon("a", owner="p2")])
        self.assertEqual(_cz_value("Zinnia's Resolve", thin, in_hand=True),
                         25.0)

    def test_energy_target_prefers_open_slots(self):
        active = FakeMon("Charizard VSTAR", fire=1, energy=2,
                         hp=280, max_hp=280)
        ctx = FakeCtx(active=active, play=[active])
        self.assertEqual(
            _cz_energy_target_score(ctx, active, "Fire Energy"), 770.0)
        self.assertEqual(
            _cz_energy_target_score(ctx, active, "Heat Fire Energy"), 830.0)
        loaded = FakeMon("Charizard VSTAR", fire=2, energy=3,
                         hp=250, max_hp=280)
        ctx2 = FakeCtx(active=loaded, play=[loaded])
        self.assertEqual(
            _cz_energy_target_score(ctx2, loaded, "Fire Energy"), 260.0)
        # threatened Active: the benched Charizard grows first
        doomed = FakeMon("Charizard VSTAR", fire=2, energy=3,
                         hp=160, max_hp=280)
        bench_z = FakeMon("Charizard V", hp=220, max_hp=220)
        ctx3 = FakeCtx(active=doomed, bench=(bench_z,), play=[doomed, bench_z])
        self.assertEqual(
            _cz_energy_target_score(ctx3, bench_z, "Fire Energy"), 780.0)

    def test_energy_value_heat_fire_on_the_active(self):
        active = FakeMon("Charizard VSTAR", fire=2, energy=2,
                         hp=280, max_hp=280)
        ctx = FakeCtx(active=active, play=[active])
        self.assertEqual(_cz_energy_value("Heat Fire Energy", ctx), 140.0)
        self.assertEqual(_cz_energy_value("Fire Energy", ctx), 125.0)

    # -- promote / gust / retreat ----------------------------------------
    def test_promote_ready_first(self):
        ready = FakeMon("Charizard VSTAR", fire=2, energy=3,
                        hp=280, max_hp=280)
        dev = FakeMon("Charizard VSTAR", hp=280, max_hp=280)
        mew = FakeMon("Mew", hp=60, max_hp=60)
        ctx = FakeCtx(active=ready, play=[ready, dev, mew])
        self.assertEqual(_cz_promote(ctx, ready), 2030.0)
        self.assertEqual(_cz_promote(ctx, dev), 900.0)
        self.assertEqual(_cz_promote(ctx, mew), 350.0)

    def test_gust_scores_ko_window(self):
        z = FakeMon("Charizard VSTAR", fire=2, energy=3,
                    hp=250, max_hp=280)
        ctx = FakeCtx(active=z, play=[z])
        target = FakeMon("V", hp=200, max_hp=280, prize=2, owner="p2")
        self.assertEqual(_cz_gust(ctx, target), 1000.0)
        self.assertEqual(len(_cz_gust_window(ctx)), 0)   # only opp Active dies
        ctx2 = FakeCtx(active=z, play=[z],
                       opp_play=[FakeMon("V", hp=100, max_hp=280, owner="p2")])
        self.assertEqual(len(_cz_gust_window(ctx2)), 1)

    def test_retreat_gate(self):
        ready = FakeMon("Charizard VSTAR", fire=2, energy=3,
                        hp=280, max_hp=280)
        stuck = FakeMon("Charizard VSTAR", fire=1, energy=1,
                        hp=280, max_hp=280)
        self.assertTrue(
            _cz_retreat_ok(FakeCtx(active=stuck, bench=(ready,),
                                   play=[stuck, ready])))
        self.assertFalse(_cz_retreat_ok(FakeCtx(active=ready, play=[ready])))
        doom = FakeMon("Charizard VSTAR", fire=2, energy=3,
                       hp=160, max_hp=280)
        self.assertTrue(
            _cz_retreat_ok(FakeCtx(active=doom, bench=(ready,),
                                   play=[doom, ready])))

    # -- allow gates -------------------------------------------------------
    def test_allow_gates(self):
        z = FakeMon("Charizard VSTAR", fire=2, energy=3, hp=280, max_hp=280)
        win = FakeCtx(active=z, play=[z],
                      opp_active=FakeMon("M", hp=300, max_hp=320, prize=3,
                                         owner="p2"),
                      opp_play=[FakeMon("V", hp=100, max_hp=280, owner="p2")])
        self.assertTrue(_cz_allow("UsePokemonAttack", "Star Blaze", win))
        lose = FakeCtx(active=z, play=[z],
                       opp_active=FakeMon("M", hp=200, max_hp=280, owner="p2"))
        self.assertFalse(_cz_allow("UsePokemonAttack", "Star Blaze", lose))
        self.assertTrue(_cz_allow("UsePokemonAttack", "Explosive Fire", lose))

        self.assertFalse(_cz_allow(
            "UseTrainerCard", "Professor's Research",
            FakeCtx(hand=list("abcdef"), deck=12)))
        self.assertTrue(_cz_allow(
            "UseTrainerCard", "Professor's Research",
            FakeCtx(hand=list("abcd"), deck=12)))
        self.assertFalse(_cz_allow(
            "UseTrainerCard", "Professor's Research",
            FakeCtx(hand=list("abcd"), deck=6)))
        self.assertFalse(_cz_allow("UseTrainerCard", "Boss's Orders",
                                   FakeCtx()))

        basin_ready = FakeCtx(
            discard=("Heat Fire Energy",),
            bench=(FakeMon("Moltres", hp=120, max_hp=120),))
        self.assertTrue(_cz_allow("DefaultStadiumPlayAbility", "Magma Basin",
                                  basin_ready))
        self.assertTrue(_cz_allow("UseTrainerCard", "Magma Basin",
                                  basin_ready))
        self.assertFalse(_cz_allow("DefaultStadiumPlayAbility", "Magma Basin",
                                   FakeCtx()))
        stadium_up = FakeCtx(stadium="Magma Basin",
                             discard=("Fire Energy",),
                             bench=(FakeMon("Moltres", hp=120, max_hp=120),))
        self.assertFalse(_cz_allow("DefaultStadiumPlayAbility", "Magma Basin",
                                   stadium_up))

        self.assertFalse(_cz_allow("DefaultPokemonPlayAbility", "Crobat V",
                                   FakeCtx(hand=list("abcdefg"))))
        self.assertTrue(_cz_allow("DefaultPokemonPlayAbility", "Crobat V",
                                  FakeCtx(hand=list("abc"))))
        self.assertFalse(_cz_allow(
            "DefaultPokemonPlayAbility", "Lumineon V",
            FakeCtx(hand=["Boss's Orders", "Switch", "Switch", "Marnie",
                          "Quick Ball", "Ultra Ball", "Magma Basin"])))
        self.assertTrue(_cz_allow("DefaultPokemonPlayAbility", "Lumineon V",
                                  FakeCtx(hand=["Switch", "Switch",
                                                "Fire Energy"])))

    # -- picker routing ----------------------------------------------------
    def test_pick_routing(self):
        ready = FakeMon("Charizard VSTAR", fire=2, energy=3,
                        hp=250, max_hp=280)
        ctx = FakeCtx(active=ready, play=[ready])
        dev_v = FakeMon("Charizard V", hp=220, max_hp=220, owner="p1")
        self.assertEqual(
            _cz_pick("Choose your new Active Pokemon", ctx, dev_v), 600.0)
        # Magma Basin bench target: open Fire gaps first
        self.assertEqual(
            _cz_pick("Choose 1 of your Benched Fire Pokemon", ctx, dev_v),
            580.0)
        # opponent switch: KO window first
        weak = FakeMon("Mew", hp=30, max_hp=60, owner="p2")
        self.assertEqual(
            _cz_pick("Choose your opponent's new Active", ctx, weak), 1070.0)
        # energy card itself
        self.assertEqual(
            _cz_pick("Choose a Fire Energy card to attach.", ctx,
                     FakeMon("Fire Energy", owner="p1")), 100.0)
        # hand discard: dump the least valuable card
        disc_ctx = FakeCtx(hand=["Marnie", "Marnie"])
        self.assertEqual(
            _cz_pick("Discard 2 cards", disc_ctx, FakeMon("Marnie")),
            -50.0)

    def test_search_score_is_the_value_ladder(self):
        zards_out = FakeCtx(play=[FakeMon("Charizard V", hp=220,
                                          max_hp=220)])
        self.assertEqual(
            _cz_search_score(FakeMon("Charizard VSTAR"), zards_out), 90.0)
        empty = FakeCtx()
        self.assertEqual(
            _cz_search_score(FakeMon("Quick Ball"), empty), 85.0)


class WiringTests(unittest.TestCase):
    def test_ai_player_attaches_brain_from_deck_name(self):
        from spirit.game.session.ai_player import AIPlayer
        player = AIPlayer("bot-1", "Bot", {"deckName": "Dragapult Inteleon"}, None)
        self.assertIs(player.deck_strategy, DRAGAPULT_INTELEON)
        ray = AIPlayer("bot-4", "Bot", {"deckName": "Rayquaza V"}, None)
        self.assertIs(ray.deck_strategy, RAYQUAZA_VMAX_FLAFFY)
        zard = AIPlayer("bot-5", "Bot",
                        {"deckName": "Charizard (charizard-vmax)"}, None)
        self.assertIs(zard.deck_strategy, CHARIZARD_VSTAR)
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
