"""Functional self-tests for the engine-sprint features (sprint 1: E1/E2/E3/
E8/E10/E11/E14/E16; sprint 2: E4/E5/E6/E7/E9/E12/E13/E15/E17 + E18 minis),
with hard assertions.

Runs headless on the effect_smoke harness (SmokeSession + Rig, two AIPlayers,
no network/DB). Usage: python -m spirit.tools.engine_selftest -- exit 0 iff
every assertion passes.
"""

import asyncio
import logging
import random
import sys
import traceback
import uuid
from typing import Any, Dict

from spirit.game.attributes import (
    AttrID, PokemonStage, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.passives_common import (
    energy_attach_tax_passive,
    flip_prevent_damage_passive,
    guts_survive_passive,
    replace_opponent_supporters,
    trainer_effect_shield_passive,
)
from spirit.game.data_utils import (
    ABILITIES_BY_ID, Ability, Activations, Attack, CARD_DEFS_BY_GUID,
    TRAINER_EFFECTS_BY_GUID, Triggers, evolves_from, evolves_from_chain,
)
from spirit.game.models.board import EnergyEntity, PokemonEntity
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.session import legal_actions, passives
from spirit.game.session.constants import GamePhase, SelectionKind
from spirit.game.session.effects import (
    EffectContext,
    is_item_card,
    resolve_activated_ability,
    resolve_attack,
    resolve_trainer_effect,
)
from spirit.game.session.game_session import GameOver
from spirit.game.session.legal_actions import (
    ACTION_ATTACH_TOOL,
    ACTION_EVOLVE,
    ACTION_PLAY_ENERGY,
    ACTION_PLAY_POKEMON,
    ACTION_RETREAT,
    ACTION_USE_ABILITY,
    ACTION_USE_ATTACK,
    ACTION_USE_TRAINER,
    TurnState,
    compute_legal_actions,
)
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    compute_damage,
    carrier_pokemon,
)
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import (
    P1,
    P2,
    Rig,
    basic_energy_guids,
    pick_filler_basic,
    pick_filler_item,
)

FILLER = None
ENERGY_GUIDS: Dict[int, str] = {}
ITEM = None


# ----------------------------------------------------------------------
# Probe passives
# ----------------------------------------------------------------------

class Shield(Passive):
    def prevents_damage(self, calc, carrier):
        return carrier_pokemon(carrier) is calc.target


class NoRetreat(Passive):
    def blocks_retreat(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


class NoConditions(Passive):
    def blocks_special_conditions(self, target, condition, carrier):
        return carrier_pokemon(carrier) is target


class NoHealing(Passive):
    def prevents_healing(self, target, carrier):
        return carrier_pokemon(carrier) is target


class TripleWeakness(Passive):
    def modify_weakness(self, calc, carrier):
        calc.weakness_multiplier = 3


class GrantWeakness(Passive):
    def __init__(self, weak_type):
        self.weak_type = weak_type

    def modify_weakness(self, calc, carrier):
        calc.weak_types = [self.weak_type]


class NoResistance(Passive):
    def modify_resistance(self, calc, carrier):
        calc.resistance_applies = False


# ----------------------------------------------------------------------
# Rig helpers
# ----------------------------------------------------------------------

def new_rig():
    rig = Rig(FILLER, FILLER, ENERGY_GUIDS, ITEM)
    entities = rig.setup("pokemon")
    assert entities["p1_active"] is not None and entities["p2_active"] is not None
    return rig, entities


def attack_ctx(rig, entities, damage=50, title="Test Blast") -> EffectContext:
    return EffectContext(
        rig.session, P1, entities["p1_active"],
        Attack(title, cost={}, damage=damage),
    )


def attacker_type(entities) -> int:
    types = entities["p1_active"].get_attribute(AttrID.POKEMON_TYPES) or []
    return types[0] if types else PokemonTypes.WATER.value


def neutralize_wr(entities):
    """Strips the filler target's printed Weakness/Resistance for exact math."""
    entities["p2_active"].set_attribute(AttrID.WEAKNESS_TYPES, [])
    entities["p2_active"].set_attribute(AttrID.RESISTANCE_TYPES, -1)


def register_ability(ability) -> str:
    ability.ability_id = str(uuid.uuid4())
    ABILITIES_BY_ID[ability.ability_id] = ability
    return ability.ability_id


class forced_flips:
    """Overrides random.choice with a fixed flip run (0 = heads, 1 = tails);
    an unexpected extra flip raises StopIteration (= 'was consulted')."""

    def __init__(self, *results):
        self.results = list(results)

    def __enter__(self):
        self._orig = random.choice
        it = iter(self.results)
        random.choice = lambda seq, _it=it: next(_it)
        return self

    def __exit__(self, *exc):
        random.choice = self._orig
        return False


def action_entry(pokemon, ability_id) -> Dict[str, Any]:
    return {
        "entityID": pokemon.entity_id,
        "selectableAction": {"actionID": ability_id,
                             "description": ACTION_USE_ABILITY},
        "targetInfoLst": [],
    }


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------

async def test_temp_passive_prevents_then_expires():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state  # turn 3
    ctx = attack_ctx(rig, e)
    ctx.add_passive_through_opponents_turn(e["p2_active"], Shield())  # thru 4
    calc = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False)
    assert calc.prevented and calc.amount == 0, "shield must prevent on turn 3"
    ts.begin_turn(P2, board)  # turn 4: still within lifetime
    calc = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False)
    assert calc.prevented, "shield must survive through the opponent's turn"
    ts.begin_turn(P1, board)  # turn 5: expired
    assert board.temporary_passives == [], "expired temp passive must be pruned"
    calc = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False)
    assert not calc.prevented and calc.amount == 50


async def test_temp_passive_cleared_on_leave():
    rig, e = new_rig()
    board = rig.board
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p2_active"], Shield())  # until-leaves
    calc = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False)
    assert calc.prevented
    rig.session.clear_pokemon_effects(e["p2_active"])
    assert board.temporary_passives == [], "clear_pokemon_effects must drop it"
    calc = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False)
    assert not calc.prevented
    # A carrier that leaves play without a clear is silently skipped.
    marker = Shield()
    ctx.add_temporary_passive(e["p2_active"], marker)
    discard = board.find_player_area(P2, "discard")
    board.move_card(e["p2_active"].entity_id, discard.entity_id)
    assert all(p is not marker for p, _ in passives.active_passives(board))


async def test_turn_damage_modifier_scoping():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state  # turn 3
    ts.damage_modifiers.append(TurnDamageModifier(
        30, P1, attack_title="Test Blast",
        expires_after_turn=ts.turn_number + 1,
    ))
    boosted = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                             apply_modifiers=False, attack_title="Test Blast")
    assert boosted.amount == 80, f"title-matched boost expected 80, got {boosted.amount}"
    other = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                           apply_modifiers=False, attack_title="Other Attack")
    assert other.amount == 50, "boost must not apply to other attack titles"
    ts.begin_turn(P2, board)  # turn 4: still alive
    assert compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False,
                          attack_title="Test Blast").amount == 80
    ts.begin_turn(P1, board)  # turn 5: expired
    assert ts.damage_modifiers == []
    assert compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False,
                          attack_title="Test Blast").amount == 50
    # Legacy shape (no expiry) still clears at the next turn boundary.
    ts.damage_modifiers.append(TurnDamageModifier(30, P1))
    ts.begin_turn(P2, board)
    assert ts.damage_modifiers == []
    # source_entity_id gates the attacker.
    ts.damage_modifiers.append(TurnDamageModifier(
        30, P1, source_entity_id=e["p1_active"].entity_id,
        expires_after_turn=ts.turn_number,
    ))
    bench = [c for c in rig.board.find_player_area(P1, "bench").children]
    assert compute_damage(board, e["p1_active"], e["p2_active"], 50,
                          apply_modifiers=False).amount == 80
    assert compute_damage(board, bench[0], e["p2_active"], 50,
                          apply_modifiers=False).amount == 50


async def test_retreat_lock_blocks_then_expires():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state  # turn 3
    for _ in range(4):
        rig.attach_energy_type(P1, e["p1_active"], PokemonTypes.WATER.value)
    game_id = rig.session.game_id
    assert legal_actions._retreat_entry(board, ts, P1, game_id), \
        "retreat must be offered on the baseline board"
    ctx = attack_ctx(rig, e)
    ctx.lock_retreat(e["p1_active"])  # locked through turn 4
    assert legal_actions._retreat_entry(board, ts, P1, game_id) == []
    ts.begin_turn(P2, board)  # turn 4: still locked
    assert legal_actions._retreat_entry(board, ts, P1, game_id) == []
    ts.begin_turn(P1, board)  # turn 5: expired
    assert legal_actions._retreat_entry(board, ts, P1, game_id), \
        "retreat lock must expire after the opponent's turn"
    # clear_pokemon_effects releases an until-leaves lock.
    ctx.lock_retreat(e["p1_active"], legal_actions.LOCK_UNTIL_LEAVES_ACTIVE)
    assert legal_actions._retreat_entry(board, ts, P1, game_id) == []
    rig.session.clear_pokemon_effects(e["p1_active"])
    assert legal_actions._retreat_entry(board, ts, P1, game_id)


async def test_blocks_retreat_passive():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    for _ in range(4):
        rig.attach_energy_type(P1, e["p1_active"], PokemonTypes.WATER.value)
    game_id = rig.session.game_id
    assert legal_actions._retreat_entry(board, ts, P1, game_id)
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], NoRetreat())
    assert legal_actions._retreat_entry(board, ts, P1, game_id) == [], \
        "blocks_retreat passive must suppress the retreat offer"


async def test_history_rotation_attacks_used():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    ctx = attack_ctx(rig, e)
    await resolve_attack(rig.session, P1, e["p1_active"],
                         Attack("Test Ledger Hit", cost={}, damage=10),
                         str(uuid.uuid4()))
    assert any(t == "Test Ledger Hit" for _, _, t in ts.attacks_used), \
        "resolve_attack must record the declared attack"
    assert not ctx.attack_used_last_turn(title="Test Ledger Hit")
    ts.begin_turn(P2, board)
    assert ctx.attack_used_last_turn(title="Test Ledger Hit")
    assert ctx.attack_used_last_turn(entity=e["p1_active"])
    assert not ctx.attack_used_last_turn(title="Never Used")
    ts.begin_turn(P1, board)
    assert not ctx.attack_used_last_turn(title="Test Ledger Hit"), \
        "history older than one turn must be dropped"


async def test_damage_taken_recorded():
    rig, e = new_rig()
    ts = rig.session.turn_state
    neutralize_wr(e)
    ctx = attack_ctx(rig, e, damage=30)
    dealt = await ctx.deal_damage(30)
    assert dealt == 30
    assert ts.damage_taken.get(e["p2_active"].entity_id) == 30
    ts.begin_turn(P2, rig.board)
    assert ctx.damage_taken_last_turn(e["p2_active"]) == 30


async def test_ends_turn_plumbing():
    rig, e = new_rig()
    pokemon = e["p1_active"]

    async def _draw_one(c):
        await c.draw_cards(1)

    ability = Ability("Test Charge", activation=Activations.ONCE_PER_TURN,
                      ends_turn=True, effect=_draw_one)
    aid = register_ability(ability)
    try:
        turn_over = await rig.session._execute_use_ability(
            P1, pokemon, action_entry(pokemon, aid))
        assert turn_over is True, "ends_turn ability that ran must end the turn"
        assert (pokemon.entity_id, aid) in rig.session.turn_state.used_abilities
    finally:
        ABILITIES_BY_ID.pop(aid, None)

    async def _noop(c):
        pass

    ability = Ability("Test NoOp", activation=Activations.ONCE_PER_TURN,
                      ends_turn=True, effect=_noop)
    aid = register_ability(ability)
    try:
        turn_over = await rig.session._execute_use_ability(
            P1, pokemon, action_entry(pokemon, aid))
        assert turn_over is False, "a no-op effect must not end the turn"
    finally:
        ABILITIES_BY_ID.pop(aid, None)

    async def _flag_only(c):
        c.ends_turn = True

    ability = Ability("Test Flag", activation=Activations.ONCE_PER_TURN,
                      effect=_flag_only)
    aid = register_ability(ability)
    try:
        ctx = await resolve_activated_ability(rig.session, P1, pokemon, ability)
        assert ctx.ends_turn is True, "script-set ctx.ends_turn must survive"
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_flip_until_tails():
    rig, e = new_rig()
    for seed in (1, 7, 42):
        random.seed(seed)
        ctx = attack_ctx(rig, e)  # attack context queues inline
        heads = await ctx.flip_until_tails("Test Flips")
        flips = [m for _, m, _ in ctx._messages
                 if m.get("name", "").endswith("CoinFlipWithContextEffect")
                 or "resultLst" in (m.get("value") or {})]
        assert len(ctx._messages) == 1 and len(flips) == 1, \
            "flip_until_tails must queue exactly one coin message"
        results = flips[0]["value"]["resultLst"]
        assert results[-1] == 1, "the run must end in tails"
        assert results.count(1) == 1, "only the final flip is tails"
        assert results.count(0) == heads, "returned heads must match the run"
    # Trainer context sends immediately (nothing rides ctx._messages).
    random.seed(3)
    tctx = EffectContext(rig.session, P1, e["p1_active"], None)
    heads = await tctx.flip_until_tails("Test Flips")
    assert heads >= 0 and tctx._messages == []


async def test_ignore_resistance():
    rig, e = new_rig()
    board = rig.board
    t = attacker_type(e)
    e["p2_active"].set_attribute(AttrID.WEAKNESS_TYPES, [])
    e["p2_active"].set_attribute(AttrID.RESISTANCE_TYPES, t)
    plain = compute_damage(board, e["p1_active"], e["p2_active"], 50)
    assert plain.amount == 20 and plain.resistance_hit
    skipped = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                             ignore_resistance=True)
    assert skipped.amount == 50 and not skipped.resistance_hit
    # With weakness in the mix, only the resistance stage is skipped.
    e["p2_active"].set_attribute(AttrID.WEAKNESS_TYPES, [t])
    both = compute_damage(board, e["p1_active"], e["p2_active"], 50)
    assert both.amount == 70  # 50*2 - 30
    weak_only = compute_damage(board, e["p1_active"], e["p2_active"], 50,
                               ignore_resistance=True)
    assert weak_only.amount == 100, "weakness must still apply"
    # The modify_resistance hook path clears the same flag.
    e["p2_active"].set_attribute(AttrID.WEAKNESS_TYPES, [])
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], NoResistance())
    hooked = compute_damage(board, e["p1_active"], e["p2_active"], 50)
    assert hooked.amount == 50 and not hooked.resistance_hit


async def test_unlimited_activation():
    rig, e = new_rig()
    pokemon = e["p1_active"]
    ts = rig.session.turn_state

    async def _draw_one(c):
        await c.draw_cards(1)

    ability = Ability("Test Endless", activation=Activations.UNLIMITED,
                      effect=_draw_one)
    aid = register_ability(ability)
    try:
        await rig.session._execute_use_ability(P1, pokemon, action_entry(pokemon, aid))
        assert (pokemon.entity_id, aid) not in ts.used_abilities, \
            "UNLIMITED use must not consume the once-per-turn mark"
        pokemon.set_attribute(AttrID.PIE_ABILITIES,
                              [{"abilityID": aid, "abilityType": "PokeAbility"}])
        entries = legal_actions._ability_entries(
            rig.board, ts, P1, rig.session.game_id, [pokemon])
        assert any(en["selectableAction"]["actionID"] == aid for en in entries)
        # Even a stale used mark never suppresses an UNLIMITED offer.
        ts.used_abilities.add((pokemon.entity_id, aid))
        entries = legal_actions._ability_entries(
            rig.board, ts, P1, rig.session.game_id, [pokemon])
        assert any(en["selectableAction"]["actionID"] == aid for en in entries)
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_blocks_special_conditions():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p2_active"], NoConditions())
    assert passives.conditions_blocked(rig.board, e["p2_active"],
                                       SpecialConditions.ASLEEP)
    applied = await ctx.apply_special_condition(
        e["p2_active"], SpecialConditions.ASLEEP)
    assert applied is False
    assert not (e["p2_active"].get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    rig.board.temporary_passives = []
    applied = await ctx.apply_special_condition(
        e["p2_active"], SpecialConditions.ASLEEP)
    assert applied is True
    assert "Asleep" in (e["p2_active"].get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def test_prevents_healing():
    rig, e = new_rig()
    pokemon = e["p1_active"]
    ts = rig.session.turn_state
    pokemon.set_attribute(AttrID.HP, pokemon.get_attribute(AttrID.HP, 0) - 40)
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(pokemon, NoHealing())
    assert await ctx.heal(30, pokemon) == 0, "prevents_healing must zero the heal"
    assert pokemon.entity_id not in ts.healed_entities
    rig.board.temporary_passives = []
    assert await ctx.heal(30, pokemon) == 30
    assert pokemon.entity_id in ts.healed_entities


async def test_usable_first_turn():
    rig, e = new_rig()
    pokemon = e["p1_active"]
    ok = Attack("Test Quick", cost={}, damage=10, usable_first_turn=True)
    slow = Attack("Test Slow", cost={}, damage=10)
    ok_id, slow_id = register_ability(ok), register_ability(slow)
    try:
        pokemon.set_attribute(AttrID.PIE_ABILITIES, [
            {"abilityID": ok_id, "abilityType": "Attack", "cost": {}},
            {"abilityID": slow_id, "abilityType": "Attack", "cost": {}},
        ])
        turn1 = TurnState()
        turn1.begin_turn(P1, rig.board)  # turn 1, going first
        entries = legal_actions._attack_entries(
            rig.board, turn1, P1, rig.session.game_id)
        ids = {en["selectableAction"]["actionID"] for en in entries}
        assert ok_id in ids, "usable_first_turn attack must be offered on turn 1"
        assert slow_id not in ids, "normal attacks stay blocked on turn 1"
        # The full offer builder now reaches _attack_entries on turn 1 too.
        actions = compute_legal_actions(rig.board, turn1, P1, rig.session.game_id)
        ids = {a["selectableAction"]["actionID"] for a in actions}
        assert ok_id in ids and slow_id not in ids
        # From turn 2 on, both are offered.
        turn1.begin_turn(P2, rig.board)
        turn1.begin_turn(P1, rig.board)
        entries = legal_actions._attack_entries(
            rig.board, turn1, P1, rig.session.game_id)
        ids = {en["selectableAction"]["actionID"] for en in entries}
        assert ok_id in ids and slow_id in ids
    finally:
        ABILITIES_BY_ID.pop(ok_id, None)
        ABILITIES_BY_ID.pop(slow_id, None)


async def test_weakness_multiplier_and_types():
    rig, e = new_rig()
    board = rig.board
    t = attacker_type(e)
    e["p2_active"].set_attribute(AttrID.WEAKNESS_TYPES, [t])
    e["p2_active"].set_attribute(AttrID.RESISTANCE_TYPES, -1)
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], TripleWeakness())
    calc = compute_damage(board, e["p1_active"], e["p2_active"], 50)
    assert calc.amount == 150 and calc.weakness_hit, \
        f"weakness_multiplier=3 must triple (got {calc.amount})"
    # weak_types is hook-rewritable: grant weakness a target doesn't print.
    board.temporary_passives = []
    e["p2_active"].set_attribute(AttrID.WEAKNESS_TYPES, [])
    ctx.add_temporary_passive(e["p1_active"], GrantWeakness(t))
    calc = compute_damage(board, e["p1_active"], e["p2_active"], 50)
    assert calc.amount == 100 and calc.weakness_hit


async def test_switch_active_stamp():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    bench = ctx.my_bench()
    assert bench
    assert await ctx.switch_active(P1, bench[0])
    assert ctx.entered_active_this_turn(bench[0]), \
        "switch_active must stamp became_active_turn"


# ----------------------------------------------------------------------
# Sprint 2 tests
# ----------------------------------------------------------------------

def _pie_entry(pokemon, ability_id, hint="PokeAbility"):
    pokemon.set_attribute(AttrID.PIE_ABILITIES,
                          [{"abilityID": ability_id, "abilityType": hint}])


async def test_reveal_cards_shapes():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    hand = rig.board.find_player_area(P1, "hand")
    hand_card = hand.children[0]
    await ctx.reveal_cards([hand_card])
    assert ctx.messages_for(P1) == [], "owner already sees their hand card"
    runs = ctx.bracket_runs_for(P2)
    assert [name for name, _ in runs] == ["SerialSequence", "GroupedMove"]
    assert runs[0][1][0]["name"] == OutboundMsg.ENTITY_INTRODUCED.value
    names = [m["name"] for m in runs[1][1]]
    assert names == [OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value,
                     OutboundMsg.ENTITY_MOVED.value]
    assert runs[1][1][0]["value"]["Return"] is True
    move = runs[1][1][1]["value"]
    assert move["destinationID"] == hand.entity_id, "same-position move"
    assert hand.children[move["positionInParent"]] is hand_card
    # Deck-top reveals reach BOTH viewers (hidden from the owner too).
    ctx2 = attack_ctx(rig, e)
    top = ctx2.deck_top(1)[0]
    await ctx2.reveal_cards([top])
    assert ctx2.messages_for(P1) and ctx2.messages_for(P2)
    # to_player narrows the audience explicitly.
    ctx3 = attack_ctx(rig, e)
    await ctx3.reveal_cards([ctx3.deck_top(1)[0]], to_player=P1)
    assert ctx3.messages_for(P1) and not ctx3.messages_for(P2)


async def test_reveal_hand_view_only():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    hand_cards = ctx.hand(P1)
    cards = await ctx.reveal_hand(P1)  # AI viewer: skips the wire safely
    assert [c.entity_id for c in cards] == [c.entity_id for c in hand_cards]
    info = rig.session._view_cards_offer_info(cards, "peek")
    assert info["name"] == SelectionKind.COMPOSITE_REVEAL.value
    assert set(info["revealEntities"]) == {c.entity_id for c in cards}
    assert all(isinstance(v, list) and v for v in info["revealEntities"].values()), \
        "card faces must travel inline"
    inner = info["selections"][0]
    assert inner["validTargets"] == [] and inner["minimumToSelect"] == 0
    assert inner["forced"] is False and info["forced"] is False
    assert inner["targetPrompt"] is not None, "null targetPrompt NREs Initialize"


async def test_move_energy():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    active, bench0 = e["p1_active"], ctx.my_bench()[0]
    energy = ctx.attached_energies(active)[0]
    refreshed = []

    async def _spy(pokemon):
        refreshed.append(pokemon)

    rig.session.refresh_granted_abilities = _spy
    ctx._tool_holder_before_move = lambda card: active  # granted-ability def stand-in
    assert await ctx.move_energy(energy, bench0)
    assert energy.parent is bench0, "attach_card must reparent the energy"
    msgs = [m for _, m, _ in ctx._messages]
    assert len(msgs) == 1 and msgs[0]["name"] == OutboundMsg.ENTITY_MOVED.value, \
        "already-public attached cards move with NO intro"
    assert refreshed == [active], "old holder must refresh granted abilities"
    # Free distribution: the AI moves each energy once, then the loop ends.
    ctx2 = attack_ctx(rig, e)
    remaining = len(ctx2.attached_energies(active))
    assert remaining > 0
    moved = await ctx2.move_energy_freely([active], [bench0])
    assert len(moved) == remaining
    assert all(dest is bench0 for _, dest in moved)
    assert ctx2.attached_energies(active) == []
    # max_count caps the loop.
    ctx3 = attack_ctx(rig, e)
    capped = await ctx3.move_energy_freely([bench0], [active], max_count=1)
    assert len(capped) == 1


async def test_on_damaged_by_attack():
    rig, e = new_rig()
    neutralize_wr(e)
    fired = []

    async def _record(c):
        fired.append((c.damaged_by, c.damage_amount, c.pre_hit_hp, c.source))

    ability = Ability("Test Rough Skin", trigger=Triggers.ON_DAMAGED_BY_ATTACK,
                      effect=_record)
    aid = register_ability(ability)
    try:
        _pie_entry(e["p2_active"], aid)
        pre_hp = e["p2_active"].get_attribute(AttrID.HP, 0)
        lethal = pre_hp + 50
        await resolve_attack(rig.session, P1, e["p1_active"],
                             Attack("Test KO Blow", cost={}, damage=lethal),
                             str(uuid.uuid4()))
        assert len(fired) == 1, "trigger must fire exactly once"
        damaged_by, amount, pre, src = fired[0]
        assert damaged_by is e["p1_active"] and src is e["p2_active"]
        assert amount == lethal and pre == pre_hp, \
            "trigger ctx must carry the dealt amount and pre-hit HP"
        discard = rig.board.find_player_area(P2, "discard")
        assert e["p2_active"] in discard.children, \
            "trigger fires even though the target was Knocked Out"
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_perform_evolution_and_chain():
    rig, e = new_rig()
    session, board = rig.session, rig.board
    ctx = attack_ctx(rig, e)
    target = e["p1_active"]
    target.set_attribute(AttrID.HP, target.get_attribute(AttrID.HP, 0) - 20)
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
    fired = []

    async def _on_evolve(c):
        fired.append(c.source)

    ability = Ability("Test Shady Dealings", trigger=Triggers.ON_EVOLVE,
                      effect=_on_evolve)
    aid = register_ability(ability)
    try:
        evo = next(c for c in ctx.hand(P1) if isinstance(c, PokemonEntity))
        _pie_entry(evo, aid)
        assert await session.perform_evolution(P1, evo, target)
        active_area = board.find_player_area(P1, "activePokemonArea")
        assert evo.parent is active_area, "evolution takes the slot"
        assert target.parent is evo, "old stage tucks underneath"
        assert evo.get_attribute(AttrID.HP) == \
            passives.effective_max_hp(board, evo) - 20, "damage carries over"
        assert not (target.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), \
            "evolving cures the pre-evolution's conditions"
        ts = session.turn_state
        assert ts.entered_play_turn.get(evo.entity_id) == ts.turn_number
        assert fired == [evo], "ON_EVOLVE must fire on the evolution card"
    finally:
        ABILITIES_BY_ID.pop(aid, None)
    # Effect-driven, deck-sourced evolution bypasses may_evolve_target.
    ctx2 = attack_ctx(rig, e)
    bench_target = ctx2.my_bench()[0]
    session.turn_state.mark_entered_play(bench_target.entity_id)  # just played
    deck_evo = next(c for c in ctx2.deck(P1) if isinstance(c, PokemonEntity))
    assert await ctx2.evolve_pokemon(bench_target, deck_evo)
    assert bench_target.parent is deck_evo
    assert deck_evo.parent is board.find_player_area(P1, "bench")
    # Lineage helper: any loaded Stage2's chain walks down to its Basic.
    sample = next(
        (guid for guid in CARD_DEFS_BY_GUID
         if len(evolves_from_chain(guid)) == 2), None)
    assert sample is not None, "no 2-deep evolution line found in loaded cards"
    chain = evolves_from_chain(sample)
    assert evolves_from(sample, chain[0]) and evolves_from(sample, chain[1])
    assert not evolves_from(sample, "NoSuchPokemonName")


async def test_on_energy_attached():
    rig, e = new_rig()
    session = rig.session
    fired = []

    async def _observe(c):
        fired.append((c.player_id, c.attaching_player_id,
                      c.attached_energy, c.energy_receiver, c.source))

    ab1 = Ability("Test Watcher A", trigger=Triggers.ON_ENERGY_ATTACHED, effect=_observe)
    ab2 = Ability("Test Watcher B", trigger=Triggers.ON_ENERGY_ATTACHED, effect=_observe)
    a1, a2 = register_ability(ab1), register_ability(ab2)
    try:
        _pie_entry(e["p1_active"], a1)
        _pie_entry(e["p2_active"], a2)
        energy = next(c for c in rig.board.find_player_area(P1, "hand").children
                      if isinstance(c, EnergyEntity))
        entry = {
            "entityID": energy.entity_id,
            "selectableAction": {"actionID": str(uuid.uuid4()),
                                 "description": ACTION_PLAY_ENERGY},
            "targetInfoLst": [{"validTargets": [e["p1_active"].entity_id]}],
        }
        await session._execute_attach_energy(
            P1, energy, entry, [e["p1_active"].entity_id])
        assert len(fired) == 2, "both sides' observers fire on a manual attach"
        assert all(rec[1] == P1 and rec[2] is energy
                   and rec[3] is e["p1_active"] for rec in fired)
        assert {rec[4].entity_id for rec in fired} == \
            {e["p1_active"].entity_id, e["p2_active"].entity_id}
        # ctx.attach_energy: silent by default, opt-in via counts_as_attachment.
        fired.clear()
        ctx = attack_ctx(rig, e)
        deck_energy = next(c for c in ctx.deck(P1) if isinstance(c, EnergyEntity))
        await ctx.attach_energy(deck_energy, e["p1_active"])
        for hook in ctx.deferred_actions:
            await hook()
        assert fired == [], "effect attaches don't count as attachments by default"
        ctx2 = attack_ctx(rig, e)
        deck_energy2 = next(c for c in ctx2.deck(P1) if isinstance(c, EnergyEntity))
        await ctx2.attach_energy(deck_energy2, e["p1_active"],
                                 counts_as_attachment=True)
        for hook in ctx2.deferred_actions:
            await hook()
        assert len(fired) == 2, "opt-in flag fires the observers"
    finally:
        ABILITIES_BY_ID.pop(a1, None)
        ABILITIES_BY_ID.pop(a2, None)


async def test_play_locks():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state  # turn 3
    game_id = rig.session.game_id
    item = next(c for c in board.find_player_area(P1, "hand").children
                if is_item_card(c))

    def offered():
        return any(a["entityID"] == item.entity_id
                   for a in compute_legal_actions(board, ts, P1, game_id))

    assert offered()
    ctx = attack_ctx(rig, e)
    ctx.lock_plays(P1, is_item_card)  # locked through turn 4
    assert not offered(), "play lock must gate the trainer offer"
    ts.begin_turn(P2, board)  # turn 4: still locked
    assert not offered()
    ts.begin_turn(P1, board)  # turn 5: expired and pruned
    assert not ts.play_locks
    assert offered()

    class NoItems(Passive):
        def blocks_trainer_play(self, card, player_id, carrier):
            return is_item_card(card)

    ctx.add_temporary_passive(e["p2_active"], NoItems())
    assert not offered(), "blocks_trainer_play passive must gate the offer"
    board.temporary_passives = []
    # Attach restriction filters the Pokemon out of energy validTargets.
    energy = next(c for c in board.find_player_area(P1, "hand").children
                  if isinstance(c, EnergyEntity))

    def energy_targets():
        for a in compute_legal_actions(board, ts, P1, game_id):
            if a["entityID"] == energy.entity_id:
                return a["targetInfoLst"][0]["validTargets"]
        return None

    assert e["p1_active"].entity_id in (energy_targets() or [])
    ctx.restrict_attachments(e["p1_active"])
    targets = energy_targets()
    assert targets is None or e["p1_active"].entity_id not in targets


async def test_usable_from_offers():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    game_id = rig.session.game_id

    async def _draw_one(c):
        await c.draw_cards(1)

    hand_ab = Ability("Test From Hand", activation=Activations.ONCE_PER_TURN,
                      usable_from="hand", effect=_draw_one)
    disc_ab = Ability("Test From Discard", activation=Activations.ONCE_PER_TURN,
                      usable_from="discard", effect=_draw_one)
    h_id, d_id = register_ability(hand_ab), register_ability(disc_ab)
    try:
        hand_card = next(c for c in board.find_player_area(P1, "hand").children
                         if isinstance(c, PokemonEntity))
        disc_card = board.find_player_area(P1, "discard").children[0]
        _pie_entry(hand_card, h_id)
        _pie_entry(disc_card, d_id)
        actions = compute_legal_actions(board, ts, P1, game_id)
        by_action = {a["selectableAction"]["actionID"]: a for a in actions}
        assert h_id in by_action and d_id in by_action
        for aid, card in ((h_id, hand_card), (d_id, disc_card)):
            assert by_action[aid]["entityID"] == card.entity_id
            assert by_action[aid]["selectableAction"]["selectionType"] == \
                SelectionKind.OUT_OF_PLAY.value
        # Once-per-turn bookkeeping applies to out-of-zone uses too.
        ts.used_abilities.add((hand_card.entity_id, h_id))
        actions = compute_legal_actions(board, ts, P1, game_id)
        ids = {a["selectableAction"]["actionID"] for a in actions}
        assert h_id not in ids and d_id in ids
        # The executor resolves an out-of-play source.
        turn_over = await rig.session._execute_use_ability(
            P1, disc_card, action_entry(disc_card, d_id))
        assert turn_over is False
        assert (disc_card.entity_id, d_id) in ts.used_abilities
    finally:
        ABILITIES_BY_ID.pop(h_id, None)
        ABILITIES_BY_ID.pop(d_id, None)


async def test_prize_hooks():
    rig, e = new_rig()
    board = rig.board
    board.deal_from_deck(P1, "prizePile", 6)

    class ExtraPrizeToDiscard(Passive):
        def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
            return count + 1

        def prize_destination(self, pokemon, ctx, carrier):
            return "discard"

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], ExtraPrizeToDiscard())
    discard_before = len(board.find_player_area(P1, "discard").children)
    hand_before = len(board.find_player_area(P1, "hand").children)
    await ctx.knock_out(e["p2_active"])
    await rig.session.resolve_knockouts(ctx)
    assert len(board.find_player_area(P1, "prizePile").children) == 4, \
        "count hook must lift the take from 1 to 2"
    assert len(board.find_player_area(P1, "discard").children) == discard_before + 2, \
        "destination hook must reroute the prizes to the discard"
    assert len(board.find_player_area(P1, "hand").children) == hand_before


async def test_move_damage_counters():
    rig, e = new_rig()
    neutralize_wr(e)
    ctx = attack_ctx(rig, e)
    src, tgt = e["p1_active"], e["p2_active"]
    max_hp = ctx.max_hp(src)
    src.set_attribute(AttrID.HP, max_hp - 30)
    tgt_hp = tgt.get_attribute(AttrID.HP, 0)
    moved = await ctx.move_damage_counters(src, tgt, max_count=5)
    assert moved == 3, "move clamps to the source's actual damage"
    assert src.get_attribute(AttrID.HP) == max_hp, "source heals what moved"
    assert tgt.get_attribute(AttrID.HP) == tgt_hp - 30

    class EffShield(Passive):
        def blocks_attack_effects(self, target, carrier):
            return carrier_pokemon(carrier) is target

    src.set_attribute(AttrID.HP, max_hp - 20)
    ctx.add_temporary_passive(tgt, EffShield())
    tgt_hp2 = tgt.get_attribute(AttrID.HP, 0)
    assert await ctx.move_damage_counters(src, tgt) == 0, \
        "a shielded single destination fizzles the whole move"
    assert src.get_attribute(AttrID.HP) == max_hp - 20
    assert tgt.get_attribute(AttrID.HP) == tgt_hp2


async def test_modify_energy_provided():
    from spirit.game.attributes import CLIENT_POKEMON_TYPE_NAMES
    rig, e = new_rig()
    board = rig.board
    bench0 = next(c for c in board.find_player_area(P1, "bench").children
                  if isinstance(c, PokemonEntity))
    loose = next(c for c in board.find_player_area(P1, "hand").children
                 if isinstance(c, EnergyEntity))
    board.attach_card(loose.entity_id, bench0.entity_id)
    energies = board.attached_energies(bench0)
    assert len(energies) == 1
    type_value = next(iter(legal_actions._energy_provided_types(energies[0])))
    cost = {CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(type_value)]: 2}
    assert not legal_actions.attack_cost_satisfied(cost, energies, board)

    class DoubleProvide(Passive):
        def modify_energy_provided(self, options, energy, holder, board):
            return [option * 2 for option in options]

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], DoubleProvide())
    assert legal_actions.energy_provided_count(energies[0], board) == 2
    assert legal_actions.attack_cost_satisfied(cost, energies, board), \
        "provided-modifying passive must change cost satisfaction"
    board.temporary_passives = []
    # Suppression: the special energy provides only Colorless and its own
    # passive contribution switches off.
    energy = energies[0]
    energy.set_attribute(AttrID.IS_SPECIAL_ENERGY, True)
    marker = Shield()
    ctx.add_temporary_passive(energy, marker)
    assert any(p is marker for p, _ in passives.active_passives(board))

    class Temple(Passive):
        def suppresses_special_energy(self, energy, carrier):
            return True

    ctx.add_temporary_passive(e["p2_active"], Temple())
    assert all(p is not marker for p, _ in passives.active_passives(board)), \
        "a suppressed special energy contributes no passive"
    assert passives.energy_provided_options(board, energy) == \
        [[PokemonTypes.COLORLESS.value]]
    assert legal_actions._energy_provided_types(energy, board) == \
        {PokemonTypes.COLORLESS.value}


async def test_hyper_potion_double_turbo_energy():
    hyper_guid = card_loader.cards_by_stem["HyperPotion_166"]
    hyper = CARD_DEFS_BY_GUID[hyper_guid.lower()]
    alt_guid = card_loader.cards_by_stem["HyperPotion_54"]
    alt_hyper = CARD_DEFS_BY_GUID[alt_guid.lower()]
    rig = Rig(hyper, FILLER, ENERGY_GUIDS, ITEM)
    e = rig.setup("trainer")
    board = rig.board
    active = e["p1_active"]
    trainer = e["target"]
    energies = board.attached_energies(active)
    assert len(energies) >= 2

    # Leave one physical Energy card attached. As a basic Energy it provides
    # only one unit, so neither printing may be offered.
    energy = energies[0]
    deck = board.find_player_area(P1, "deck")
    for extra in energies[1:]:
        board.move_card(extra.entity_id, deck.entity_id)

    def hyper_is_offered():
        return any(
            entry["entityID"] == trainer.entity_id
            and entry["selectableAction"]["description"] == ACTION_USE_TRAINER
            for entry in compute_legal_actions(
                board, rig.session.turn_state, P1, rig.session.game_id
            )
        )

    assert not hyper_is_offered(), \
        "one Energy card providing one Energy must not enable Hyper Potion"
    assert not alt_hyper.condition(board, P1)

    # Give that same physical card Double Turbo's [[C, C]] provided value.
    # Legality and payment must count two Energy units, not two entities.
    energy.set_attribute(
        AttrID.ENERGY_INFO,
        {"options": [[PokemonTypes.COLORLESS.value,
                      PokemonTypes.COLORLESS.value]]},
    )
    assert hyper_is_offered(), \
        "one Double Turbo Energy must enable Hyper Potion"
    assert alt_hyper.condition(board, P1), \
        "both Hyper Potion printings must share provided-Energy legality"

    max_hp = passives.effective_max_hp(board, active)
    active.set_attribute(AttrID.HP, max_hp - 50)
    await resolve_trainer_effect(rig.session, P1, trainer)
    assert active.get_attribute(AttrID.HP) == max_hp, \
        "Hyper Potion heals the damaged target"
    discard = board.find_player_area(P1, "discard")
    assert energy.parent is discard, \
        "the one Double Turbo card pays and is discarded as two Energy"


async def test_on_move_to_active_once():
    rig, e = new_rig()
    session = rig.session
    fired = []

    async def _libero(c):
        fired.append(c.source.entity_id)

    ability = Ability("Test Libero", trigger=Triggers.ON_MOVE_TO_ACTIVE,
                      effect=_libero)
    aid = register_ability(ability)
    try:
        ctx = attack_ctx(rig, e)
        bench0 = ctx.my_bench()[0]
        _pie_entry(bench0, aid)
        assert await ctx.switch_active(P1, bench0)
        for hook in ctx.deferred_actions:
            await hook()
        assert fired == [bench0.entity_id]
        # Bounce it out and back in the same turn: no second fire.
        ctx2 = attack_ctx(rig, e)
        other = ctx2.my_bench()[0]
        await ctx2.switch_active(P1, other)
        for hook in ctx2.deferred_actions:
            await hook()
        ctx3 = attack_ctx(rig, e)
        await ctx3.switch_active(P1, bench0)
        for hook in ctx3.deferred_actions:
            await hook()
        assert fired == [bench0.entity_id], "at most once per entity per turn"
        # A new turn clears the once-per-turn gate.
        session.turn_state.begin_turn(P2, rig.board)
        session.turn_state.begin_turn(P1, rig.board)
        await session.fire_move_to_active_triggers(bench0)
        assert fired == [bench0.entity_id] * 2
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_on_ally_knocked_out():
    rig, e = new_rig()
    session, board = rig.session, rig.board
    victim = e["p1_active"]
    assert board.attached_energies(victim), "rig attaches cost energies"
    ally = next(c for c in board.find_player_area(P1, "bench").children
                if isinstance(c, PokemonEntity))
    recorded = []

    async def _exp_share(c):
        recorded.append((c.ko_pokemon, len(c.attached_energies(c.ko_pokemon)),
                         c.ko_pokemon._containing_area_name(), c.ko_from_attack))

    ability = Ability("Test Exp Share", trigger=Triggers.ON_ALLY_KNOCKED_OUT,
                      effect=_exp_share)
    aid = register_ability(ability)
    try:
        _pie_entry(ally, aid)
        ctx = EffectContext(session, P2, e["p2_active"],
                            Attack("Test Crunch", cost={}, damage=200))
        victim.set_attribute(AttrID.HP, 0)
        # "By damage from an attack" needs the hit ledger a real deal_damage
        # would have written; a bare knock_out must NOT count as one.
        ctx.attack_damage[victim.entity_id] = (200, 180)
        ctx.knockouts.append(victim)
        await session.resolve_knockouts(ctx)
        assert len(recorded) == 1
        ko_pokemon, energy_count, area, from_attack = recorded[0]
        assert ko_pokemon is victim and from_attack is True
        assert energy_count >= 1, "fires pre-discard with energies still attached"
        assert area == "activePokemonArea", "the KO'd stack had not moved yet"
        assert victim.parent is board.find_player_area(P1, "discard")
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_evolution_gate_passives():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    game_id = rig.session.game_id
    active = e["p1_active"]
    evo = next(c for c in board.find_player_area(P1, "hand").children
               if isinstance(c, PokemonEntity))
    evo.set_attribute(AttrID.STAGE, PokemonStage.STAGE1.value)
    evo.set_attribute(AttrID.EVOLUTION_LOGIC_FROM,
                      active.get_attribute(AttrID.EVOLUTION_LOGIC_NAME))

    def evolve_targets():
        for a in compute_legal_actions(board, ts, P1, game_id):
            if a["entityID"] == evo.entity_id \
                    and a["selectableAction"]["description"] == ACTION_EVOLVE:
                return a["targetInfoLst"][0]["validTargets"]
        return None

    assert active.entity_id in (evolve_targets() or [])
    # Everything freshly entered play: the just-played gate closes the offer.
    for p in board.pokemon_in_play(P1):
        ts.mark_entered_play(p.entity_id)
    assert evolve_targets() is None

    class EarlyBird(Passive):
        def may_evolve_early(self, pokemon, carrier):
            return carrier_pokemon(carrier) is pokemon

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(active, EarlyBird())
    assert evolve_targets() == [active.entity_id], \
        "may_evolve_early must reopen only its carrier"

    class NoEvo(Passive):
        def blocks_evolution(self, player_id, target, carrier):
            return True

    ctx.add_temporary_passive(e["p2_active"], NoEvo())
    assert evolve_targets() is None, "blocks_evolution wins over everything"


async def test_burn_hooks():
    rig, e = new_rig()
    session = rig.session
    active = e["p1_active"]
    active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Burned"])
    hp = active.get_attribute(AttrID.HP, 0)

    class HotBurn(Passive):
        def modify_burn_counters(self, counters, pokemon, carrier):
            return counters + 2

        def blocks_burn_recovery(self, pokemon, carrier):
            return True

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p2_active"], HotBurn())
    await session._checkup_burn(P1, active)
    assert active.get_attribute(AttrID.HP) == hp - 40, \
        "modify_burn_counters must raise the tick to 4 counters"
    assert "Burned" in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), \
        "blocks_burn_recovery skips the flip: still Burned regardless"
    rig.board.temporary_passives = []
    hp2 = active.get_attribute(AttrID.HP, 0)
    await session._checkup_burn(P1, active)
    assert active.get_attribute(AttrID.HP) == hp2 - 20, "base tick is 2 counters"


async def test_stacking_key_dedup():
    class HPBoost(Passive):
        stacking_key = "test-boost"

        def max_hp_bonus(self, pokemon, carrier):
            return 20

    class OtherBoost(HPBoost):
        stacking_key = "test-other"

    rig, e = new_rig()
    active = e["p1_active"]
    base = passives.effective_max_hp(rig.board, active)
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(active, HPBoost())
    ctx.add_temporary_passive(active, HPBoost())
    assert passives.effective_max_hp(rig.board, active) == base + 20, \
        "same-key passives count once"
    ctx.add_temporary_passive(active, OtherBoost())
    assert passives.effective_max_hp(rig.board, active) == base + 40


async def test_cure_condition_single():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    tgt = e["p2_active"]
    await ctx.apply_special_condition(tgt, SpecialConditions.POISONED,
                                      poison_counters=2)
    await ctx.apply_special_condition(tgt, SpecialConditions.BURNED)
    ctx._messages.clear()
    assert await ctx.cure_condition(tgt, SpecialConditions.POISONED)
    assert (tgt.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) == ["Burned"], \
        "only the cured condition is removed"
    assert tgt.entity_id not in rig.session.poison_counters
    runs = ctx.bracket_runs_for(P1)
    assert runs[0][0] == "RemoveSpecialCondition" and len(runs[0][1]) == 2, \
        "single-cure rides one RemoveSpecialCondition bracket (Target + attr)"
    assert await ctx.cure_condition(tgt, SpecialConditions.POISONED) is False


async def test_set_damage_counters():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    tgt = e["p2_active"]
    max_hp = ctx.max_hp(tgt)
    await ctx.set_damage_counters(tgt, 3)
    assert tgt.get_attribute(AttrID.HP) == max_hp - 30
    assert tgt not in ctx.knockouts
    await ctx.set_damage_counters(tgt, max_hp // 10)
    assert tgt.get_attribute(AttrID.HP) == 0 and tgt in ctx.knockouts, \
        "setting damage to max HP enqueues the KO"


async def test_pokemon_card_def_passive():
    rig, e = new_rig()
    marker = Shield()
    FILLER.passive = marker
    try:
        carriers = [c for p, c in passives.active_passives(rig.board)
                    if p is marker]
        assert e["p2_active"] in carriers, \
            "PokemonCardDef(passive=) must ride top-level in-play Pokemon"
        assert all(isinstance(c, PokemonEntity) for c in carriers)
    finally:
        FILLER.passive = None


async def test_tool_capacity_and_attach_to():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    game_id = rig.session.game_id
    active = e["p1_active"]
    tool = next(c for c in board.find_player_area(P1, "hand").children
                if (c.archetype_id or "").lower() == ITEM.guid.lower())
    tool.set_attribute(AttrID.TRAINER_TYPE, TrainerType.POKEMON_TOOL.value)
    tool2 = rig.to_area(rig.pull_guid(P1, ITEM.guid), P1, "hand")
    tool2.set_attribute(AttrID.TRAINER_TYPE, TrainerType.POKEMON_TOOL.value)

    def tool_targets(card):
        for a in compute_legal_actions(board, ts, P1, game_id):
            if a["entityID"] == card.entity_id \
                    and a["selectableAction"]["description"] == ACTION_ATTACH_TOOL:
                return a["targetInfoLst"][0]["validTargets"]
        return None

    assert active.entity_id in (tool_targets(tool) or [])
    board.attach_card(tool.entity_id, active.entity_id)
    assert passives.tool_slots_free(board, active) == 0
    targets = tool_targets(tool2)
    assert targets is None or active.entity_id not in targets, \
        "a full holder must leave the tool targets"

    class BigPockets(Passive):
        def tool_capacity(self, pokemon, carrier):
            return 2

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(active, BigPockets())
    assert passives.tool_slots_free(board, active) == 1
    assert active.entity_id in (tool_targets(tool2) or []), \
        "tool_capacity 2 must reopen the second slot"
    ITEM.attach_to = lambda p: False
    try:
        assert tool_targets(tool2) is None, \
            "PokemonToolCardDef.attach_to must filter every target"
    finally:
        del ITEM.attach_to


async def test_bench_capacity():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    game_id = rig.session.game_id
    basic = next(c for c in board.find_player_area(P1, "hand").children
                 if isinstance(c, PokemonEntity))

    def play_offered():
        return any(
            a["entityID"] == basic.entity_id
            and a["selectableAction"]["description"] == ACTION_PLAY_POKEMON
            for a in compute_legal_actions(board, ts, P1, game_id))

    assert passives.effective_bench_capacity(board, P1) == 5
    assert play_offered()

    class TinyBench(Passive):
        def bench_capacity(self, player_id, carrier):
            return 2

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], TinyBench())
    assert passives.effective_bench_capacity(board, P1) == 2
    assert not play_offered(), "shrunken capacity must gate the bench play"
    ctx2 = attack_ctx(rig, e)
    deck_poke = next(c for c in ctx2.deck(P1) if isinstance(c, PokemonEntity))
    assert await ctx2.bench_pokemon(deck_poke) is False
    board.temporary_passives = []
    assert await ctx2.bench_pokemon(deck_poke) is True


async def test_bench_shrink_discard():
    rig, e = new_rig()
    board, session = rig.board, rig.session
    bench = board.find_player_area(P1, "bench")
    for _ in range(5 - len(bench.children)):
        assert rig.to_area(rig.pull_guid(P1, FILLER.guid), P1, "bench") is not None
    assert len(bench.children) == 5
    victim = bench.children[0]  # AI auto-pick takes the first candidate
    rig.attach(rig.pull(P1, lambda c: isinstance(c, EnergyEntity)), victim)
    energy = board.attached_energies(victim)[0]
    max_hp = passives.effective_max_hp(board, victim)
    victim.set_attribute(AttrID.HP, max_hp - 20)
    ctx = attack_ctx(rig, e)
    await ctx.apply_special_condition(victim, SpecialConditions.ASLEEP)
    fired = []

    async def _ko_recorder(c):
        fired.append(c.source)

    ability = Ability("Test Last Words", trigger=Triggers.ON_KNOCKED_OUT,
                      effect=_ko_recorder)
    aid = register_ability(ability)
    try:
        _pie_entry(victim, aid)
        board.deal_from_deck(P2, "prizePile", 6)

        class Bench4(Passive):
            def bench_capacity(self, player_id, carrier):
                return 4 if player_id == P1 else None

        ctx.add_temporary_passive(e["p1_active"], Bench4())
        await session.enforce_bench_capacity()
        discard = board.find_player_area(P1, "discard")
        assert len(bench.children) == 4, "exactly one stack is discarded"
        assert victim.parent is discard, "the picked Pokemon goes to the discard"
        assert energy.parent is discard, "its attachments ride along"
        assert fired == [], "not a Knock Out: ON_KNOCKED_OUT must not fire"
        assert len(board.find_player_area(P2, "prizePile").children) == 6, \
            "not a Knock Out: no prizes taken"
        assert not (victim.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), \
            "conditions clear on leaving play"
        assert victim.get_attribute(AttrID.HP) == max_hp, \
            "damage resets on leaving play"
        # Capacity restored: no further discards.
        board.temporary_passives = []
        discarded_before = len(discard.children)
        await session.enforce_bench_capacity()
        assert len(bench.children) == 4
        assert len(discard.children) == discarded_before
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_bench_shrink_turn_order():
    rig, e = new_rig()
    board, session = rig.board, rig.session
    assert rig.to_area(rig.pull_guid(P2, FILLER.guid), P2, "bench") is not None
    p1_bench = board.find_player_area(P1, "bench")
    p2_bench = board.find_player_area(P2, "bench")
    assert len(p1_bench.children) == 3 and len(p2_bench.children) == 3

    class Tiny2(Passive):
        def bench_capacity(self, player_id, carrier):
            return 2

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], Tiny2())
    session.turn_state.active_player_id = P2
    picked_order = []

    async def _spy(player_id, source_entity_id, cards, count, minimum=None,
                   prompt=""):
        picked_order.append(player_id)
        return [c.entity_id for c in cards[:count]]

    session.prompt_entity_picker = _spy
    await session.enforce_bench_capacity()
    assert picked_order == [P2, P1], "the active player resolves first"
    assert len(p1_bench.children) == 2 and len(p2_bench.children) == 2


async def test_bench_shrink_reentrancy_cap():
    from spirit.game.session.game_session import _MAX_BENCH_ENFORCE_PASSES
    rig, _ = new_rig()
    session = rig.session
    calls = []

    async def _always_over():
        calls.append(1)
        await session.enforce_bench_capacity()  # reentrant: must no-op
        return True

    session._enforce_bench_capacity_once = _always_over
    await session.enforce_bench_capacity()
    assert len(calls) == _MAX_BENCH_ENFORCE_PASSES, \
        f"unstable capacity must stop at the pass cap (got {len(calls)})"
    assert session._enforcing_bench is False, "the guard must reset"
    calls.clear()

    async def _stable():
        calls.append(1)
        return False

    session._enforce_bench_capacity_once = _stable
    await session.enforce_bench_capacity()
    assert len(calls) == 1, "a stable board exits after one pass"


async def test_blocks_ability_effects():
    rig, e = new_rig()
    tgt = e["p2_active"]

    class AbilityShield(Passive):
        def blocks_ability_effects(self, target, carrier):
            return carrier_pokemon(carrier) is target

    ability_ctx = EffectContext(rig.session, P1, e["p1_active"],
                                Ability("Test Power"))
    ability_ctx.add_temporary_passive(tgt, AbilityShield())
    assert ability_ctx.is_ability_effect()
    assert ability_ctx.effects_blocked(tgt)
    hp = tgt.get_attribute(AttrID.HP, 0)
    await ability_ctx.deal_damage(30, target=tgt, as_counters=True)
    assert tgt.get_attribute(AttrID.HP) == hp, \
        "ability-context counter placement must be prevented"
    atk = attack_ctx(rig, e)
    assert not atk.effects_blocked(tgt), \
        "an Ability shield must not block ATTACK effects"


async def test_blocks_discard():
    rig, e = new_rig()
    board = rig.board
    energy = board.attached_energies(e["p1_active"])[0]

    class Sticky(Passive):
        def blocks_discard(self, card, carrier):
            return isinstance(card, EnergyEntity)

    opp_ctx = EffectContext(rig.session, P2, e["p2_active"],
                            Attack("Test Rip Away", cost={}, damage=10))
    opp_ctx.add_temporary_passive(e["p2_active"], Sticky())
    await opp_ctx.discard_cards([energy])
    assert energy.parent is e["p1_active"], \
        "opponent-caused discard must be blocked"
    own_ctx = attack_ctx(rig, e)
    await own_ctx.discard_cards([energy])
    assert energy.parent is board.find_player_area(P1, "discard"), \
        "own discards (costs) always resolve"


async def test_take_prizes_win_declare():
    rig, e = new_rig()
    board, session = rig.board, rig.session
    board.deal_from_deck(P1, "prizePile", 2)
    hand_before = len(board.find_player_area(P1, "hand").children)
    ctx = attack_ctx(rig, e)
    raised = False
    try:
        await ctx.take_prizes(2)
    except GameOver:
        raised = True
    assert raised and session.game_phase == GamePhase.GAME_OVER, \
        "emptying the prize pile must win the game"
    assert len(board.find_player_area(P1, "hand").children) == hand_before + 2
    assert not board.find_player_area(P1, "prizePile").children
    rig2, e2 = new_rig()
    ctx2 = attack_ctx(rig2, e2)
    raised = False
    try:
        await ctx2.win_game("test win")
    except GameOver:
        raised = True
    assert raised and rig2.session.game_phase == GamePhase.GAME_OVER
    # declare_winner: the pure, wire-free game-over path.
    rig3, _ = new_rig()
    result = rig3.session.declare_winner(P1, "headless")
    assert result == {"winner": P1, "loser": P2, "reason": "headless"}
    assert rig3.session.game_result == result
    assert rig3.session.game_phase == GamePhase.GAME_OVER


async def test_reorder_deck_top():
    rig, e = new_rig()
    ctx = attack_ctx(rig, e)
    deck_size = len(ctx.deck(P1))
    top_before = ctx.deck_top(3)

    async def _reversed_pick(pid, src, cards, count, minimum=None,
                             prompt="", ordered=False, display_cards=None,
                             slot_prompt=""):
        assert ordered is True
        return [c.entity_id for c in reversed(list(cards))]

    rig.session.prompt_card_chooser = _reversed_pick
    order = await ctx.reorder_deck_top(3)
    assert [c.entity_id for c in order] == \
        [c.entity_id for c in reversed(top_before)]
    assert [c.entity_id for c in ctx.deck_top(3)] == \
        [c.entity_id for c in reversed(top_before)], "picked order = new top order"
    assert len(ctx.deck(P1)) == deck_size
    assert ctx._messages == [], "hidden reorder sends nothing on the wire"


async def test_unplayable_from_hand():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    game_id = rig.session.game_id
    basic = next(c for c in board.find_player_area(P1, "hand").children
                 if isinstance(c, PokemonEntity))

    def play_offered():
        return any(
            a["entityID"] == basic.entity_id
            and a["selectableAction"]["description"] == ACTION_PLAY_POKEMON
            for a in compute_legal_actions(board, ts, P1, game_id))

    assert play_offered()
    assert basic in board.basic_pokemon_in_hand(P1)
    FILLER.unplayable_from_hand = True
    try:
        assert not play_offered(), "unplayable_from_hand must gate the bench play"
        assert basic not in board.basic_pokemon_in_hand(P1), \
            "setup placement/mulligan scans must skip it too"
    finally:
        FILLER.unplayable_from_hand = False


async def test_cards_by_stem():
    assert len(card_loader.cards_by_stem) > 2000
    for stem, guid in list(card_loader.cards_by_stem.items())[:25]:
        assert isinstance(stem, str) and stem and not stem.endswith(".py")
        assert card_loader.cards_by_guid.get(guid.lower()) is not None \
            or card_loader.cards_by_guid.get(guid) is not None
    assert "Potion_100" in card_loader.cards_by_stem


# ----------------------------------------------------------------------
# Sprint 4 tests
# ----------------------------------------------------------------------

async def test_flip_prevent_damage():
    rig, e = new_rig()
    neutralize_wr(e)
    tgt = e["p2_active"]
    ctx = attack_ctx(rig, e, damage=30)
    ctx.add_temporary_passive(tgt, flip_prevent_damage_passive("Test Infiltrator"))
    hp = tgt.get_attribute(AttrID.HP, 0)
    with forced_flips(0):  # heads
        dealt = await ctx.deal_damage(30)
    assert dealt == 0 and tgt.get_attribute(AttrID.HP) == hp, \
        "heads must prevent the whole hit"
    flips = [m for _, m, _ in ctx._messages if "resultLst" in (m.get("value") or {})]
    assert len(flips) == 1 and flips[0]["value"]["source"] == tgt.entity_id, \
        "one coin message anchored on the carrier, queued inline"
    ctx2 = attack_ctx(rig, e, damage=30)
    with forced_flips(1):  # tails
        dealt = await ctx2.deal_damage(30)
    assert dealt == 30 and tgt.get_attribute(AttrID.HP) == hp - 30


async def test_guts_survive():
    rig, e = new_rig()
    neutralize_wr(e)
    tgt = e["p2_active"]
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(tgt, guts_survive_passive())
    hp = tgt.get_attribute(AttrID.HP, 0)
    # Not a KO: the interceptor stays silent (a consulted flip would raise).
    with forced_flips():
        dealt = await ctx.deal_damage(hp - 20)
    assert dealt == hp - 20 and tgt.get_attribute(AttrID.HP) == 20
    # Lethal + heads: survives at exactly hp_floor.
    ctx2 = attack_ctx(rig, e)
    with forced_flips(0):
        await ctx2.deal_damage(500)
    assert tgt.get_attribute(AttrID.HP) == 10 and tgt not in ctx2.knockouts, \
        "heads must leave the survivor at 10 HP with no KO enqueued"
    # Lethal + tails: the KO goes through.
    ctx3 = attack_ctx(rig, e)
    with forced_flips(1):
        await ctx3.deal_damage(500)
    assert tgt.get_attribute(AttrID.HP) == 0 and tgt in ctx3.knockouts
    # ignore_target_effects skips interceptors riding the target entirely.
    rig2, e2 = new_rig()
    neutralize_wr(e2)
    tgt2 = e2["p2_active"]
    ctx4 = attack_ctx(rig2, e2)
    ctx4.add_temporary_passive(tgt2, guts_survive_passive())
    with forced_flips():
        await ctx4.deal_damage(500, ignore_target_effects=True)
    assert tgt2.get_attribute(AttrID.HP) == 0


async def test_attack_flip_check():
    rig, e = new_rig()
    neutralize_wr(e)
    session, ts = rig.session, rig.session.turn_state  # turn 3
    attacker = e["p1_active"]
    atk = Attack("Test Locked Blast", cost={}, damage=30, locks_next_turn=True)
    aid = register_ability(atk)
    entry = {
        "entityID": attacker.entity_id,
        "selectableAction": {"actionID": aid, "description": ACTION_USE_ATTACK},
        "targetInfoLst": [],
    }
    try:
        ts.set_attack_flip_check(attacker.entity_id, title="Test Smokescreen")
        tgt_hp = e["p2_active"].get_attribute(AttrID.HP, 0)
        with forced_flips(1):  # tails cancels the attack
            turn_over = await session._execute_attack(P1, attacker, entry)
        assert turn_over is True, "the turn still ends on tails"
        assert e["p2_active"].get_attribute(AttrID.HP) == tgt_hp, "no damage on tails"
        assert not ts.attack_locked(attacker.entity_id, aid), \
            "a cancelled attack never happened for lock bookkeeping"
        with forced_flips(0):  # heads proceeds
            turn_over = await session._execute_attack(P1, attacker, entry)
        assert turn_over is True
        assert e["p2_active"].get_attribute(AttrID.HP) == tgt_hp - 30
        assert ts.attack_locked(attacker.entity_id, aid)
        # Lifetime: through the opponent's next turn, then pruned.
        assert ts.attack_flip_check(attacker.entity_id) == "Test Smokescreen"
        ts.begin_turn(P2, rig.board)  # turn 4: still armed
        assert ts.attack_flip_check(attacker.entity_id) is not None
        ts.begin_turn(P1, rig.board)  # turn 5: expired and pruned
        assert ts.attack_flip_check(attacker.entity_id) is None
        assert attacker.entity_id not in ts.attack_flip_checks
        # Factory: printed damage + the rider on the Defending Pokemon.
        ctx = attack_ctx(rig, e, damage=10, title="Test Smoke")
        with forced_flips():
            await smokescreen_attack()(ctx)
        assert ts.attack_flip_check(e["p2_active"].entity_id) == "Test Smoke"
        # clear_pokemon_effects releases the check (leaves the Active).
        session.clear_pokemon_effects(e["p2_active"])
        assert ts.attack_flip_check(e["p2_active"].entity_id) is None
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_was_active_at_ko():
    rig, e = new_rig()
    session, board = rig.session, rig.board
    recorded = []

    async def _record(c):
        recorded.append(c.was_active_at_ko)

    ability = Ability("Test Entrusted Wishes", trigger=Triggers.ON_KNOCKED_OUT,
                      effect=_record)
    aid = register_ability(ability)
    try:
        victim = e["p1_active"]
        _pie_entry(victim, aid)
        ctx = EffectContext(session, P2, e["p2_active"],
                            Attack("Test Crunch", cost={}, damage=200))
        await ctx.knock_out(victim)
        await session.resolve_knockouts(ctx)
        assert recorded == [True], "an Active-spot KO must set was_active_at_ko"
        benched = next(c for c in board.find_player_area(P1, "bench").children
                       if isinstance(c, PokemonEntity))
        _pie_entry(benched, aid)
        ctx2 = EffectContext(session, P2, e["p2_active"],
                             Attack("Test Crunch", cost={}, damage=200))
        await ctx2.knock_out(benched)
        await session.resolve_knockouts(ctx2)
        assert recorded == [True, False], "a bench KO reads False"
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_on_turn_drawn():
    rig, e = new_rig()
    session, board = rig.session, rig.board
    fired = []

    async def _top_entry(c):
        fired.append(c.source)

    ability = Ability("Test Top Entry", trigger=Triggers.ON_TURN_DRAWN,
                      effect=_top_entry)
    aid = register_ability(ability)
    try:
        deck = board.find_player_area(P1, "deck")
        top = deck.children[-1]
        _pie_entry(top, aid)
        await session._begin_turn(P1)
        assert fired == [top], "the turn draw must fire ON_TURN_DRAWN"
        assert top.parent is board.find_player_area(P1, "hand")
        assert top.entity_id in session.turn_state.turn_draw_entity_ids
        # Effect draws are NOT the beginning-of-turn draw: no fire.
        _pie_entry(deck.children[-1], aid)
        ctx = attack_ctx(rig, e)
        await ctx.draw_cards(1)
        assert fired == [top]
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_on_taken_as_prize():
    rig, e = new_rig()
    session, board = rig.session, rig.board
    board.deal_from_deck(P1, "prizePile", 2)
    prize_area = board.find_player_area(P1, "prizePile")
    fired = []

    async def _dream(c):
        fired.append(c.source)

    ability = Ability("Test Dream Window", trigger=Triggers.ON_TAKEN_AS_PRIZE,
                      effect=_dream)
    aid = register_ability(ability)
    try:
        first = prize_area.children[0]  # the AI pick takes children order
        _pie_entry(first, aid)
        await session._take_prizes(P1, 1)
        assert fired == [first], "taking the prize must fire ON_TAKEN_AS_PRIZE"
        assert first.parent is board.find_player_area(P1, "hand")
    finally:
        ABILITIES_BY_ID.pop(aid, None)


async def test_trainer_effect_shield():
    rig, e = new_rig()
    board, session = rig.board, rig.session
    trainer = next(c for c in board.find_player_area(P1, "hand").children
                   if is_item_card(c))
    ctx = EffectContext(session, P1, trainer, None)
    ctx.is_trainer_effect = True
    ctx.add_temporary_passive(
        e["p2_active"], trainer_effect_shield_passive(supporters_only=False))
    p2_hand = len(ctx.hand(P2))
    assert await ctx.draw_cards(2, player_id=P2) == 0, "shielded draw no-ops"
    assert len(ctx.hand(P2)) == p2_hand
    assert await ctx.discard_from_hand(1, player_id=P2) == []
    assert len(ctx.hand(P2)) == p2_hand
    assert await ctx.hand_to_bottom_of_deck(P2) == 0
    bench2 = next(c for c in board.find_player_area(P2, "bench").children
                  if isinstance(c, PokemonEntity))
    assert await ctx.switch_active(P2, bench2) is False, "shielded gust no-ops"
    assert await ctx.apply_special_condition(
        e["p2_active"], SpecialConditions.ASLEEP) is False
    assert not (e["p2_active"].get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    hp = e["p2_active"].get_attribute(AttrID.HP, 0)
    assert await ctx.deal_damage(30, target=e["p2_active"]) == 0
    assert e["p2_active"].get_attribute(AttrID.HP) == hp
    energy = board.attached_energies(e["p2_active"])[0]
    await ctx.discard_cards([energy])
    assert energy.parent is e["p2_active"], "shielded attachment discard no-ops"
    # Self-effects still resolve; non-trainer contexts are never gated.
    assert await ctx.draw_cards(1) == 1
    neutralize_wr(e)
    atk = attack_ctx(rig, e, damage=30)
    assert await atk.deal_damage(30) == 30


async def test_replace_supporter_effect():
    rig, e = new_rig()
    board, session = rig.board, rig.session
    card = next(c for c in board.find_player_area(P1, "hand").children
                if is_item_card(c))
    card.set_attribute(AttrID.TRAINER_TYPE, TrainerType.SUPPORTER.value)
    calls = []

    async def _original(c):
        calls.append("original")

    async def _replacement(c):
        calls.append("replacement")
        await c.draw_cards(3)

    guid = (card.archetype_id or "").lower()
    TRAINER_EFFECTS_BY_GUID[guid] = _original
    try:
        ctx = attack_ctx(rig, e)
        ctx.add_temporary_passive(e["p2_active"],
                                  replace_opponent_supporters(_replacement))
        hand_before = len(board.find_player_area(P1, "hand").children)
        tctx = await resolve_trainer_effect(session, P1, card)
        assert calls == ["replacement"], "the replacement supplants the original"
        assert tctx is not None and tctx.is_trainer_effect
        assert len(board.find_player_area(P1, "hand").children) == hand_before + 3
        # No replacer in play: the registered effect runs normally.
        calls.clear()
        board.temporary_passives = []
        tctx = await resolve_trainer_effect(session, P1, card)
        assert calls == ["original"] and tctx.is_trainer_effect
    finally:
        TRAINER_EFFECTS_BY_GUID.pop(guid, None)


async def test_energy_attach_tax():
    rig, e = new_rig()
    board, session = rig.board, rig.session
    ts = session.turn_state
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p2_active"], energy_attach_tax_passive())
    energy = next(c for c in board.find_player_area(P1, "hand").children
                  if isinstance(c, EnergyEntity))
    entry = {
        "entityID": energy.entity_id,
        "selectableAction": {"actionID": str(uuid.uuid4()),
                             "description": ACTION_PLAY_ENERGY},
        "targetInfoLst": [{"validTargets": [e["p1_active"].entity_id]}],
    }
    with forced_flips(1):  # tails: discard instead of attaching
        await session._execute_attach_energy(
            P1, energy, entry, [e["p1_active"].entity_id])
    assert energy.parent is board.find_player_area(P1, "discard")
    assert ts.energy_attached is False, \
        "per the card text a taxed-away attach does NOT use the turn attachment"
    energy2 = next(c for c in board.find_player_area(P1, "hand").children
                   if isinstance(c, EnergyEntity))
    entry["entityID"] = energy2.entity_id
    with forced_flips(0):  # heads: the attach proceeds normally
        await session._execute_attach_energy(
            P1, energy2, entry, [e["p1_active"].entity_id])
    assert energy2.parent is e["p1_active"] and ts.energy_attached is True
    # No taxer in play: no flip is consulted at all.
    board.temporary_passives = []
    ts.energy_attached = False
    deck_energy = rig.to_area(
        rig.pull(P1, lambda c: isinstance(c, EnergyEntity)), P1, "hand")
    entry["entityID"] = deck_energy.entity_id
    with forced_flips():
        await session._execute_attach_energy(
            P1, deck_energy, entry, [e["p1_active"].entity_id])
    assert deck_energy.parent is e["p1_active"]


async def test_scheduled_effects():
    rig, e = new_rig()
    session = rig.session
    ts = session.turn_state  # turn 3
    fired = []

    async def _boom(s):
        fired.append(s.turn_state.turn_number)

    ctx = attack_ctx(rig, e)
    ctx.schedule_at_checkup(1, _boom)
    await session._run_pokemon_checkup(P1)  # checkup of turn 3: not due yet
    assert fired == [] and len(session.scheduled_effects) == 1
    ts.begin_turn(P2, rig.board)  # turn 4
    await session._run_pokemon_checkup(P2)
    assert fired == [4], "must fire at the checkup of turn+1"
    assert session.scheduled_effects == []
    # A False guard drops the entry without running it.
    ctx.schedule_at_checkup(0, _boom, guard=lambda board: False)
    await session._run_pokemon_checkup(P2)
    assert fired == [4] and session.scheduled_effects == []
    # A passing guard runs like normal.
    ctx.schedule_at_checkup(0, _boom, guard=lambda board: True)
    await session._run_pokemon_checkup(P2)
    assert fired == [4, 4]


async def test_retreat_cost_board_param():
    rig, e = new_rig()
    board = rig.board
    seen = []

    class BoardAware(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            seen.append(board)
            return 0

    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(e["p1_active"], BoardAware())
    assert passives.effective_retreat_cost(board, e["p1_active"]) == 0
    assert seen and all(b is board for b in seen), \
        "modify_retreat_cost must receive the live board"


async def test_ignore_target_effects_turn_flag():
    rig, e = new_rig()
    neutralize_wr(e)
    ts = rig.session.turn_state
    tgt = e["p2_active"]
    ctx = attack_ctx(rig, e)
    ctx.add_temporary_passive(tgt, Shield())
    assert await ctx.deal_damage(30) == 0, "the target shield prevents normally"
    ctx.ignore_own_target_effects(e["p1_active"])
    assert await ctx.deal_damage(30) == 30, "the turn flag ignores target passives"
    # Interceptors riding the target are skipped under the flag too.
    rig.board.temporary_passives = []
    ctx.add_temporary_passive(tgt, flip_prevent_damage_passive("Test Flip"))
    with forced_flips():
        assert await ctx.deal_damage(30) == 30
    # A new turn clears the flag: the interceptor is consulted again.
    ts.begin_turn(P2, rig.board)
    with forced_flips(0):
        assert await ctx.deal_damage(30) == 0, "a new turn must clear the flag"


async def test_usable_despite_conditions():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    game_id = rig.session.game_id
    active = e["p1_active"]
    ok = Attack("Test Struggle", cost={}, damage=10, usable_despite_conditions=True)
    slow = Attack("Test Nap", cost={}, damage=10)
    ok_id, slow_id = register_ability(ok), register_ability(slow)
    try:
        active.set_attribute(AttrID.PIE_ABILITIES, [
            {"abilityID": ok_id, "abilityType": "Attack", "cost": {}},
            {"abilityID": slow_id, "abilityType": "Attack", "cost": {}},
        ])
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Asleep"])
        actions = compute_legal_actions(board, ts, P1, game_id)
        ids = {a["selectableAction"]["actionID"] for a in actions}
        assert ok_id in ids, "usable_despite_conditions is offered while Asleep"
        assert slow_id not in ids, "normal attacks stay suppressed"
        assert not any(a["selectableAction"]["description"] == ACTION_RETREAT
                       for a in actions), "retreat stays suppressed"
        active.set_attribute(AttrID.SPECIAL_CONDITIONS, [])
        ids = {a["selectableAction"]["actionID"]
               for a in compute_legal_actions(board, ts, P1, game_id)}
        assert ok_id in ids and slow_id in ids
    finally:
        ABILITIES_BY_ID.pop(ok_id, None)
        ABILITIES_BY_ID.pop(slow_id, None)


async def test_on_play_trigger_ends_turn():
    rig, e = new_rig()
    pokemon = e["p1_active"]
    saved = pokemon.get_attribute(AttrID.PIE_ABILITIES)

    async def _draw_one(c):
        await c.draw_cards(1)

    ability = Ability("Test Gate", trigger=Triggers.ON_PLAY,
                      ends_turn=True, effect=_draw_one)
    aid = register_ability(ability)
    try:
        pokemon.set_attribute(AttrID.PIE_ABILITIES, [{"abilityID": aid}])
        over = await rig.session._fire_triggered_abilities(
            P1, pokemon, Triggers.ON_PLAY)
        assert over is True, "resolved ON_PLAY ends_turn trigger must end the turn"
    finally:
        ABILITIES_BY_ID.pop(aid, None)

    async def _noop(c):
        pass

    ability = Ability("Test Gate Declined", trigger=Triggers.ON_PLAY,
                      ends_turn=True, effect=_noop)
    aid = register_ability(ability)
    try:
        pokemon.set_attribute(AttrID.PIE_ABILITIES, [{"abilityID": aid}])
        over = await rig.session._fire_triggered_abilities(
            P1, pokemon, Triggers.ON_PLAY)
        assert over is False, "a declined/no-op trigger must not end the turn"
    finally:
        ABILITIES_BY_ID.pop(aid, None)
        pokemon.set_attribute(AttrID.PIE_ABILITIES, saved)


async def test_extra_prize_watchers():
    rig, e = new_rig()
    board, ts = rig.board, rig.session.turn_state
    neutralize_wr(e)
    board.deal_from_deck(P1, "prizePile", 6)
    attacker, target = e["p1_active"], e["p2_active"]
    ctx = attack_ctx(rig, e)
    ctx.add_extra_prize_watcher(lambda a: False, None)  # never matches
    ctx.add_extra_prize_watcher(
        lambda a: a is attacker, lambda t: t is target, prizes=1)
    await ctx.deal_damage(1000)
    await rig.session.resolve_knockouts(ctx)
    assert len(board.find_player_area(P1, "prizePile").children) == 4, \
        "matching watcher adds +1 to the take; non-matching adds nothing"
    ts.begin_turn(P2, board)
    assert ts.extra_prize_watchers == [], "watchers are this-turn only"


async def test_setup_as_active():
    from spirit.game.data_utils import def_for
    luxray = def_for("ef8ca3ef-7c49-55f9-8a3b-0bf871f8e524")  # CZ Luxray
    assert luxray is not None and getattr(luxray, "setup_as_active", False), \
        "CZ Luxray must carry setup_as_active"
    rig = Rig(luxray, FILLER, ENERGY_GUIDS, ITEM)
    rig.setup("pokemon")
    board = rig.board
    in_hand = rig.to_area(rig.pull_guid(P1, luxray.guid), P1, "hand")
    assert in_hand is not None
    basics = board.basic_pokemon_in_hand(P1)
    assert in_hand not in basics, \
        "Stage 2 stays out of the Basic scans (bench offer / bench plays)"
    candidates = board.setup_active_candidates(P1)
    assert in_hand in candidates, "setup_as_active joins the opening-Active offer"
    assert candidates[:len(basics)] == basics, \
        "Basics stay first (the AI pick prefers a true Basic)"
    assert board.player_has_any_basic(P1)


TESTS = [
    test_temp_passive_prevents_then_expires,
    test_temp_passive_cleared_on_leave,
    test_turn_damage_modifier_scoping,
    test_retreat_lock_blocks_then_expires,
    test_blocks_retreat_passive,
    test_history_rotation_attacks_used,
    test_damage_taken_recorded,
    test_ends_turn_plumbing,
    test_flip_until_tails,
    test_ignore_resistance,
    test_unlimited_activation,
    test_blocks_special_conditions,
    test_prevents_healing,
    test_usable_first_turn,
    test_weakness_multiplier_and_types,
    test_switch_active_stamp,
    test_reveal_cards_shapes,
    test_reveal_hand_view_only,
    test_move_energy,
    test_on_damaged_by_attack,
    test_perform_evolution_and_chain,
    test_on_energy_attached,
    test_play_locks,
    test_usable_from_offers,
    test_prize_hooks,
    test_move_damage_counters,
    test_modify_energy_provided,
    test_hyper_potion_double_turbo_energy,
    test_on_move_to_active_once,
    test_on_ally_knocked_out,
    test_evolution_gate_passives,
    test_burn_hooks,
    test_stacking_key_dedup,
    test_cure_condition_single,
    test_set_damage_counters,
    test_pokemon_card_def_passive,
    test_tool_capacity_and_attach_to,
    test_bench_capacity,
    test_bench_shrink_discard,
    test_bench_shrink_turn_order,
    test_bench_shrink_reentrancy_cap,
    test_blocks_ability_effects,
    test_blocks_discard,
    test_take_prizes_win_declare,
    test_reorder_deck_top,
    test_unplayable_from_hand,
    test_cards_by_stem,
    test_flip_prevent_damage,
    test_guts_survive,
    test_attack_flip_check,
    test_was_active_at_ko,
    test_on_turn_drawn,
    test_on_taken_as_prize,
    test_trainer_effect_shield,
    test_replace_supporter_effect,
    test_energy_attach_tax,
    test_scheduled_effects,
    test_retreat_cost_board_param,
    test_ignore_target_effects_turn_flag,
    test_usable_despite_conditions,
    test_on_play_trigger_ends_turn,
    test_extra_prize_watchers,
    test_setup_as_active,
]


async def main_async() -> int:
    global FILLER, ENERGY_GUIDS, ITEM
    card_loader.load_all()
    FILLER = pick_filler_basic()
    ENERGY_GUIDS = basic_energy_guids()
    ITEM = pick_filler_item()

    failures = 0
    for test in TESTS:
        random.seed(0xC0FFEE)
        try:
            await asyncio.wait_for(test(), timeout=30.0)
            print(f"[PASS] {test.__name__}")
        except Exception:
            failures += 1
            print(f"[FAIL] {test.__name__}")
            traceback.print_exc()
    print(f"\n=== engine selftest: {len(TESTS) - failures}/{len(TESTS)} passed ===")
    return 1 if failures else 0


def main():
    logging.basicConfig(level=logging.ERROR)
    logging.disable(logging.WARNING)
    sys.exit(asyncio.run(main_async()))


if __name__ == "__main__":
    main()
