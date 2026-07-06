"""End-to-end unit tests for the staple-trainer sweep (Batch C): shared
implementations added to spirit/game/card_effects/trainers.py and their
script wiring across SWSH1/2/3/4/9/10/35/45/PGO."""

import importlib.util
import os
import unittest

from spirit.tests.test_phase1_engine import EngineTestBase, P1, P2, make_card

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects import trainers
from spirit.game.data_utils import (
    EnergyCardDef,
    ItemCardDef,
    PokemonCardDef,
    PokemonStage,
    SupporterCardDef,
)
from spirit.game.models.board import create_card_entity
from spirit.game.session.effects import EffectContext, resolve_trainer_effect

SCRIPTS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "game", "scripts", "cards"
)


def load_script(*parts):
    """Imports a card script module directly, bypassing the full loader."""
    path = os.path.join(SCRIPTS_DIR, *parts)
    spec = importlib.util.spec_from_file_location(
        "test_staple_script_" + "_".join(parts), path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.card


# ----------------------------------------------------------------------
# Local test fixtures (guids under a private 50000000 prefix, unused
# elsewhere in the suite)
# ----------------------------------------------------------------------

BASIC_DEF = PokemonCardDef(
    guid="50000000-0000-0000-0000-0000000000a1",
    key="TST", name="com.test.pokemon.Basic.Name",
    collector_number=901, set_code="TST", rarity=1,
    hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC,
)
DARKNESS_BASIC_DEF = PokemonCardDef(
    guid="50000000-0000-0000-0000-0000000000a2",
    key="TST", name="com.test.pokemon.DarknessBasic.Name",
    collector_number=902, set_code="TST", rarity=1,
    hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC,
)
VMAX_DEF = PokemonCardDef(
    guid="50000000-0000-0000-0000-0000000000a3",
    key="TST", name="com.test.pokemon.VMax.Name",
    collector_number=903, set_code="TST", rarity=1,
    hp=320, elements=[PokemonTypes.COLORLESS], subtypes=["VMAX"],
)
PLAIN_MON_DEF = PokemonCardDef(
    guid="50000000-0000-0000-0000-0000000000a4",
    key="TST", name="com.test.pokemon.Plain.Name",
    collector_number=904, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS],
)

SUPPORTER_FILLER_DEF = SupporterCardDef(
    guid="50000000-0000-0000-0000-0000000000c1",
    key="TST", name="com.test.trainer.SupporterFiller.Name",
    collector_number=920, set_code="TST", rarity=1,
)
ITEM_FILLER_DEF = ItemCardDef(
    guid="50000000-0000-0000-0000-0000000000c2",
    key="TST", name="com.test.trainer.ItemFiller.Name",
    collector_number=921, set_code="TST", rarity=1,
)

BASIC_ENERGY_DEF = EnergyCardDef(
    guid="50000000-0000-0000-0000-0000000000e1",
    key="TST", name="com.test.energy.Basic.Name",
    collector_number=930, set_code="TST", rarity=0,
    energy_type=PokemonTypes.COLORLESS,
)
METAL_ENERGY_DEF = EnergyCardDef(
    guid="50000000-0000-0000-0000-0000000000e2",
    key="TST", name="com.test.energy.Metal.Name",
    collector_number=931, set_code="TST", rarity=0,
    energy_type=PokemonTypes.METAL,
)
GRASS_ENERGY_DEF = EnergyCardDef(
    guid="50000000-0000-0000-0000-0000000000e3",
    key="TST", name="com.test.energy.Grass.Name",
    collector_number=932, set_code="TST", rarity=0,
    energy_type=PokemonTypes.GRASS,
)
SPECIAL_ENERGY_DEF = EnergyCardDef(
    guid="50000000-0000-0000-0000-0000000000e4",
    key="TST", name="com.test.energy.Special.Name",
    collector_number=933, set_code="TST", rarity=0,
    energy_type=PokemonTypes.WATER, is_special=True,
)


class TrainerDeckTestBase(EngineTestBase):
    async def play_trainer(self, card_def, player_id=P1):
        """Runs a trainer's registered effect through the trainer-slot flow,
        mirroring GameSession._execute_play_trainer's board state."""
        card = self.add_to("discard", make_card(card_def), player_id)
        trainer_area = self.board.find_global_area("activeTrainer")
        self.board.move_card(card.entity_id, trainer_area.entity_id)
        card.owning_player_id = player_id
        return await resolve_trainer_effect(self.session, player_id, card)

    def played_source(self, card_def, player_id=P1):
        """A trainer source sitting in activeTrainer (already off the hand),
        matching the real placement-before-effect flow -- for tests where the
        card's own hand-count would otherwise pollute a draw/discard assert."""
        entity = create_card_entity(make_card(card_def), owning_player_id=player_id)
        trainer_area = self.board.find_global_area("activeTrainer")
        self.board.add_card_to_area(entity, trainer_area)
        return entity


# ----------------------------------------------------------------------
# 1. Piers
# ----------------------------------------------------------------------

class TestPiers(TrainerDeckTestBase):
    async def test_finds_an_energy_and_a_darkness_pokemon(self):
        energy = self.add_to("deck", make_card(BASIC_ENERGY_DEF), P1)
        darkness = self.add_to("deck", make_card(DARKNESS_BASIC_DEF), P1)
        self.add_to("deck", make_card(PLAIN_MON_DEF), P1)  # not selectable
        source = self.add_to("hand", make_card(ITEM_FILLER_DEF), P1)
        self.session.chooser_replies = [[energy.entity_id], [darkness.entity_id]]
        await trainers.piers(EffectContext(self.session, P1, source, None))
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(energy, hand.children)
        self.assertIn(darkness, hand.children)


# ----------------------------------------------------------------------
# 2. Professor's Research (+ Professor Magnolia reprint)
# ----------------------------------------------------------------------

class TestProfessorsResearch(TrainerDeckTestBase):
    async def test_discards_hand_and_draws_7(self):
        for _ in range(3):
            self.add_to("hand", make_card(BASIC_DEF), P1)
        for _ in range(7):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        await trainers.professors_research(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 7)
        self.assertEqual(len(self.board.find_player_area(P1, "discard").children), 4)

    def test_reprints_wired(self):
        for set_code, filename in [
            ("PGO", "ProfessorsResearch_78.py"), ("PGO", "ProfessorsResearch_84.py"),
            ("SWSH45", "ProfessorsResearch_60.py"), ("SWSH9", "ProfessorsResearch_147.py"),
            ("SWSH1", "ProfessorsResearchProfessorMagnolia_178.py"),
            ("SWSH1", "ProfessorsResearchProfessorMagnolia_201.py"),
            ("SWSH1", "ProfessorsResearchProfessorMagnolia_209.py"),
            ("SWSH35", "ProfessorsResearchProfessorMagnolia_62.py"),
        ]:
            card = load_script(set_code, filename)
            self.assertIs(card.effect, trainers.professors_research)


# ----------------------------------------------------------------------
# 3. Bede
# ----------------------------------------------------------------------

class TestBede(TrainerDeckTestBase):
    def test_condition_requires_bench_and_basic_energy(self):
        self.assertFalse(trainers.bede_playable(self.board, P1))
        self.add_to("bench", make_card(BASIC_DEF), P1)
        self.assertFalse(trainers.bede_playable(self.board, P1))
        self.add_to("hand", make_card(BASIC_ENERGY_DEF), P1)
        self.assertTrue(trainers.bede_playable(self.board, P1))

    def test_special_energy_does_not_satisfy_condition(self):
        self.add_to("bench", make_card(BASIC_DEF), P1)
        self.add_to("hand", make_card(SPECIAL_ENERGY_DEF), P1)
        self.assertFalse(trainers.bede_playable(self.board, P1))

    async def test_attaches_chosen_basic_energy_to_chosen_bench_pokemon(self):
        bench = self.add_to("bench", make_card(BASIC_DEF), P1)
        energy = self.add_to("hand", make_card(BASIC_ENERGY_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [[energy.entity_id], [bench.entity_id]]
        await trainers.bede(EffectContext(self.session, P1, source, None))
        self.assertIn(energy, bench.children)


# ----------------------------------------------------------------------
# 4. Team Yell Grunt
# ----------------------------------------------------------------------

class TestTeamYellGrunt(TrainerDeckTestBase):
    def test_condition_requires_opponent_energy_attached(self):
        pokemon = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P2)
        self.assertFalse(trainers.opponent_has_energy_attached(self.board, P1))
        energy = self.add_to("discard", make_card(BASIC_ENERGY_DEF), P2)
        self.board.attach_card(energy.entity_id, pokemon.entity_id)
        self.assertTrue(trainers.opponent_has_energy_attached(self.board, P1))

    async def test_returns_opponent_energy_to_their_hand(self):
        pokemon = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P2)
        energy = self.add_to("discard", make_card(BASIC_ENERGY_DEF), P2)
        self.board.attach_card(energy.entity_id, pokemon.entity_id)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [[energy.entity_id]]
        await trainers.team_yell_grunt(EffectContext(self.session, P1, source, None))
        self.assertIn(energy, self.board.find_player_area(P2, "hand").children)


# ----------------------------------------------------------------------
# 5. Milo
# ----------------------------------------------------------------------

class TestMilo(TrainerDeckTestBase):
    async def test_draws_2_per_card_discarded(self):
        for _ in range(2):
            self.add_to("hand", make_card(BASIC_DEF), P1)
        for _ in range(4):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.played_source(SUPPORTER_FILLER_DEF)
        hand_cards = self.board.find_player_area(P1, "hand").children
        discard_ids = [c.entity_id for c in hand_cards][:2]
        self.session.chooser_replies = [discard_ids]
        await trainers.milo(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 4)

    async def test_no_discard_means_no_draw(self):
        source = self.played_source(SUPPORTER_FILLER_DEF)
        self.session.chooser_replies = [[]]
        await trainers.milo(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 0)


# ----------------------------------------------------------------------
# 6. Sonia
# ----------------------------------------------------------------------

class TestSonia(TrainerDeckTestBase):
    async def test_can_search_up_to_2_basic_pokemon(self):
        basics = [self.add_to("deck", make_card(BASIC_DEF), P1) for _ in range(2)]
        self.add_to("deck", make_card(BASIC_ENERGY_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.choice_replies = [0]  # choose "Basic Pokemon"
        self.session.chooser_replies = [[c.entity_id for c in basics]]
        await trainers.sonia(EffectContext(self.session, P1, source, None))
        hand = self.board.find_player_area(P1, "hand")
        for card in basics:
            self.assertIn(card, hand.children)

    async def test_can_search_up_to_2_basic_energy_instead(self):
        energies = [self.add_to("deck", make_card(BASIC_ENERGY_DEF), P1) for _ in range(2)]
        self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.choice_replies = [1]  # choose "basic Energy cards"
        self.session.chooser_replies = [[c.entity_id for c in energies]]
        await trainers.sonia(EffectContext(self.session, P1, source, None))
        hand = self.board.find_player_area(P1, "hand")
        for card in energies:
            self.assertIn(card, hand.children)


# ----------------------------------------------------------------------
# 7. Kabu
# ----------------------------------------------------------------------

class TestKabu(TrainerDeckTestBase):
    async def test_draws_4_with_a_benched_pokemon(self):
        self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P1)
        self.add_to("bench", make_card(BASIC_DEF), P1)
        for _ in range(2):
            self.add_to("hand", make_card(BASIC_DEF), P1)
        for _ in range(10):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        await trainers.kabu(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 4)

    async def test_draws_8_when_active_is_only_pokemon(self):
        self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P1)
        for _ in range(2):
            self.add_to("hand", make_card(BASIC_DEF), P1)
        for _ in range(10):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        await trainers.kabu(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 8)


# ----------------------------------------------------------------------
# 8. Rose
# ----------------------------------------------------------------------

class TestRose(TrainerDeckTestBase):
    def test_condition_requires_a_vmax_in_play(self):
        self.assertFalse(trainers.has_vmax_in_play(self.board, P1))
        self.add_to("activePokemonArea", make_card(VMAX_DEF), P1)
        self.assertTrue(trainers.has_vmax_in_play(self.board, P1))

    async def test_attaches_energy_and_discards_hand_when_any_attached(self):
        vmax = self.add_to("activePokemonArea", make_card(VMAX_DEF), P1)
        energies = [self.add_to("discard", make_card(BASIC_ENERGY_DEF), P1) for _ in range(2)]
        hand_card = self.add_to("hand", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [
            [vmax.entity_id], [c.entity_id for c in energies]
        ]
        await trainers.rose(EffectContext(self.session, P1, source, None))
        for energy in energies:
            self.assertIn(energy, vmax.children)
        self.assertIn(hand_card, self.board.find_player_area(P1, "discard").children)

    async def test_no_energy_attached_keeps_hand(self):
        vmax = self.add_to("activePokemonArea", make_card(VMAX_DEF), P1)
        hand_card = self.add_to("hand", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [[vmax.entity_id], []]
        await trainers.rose(EffectContext(self.session, P1, source, None))
        self.assertIn(hand_card, self.board.find_player_area(P1, "hand").children)


# ----------------------------------------------------------------------
# 9. Hop
# ----------------------------------------------------------------------

class TestHop(TrainerDeckTestBase):
    async def test_draws_3(self):
        for _ in range(3):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.played_source(SUPPORTER_FILLER_DEF)
        await trainers.hop(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 3)


# ----------------------------------------------------------------------
# 10. Marnie reprint wiring (shared impl already tested elsewhere)
# ----------------------------------------------------------------------

class TestMarnieReprints(unittest.TestCase):
    def test_reprints_wired_to_shared_marnie(self):
        for set_code, filename in [
            ("SWSH1", "Marnie_169.py"), ("SWSH1", "Marnie_200.py"),
            ("SWSH1", "Marnie_208.py"), ("SWSH35", "Marnie_56.py"),
        ]:
            card = load_script(set_code, filename)
            self.assertIs(card.effect, trainers.marnie)


# ----------------------------------------------------------------------
# 11. Adaman
# ----------------------------------------------------------------------

class TestAdaman(TrainerDeckTestBase):
    def test_condition_requires_2_metal_energy_in_hand(self):
        self.assertFalse(trainers.has_two_metal_energy_in_hand(self.board, P1))
        self.add_to("hand", make_card(METAL_ENERGY_DEF), P1)
        self.assertFalse(trainers.has_two_metal_energy_in_hand(self.board, P1))
        self.add_to("hand", make_card(METAL_ENERGY_DEF), P1)
        self.assertTrue(trainers.has_two_metal_energy_in_hand(self.board, P1))

    async def test_discards_2_metal_energy_then_searches_without_reveal(self):
        metals = [self.add_to("hand", make_card(METAL_ENERGY_DEF), P1) for _ in range(2)]
        found = self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [
            [c.entity_id for c in metals], [found.entity_id]
        ]
        ctx = EffectContext(self.session, P1, source, None)
        await trainers.adaman(ctx)
        for metal in metals:
            self.assertIn(metal, self.board.find_player_area(P1, "discard").children)
        self.assertIn(found, self.board.find_player_area(P1, "hand").children)
        p2_intros = {m["value"]["entityID"] for m in ctx.messages_for(P2)
                     if m["name"] == "EntityIntroduced"}
        self.assertNotIn(found.entity_id, p2_intros)

    async def test_insufficient_metal_energy_cancels_search(self):
        metal = self.add_to("hand", make_card(METAL_ENERGY_DEF), P1)
        self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [[metal.entity_id]]
        await trainers.adaman(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.session.chooser_calls), 1)  # only the discard pick


# ----------------------------------------------------------------------
# 12. Gardenia's Vigor
# ----------------------------------------------------------------------

class TestGardeniasVigor(TrainerDeckTestBase):
    async def test_draws_2_then_attaches_up_to_2_grass_energy(self):
        for _ in range(2):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        bench = self.add_to("bench", make_card(BASIC_DEF), P1)
        grass = [self.add_to("hand", make_card(GRASS_ENERGY_DEF), P1) for _ in range(2)]
        source = self.played_source(SUPPORTER_FILLER_DEF)
        self.session.chooser_replies = [
            [bench.entity_id], [c.entity_id for c in grass]
        ]
        await trainers.gardenias_vigor(EffectContext(self.session, P1, source, None))
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 2)
        for energy in grass:
            self.assertIn(energy, bench.children)

    async def test_no_draws_available_skips_attach_entirely(self):
        bench = self.add_to("bench", make_card(BASIC_DEF), P1)
        grass = self.add_to("hand", make_card(GRASS_ENERGY_DEF), P1)
        source = self.played_source(SUPPORTER_FILLER_DEF)
        await trainers.gardenias_vigor(EffectContext(self.session, P1, source, None))
        self.assertNotIn(grass, bench.children)
        self.assertEqual(self.session.chooser_calls, [])


# ----------------------------------------------------------------------
# 13. Kamado
# ----------------------------------------------------------------------

class TestKamado(TrainerDeckTestBase):
    def test_condition_requires_another_card_in_hand(self):
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        board = self.board_for_hand_size(1)
        self.assertFalse(trainers.hand_size_at_least(2)(board, P1))
        self.add_to("hand", make_card(BASIC_DEF), P1)
        self.assertTrue(trainers.hand_size_at_least(2)(self.board, P1))

    async def test_keeps_chosen_card_discards_rest_draws_4(self):
        keep = self.add_to("hand", make_card(BASIC_DEF), P1)
        discard_these = [self.add_to("hand", make_card(BASIC_DEF), P1) for _ in range(2)]
        for _ in range(4):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [[keep.entity_id]]
        await trainers.kamado(EffectContext(self.session, P1, source, None))
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(keep, hand.children)
        for card in discard_these:
            self.assertIn(card, self.board.find_player_area(P1, "discard").children)
        self.assertEqual(len(hand.children), 5)  # kept + 4 drawn

    @staticmethod
    def board_for_hand_size(count):
        from spirit.game.models.board import BoardState, create_card_entity
        board = BoardState("wiring-test", [P1, P2])
        hand = board.find_player_area(P1, "hand")
        for _ in range(count):
            entity = create_card_entity(make_card(BASIC_DEF), owning_player_id=P1)
            board.add_card_to_area(entity, hand)
        return board


# ----------------------------------------------------------------------
# 14. Zisu
# ----------------------------------------------------------------------

class TestZisu(TrainerDeckTestBase):
    async def test_draws_until_1_more_than_opponent(self):
        for _ in range(2):
            self.add_to("hand", make_card(BASIC_DEF), P2)
        for _ in range(5):
            self.add_to("deck", make_card(BASIC_DEF), P1)
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        await trainers.zisu(EffectContext(self.session, P1, source, None))
        # 1 (source already removed via play_trainer path not used here, but
        # ctx.hand() only sees what's actually in the hand area) + drawn to 3.
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children),
                          self.session.board_state.find_player_area(P2, "hand").children.__len__() + 1)


# ----------------------------------------------------------------------
# 15. Pokemon Center Lady (unblocked by ctx.cure_all_conditions)
# ----------------------------------------------------------------------

class TestPokemonCenterLady(TrainerDeckTestBase):
    async def test_heals_60_and_cures_all_conditions(self):
        pokemon = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P1)
        pokemon.set_attribute(AttrID.HP, 20)
        pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned", "Asleep"])
        self.session.sleep_checkup_coins[pokemon.entity_id] = 1
        self.session.poison_counters[pokemon.entity_id] = 2
        source = self.add_to("hand", make_card(SUPPORTER_FILLER_DEF), P1)
        self.session.chooser_replies = [[pokemon.entity_id]]
        await trainers.pokemon_center_lady(EffectContext(self.session, P1, source, None))
        self.assertEqual(pokemon.get_attribute(AttrID.HP), 80)
        self.assertEqual(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(pokemon.entity_id, self.session.sleep_checkup_coins)
        self.assertNotIn(pokemon.entity_id, self.session.poison_counters)

    async def test_condition_requires_damage_or_conditions(self):
        pokemon = self.add_to("activePokemonArea", make_card(PLAIN_MON_DEF), P1)
        self.assertFalse(trainers.center_lady_playable(self.board, P1))
        pokemon.set_attribute(AttrID.HP, 90)
        self.assertTrue(trainers.center_lady_playable(self.board, P1))

    def test_reprints_wired(self):
        for set_code, filename in [
            ("SWSH1", "PokmonCenterLady_176.py"),
            ("SWSH35", "PokmonCenterLady_60.py"),
            ("SWSH4", "PokmonCenterLady_185.py"),
        ]:
            card = load_script(set_code, filename)
            self.assertIs(card.effect, trainers.pokemon_center_lady)
            self.assertIs(card.condition, trainers.center_lady_playable)


# ----------------------------------------------------------------------
# 16. Deferred cards: still effect=unimplemented (missing primitives)
# ----------------------------------------------------------------------

class TestDeferredCards(unittest.TestCase):

    def test_grant_reprints_stay_unimplemented(self):
        from spirit.game.data_utils import unimplemented
        for set_code, filename in [
            ("SWSH10", "Grant_144.py"), ("SWSH10", "Grant_185.py"),
            ("SWSH10", "Grant_203.py"),
        ]:
            card = load_script(set_code, filename)
            self.assertIs(card.effect, unimplemented)

    def test_choy_reprints_stay_unimplemented(self):
        from spirit.game.data_utils import unimplemented
        for set_code, filename in [
            ("SWSH10", "Choy_137.py"), ("SWSH10", "Choy_182.py"),
            ("SWSH10", "Choy_200.py"),
        ]:
            card = load_script(set_code, filename)
            self.assertIs(card.effect, unimplemented)


if __name__ == "__main__":
    unittest.main()
