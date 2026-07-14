"""Legal-action computation for the main turn loop.

Builds the targetMap of a SelectionWithTargetsAndActionsRequired offer; the
client highlights exactly those entities (it does no legality checks itself).
"""

import logging
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

from spirit.game.attributes import (
    AttrID,
    CLIENT_SPECIAL_CONDITION_NAMES,
    PokemonStage,
    PokemonTypes,
    POKEMON_TYPES_BY_CLIENT_NAME,
    SpecialConditions,
    TrainerType,
)
from spirit.game.data_utils import ABILITIES_BY_ID, Activations, def_for
from spirit.game.models.board import (
    BoardState,
    EnergyEntity,
    PokemonEntity,
    TrainerEntity,
)
from .constants import (
    PROMPT_RETREAT_COST,
    PROMPT_RETREAT_NEW_ACTIVE,
    SelectionKind,
)
from .passives import (
    ability_locked,
    can_attack_despite_conditions,
    can_evolve_early,
    effective_attack_cost,
    effective_bench_capacity,
    effective_retreat_cost,
    energy_provided_options,
    evolution_blocked,
    retreat_blocked,
    tool_slots_free,
    trainer_play_blocked,
)


# Semantic action names from the client's Actions enum / SelectableActionUtil.
ACTION_PLAY_POKEMON = "DefaultPokemonPlayAbility"
ACTION_EVOLVE = "EvolvePokemonPlayAbility"
ACTION_PLAY_ENERGY = "DefaultEnergyPlayAbility"
ACTION_USE_TRAINER = "UseTrainerCard"
ACTION_PLAY_STADIUM = "DefaultStadiumPlayAbility"
ACTION_USE_ABILITY = "UsePokemonAbility"
ACTION_USE_ATTACK = "UsePokemonAttack"
ACTION_RETREAT = "BaseRetreat"
# No dedicated tool member exists in the client's Actions enum; the string is
# free-form (only the action-panel icon lookup reads it) and the drop target
# comes from the target node's validTargets, exactly like energy.
ACTION_ATTACH_TOOL = "DefaultToolPlayAbility"

# Conditions that stop the Active from attacking or retreating.
_IMMOBILIZING_CONDITIONS = {
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP],
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.PARALYZED],
}

# ActionsNode Kind: "Ability" (j.V) auto-resolves plays; "AbilitySelection" (K.O) opens the ability panel.
SELECTION_TYPE_PLAY = SelectionKind.ABILITY.value
SELECTION_TYPE_PANEL = SelectionKind.ABILITY_SELECTION.value

# Energy cost types that any energy card can pay.
_WILDCARD_COST_TYPES = (PokemonTypes.NO_COLOR.value, PokemonTypes.COLORLESS.value)

_ACTION_ID_NAMESPACE = uuid.UUID("f6c1b1de-5e1a-4b52-9c40-1d1c4e6a7b0d")

# Sentinel lock horizon: stays locked until the Pokemon leaves the Active spot.
LOCK_UNTIL_LEAVES_ACTIVE = 10 ** 9


def action_id_for(entity_id: str, verb: str) -> str:
    """Deterministic GUID action ID (must be a GUID: the client runs new Guid(id))."""
    return str(uuid.uuid5(_ACTION_ID_NAMESPACE, f"{entity_id}:{verb}"))


@dataclass
class TurnState:
    """Per-game turn bookkeeping consumed by the legality rules."""

    turn_number: int = 0
    active_player_id: Optional[str] = None
    supporter_played: bool = False
    energy_attached: bool = False
    retreated: bool = False
    # entity_id -> turn number it entered play (or last evolved). Entities
    # placed during setup are absent and default to turn 0.
    entered_play_turn: Dict[str, int] = field(default_factory=dict)
    # (entity_id, ability_id) pairs used this turn (once-per-turn abilities).
    used_abilities: Set[Tuple[str, str]] = field(default_factory=set)
    # Ability names used this turn that are "1 per turn" shared across copies
    # (Dark Asset, Flower Selecting, Dragon's Hoard).
    used_named_abilities: Set[str] = field(default_factory=set)
    # Players who already used their once-per-game VSTAR Power.
    vstar_used: Set[str] = field(default_factory=set)
    # (entity_id, ability_id) -> last turn number the attack stays locked
    # ("during your next turn, this Pokemon can't use ...").
    attack_locks: Dict[Tuple[str, str], int] = field(default_factory=dict)
    # entity_id -> last turn number retreat stays locked ("the Defending
    # Pokemon can't retreat"); LOCK_UNTIL_LEAVES_ACTIVE = until it leaves.
    retreat_locks: Dict[str, int] = field(default_factory=dict)
    # Turn-scoped attacker-side damage boosts (Power Tablet); pruned by
    # expires_after_turn each begin_turn (None = this turn only).
    damage_modifiers: List[Any] = field(default_factory=list)
    # --- two-turn history ledgers, rotated this-turn -> last-turn ---
    # (archetype_id, display_name, trainer_type) per trainer/stadium played.
    trainers_played: List[Tuple[str, str, int]] = field(default_factory=list)
    # (entity_id, archetype_id, attack_title) per declared attack.
    attacks_used: List[Tuple[str, str, str]] = field(default_factory=list)
    # victim owner player_id -> [{archetype_id, subtypes}] for attack KOs.
    kos_by_attack: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    # entity_id -> damage dealt to it by the other side this turn.
    damage_taken: Dict[str, int] = field(default_factory=dict)
    # player_id -> prize cards taken this turn.
    prizes_taken: Dict[str, int] = field(default_factory=dict)
    retreated_entities: Set[str] = field(default_factory=set)
    healed_entities: Set[str] = field(default_factory=set)
    turn_draw_entity_ids: Set[str] = field(default_factory=set)
    trainers_played_last_turn: List[Tuple[str, str, int]] = field(default_factory=list)
    attacks_used_last_turn: List[Tuple[str, str, str]] = field(default_factory=list)
    kos_by_attack_last_turn: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    damage_taken_last_turn: Dict[str, int] = field(default_factory=dict)
    prizes_taken_last_turn: Dict[str, int] = field(default_factory=dict)
    retreated_entities_last_turn: Set[str] = field(default_factory=set)
    healed_entities_last_turn: Set[str] = field(default_factory=set)
    turn_draw_entity_ids_last_turn: Set[str] = field(default_factory=set)
    # entity_id -> turn it last moved into the Active spot (persistent stamp).
    became_active_turn: Dict[str, int] = field(default_factory=dict)
    # player_id -> [(card_predicate, expires_after_turn)] play restrictions
    # ("your opponent can't play Item cards during their next turn"); a None
    # expiry holds until cleared.
    play_locks: Dict[str, List[Tuple[Any, Optional[int]]]] = field(default_factory=dict)
    # entity_id -> last turn number energy may not be attached to it (Masquerain).
    attach_restrictions: Dict[str, int] = field(default_factory=dict)
    # Entities whose ON_MOVE_TO_ACTIVE trigger already fired this turn.
    on_move_to_active_fired: Set[str] = field(default_factory=set)
    # Whether the turn player used their once-per-turn attack-coin re-flip
    # (Glimwood Tangle); only actually re-flipping consumes it.
    attack_coin_reroll_used: bool = False
    # entity_id -> (through_turn, flip_title): a Smokescreen-family check --
    # this entity must flip a coin to attack, tails cancels the attack.
    attack_flip_checks: Dict[str, Tuple[int, str]] = field(default_factory=dict)
    # Entities whose attacks ignore effects on the opponent's Active THIS turn
    # (Phoebe); cleared every begin_turn.
    ignore_target_effects_entities: Set[str] = field(default_factory=set)
    # player_id -> attack titles that player declared on THEIR previous turn
    # ("If 1 of your Pokemon used Yoga Loop during your last turn...").
    attack_titles_prev_turn_by_player: Dict[str, List[str]] = field(default_factory=dict)
    # This-turn bonus-prize watches (Sky Seal Stone's Star Order):
    # {player_id, attacker_predicate, target_predicate, prizes}; consulted by
    # resolve_knockouts on attack-damage KOs, cleared every begin_turn.
    extra_prize_watchers: List[Dict[str, Any]] = field(default_factory=list)

    def begin_turn(self, player_id: str, board: Optional[Any] = None):
        """Advances to the next turn, resets the once-per-turn flags, rotates
        the two-turn history, and prunes expired turn-scoped effects."""
        if self.active_player_id:
            self.attack_titles_prev_turn_by_player[self.active_player_id] = [
                title for _, _, title in self.attacks_used
            ]
        self.turn_number += 1
        self.active_player_id = player_id
        self.supporter_played = False
        self.energy_attached = False
        self.retreated = False
        self.used_abilities = set()
        self.used_named_abilities = set()
        self.damage_modifiers = [
            m for m in self.damage_modifiers
            if getattr(m, "expires_after_turn", None) is not None
            and m.expires_after_turn >= self.turn_number
        ]
        self.trainers_played_last_turn = self.trainers_played
        self.trainers_played = []
        self.attacks_used_last_turn = self.attacks_used
        self.attacks_used = []
        self.kos_by_attack_last_turn = self.kos_by_attack
        self.kos_by_attack = {}
        self.damage_taken_last_turn = self.damage_taken
        self.damage_taken = {}
        self.prizes_taken_last_turn = self.prizes_taken
        self.prizes_taken = {}
        self.retreated_entities_last_turn = self.retreated_entities
        self.retreated_entities = set()
        self.healed_entities_last_turn = self.healed_entities
        self.healed_entities = set()
        self.turn_draw_entity_ids_last_turn = self.turn_draw_entity_ids
        self.turn_draw_entity_ids = set()
        self.on_move_to_active_fired = set()
        self.attack_coin_reroll_used = False
        self.play_locks = {
            pid: kept for pid, locks in self.play_locks.items()
            if (kept := [(p, exp) for p, exp in locks
                         if exp is None or exp >= self.turn_number])
        }
        self.attach_restrictions = {
            eid: exp for eid, exp in self.attach_restrictions.items()
            if exp >= self.turn_number
        }
        self.attack_flip_checks = {
            eid: entry for eid, entry in self.attack_flip_checks.items()
            if entry[0] >= self.turn_number
        }
        self.ignore_target_effects_entities = set()
        self.extra_prize_watchers = []
        if board is not None:
            board.temporary_passives = [
                tp for tp in (getattr(board, "temporary_passives", None) or [])
                if tp.expires_after_turn is None
                or tp.expires_after_turn >= self.turn_number
            ]

    def mark_entered_play(self, entity_id: str):
        self.entered_play_turn[entity_id] = self.turn_number

    def lock_attack(self, entity_id: str, ability_id: str):
        """Locks an attack through its user's next turn."""
        self.attack_locks[(entity_id, ability_id)] = self.turn_number + 2

    def attack_locked(self, entity_id: str, ability_id: str) -> bool:
        return self.turn_number <= self.attack_locks.get((entity_id, ability_id), 0)

    def lock_retreat(self, entity_id: str, through_turn: Optional[int] = None):
        """Blocks retreat through `through_turn` (default: the opponent's next turn)."""
        self.retreat_locks[entity_id] = (
            self.turn_number + 1 if through_turn is None else through_turn
        )

    def retreat_locked(self, entity_id: str) -> bool:
        return self.turn_number <= self.retreat_locks.get(entity_id, 0)

    def lock_plays(self, player_id: str, predicate, through_turn: Optional[int] = None):
        """Forbids `player_id` playing hand cards matching `predicate`
        (default: through their next turn)."""
        self.play_locks.setdefault(player_id, []).append(
            (predicate, self.turn_number + 1 if through_turn is None else through_turn)
        )

    def play_locked(self, player_id: str, card: Any) -> bool:
        return any(
            (exp is None or self.turn_number <= exp) and pred(card)
            for pred, exp in self.play_locks.get(player_id, [])
        )

    def restrict_attachments(self, entity_id: str, through_turn: Optional[int] = None):
        """Forbids energy attachments onto `entity_id` (default: through the
        opponent's next turn)."""
        self.attach_restrictions[entity_id] = (
            self.turn_number + 1 if through_turn is None else through_turn
        )

    def attach_restricted(self, entity_id: str) -> bool:
        return self.turn_number <= self.attach_restrictions.get(entity_id, -1)

    def set_attack_flip_check(self, entity_id: str, through_turn: Optional[int] = None,
                              title: str = ""):
        """Requires a coin flip before `entity_id` attacks (tails = the attack
        doesn't happen); default lifetime: through the opponent's next turn."""
        self.attack_flip_checks[entity_id] = (
            self.turn_number + 1 if through_turn is None else through_turn,
            title,
        )

    def attack_flip_check(self, entity_id: str) -> Optional[str]:
        """The flip title when `entity_id` must flip to attack this turn, else None."""
        entry = self.attack_flip_checks.get(entity_id)
        if entry is not None and self.turn_number <= entry[0]:
            return entry[1]
        return None

    def may_evolve_target(self, entity_id: str) -> bool:
        """A Pokemon may evolve only if it has been in play since a previous
        turn, and never during either player's first turn (turns 1 and 2)."""
        if self.turn_number <= 2:
            return False
        return self.entered_play_turn.get(entity_id, 0) < self.turn_number


def selectable_action(
    game_id: str,
    action_id: str,
    description: str,
    selection_type: str = SELECTION_TYPE_PLAY,
) -> Dict[str, Any]:
    """Builds a SelectableAction wire dict."""
    return {
        "gameID": game_id,
        "actionID": action_id,
        "description": description,
        "selectionType": selection_type,
    }


def entity_list_target_info(
    valid_targets: List[str],
    number_to_select: int = 1,
    minimum_to_select: int = 1,
    forced: bool = True,
    kind: str = SelectionKind.ENTITY_LIST.value,
) -> Dict[str, Any]:
    """Builds an interactive EntityListTargetInformation wire dict."""
    return {
        "name": kind,
        "selected": True,
        "validTargets": valid_targets,
        "numberToSelect": number_to_select,
        "minimumToSelect": minimum_to_select,
        "forced": forced,
    }


def _target_map_entry(
    game_id: str,
    entity_id: str,
    action_id: str,
    description: str,
    target_infos: Optional[List[Dict[str, Any]]] = None,
    selection_type: str = SELECTION_TYPE_PLAY,
) -> Dict[str, Any]:
    return {
        "entityID": entity_id,
        "selectableAction": selectable_action(
            game_id, action_id, description, selection_type
        ),
        "targetInfoLst": target_infos or [],
    }


def energy_provided_count(energy: EnergyEntity, board: Optional[BoardState] = None) -> int:
    """How much one energy card pays toward a cost (client s.y: max option
    length); with a board, provided-modifying passives apply."""
    options = energy_provided_options(board, energy)
    return max((len(option) for option in options), default=1)


def _energy_provided_types(energy: EnergyEntity, board: Optional[BoardState] = None) -> set:
    """The set of types one energy can provide (union of the options)."""
    provided = set()
    for option in energy_provided_options(board, energy):
        provided.update(option)
    return provided


def attack_cost_satisfied(cost: Dict[str, int], energies: List[EnergyEntity],
                          board: Optional[BoardState] = None) -> bool:
    """Whether the attached energies can pay an attack's cost.

    Each card pays up to its provided count (Double Turbo pays 2); typed
    requirements consume the most type-constrained cards first, colorless
    accepts whatever capacity remains.
    """
    pool = [
        {"types": _energy_provided_types(e, board), "count": energy_provided_count(e, board)}
        for e in energies
    ]
    colorless_needed = 0
    for type_key, count in (cost or {}).items():
        # Wire cost keys are client enum names ("Grass"); accept legacy ints too.
        if type_key in POKEMON_TYPES_BY_CLIENT_NAME:
            type_val = POKEMON_TYPES_BY_CLIENT_NAME[type_key].value
        else:
            type_val = int(type_key)
        if type_val in _WILDCARD_COST_TYPES:
            colorless_needed += count
            continue
        for _ in range(count):
            candidates = [p for p in pool if type_val in p["types"]]
            if not candidates:
                return False
            candidates.sort(key=lambda p: len(p["types"]))
            chosen = candidates[0]
            chosen["count"] -= 1
            if chosen["count"] <= 0:
                pool.remove(chosen)
    return sum(p["count"] for p in pool) >= colorless_needed


def pokemon_without_tool(pokemon: Any) -> bool:
    """A Pokemon may hold one Pokemon Tool (server rule; client has no cap)."""
    return not any(
        child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
        for child in pokemon.children
    )


def _active_immobilized(board: BoardState, player_id: str) -> bool:
    """Asleep/Paralyzed Actives can neither attack nor retreat."""
    active = board.active_pokemon(player_id)
    conditions = active.get_attribute(AttrID.SPECIAL_CONDITIONS) if active else None
    return any(c in _IMMOBILIZING_CONDITIONS for c in (conditions or []))


def compute_legal_actions(
    board: BoardState,
    state: TurnState,
    player_id: str,
    game_id: str,
) -> List[Dict[str, Any]]:
    """All legal plays for the acting player, as targetMap entries."""
    entries: List[Dict[str, Any]] = []

    hand_area = board.find_player_area(player_id, "hand")
    bench_area = board.find_player_area(player_id, "bench")
    if not hand_area or not bench_area:
        return entries

    in_play = board.pokemon_in_play(player_id)
    in_play_ids = [p.entity_id for p in in_play]
    bench_has_space = len(bench_area.children) < effective_bench_capacity(board, player_id)

    for card in hand_area.children:
        if isinstance(card, PokemonEntity):
            stage = card.get_attribute(AttrID.STAGE)
            if stage == PokemonStage.BASIC.value:
                if getattr(def_for(card.archetype_id), "unplayable_from_hand", False):
                    continue  # Shedinja: enters play only via an effect
                # Fossils stay Item cards in hand: Item locks gate the bench play.
                if card.get_attribute(AttrID.TRAINER_TYPE) is not None \
                        and (state.play_locked(player_id, card)
                             or trainer_play_blocked(board, player_id, card)):
                    continue
                if bench_has_space:
                    # The bench area is the drop target; without it the drag
                    # dead-ends at the ActionsNode and nothing highlights.
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "play"), ACTION_PLAY_POKEMON,
                        [entity_list_target_info([bench_area.entity_id])],
                    ))
                continue

            evolves_from = card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
            if not evolves_from:
                continue
            evolve_targets = [
                p.entity_id for p in in_play
                if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == evolves_from
                and not evolution_blocked(board, player_id, p)
                and (state.may_evolve_target(p.entity_id)
                     or can_evolve_early(board, p))
            ]
            if evolve_targets:
                entries.append(_target_map_entry(
                    game_id, card.entity_id,
                    action_id_for(card.entity_id, "evolve"), ACTION_EVOLVE,
                    [entity_list_target_info(evolve_targets)],
                ))

        elif isinstance(card, EnergyEntity):
            if state.energy_attached or not in_play_ids:
                continue
            if state.play_locked(player_id, card):
                continue
            definition = def_for(card.archetype_id)
            condition = getattr(definition, "attach_condition", None)
            if condition is not None and not condition(board, player_id):
                continue
            attach_to = getattr(definition, "attach_to", None)
            targets = [
                p.entity_id for p in in_play
                if (attach_to is None or attach_to(p))
                and not state.attach_restricted(p.entity_id)
            ]
            if targets:
                entries.append(_target_map_entry(
                    game_id, card.entity_id,
                    action_id_for(card.entity_id, "energy"), ACTION_PLAY_ENERGY,
                    [entity_list_target_info(targets)],
                ))

        elif isinstance(card, TrainerEntity):
            trainer_type = card.get_attribute(AttrID.TRAINER_TYPE)
            if state.play_locked(player_id, card) \
                    or trainer_play_blocked(board, player_id, card):
                continue
            definition = def_for(card.archetype_id)
            condition = getattr(definition, "condition", None)
            if condition is not None \
                    and not trainer_condition_met(condition, board, player_id, card):
                continue
            if trainer_type == TrainerType.ITEM.value:
                entries.append(_target_map_entry(
                    game_id, card.entity_id,
                    action_id_for(card.entity_id, "item"), ACTION_USE_TRAINER,
                ))
            elif trainer_type == TrainerType.SUPPORTER.value:
                if not state.supporter_played and state.turn_number > 1:
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "supporter"), ACTION_USE_TRAINER,
                    ))
            elif trainer_type == TrainerType.STADIUM.value:
                if not _same_stadium_in_play(board, card):
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "stadium"), ACTION_PLAY_STADIUM,
                    ))
            elif trainer_type == TrainerType.POKEMON_TOOL.value:
                tool_attach_to = getattr(definition, "attach_to", None)
                tool_targets = [
                    p.entity_id for p in in_play
                    if tool_slots_free(board, p) > 0
                    and (tool_attach_to is None or tool_attach_to(p))
                ]
                if tool_targets:
                    entries.append(_target_map_entry(
                        game_id, card.entity_id,
                        action_id_for(card.entity_id, "tool"), ACTION_ATTACH_TOOL,
                        [entity_list_target_info(tool_targets)],
                    ))

    entries.extend(_ability_entries(board, state, player_id, game_id, in_play))
    entries.extend(_out_of_zone_ability_entries(board, state, player_id, game_id))
    entries.extend(_stadium_ability_entries(board, state, player_id, game_id))
    # Asleep/Paralyzed gates attacks per-attack (Attack(usable_despite_conditions)).
    immobilized = _active_immobilized(board, player_id)
    entries.extend(_attack_entries(board, state, player_id, game_id, immobilized))
    if not immobilized:
        entries.extend(_retreat_entry(board, state, player_id, game_id))
    # A turn kept alive past an attack (Fluffy Barrage's second strike) stays
    # in the attack phase: only attacking (or End Turn) remains legal.
    if state.attacks_used:
        entries = [
            e for e in entries
            if e["selectableAction"]["description"] == ACTION_USE_ATTACK
        ]
    return entries


def _ability_entries(
    board: BoardState,
    state: TurnState,
    player_id: str,
    game_id: str,
    in_play: List[PokemonEntity],
) -> List[Dict[str, Any]]:
    """Usable activated abilities on the player's in-play Pokemon."""
    entries = []
    for pokemon in in_play:
        locked = ability_locked(board, pokemon)
        for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
            if not isinstance(entry, dict):
                continue
            ability_id = entry.get("abilityID")
            ability = ABILITIES_BY_ID.get(ability_id) if ability_id else None
            if ability is None or ability.activation not in (
                    Activations.ONCE_PER_TURN, Activations.UNLIMITED):
                continue
            # Path to the Peak locks a Pokemon's own Abilities, but a Tool-
            # granted ability (Forest Seal Stone) lives on the tool, not the
            # Pokemon, so it stays usable.
            if locked and not ability.is_granted:
                continue
            if ability.activation != Activations.UNLIMITED \
                    and (pokemon.entity_id, ability_id) in state.used_abilities:
                continue
            if ability.vstar and player_id in state.vstar_used:
                continue
            if ability.effect is None:
                continue
            if ability.shared_once_per_turn \
                    and ability.shared_once_per_turn in state.used_named_abilities:
                continue
            if ability.condition and not ability.condition(board, player_id, pokemon):
                continue
            # The actionID must be the PIE_ABILITIES abilityID so the pulled-
            # back panel can resolve the ability's text.
            entries.append(_target_map_entry(
                game_id, pokemon.entity_id, ability_id, ACTION_USE_ABILITY,
                selection_type=SELECTION_TYPE_PANEL,
            ))
    return entries


def _out_of_zone_ability_entries(
    board: BoardState, state: TurnState, player_id: str, game_id: str
) -> List[Dict[str, Any]]:
    """Abilities flagged usable_from='hand'/'discard' on the player's cards in
    those zones, offered with the OutOfPlay selection flow (b.h).

    Ruling: ability locks (Path to the Peak) read "Pokemon in play", so they
    do NOT gate hand/discard sources.
    """
    entries = []
    for zone in ("hand", "discard"):
        area = board.find_player_area(player_id, zone)
        for card in (area.children if area else []):
            for entry in card.get_attribute(AttrID.PIE_ABILITIES) or []:
                if not isinstance(entry, dict):
                    continue
                ability_id = entry.get("abilityID")
                ability = ABILITIES_BY_ID.get(ability_id) if ability_id else None
                if ability is None or ability.usable_from != zone:
                    continue
                if ability.effect is None:
                    continue
                if ability.activation not in (
                        Activations.ONCE_PER_TURN, Activations.UNLIMITED):
                    continue
                if ability.activation != Activations.UNLIMITED \
                        and (card.entity_id, ability_id) in state.used_abilities:
                    continue
                if ability.vstar and player_id in state.vstar_used:
                    continue
                if ability.shared_once_per_turn \
                        and ability.shared_once_per_turn in state.used_named_abilities:
                    continue
                if ability.condition and not ability.condition(board, player_id, card):
                    continue
                entries.append(_target_map_entry(
                    game_id, card.entity_id, ability_id, ACTION_USE_ABILITY,
                    selection_type=SelectionKind.OUT_OF_PLAY.value,
                ))
    return entries


def _stadium_ability_entries(
    board: BoardState, state: TurnState, player_id: str, game_id: str
) -> List[Dict[str, Any]]:
    """The in-play Stadium's activated ability (Training Court), offered once
    during each player's turn. Only the active player is offered actions and
    used_abilities resets each turn, so (stadium, ability) is a clean
    once-per-player-turn key."""
    stadium_area = board.find_global_area("activeStadium")
    entries = []
    for stadium in (stadium_area.children if stadium_area else []):
        definition = def_for(stadium.archetype_id)
        ability = getattr(definition, "ability", None)
        if ability is None or ability.effect is None or not ability.ability_id:
            continue
        if (stadium.entity_id, ability.ability_id) in state.used_abilities:
            continue
        if ability.condition and not ability.condition(board, player_id, stadium):
            continue
        entries.append(_target_map_entry(
            game_id, stadium.entity_id, ability.ability_id, ACTION_USE_ABILITY,
            selection_type=SELECTION_TYPE_PANEL,
        ))
    return entries


def _retreat_entry(
    board: BoardState, state: TurnState, player_id: str, game_id: str
) -> List[Dict[str, Any]]:
    """Retreat offer for the Active (once per turn, cost payable, bench occupied)."""
    if state.retreated:
        return []
    active = board.active_pokemon(player_id)
    if not active:
        return []
    if state.retreat_locked(active.entity_id) or retreat_blocked(board, active):
        return []
    bench_area = board.find_player_area(player_id, "bench")
    bench_ids = [
        c.entity_id for c in (bench_area.children if bench_area else [])
        if isinstance(c, PokemonEntity)
    ]
    if not bench_ids:
        return []
    cost = effective_retreat_cost(board, active)
    energies = board.attached_energies(active)
    if sum(energy_provided_count(e, board) for e in energies) < cost:
        return []

    # New active FIRST, cost LAST: the Done button only renders on a node with
    # no successor (NodeToAdvanceTo()==null), and SelectingForAnAbility()
    # special-cases the RetreatNewActive kind as an action's first node.
    new_active_info = entity_list_target_info(
        bench_ids, kind=SelectionKind.RETREAT_NEW_ACTIVE.value
    )
    new_active_info["targetPrompt"] = {"id": PROMPT_RETREAT_NEW_ACTIVE}
    infos = [new_active_info]
    if cost > 0:
        # d.j's pip tray tallies each picked card's provided amount against
        # valueToSelect (a double energy pays 2); numberToSelect only caps
        # the card count. targetPrompt is the tray's label (it caches the
        # last prompt shown, so leaving it unset displays stale text).
        info = entity_list_target_info(
            [e.entity_id for e in energies],
            number_to_select=cost,
            minimum_to_select=-1,
            kind=SelectionKind.RETREAT_COST_ENTITY_LIST.value,
        )
        info["valueToSelect"] = cost
        info["targetPrompt"] = {"id": PROMPT_RETREAT_COST}
        infos.append(info)
    return [_target_map_entry(
        game_id, active.entity_id,
        action_id_for(active.entity_id, "retreat"), ACTION_RETREAT,
        infos, selection_type=SELECTION_TYPE_PANEL,
    )]


def trainer_condition_met(condition, board: BoardState, player_id: str, card) -> bool:
    """condition(board, player_id[, card]) -- 3-arg variants get the specific
    hand copy (Nugget's turn-draw provenance is per-card)."""
    code = getattr(condition, "__code__", None)
    if code is not None and code.co_argcount >= 3:
        return bool(condition(board, player_id, card))
    return bool(condition(board, player_id))


def _same_stadium_in_play(board: BoardState, card: TrainerEntity) -> bool:
    """A Stadium is unplayable if one with the same archetype is in play."""
    stadium_area = board.find_global_area("activeStadium")
    return any(
        getattr(existing, "archetype_id", None) == card.archetype_id
        for existing in (stadium_area.children if stadium_area else [])
    )


def _attack_entries(
    board: BoardState, state: TurnState, player_id: str, game_id: str,
    immobilized: bool = False,
) -> List[Dict[str, Any]]:
    """Usable attacks of the Active Pokemon (energy requirement met)."""
    active = board.active_pokemon(player_id)
    if not active:
        return []
    # A passive (Windup Arm) can exempt the whole Pokemon from the gate.
    if immobilized and can_attack_despite_conditions(board, active):
        immobilized = False
    abilities = active.get_attribute(AttrID.PIE_ABILITIES) or []
    if not isinstance(abilities, list):
        logging.warning(
            f"[LegalActions] Unparsed PIE_ABILITIES on {active.entity_id}: {abilities!r}"
        )
        return []

    energies = board.attached_energies(active)
    entries = []
    for ability in abilities:
        # abilityType carries the PieAbilityDescription class-name hint string.
        if ability.get("abilityType") != "Attack":
            continue
        ability_id = ability.get("abilityID")
        if not ability_id:
            continue  # legacy scripts without ability IDs can't be offered
        if state.attack_locked(active.entity_id, ability_id):
            continue
        definition = ABILITIES_BY_ID.get(ability_id)
        # Asleep/Paralyzed suppression, per-attack exemptable (Windup Arm).
        if immobilized and not getattr(definition, "usable_despite_conditions", False):
            continue
        # The player going first cannot attack on turn 1 unless the attack
        # explicitly allows it (Indeedee's Watch Over).
        if state.turn_number == 1 \
                and not getattr(definition, "usable_first_turn", False):
            continue
        if definition is not None and definition.vstar \
                and player_id in state.vstar_used:
            continue
        # Attack usage restriction ("You can use this attack only if...").
        if definition is not None and definition.condition is not None \
                and not definition.condition(board, player_id, active):
            continue
        # Cost-modifying passives (e.g. Excited Heart) apply here.
        cost = effective_attack_cost(board, active, ability.get("cost") or {})
        if attack_cost_satisfied(cost, energies, board):
            entries.append(_target_map_entry(
                game_id, active.entity_id, ability_id, ACTION_USE_ATTACK,
                selection_type=SELECTION_TYPE_PANEL,
            ))
    return entries


# TargetInformation kind: l.m node -> command l.L renders the choices (full
# PieAbilityDescription rows: cost pips, damage, owner type) in the panel's
# bonus ability scroll list.
KIND_CAKE_ATTACK_CHOICE = "CakeAttackCustomChoiceTargetInformation"


def copy_attack_choice_node(
    source_entity_id: str,
    candidates: List[Tuple[Any, Any]],
    prompt: str = "",
) -> Dict[str, Any]:
    """A CakeAttackCustomChoiceTargetInformation node whose `choices` are the
    [(pokemon, attack)] candidates' PieAbilityDescription dicts; the reply
    rides an IntTargetResponse (`amount` = candidate index). Never build one
    from an empty list (l.L's scroll list would soft-lock)."""
    choices: List[Dict[str, Any]] = []
    for i, (pokemon, attack) in enumerate(candidates):
        row = attack.to_dict()
        # Each choice needs its own GUID: l.L matches the clicked button by ID.
        row["abilityID"] = action_id_for(source_entity_id, f"copychoice:{i}")
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        row["bonusInfo"] = {
            "originalOwnerTypes": list(types) or [PokemonTypes.COLORLESS.value]
        }
        choices.append(row)
    return {
        "name": KIND_CAKE_ATTACK_CHOICE,
        "selected": True,
        "targetPrompt": {"id": prompt},
        "sortType": None,
        "choices": choices,
    }
