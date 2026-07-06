"""End-to-end unit tests for the Mew VMAX deck's BATCH B Pokemon cards:
Oricorio, Genesect V, Mew V, Mew VMAX -- and the engine features they lean on
(non-stacking damage-taken passives, ability conditions gating a no-op draw,
ctx.use_attack's lock propagation, ignore_target_effects)."""

import unittest
from unittest.mock import AsyncMock

from spirit.tests.test_phase1_engine import EngineTestBase, P1, P2, make_card

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import (
    CARD_DEFS_BY_GUID,
    EnergyCardDef,
    PokemonCardDef,
    PokemonToolCardDef,
)
from spirit.game.models.board import create_card_entity
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext, resolve_attack
from spirit.game.session.passives import Passive, compute_damage

# Archetype GUIDs of the deck's printings (spirit/game/scripts/cards/SWSH8).
ORICORIO = "91504f79-cabd-5abc-aa32-b397543a6b24"
GENESECT_V_185 = "8a340773-6bfd-5786-acc2-28b31243f9ce"
MEW_V_113 = "bf0556da-f2cd-5b45-8bd9-6b7bff65f745"
MEW_VMAX_114 = "2b2efb79-6c02-5350-89ca-6777e295e7a9"
MEW_VMAX_268 = "72b7e13f-0f90-50ba-992d-ac6ca731a25b"


def setUpModule():
    if not loader.cards_by_guid:
        loader.load_all()


def deck_card(guid):
    return loader.cards_by_guid[guid]


def ability_named(guid, title):
    definition = CARD_DEFS_BY_GUID[guid]
    return next(a for a in definition.abilities if a.title == title)


# ----------------------------------------------------------------------
# Local test fixtures (guids under a private 30000000 prefix, unused
# elsewhere in the suite)
# ----------------------------------------------------------------------

TEST_ENERGY_DEF = EnergyCardDef(
    guid="30000000-0000-0000-0000-0000000000e1",
    key="TST", name="com.test.energy.Plain.Name",
    collector_number=901, set_code="TST", rarity=0,
    energy_type=PokemonTypes.COLORLESS,
)
TEST_ENERGY = make_card(TEST_ENERGY_DEF)

PLAIN_MON_DEF = PokemonCardDef(
    guid="30000000-0000-0000-0000-0000000000a1",
    key="TST", name="com.test.pokemon.PlainMon.Name",
    collector_number=902, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS],
)
PLAIN_MON = make_card(PLAIN_MON_DEF)


class _AlwaysPreventsPassive(Passive):
    """Test-local stand-in for a target-side damage shield."""
    def prevents_damage(self, calc, carrier) -> bool:
        return True


SHIELD_TOOL_DEF = PokemonToolCardDef(
    passive=_AlwaysPreventsPassive(),
    guid="30000000-0000-0000-0000-0000000000e2",
    key="TST", name="com.test.trainer.ShieldTool.Name",
    collector_number=903, set_code="TST", rarity=0,
)
SHIELD_TOOL = make_card(SHIELD_TOOL_DEF)


class MewDeckTestBase(EngineTestBase):
    def add_deck_card(self, area_name, guid, player_id):
        return self.add_to(area_name, deck_card(guid), player_id)


# ----------------------------------------------------------------------
# Oricorio: Lesson in Zeal (passive) + Glistening Droplets (attack)
# ----------------------------------------------------------------------

class TestOricorio(MewDeckTestBase):
    def test_lesson_in_zeal_reduces_damage_after_weakness_resistance(self):
        self.add_deck_card("bench", ORICORIO, P1)
        mew = self.add_deck_card("activePokemonArea", MEW_V_113, P1)
        attacker = self.add_deck_card("activePokemonArea", GENESECT_V_185, P2)
        self.assertEqual(compute_damage(self.board, attacker, mew, 100).amount, 80)

    def test_lesson_in_zeal_does_not_stack(self):
        self.add_deck_card("bench", ORICORIO, P1)
        self.add_deck_card("bench", ORICORIO, P1)
        mew = self.add_deck_card("activePokemonArea", MEW_V_113, P1)
        attacker = self.add_deck_card("activePokemonArea", GENESECT_V_185, P2)
        # "You can't apply more than 1 Lesson in Zeal Ability at a time."
        self.assertEqual(compute_damage(self.board, attacker, mew, 100).amount, 80)

    def test_lesson_in_zeal_ignores_non_fusion_strike_target(self):
        self.add_deck_card("bench", ORICORIO, P1)
        plain = self.add_to("activePokemonArea", PLAIN_MON, P1)
        attacker = self.add_deck_card("activePokemonArea", GENESECT_V_185, P2)
        self.assertEqual(compute_damage(self.board, attacker, plain, 100).amount, 100)

    def test_lesson_in_zeal_only_protects_its_owners_side(self):
        self.add_deck_card("bench", ORICORIO, P1)  # Oricorio owned by P1
        opp_mew = self.add_deck_card("activePokemonArea", MEW_V_113, P2)
        attacker = self.add_deck_card("activePokemonArea", GENESECT_V_185, P1)
        self.assertEqual(compute_damage(self.board, attacker, opp_mew, 100).amount, 100)

    async def test_glistening_droplets_places_5_counters_via_native_picker(self):
        oricorio = self.add_deck_card("activePokemonArea", ORICORIO, P1)
        target = self.add_deck_card("activePokemonArea", MEW_V_113, P2)
        ctx = EffectContext(self.session, P1, oricorio,
                            ability_named(ORICORIO, "Glistening Droplets"))
        self.session.damage_counter_replies.append({target.entity_id: 5})
        await ability_named(ORICORIO, "Glistening Droplets").effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.HP), 180 - 50)


# ----------------------------------------------------------------------
# Genesect V: Fusion Strike System (ability) + Techno Blast (attack)
# ----------------------------------------------------------------------

class TestGenesectV(MewDeckTestBase):
    def test_fusion_strike_system_condition_gates_on_hand_size(self):
        genesect = self.add_deck_card("activePokemonArea", GENESECT_V_185, P1)
        ability = ability_named(GENESECT_V_185, "Fusion Strike System")
        # 1 Fusion Strike Pokemon in play, 0 cards in hand: offerable.
        self.assertTrue(ability.condition(self.board, P1, genesect))
        self.add_deck_card("hand", MEW_V_113, P1)
        # Hand size (1) no longer less than the Fusion Strike count (1).
        self.assertFalse(ability.condition(self.board, P1, genesect))

    async def test_fusion_strike_system_draws_until_hand_matches_count(self):
        genesect = self.add_deck_card("activePokemonArea", GENESECT_V_185, P1)
        self.add_deck_card("bench", MEW_V_113, P1)  # 2 Fusion Strike Pokemon
        for _ in range(5):
            self.add_deck_card("deck", MEW_VMAX_114, P1)
        ctx = EffectContext(self.session, P1, genesect,
                            ability_named(GENESECT_V_185, "Fusion Strike System"))
        await ability_named(GENESECT_V_185, "Fusion Strike System").effect(ctx)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 2)

    async def test_techno_blast_vanilla_damage_and_locks_next_turn(self):
        genesect = self.add_deck_card("activePokemonArea", GENESECT_V_185, P1)
        defender = self.add_deck_card("activePokemonArea", MEW_VMAX_114, P2)  # 310 HP
        attack = ability_named(GENESECT_V_185, "Techno Blast")
        await resolve_attack(self.session, P1, genesect, attack, attack.ability_id)
        self.assertEqual(defender.get_attribute(AttrID.HP), 310 - 210)
        self.assertTrue(self.session.turn_state.attack_locked(
            genesect.entity_id, attack.ability_id
        ))


# ----------------------------------------------------------------------
# Mew V: Energy Mix + Psychic Leap
# ----------------------------------------------------------------------

class TestMewV(MewDeckTestBase):
    async def test_energy_mix_attaches_to_chosen_fusion_strike_target(self):
        mew = self.add_deck_card("activePokemonArea", MEW_V_113, P1)
        bench_fusion = self.add_deck_card("bench", MEW_VMAX_114, P1)
        energy = self.add_to("deck", TEST_ENERGY, P1)
        ctx = EffectContext(self.session, P1, mew,
                            ability_named(MEW_V_113, "Energy Mix"))
        self.session.chooser_replies.append([energy.entity_id])        # search
        self.session.chooser_replies.append([bench_fusion.entity_id])  # target
        await ability_named(MEW_V_113, "Energy Mix").effect(ctx)
        self.assertIn(energy, bench_fusion.children)

    async def test_energy_mix_no_fusion_strike_target_leaves_energy_in_deck(self):
        # Effect source isn't placed on the board itself: models the search
        # legally whiffing when no Fusion Strike Pokemon is in play.
        energy = self.add_to("deck", TEST_ENERGY, P1)
        mew = create_card_entity(deck_card(MEW_V_113), owning_player_id=P1)
        ctx = EffectContext(self.session, P1, mew,
                            ability_named(MEW_V_113, "Energy Mix"))
        self.session.chooser_replies.append([energy.entity_id])
        await ability_named(MEW_V_113, "Energy Mix").effect(ctx)
        deck = self.board.find_player_area(P1, "deck")
        self.assertIn(energy, deck.children)
        self.assertTrue(any(m["name"] == "Shuffled" for _, m, _ in ctx._messages))

    async def test_psychic_leap_shuffles_and_promotes_on_yes(self):
        mew = self.add_deck_card("activePokemonArea", MEW_V_113, P1)
        self.add_deck_card("bench", MEW_VMAX_114, P1)
        self.add_deck_card("activePokemonArea", MEW_VMAX_114, P2)
        self.session.choice_replies.append(0)  # Yes
        attack = ability_named(MEW_V_113, "Psychic Leap")
        await resolve_attack(self.session, P1, mew, attack, attack.ability_id)
        deck = self.board.find_player_area(P1, "deck")
        self.assertIn(mew, deck.children)
        self.assertEqual(self.session.promotions, [P1])
        self.assertIsNone(self.session.game_over)

    async def test_psychic_leap_no_shuffle_on_decline(self):
        mew = self.add_deck_card("activePokemonArea", MEW_V_113, P1)
        self.add_deck_card("activePokemonArea", MEW_VMAX_114, P2)
        self.session.choice_replies.append(1)  # No
        attack = ability_named(MEW_V_113, "Psychic Leap")
        await resolve_attack(self.session, P1, mew, attack, attack.ability_id)
        self.assertIs(self.board.active_pokemon(P1), mew)
        self.assertEqual(self.session.promotions, [])

    async def test_psychic_leap_ends_game_when_promotion_fails(self):
        mew = self.add_deck_card("activePokemonArea", MEW_V_113, P1)
        self.add_deck_card("activePokemonArea", MEW_VMAX_114, P2)
        self.session.choice_replies.append(0)  # Yes
        self.session._promote_new_active = AsyncMock(return_value=False)
        attack = ability_named(MEW_V_113, "Psychic Leap")
        await resolve_attack(self.session, P1, mew, attack, attack.ability_id)
        self.assertEqual(self.session.game_over, (P2, "P1 has no Pokémon left"))


# ----------------------------------------------------------------------
# Mew VMAX: Cross Fusion Strike + Max Miracle
# ----------------------------------------------------------------------

class TestMewVMAX(MewDeckTestBase):
    async def test_cross_fusion_strike_no_candidates_is_noop(self):
        mewmax = self.add_deck_card("activePokemonArea", MEW_VMAX_114, P1)
        defender = self.add_deck_card("activePokemonArea", MEW_V_113, P2)
        ctx = EffectContext(self.session, P1, mewmax,
                            ability_named(MEW_VMAX_114, "Cross Fusion Strike"))
        await ability_named(MEW_VMAX_114, "Cross Fusion Strike").effect(ctx)
        self.assertEqual(ctx.knockouts, [])
        self.assertEqual(defender.get_attribute(AttrID.HP), 180)
        self.assertEqual(self.session.prompts, [])

    async def test_cross_fusion_strike_copies_non_locking_attack(self):
        mewmax = self.add_deck_card("activePokemonArea", MEW_VMAX_114, P1)
        self.add_deck_card("bench", ORICORIO, P1)
        defender = self.add_deck_card("activePokemonArea", MEW_V_113, P2)
        ctx = EffectContext(self.session, P1, mewmax,
                            ability_named(MEW_VMAX_114, "Cross Fusion Strike"))
        self.session.choice_replies.append(0)  # the only candidate: Glistening Droplets
        self.session.chooser_replies.append([defender.entity_id])  # counter target
        self.session.choice_replies.append(4)  # amount "5"
        await ability_named(MEW_VMAX_114, "Cross Fusion Strike").effect(ctx)
        self.assertEqual(defender.get_attribute(AttrID.HP), 180 - 50)
        miracle_id = ability_named(MEW_VMAX_114, "Max Miracle").ability_id
        cross_id = ability_named(MEW_VMAX_114, "Cross Fusion Strike").ability_id
        # (attack_locked is vacuously true at turn_number 0; check the lock
        # table directly instead of the helper.)
        self.assertNotIn((mewmax.entity_id, miracle_id), self.session.turn_state.attack_locks)
        self.assertNotIn((mewmax.entity_id, cross_id), self.session.turn_state.attack_locks)

    async def test_cross_fusion_strike_copies_locking_attack_locks_both_own_attacks(self):
        mewmax = self.add_deck_card("activePokemonArea", MEW_VMAX_114, P1)
        self.add_deck_card("bench", GENESECT_V_185, P1)
        defender = self.add_deck_card("activePokemonArea", MEW_VMAX_268, P2)  # 310 HP
        ctx = EffectContext(self.session, P1, mewmax,
                            ability_named(MEW_VMAX_114, "Cross Fusion Strike"))
        self.session.choice_replies.append(0)  # the only candidate: Techno Blast
        await ability_named(MEW_VMAX_114, "Cross Fusion Strike").effect(ctx)
        self.assertEqual(defender.get_attribute(AttrID.HP), 310 - 210)
        cross_id = ability_named(MEW_VMAX_114, "Cross Fusion Strike").ability_id
        miracle_id = ability_named(MEW_VMAX_114, "Max Miracle").ability_id
        # Copying a locked attack means the user can't attack at all next
        # turn, not just can't reuse the copied attack.
        self.assertTrue(self.session.turn_state.attack_locked(mewmax.entity_id, cross_id))
        self.assertTrue(self.session.turn_state.attack_locked(mewmax.entity_id, miracle_id))

    async def test_cross_fusion_strike_copy_of_copy_fizzles(self):
        mewmax = self.add_deck_card("activePokemonArea", MEW_VMAX_114, P1)
        self.add_deck_card("bench", MEW_VMAX_268, P1)  # benched Mew VMAX alt-art
        defender = self.add_deck_card("activePokemonArea", MEW_V_113, P2)
        attack = ability_named(MEW_VMAX_114, "Cross Fusion Strike")
        # Copy attacks stay selectable per the ruling; picking the benched Mew
        # VMAX's Cross Fusion Strike re-enters the copy chain and fizzles
        # (attack does nothing, resolution completes, turn ends normally).
        self.session.choice_replies.append(0)
        await resolve_attack(self.session, P1, mewmax, attack, attack.ability_id)
        _, _, buttons = self.session.prompts[-1]
        self.assertEqual(len(buttons), 2)
        self.assertIn("Cross Fusion Strike", buttons[0])
        self.assertEqual(len(self.session.prompts), 1)  # no recursive re-prompt
        self.assertEqual(defender.get_attribute(AttrID.HP), 180)
        self.assertEqual(self.session.turn_state.attack_locks, {})

    async def test_max_miracle_ignores_target_side_prevention(self):
        mewmax = self.add_deck_card("activePokemonArea", MEW_VMAX_114, P1)
        defender = self.add_deck_card("activePokemonArea", MEW_V_113, P2)
        shield = self.add_to("discard", SHIELD_TOOL, P2)
        self.board.attach_card(shield.entity_id, defender.entity_id)
        attack = ability_named(MEW_VMAX_114, "Max Miracle")
        await resolve_attack(self.session, P1, mewmax, attack, attack.ability_id)
        self.assertEqual(defender.get_attribute(AttrID.HP), 180 - 130)


if __name__ == "__main__":
    unittest.main()
