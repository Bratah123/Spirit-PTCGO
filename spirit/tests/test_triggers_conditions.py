"""Tests for the trigger-system expansion (ON_EVOLVE/ON_KNOCKED_OUT/
BETWEEN_TURNS) and the special-condition checkup engine (poison/burn/
paralysis/confusion), plus the T8 leave-Active-spot effect cleanup."""

import unittest
import uuid
from unittest.mock import AsyncMock, patch

from spirit.game.attributes import AttrID, GameSequence, PokemonStage, PokemonTypes, SpecialConditions
from spirit.game.card_effects.pokemon import UnfazedFatPassive, condition_attack
from spirit.game.data_utils import (
    Ability,
    Attack,
    PokemonCardDef,
    StadiumCardDef,
    Triggers,
)
from spirit.game.models.board import create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.effects import EffectContext, resolve_attack
from spirit.game.session.game_session import GameSession
from spirit.game.session.constants import SelectionKind
from spirit.game.session.legal_actions import ACTION_RETREAT, compute_legal_actions
from spirit.game.session.passives import Passive

P1 = "player-1"
P2 = "player-2"


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


# ----------------------------------------------------------------------
# Shared card fixtures
# ----------------------------------------------------------------------

BASIC_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000001",
    key="TST", name="com.test.pokemon.TrigBasic.Name",
    collector_number=1, set_code="TST", rarity=1,
    hp=60, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
)
BASIC = make_card(BASIC_DEF)

PLAIN_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000002",
    key="TST", name="com.test.pokemon.TrigPlain.Name",
    collector_number=2, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
)
PLAIN = make_card(PLAIN_DEF)

LOW_HP_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000003",
    key="TST", name="com.test.pokemon.TrigLowHP.Name",
    collector_number=3, set_code="TST", rarity=1,
    hp=5, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
)
LOW_HP = make_card(LOW_HP_DEF)

EVOLVE_MARKER_CALLS = []


async def _evolve_marker_effect(ctx):
    EVOLVE_MARKER_CALLS.append(ctx.source.entity_id)


EVOLUTION_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000004",
    key="TST", name="com.test.pokemon.TrigEvo.Name",
    collector_number=4, set_code="TST", rarity=1,
    hp=120, elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1, retreat_cost=0,
    evolves_from="com.test.pokemon.TrigBasic.Name",
    abilities=[Ability("On Evolve Marker", trigger=Triggers.ON_EVOLVE,
                       effect=_evolve_marker_effect)],
)
EVOLUTION = make_card(EVOLUTION_DEF)


class _LocksAllAbilitiesPassive(Passive):
    """Test-local stand-in for a Path to the Peak-style stadium."""
    def blocks_abilities(self, pokemon, carrier) -> bool:
        return True


LOCK_STADIUM_DEF = StadiumCardDef(
    passive=_LocksAllAbilitiesPassive(),
    guid="70000000-0000-0000-0000-000000000005",
    key="TST", name="com.test.trainer.LockStadium.Name",
    collector_number=5, set_code="TST", rarity=0,
)
LOCK_STADIUM = make_card(LOCK_STADIUM_DEF)

KO_TRIGGER_CALLS = []


async def _ko_marker_effect(ctx):
    KO_TRIGGER_CALLS.append((ctx.ko_from_attack, ctx.ko_attacker))


KO_TARGET_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000006",
    key="TST", name="com.test.pokemon.TrigKOTarget.Name",
    collector_number=6, set_code="TST", rarity=1,
    hp=10, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Ability("On KO Marker", trigger=Triggers.ON_KNOCKED_OUT,
                       effect=_ko_marker_effect)],
)
KO_TARGET = make_card(KO_TARGET_DEF)

LETHAL_ATTACKER_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000007",
    key="TST", name="com.test.pokemon.TrigLethal.Name",
    collector_number=7, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack("Smash", cost={PokemonTypes.COLORLESS: 1}, damage=50)],
)
LETHAL_ATTACKER = make_card(LETHAL_ATTACKER_DEF)
LETHAL_ATTACK = LETHAL_ATTACKER_DEF.abilities[0]

CHAIN_CALLS = []


async def _chain_a_effect(ctx):
    CHAIN_CALLS.append("A")
    await ctx.knock_out(ctx.opponent_active())


async def _chain_b_effect(ctx):
    CHAIN_CALLS.append("B")


CHAIN_A_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000008",
    key="TST", name="com.test.pokemon.TrigChainA.Name",
    collector_number=8, set_code="TST", rarity=1,
    hp=10, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Ability("Chain A", trigger=Triggers.ON_KNOCKED_OUT, effect=_chain_a_effect)],
)
CHAIN_A = make_card(CHAIN_A_DEF)

CHAIN_B_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000009",
    key="TST", name="com.test.pokemon.TrigChainB.Name",
    collector_number=9, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[
        Attack("Zap", cost={PokemonTypes.COLORLESS: 1}, damage=50),
        Ability("Chain B", trigger=Triggers.ON_KNOCKED_OUT, effect=_chain_b_effect),
    ],
)
CHAIN_B = make_card(CHAIN_B_DEF)
CHAIN_B_ATTACK = CHAIN_B_DEF.abilities[0]

BETWEEN_TURNS_CALLS = []


async def _between_turns_effect(ctx):
    BETWEEN_TURNS_CALLS.append(ctx.source.entity_id)


BETWEEN_TURNS_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-00000000000a",
    key="TST", name="com.test.pokemon.TrigBetween.Name",
    collector_number=10, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Ability("Between Marker", trigger=Triggers.BETWEEN_TURNS,
                       effect=_between_turns_effect)],
)
BETWEEN_TURNS_POKEMON = make_card(BETWEEN_TURNS_DEF)

CONFUSED_ATTACKER_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-00000000000b",
    key="TST", name="com.test.pokemon.TrigConfused.Name",
    collector_number=11, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack("Tackle", cost={PokemonTypes.COLORLESS: 1}, damage=30)],
)
CONFUSED_ATTACKER = make_card(CONFUSED_ATTACKER_DEF)
CONFUSED_ATTACK = CONFUSED_ATTACKER_DEF.abilities[0]

LOW_HP_CONFUSED_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-00000000000c",
    key="TST", name="com.test.pokemon.TrigConfusedLowHP.Name",
    collector_number=12, set_code="TST", rarity=1,
    hp=20, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack("Tackle", cost={PokemonTypes.COLORLESS: 1}, damage=30)],
)
LOW_HP_CONFUSED = make_card(LOW_HP_CONFUSED_DEF)
LOW_HP_CONFUSED_ATTACK = LOW_HP_CONFUSED_DEF.abilities[0]

VSTAR_LOCK_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-00000000001b",
    key="TST", name="com.test.pokemon.TrigVstarLock.Name",
    collector_number=27, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack("Star Burst", cost={PokemonTypes.COLORLESS: 1}, damage=30,
                      vstar=True, locks_next_turn=True)],
)
VSTAR_LOCK_ATTACKER = make_card(VSTAR_LOCK_DEF)
VSTAR_LOCK_ATTACK = VSTAR_LOCK_DEF.abilities[0]

POISON_ATTACK_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-00000000000d",
    key="TST", name="com.test.pokemon.TrigPoisonAttacker.Name",
    collector_number=13, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack("Poison Sting", cost={PokemonTypes.COLORLESS: 1}, damage=10,
                      effect=condition_attack(SpecialConditions.POISONED))],
)
POISON_ATTACKER = make_card(POISON_ATTACK_DEF)
POISON_ATTACK = POISON_ATTACK_DEF.abilities[0]

FLIP_PARALYZE_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-00000000000e",
    key="TST", name="com.test.pokemon.TrigFlipAttacker.Name",
    collector_number=14, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack("Static Shock", cost={PokemonTypes.COLORLESS: 1},
                      effect=condition_attack(SpecialConditions.PARALYZED, flip=True))],
)
FLIP_PARALYZE_ATTACKER = make_card(FLIP_PARALYZE_DEF)
FLIP_PARALYZE_ATTACK = FLIP_PARALYZE_DEF.abilities[0]

MULTI_CONDITION_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-00000000000f",
    key="TST", name="com.test.pokemon.TrigMultiCondition.Name",
    collector_number=15, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack(
        "Toxic Burn", cost={PokemonTypes.COLORLESS: 1}, damage=10,
        effect=condition_attack(SpecialConditions.POISONED, SpecialConditions.BURNED,
                                self_conditions=(SpecialConditions.CONFUSED,)),
    )],
)
MULTI_CONDITION_ATTACKER = make_card(MULTI_CONDITION_DEF)
MULTI_CONDITION_ATTACK = MULTI_CONDITION_DEF.abilities[0]

# UnfazedFatPassive's `target is carrier` check assumes an ABILITY passive
# (carrier = the Pokemon itself), not a tool/energy attachment's carrier.
SHIELDED_DEFENDER_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000010",
    key="TST", name="com.test.pokemon.TrigShieldedDefender.Name",
    collector_number=16, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Ability("Unfazed Fat", passive=UnfazedFatPassive())],
)
SHIELDED_DEFENDER = make_card(SHIELDED_DEFENDER_DEF)

LOCK_ATTACKER_DEF = PokemonCardDef(
    guid="70000000-0000-0000-0000-000000000011",
    key="TST", name="com.test.pokemon.TrigLockAttacker.Name",
    collector_number=17, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS], retreat_cost=0,
    abilities=[Attack("Overexert", cost={PokemonTypes.COLORLESS: 1}, damage=10,
                      locks_next_turn=True)],
)
LOCK_ATTACKER = make_card(LOCK_ATTACKER_DEF)
LOCK_ATTACK = LOCK_ATTACKER_DEF.abilities[0]


class MockClientHandler:
    def __init__(self, account_id, username):
        self.player = type("P", (), {
            "account_id": account_id, "username": username,
            "screen_name": username, "avatar_decks": [],
        })()
        self.addr = ("127.0.0.1", 12345)
        self.sent_packets = []

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)


class TriggerTestBase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client1 = MockClientHandler(P1, "Ash")
        self.client2 = MockClientHandler(P2, "Gary")
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
        self.session.turn_state.begin_turn(P1)
        EVOLVE_MARKER_CALLS.clear()
        KO_TRIGGER_CALLS.clear()
        CHAIN_CALLS.clear()
        BETWEEN_TURNS_CALLS.clear()

    def add_to(self, area_name, card, player_id=P1):
        entity = create_card_entity(card, owning_player_id=player_id)
        self.board.add_card_to_area(entity, self.board.find_player_area(player_id, area_name))
        return entity

    def add_stadium(self, card, player_id=P1):
        entity = create_card_entity(card, owning_player_id=player_id)
        self.board.add_card_to_area(entity, self.board.find_global_area("activeStadium"))
        return entity

    def brackets(self, client, name):
        """Inner messages of each sequence bracket with the given name."""
        out = []
        current = None
        for packet in client.sent_packets:
            msg = packet.get("msg") if isinstance(packet, dict) else None
            if not isinstance(msg, dict):
                continue
            if msg.get("name") == "StartSequence" and msg["value"].get("name") == name:
                current = []
            elif msg.get("name") == "StopSequence" and current is not None:
                out.append(current)
                current = None
            elif current is not None:
                current.append(msg)
        return out


NO_SLEEP = patch("spirit.game.session.game_session.asyncio.sleep", new=AsyncMock())


# ----------------------------------------------------------------------
# T1/T2/T3: ON_EVOLVE / ON_KNOCKED_OUT / BETWEEN_TURNS
# ----------------------------------------------------------------------

class TestOnEvolveTrigger(TriggerTestBase):
    def _evolve_entry(self, evo_card):
        entries = compute_legal_actions(self.board, self.session.turn_state, P1, self.session.game_id)
        return next(e for e in entries if e["entityID"] == evo_card.entity_id)

    async def test_fires_after_evolve(self):
        self.session.turn_state.begin_turn(P2)
        self.session.turn_state.begin_turn(P1)  # turn 3: evolving is legal
        target = self.add_to("bench", BASIC, P1)
        evo_card = self.add_to("hand", EVOLUTION, P1)
        entry = self._evolve_entry(evo_card)

        await self.session._execute_evolve(P1, evo_card, entry, [target.entity_id])

        self.assertEqual(EVOLVE_MARKER_CALLS, [evo_card.entity_id])

    async def test_does_not_fire_when_path_locked(self):
        self.session.turn_state.begin_turn(P2)
        self.session.turn_state.begin_turn(P1)
        self.add_stadium(LOCK_STADIUM, P2)
        target = self.add_to("bench", BASIC, P1)
        evo_card = self.add_to("hand", EVOLUTION, P1)
        entry = self._evolve_entry(evo_card)

        await self.session._execute_evolve(P1, evo_card, entry, [target.entity_id])

        self.assertEqual(EVOLVE_MARKER_CALLS, [])


class TestEvolveCure(TriggerTestBase):
    async def test_evolving_clears_pre_evolution_conditions(self):
        self.session.turn_state.begin_turn(P2)
        self.session.turn_state.begin_turn(P1)
        target = self.add_to("bench", BASIC, P1)
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned"])
        self.session.poison_counters[target.entity_id] = 3
        evo_card = self.add_to("hand", EVOLUTION, P1)
        entries = compute_legal_actions(self.board, self.session.turn_state, P1, self.session.game_id)
        entry = next(e for e in entries if e["entityID"] == evo_card.entity_id)

        await self.session._execute_evolve(P1, evo_card, entry, [target.entity_id])

        self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(target.entity_id, self.session.poison_counters)
        cure_brackets = self.brackets(self.client1, GameSequence.REMOVE_SPECIAL_CONDITION.value)
        self.assertEqual(len(cure_brackets), 1)
        self.assertEqual(cure_brackets[0][0]["value"]["key"], "Target")
        self.assertEqual(cure_brackets[0][0]["value"]["value"], target.entity_id)


class TestOnKnockedOutTrigger(TriggerTestBase):
    async def test_fires_with_ko_from_attack_and_attacker(self):
        attacker = self.add_to("activePokemonArea", LETHAL_ATTACKER, P1)
        target = self.add_to("activePokemonArea", KO_TARGET, P2)
        self.add_to("bench", BASIC, P2)  # promotion candidate

        await resolve_attack(self.session, P1, attacker, LETHAL_ATTACK, LETHAL_ATTACK.ability_id)

        self.assertEqual(KO_TRIGGER_CALLS, [(True, attacker)])
        discard = self.board.find_player_area(P2, "discard")
        self.assertIn(target, discard.children)

    async def test_does_not_fire_when_path_locked(self):
        attacker = self.add_to("activePokemonArea", LETHAL_ATTACKER, P1)
        self.add_stadium(LOCK_STADIUM, P1)
        target = self.add_to("activePokemonArea", KO_TARGET, P2)
        self.add_to("bench", BASIC, P2)

        await resolve_attack(self.session, P1, attacker, LETHAL_ATTACK, LETHAL_ATTACK.ability_id)

        self.assertEqual(KO_TRIGGER_CALLS, [])

    async def test_chained_knockout_recursion(self):
        attacker = self.add_to("activePokemonArea", CHAIN_B, P1)
        self.add_to("bench", BASIC, P1)  # P1 promotion candidate
        chain_a = self.add_to("activePokemonArea", CHAIN_A, P2)
        self.add_to("bench", BASIC, P2)  # P2 promotion candidate

        await resolve_attack(self.session, P1, attacker, CHAIN_B_ATTACK, CHAIN_B_ATTACK.ability_id)

        self.assertEqual(CHAIN_CALLS, ["A", "B"])
        self.assertIn(attacker, self.board.find_player_area(P1, "discard").children)
        self.assertIn(chain_a, self.board.find_player_area(P2, "discard").children)


class TestBetweenTurnsTrigger(TriggerTestBase):
    async def test_fires_each_checkup_for_every_in_play_pokemon(self):
        p1_active = self.add_to("activePokemonArea", BETWEEN_TURNS_POKEMON, P1)
        p2_active = self.add_to("activePokemonArea", PLAIN, P2)

        with NO_SLEEP:
            await self.session._run_pokemon_checkup(P1)

        self.assertEqual(BETWEEN_TURNS_CALLS, [p1_active.entity_id])

        with NO_SLEEP:
            await self.session._run_pokemon_checkup(P1)

        self.assertEqual(BETWEEN_TURNS_CALLS, [p1_active.entity_id, p1_active.entity_id])


# ----------------------------------------------------------------------
# T4: Special-condition checkup completion (poison/burn/sleep/paralysis)
# ----------------------------------------------------------------------

class TestPoisonCheckup(TriggerTestBase):
    async def test_bracket_order_and_default_damage(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned"])

        with NO_SLEEP:
            await self.session._checkup_poison(active)

        self.assertEqual(active.get_attribute(AttrID.HP), 90)
        brackets = self.brackets(self.client1, GameSequence.POISON_DAMAGE.value)
        self.assertEqual(len(brackets), 1)
        names = [m["name"] for m in brackets[0]]
        self.assertEqual(names, ["PlaceDamageEffect", "AttributeModified"])
        self.assertEqual(brackets[0][0]["value"]["amount"], 10)
        self.assertEqual(brackets[0][0]["value"]["destinationID"], active.entity_id)

    async def test_elevated_poison_counters(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned"])
        self.session.poison_counters[active.entity_id] = 3

        with NO_SLEEP:
            await self.session._checkup_poison(active)

        self.assertEqual(active.get_attribute(AttrID.HP), 70)

    async def test_poison_knockout_path(self):
        low = self.add_to("activePokemonArea", LOW_HP, P2)
        self.add_to("bench", BASIC, P2)
        low.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned"])

        with NO_SLEEP:
            await self.session._checkup_poison(low)

        discard = self.board.find_player_area(P2, "discard")
        self.assertIn(low, discard.children)


class TestBurnCheckup(TriggerTestBase):
    async def test_tick_then_cure_on_heads(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Burned"])

        with patch("spirit.game.session.game_session.random.choice", return_value=0), NO_SLEEP:
            await self.session._checkup_burn(P2, active)

        self.assertEqual(active.get_attribute(AttrID.HP), 80)
        self.assertEqual(active.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertEqual(len(self.brackets(self.client1, GameSequence.BURN_DAMAGE.value)), 1)
        self.assertEqual(len(self.brackets(self.client1, GameSequence.FLIP_FOR_BURN.value)), 1)
        self.assertEqual(len(self.brackets(self.client1, GameSequence.REMOVE_SPECIAL_CONDITION.value)), 1)

    async def test_tails_stays_burned(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Burned"])

        with patch("spirit.game.session.game_session.random.choice", return_value=1), NO_SLEEP:
            await self.session._checkup_burn(P2, active)

        self.assertEqual(active.get_attribute(AttrID.HP), 80)
        self.assertEqual(active.get_attribute(AttrID.SPECIAL_CONDITIONS), ["Burned"])
        self.assertEqual(len(self.brackets(self.client1, GameSequence.REMOVE_SPECIAL_CONDITION.value)), 0)

    async def test_poison_and_burn_both_tick(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned", "Burned"])

        with patch("spirit.game.session.game_session.random.choice", return_value=1), NO_SLEEP:
            await self.session._checkup_poison(active)
            await self.session._checkup_burn(P2, active)

        self.assertEqual(active.get_attribute(AttrID.HP), 70)  # 100 - 10 - 20


class TestSleepCheckupUnchanged(TriggerTestBase):
    async def test_wake_on_all_heads(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Asleep"])

        with patch("spirit.game.session.game_session.random.choice", return_value=0), NO_SLEEP:
            await self.session._checkup_sleep(P2, active)

        self.assertEqual(active.get_attribute(AttrID.SPECIAL_CONDITIONS), [])

    async def test_stays_asleep_on_any_tails(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Asleep"])

        with patch("spirit.game.session.game_session.random.choice", return_value=1), NO_SLEEP:
            await self.session._checkup_sleep(P2, active)

        self.assertEqual(active.get_attribute(AttrID.SPECIAL_CONDITIONS), ["Asleep"])


class TestParalysisCure(TriggerTestBase):
    async def test_cures_after_owner_next_turn_not_same_turn(self):
        active = self.add_to("activePokemonArea", PLAIN, P1)
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Paralyzed"])
        self.session.paralyzed_since[active.entity_id] = self.session.turn_state.turn_number

        with NO_SLEEP:
            await self.session._run_pokemon_checkup(P1)
        self.assertIn("Paralyzed", active.get_attribute(AttrID.SPECIAL_CONDITIONS))

        self.session.turn_state.begin_turn(P2)
        self.session.turn_state.begin_turn(P1)
        with NO_SLEEP:
            await self.session._run_pokemon_checkup(P1)
        self.assertNotIn("Paralyzed", active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


# ----------------------------------------------------------------------
# T5: Confusion attack flip
# ----------------------------------------------------------------------

class TestConfusionAttackFlip(TriggerTestBase):
    async def test_heads_proceeds_with_normal_attack(self):
        attacker = self.add_to("activePokemonArea", CONFUSED_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN, P2)
        attacker.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Confused"])
        entry = {"selectableAction": {"actionID": CONFUSED_ATTACK.ability_id}}

        with patch("spirit.game.session.game_session.random.choice", return_value=0), NO_SLEEP:
            turn_over = await self.session._execute_attack(P1, attacker, entry)

        self.assertTrue(turn_over)
        self.assertEqual(defender.get_attribute(AttrID.HP), 70)
        self.assertEqual(attacker.get_attribute(AttrID.HP), 100)
        self.assertEqual(len(self.brackets(self.client1, GameSequence.FLIP_FOR_CONFUSION.value)), 1)
        self.assertEqual(len(self.brackets(self.client1, GameSequence.HURT_FROM_CONFUSION.value)), 0)

    async def test_tails_hurts_self_and_ends_turn_without_attacking(self):
        attacker = self.add_to("activePokemonArea", CONFUSED_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN, P2)
        attacker.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Confused"])
        entry = {"selectableAction": {"actionID": CONFUSED_ATTACK.ability_id}}

        with patch("spirit.game.session.game_session.random.choice", return_value=1), NO_SLEEP:
            turn_over = await self.session._execute_attack(P1, attacker, entry)

        self.assertTrue(turn_over)
        self.assertEqual(defender.get_attribute(AttrID.HP), 100)
        self.assertEqual(attacker.get_attribute(AttrID.HP), 70)
        hurt_brackets = self.brackets(self.client1, GameSequence.HURT_FROM_CONFUSION.value)
        self.assertEqual(len(hurt_brackets), 1)
        self.assertEqual([m["name"] for m in hurt_brackets[0]],
                         ["PlaceDamageEffect", "AttributeModified"])

    async def test_tails_does_not_consume_vstar_or_apply_locks(self):
        attacker = self.add_to("activePokemonArea", VSTAR_LOCK_ATTACKER, P1)
        self.add_to("activePokemonArea", PLAIN, P2)
        attacker.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Confused"])
        entry = {"selectableAction": {"actionID": VSTAR_LOCK_ATTACK.ability_id}}

        with patch("spirit.game.session.game_session.random.choice", return_value=1), NO_SLEEP:
            turn_over = await self.session._execute_attack(P1, attacker, entry)

        # A confusion-failed attack never happened: no VSTAR use, no lock.
        self.assertTrue(turn_over)
        self.assertNotIn(P1, self.session.turn_state.vstar_used)
        self.assertEqual(self.session.turn_state.attack_locks, {})

    async def test_tails_self_knockout_promotes_new_active(self):
        attacker = self.add_to("activePokemonArea", LOW_HP_CONFUSED, P1)
        bench = self.add_to("bench", BASIC, P1)
        self.add_to("activePokemonArea", PLAIN, P2)
        attacker.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Confused"])
        entry = {"selectableAction": {"actionID": LOW_HP_CONFUSED_ATTACK.ability_id}}

        with patch("spirit.game.session.game_session.random.choice", return_value=1), NO_SLEEP:
            await self.session._execute_attack(P1, attacker, entry)

        discard = self.board.find_player_area(P1, "discard")
        self.assertIn(attacker, discard.children)
        active_area = self.board.find_player_area(P1, "activePokemonArea")
        self.assertEqual(active_area.children, [bench])


# ----------------------------------------------------------------------
# T6: Condition bookkeeping (mutual exclusivity)
# ----------------------------------------------------------------------

class TestMutualExclusivity(TriggerTestBase):
    async def test_asleep_confused_paralyzed_replace_each_other(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        ctx = EffectContext(self.session, P1, active, None)

        await ctx.apply_special_condition(active, SpecialConditions.ASLEEP, checkup_coins=2)
        self.assertEqual(self.session.sleep_checkup_coins.get(active.entity_id), 2)

        await ctx.apply_special_condition(active, SpecialConditions.PARALYZED)
        self.assertEqual(active.get_attribute(AttrID.SPECIAL_CONDITIONS), ["Paralyzed"])
        self.assertNotIn(active.entity_id, self.session.sleep_checkup_coins)

        await ctx.apply_special_condition(active, SpecialConditions.CONFUSED)
        self.assertEqual(active.get_attribute(AttrID.SPECIAL_CONDITIONS), ["Confused"])
        self.assertNotIn(active.entity_id, self.session.paralyzed_since)

    async def test_poison_and_burn_stack_with_everything(self):
        active = self.add_to("activePokemonArea", PLAIN, P2)
        ctx = EffectContext(self.session, P1, active, None)

        await ctx.apply_special_condition(active, SpecialConditions.CONFUSED)
        await ctx.apply_special_condition(active, SpecialConditions.POISONED, poison_counters=2)
        await ctx.apply_special_condition(active, SpecialConditions.BURNED)

        self.assertEqual(
            set(active.get_attribute(AttrID.SPECIAL_CONDITIONS)),
            {"Confused", "Poisoned", "Burned"},
        )
        self.assertEqual(self.session.poison_counters.get(active.entity_id), 2)


# ----------------------------------------------------------------------
# T7: condition_attack factory
# ----------------------------------------------------------------------

class TestConditionAttackFactory(TriggerTestBase):
    async def test_no_flip_applies_condition_and_damage(self):
        attacker = self.add_to("activePokemonArea", POISON_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN, P2)

        await resolve_attack(self.session, P1, attacker, POISON_ATTACK, POISON_ATTACK.ability_id)

        self.assertEqual(defender.get_attribute(AttrID.HP), 90)
        self.assertIn("Poisoned", defender.get_attribute(AttrID.SPECIAL_CONDITIONS))

    async def test_flip_heads_applies_condition(self):
        attacker = self.add_to("activePokemonArea", FLIP_PARALYZE_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN, P2)

        with patch("spirit.game.session.effects.random.choice", return_value=0):
            await resolve_attack(self.session, P1, attacker, FLIP_PARALYZE_ATTACK,
                                 FLIP_PARALYZE_ATTACK.ability_id)

        self.assertIn("Paralyzed", defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])

    async def test_flip_tails_applies_nothing(self):
        attacker = self.add_to("activePokemonArea", FLIP_PARALYZE_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN, P2)

        with patch("spirit.game.session.effects.random.choice", return_value=1):
            await resolve_attack(self.session, P1, attacker, FLIP_PARALYZE_ATTACK,
                                 FLIP_PARALYZE_ATTACK.ability_id)

        self.assertNotIn("Paralyzed", defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])

    async def test_multi_condition_and_self_condition(self):
        attacker = self.add_to("activePokemonArea", MULTI_CONDITION_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN, P2)

        await resolve_attack(self.session, P1, attacker, MULTI_CONDITION_ATTACK,
                             MULTI_CONDITION_ATTACK.ability_id)

        self.assertEqual(
            set(defender.get_attribute(AttrID.SPECIAL_CONDITIONS)),
            {"Poisoned", "Burned"},
        )
        self.assertEqual(attacker.get_attribute(AttrID.SPECIAL_CONDITIONS), ["Confused"])

    async def test_blocked_by_effect_shield_but_damage_still_applies(self):
        attacker = self.add_to("activePokemonArea", POISON_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", SHIELDED_DEFENDER, P2)

        await resolve_attack(self.session, P1, attacker, POISON_ATTACK, POISON_ATTACK.ability_id)

        self.assertEqual(defender.get_attribute(AttrID.HP), 90)  # damage isn't an effect
        self.assertNotIn("Poisoned", defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


# ----------------------------------------------------------------------
# T8: Effects clear when a Pokemon leaves the Active spot / play
# ----------------------------------------------------------------------

class TestRetreatClearsEffects(TriggerTestBase):
    async def test_retreat_clears_conditions_and_broadcasts(self):
        active = self.add_to("activePokemonArea", BASIC, P1)
        bench = self.add_to("bench", BASIC, P1)
        # Asleep/Paralyzed would themselves block the retreat OFFER (legal_actions'
        # immobilization gate, tested elsewhere) -- build the entry directly to
        # exercise the executor's cleanup regardless of the condition applied.
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned", "Asleep"])
        self.session.poison_counters[active.entity_id] = 2
        self.session.sleep_checkup_coins[active.entity_id] = 2

        entry = {"targetInfoLst": [
            {"name": SelectionKind.RETREAT_NEW_ACTIVE.value, "validTargets": [bench.entity_id]},
        ]}
        await self.session._execute_retreat(P1, active, entry, [bench.entity_id])

        self.assertEqual(active.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(active.entity_id, self.session.poison_counters)
        self.assertNotIn(active.entity_id, self.session.sleep_checkup_coins)
        cure_brackets = self.brackets(self.client1, GameSequence.REMOVE_SPECIAL_CONDITION.value)
        self.assertEqual(len(cure_brackets), 1)
        self.assertEqual([m["name"] for m in cure_brackets[0]],
                         ["EntityIDDataEffect", "AttributeModified"])

    async def test_locked_attack_survives_retreat_and_repromotion(self):
        attacker = self.add_to("activePokemonArea", LOCK_ATTACKER, P1)
        bench = self.add_to("bench", BASIC, P1)
        self.session.turn_state.lock_attack(attacker.entity_id, LOCK_ATTACK.ability_id)
        self.assertTrue(self.session.turn_state.attack_locked(attacker.entity_id, LOCK_ATTACK.ability_id))

        entries = compute_legal_actions(self.board, self.session.turn_state, P1, self.session.game_id)
        entry = next(e for e in entries if e["selectableAction"]["description"] == ACTION_RETREAT)
        await self.session._execute_retreat(P1, attacker, entry, [bench.entity_id])

        self.assertFalse(self.session.turn_state.attack_locked(attacker.entity_id, LOCK_ATTACK.ability_id))


class TestSwitchActiveClearsEffects(TriggerTestBase):
    async def test_switch_active_drops_attack_locks_and_still_cures(self):
        old_active = self.add_to("activePokemonArea", PLAIN, P1)
        new_active = self.add_to("bench", BASIC, P1)
        old_active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Asleep"])
        self.session.sleep_checkup_coins[old_active.entity_id] = 2
        self.session.turn_state.lock_attack(old_active.entity_id, "some-ability-id")

        ctx = EffectContext(self.session, P1, old_active, None)
        result = await ctx.switch_active(P1, new_active)

        self.assertTrue(result)
        self.assertEqual(old_active.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(old_active.entity_id, self.session.sleep_checkup_coins)
        self.assertFalse(self.session.turn_state.attack_locked(old_active.entity_id, "some-ability-id"))
        # Choreography is unchanged: the cure rides ctx._messages same as before.
        names = [m["name"] for _, m, bracket in ctx._messages
                 if bracket == GameSequence.REMOVE_SPECIAL_CONDITION.value]
        self.assertEqual(names, ["EntityIDDataEffect", "AttributeModified"])


class TestLeavePlayClearsEffects(TriggerTestBase):
    async def test_shuffle_into_deck_clears_state_silently(self):
        pokemon = self.add_to("bench", PLAIN, P1)
        pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned"])
        self.session.poison_counters[pokemon.entity_id] = 3
        ctx = EffectContext(self.session, P1, pokemon, None)

        await ctx.shuffle_into_deck([pokemon], P1)

        self.assertEqual(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(pokemon.entity_id, self.session.poison_counters)
        cure_msgs = [m for _, m, bracket in ctx._messages
                     if bracket == GameSequence.REMOVE_SPECIAL_CONDITION.value]
        self.assertEqual(cure_msgs, [])


if __name__ == "__main__":
    unittest.main()
