"""End-to-end unit tests for BATCH A of the Mew VMAX deck spec: the
Trainer/Stadium/Pokemon Tool cards in spirit/game/card_effects/trainers.py
and their script wiring (spirit/game/scripts/cards/**)."""

import importlib.util
import os
import unittest
from unittest.mock import AsyncMock, patch

from spirit.tests.test_phase1_engine import EngineTestBase, P1, P2, make_card

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects import trainers
from spirit.game.card_effects.energies import DoubleTurboPassive
from spirit.game.card_effects.pokemon import ChoiceBeltPassive
from spirit.game.data_utils import (
    Ability,
    Activations,
    Attack,
    EnergyCardDef,
    ItemCardDef,
    PokemonCardDef,
    PokemonStage,
    PokemonToolCardDef,
    StadiumCardDef,
    SupporterCardDef,
)
from spirit.game.models.board import BoardState, create_card_entity
from spirit.game.session.effects import EffectContext, resolve_trainer_effect
from spirit.game.session.passives import ability_locked, compute_damage

SCRIPTS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "game", "scripts", "cards"
)


def load_script(*parts):
    """Imports a card script module directly, bypassing the full loader."""
    path = os.path.join(SCRIPTS_DIR, *parts)
    spec = importlib.util.spec_from_file_location(
        "test_script_" + "_".join(parts), path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.card


# ----------------------------------------------------------------------
# Local test fixtures (guids under a private 40000000 prefix, unused
# elsewhere in the suite)
# ----------------------------------------------------------------------

BASIC_DEF = PokemonCardDef(
    guid="40000000-0000-0000-0000-0000000000a1",
    key="TST", name="com.test.pokemon.Basic.Name",
    collector_number=901, set_code="TST", rarity=1,
    hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC,
)
STAGE1_DEF = PokemonCardDef(
    guid="40000000-0000-0000-0000-0000000000a2",
    key="TST", name="com.test.pokemon.Stage1.Name",
    collector_number=902, set_code="TST", rarity=1,
    hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1,
)
WATER_BASIC_DEF = PokemonCardDef(
    guid="40000000-0000-0000-0000-0000000000a3",
    key="TST", name="com.test.pokemon.WaterBasic.Name",
    collector_number=903, set_code="TST", rarity=1,
    hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC,
)
V_POKEMON_DEF = PokemonCardDef(
    guid="40000000-0000-0000-0000-0000000000a4",
    key="TST", name="com.test.pokemon.VMon.Name",
    collector_number=904, set_code="TST", rarity=1,
    hp=200, elements=[PokemonTypes.COLORLESS], subtypes=["V"],
)
PLAIN_MON_DEF = PokemonCardDef(
    guid="40000000-0000-0000-0000-0000000000a5",
    key="TST", name="com.test.pokemon.Plain.Name",
    collector_number=905, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS],
)
FUSION_ATTACKER_DEF = PokemonCardDef(
    guid="40000000-0000-0000-0000-0000000000a6",
    key="TST", name="com.test.pokemon.FusionAttacker.Name",
    collector_number=906, set_code="TST", rarity=1,
    hp=120, elements=[PokemonTypes.COLORLESS], subtypes=["Fusion Strike"],
    abilities=[Attack("Poke Punch", cost={PokemonTypes.COLORLESS: 1}, damage=50)],
)
FUSION_ATTACK = FUSION_ATTACKER_DEF.abilities[0]

SUPPORTER_FILLER_DEF = SupporterCardDef(
    guid="40000000-0000-0000-0000-0000000000c1",
    key="TST", name="com.test.trainer.SupporterFiller.Name",
    collector_number=920, set_code="TST", rarity=1,
)
ITEM_FILLER_DEF = ItemCardDef(
    guid="40000000-0000-0000-0000-0000000000c2",
    key="TST", name="com.test.trainer.ItemFiller.Name",
    collector_number=921, set_code="TST", rarity=1,
)
SPECIAL_ENERGY_DEF = EnergyCardDef(
    guid="40000000-0000-0000-0000-0000000000e1",
    key="TST", name="com.test.energy.Special.Name",
    collector_number=930, set_code="TST", rarity=0,
    energy_type=PokemonTypes.WATER, is_special=True,
)
PLAIN_ENERGY_DEF = EnergyCardDef(
    guid="40000000-0000-0000-0000-0000000000e2",
    key="TST", name="com.test.energy.Plain.Name",
    collector_number=931, set_code="TST", rarity=0,
    energy_type=PokemonTypes.COLORLESS,
)


def deck_of(count, definition=BASIC_DEF):
    return [make_card(definition) for _ in range(count)]


class TrainerDeckTestBase(EngineTestBase):
    async def play_trainer(self, card_def, player_id=P1):
        """Runs a trainer's registered effect through the trainer-slot flow,
        mirroring GameSession._execute_play_trainer's board state."""
        card = self.add_to("discard", make_card(card_def), player_id)
        trainer_area = self.board.find_global_area("activeTrainer")
        self.board.move_card(card.entity_id, trainer_area.entity_id)
        card.owning_player_id = player_id
        return await resolve_trainer_effect(self.session, player_id, card)


# ----------------------------------------------------------------------
# 1. Switch
# ----------------------------------------------------------------------

class TestSwitch(TrainerDeckTestBase):
    def test_condition_requires_own_bench(self):
        self.assertFalse(trainers.player_has_bench(self.board, P1))
        self.add_to("bench", make_card(BASIC_DEF), P1)
        self.assertTrue(trainers.player_has_bench(self.board, P1))

    async def test_switches_active_with_chosen_benched_pokemon(self):
        self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P1)
        benched = self.add_to("bench", make_card(BASIC_DEF), P1)
        await trainers.switch(EffectContext(self.session, P1, benched, None))
        self.assertIs(self.board.active_pokemon(P1), benched)


# ----------------------------------------------------------------------
# 2. Pal Pad
# ----------------------------------------------------------------------

class TestPalPad(TrainerDeckTestBase):
    def test_condition_requires_supporter_in_discard(self):
        self.assertFalse(trainers.has_supporter_in_discard(self.board, P1))
        self.add_to("discard", make_card(SUPPORTER_FILLER_DEF), P1)
        self.assertTrue(trainers.has_supporter_in_discard(self.board, P1))

    async def test_shuffles_up_to_2_supporters_into_deck(self):
        supporters = [self.add_to("discard", make_card(SUPPORTER_FILLER_DEF), P1)
                      for _ in range(3)]
        item = self.add_to("discard", make_card(ITEM_FILLER_DEF), P1)
        self.session.chooser_replies = [
            [supporters[0].entity_id, supporters[1].entity_id]
        ]
        await trainers.pal_pad(EffectContext(self.session, P1, supporters[0], None))
        deck = self.board.find_player_area(P1, "deck")
        self.assertIn(supporters[0], deck.children)
        self.assertIn(supporters[1], deck.children)
        discard = self.board.find_player_area(P1, "discard")
        self.assertIn(supporters[2], discard.children)
        self.assertIn(item, discard.children)  # not a Supporter: untouched
        # Only Supporters were offered to the chooser.
        offered = self.session.chooser_calls[0][1]
        self.assertNotIn(item.entity_id, offered)


# ----------------------------------------------------------------------
# 3. Judge
# ----------------------------------------------------------------------

class TestJudge(TrainerDeckTestBase):
    async def test_each_player_shuffles_hand_and_draws_4(self):
        for _ in range(2):
            self.add_to("hand", make_card(BASIC_DEF), P1)
            self.add_to("hand", make_card(BASIC_DEF), P2)
        for _ in range(8):
            self.add_to("deck", make_card(BASIC_DEF), P1)
            self.add_to("deck", make_card(BASIC_DEF), P2)
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        await trainers.judge(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 4)
        self.assertEqual(len(self.board.find_player_area(P2, "hand").children), 4)


# ----------------------------------------------------------------------
# 4. Roxanne
# ----------------------------------------------------------------------

class TestRoxanne(TrainerDeckTestBase):
    def test_condition_gates_on_opponent_prizes_remaining(self):
        for _ in range(4):
            self.add_to("prizePile", make_card(BASIC_DEF), P2)
        self.assertFalse(trainers.opponent_prizes_low(self.board, P1))
        prize_pile = self.board.find_player_area(P2, "prizePile")
        discard = self.board.find_player_area(P2, "discard")
        # Taking 1 prize leaves 3 remaining: the condition flips on.
        self.board.move_card(prize_pile.children[0].entity_id, discard.entity_id)
        self.assertTrue(trainers.opponent_prizes_low(self.board, P1))

    async def test_self_draws_6_opponent_draws_2(self):
        self.add_to("hand", make_card(BASIC_DEF), P1)
        self.add_to("hand", make_card(BASIC_DEF), P2)
        for _ in range(10):
            self.add_to("deck", make_card(BASIC_DEF), P1)
            self.add_to("deck", make_card(BASIC_DEF), P2)
        await trainers.roxanne(EffectContext(self.session, P1, None, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 6)
        self.assertEqual(len(self.board.find_player_area(P2, "hand").children), 2)


# ----------------------------------------------------------------------
# 5. Cyllene
# ----------------------------------------------------------------------

class TestCyllene(TrainerDeckTestBase):
    def test_condition_requires_a_discarded_card(self):
        self.assertFalse(trainers.has_discard_card(self.board, P1))
        self.add_to("discard", make_card(BASIC_DEF), P1)
        self.assertTrue(trainers.has_discard_card(self.board, P1))

    async def test_two_heads_puts_two_cards_on_top_in_order(self):
        card_a = self.add_to("discard", make_card(BASIC_DEF), P1)
        card_b = self.add_to("discard", make_card(STAGE1_DEF), P1)
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        self.session.chooser_replies = [[card_a.entity_id, card_b.entity_id]]
        with patch("spirit.game.session.effects.random.choice", side_effect=[0, 0]), \
             patch("spirit.game.session.effects.asyncio.sleep", new=AsyncMock()):
            await trainers.cyllene(EffectContext(self.session, P1, source, None))
        deck = self.board.find_player_area(P1, "deck")
        # card_b was picked last -> ends up on top of the deck.
        self.assertEqual(deck.children[-1], card_b)
        self.assertIn(card_a, deck.children)

    async def test_all_tails_moves_nothing(self):
        self.add_to("discard", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        with patch("spirit.game.session.effects.random.choice", side_effect=[1, 1]), \
             patch("spirit.game.session.effects.asyncio.sleep", new=AsyncMock()):
            await trainers.cyllene(EffectContext(self.session, P1, source, None))
        self.assertEqual(self.session.chooser_calls, [])


# ----------------------------------------------------------------------
# 6. Battle VIP Pass
# ----------------------------------------------------------------------

class TestBattleVIPPass(TrainerDeckTestBase):
    def test_condition_first_turn_and_bench_space_only(self):
        self.session.turn_state.turn_number = 2
        self.assertTrue(trainers.battle_vip_pass_playable(self.board, P1))
        self.session.turn_state.turn_number = 3
        self.assertFalse(trainers.battle_vip_pass_playable(self.board, P1))

    def test_condition_false_when_bench_full(self):
        self.session.turn_state.turn_number = 1
        for _ in range(5):
            self.add_to("bench", make_card(BASIC_DEF), P1)
        self.assertFalse(trainers.battle_vip_pass_playable(self.board, P1))

    async def test_benches_up_to_2_basics_and_shuffles(self):
        basics = [self.add_to("deck", make_card(BASIC_DEF), P1) for _ in range(2)]
        self.add_to("deck", make_card(STAGE1_DEF), P1)  # not Basic: filtered
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        self.session.chooser_replies = [[c.entity_id for c in basics]]
        await trainers.battle_vip_pass(EffectContext(self.session, P1, source, None))
        bench = self.board.find_player_area(P1, "bench")
        for card in basics:
            self.assertIn(card, bench.children)

    async def test_caps_search_count_by_remaining_bench_space(self):
        for _ in range(4):
            self.add_to("bench", make_card(BASIC_DEF), P1)  # 1 slot left
        basic = self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        await trainers.battle_vip_pass(EffectContext(self.session, P1, source, None))
        self.assertEqual(self.session.chooser_calls[0][2], 1)  # count capped to 1
        self.assertIn(basic, self.board.find_player_area(P1, "bench").children)


# ----------------------------------------------------------------------
# 7. Power Tablet
# ----------------------------------------------------------------------

class TestPowerTablet(TrainerDeckTestBase):
    async def test_adds_30_damage_modifier_for_fusion_strike_this_turn(self):
        attacker = self.add_to("activePokemonArea", make_card(FUSION_ATTACKER_DEF), P1)
        target = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P2)
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        await trainers.power_tablet(EffectContext(self.session, P1, source, None))
        calc = compute_damage(self.board, attacker, target, 50)
        self.assertEqual(calc.amount, 80)

    async def test_no_condition_gate(self):
        card = load_script("SWSH8", "PowerTablet_281.py")
        self.assertIsNone(card.condition)


# ----------------------------------------------------------------------
# 8. Cram-o-matic
# ----------------------------------------------------------------------

class TestCramomatic(TrainerDeckTestBase):
    def test_condition_requires_another_item_besides_itself(self):
        self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)  # itself, conceptually
        self.assertFalse(trainers.has_other_item_in_hand(self.board, P1))
        self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        self.assertTrue(trainers.has_other_item_in_hand(self.board, P1))

    async def test_heads_searches_deck_without_revealing(self):
        fodder = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        kept = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)  # not discardable
        found = self.add_to("deck", make_card(BASIC_DEF), P1)
        self.session.chooser_replies = [[fodder.entity_id], [found.entity_id]]
        with patch("spirit.game.session.effects.random.choice", side_effect=[0]):
            ctx = EffectContext(self.session, P1, fodder, None)
            await trainers.cramomatic(ctx)
        self.assertIn(fodder, self.board.find_player_area(P1, "discard").children)
        self.assertIn(kept, self.board.find_player_area(P1, "hand").children)
        self.assertIn(found, self.board.find_player_area(P1, "hand").children)
        # No "reveal it" clause: the opponent never learns the found card's
        # identity (no EntityIntroduced for it), unlike the discarded fodder
        # (discarding is always public).
        p2_intros = {m["value"]["entityID"] for m in ctx.messages_for(P2)
                     if m["name"] == "EntityIntroduced"}
        self.assertNotIn(found.entity_id, p2_intros)
        self.assertIn(fodder.entity_id, p2_intros)

    async def test_tails_does_not_search(self):
        fodder = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        self.add_to("deck", make_card(BASIC_DEF), P1)
        self.session.chooser_replies = [[fodder.entity_id]]
        with patch("spirit.game.session.effects.random.choice", side_effect=[1]):
            ctx = EffectContext(self.session, P1, fodder, None)
            await trainers.cramomatic(ctx)
        self.assertEqual(len(self.session.chooser_calls), 1)  # only the discard pick


# ----------------------------------------------------------------------
# 9. Rotom Phone
# ----------------------------------------------------------------------

class TestRotomPhone(TrainerDeckTestBase):
    def test_condition_requires_nonempty_deck(self):
        self.assertFalse(trainers.deck_nonempty(self.board, P1))
        self.add_to("deck", make_card(BASIC_DEF), P1)
        self.assertTrue(trainers.deck_nonempty(self.board, P1))

    async def test_looks_at_top_5_and_puts_chosen_on_top(self):
        cards = [self.add_to("deck", make_card(BASIC_DEF), P1) for _ in range(7)]
        top5 = list(reversed(cards[-5:]))
        chosen = top5[2]
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        self.session.chooser_replies = [[chosen.entity_id]]
        await trainers.rotom_phone(EffectContext(self.session, P1, source, None))
        deck = self.board.find_player_area(P1, "deck")
        self.assertEqual(deck.children[-1], chosen)
        self.assertEqual(set(deck.children), set(cards))  # nothing lost


# ----------------------------------------------------------------------
# 10. Fan of Waves
# ----------------------------------------------------------------------

class TestFanOfWaves(TrainerDeckTestBase):
    def test_condition_requires_opponent_special_energy(self):
        pokemon = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P2)
        self.assertFalse(trainers.opponent_has_special_energy(self.board, P1))
        energy = self.add_to("discard", make_card(SPECIAL_ENERGY_DEF), P2)
        self.board.attach_card(energy.entity_id, pokemon.entity_id)
        self.assertTrue(trainers.opponent_has_special_energy(self.board, P1))

    async def test_puts_special_energy_on_bottom_of_opponents_deck(self):
        pokemon = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P2)
        energy = self.add_to("discard", make_card(SPECIAL_ENERGY_DEF), P2)
        self.board.attach_card(energy.entity_id, pokemon.entity_id)
        plain_energy = self.add_to("discard", make_card(PLAIN_ENERGY_DEF), P2)
        self.board.attach_card(plain_energy.entity_id, pokemon.entity_id)
        self.add_to("deck", make_card(BASIC_DEF), P2)
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        await trainers.fan_of_waves(EffectContext(self.session, P1, source, None))
        deck = self.board.find_player_area(P2, "deck")
        self.assertEqual(deck.children[0], energy)  # bottom of deck = index 0
        # The plain (non-Special) Energy was never a valid target.
        self.assertNotIn(plain_energy, deck.children)
        offered = self.session.chooser_calls[0][1]
        self.assertNotIn(plain_energy.entity_id, offered)


# ----------------------------------------------------------------------
# 11. Big Parasol
# ----------------------------------------------------------------------

BIG_PARASOL_TEST_DEF = PokemonToolCardDef(
    passive=trainers.BigParasolPassive(),
    guid="40000000-0000-0000-0000-0000000000e3",
    key="TST", name="com.test.trainer.BigParasolTest.Name",
    collector_number=910, set_code="TST", rarity=0,
)


class TestBigParasol(TrainerDeckTestBase):
    def _attach(self, area_name):
        holder = self.add_to(area_name, make_card(BASIC_DEF), P2)
        tool = self.add_to("discard", make_card(BIG_PARASOL_TEST_DEF), P2)
        self.board.attach_card(tool.entity_id, holder.entity_id)
        return holder

    def test_shields_whole_side_while_holder_is_active(self):
        holder = self._attach("activePokemonArea")
        bench_mate = self.add_to("bench", make_card(BASIC_DEF), P2)
        attacker = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P1)
        atk = Attack("Zap", cost={}, damage=0)
        ctx = EffectContext(self.session, P1, attacker, atk)
        self.assertTrue(ctx.effects_blocked(holder))
        self.assertTrue(ctx.effects_blocked(bench_mate))

    def test_no_shield_when_holder_is_benched(self):
        holder = self._attach("bench")
        attacker = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P1)
        atk = Attack("Zap", cost={}, damage=0)
        ctx = EffectContext(self.session, P1, attacker, atk)
        self.assertFalse(ctx.effects_blocked(holder))

    def test_does_not_block_damage(self):
        holder = self._attach("activePokemonArea")
        attacker = self.add_to("bench", make_card(PLAIN_MON_DEF), P1)
        self.assertFalse(compute_damage(self.board, attacker, holder, 30).prevented)


# ----------------------------------------------------------------------
# 12. Path to the Peak
# ----------------------------------------------------------------------

PATH_TO_THE_PEAK_TEST_DEF = StadiumCardDef(
    passive=trainers.PathToThePeakPassive(),
    guid="40000000-0000-0000-0000-0000000000f1",
    key="TST", name="com.test.trainer.PathToThePeakTest.Name",
    collector_number=911, set_code="TST", rarity=0,
)


class TestPathToThePeak(TrainerDeckTestBase):
    def test_locks_rule_box_abilities_both_sides(self):
        v_pokemon = self.add_to("bench", make_card(V_POKEMON_DEF), P1)
        self.assertFalse(ability_locked(self.board, v_pokemon))
        stadium_area = self.board.find_global_area("activeStadium")
        entity = create_card_entity(make_card(PATH_TO_THE_PEAK_TEST_DEF), owning_player_id=P2)
        self.board.add_card_to_area(entity, stadium_area)
        self.assertTrue(ability_locked(self.board, v_pokemon))

    def test_leaves_non_rule_box_pokemon_alone(self):
        plain = self.add_to("bench", make_card(PLAIN_MON_DEF), P1)
        stadium_area = self.board.find_global_area("activeStadium")
        entity = create_card_entity(make_card(PATH_TO_THE_PEAK_TEST_DEF), owning_player_id=P2)
        self.board.add_card_to_area(entity, stadium_area)
        self.assertFalse(ability_locked(self.board, plain))


# ----------------------------------------------------------------------
# 13. Lost City
# ----------------------------------------------------------------------

class TestLostCity(unittest.TestCase):
    def test_reroutes_every_knockout_to_the_lost_zone(self):
        passive = trainers.LostCityPassive()
        self.assertEqual(passive.knockout_destination(object(), object()), "lostZone")


# ----------------------------------------------------------------------
# 14. Forest Seal Stone
# ----------------------------------------------------------------------

class TestForestSealStone(TrainerDeckTestBase):
    def test_script_wires_a_vstar_granted_ability(self):
        card = load_script("SWSH12", "ForestSealStone_156.py")
        self.assertEqual(len(card.granted_abilities), 1)
        ability = card.granted_abilities[0]
        self.assertEqual(ability.title, "Star Alchemy")
        self.assertTrue(ability.vstar)
        self.assertEqual(ability.activation, Activations.ONCE_PER_TURN)
        self.assertIs(ability.effect, trainers.star_alchemy)

    def test_condition_requires_a_pokemon_v_holder(self):
        card = load_script("SWSH12", "ForestSealStone_156.py")
        condition = card.granted_abilities[0].condition
        v_pokemon = self.add_to("bench", make_card(V_POKEMON_DEF), P1)
        plain = self.add_to("bench", make_card(PLAIN_MON_DEF), P1)
        self.assertTrue(condition(self.board, P1, v_pokemon))
        self.assertFalse(condition(self.board, P1, plain))

    async def test_star_alchemy_searches_without_revealing(self):
        found = self.add_to("deck", make_card(BASIC_DEF), P1)
        holder = self.add_to("bench", make_card(V_POKEMON_DEF), P1)
        self.session.chooser_replies = [[found.entity_id]]
        ctx = EffectContext(self.session, P1, holder, None)
        await trainers.star_alchemy(ctx)
        self.assertIn(found, self.board.find_player_area(P1, "hand").children)
        p2_intros = {m["value"]["entityID"] for m in ctx.messages_for(P2)
                     if m["name"] == "EntityIntroduced"}
        self.assertNotIn(found.entity_id, p2_intros)


# ----------------------------------------------------------------------
# 15. Stub reprints wired to already-shared effects
# ----------------------------------------------------------------------

class TestReprintWiring(unittest.TestCase):
    def test_bosss_orders_reprints(self):
        for set_code, filename in [
            ("SWSH2", "BosssOrders_154.py"), ("SWSH2", "BosssOrders_200.py"),
            ("SWSH45", "BosssOrders_58.py"), ("SWSH9", "BosssOrders_132.py"),
        ]:
            card = load_script(set_code, filename)
            self.assertIs(card.effect, trainers.bosss_orders)
            self.assertIs(card.condition, trainers.opponent_has_bench)

    def test_ultra_ball_reprint(self):
        card = load_script("SWSH9", "UltraBall_150.py")
        self.assertIs(card.effect, trainers.ultra_ball)
        self.assertTrue(card.condition(self.board_for_hand_size(3), P1))
        self.assertFalse(card.condition(self.board_for_hand_size(2), P1))

    def test_quick_ball_reprints(self):
        for set_code, filename in [
            ("SWSH1", "QuickBall_179.py"), ("SWSH8", "QuickBall_237.py"),
        ]:
            card = load_script(set_code, filename)
            self.assertIs(card.effect, trainers.quick_ball)
            self.assertTrue(card.condition(self.board_for_hand_size(2), P1))
            self.assertFalse(card.condition(self.board_for_hand_size(1), P1))

    def test_lost_vacuum_reprint(self):
        card = load_script("SWSH11", "LostVacuum_217.py")
        self.assertIs(card.effect, trainers.lost_vacuum)
        self.assertIs(card.condition, trainers.lost_vacuum_playable)

    def test_choice_belt_reprint(self):
        card = load_script("SWSH10", "ChoiceBelt_211.py")
        self.assertIsInstance(card.passive, ChoiceBeltPassive)

    def test_double_turbo_energy_reprint(self):
        card = load_script("SWSH10", "DoubleTurboEnergy_216.py")
        self.assertIsInstance(card.passive, DoubleTurboPassive)
        self.assertEqual(
            card.extra_attributes[str(AttrID.ENERGY_INFO.value)]["value"],
            '{"options": [[1, 1]]}',
        )

    @staticmethod
    def board_for_hand_size(count):
        board = BoardState("wiring-test", [P1, P2])
        hand = board.find_player_area(P1, "hand")
        for _ in range(count):
            entity = create_card_entity(make_card(BASIC_DEF), owning_player_id=P1)
            board.add_card_to_area(entity, hand)
        return board


if __name__ == "__main__":
    unittest.main()
