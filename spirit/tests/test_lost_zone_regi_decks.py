"""Tests for the Lost Zone Box and Regigigas deck card implementations."""

import unittest
import uuid

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes
from spirit.game.data_utils import EnergyCardDef, PokemonCardDef
from spirit.game.models.board import create_card_entity
from spirit.game.session.effects import EffectContext, resolve_attack
from spirit.game.session.game_session import GameSession
from spirit.game.session.legal_actions import (
    ACTION_USE_ABILITY, ACTION_USE_ATTACK, compute_legal_actions,
    effective_attack_cost, energy_provided_count,
)
from spirit.game.session.passives import effective_retreat_cost

from spirit.tests.test_effects import (
    EffectsTestBase, make_card, P1, P2, GAME_ID,
)

# Card definitions under test (importing runs their scripts / registers them).
from spirit.game.scripts.cards.SWSH11.Cramorant_50 import card as CRAMORANT
from spirit.game.scripts.cards.SWSH4.Zeraora_61 import card as ZERAORA
from spirit.game.scripts.cards.SWSH10.Regigigas_130 import card as REGIGIGAS
from spirit.game.scripts.cards.SWSH10.Registeel_108 import card as REGISTEEL
from spirit.game.scripts.cards.SWSH7.Regidrago_124 import card as REGIDRAGO_EVS
from spirit.game.scripts.cards.SWSH10.Regidrago_118 import card as REGIDRAGO_ASR
from spirit.game.scripts.cards.SWSH10.Regice_37 import card as REGICE
from spirit.game.scripts.cards.SWSH10.Regirock_75 import card as REGIROCK
from spirit.game.scripts.cards.SWSH11.Sableye_70 import card as SABLEYE
from spirit.game.scripts.cards.SWSH11.AerodactylVSTAR_93 import card as AERO_VSTAR
from spirit.game.scripts.cards.SWSH45.CrobatV_44 import card as CROBAT_V
from spirit.game.scripts.cards.SWSH1.AirBalloon_156 import card as AIR_BALLOON
from spirit.game.scripts.cards.SWSH2.TwinEnergy_174 import card as TWIN_ENERGY
from spirit.game.scripts.cards.SWSH11.DrapionV_118 import card as DRAPION_V
from spirit.game.scripts.cards.SWSH10.RadiantGreninja_46 import card as RADIANT_GRENINJA

from spirit.game.card_effects.trainers import (
    colresss_experiment, scoop_up_net, switch_cart, energy_recycler,
    trekking_shoes, mirage_gate, mirage_gate_condition,
)
from spirit.game.card_effects.energies import gift_energy_on_ko
from spirit.game.card_effects.pokemon import dark_asset


PSYCHIC_ENERGY_DEF = EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000e5",
    key="BW1", name="com.test.energy.Psychic", collector_number=200,
    set_code="BW1", rarity=0, energy_type=PokemonTypes.PSYCHIC,
)
WATER_ENERGY_DEF = EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000e6",
    key="BW1", name="com.test.energy.Water", collector_number=201,
    set_code="BW1", rarity=0, energy_type=PokemonTypes.WATER,
)
WEAK_TO_WATER_DEF = PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000f9",
    key="BW1", name="com.test.pokemon.WeakToWater.Name",
    collector_number=249, set_code="BW1", rarity=1,
    hp=200, elements=[PokemonTypes.COLORLESS],
    weakness_type=PokemonTypes.WATER,
)


_BASIC_COUNTER = [0]


def _basic(hp=120, elements=None, subtypes=None, retreat=1):
    _BASIC_COUNTER[0] += 1
    n = _BASIC_COUNTER[0]
    return PokemonCardDef(
        guid=f"00000000-0000-0000-0000-{n:012d}",
        key="BW1", name=f"com.test.pokemon.Mon{n}.Name",
        collector_number=n, set_code="BW1", rarity=1,
        hp=hp, elements=elements or [PokemonTypes.COLORLESS],
        stage=PokemonStage.BASIC, retreat_cost=retreat, subtypes=subtypes or ["Basic"],
    )


VMAX_DEF = _basic(hp=310, subtypes=["VMAX"])
FUSION_DEF = _basic(subtypes=["Basic", "Fusion Strike"])
PLAIN_BIG = _basic(hp=330)


class LostZoneRegiBase(EffectsTestBase):
    def attach(self, card, pokemon, player_id):
        entity = create_card_entity(card, owning_player_id=player_id)
        self.board.add_card_to_area(
            entity, self.board.find_player_area(player_id, "hand")
        )
        self.board.attach_card(entity.entity_id, pokemon.entity_id)
        return entity

    def fill_lost_zone(self, count, player_id=P1):
        for _ in range(count):
            self.add_to("lostZone", make_card(PLAIN_BIG), player_id)

    def make_source(self, card_def=None, player_id=P1):
        """A detached acting card (as a trainer sits on activeTrainer, not in
        the player's hand) so it never inflates hand/zone counts."""
        return create_card_entity(
            make_card(card_def or REGIROCK), owning_player_id=player_id
        )


class TestLostZonePassives(LostZoneRegiBase):
    async def test_lost_provisions_zeroes_cost_at_four(self):
        active = self.add_to("activePokemonArea", make_card(CRAMORANT), P1)
        cost = {"Water": 2, "Colorless": 1}
        self.fill_lost_zone(3)
        self.assertEqual(
            effective_attack_cost(self.board, active, dict(cost)), cost
        )
        self.add_to("lostZone", make_card(PLAIN_BIG), P1)  # -> 4
        self.assertEqual(effective_attack_cost(self.board, active, dict(cost)), {})

    async def test_air_balloon_reduces_retreat_cost(self):
        active = self.add_to("activePokemonArea", make_card(REGIROCK), P1)  # retreat 3
        self.assertEqual(effective_retreat_cost(self.board, active), 3)
        self.attach(make_card(AIR_BALLOON), active, P1)
        self.assertEqual(effective_retreat_cost(self.board, active), 1)


class TestAttackConditionGating(LostZoneRegiBase):
    def _lost_mine_offered(self, player_id=P1):
        self.session.turn_state.turn_number = 3
        entries = compute_legal_actions(
            self.board, self.session.turn_state, player_id, GAME_ID
        )
        lost_mine = SABLEYE.abilities[1]
        return any(
            e["selectableAction"]["description"] == ACTION_USE_ATTACK
            and e["selectableAction"]["actionID"] == lost_mine.ability_id
            for e in entries
        )

    async def test_lost_mine_gated_on_ten_lost_zone(self):
        active = self.add_to("activePokemonArea", make_card(SABLEYE), P1)
        self.attach(make_card(PSYCHIC_ENERGY_DEF), active, P1)
        self.add_to("bench", make_card(PLAIN_BIG), P1)  # a benched Pokemon exists
        self.assertFalse(self._lost_mine_offered())
        self.fill_lost_zone(10)
        self.assertTrue(self._lost_mine_offered())


class TestDragonsHoardGating(LostZoneRegiBase):
    def _hoard_offered(self, player_id=P1):
        entries = compute_legal_actions(
            self.board, self.session.turn_state, player_id, GAME_ID
        )
        hoard = REGIDRAGO_ASR.abilities[0]
        return any(
            e["selectableAction"]["description"] == ACTION_USE_ABILITY
            and e["selectableAction"]["actionID"] == hoard.ability_id
            for e in entries
        )

    async def test_hoard_gated_on_hand_below_four(self):
        self.add_to("activePokemonArea", make_card(REGIDRAGO_ASR), P1)
        # Empty hand -> would draw to 4, offered.
        self.assertTrue(self._hoard_offered())
        # Four cards in hand -> drawing to 4 does nothing, not offered.
        for _ in range(4):
            self.add_to("hand", make_card(PLAIN_BIG), P1)
        self.assertFalse(self._hoard_offered())

    async def test_hoard_not_offered_off_active(self):
        self.add_to("activePokemonArea", make_card(PLAIN_BIG), P1)
        self.add_to("bench", make_card(REGIDRAGO_ASR), P1)
        self.assertFalse(self._hoard_offered())


class TestConditionalDamage(LostZoneRegiBase):
    async def test_fighting_lightning_bonus_vs_v(self):
        attacker = self.add_to("activePokemonArea", make_card(ZERAORA), P1)
        defender = self.add_to("activePokemonArea", make_card(CROBAT_V), P2)  # 180 HP V
        attack = ZERAORA.abilities[0]
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        self.assertEqual(defender.get_attribute(AttrID.HP), 180 - 110)

    async def test_fighting_lightning_no_bonus_vs_basic(self):
        attacker = self.add_to("activePokemonArea", make_card(ZERAORA), P1)
        defender = self.add_to("activePokemonArea", make_card(PLAIN_BIG), P2)  # 330 HP
        attack = ZERAORA.abilities[0]
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        self.assertEqual(defender.get_attribute(AttrID.HP), 330 - 30)

    async def test_gigaton_break_bonus_vs_vmax(self):
        attacker = self.add_to("activePokemonArea", make_card(REGIGIGAS), P1)
        defender = self.add_to("activePokemonArea", make_card(VMAX_DEF), P2)  # 310 HP
        attack = REGIGIGAS.abilities[1]
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        self.assertEqual(defender.get_attribute(AttrID.HP), 310 - 300)

    async def test_heavy_slam_scales_with_retreat_cost(self):
        attacker = self.add_to("activePokemonArea", make_card(REGISTEEL), P1)
        defender = self.add_to("activePokemonArea", make_card(REGIGIGAS), P2)  # retreat 4
        attack = REGISTEEL.abilities[1]
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        # 220 - 50*4 = 20
        self.assertEqual(defender.get_attribute(AttrID.HP), 150 - 20)

    async def test_dragon_energy_scales_with_damage_counters(self):
        attacker = self.add_to("activePokemonArea", make_card(REGIDRAGO_EVS), P1)
        attacker.set_attribute(AttrID.HP, 130 - 30)  # 3 damage counters
        defender = self.add_to("activePokemonArea", make_card(PLAIN_BIG), P2)  # 330
        attack = REGIDRAGO_EVS.abilities[1]
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        # 240 - 20*3 = 180
        self.assertEqual(defender.get_attribute(AttrID.HP), 330 - 180)


class TestBlizzardBind(LostZoneRegiBase):
    async def test_locks_opponent_v_attacks_next_turn(self):
        self.session.turn_state.turn_number = 5
        attacker = self.add_to("activePokemonArea", make_card(REGICE), P1)
        defender = self.add_to("activePokemonArea", make_card(CROBAT_V), P2)
        attack = REGICE.abilities[1]
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        venomous = CROBAT_V.abilities[1].ability_id
        # Locked through the opponent's next turn (6), free again by turn 7.
        self.assertTrue(
            self.session.turn_state.attack_locked(defender.entity_id, venomous)
        )
        self.session.turn_state.turn_number = 7
        self.assertFalse(
            self.session.turn_state.attack_locked(defender.entity_id, venomous)
        )


class TestLostDive(LostZoneRegiBase):
    async def test_puts_top_three_in_lost_zone(self):
        attacker = self.add_to("activePokemonArea", make_card(AERO_VSTAR), P1)
        self.add_to("activePokemonArea", make_card(PLAIN_BIG), P2)
        for _ in range(5):
            self.add_to("deck", make_card(PLAIN_BIG), P1)
        attack = AERO_VSTAR.abilities[0]
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        self.assertEqual(len(self.board.find_player_area(P1, "lostZone").children), 3)
        self.assertEqual(len(self.board.find_player_area(P1, "deck").children), 2)


class TestAncientStar(LostZoneRegiBase):
    async def test_locks_opponent_v_abilities(self):
        from spirit.game.session.passives import ability_locked
        attacker = self.add_to("activePokemonArea", make_card(AERO_VSTAR), P1)
        opp_v = self.add_to("bench", make_card(CROBAT_V), P2)
        self.assertFalse(ability_locked(self.board, opp_v))
        ctx = EffectContext(self.session, P1, attacker, AERO_VSTAR.abilities[1])
        await __import__(
            "spirit.game.card_effects.pokemon", fromlist=["ancient_star"]
        ).ancient_star(ctx)
        self.assertTrue(ability_locked(self.board, opp_v))


class TestScoopUpNet(LostZoneRegiBase):
    async def test_returns_benched_pokemon_and_discards_attachments(self):
        self.add_to("activePokemonArea", make_card(REGIROCK), P1)
        benched = self.add_to("bench", make_card(SABLEYE), P1)
        self.attach(make_card(WATER_ENERGY_DEF), benched, P1)
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        self.session.chooser_replies.append([benched.entity_id])
        await scoop_up_net(ctx)
        await self.session.send_game_sequence_flush(ctx)
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(benched.entity_id, [c.entity_id for c in hand.children])
        self.assertEqual(len(self.board.find_player_area(P1, "bench").children), 0)
        self.assertEqual(len(self.board.find_player_area(P1, "discard").children), 1)

    async def test_damage_counters_cleared_when_returned_to_hand(self):
        self.add_to("activePokemonArea", make_card(REGIROCK), P1)
        benched = self.add_to("bench", make_card(SABLEYE), P1)
        printed_hp = benched.attribute_originals[AttrID.HP.value]
        benched.set_attribute(AttrID.HP, printed_hp - 30)  # 3 damage counters
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        self.session.chooser_replies.append([benched.entity_id])
        await scoop_up_net(ctx)
        await self.session.send_game_sequence_flush(ctx)
        # Back in hand as a fresh card: no damage survives.
        self.assertEqual(benched.get_attribute(AttrID.HP), printed_hp)


class TestSwitchCart(LostZoneRegiBase):
    async def test_switch_and_heal(self):
        active = self.add_to("activePokemonArea", make_card(SABLEYE), P1)  # basic
        active.set_attribute(AttrID.HP, 80 - 50)  # damaged
        benched = self.add_to("bench", make_card(REGIROCK), P1)
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        self.session.chooser_replies.append([benched.entity_id])
        await switch_cart(ctx)
        self.assertIs(self.board.active_pokemon(P1), benched)
        # Old active moved to bench, healed 30 (30 -> 60).
        self.assertEqual(active.get_attribute(AttrID.HP), 60)


class TestEnergyRecycler(LostZoneRegiBase):
    async def test_shuffles_basic_energy_into_deck(self):
        for _ in range(3):
            self.add_to("discard", make_card(WATER_ENERGY_DEF), P1)
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        # default chooser reply picks all available up to count
        await energy_recycler(ctx)
        self.assertEqual(len(self.board.find_player_area(P1, "deck").children), 3)
        self.assertEqual(len(self.board.find_player_area(P1, "discard").children), 0)


class TestColressExperiment(LostZoneRegiBase):
    async def test_take_three_lost_two(self):
        cards = [self.add_to("deck", make_card(PLAIN_BIG), P1) for _ in range(5)]
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        top3 = [c.entity_id for c in cards[-3:]]
        self.session.chooser_replies.append(top3)
        await colresss_experiment(ctx)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 3)
        self.assertEqual(len(self.board.find_player_area(P1, "lostZone").children), 2)


class TestTrekkingShoes(LostZoneRegiBase):
    def _intro_brackets(self, entity_id):
        """(viewer_ids, name) of brackets carrying an EntityIntroduced for entity_id."""
        out = []
        for viewer_ids, name, msgs in self.session.sent:
            for m in msgs:
                value = m.get("value", {}) if isinstance(m, dict) else {}
                if m["name"] == "EntityIntroduced" and value.get("entityID") == entity_id:
                    out.append((viewer_ids, name))
        return out

    def _assert_no_reveal_brackets(self, entity_id):
        """No RevealCardToAllEffect for entity_id anywhere (the panel version
        never parks the card in multiPresentArea)."""
        for _, _, msgs in self.session.sent:
            for m in msgs:
                value = m.get("value", {}) if isinstance(m, dict) else {}
                self.assertFalse(
                    m["name"] == "RevealCardToAllEffect" and value.get("entityID") == entity_id
                )

    async def test_take_into_hand(self):
        top = self.add_to("deck", make_card(PLAIN_BIG), P1)
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        self.session.choice_replies.append(0)  # Put into hand
        await trekking_shoes(ctx)
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(top.entity_id, [c.entity_id for c in hand.children])
        self.assertEqual(len(self.board.find_player_area(P1, "discard").children), 0)
        # Owner-only intro, no reveal park anywhere.
        self.assertEqual(self._intro_brackets(top.entity_id), [([P1], "SerialSequence")])
        self._assert_no_reveal_brackets(top.entity_id)
        # Floating ability panel on the revealed card (not the plain centered dialog).
        self.assertEqual(len(self.session.panel_calls), 1)
        player_id, source_id, prompt, buttons = self.session.panel_calls[0]
        self.assertEqual(player_id, P1)
        self.assertEqual(source_id, top.entity_id)
        self.assertEqual(len(buttons), 2)

    async def test_decline_discards_and_draws(self):
        top = self.add_to("deck", make_card(PLAIN_BIG), P1)
        under = self.add_to("deck", make_card(PLAIN_BIG), P1)  # becomes new top after discard
        # deck order: [top, under]; top-of-deck is last child = 'under'
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        self.session.choice_replies.append(1)  # Discard and draw a card
        await trekking_shoes(ctx)
        discard = self.board.find_player_area(P1, "discard")
        hand = self.board.find_player_area(P1, "hand")
        self.assertEqual(len(discard.children), 1)  # the peeked top card
        self.assertEqual(len(hand.children), 1)  # drew a card
        self.assertEqual(self._intro_brackets(under.entity_id), [([P1], "SerialSequence")])
        self._assert_no_reveal_brackets(under.entity_id)
        self.assertEqual(len(self.session.panel_calls), 1)
        player_id, source_id, prompt, buttons = self.session.panel_calls[0]
        self.assertEqual(player_id, P1)
        self.assertEqual(source_id, under.entity_id)
        self.assertEqual(len(buttons), 2)

    async def test_empty_deck_no_op(self):
        source = self.make_source()
        ctx = EffectContext(self.session, P1, source, None)
        await trekking_shoes(ctx)
        self.assertEqual(len(self.session.panel_calls), 0)
        self.assertEqual(len(self.session.prompts), 0)
        self.assertEqual(len(self.session.sent), 0)


class TestRegiGate(LostZoneRegiBase):
    async def test_searches_basic_onto_bench(self):
        attacker = self.add_to("activePokemonArea", make_card(REGIROCK), P1)
        self.add_to("activePokemonArea", make_card(PLAIN_BIG), P2)
        basic = self.add_to("deck", make_card(PLAIN_BIG), P1)
        attack = REGIROCK.abilities[0]
        self.session.chooser_replies.append([basic.entity_id])
        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)
        self.assertIn(basic.entity_id,
                      [c.entity_id for c in self.board.find_player_area(P1, "bench").children])


class TestWildStyle(LostZoneRegiBase):
    async def test_cost_reduction_per_opposing_special_pokemon(self):
        active = self.add_to("activePokemonArea", make_card(DRAPION_V), P1)
        cost = {"Colorless": 4}
        self.assertEqual(effective_attack_cost(self.board, active, dict(cost)), cost)
        self.add_to("bench", make_card(FUSION_DEF), P2)
        self.add_to("activePokemonArea", make_card(FUSION_DEF), P2)
        self.assertEqual(
            effective_attack_cost(self.board, active, dict(cost)), {"Colorless": 2}
        )


class TestEnergies(LostZoneRegiBase):
    async def test_twin_energy_provides_two(self):
        twin = create_card_entity(make_card(TWIN_ENERGY), owning_player_id=P1)
        self.assertEqual(energy_provided_count(twin), 2)

    async def test_gift_energy_draws_to_seven(self):
        source = self.add_to("activePokemonArea", make_card(REGIROCK), P1)
        for _ in range(10):
            self.add_to("deck", make_card(PLAIN_BIG), P1)
        self.add_to("hand", make_card(PLAIN_BIG), P1)  # 1 card in hand
        ctx = EffectContext(self.session, P1, source, None)
        await gift_energy_on_ko(ctx)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 7)


class TestDarkAsset(LostZoneRegiBase):
    async def test_draws_to_six_when_accepted(self):
        source = self.add_to("bench", make_card(CROBAT_V), P1)
        for _ in range(10):
            self.add_to("deck", make_card(PLAIN_BIG), P1)
        self.add_to("hand", make_card(PLAIN_BIG), P1)  # 1 in hand
        ctx = EffectContext(self.session, P1, source, CROBAT_V.abilities[0])
        self.session.choice_replies.append(0)  # "Yes"
        await dark_asset(ctx)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 6)


class TestMoonlightShuriken(LostZoneRegiBase):
    async def test_one_chooser_resolves_both_targets(self):
        attacker = self.add_to("activePokemonArea", make_card(RADIANT_GRENINJA), P1)
        self.attach(make_card(WATER_ENERGY_DEF), attacker, P1)
        self.attach(make_card(WATER_ENERGY_DEF), attacker, P1)
        opp_active = self.add_to("activePokemonArea", make_card(WEAK_TO_WATER_DEF), P2)
        opp_bench = self.add_to("bench", make_card(PLAIN_BIG), P2)
        attack = RADIANT_GRENINJA.abilities[1]
        self.session.chooser_replies.append([opp_active.entity_id, opp_bench.entity_id])

        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)

        self.assertEqual(len(self.session.chooser_calls), 1)
        self.assertEqual(self.session.chooser_calls[0][2], 2)
        # Active takes Weakness (x2, Greninja is Water); Benched does not.
        self.assertEqual(opp_active.get_attribute(AttrID.HP), 200 - 180)
        self.assertEqual(opp_bench.get_attribute(AttrID.HP), 330 - 90)


class TestMirageGateCondition(LostZoneRegiBase):
    async def test_requires_seven_lost_zone(self):
        self.fill_lost_zone(6)
        self.assertFalse(mirage_gate_condition(self.board, P1))
        self.add_to("lostZone", make_card(PLAIN_BIG), P1)
        self.assertTrue(mirage_gate_condition(self.board, P1))


class TestMirageGate(LostZoneRegiBase):
    async def test_one_group_per_type_then_per_energy_attach_picks(self):
        source = self.make_source(player_id=P1)
        # Multiple basics of the same type: only ONE representative per type
        # should reach the browser.
        water1 = self.add_to("deck", make_card(WATER_ENERGY_DEF), P1)
        water2 = self.add_to("deck", make_card(WATER_ENERGY_DEF), P1)
        psychic1 = self.add_to("deck", make_card(PSYCHIC_ENERGY_DEF), P1)
        psychic2 = self.add_to("deck", make_card(PSYCHIC_ENERGY_DEF), P1)
        pokemon = self.add_to("activePokemonArea", make_card(PLAIN_BIG), P1)
        ctx = EffectContext(self.session, P1, source, None)
        self.session.chooser_replies.append([water1.entity_id, psychic1.entity_id])  # energy pick
        self.session.chooser_replies.append([pokemon.entity_id])  # attach #1
        self.session.chooser_replies.append([pokemon.entity_id])  # attach #2

        await mirage_gate(ctx)

        energies = self.board.attached_energies(pokemon)
        self.assertEqual(len(energies), 2)
        self.assertIn(water1, energies)
        self.assertIn(psychic1, energies)
        self.assertEqual(len(self.session.chooser_calls), 3)
        energy_call_ids = self.session.chooser_calls[0][1]
        self.assertEqual(set(energy_call_ids), {water1.entity_id, psychic1.entity_id})
        self.assertNotIn(water2.entity_id, energy_call_ids)
        self.assertNotIn(psychic2.entity_id, energy_call_ids)

    async def test_whiffs_with_no_basic_energy_in_deck(self):
        source = self.make_source(player_id=P1)
        self.add_to("deck", make_card(PLAIN_BIG), P1)
        ctx = EffectContext(self.session, P1, source, None)
        await mirage_gate(ctx)
        self.assertEqual(len(self.session.chooser_calls), 1)  # the whiffed browse


class TestMirageGateSingleGroupOffer(unittest.IsolatedAsyncioTestCase):
    """Wire shape of the plain single-group reveal browser mirage_gate now
    uses: one representative card per basic-Energy type, not an
    AnyComposite browser (that node kind misrenders on the client)."""

    class _MockClient:
        def __init__(self, account_id, username):
            self.player = type("P", (), {
                "account_id": account_id, "username": username,
                "screen_name": username, "avatar_decks": [],
            })()
            self.addr = ("127.0.0.1", 12345)
            self.sent_packets = []

        async def send_packet(self, data, request_id=0, flags=0):
            self.sent_packets.append(data)

    def setUp(self):
        self.client1 = self._MockClient(P1, "Ash")
        self.client2 = self._MockClient(P2, "Gary")
        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                P1: {"client": self.client1, "deck": {"deckID": "d1", "deckName": "A", "cards": []}, "ready": True},
                P2: {"client": self.client2, "deck": {"deckID": "d2", "deckName": "B", "cards": []}, "ready": True},
            },
        }
        self.session = GameSession(str(uuid.uuid4()), pairing)
        self.board = self.session.board_state
        self.captured_offer = None

        async def fake_prompt(player, msg_name, offer, expected_counter=None):
            self.captured_offer = offer
            return {"selection": {"targetResponses": [
                {"entityList": [self.water.entity_id, self.psychic.entity_id]}
            ]}}
        self.session.prompt_selection_message = fake_prompt

        deck = self.board.find_player_area(P1, "deck")
        self.water = create_card_entity(make_card(WATER_ENERGY_DEF), owning_player_id=P1)
        self.board.add_card_to_area(self.water, deck)
        self.water2 = create_card_entity(make_card(WATER_ENERGY_DEF), owning_player_id=P1)
        self.board.add_card_to_area(self.water2, deck)
        self.psychic = create_card_entity(make_card(PSYCHIC_ENERGY_DEF), owning_player_id=P1)
        self.board.add_card_to_area(self.psychic, deck)
        self.source = create_card_entity(make_card(REGIROCK), owning_player_id=P1)

    async def test_offer_shape(self):
        ctx = EffectContext(self.session, P1, self.source, None)
        reps = [self.water, self.psychic]
        picked = await ctx.choose_cards(
            reps, 2, minimum=0,
            prompt="Choose up to 2 basic Energy cards of different types.",
            display_cards=reps,
        )

        offer = self.captured_offer
        node = next(iter(offer["targetMap"].values()))[0]
        self.assertEqual(node["name"], "CompositeRevealEntityListTargetInformation")
        self.assertEqual(offer["targetType"], "CompositeRevealEntityListTargetInformation")
        self.assertEqual(node["numberToSelect"], 2)
        self.assertEqual(node["minimumToSelect"], 0)
        self.assertFalse(node["forced"])
        self.assertEqual(set(node["revealEntities"].keys()),
                         {self.water.entity_id, self.psychic.entity_id})
        self.assertNotIn(self.water2.entity_id, node["revealEntities"])
        self.assertEqual(set(node["validTargets"]),
                          {self.water.entity_id, self.psychic.entity_id})
        self.assertTrue(node["targetPrompt"])
        self.assertEqual(picked, [self.water, self.psychic])


class TestDamageCounterPlacementOffer(unittest.IsolatedAsyncioTestCase):
    """Wire shape of the native click-to-place damage-counter picker (Sableye's
    Lost Mine): MultiSelectEntityListTargetInformation node (command Q.N), and
    a MultiSelectEntityListTargetResponse-shaped reply."""

    class _MockClient:
        def __init__(self, account_id, username):
            self.player = type("P", (), {
                "account_id": account_id, "username": username,
                "screen_name": username, "avatar_decks": [],
            })()
            self.addr = ("127.0.0.1", 12345)
            self.sent_packets = []

        async def send_packet(self, data, request_id=0, flags=0):
            self.sent_packets.append(data)

    def setUp(self):
        self.client1 = self._MockClient(P1, "Ash")
        self.client2 = self._MockClient(P2, "Gary")
        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                P1: {"client": self.client1, "deck": {"deckID": "d1", "deckName": "A", "cards": []}, "ready": True},
                P2: {"client": self.client2, "deck": {"deckID": "d2", "deckName": "B", "cards": []}, "ready": True},
            },
        }
        self.session = GameSession(str(uuid.uuid4()), pairing)
        self.board = self.session.board_state
        self.captured_offer = None

        self.source = create_card_entity(make_card(SABLEYE), owning_player_id=P1)
        self.active = create_card_entity(make_card(REGIROCK), owning_player_id=P2)
        self.board.add_card_to_area(
            self.active, self.board.find_player_area(P2, "activePokemonArea")
        )
        self.benched = create_card_entity(make_card(REGICE), owning_player_id=P2)
        self.board.add_card_to_area(
            self.benched, self.board.find_player_area(P2, "bench")
        )

        async def fake_prompt(player, msg_name, offer, expected_counter=None):
            self.captured_offer = offer
            return {"selection": {"targetResponses": [
                {"entities": [
                    {"target": self.active.entity_id, "selections": 9},
                    {"target": self.benched.entity_id, "selections": 3},
                ]}
            ]}}
        self.session.prompt_selection_message = fake_prompt

    async def test_offer_shape_and_reply_parsing(self):
        ctx = EffectContext(self.session, P1, self.source, None)
        await ctx.place_damage_counters(12, ctx.opponent_pokemon_in_play())

        offer = self.captured_offer
        node = next(iter(offer["targetMap"].values()))[0]
        self.assertEqual(node["name"], "MultiSelectEntityListTargetInformation")
        self.assertEqual(offer["targetType"], "MultiSelectEntityListTargetInformation")
        self.assertEqual(node["numberToSelect"], 12)
        self.assertEqual(node["minimumToSelect"], 12)
        self.assertTrue(node["forced"])
        self.assertEqual(node["amountPerClick"], 10)
        self.assertIsNotNone(node.get("hintTargetMap"))
        self.assertTrue(node["targetPrompt"])
        self.assertEqual(
            set(node["validTargets"]), {self.active.entity_id, self.benched.entity_id}
        )

        self.assertEqual(self.active.get_attribute(AttrID.HP), 130 - 90)
        self.assertEqual(self.benched.get_attribute(AttrID.HP), 130 - 30)


class TestPublicPileReveal(LostZoneRegiBase):
    """A card moved into a public pile from a zone the owner can't see (deck /
    prizes) must be introduced to BOTH viewers -- otherwise the owner's pile
    renders a faceless card back and the Lost Zone viewer NREs on the missing
    archetype attribute (a.k.InitializeStackedCards)."""

    def _intros_to(self, entity_id, viewer):
        return [m for vids, _name, msgs in self.session.sent if vids == [viewer]
                for m in msgs
                if m.get("name") == "EntityIntroduced"
                and m["value"]["entityID"] == entity_id]

    async def test_deck_card_to_lost_zone_introduces_to_both(self):
        source = self.add_to("activePokemonArea", make_card(REGIROCK), P1)
        deck_card = self.add_to("deck", make_card(PLAIN_BIG), P1)
        ctx = EffectContext(self.session, P1, source, None)
        await ctx.move_to_lost_zone([deck_card])
        await self.session.send_game_sequence_flush(ctx)

        self.assertEqual(len(self._intros_to(deck_card.entity_id, P1)), 1)
        self.assertEqual(len(self._intros_to(deck_card.entity_id, P2)), 1)
        lost = self.board.find_player_area(P1, "lostZone")
        self.assertIn(deck_card, lost.children)

    async def test_hand_card_to_discard_intros_opponent_only(self):
        # A hand card is already visible to its owner -- no redundant owner
        # intro (the opponent still needs one, hand is hidden from them).
        source = self.add_to("activePokemonArea", make_card(REGIROCK), P1)
        hand_card = self.add_to("hand", make_card(PLAIN_BIG), P1)
        ctx = EffectContext(self.session, P1, source, None)
        await ctx.discard_cards([hand_card])
        await self.session.send_game_sequence_flush(ctx)

        self.assertEqual(len(self._intros_to(hand_card.entity_id, P1)), 0)
        self.assertEqual(len(self._intros_to(hand_card.entity_id, P2)), 1)
