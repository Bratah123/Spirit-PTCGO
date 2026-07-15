"""Headless smoke-test harness for card effects.

Builds a minimal two-AI-player GameSession per test, drives every scripted
attack / ability / trainer / energy hook through the real resolve_* entry
points, and reports PASS/FAIL per (card, ability) without a client, network
stack, or DB.

Usage: python -m spirit.tools.effect_smoke --set SWSH8 [--card Absol_164] [--all]
"""

import argparse
import asyncio
import logging
import os
import random
import re
import sys
import traceback
import uuid
from typing import Any, Dict, List, Optional, Tuple

from spirit.game.attributes import AbilityTypes, AttrID, PokemonStage, PokemonTypes
from spirit.game.data_utils import (
    Ability,
    Activations,
    Attack,
    CARD_DEFS_BY_GUID,
    EnergyCardDef,
    PokemonCardDef,
    PokemonToolCardDef,
    StadiumCardDef,
    TrainerCardDef,
    Triggers,
    has_rule_box,
    unimplemented,
)
from spirit.game.models.board import CardEntity, EnergyEntity, PokemonEntity
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.session import passives
from spirit.game.session.ai_player import AIPlayer
from spirit.game.session.constants import GamePhase
from spirit.game.session.effects import (
    EffectContext,
    resolve_activated_ability,
    resolve_attack,
    resolve_energy_attach_cost,
    resolve_energy_on_attach,
    resolve_trainer_effect,
    resolve_triggered_ability,
)
from spirit.game.session.game_session import GameOver, GameSession
from spirit.game.session.legal_actions import trainer_condition_met

P1 = "smoke-p1"
P2 = "smoke-p2"
TEST_TIMEOUT = 30.0
GUID_RE = re.compile(r"guid\s*=\s*[\"']([0-9a-fA-F-]{36})[\"']")

PASS, FAIL, SKIP, UNIMPL = "PASS", "FAIL", "SKIP", "UNIMPL"


class SmokeSession(GameSession):
    """GameSession whose game-end path never touches the DB or network."""

    # Skip the choreography pacing sleeps so --all runs finish in seconds.
    choreography_pauses = False

    async def end_game(self, winner_id: str, reason: str):
        self.game_phase = GamePhase.GAME_OVER
        raise GameOver()

    async def prompt_selection_message(self, player, msg_name, value,
                                       expected_counter=None):
        # Every legit prompt path early-returns for AIPlayer; reaching here
        # with one means a prompt the AI cannot answer (would hang forever).
        if isinstance(player, AIPlayer):
            raise RuntimeError(
                f"prompt '{msg_name}' reached the wire for an AIPlayer -- "
                f"not auto-answered headlessly"
            )
        return await super().prompt_selection_message(
            player, msg_name, value, expected_counter
        )


class SmokeResult:
    def __init__(self, card: str, kind: str, label: str, status: str,
                 detail: str = "", scripted: bool = True):
        self.card, self.kind, self.label = card, kind, label
        self.status, self.detail, self.scripted = status, detail, scripted


# ----------------------------------------------------------------------
# Target discovery
# ----------------------------------------------------------------------

def discover_targets(set_code: str) -> List[Tuple[str, Any]]:
    """(script_stem, CardDefinition) for every card script in the set dir."""
    set_dir = os.path.join(card_loader.scripts_dir, set_code)
    if not os.path.isdir(set_dir):
        raise SystemExit(f"No script directory for set '{set_code}' ({set_dir})")
    targets = []
    for fname in sorted(os.listdir(set_dir)):
        if not fname.endswith(".py") or fname == "__init__.py":
            continue
        with open(os.path.join(set_dir, fname), "r", encoding="utf-8") as f:
            m = GUID_RE.search(f.read())
        stem = fname[:-3]
        definition = CARD_DEFS_BY_GUID.get(m.group(1).lower()) if m else None
        if definition is not None:
            targets.append((stem, definition))
    return targets


def _def_attr(definition, attr_id: AttrID, default=None):
    spec = definition.extra_attributes.get(str(attr_id.value))
    return spec.get("value", default) if isinstance(spec, dict) else default


def pick_filler_basic() -> Any:
    """Deterministic vanilla Basic Pokemon used to stock both boards."""
    candidates = []
    for definition in CARD_DEFS_BY_GUID.values():
        if not isinstance(definition, PokemonCardDef):
            continue
        if _def_attr(definition, AttrID.STAGE) != PokemonStage.BASIC.value:
            continue
        if has_rule_box(definition.guid):
            continue
        if any(a.effect is not None or a.passive is not None or a.trigger
               for a in definition.abilities):
            continue
        hp = _def_attr(definition, AttrID.HP, 0)
        candidates.append((hp, definition.guid, definition))
    if not candidates:
        raise SystemExit("No vanilla Basic Pokemon loaded to use as board filler")
    candidates.sort(key=lambda t: (-t[0], t[1]))
    return candidates[0][2]


def pick_filler_item() -> Optional[Any]:
    """A plain Item card so 'other Item in hand' conditions hold.

    Exact ItemCardDef only (a Tool/Fossil subclass carries board machinery
    that breaks filler roles); its effect never runs, so effect-less defs
    merely sort first now that every real Item is scripted.
    """
    from spirit.game.data_utils import ItemCardDef
    candidates = [d for d in CARD_DEFS_BY_GUID.values()
                  if type(d) is ItemCardDef and d.condition is None
                  and getattr(d, "passive", None) is None]
    candidates.sort(key=lambda d: (d.effect is not None, d.guid))
    return candidates[0] if candidates else None


def basic_energy_guids() -> Dict[int, str]:
    """PokemonTypes value -> Free_Energy basic energy GUID."""
    out: Dict[int, str] = {}
    for definition in CARD_DEFS_BY_GUID.values():
        if isinstance(definition, EnergyCardDef) and definition.set_code == "Free_Energy":
            out[definition.energy_type.value] = definition.guid
    if not out:
        raise SystemExit("Free_Energy basic energies not loaded")
    return out


# ----------------------------------------------------------------------
# Board construction
# ----------------------------------------------------------------------

class Rig:
    """One fresh session + stocked board per test."""

    def __init__(self, target_def, filler_def, energy_guids: Dict[int, str],
                 item_def=None):
        self.target_def = target_def
        self.filler_def = filler_def
        self.energy_guids = energy_guids
        self.item_def = item_def
        self.session = self._build_session()
        self.board = self.session.board_state

    def _energy_guid(self, type_value: int) -> str:
        return self.energy_guids.get(
            type_value, self.energy_guids[PokemonTypes.WATER.value])

    def _element_type(self) -> int:
        types = []
        if isinstance(self.target_def, PokemonCardDef):
            raw = _def_attr(self.target_def, AttrID.POKEMON_TYPES, "[]")
            import json as _json
            try:
                types = _json.loads(raw) if isinstance(raw, str) else list(raw)
            except (ValueError, TypeError):
                types = []
        return types[0] if types else PokemonTypes.WATER.value

    def _cost_energy_guids(self) -> List[str]:
        """Enough basic energies to cover every attack cost, plus spares."""
        need: Dict[int, int] = {}
        element = self._element_type()
        if isinstance(self.target_def, PokemonCardDef):
            for ability in self.target_def.abilities:
                cost = getattr(ability, "cost", None) or {}
                per: Dict[int, int] = {}
                for ptype, count in cost.items():
                    tval = getattr(ptype, "value", ptype)
                    if tval in (PokemonTypes.COLORLESS.value, PokemonTypes.UNSET.value):
                        tval = element
                    per[tval] = per.get(tval, 0) + count
                for tval, count in per.items():
                    need[tval] = max(need.get(tval, 0), count)
        need[element] = need.get(element, 0) + 2
        guids: List[str] = []
        for tval, count in need.items():
            guids.extend([self._energy_guid(tval)] * count)
        return guids

    def _build_session(self) -> SmokeSession:
        target_guid = self.target_def.guid
        filler_guid = self.filler_def.guid
        water = self.energy_guids[PokemonTypes.WATER.value]
        psychic = self.energy_guids.get(PokemonTypes.PSYCHIC.value, water)
        p1_pile = [target_guid] * 4 + [filler_guid] * 12 + self._cost_energy_guids() \
            + [water] * 4 + [psychic] * 2
        if self.item_def is not None:
            p1_pile += [self.item_def.guid] * 2
        p2_pile = [filler_guid] * 12 + [water] * 8 + [psychic] * 4
        pairing = {
            "is_solo": True,
            "players": {
                P1: {"client": None,
                     "deck": {"deckID": str(uuid.uuid4()), "deckName": "SmokeP1",
                              "piles": {"deck": p1_pile}}},
                P2: {"client": None,
                     "deck": {"deckID": str(uuid.uuid4()), "deckName": "SmokeP2",
                              "piles": {"deck": p2_pile}}},
            },
        }
        return SmokeSession(f"smoke-{uuid.uuid4().hex[:8]}", pairing)

    # -- deck plumbing --------------------------------------------------

    def pull(self, pid: str, predicate) -> Optional[CardEntity]:
        deck = self.board.find_player_area(pid, "deck")
        for card in list(deck.children):
            if predicate(card):
                return card
        return None

    def pull_guid(self, pid: str, guid: str) -> Optional[CardEntity]:
        return self.pull(pid, lambda c: (c.archetype_id or "").lower() == guid.lower())

    def to_area(self, card: Optional[CardEntity], pid: str, area_name: str,
                position: Optional[int] = None) -> Optional[CardEntity]:
        if card is None:
            return None
        area = self.board.find_player_area(pid, area_name)
        self.board.move_card(card.entity_id, area.entity_id, position)
        return card

    def attach(self, card: Optional[CardEntity], pokemon: PokemonEntity):
        if card is not None:
            self.board.attach_card(card.entity_id, pokemon.entity_id)

    def attach_energy_type(self, pid: str, pokemon: PokemonEntity, type_value: int):
        self.attach(self.pull_guid(pid, self._energy_guid(type_value)), pokemon)

    # -- standard layout ------------------------------------------------

    def setup(self, target_kind: str) -> Dict[str, Any]:
        """Places actives/bench/hands/discards; returns key entities."""
        session, board = self.session, self.board
        ts = session.turn_state
        ts.begin_turn(P1)
        ts.begin_turn(P2)
        ts.begin_turn(P1)  # turn 3: past both first-turn restrictions
        session.first_player_id = P1
        session.game_phase = GamePhase.TURN_LOOP

        filler_guid = self.filler_def.guid
        target_guid = self.target_def.guid

        # Opponent side: active + 2 benched fillers, some attached energy.
        p2_active = self.to_area(self.pull_guid(P2, filler_guid), P2, "activePokemonArea")
        p2_bench = [self.to_area(self.pull_guid(P2, filler_guid), P2, "bench")
                    for _ in range(2)]
        if p2_active is not None:
            self.attach_energy_type(P2, p2_active, PokemonTypes.WATER.value)
            self.attach_energy_type(P2, p2_active, PokemonTypes.PSYCHIC.value)
        if p2_bench[0] is not None:
            self.attach_energy_type(P2, p2_bench[0], PokemonTypes.WATER.value)
        for _ in range(4):
            self.to_area(self.pull(P2, lambda c: True), P2, "hand")
        for _ in range(3):
            self.to_area(self.pull(P2, lambda c: True), P2, "discard")

        # Own side.
        target_entity: Optional[CardEntity] = None
        if target_kind == "pokemon":
            target_entity = self.to_area(
                self.pull_guid(P1, target_guid), P1, "activePokemonArea")
            p1_active = target_entity
            # A second copy on the bench (own-copy interactions) and a third
            # in the discard (recursion-style abilities/conditions).
            self.to_area(self.pull_guid(P1, target_guid), P1, "bench")
            self.to_area(self.pull_guid(P1, target_guid), P1, "discard")
        else:
            p1_active = self.to_area(self.pull_guid(P1, filler_guid), P1, "activePokemonArea")
        for _ in range(2):
            self.to_area(self.pull_guid(P1, filler_guid), P1, "bench")
        if isinstance(p1_active, PokemonEntity):
            for guid in self._cost_energy_guids():
                self.attach(self.pull_guid(P1, guid), p1_active)
        # Hand: fillers + energies + a vanilla Item so discard/"other Item in
        # hand" style costs and conditions have fodder. Generic pulls must
        # never consume target copies (the target pull below needs one left).
        not_target = lambda c: (c.archetype_id or "").lower() != target_guid.lower()
        for _ in range(3):
            self.to_area(self.pull_guid(P1, filler_guid), P1, "hand")
        for _ in range(2):
            self.to_area(self.pull(
                P1, lambda c: isinstance(c, EnergyEntity) and not_target(c)),
                P1, "hand")
        if self.item_def is not None and self.item_def.guid.lower() != target_guid.lower():
            self.to_area(self.pull_guid(P1, self.item_def.guid), P1, "hand")
        for _ in range(2):
            self.to_area(self.pull(P1, not_target), P1, "discard")

        if target_kind == "trainer":
            target_entity = self.to_area(self.pull_guid(P1, target_guid), P1, "hand")
        elif target_kind == "energy":
            target_entity = self.to_area(self.pull_guid(P1, target_guid), P1, "hand")

        return {
            "p1_active": p1_active,
            "p2_active": p2_active,
            "target": target_entity,
        }


# ----------------------------------------------------------------------
# Test runners
# ----------------------------------------------------------------------

async def _flush_ctx(session, ctx: Optional[EffectContext]):
    if ctx is None:
        return
    if ctx._messages:
        await session._flush_effect_runs(ctx)
        ctx._messages.clear()
    await session.resolve_knockouts(ctx)
    for hook in ctx.deferred_actions:
        await hook()


def _condition_blocks(definition, ability, rig, entities) -> Optional[str]:
    """Evaluate the offer-gating condition; None = proceed, str = skip note.

    On False, retries under fallback board shapes (first turn, emptied hand)
    so turn-gated / hand-gated cards still get their effect exercised.
    """
    board = rig.board
    if isinstance(ability, Ability) and ability.condition is not None:
        check = lambda: bool(ability.condition(board, P1, entities["p1_active"]))
        label = "ability"
    elif isinstance(definition, TrainerCardDef) \
            and getattr(definition, "condition", None) and ability is None:
        check = lambda: trainer_condition_met(
            definition.condition, board, P1, entities["target"])
        label = "card"
    else:
        return None
    if check():
        return None
    # Fallback 1: rewind to the player's first turn (Battle VIP Pass).
    rig.session.turn_state.turn_number = 1
    if check():
        return None
    # Fallback 1b: stamp the target as this turn's draw (Nugget provenance).
    target = entities.get("target")
    if target is not None:
        rig.session.turn_state.turn_draw_entity_ids.add(target.entity_id)
        if check():
            return None
    # Fallback 1c: a 2nd copy of the target in hand (pair items -- Cross Switcher).
    extra_copy = rig.to_area(rig.pull_guid(P1, definition.guid), P1, "hand")
    if extra_copy is not None and check():
        return None
    # Fallback 2: dump the hand back into the deck (hand-size-gated abilities).
    hand = board.find_player_area(P1, "hand")
    deck = board.find_player_area(P1, "deck")
    target = entities.get("target")
    for card in list(hand.children):
        if card is not target:
            board.move_card(card.entity_id, deck.entity_id)
    if check():
        return None
    # Fallback 3: deal prize piles (prize-gated cards -- Peonia, Shuffle Dance).
    for pid in (P1, P2):
        pile = board.find_player_area(pid, "prizePile")
        if pile is not None and not pile.children:
            board.deal_from_deck(pid, "prizePile", 6)
    if check():
        return None
    # Fallback 4: stamp damage on both boards (heal-gated cards -- Potion).
    for pid in (P1, P2):
        for pokemon in board.pokemon_in_play(pid):
            pokemon.set_attribute(
                AttrID.HP,
                max(10, passives.effective_max_hp(board, pokemon) - 30))
    if check():
        return None
    # Fallback 4b: two Energy on the damaged Active (Hyper Potion).
    p1_active = entities.get("p1_active")
    if isinstance(p1_active, PokemonEntity):
        rig.attach_energy_type(P1, p1_active, PokemonTypes.WATER.value)
        rig.attach_energy_type(P1, p1_active, PokemonTypes.WATER.value)
        if check():
            return None
    rig.session.turn_state.turn_number = 3
    return f"{label} condition returned False on the smoke board (all fallbacks)"


async def run_pokemon_ability(rig: Rig, ability: Ability, entities) -> None:
    session = rig.session
    pokemon = entities["p1_active"]
    is_attack = isinstance(ability, Attack) or ability.ability_type in (
        AbilityTypes.ATTACK, AbilityTypes.NON_DAMAGING_ATTACK)
    if is_attack:
        action_id = ability.ability_id or str(uuid.uuid4())
        await resolve_attack(session, P1, pokemon, ability, action_id)
    elif ability.trigger is not None:
        def _setup(ctx):
            if ability.has_trigger(Triggers.ON_KNOCKED_OUT):
                ctx.ko_from_attack = True
                ctx.ko_attacker = entities["p2_active"]
        await resolve_triggered_ability(session, P1, pokemon, ability, ctx_setup=_setup)
    else:
        await resolve_activated_ability(session, P1, pokemon, ability)


async def run_passive_probe(rig: Rig, entities) -> None:
    board = rig.board
    p1_active, p2_active = entities["p1_active"], entities["p2_active"]
    list(passives.active_passives(board))
    passives.compute_damage(board, p1_active, p2_active, 50, is_attack=True)
    passives.compute_damage(board, p2_active, p1_active, 50, is_attack=True)
    passives.effective_max_hp(board, p1_active)
    passives.effective_retreat_cost(board, p1_active)
    cost_fn = getattr(passives, "effective_attack_cost", None)
    if cost_fn is not None:
        from spirit.game.attributes import CLIENT_POKEMON_TYPE_NAMES
        for ability in getattr(rig.target_def, "abilities", []) or []:
            if isinstance(ability, Attack):
                # Same wire shape legal_actions feeds it: client enum NAME keys.
                cost = {CLIENT_POKEMON_TYPE_NAMES[k]: v
                        for k, v in (ability.cost or {}).items()}
                cost_fn(board, p1_active, cost)


async def run_trainer_effect(rig: Rig, entities) -> None:
    session, board = rig.session, rig.board
    card = entities["target"]
    slot = board.find_global_area("activeTrainer")
    board.move_card(card.entity_id, slot.entity_id)
    ctx = await resolve_trainer_effect(session, P1, card)
    await _flush_ctx(session, ctx)
    # Mirror the engine: the trainer goes to the discard after resolving,
    # unless the effect already moved it (Hisuian Heavy Ball prize swap).
    if card.parent is slot:
        discard = board.find_player_area(P1, "discard")
        board.move_card(card.entity_id, discard.entity_id)


async def run_stadium_ability(rig: Rig, ability: Ability, entities) -> None:
    session, board = rig.session, rig.board
    card = entities["target"]
    slot = board.find_global_area("activeStadium")
    board.move_card(card.entity_id, slot.entity_id)
    await resolve_activated_ability(session, P1, card, ability)


async def run_trainer_trigger(rig: Rig, ability: Ability, entities) -> None:
    """Trainer-declared trigger fired on the hand copy (Dream Ball's window)."""
    await resolve_triggered_ability(rig.session, P1, entities["target"], ability)


async def run_stadium_trigger(rig: Rig, ability: Ability, entities) -> None:
    """Stadium-declared triggered ability (Old Cemetery/Gapejaw Bog watchers)."""
    session, board = rig.session, rig.board
    card = entities["target"]
    slot = board.find_global_area("activeStadium")
    board.move_card(card.entity_id, slot.entity_id)
    receiver = entities["p1_active"]

    def _setup(ctx):
        ctx.attaching_player_id = P1
        ctx.attached_energy = next(iter(receiver.children), None)
        ctx.energy_receiver = receiver
        ctx.benching_player_id = P1
        ctx.benched_pokemon = receiver

    await resolve_triggered_ability(session, P1, card, ability, ctx_setup=_setup)


async def run_tool_granted_ability(rig: Rig, ability: Ability, entities) -> None:
    session, board = rig.session, rig.board
    holder = entities["p1_active"]
    board.attach_card(entities["target"].entity_id, holder.entity_id)
    await session.refresh_granted_abilities(holder)
    await resolve_activated_ability(session, P1, holder, ability)


async def run_energy_attach(rig: Rig, entities) -> None:
    session, board = rig.session, rig.board
    energy = entities["target"]
    target = entities["p1_active"]
    definition = rig.target_def
    if definition.attach_condition is not None \
            and not definition.attach_condition(board, P1):
        raise _SkipTest("attach_condition returned False on the smoke board")
    if definition.attach_to is not None:
        definition.attach_to(target)
    ctx = await resolve_energy_attach_cost(session, P1, energy, target)
    if ctx is None:
        return  # cost hook cancelled the attach; a legal outcome
    await _flush_ctx(session, ctx)
    board.attach_card(energy.entity_id, target.entity_id)
    on_attach_ctx = await resolve_energy_on_attach(session, P1, energy, target)
    await _flush_ctx(session, on_attach_ctx)


async def run_energy_carrier_ko(rig: Rig, entities) -> None:
    session, board = rig.session, rig.board
    energy = entities["target"]
    carrier = entities["p2_active"]
    board.attach_card(energy.entity_id, carrier.entity_id)
    hook = rig.target_def.on_carrier_knocked_out
    ctx = EffectContext(session, P2, entities["p1_active"], None)
    await hook(ctx)
    await _flush_ctx(session, ctx)


class _SkipTest(Exception):
    def __init__(self, note: str):
        self.note = note


# ----------------------------------------------------------------------
# Per-card orchestration
# ----------------------------------------------------------------------

def _plan_tests(definition) -> List[Tuple[str, str, Any, bool]]:
    """(kind_label, ability_label, runner_key, scripted) rows for a card def."""
    plans: List[Tuple[str, str, Any, bool]] = []
    # Fossils (plays_as_pokemon trainers) exercise like Pokemon: abilities + passive.
    if isinstance(definition, PokemonCardDef) \
            or getattr(definition, "plays_as_pokemon", False):
        for ability in definition.abilities:
            scripted = callable(ability.effect)
            if isinstance(ability, Attack) or ability.ability_type in (
                    AbilityTypes.ATTACK, AbilityTypes.NON_DAMAGING_ATTACK):
                plans.append(("attack", ability.title, ability, scripted))
            elif ability.trigger is not None or ability.activation is not None \
                    or callable(ability.effect):
                plans.append(("ability", ability.title, ability, scripted))
            elif ability.passive is not None:
                plans.append(("passive", ability.title, "passive", True))
            elif ability.effect is unimplemented:
                plans.append(("ability", ability.title, ability, False))
        if definition.passive is not None and not any(k == "passive" for k, *_ in plans):
            plans.append(("passive", "(card passive)", "passive", True))
    elif isinstance(definition, StadiumCardDef):
        if callable(definition.effect):
            plans.append(("trainer", "(on play)", "trainer", True))
        elif definition.effect is unimplemented:
            plans.append(("trainer", "(on play)", "trainer", False))
        if definition.ability is not None:
            plans.append(("stadium-ability", definition.ability.title,
                          definition.ability,
                          callable(definition.ability.effect)))
        for ability in definition.abilities:
            if ability.trigger is not None:
                plans.append(("stadium-trigger", ability.title, ability,
                              callable(ability.effect)))
        if definition.passive is not None:
            plans.append(("passive", "(stadium passive)", "stadium-passive", True))
    elif isinstance(definition, PokemonToolCardDef):
        for ability in definition.granted_abilities:
            plans.append(("tool-ability", ability.title, ability,
                          callable(ability.effect)))
        if definition.passive is not None:
            plans.append(("passive", "(tool passive)", "tool-passive", True))
        if callable(definition.effect):
            plans.append(("trainer", "(on play)", "trainer", True))
    elif isinstance(definition, TrainerCardDef):
        scripted = callable(definition.effect)
        plans.append(("trainer", "(on play)", "trainer",
                      scripted))
        for ability in definition.abilities:
            if ability.trigger is not None:
                plans.append(("trainer-trigger", ability.title, ability,
                              callable(ability.effect)))
    elif isinstance(definition, EnergyCardDef):
        if callable(definition.attach_cost) or callable(definition.on_attach):
            plans.append(("energy-attach", "(attach hooks)", "energy-attach", True))
        if callable(definition.on_carrier_knocked_out):
            plans.append(("energy-ko", "(carrier KO hook)", "energy-ko", True))
        if definition.passive is not None:
            plans.append(("passive", "(energy passive)", "energy-passive", True))
    return plans


async def run_one(stem: str, definition, kind: str, label: str, runner_key,
                  filler_def, energy_guids, scripted: bool,
                  timeout: float, item_def=None) -> SmokeResult:
    random.seed(0xC0FFEE)
    rig = Rig(definition, filler_def, energy_guids, item_def)
    target_kind = "pokemon" if isinstance(definition, PokemonCardDef) \
        or getattr(definition, "plays_as_pokemon", False) else \
        "energy" if isinstance(definition, EnergyCardDef) else "trainer"

    async def _drive():
        entities = rig.setup(target_kind)
        needed = "p1_active" if target_kind == "pokemon" else "target"
        if entities.get(needed) is None or entities.get("p1_active") is None:
            raise RuntimeError(
                f"harness rig could not place the {target_kind} target on the board")
        if isinstance(runner_key, Ability):
            note = _condition_blocks(definition, runner_key, rig, entities)
            if note:
                raise _SkipTest(note)
            if kind == "stadium-ability":
                await run_stadium_ability(rig, runner_key, entities)
            elif kind == "stadium-trigger":
                await run_stadium_trigger(rig, runner_key, entities)
            elif kind == "trainer-trigger":
                await run_trainer_trigger(rig, runner_key, entities)
            elif kind == "tool-ability":
                await run_tool_granted_ability(rig, runner_key, entities)
            else:
                await run_pokemon_ability(rig, runner_key, entities)
        elif runner_key == "trainer":
            note = _condition_blocks(definition, None, rig, entities)
            if note:
                raise _SkipTest(note)
            if not scripted:
                raise _SkipTest("effect text not scripted (unimplemented/none)")
            await run_trainer_effect(rig, entities)
        elif runner_key == "energy-attach":
            await run_energy_attach(rig, entities)
        elif runner_key == "energy-ko":
            await run_energy_carrier_ko(rig, entities)
        elif str(runner_key).endswith("passive") or runner_key == "passive":
            if runner_key == "tool-passive":
                rig.board.attach_card(entities["target"].entity_id,
                                      entities["p1_active"].entity_id)
            elif runner_key == "stadium-passive":
                slot = rig.board.find_global_area("activeStadium")
                rig.board.move_card(entities["target"].entity_id, slot.entity_id)
            elif runner_key == "energy-passive":
                rig.board.attach_card(entities["target"].entity_id,
                                      entities["p1_active"].entity_id)
            await run_passive_probe(rig, entities)

    try:
        try:
            await asyncio.wait_for(_drive(), timeout=timeout)
            return SmokeResult(stem, kind, label, PASS, scripted=scripted)
        except GameOver:
            return SmokeResult(stem, kind, label, PASS, "(game ended)", scripted)
        except _SkipTest as skip:
            status = UNIMPL if "not scripted" in skip.note else SKIP
            return SmokeResult(stem, kind, label, status, skip.note, scripted)
        except asyncio.TimeoutError:
            return SmokeResult(stem, kind, label, FAIL,
                               f"timed out after {timeout}s (blocked prompt?)",
                               scripted)
        except Exception:
            tail = "".join(traceback.format_exc().splitlines(keepends=True)[-6:])
            return SmokeResult(stem, kind, label, FAIL, tail.rstrip(), scripted)
    finally:
        rig.session.cleanup()


async def main_async(args) -> int:
    card_loader.load_all()
    filler_def = pick_filler_basic()
    energy_guids = basic_energy_guids()
    item_def = pick_filler_item()

    targets = discover_targets(args.set)
    if args.card:
        wanted = args.card.lower()
        targets = [(s, d) for s, d in targets if s.lower() == wanted]
        if not targets:
            print(f"No script named '{args.card}' in set {args.set}")
            return 2

    results: List[SmokeResult] = []
    for stem, definition in targets:
        plans = _plan_tests(definition)
        if not plans:
            result = SmokeResult(stem, "-", "(no behaviors)", SKIP,
                                 "vanilla card: nothing to execute", False)
            results.append(result)
            if args.verbose:
                _print_result(result)
            continue
        for kind, label, runner_key, scripted in plans:
            result = await run_one(stem, definition, kind, label, runner_key,
                                   filler_def, energy_guids, scripted,
                                   args.timeout, item_def)
            results.append(result)
            if args.verbose or result.status == FAIL:
                _print_result(result)

    _print_summary(results, args)
    return 1 if any(r.status == FAIL for r in results) else 0


def _print_result(r: SmokeResult):
    line = f"[{r.status:6}] {r.card:32} {r.kind:15} {r.label}"
    print(line)
    if r.detail:
        for detail_line in r.detail.splitlines():
            print(f"         {detail_line}")


def _print_summary(results: List[SmokeResult], args):
    counts: Dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    scripted = [r for r in results if r.scripted and r.status in (PASS, FAIL)]
    scripted_pass = sum(1 for r in scripted if r.status == PASS)
    print()
    print(f"=== effect smoke: set {args.set} ===")
    print(f"tests: {len(results)}  "
          + "  ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    print(f"scripted effects exercised: {len(scripted)} "
          f"(PASS {scripted_pass} / FAIL {len(scripted) - scripted_pass})")
    fails = [r for r in results if r.status == FAIL]
    if fails:
        print("\nfailures:")
        for r in fails:
            print(f"  {r.card} :: {r.kind} :: {r.label}")


def main():
    parser = argparse.ArgumentParser(
        description="Headless smoke tests for card-effect scripts.")
    parser.add_argument("--set", required=True, help="Set code (script dir name)")
    parser.add_argument("--card", help="Single card script stem, e.g. Absol_164")
    parser.add_argument("--all", action="store_true",
                        help="Run every card in the set (default when --card omitted)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print every result, not just failures")
    parser.add_argument("--timeout", type=float, default=TEST_TIMEOUT)
    args = parser.parse_args()
    logging.basicConfig(level=logging.ERROR)
    if not args.verbose:
        logging.disable(logging.WARNING)
    sys.exit(asyncio.run(main_async(args)))


if __name__ == "__main__":
    main()
