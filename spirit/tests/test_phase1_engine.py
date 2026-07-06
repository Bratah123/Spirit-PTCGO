"""Unit tests for the Phase 1 engine prerequisites (spirit/game/session/
passives.py, effects.py, legal_actions.py, game_session.py) needed by the
Mew VMAX deck: turn-scoped damage modifiers, ability locks, knockout
destinations, coin flips, deck peek/bottom, effect-immune damage, tool-
granted abilities, and damage-counter placement."""

import unittest
from unittest.mock import AsyncMock, patch

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import (
    Ability,
    Activations,
    Attack,
    EnergyCardDef,
    PokemonCardDef,
    PokemonToolCardDef,
    StadiumCardDef,
    Triggers,
    has_rule_box,
    unimplemented,
)
from spirit.game.models.board import BoardState, create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.effects import EffectContext, resolve_attack, resolve_on_play_ability
from spirit.game.session.game_session import GameSession
from spirit.game.card_effects.pokemon import fusion_strike_bench_attacks
from spirit.game.session.legal_actions import (
    ACTION_USE_ABILITY,
    ACTION_USE_ATTACK,
    KIND_CAKE_ATTACK_CHOICE,
    TurnState,
    _attack_entries,
    compute_legal_actions,
    copy_attack_choice_node,
)
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    ability_locked,
    active_passives,
    compute_damage,
)
from spirit.network.message_names import OutboundMsg

P1 = "player-1"
P2 = "player-2"
GAME_ID = "test-game"


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


# ----------------------------------------------------------------------
# Shared card fixtures
# ----------------------------------------------------------------------

FUSION_ATTACKER_DEF = PokemonCardDef(
    guid="10000000-0000-0000-0000-0000000000a1",
    key="TST", name="com.test.pokemon.FusionAttacker.Name",
    collector_number=1, set_code="TST", rarity=1,
    hp=120, elements=[PokemonTypes.COLORLESS],
    subtypes=["Fusion Strike"],
    abilities=[Attack("Poke Punch", cost={PokemonTypes.COLORLESS: 1}, damage=10)],
)
FUSION_ATTACKER = make_card(FUSION_ATTACKER_DEF)
FUSION_VANILLA_ATTACK = FUSION_ATTACKER_DEF.abilities[0]

PLAIN_ATTACKER_DEF = PokemonCardDef(
    guid="10000000-0000-0000-0000-0000000000a2",
    key="TST", name="com.test.pokemon.PlainAttacker.Name",
    collector_number=2, set_code="TST", rarity=1,
    hp=90, elements=[PokemonTypes.COLORLESS],
    abilities=[Attack("Tackle", cost={PokemonTypes.COLORLESS: 1}, damage=10)],
)
PLAIN_ATTACKER = make_card(PLAIN_ATTACKER_DEF)
PLAIN_VANILLA_ATTACK = PLAIN_ATTACKER_DEF.abilities[0]

PLAIN_DEFENDER_DEF = PokemonCardDef(
    guid="10000000-0000-0000-0000-0000000000d1",
    key="TST", name="com.test.pokemon.PlainDefender.Name",
    collector_number=3, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS],
)
PLAIN_DEFENDER = make_card(PLAIN_DEFENDER_DEF)

BENCH_DEFENDER_DEF = PokemonCardDef(
    guid="10000000-0000-0000-0000-0000000000d2",
    key="TST", name="com.test.pokemon.BenchDefender.Name",
    collector_number=4, set_code="TST", rarity=1,
    hp=100, elements=[PokemonTypes.COLORLESS],
)
BENCH_DEFENDER = make_card(BENCH_DEFENDER_DEF)


# ----------------------------------------------------------------------
# Shared duck-typed GameSession stub (mirrors test_effects.FakeSession, plus
# delegates resolve_knockouts/refresh_granted_abilities to the REAL
# GameSession implementation so E6/E10 exercise production code).
# ----------------------------------------------------------------------

class FakePlayer:
    def __init__(self, name):
        self.screen_name = name


class FakeSession:
    def __init__(self, board):
        self.board_state = board
        self.game_id = GAME_ID
        self.players = {P1: FakePlayer("P1"), P2: FakePlayer("P2")}
        self.turn_state = TurnState()
        self._turn_visualizations = {}
        self.sleep_checkup_coins = {}
        self.poison_counters = {}
        self.paralyzed_since = {}
        self.sent = []
        self.broadcasts = []
        self.prompts = []
        self.choice_replies = []
        self.chooser_calls = []
        self.chooser_replies = []
        self.damage_counter_calls = []
        self.damage_counter_replies = []
        self.attack_sources = None
        self.prize_awards = []
        self.promotions = []
        self.game_over = None
        self.game_stats = {P1: {}, P2: {}}
        self.mvp_damage = {P1: {}, P2: {}}

    def credit_card_damage(self, player_id, entity, amount):
        guid = getattr(entity, "archetype_id", None)
        if not guid or amount <= 0:
            return
        entry = self.mvp_damage.setdefault(player_id, {}).setdefault(guid, [0, ""])
        entry[0] += amount

    def stat_add(self, player_id, key, amount=1):
        stats = self.game_stats.setdefault(player_id, {})
        stats[key] = stats.get(key, 0) + amount

    def stat_max(self, player_id, key, value):
        stats = self.game_stats.setdefault(player_id, {})
        if value > stats.get(key, 0):
            stats[key] = value

    def _opponent_id(self, player_id):
        return P2 if player_id == P1 else P1

    @staticmethod
    def _build_msg(name, value):
        return {"name": name, "value": value}

    def _sequence_envelope(self, sequence_id, msg):
        return {"sequenceID": sequence_id, "gameID": self.game_id, "msg": msg}

    async def broadcast_packet(self, name, value, flags=0):
        self.broadcasts.append((name, value))

    def _entity_introduced_msg(self, card):
        return self._build_msg(OutboundMsg.ENTITY_INTRODUCED.value, {
            "gameID": self.game_id,
            "entityID": card.entity_id,
            "entityName": card.get_entity_name(),
            "attributeMap": card.serialize_attributes(),
        })

    def _entity_moved_msg(self, entity_id, destination_id, position):
        return self._build_msg(OutboundMsg.ENTITY_MOVED.value, {
            "gameID": self.game_id,
            "entityID": entity_id,
            "destinationID": destination_id,
            "positionInParent": position,
            "animDuration": 300,
        })

    def _reveal_card_msg(self, entity_id, return_to_origin):
        return self._build_msg(OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value, {
            "gameID": self.game_id,
            "entityID": entity_id,
            "Return": return_to_origin,
            "alwaysReveal": False,
        })

    def _entity_id_data_effect_msg(self, key, entity_id):
        return self._build_msg(OutboundMsg.ENTITY_ID_DATA_EFFECT.value, {
            "gameID": self.game_id, "key": key, "value": entity_id,
        })

    def _condition_attr_msg(self, pokemon):
        conditions = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        return self._build_msg(OutboundMsg.ATTRIBUTE_MODIFIED.value, {
            "gameID": self.game_id,
            "entityID": pokemon.entity_id,
            "attribute": {
                "name": AttrID.SPECIAL_CONDITIONS.value,
                "value": conditions,
                "originalValue": conditions,
                "modValue": None,
            },
        })

    async def send_game_sequence(self, players, name, inner_messages):
        viewer_ids = [pid for pid, p in self.players.items() if p in players]
        self.sent.append((viewer_ids, getattr(name, "value", name), list(inner_messages)))

    async def prompt_player_choice(self, player_id, prompt, buttons, sort_type=""):
        self.prompts.append((player_id, prompt, buttons))
        return self.choice_replies.pop(0) if self.choice_replies else 0

    async def prompt_choice_panel(self, player_id, source, options,
                                  prompt=None, descriptions=None):
        self.prompts.append((player_id, prompt, options))
        return self.choice_replies.pop(0) if self.choice_replies else 0

    async def prompt_attack_selection(self, player_id, source, candidates, prompt=""):
        labels = [attack.title for _pokemon, attack in candidates]
        self.prompts.append((player_id, prompt, labels))
        if not candidates:
            return None
        return self.choice_replies.pop(0) if self.choice_replies else 0

    async def prompt_card_chooser(self, player_id, source_entity_id, cards,
                                  count, minimum=None, prompt="", ordered=False,
                                  display_cards=None, slot_prompt=""):
        ids = [c.entity_id for c in cards]
        self.chooser_calls.append((player_id, ids, count, minimum, prompt))
        if self.chooser_replies:
            return [i for i in self.chooser_replies.pop(0) if i in ids][:count]
        return ids[:count]

    async def prompt_entity_picker(self, player_id, source_entity_id, cards,
                                   count, minimum=None, prompt=""):
        return await self.prompt_card_chooser(
            player_id, source_entity_id, cards, count, minimum, prompt
        )

    async def prompt_card_chooser_groups(self, player_id, source_entity_id,
                                         groups, prompt="", display_cards=None,
                                         total=None, any_of=False):
        picked = []
        for group in groups:
            picked.append(await self.prompt_card_chooser(
                player_id, source_entity_id, group["cards"], group["count"],
                group.get("minimum", 0), prompt,
            ))
        return picked

    async def prompt_damage_counter_placement(self, player_id, source_entity_id,
                                              candidates, count,
                                              amount_per_click=10, prompt=""):
        ids = [c.entity_id for c in candidates]
        self.damage_counter_calls.append((player_id, ids, count, prompt))
        if self.damage_counter_replies:
            return self.damage_counter_replies.pop(0)
        return {ids[0]: count} if ids else {}

    async def _broadcast_attack_sources(self, entity_ids):
        self.attack_sources = entity_ids

    async def _take_prizes(self, player_id, count):
        self.prize_awards.append((player_id, count))

    async def _promote_new_active(self, player_id):
        self.promotions.append(player_id)
        return True

    async def end_game(self, winner_id, reason):
        self.game_over = (winner_id, reason)

    # Delegate to the REAL GameSession implementations so these tests
    # exercise production code, not a hand-rolled mirror.
    async def resolve_knockouts(self, ctx, _ko_depth=0):
        await GameSession.resolve_knockouts(self, ctx, _ko_depth=_ko_depth)

    def clear_condition_state(self, entity_id):
        GameSession.clear_condition_state(self, entity_id)

    def clear_pokemon_effects(self, pokemon):
        return GameSession.clear_pokemon_effects(self, pokemon)

    def reset_pokemon_damage(self, pokemon):
        return GameSession.reset_pokemon_damage(self, pokemon)

    def reset_ability_usage(self, pokemon):
        return GameSession.reset_ability_usage(self, pokemon)

    def _pie_ability_entries(self, pokemon):
        return GameSession._pie_ability_entries(self, pokemon)

    async def refresh_granted_abilities(self, pokemon):
        await GameSession.refresh_granted_abilities(self, pokemon)

    async def _broadcast_entity_attribute(self, entity, attr, value):
        await GameSession._broadcast_entity_attribute(self, entity, attr, value)

    def _clear_entity_visualizations_msg(self, entity):
        return GameSession._clear_entity_visualizations_msg(self, entity)

    async def add_turn_stat_visualization(self, pokemon, arrow, display_type,
                                          source_name, card_text=None):
        await GameSession.add_turn_stat_visualization(
            self, pokemon, arrow, display_type, source_name, card_text
        )


class EngineTestBase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.board = BoardState(GAME_ID, [P1, P2])
        self.session = FakeSession(self.board)
        self.board.turn_state = self.session.turn_state

    def add_to(self, area_name, card, player_id):
        entity = create_card_entity(card, owning_player_id=player_id)
        area = self.board.find_player_area(player_id, area_name)
        self.board.add_card_to_area(entity, area)
        return entity

    def brackets(self, name):
        return [s for s in self.session.sent if s[1] == name]


# ----------------------------------------------------------------------
# E1: TurnState reference on BoardState
# ----------------------------------------------------------------------

class TestTurnStateReference(unittest.TestCase):
    def test_default_is_none_and_neutral_in_compute_damage(self):
        board = BoardState(GAME_ID, [P1, P2])
        self.assertIsNone(board.turn_state)
        attacker = create_card_entity(PLAIN_ATTACKER, owning_player_id=P1)
        target = create_card_entity(PLAIN_DEFENDER, owning_player_id=P2)
        board.find_player_area(P1, "activePokemonArea").add_child(attacker)
        board.find_player_area(P2, "activePokemonArea").add_child(target)
        # No turn_state at all: modifiers loop must not crash.
        calc = compute_damage(board, attacker, target, 10)
        self.assertEqual(calc.amount, 10)


# ----------------------------------------------------------------------
# E3: Turn-scoped damage modifiers (Power Tablet)
# ----------------------------------------------------------------------

class TestTurnDamageModifier(EngineTestBase):
    def test_modifier_applies_only_to_matching_subtype_owner_and_active(self):
        attacker = self.add_to("activePokemonArea", FUSION_ATTACKER, P1)
        active_target = self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)
        bench_target = self.add_to("bench", BENCH_DEFENDER, P2)
        self.board.turn_state.damage_modifiers.append(
            TurnDamageModifier(amount=30, player_id=P1, requires_subtype="Fusion Strike")
        )

        # Matching owner + subtype + opponent's Active: +30.
        self.assertEqual(
            compute_damage(self.board, attacker, active_target, 10).amount, 40
        )
        # Not versus the Active (opposing_active_only default True): no bonus.
        self.assertEqual(
            compute_damage(self.board, attacker, bench_target, 10,
                           apply_modifiers=False).amount,
            10,
        )

    def test_modifier_ignores_non_matching_subtype(self):
        attacker = self.add_to("activePokemonArea", PLAIN_ATTACKER, P1)
        target = self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)
        self.board.turn_state.damage_modifiers.append(
            TurnDamageModifier(amount=30, player_id=P1, requires_subtype="Fusion Strike")
        )
        self.assertEqual(compute_damage(self.board, attacker, target, 10).amount, 10)

    def test_modifier_ignores_other_players_attackers(self):
        attacker = self.add_to("activePokemonArea", FUSION_ATTACKER, P2)
        target = self.add_to("activePokemonArea", PLAIN_DEFENDER, P1)
        self.board.turn_state.damage_modifiers.append(
            TurnDamageModifier(amount=30, player_id=P1, requires_subtype="Fusion Strike")
        )
        self.assertEqual(compute_damage(self.board, attacker, target, 10).amount, 10)

    def test_cleared_by_begin_turn(self):
        self.board.turn_state.damage_modifiers.append(
            TurnDamageModifier(amount=30, player_id=P1)
        )
        self.board.turn_state.begin_turn(P1)
        self.assertEqual(self.board.turn_state.damage_modifiers, [])

    async def test_ctx_add_turn_damage_modifier_helper(self):
        attacker = self.add_to("activePokemonArea", FUSION_ATTACKER, P1)
        ctx = EffectContext(self.session, P1, attacker, FUSION_VANILLA_ATTACK)
        mod = TurnDamageModifier(amount=15, player_id=P1)
        ctx.add_turn_damage_modifier(mod)
        self.assertIn(mod, self.session.turn_state.damage_modifiers)


# ----------------------------------------------------------------------
# E4 + E5: Stadium passives & ability lock (Path to the Peak)
# ----------------------------------------------------------------------

class _PathToThePeakPassive(Passive):
    """Test-local stand-in: turns off Abilities of any Rule Box Pokemon."""
    def blocks_abilities(self, pokemon, carrier) -> bool:
        return has_rule_box(pokemon.archetype_id)


class _InertToolPassive(Passive):
    """Marker passive with no active hooks, just to prove survival."""


class _InertAbilityPassive(Passive):
    """Marker passive (e.g. a Poke-Body) riding the V's own ability slot."""


async def _dummy_ability_effect(ctx):
    pass


V_ABILITY = Ability(
    "Star Alchemy", "text",
    activation=Activations.ONCE_PER_TURN, effect=_dummy_ability_effect,
    passive=_InertAbilityPassive(),
)

V_POKEMON_DEF = PokemonCardDef(
    guid="10000000-0000-0000-0000-0000000000a3",
    key="TST", name="com.test.pokemon.RuleBoxV.Name",
    collector_number=5, set_code="TST", rarity=1,
    hp=200, elements=[PokemonTypes.COLORLESS], subtypes=["V"],
    abilities=[V_ABILITY],
)
V_POKEMON = make_card(V_POKEMON_DEF)

INERT_TOOL_DEF = PokemonToolCardDef(
    passive=_InertToolPassive(),
    guid="10000000-0000-0000-0000-0000000000e3",
    key="TST", name="com.test.trainer.InertTool.Name",
    collector_number=6, set_code="TST", rarity=0,
)
INERT_TOOL = make_card(INERT_TOOL_DEF)

PATH_TO_THE_PEAK_DEF = StadiumCardDef(
    passive=_PathToThePeakPassive(),
    guid="10000000-0000-0000-0000-0000000000f1",
    key="TST", name="com.test.trainer.PathToThePeak.Name",
    collector_number=7, set_code="TST", rarity=0,
)
PATH_TO_THE_PEAK = make_card(PATH_TO_THE_PEAK_DEF)


class TestStadiumPassiveAndAbilityLock(EngineTestBase):
    def _setup_v_with_tool(self):
        v_pokemon = self.add_to("bench", V_POKEMON, P1)
        tool = self.add_to("discard", INERT_TOOL, P1)
        self.board.attach_card(tool.entity_id, v_pokemon.entity_id)
        return v_pokemon, tool

    def test_ability_and_tool_passives_active_without_stadium(self):
        v_pokemon, tool = self._setup_v_with_tool()
        pairs = active_passives(self.board)
        carriers = [c for _, c in pairs]
        self.assertIn(v_pokemon, carriers)
        self.assertIn(tool, carriers)
        self.assertFalse(ability_locked(self.board, v_pokemon))

    def test_stadium_locks_ability_but_tool_survives(self):
        v_pokemon, tool = self._setup_v_with_tool()
        stadium_area = self.board.find_global_area("activeStadium")
        stadium = create_card_entity(PATH_TO_THE_PEAK, owning_player_id=P2)
        self.board.add_card_to_area(stadium, stadium_area)

        self.assertTrue(ability_locked(self.board, v_pokemon))
        pairs = active_passives(self.board)
        carriers = [c for _, c in pairs]
        self.assertNotIn(v_pokemon, carriers)  # ability passive excluded
        self.assertIn(tool, carriers)          # tool passive survives
        self.assertIn(stadium, carriers)       # stadium's own passive counts

    def test_stadium_lock_gates_legal_action_offer(self):
        v_pokemon, _ = self._setup_v_with_tool()
        state = TurnState()
        state.turn_number = 3
        entries = compute_legal_actions(self.board, state, P1, GAME_ID)
        self.assertTrue(any(
            e["selectableAction"]["actionID"] == V_ABILITY.ability_id
            for e in entries
        ))

        stadium_area = self.board.find_global_area("activeStadium")
        stadium = create_card_entity(PATH_TO_THE_PEAK, owning_player_id=P2)
        self.board.add_card_to_area(stadium, stadium_area)
        entries = compute_legal_actions(self.board, state, P1, GAME_ID)
        self.assertFalse(any(
            e["selectableAction"]["actionID"] == V_ABILITY.ability_id
            for e in entries
        ))

    def test_lock_off_after_stadium_discarded(self):
        v_pokemon, _ = self._setup_v_with_tool()
        stadium_area = self.board.find_global_area("activeStadium")
        stadium = create_card_entity(PATH_TO_THE_PEAK, owning_player_id=P2)
        self.board.add_card_to_area(stadium, stadium_area)
        self.assertTrue(ability_locked(self.board, v_pokemon))

        discard = self.board.find_player_area(P2, "discard")
        self.board.move_card(stadium.entity_id, discard.entity_id)
        self.assertFalse(ability_locked(self.board, v_pokemon))

    async def test_resolve_on_play_ability_returns_early_when_locked(self):
        stadium_area = self.board.find_global_area("activeStadium")
        stadium = create_card_entity(PATH_TO_THE_PEAK, owning_player_id=P2)
        self.board.add_card_to_area(stadium, stadium_area)
        v_pokemon = self.add_to("bench", V_POKEMON, P1)

        called = False

        async def marker_effect(ctx):
            nonlocal called
            called = True

        locked_ability = Ability(
            "Locked On-Play", "text", trigger=Triggers.ON_PLAY, effect=marker_effect,
        )
        await resolve_on_play_ability(self.session, P1, v_pokemon, locked_ability)
        self.assertFalse(called)


# ----------------------------------------------------------------------
# E6: Knockout destination (Lost City)
# ----------------------------------------------------------------------

class _LostCityPassive(Passive):
    def knockout_destination(self, pokemon, carrier):
        return "lostZone"


LOST_CITY_DEF = StadiumCardDef(
    passive=_LostCityPassive(),
    guid="10000000-0000-0000-0000-0000000000f2",
    key="TST", name="com.test.trainer.LostCity.Name",
    collector_number=8, set_code="TST", rarity=0,
)
LOST_CITY = make_card(LOST_CITY_DEF)

TEST_ENERGY_DEF = EnergyCardDef(
    guid="10000000-0000-0000-0000-0000000000e2",
    key="TST", name="com.test.energy.Plain.Name",
    collector_number=900, set_code="TST", rarity=0,
    energy_type=PokemonTypes.COLORLESS,
)
TEST_ENERGY = make_card(TEST_ENERGY_DEF)


class TestKnockoutDestination(EngineTestBase):
    async def test_pokemon_stack_to_lost_zone_energy_to_discard(self):
        stadium_area = self.board.find_global_area("activeStadium")
        stadium = create_card_entity(LOST_CITY, owning_player_id=P1)
        self.board.add_card_to_area(stadium, stadium_area)

        # Benched (not Active) so promotion/prize logic no-ops cleanly.
        pokemon = self.add_to("bench", PLAIN_DEFENDER, P2)
        pre_evo = self.add_to("discard", PLAIN_DEFENDER, P2)
        self.board.attach_card(pre_evo.entity_id, pokemon.entity_id)
        energy = self.add_to("discard", TEST_ENERGY, P2)
        self.board.attach_card(energy.entity_id, pokemon.entity_id)

        ctx = EffectContext(self.session, P1, pokemon, None)
        ctx.knockouts.append(pokemon)
        await self.session.resolve_knockouts(ctx)

        lost_zone = self.board.find_player_area(P2, "lostZone")
        discard = self.board.find_player_area(P2, "discard")
        self.assertIn(pokemon, lost_zone.children)
        self.assertIn(pre_evo, lost_zone.children)
        self.assertIn(energy, discard.children)
        self.assertEqual(self.session.prize_awards, [(P1, 1)])
        self.assertEqual(self.session.promotions, [])


# ----------------------------------------------------------------------
# E7: ctx.use_attack (Cross Fusion)
# ----------------------------------------------------------------------

BORROWED_ATTACK = Attack(
    "Borrowed Blast", cost={PokemonTypes.COLORLESS: 2}, damage=50,
    locks_next_turn=True,
)
BORROWED_ATTACK.ability_id = "10000000-0000-0000-0000-0000000000ab"


async def _cross_fusion_effect(ctx):
    await ctx.use_attack(BORROWED_ATTACK)


CROSS_FUSION_ATTACK = Attack("Cross Fusion", cost={PokemonTypes.COLORLESS: 1},
                             effect=_cross_fusion_effect)
CROSS_FUSION_ATTACK.ability_id = "10000000-0000-0000-0000-0000000000ac"


class TestUseAttack(EngineTestBase):
    async def test_resolves_borrowed_damage_and_locks_attacker(self):
        attacker = self.add_to("activePokemonArea", PLAIN_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)

        await resolve_attack(self.session, P1, attacker, CROSS_FUSION_ATTACK,
                             CROSS_FUSION_ATTACK.ability_id)

        self.assertEqual(defender.get_attribute(AttrID.HP), 50)  # 100 - 50
        self.assertTrue(
            self.session.turn_state.attack_locked(
                attacker.entity_id, BORROWED_ATTACK.ability_id
            )
        )
        # The outer bracket's title/actionID stay the USER attack's (captured
        # before the effect ran and swapped ctx.ability).
        attack_brackets = [s for s in self.session.sent if s[1] == "Attack"]
        head = attack_brackets[0][2][0]
        self.assertEqual(head["value"]["abilityID"], CROSS_FUSION_ATTACK.ability_id)
        self.assertEqual(head["value"]["abilityTitle"], {"id": "Cross Fusion"})


# ----------------------------------------------------------------------
# E8: Deck peek / bottom-of-deck
# ----------------------------------------------------------------------

class TestDeckPeekAndBottom(EngineTestBase):
    def test_deck_top_returns_topmost_first(self):
        card1 = self.add_to("deck", PLAIN_DEFENDER, P1)
        card2 = self.add_to("deck", BENCH_DEFENDER, P1)
        card3 = self.add_to("deck", PLAIN_ATTACKER, P1)
        ctx = EffectContext(self.session, P1, card1, None)

        self.assertEqual(ctx.deck_top(1), [card3])
        self.assertEqual(ctx.deck_top(2), [card3, card2])
        self.assertEqual(ctx.deck_top(3), [card3, card2, card1])

    async def test_put_on_bottom_of_deck(self):
        self.add_to("deck", PLAIN_DEFENDER, P1)
        card = self.add_to("hand", BENCH_DEFENDER, P1)
        ctx = EffectContext(self.session, P1, card, None)

        result = await ctx.put_on_bottom_of_deck(card)

        self.assertTrue(result)
        deck = self.board.find_player_area(P1, "deck")
        self.assertEqual(deck.children[0], card)
        moves = [m for _, m, bracket in ctx._messages if bracket == "GroupedMove"]
        self.assertEqual(moves[0]["value"]["positionInParent"], 0)
        self.assertEqual(moves[0]["value"]["entityID"], card.entity_id)


# ----------------------------------------------------------------------
# E9: Effect-immune damage (Max Miracle)
# ----------------------------------------------------------------------

class _AlwaysPreventsPassive(Passive):
    def prevents_damage(self, calc, carrier) -> bool:
        return True


class _AttackerBoostPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        calc.amount += 20


ATTACKER_TOOL_DEF = PokemonToolCardDef(
    passive=_AttackerBoostPassive(),
    guid="10000000-0000-0000-0000-0000000000e4",
    key="TST", name="com.test.trainer.AttackerBoost.Name",
    collector_number=9, set_code="TST", rarity=0,
)
ATTACKER_TOOL = make_card(ATTACKER_TOOL_DEF)

TARGET_SHIELD_TOOL_DEF = PokemonToolCardDef(
    passive=_AlwaysPreventsPassive(),
    guid="10000000-0000-0000-0000-0000000000e5",
    key="TST", name="com.test.trainer.TargetShield.Name",
    collector_number=10, set_code="TST", rarity=0,
)
TARGET_SHIELD_TOOL = make_card(TARGET_SHIELD_TOOL_DEF)


class TestIgnoreTargetEffects(EngineTestBase):
    def test_ignore_target_effects_skips_target_side_prevention_only(self):
        attacker = self.add_to("activePokemonArea", PLAIN_ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)
        atk_tool = self.add_to("discard", ATTACKER_TOOL, P1)
        self.board.attach_card(atk_tool.entity_id, attacker.entity_id)
        shield_tool = self.add_to("discard", TARGET_SHIELD_TOOL, P2)
        self.board.attach_card(shield_tool.entity_id, defender.entity_id)

        # Without the flag: the target's shield prevents the hit entirely.
        blocked = compute_damage(self.board, attacker, defender, 10)
        self.assertTrue(blocked.prevented)
        self.assertEqual(blocked.amount, 0)

        # With it: attacker-side boost still applies, target shield skipped.
        calc = compute_damage(self.board, attacker, defender, 10,
                              ignore_target_effects=True)
        self.assertFalse(calc.prevented)
        self.assertEqual(calc.amount, 30)


# ----------------------------------------------------------------------
# E10: Tool-granted abilities (Forest Seal Stone)
# ----------------------------------------------------------------------

HOLDER_POKEMON_DEF = PokemonCardDef(
    guid="10000000-0000-0000-0000-0000000000a4",
    key="TST", name="com.test.pokemon.ToolHolder.Name",
    collector_number=11, set_code="TST", rarity=1,
    hp=150, elements=[PokemonTypes.COLORLESS],
)
HOLDER_POKEMON = make_card(HOLDER_POKEMON_DEF)


async def _granted_effect(ctx):
    pass


FOREST_SEAL_STONE_DEF = PokemonToolCardDef(
    granted_abilities=[
        Ability("Star Alchemy", "text", activation=Activations.ONCE_PER_TURN,
                effect=_granted_effect),
    ],
    guid="10000000-0000-0000-0000-0000000000e6",
    key="TST", name="com.test.trainer.ForestSealStone.Name",
    collector_number=12, set_code="TST", rarity=0,
)
FOREST_SEAL_STONE = make_card(FOREST_SEAL_STONE_DEF)


class TestGrantedAbilities(EngineTestBase):
    async def test_attach_grants_and_discard_revokes(self):
        pokemon = self.add_to("bench", HOLDER_POKEMON, P1)
        tool = self.add_to("discard", FOREST_SEAL_STONE, P1)
        self.board.attach_card(tool.entity_id, pokemon.entity_id)

        await self.session.refresh_granted_abilities(pokemon)
        entries = pokemon.get_attribute(AttrID.PIE_ABILITIES)
        self.assertEqual(len(entries), 1)
        self.assertEqual(
            entries[0]["abilityID"],
            FOREST_SEAL_STONE_DEF.granted_abilities[0].ability_id,
        )

        ctx = EffectContext(self.session, P1, pokemon, None)
        await ctx.discard_cards([tool])

        entries_after = pokemon.get_attribute(AttrID.PIE_ABILITIES)
        self.assertEqual(entries_after, [])
        discard = self.board.find_player_area(P1, "discard")
        self.assertIn(tool, discard.children)


# ----------------------------------------------------------------------
# E2: ctx.flip_coins
# ----------------------------------------------------------------------

class TestFlipCoins(EngineTestBase):
    async def test_ability_context_queues_inline_and_tallies_stats(self):
        attacker = self.add_to("activePokemonArea", PLAIN_ATTACKER, P1)
        ctx = EffectContext(self.session, P1, attacker, PLAIN_VANILLA_ATTACK)

        with patch("spirit.game.session.effects.random.choice", side_effect=[0, 1, 0]):
            results = await ctx.flip_coins(3, title="Coin Check")

        self.assertEqual(results, [True, False, True])
        self.assertEqual(self.session.game_stats[P1]["headsflipped"], 2)
        self.assertEqual(self.session.game_stats[P1]["tailsflipped"], 1)
        # Ability context: queued inline (bracket=None), never sent directly.
        self.assertEqual(len(ctx._messages), 1)
        vid, msg, bracket = ctx._messages[0]
        self.assertIsNone(bracket)
        self.assertEqual(msg["value"]["resultLst"], [0, 1, 0])
        self.assertEqual(msg["value"]["title"], {"id": "Coin Check"})
        self.assertEqual(self.session.sent, [])

    async def test_trainer_context_sends_immediately_with_source_name_fallback(self):
        card = self.add_to("hand", PLAIN_DEFENDER, P1)
        ctx = EffectContext(self.session, P1, card, None)

        with patch("spirit.game.session.effects.random.choice", side_effect=[1, 1]), \
             patch("spirit.game.session.effects.asyncio.sleep", new=AsyncMock()) as mock_sleep:
            results = await ctx.flip_coins(2)

        self.assertEqual(results, [False, False])
        mock_sleep.assert_awaited_once()
        flip_brackets = self.brackets("PokeAbility")
        self.assertEqual(len(flip_brackets), 1)
        value = flip_brackets[0][2][0]["value"]
        self.assertEqual(value["resultLst"], [1, 1])
        self.assertEqual(value["title"], {"id": "com.test.pokemon.PlainDefender.Name"})


# ----------------------------------------------------------------------
# E11: Damage-counter placement (Glistening Droplets)
# ----------------------------------------------------------------------

class TestPlaceDamageCounters(EngineTestBase):
    async def test_single_offer_distributes_counters_per_scripted_placement(self):
        source = self.add_to("activePokemonArea", PLAIN_ATTACKER, P1)
        active = self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)
        benched = self.add_to("bench", BENCH_DEFENDER, P2)
        ctx = EffectContext(self.session, P1, source, None)

        self.session.damage_counter_replies.append(
            {active.entity_id: 2, benched.entity_id: 1}
        )

        await ctx.place_damage_counters(3, candidates=[active, benched])

        self.assertEqual(len(self.session.damage_counter_calls), 1)
        call_player, call_ids, call_count, _prompt = self.session.damage_counter_calls[0]
        self.assertEqual(call_player, P1)
        self.assertEqual(set(call_ids), {active.entity_id, benched.entity_id})
        self.assertEqual(call_count, 3)
        self.assertEqual(active.get_attribute(AttrID.HP), 80)   # 100 - 20
        self.assertEqual(benched.get_attribute(AttrID.HP), 90)  # 100 - 10


# ----------------------------------------------------------------------
# E12: Copy-attack choice node (Cross Fusion Strike's forced CakeAttack pick)
# ----------------------------------------------------------------------

COPY_MASTER_DEF = PokemonCardDef(
    guid="10000000-0000-0000-0000-0000000000c1",
    key="TST", name="com.test.pokemon.CopyMaster.Name",
    collector_number=5, set_code="TST", rarity=1,
    hp=310, elements=[PokemonTypes.PSYCHIC],
    subtypes=["Fusion Strike"],
    abilities=[Attack("Cross Copy")],
)
COPY_MASTER = make_card(COPY_MASTER_DEF)
COPY_ATTACK = COPY_MASTER_DEF.abilities[0]


class TestCopyAttackChoiceNode(EngineTestBase):
    def test_choice_node_wire_shape(self):
        active = self.add_to("activePokemonArea", COPY_MASTER, P1)
        self.add_to("bench", FUSION_ATTACKER, P1)
        self.add_to("bench", PLAIN_ATTACKER, P1)  # not Fusion Strike: excluded

        candidates = fusion_strike_bench_attacks(self.board, P1)
        node = copy_attack_choice_node(
            active.entity_id, candidates, "Choose an attack."
        )

        self.assertEqual(node["name"], KIND_CAKE_ATTACK_CHOICE)
        self.assertTrue(node["selected"])
        self.assertEqual(node["targetPrompt"], {"id": "Choose an attack."})
        choices = node["choices"]
        self.assertEqual(len(choices), 1)
        self.assertEqual(choices[0]["title"], {"id": "Poke Punch"})
        self.assertTrue(choices[0]["abilityID"])
        # bonusInfo renders each choice with the OWNER's type, not the copier's.
        self.assertEqual(
            choices[0]["bonusInfo"]["originalOwnerTypes"],
            [PokemonTypes.COLORLESS.value],
        )

    def test_candidates_exclude_non_fusion_and_dedupe(self):
        self.add_to("activePokemonArea", COPY_MASTER, P1)
        fusion = self.add_to("bench", FUSION_ATTACKER, P1)
        self.add_to("bench", FUSION_ATTACKER, P1)  # duplicate: deduped
        self.add_to("bench", PLAIN_ATTACKER, P1)

        candidates = fusion_strike_bench_attacks(self.board, P1)

        self.assertEqual(candidates, [(fusion, FUSION_VANILLA_ATTACK)])

    def test_attack_entries_stay_plain(self):
        # The copy pick rides a FORCED follow-up offer, never the main-turn
        # entry's targetInfoLst (nodes under an ActionsNode are cancellable).
        self.add_to("activePokemonArea", COPY_MASTER, P1)
        self.add_to("bench", FUSION_ATTACKER, P1)
        self.session.turn_state.turn_number = 3  # attack_locked(0, ...) is True
        entries = _attack_entries(
            self.board, self.session.turn_state, P1, GAME_ID
        )
        entry = next(
            e for e in entries
            if e["selectableAction"]["actionID"] == COPY_ATTACK.ability_id
        )
        self.assertEqual(entry["targetInfoLst"], [])


if __name__ == "__main__":
    unittest.main()
