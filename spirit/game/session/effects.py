"""Card-effect execution engine.

Card scripts receive an EffectContext (`ctx`) and act through its primitives
(deal_damage, draw_cards, search_deck, switch_active, ...); every primitive
updates the server board state and queues the wire messages that ride the
play's sequence brackets. Interactive primitives (choosers, dialogs) resolve
inline before any choreography is flushed.
"""

import logging
import random
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, cast
from .legal_actions import energy_provided_count
from spirit.game.attributes import (
    AbilityTypes,
    AttrID,
    CardType,
    CLIENT_POKEMON_TYPE_NAMES,
    CLIENT_SPECIAL_CONDITION_NAMES,
    GameSequence,
    PokemonStage,
    PokemonTypes,
    SpecialConditions,
    TrainerType,
)
from spirit.game.data_utils import (
    ABILITIES_BY_ID,
    TRAINER_EFFECTS_BY_GUID,
    Ability,
    Triggers,
    def_for,
    has_rule_box,
    unimplemented,
)
from spirit.game.models.board import BoardEntity, CardEntity, EnergyEntity, PokemonEntity
from spirit.network.message_names import OutboundMsg
from .constants import PROMPT_NO, PROMPT_YES
from .passives import (
    TempPassive,
    ability_effects_blocked,
    ability_locked,
    active_passives,
    active_to_bench_counters,
    attack_coin_reroll_offered,
    attack_effects_blocked,
    carrier_pokemon,
    compute_damage,
    conditions_blocked,
    discard_blocked,
    effective_bench_capacity,
    effective_max_hp,
    effective_pokemon_types,
    energy_removal_blocked,
    healing_blocked,
    supporter_effect_replacement,
    trainer_effects_blocked,
)

# CakeAttackEffect's damageType is a string array of client type names.
CLIENT_TYPE_NAMES = {t.value: name for t, name in CLIENT_POKEMON_TYPE_NAMES.items()}

# n.j.InteractionVisualizations
VISUAL_DAMAGING = 0
VISUAL_NON_DAMAGING = 1

# Asleep/Confused/Paralyzed replace each other; Poisoned/Burned stack with everything.
_MUTUALLY_EXCLUSIVE = {
    SpecialConditions.ASLEEP, SpecialConditions.CONFUSED, SpecialConditions.PARALYZED,
}


def _display_name(entity: BoardEntity) -> str:
    """Best-effort loc-key name for prompts/coin-flip titles."""
    name = entity.get_attribute(AttrID.NAME)
    return name.get("id", "") if isinstance(name, dict) else (name or "")


class EffectContext:
    """Everything a card script may see and do while its effect resolves.

    Messages queue as (viewer_id, msg, bracket) tuples -- viewer_id None
    broadcasts, bracket None uses the flush site's default -- and are flushed
    into sequence brackets per viewer afterwards.
    """

    def __init__(self, session, player_id: str, source: BoardEntity,
                 ability: Optional[Ability], attached_to: Optional[PokemonEntity] = None):
        self.session = session
        self.board = session.board_state
        self.game_id = session.game_id
        self.player_id = player_id
        self.opponent_id = session._opponent_id(player_id)
        self.source = source
        self.attacker = source  # alias: attack scripts read ctx.attacker
        self.ability = ability
        # For energy on-attach effects: the Pokemon the card just attached to.
        self.attached_to = attached_to
        self.knockouts: List[PokemonEntity] = []
        # Extra prizes the attacker takes for knockouts this attack causes
        # (e.g. Stoutland V's Double Dip Fangs).
        self.extra_prizes = 0
        # Entities the ability's orb-of-light FX shoots at; defaults to the
        # piles the effect pulled cards from (deck for draws/searches, the
        # discard for Summoning Star-style recursion).
        self.visual_targets: List[str] = []
        self._visual_sources: List[str] = []
        # Whether a CakeAttackEffect hit an opponent's Pokemon: gates the
        # non-damaging orb in the Attack bracket (mirrors M.N's flag7).
        self._dealt_opponent_damage = False
        # Async callables run AFTER the choreography flushes (promotions and
        # anything else that must not interleave with the pending brackets).
        self.deferred_actions: List[Callable[[], Any]] = []
        # Set by the effect (or auto-set from Ability.ends_turn) to end the
        # acting player's turn once this effect resolves (Rotom Bike).
        self.ends_turn: bool = False
        # Triggered "you may" effects set this when the window never opened:
        # skips even the announce-only PokeAbility bracket.
        self.suppress_announce: bool = False
        # Attack-flow only: the resolved attack does NOT end the turn.
        self.attack_keeps_turn: bool = False
        # Snapshot of ctx.knockouts taken just before resolve_knockouts clears
        # it (post-attack hooks need the KO evidence).
        self.knockouts_resolved: List[PokemonEntity] = []
        # Attack titles already resolving in this attack (copy-loop guard).
        self._copy_chain: List[str] = []
        # Wire-encoded results (0=heads) of coins this effect itself flipped;
        # defensive interceptor flips excluded (Blunder Policy's tails check).
        self.coin_results: List[int] = []
        self._in_interceptor = False
        self._messages: List[Tuple[Optional[str], Dict[str, Any], Optional[str]]] = []
        # Set by resolve_knockouts before firing an ON_KNOCKED_OUT trigger:
        # True iff the causing damage was an opposing Pokemon's attack.
        self.ko_from_attack: bool = False
        self.ko_attacker: Optional[PokemonEntity] = None
        # ON_KNOCKED_OUT only: whether this Pokemon sat in the Active spot at
        # the moment it was Knocked Out (Radiant Jirachi).
        self.was_active_at_ko: bool = False
        # Set by resolve_trainer_effect: primitives against a shielded OTHER
        # player no-op (Dew Guard, via _trainer_blocked).
        self.is_trainer_effect: bool = False
        # ON_ALLY_KNOCKED_OUT: the KO'd ally (still on board, energies attached).
        self.ko_pokemon: Optional[PokemonEntity] = None
        # target entity_id -> (dealt, pre_hit_hp); first attack hit wins.
        # Feeds ON_DAMAGED_BY_ATTACK and full-HP-at-KO checks.
        self.attack_damage: Dict[str, Tuple[int, int]] = {}
        # ON_DAMAGED_BY_ATTACK trigger inputs (set via ctx_setup).
        self.damaged_by: Optional[PokemonEntity] = None
        self.damage_amount: int = 0
        self.pre_hit_hp: int = 0
        # ON_ENERGY_ATTACHED trigger inputs (set via ctx_setup).
        self.attaching_player_id: Optional[str] = None
        self.attached_energy: Optional[CardEntity] = None
        self.energy_receiver: Optional[PokemonEntity] = None
        # ON_ALLY_EVOLVED trigger inputs (set via ctx_setup).
        self.evolved_pokemon: Optional[CardEntity] = None
        self.evolved_from: Optional[PokemonEntity] = None
        # ON_POKEMON_BENCHED trigger inputs (set via ctx_setup).
        self.benching_player_id: Optional[str] = None
        self.benched_pokemon: Optional[PokemonEntity] = None

    # ------------------------------------------------------------------
    # Game state accessors
    # ------------------------------------------------------------------

    @property
    def defender(self) -> Optional[PokemonEntity]:
        """The opponent's Active Pokemon (the default attack target)."""
        return self.board.active_pokemon(self.opponent_id)

    def my_active(self) -> Optional[PokemonEntity]:
        return self.board.active_pokemon(self.player_id)

    def opponent_active(self) -> Optional[PokemonEntity]:
        return self.board.active_pokemon(self.opponent_id)

    def my_bench(self) -> List[PokemonEntity]:
        return self._bench(self.player_id)

    def opponent_bench(self) -> List[PokemonEntity]:
        return self._bench(self.opponent_id)

    def _bench(self, player_id: str) -> List[PokemonEntity]:
        area = self.board.find_player_area(player_id, "bench")
        return [c for c in (area.children if area else [])
                if isinstance(c, PokemonEntity)]

    def my_pokemon_in_play(self) -> List[PokemonEntity]:
        return self.board.pokemon_in_play(self.player_id)

    def opponent_pokemon_in_play(self) -> List[PokemonEntity]:
        return self.board.pokemon_in_play(self.opponent_id)

    def attached_energies(self, pokemon: PokemonEntity) -> list:
        return self.board.attached_energies(pokemon)

    def hand(self, player_id: Optional[str] = None) -> list:
        area = self.board.find_player_area(player_id or self.player_id, "hand")
        return list(area.children) if area else []

    def hand_size(self, player_id: Optional[str] = None) -> int:
        return len(self.hand(player_id))

    def deck(self, player_id: Optional[str] = None) -> list:
        area = self.board.find_player_area(player_id or self.player_id, "deck")
        return list(area.children) if area else []

    def deck_top(self, count: int = 1, player_id: Optional[str] = None) -> List[CardEntity]:
        """Top `count` cards, topmost first. Pure read, no wire messages."""
        cards = self.deck(player_id)
        return list(reversed(cards[-count:])) if count > 0 else []

    def discard_pile(self, player_id: Optional[str] = None) -> list:
        area = self.board.find_player_area(player_id or self.player_id, "discard")
        return list(area.children) if area else []

    def lost_zone(self, player_id: Optional[str] = None) -> list:
        area = self.board.find_player_area(player_id or self.player_id, "lostZone")
        return list(area.children) if area else []

    def lost_zone_count(self, player_id: Optional[str] = None) -> int:
        return len(self.lost_zone(player_id))

    def max_hp(self, pokemon: PokemonEntity) -> int:
        return effective_max_hp(self.board, pokemon)

    def stadium_in_play(self) -> Optional[BoardEntity]:
        """The Stadium card currently in play (either player's), or None."""
        area = self.board.find_global_area("activeStadium")
        return next(iter(area.children), None) if area else None

    def tools_in_play(self) -> List[Tuple[CardEntity, PokemonEntity]]:
        """Every attached Pokemon Tool as (tool, pokemon) pairs, both sides."""
        pairs = []
        for pid in self.board.player_ids:
            for pokemon in self.board.pokemon_in_play(pid):
                for child in pokemon.children:
                    if child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value:
                        pairs.append((child, pokemon))
        return pairs

    def prizes_taken(self, player_id: Optional[str] = None) -> int:
        return self.board.prizes_taken(player_id or self.player_id)

    def is_attack_effect(self) -> bool:
        """Whether this ctx's ability is an attack (vs. a PokeAbility/trainer)."""
        return self.ability is not None and self.ability.ability_type in (
            AbilityTypes.ATTACK, AbilityTypes.NON_DAMAGING_ATTACK
        )

    def is_ability_effect(self) -> bool:
        """Whether this ctx resolves a Pokemon Ability (not an attack/trainer)."""
        return self.ability is not None and not self.is_attack_effect()

    def effects_blocked(self, target: PokemonEntity) -> bool:
        """Whether an opposing attack/Ability EFFECT on `target` is shielded
        (Unfazed Fat / Corviknight VMAX). Only effects against the other
        side count; trainer effects are never shielded here."""
        if target.owning_player_id == self.player_id:
            return False
        if self.is_attack_effect():
            return attack_effects_blocked(self.board, target)
        if self.is_ability_effect():
            return ability_effects_blocked(self.board, target)
        return False

    def _trainer_blocked(self, player_or_entity) -> bool:
        """Dew Guard shield: in a trainer context, True when the primitive's
        direct object belongs to a shielded player OTHER than the acting one.
        Guards: deal_damage/counters, apply_special_condition, switch_active,
        draw_cards/draw_until, discard_from_hand, hand_to_bottom_of_deck,
        shuffle_into_deck, discard_cards/move_to_lost_zone (per card)."""
        if not self.is_trainer_effect:
            return False
        pid = player_or_entity if isinstance(player_or_entity, str) \
            else getattr(player_or_entity, "owning_player_id", None)
        if pid is None or pid == self.player_id:
            return False
        entity = None if isinstance(player_or_entity, str) else player_or_entity
        if trainer_effects_blocked(self.board, pid, self.source, entity):
            logging.info(
                f"[Effects {self.game_id}] Trainer effect on {pid} blocked "
                f"by a trainer-effect shield."
            )
            return True
        return False

    def _energy_removal_blocked(self, card) -> bool:
        """Brazen Tail shield: in a trainer context, True when a passive keeps
        this attached Energy from moving to hand/deck/discard."""
        if not self.is_trainer_effect:
            return False
        if energy_removal_blocked(self.board, self.player_id, card):
            logging.info(
                f"[Effects {self.game_id}] Energy removal of {card.entity_id} "
                f"blocked by a passive."
            )
            return True
        return False

    async def _run_damage_interceptors(self, calc, target: PokemonEntity) -> int:
        """Awaitable damage stage (Guts/Infiltrator): runs AFTER compute_damage
        and BEFORE the HP write; each interceptor may rewrite calc.amount.
        Interceptors riding the target are skipped under ignore_target_effects
        (a flip-prevention IS an effect on the opponent's Active -- Max
        Miracle ruling)."""
        self._in_interceptor = True
        try:
            for passive, carrier in active_passives(self.board):
                interceptor = getattr(passive, "damage_interceptor", None)
                if interceptor is None:
                    continue
                if calc.ignore_target_effects and carrier_pokemon(carrier) is target:
                    continue
                new_amount = await interceptor(self, calc, target, carrier)
                if new_amount is not None:
                    calc.amount = max(0, int(new_amount))
        finally:
            self._in_interceptor = False
        return calc.amount

    # ------------------------------------------------------------------
    # Damage / HP primitives
    # ------------------------------------------------------------------

    async def deal_damage(
        self,
        amount: Optional[int] = None,
        target: Optional[PokemonEntity] = None,
        apply_modifiers: Optional[bool] = None,
        is_attack: Optional[bool] = None,
        ignore_target_effects: bool = False,
        ignore_weakness: bool = False,
        ignore_resistance: bool = False,
        as_counters: bool = False,
    ) -> int:
        """Damages a Pokemon (default: the attack's printed damage onto the
        opponent's Active) and returns the final amount after modifiers.

        Weakness/Resistance apply only to the opponent's Active by default
        (bench damage in the TCG is unmodified unless the card says otherwise).
        ignore_target_effects (Max Miracle) skips passives riding the target.
        ignore_weakness (Spit Innocently) skips only the Weakness stage;
        ignore_resistance (Buster Swing) skips only the Resistance stage.
        as_counters plays the counter-drop FX (PlaceDamageEffect, m.p) instead
        of the attack lunge (CakeAttackEffect) -- "put N damage counters"
        effects (Lost Mine, Glistening Droplets).
        """
        target = target if target is not None else self.defender
        if target is None:
            logging.warning(f"[Effects {self.game_id}] deal_damage with no target; skipped.")
            return 0
        if self._trainer_blocked(target):
            return 0
        base = amount if amount is not None else getattr(self.ability, "damage", 0)
        if base <= 0:
            return 0
        if apply_modifiers is None:
            apply_modifiers = target is self.opponent_active()
        if is_attack is None:
            is_attack = self.is_attack_effect()
        # Turn-scoped Max Miracle flag on the attacker (Phoebe).
        if not ignore_target_effects and self.attacker is not None \
                and self.attacker.entity_id in \
                self.session.turn_state.ignore_target_effects_entities:
            ignore_target_effects = True

        if as_counters:
            # Damage counters are RAW -- not "damage from an attack", so they
            # skip the damage pipeline: no Weakness/Resistance, no damage-taken
            # reduction, no damage-prevention (Miltank's Miracle Body, "take 30
            # less damage" only apply to attack DAMAGE). But placing counters
            # IS an attack EFFECT, so an attack-effect shield (Snorlax's Unfazed
            # Fat) prevents them: the target stays a legal pick but takes 0.
            dealt = 0 if self.effects_blocked(target) else base
        else:
            calc = compute_damage(
                self.board, self.attacker, target, base,
                is_attack=is_attack, apply_modifiers=apply_modifiers,
                ignore_target_effects=ignore_target_effects,
                ignore_weakness=ignore_weakness,
                ignore_resistance=ignore_resistance,
                attack_title=self.ability.title if self.ability else None,
            )
            if calc.prevented:
                logging.info(
                    f"[Effects {self.game_id}] Damage to {target.entity_id} "
                    f"prevented by a passive effect."
                )
                return 0
            dealt = calc.amount
            if dealt > 0:
                dealt = await self._run_damage_interceptors(calc, target)

        current = target.get_attribute(AttrID.HP, 0)
        remaining = max(0, current - dealt)
        target.set_attribute(AttrID.HP, remaining)

        # m.p/m.m both read current HP when they play, so the damage FX must
        # precede the HP AttributeModified for the knockout check to see
        # pre-hit HP.
        if as_counters:
            # PlaceDamageEffect (UNSET condition => generic counter-drop, not
            # the poison/burn overlay); leave _dealt_opponent_damage False so
            # the attacker tucks via the non-damaging orb aimed at the targets.
            self._queue(self.session._place_damage_effect_msg(
                target.entity_id, dealt))
            if target.entity_id not in self.visual_targets:
                self.visual_targets.append(target.entity_id)
        else:
            title = self.ability.title if self.ability else ""
            attacker_types = effective_pokemon_types(self.board, self.attacker)
            type_name = CLIENT_TYPE_NAMES.get(attacker_types[0], "Colorless") \
                if attacker_types else "Colorless"
            self._queue(self.session._build_msg(
                OutboundMsg.CAKE_ATTACK_EFFECT.value,
                {
                    "gameID": self.game_id,
                    "damageSource": self.attacker.entity_id,
                    "entityID": target.entity_id,
                    "weaknessTriggered": calc.weakness_hit,
                    "resistanceTrigger": calc.resistance_hit,
                    "damageType": [type_name],
                    "attackName": {"id": title},
                    "damageAmount": dealt,
                    "damageModification": 0,
                    "visualType": VISUAL_DAMAGING,
                },
            ))
        if target.owning_player_id != self.attacker.owning_player_id:
            if not as_counters:
                self._dealt_opponent_damage = True
                # ON_DAMAGED_BY_ATTACK ledger: attack hits only, first-write
                # wins so the pre-hit HP is the true pre-attack value.
                if dealt > 0 and is_attack:
                    self.attack_damage.setdefault(target.entity_id, (dealt, current))
            if dealt > 0:
                taken = self.session.turn_state.damage_taken
                taken[target.entity_id] = taken.get(target.entity_id, 0) + dealt
            self.session.stat_add(self.player_id, "damagedealt", dealt)
            self.session.credit_card_damage(self.player_id, self.attacker, dealt)
            if is_attack:
                self.session.stat_max(self.player_id, "biggestattack", dealt)
        self._queue_hp_update(target)

        if remaining <= 0 and target not in self.knockouts:
            self.knockouts.append(target)
        return dealt

    async def knock_out(self, target: Optional[PokemonEntity]) -> bool:
        """Knocks a Pokemon Out directly (an attack EFFECT, not damage)."""
        if target is None:
            return False
        if self.effects_blocked(target):
            logging.info(
                f"[Effects {self.game_id}] Knock Out of {target.entity_id} "
                f"blocked by an effect shield."
            )
            return False
        target.set_attribute(AttrID.HP, 0)
        self._queue_hp_update(target)
        if target not in self.knockouts:
            self.knockouts.append(target)
        return True

    async def heal(self, amount: int, target: Optional[PokemonEntity] = None) -> int:
        """Heals damage from a Pokemon (default: own Active); returns the healed amount."""
        target = target if target is not None else self.my_active()
        if target is None or amount <= 0:
            return 0
        if healing_blocked(self.board, target):
            logging.info(
                f"[Effects {self.game_id}] Healing on {target.entity_id} "
                f"prevented by a passive effect."
            )
            return 0
        current = target.get_attribute(AttrID.HP, 0)
        healed = min(self.max_hp(target), current + amount) - current
        if healed <= 0:
            return 0
        target.set_attribute(AttrID.HP, current + healed)
        self.session.turn_state.healed_entities.add(target.entity_id)
        self.session.stat_add(self.player_id, "damagehealed", healed)
        # Heal FX + fly-text (L.y) must precede the HP update, like CakeAttackEffect.
        source_id = self.source.entity_id if self.source is not None \
            else target.entity_id
        self._queue(self.session._build_msg(
            OutboundMsg.CREATURE_HEAL_WITH_CONTEXT_EVENT.value,
            {
                "gameID": self.game_id,
                "source": source_id,
                "targets": [target.entity_id],
                "amount": healed,
            },
        ))
        # Trailing empty-targets event: forces k.z's fire-and-forget path on the
        # real one (awaited L.y can stall the client's sequence pump forever).
        self._queue(self.session._build_msg(
            OutboundMsg.CREATURE_HEAL_WITH_CONTEXT_EVENT.value,
            {
                "gameID": self.game_id,
                "source": source_id,
                "targets": [],
                "amount": 0,
            },
        ))
        self._queue_hp_update(target)
        return healed

    async def apply_special_condition(
        self,
        target: Optional[PokemonEntity],
        condition: SpecialConditions,
        checkup_coins: int = 1,
        poison_counters: int = 1,
    ) -> bool:
        """Applies a Special Condition (Asleep etc.); returns False if shielded.

        checkup_coins: coins flipped at Pokemon Checkup for Asleep -- waking
        requires ALL heads (Snorlax's Thumping Snore flips 2).
        poison_counters: damage-counter multiplier recorded for Poisoned
        (10 * poison_counters dealt each checkup).
        Asleep/Confused/Paralyzed are mutually exclusive and replace each
        other; Poisoned/Burned stack with everything.
        """
        if target is None:
            return False
        if self._trainer_blocked(target):
            return False
        if self.effects_blocked(target):
            logging.info(
                f"[Effects {self.game_id}] {condition.name} on {target.entity_id} "
                f"blocked by an effect shield."
            )
            return False
        if conditions_blocked(self.board, target, condition):
            logging.info(
                f"[Effects {self.game_id}] {condition.name} on {target.entity_id} "
                f"blocked by a condition-immunity passive."
            )
            return False
        name = CLIENT_SPECIAL_CONDITION_NAMES[condition]
        conditions = list(target.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        if condition in _MUTUALLY_EXCLUSIVE:
            for other in _MUTUALLY_EXCLUSIVE - {condition}:
                other_name = CLIENT_SPECIAL_CONDITION_NAMES[other]
                if other_name in conditions:
                    conditions.remove(other_name)
                if other == SpecialConditions.ASLEEP:
                    self.session.sleep_checkup_coins.pop(target.entity_id, None)
                else:  # PARALYZED
                    self.session.paralyzed_since.pop(target.entity_id, None)
        if name not in conditions:
            conditions.append(name)
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, conditions)
        if condition == SpecialConditions.ASLEEP:
            self.session.sleep_checkup_coins[target.entity_id] = checkup_coins
        elif condition == SpecialConditions.POISONED:
            self.session.poison_counters[target.entity_id] = poison_counters
        elif condition == SpecialConditions.PARALYZED:
            self.session.paralyzed_since[target.entity_id] = self.session.turn_state.turn_number
        # The executor diffs the full new array; its ctor requires a "Target" data effect.
        self._queue(
            self.session._entity_id_data_effect_msg("Target", target.entity_id),
            bracket=GameSequence.ADD_SPECIAL_CONDITION.value,
        )
        self._queue(
            self.session._condition_attr_msg(target),
            bracket=GameSequence.ADD_SPECIAL_CONDITION.value,
        )
        return True

    async def cure_all_conditions(self, target: Optional[PokemonEntity]) -> bool:
        """Removes every Special Condition from `target` ("...it recovers from
        all Special Conditions"); returns True if any were removed."""
        if target is None or not target.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, [])
        self.session.clear_condition_state(target.entity_id)
        # The executor diffs the full new array; its ctor requires a "Target" data effect.
        self._queue(
            self.session._entity_id_data_effect_msg("Target", target.entity_id),
            bracket=GameSequence.REMOVE_SPECIAL_CONDITION.value,
        )
        self._queue(
            self.session._condition_attr_msg(target),
            bracket=GameSequence.REMOVE_SPECIAL_CONDITION.value,
        )
        return True

    async def cure_condition(self, target: Optional[PokemonEntity],
                             condition: SpecialConditions) -> bool:
        """Removes exactly ONE Special Condition (Clefable's Moonlit Cure);
        other conditions stay. Returns True if it was present."""
        if target is None:
            return False
        name = CLIENT_SPECIAL_CONDITION_NAMES[condition]
        if name not in (target.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return False
        msg = self.session._remove_single_condition(target, condition)
        # Executor ctor (M.t) indexes the bracket's data effects with "Target".
        self._queue(
            self.session._entity_id_data_effect_msg("Target", target.entity_id),
            bracket=GameSequence.REMOVE_SPECIAL_CONDITION.value,
        )
        self._queue(msg, bracket=GameSequence.REMOVE_SPECIAL_CONDITION.value)
        return True

    def add_turn_damage_modifier(self, mod) -> None:
        """Registers a TurnDamageModifier (expires_after_turn None = this turn)."""
        self.session.turn_state.damage_modifiers.append(mod)

    def add_extra_prize_watcher(self, attacker_predicate=None,
                                target_predicate=None, prizes: int = 1) -> None:
        """This-turn bonus-prize watch (Star Order): when this player's attack
        KOs by damage a Pokemon passing target_predicate and the attacker
        passes attacker_predicate, resolve_knockouts adds `prizes` to the take."""
        self.session.turn_state.extra_prize_watchers.append({
            "player_id": self.player_id,
            "attacker_predicate": attacker_predicate,
            "target_predicate": target_predicate,
            "prizes": prizes,
        })

    def add_temporary_passive(self, target, passive,
                              expires_after_turn: Optional[int] = None) -> None:
        """Attaches an effect-granted passive to `target` (expires_after_turn
        None = until it leaves the Active spot / play)."""
        self.board.temporary_passives.append(
            TempPassive(passive, target.entity_id, expires_after_turn)
        )

    def add_passive_through_opponents_turn(self, target, passive) -> None:
        """"During your opponent's next turn ..." lifetime."""
        self.add_temporary_passive(
            target, passive, self.session.turn_state.turn_number + 1
        )

    def add_passive_through_own_next_turn(self, target, passive) -> None:
        """"During your next turn ..." lifetime (spans the opponent's turn too)."""
        self.add_temporary_passive(
            target, passive, self.session.turn_state.turn_number + 2
        )

    def lock_retreat(self, target: PokemonEntity,
                     through_turn: Optional[int] = None) -> None:
        """"The Defending Pokemon can't retreat during your opponent's next
        turn" (default); pass legal_actions.LOCK_UNTIL_LEAVES_ACTIVE to hold
        the lock until it leaves the Active spot."""
        self.session.turn_state.lock_retreat(target.entity_id, through_turn)

    def lock_plays(self, player_id: str, predicate: Callable[[CardEntity], bool],
                   through_turn: Optional[int] = None) -> None:
        """"<player> can't play <cards matching predicate>" (default: through
        their next turn)."""
        self.session.turn_state.lock_plays(player_id, predicate, through_turn)

    def restrict_attachments(self, target: PokemonEntity,
                             through_turn: Optional[int] = None) -> None:
        """"Energy can't be attached to the Defending Pokemon" (default:
        through the opponent's next turn); manual attach offers exclude it."""
        self.session.turn_state.restrict_attachments(target.entity_id, through_turn)

    def require_attack_flip(self, target: Optional[PokemonEntity],
                            through_turn: Optional[int] = None,
                            title: Optional[str] = None) -> None:
        """Smokescreen: "if the Defending Pokemon tries to attack ... flip a
        coin. If tails, that attack doesn't happen" (default: through the
        opponent's next turn; cleared when the target leaves the Active)."""
        if target is None:
            return
        self.session.turn_state.set_attack_flip_check(
            target.entity_id, through_turn,
            title if title is not None else (self.ability.title if self.ability else ""),
        )

    def ignore_own_target_effects(self, entity: PokemonEntity) -> None:
        """"During this turn, <entity>'s attacks aren't affected by effects on
        the opponent's Active" (Phoebe); cleared at begin_turn."""
        self.session.turn_state.ignore_target_effects_entities.add(entity.entity_id)

    def take_extra_turn(self) -> None:
        """"Take another turn after this one. (Skip Pokemon Checkup.)"
        (Star Chronos, Yoga Loop); consumed by run_turn_loop."""
        self.session.extra_turn_pending = True

    def schedule_at_checkup(self, turns_ahead: int, effect,
                            guard: Optional[Callable] = None) -> None:
        """Schedules async `effect(session)` at the START of the Pokemon
        Checkup `turns_ahead` turns from now (0 = this turn's checkup, 1 = the
        checkup ending the opponent's next turn -- Word of Ruin's delayed KO);
        `guard(board)` returning False at fire time drops it silently."""
        self.session.scheduled_effects.append({
            "fire_at_checkup_of_turn":
                self.session.turn_state.turn_number + turns_ahead,
            "guard": guard,
            "effect": effect,
        })

    # ------------------------------------------------------------------
    # Turn-history accessors (two turns kept, rotated at begin_turn)
    # ------------------------------------------------------------------

    def kos_suffered_last_turn(self, player_id: Optional[str] = None) -> int:
        """How many of a player's Pokemon were KO'd by attacks last turn."""
        ledger = self.session.turn_state.kos_by_attack_last_turn
        return len(ledger.get(player_id or self.player_id, []))

    def attack_used_last_turn(self, title: Optional[str] = None,
                              entity=None) -> bool:
        """Whether an attack (optionally by title and/or entity) was declared last turn."""
        entity_id = getattr(entity, "entity_id", entity)
        for used_id, _archetype, used_title in self.session.turn_state.attacks_used_last_turn:
            if title is not None and used_title != title:
                continue
            if entity_id is not None and used_id != entity_id:
                continue
            return True
        return False

    def damage_taken_last_turn(self, pokemon) -> int:
        return self.session.turn_state.damage_taken_last_turn.get(
            pokemon.entity_id, 0
        )

    def entered_active_this_turn(self, pokemon) -> bool:
        state = self.session.turn_state
        return state.became_active_turn.get(pokemon.entity_id) == state.turn_number

    def played_trainer_this_turn(self, name_or_pred=None) -> int:
        """Count of trainers played this turn; filter by display name (str) or
        a predicate over the (archetype_id, name, trainer_type) record."""
        count = 0
        for record in self.session.turn_state.trainers_played:
            if name_or_pred is None:
                count += 1
            elif callable(name_or_pred):
                count += 1 if name_or_pred(record) else 0
            elif record[1] == name_or_pred:
                count += 1
        return count

    def supporters_played_this_turn(self) -> int:
        return self.played_trainer_this_turn(
            lambda r: r[2] == TrainerType.SUPPORTER.value
        )

    def items_played_this_turn(self) -> int:
        return self.played_trainer_this_turn(
            lambda r: r[2] == TrainerType.ITEM.value
        )

    async def add_stat_visualization(
        self, pokemon: PokemonEntity, arrow: str, display_type: str,
        card_text: Optional[str] = None,
    ) -> None:
        """Shows a stat-modifier PiP on `pokemon` for the rest of the turn
        (green up arrow / red down arrow). arrow: "Positive"/"Negative";
        display_type: a client VisualizationTypes member name."""
        await self.session.add_turn_stat_visualization(
            pokemon, arrow, display_type, _display_name(self.source), card_text
        )

    async def choose_attack_to_copy(self, candidates, prompt: str = ""):
        """Presents (pokemon, attack) candidates as full attack rows in the
        floating panel (a FORCED pick: once the copy attack is declared it
        cannot be cancelled) and returns the chosen pair."""
        idx = await self.session.prompt_attack_selection(
            self.player_id, self.source, candidates, prompt
        )
        return candidates[idx] if idx is not None else None

    async def use_attack(self, ability: Ability) -> bool:
        """Resolves another attack's damage/effect as this attack (Cross Fusion).

        Returns False (a fizzle: the attack does nothing and the turn ends
        normally) when the copy chain revisits an attack title -- Cross Fusion
        copying another Mew VMAX's Cross Fusion Strike -- or exceeds the depth
        cap. Titles, not ability_ids: alt-art reprints copy under distinct ids.
        """
        if ability.title in self._copy_chain or len(self._copy_chain) >= 8:
            logging.info(
                f"[Effects {self.game_id}] Copied attack '{ability.title}' "
                f"re-entered the copy chain {self._copy_chain}; fizzling."
            )
            return False
        self._copy_chain.append(ability.title)
        self.ability = ability
        if ability.effect is None or ability.effect is unimplemented:
            if ability.effect is unimplemented:
                logging.warning(
                    f"[Effects {self.game_id}] Attack '{ability.title}' has "
                    f"unimplemented text; resolving base damage only."
                )
            await self.deal_damage()
        else:
            await ability.effect(self)
        if getattr(ability, "locks_next_turn", False):
            self.session.turn_state.lock_attack(self.attacker.entity_id, ability.ability_id)
        return True

    async def _queue_coin_results(self, results: List[int], title: str,
                                  source: Optional[BoardEntity] = None,
                                  immediate: bool = False):
        """Sends ONE MultipleCoinFlipWithContextEffect for a pre-rolled run
        (0 = heads); queued inline in attack/ability context, sent as its own
        PokeAbility bracket + pacing pause in trainer context. `source`
        overrides the flip's visual anchor (defensive flips ride the carrier);
        `immediate` forces the send-now path (Glimwood re-flip: the player
        must SEE the run before deciding)."""
        heads = results.count(0)
        if not self._in_interceptor:
            self.coin_results.extend(results)
        source = source if source is not None else self.source
        self.session.stat_add(self.player_id, "headsflipped", heads)
        self.session.stat_add(self.player_id, "tailsflipped", len(results) - heads)
        msg = self.session._build_msg(
            OutboundMsg.MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT.value,
            {
                "gameID": self.game_id,
                "resultLst": results,
                "title": {"id": title or _display_name(source)},
                "gameText": {"id": f"{heads} heads"},
                "source": source.entity_id,
                "targets": [source.entity_id],
            },
        )
        if self.ability is not None and not immediate:
            # Attack/PokeAbility brackets play the coin flip natively inline.
            self._queue(msg)
        else:
            # Trainer context: PokeAbility, NOT FlipToWakeUp -- d.s stamps the
            # "Asleep" pop-in (abilitypopin.asleep.label) onto every L.x it runs.
            await self.session.send_game_sequence(
                list(self.session.players.values()),
                GameSequence.POKE_ABILITY, [msg],
            )
            await self.session.choreo_pause(2.5)

    async def _maybe_reroll_attack_coins(
        self, results: List[int], title: str,
        source: Optional[BoardEntity], reroll: Callable[[], List[int]],
    ) -> Optional[List[int]]:
        """Glimwood Tangle: once during their turn, after flipping coins for
        an attack, the player may ignore the results and flip again. Returns
        the final (already-displayed) run, or None when no re-flip was offered
        (the caller queues the flip normally). `source`-anchored runs are
        defensive/carrier flips, never the player's own attack coins."""
        if source is not None or not self.is_attack_effect():
            return None
        ts = self.session.turn_state
        if ts.attack_coin_reroll_used or self.player_id != ts.active_player_id:
            return None
        if not attack_coin_reroll_offered(self.board, self.player_id):
            return None
        await self._queue_coin_results(results, title, source, immediate=True)
        if not await self.ask_yes_no(
                "Ignore all results of those coin flips and begin flipping again?"):
            return results
        ts.attack_coin_reroll_used = True
        # "Ignore all results of those coin flips": the ignored run must not
        # feed post-attack followups (Blunder Policy's tails check).
        del self.coin_results[len(self.coin_results) - len(results):]
        new_results = reroll()
        await self._queue_coin_results(new_results, title, source, immediate=True)
        return new_results

    async def flip_coins(self, count: int, title: str = "",
                         source: Optional[BoardEntity] = None) -> List[bool]:
        """Flips `count` coins for a card effect ("Flip 2 coins..."); returns
        the results, True = heads. `source` re-anchors the flip visual."""
        if count <= 0:
            return []
        results = [random.choice([0, 1]) for _ in range(count)]
        final = await self._maybe_reroll_attack_coins(
            results, title, source,
            lambda: [random.choice([0, 1]) for _ in range(count)])
        if final is None:
            await self._queue_coin_results(results, title, source)
        else:
            results = final
        return [r == 0 for r in results]

    async def flip_until_tails(self, title: str = "") -> int:
        """"Flip a coin until you get tails": one coin screen shows the whole
        run; returns the heads count."""
        def _run() -> List[int]:
            run = [random.choice([0, 1])]
            while run[-1] == 0:
                run.append(random.choice([0, 1]))
            return run
        results = _run()
        final = await self._maybe_reroll_attack_coins(results, title, None, _run)
        if final is None:
            await self._queue_coin_results(results, title)
        else:
            results = final
        return results.count(0)

    async def place_damage_counters(
        self, count: int, candidates: Optional[List[PokemonEntity]] = None
    ) -> None:
        """Distributes `count` damage counters (10 HP each) over `candidates`
        (default: all of the opponent's in-play Pokemon) via the native
        click-to-place picker (one offer, Done gates on exactly `count`
        clicks)."""
        pool = list(candidates) if candidates is not None else self.opponent_pokemon_in_play()
        in_play_ids = {p.entity_id for p in self.my_pokemon_in_play() + self.opponent_pokemon_in_play()}
        pool = [p for p in pool if p.entity_id in in_play_ids]
        if not pool or count <= 0:
            return
        placement = await self.session.prompt_damage_counter_placement(
            self.player_id, self.source.entity_id, pool, count,
            prompt=f"Place {count} damage counters on your opponent's Pokemon.",
        )
        by_id = {p.entity_id: p for p in pool}
        for entity_id, counters in placement.items():
            if counters <= 0 or entity_id not in by_id:
                continue
            await self.deal_damage(
                amount=counters * 10, target=by_id[entity_id], as_counters=True,
            )

    async def set_damage_counters(self, target: Optional[PokemonEntity],
                                  counters: int) -> None:
        """Sets a Pokemon's damage to exactly `counters` (HP = max - 10n,
        Claydol-style); a result of 0 HP enqueues the knockout."""
        if target is None:
            return
        new_hp = max(0, self.max_hp(target) - counters * 10)
        target.set_attribute(AttrID.HP, new_hp)
        self._queue_hp_update(target)
        if new_hp <= 0 and target not in self.knockouts:
            self.knockouts.append(target)

    async def move_damage_counters(
        self,
        source: Optional[PokemonEntity],
        dest_or_targets,
        max_count: Optional[int] = None,
        prompt: str = "Place the moved damage counters",
    ) -> int:
        """Moves damage counters off `source` (heal + raw counter placement,
        atomic), clamped to its actual damage; returns counters moved.

        A single shielded destination fizzles the WHOLE move; in a
        multi-target distribution shielded picks stay legal but their
        counters are prevented (wasted), per the Unfazed Fat ruling.
        """
        if source is None:
            return 0
        damage = max(0, self.max_hp(source) - source.get_attribute(AttrID.HP, 0))
        available = damage // 10
        count = available if max_count is None else min(available, max_count)
        if count <= 0:
            return 0
        if isinstance(dest_or_targets, PokemonEntity):
            if self.effects_blocked(dest_or_targets):
                return 0
            pool = [dest_or_targets]
            placement = {dest_or_targets.entity_id: count}
        else:
            pool = [p for p in dest_or_targets if p is not source]
            if not pool:
                return 0
            placement = await self.session.prompt_damage_counter_placement(
                self.player_id, self.source.entity_id, pool, count, prompt=prompt,
            )
        total = sum(v for v in placement.values() if v > 0)
        if total <= 0:
            return 0
        healed = await self.heal(total * 10, source)
        if healed <= 0:
            return 0
        remaining = healed // 10
        by_id = {p.entity_id: p for p in pool}
        for entity_id, n in placement.items():
            if n <= 0 or entity_id not in by_id or remaining <= 0:
                continue
            n = min(n, remaining)
            remaining -= n
            await self.deal_damage(amount=n * 10, target=by_id[entity_id],
                                   as_counters=True)
        return healed // 10

    # ------------------------------------------------------------------
    # Interactive primitives (resolve inline, before choreography)
    # ------------------------------------------------------------------

    async def choose(self, prompt: str, buttons: List[str],
                     player_id: Optional[str] = None,
                     descriptions: Optional[List[str]] = None,
                     use_panel: bool = True) -> int:
        """Presents a "Choose 1"-style menu to a player (default: the effect's
        owner) and returns the picked button index.

        By default the options render as buttons in the floating ability panel
        on the effect's source card (the original client's trainer/attack option
        UX). `use_panel=False` falls back to the plain button dialog -- used for
        Yes/No confirms and numeric pickers. The panel needs a visible in-play
        source controlled by the chooser, so a cross-player prompt uses the
        dialog."""
        pid = player_id or self.player_id
        if use_panel and self.source is not None and pid == self.player_id:
            return await self.session.prompt_choice_panel(
                pid, self.source, buttons, prompt, descriptions
            )
        return await self.session.prompt_player_choice(pid, prompt, buttons)

    async def ask_yes_no(self, prompt: str, player_id: Optional[str] = None) -> bool:
        """Yes/No dialog for a card's "you may ..." text; True when Yes is picked."""
        return await self.choose(
            prompt, [PROMPT_YES, PROMPT_NO], player_id, use_panel=False
        ) == 0

    async def choose_cards(
        self,
        cards: Sequence[CardEntity],
        count: int,
        minimum: Optional[int] = None,
        prompt: str = "Choose a card",
        player_id: Optional[str] = None,
        ordered: bool = False,
        display_cards: Optional[Sequence[CardEntity]] = None,
        slot_prompt: str = "",
    ) -> List[CardEntity]:
        """Card pick over `cards`; returns the picked entities.

        Cards the chooser can already see in place (their own hand, top-level
        in-play Pokemon) glow green where they sit; anything else (deck,
        discard, attached cards) opens the full-screen browser instead.
        display_cards forces the browser and shows the whole set (e.g. the
        full deck) with only `cards` selectable. slot_prompt labels the
        browser's empty pick slot ("Choose a Basic Pokemon to put into your
        hand."). minimum=None means exactly `count` (or every card if fewer
        exist); minimum=0 makes the pick optional ("up to count").
        """
        if (not cards and not display_cards) or count <= 0:
            return []
        pid = player_id or self.player_id
        if not ordered and display_cards is None and cards \
                and self._visible_in_place(cards, pid):
            picked_ids = await self.session.prompt_entity_picker(
                pid, self.source.entity_id, cards, count, minimum, prompt
            )
        else:
            picked_ids = await self.session.prompt_card_chooser(
                pid, self.source.entity_id, cards, count, minimum, prompt,
                ordered, display_cards, slot_prompt
            )
        by_id = {c.entity_id: c for c in cards}
        return [by_id[i] for i in picked_ids if i in by_id]

    def _visible_in_place(self, cards: Sequence[CardEntity], player_id: str) -> bool:
        """True when every card sits where the chooser can click it directly:
        their own hand, a top-level in-play spot, or attached to an in-play
        Pokemon. The reveal browser can NEVER show in-play cards (their
        renders belong to the playmat's higher-layer requesters), so those
        must glow in place; only hidden zones and the discard need it."""
        for card in cards:
            entity = card
            # Climb attachment chains (tools/energies/evolution underlays).
            while isinstance(getattr(entity, "parent", None), CardEntity):
                entity = entity.parent
            parent = getattr(entity, "parent", None)
            if parent is None:
                return False
            area_name = parent.get_attribute(AttrID.NAME)
            if area_name == "hand":
                if card.owning_player_id != player_id or entity is not card:
                    return False
            elif area_name not in ("activePokemonArea", "bench", "activeStadium"):
                return False
        return True

    async def choose_pokemon(
        self,
        candidates: Sequence[PokemonEntity],
        prompt: str,
        player_id: Optional[str] = None,
        optional: bool = False,
    ) -> Optional[PokemonEntity]:
        """Picks one in-play Pokemon via the card browser; None if declined."""
        picks = await self.choose_cards(
            candidates, 1, minimum=0 if optional else None,
            prompt=prompt, player_id=player_id,
        )
        return cast(PokemonEntity, picks[0]) if picks else None

    async def search_deck(
        self,
        predicate: Optional[Callable[[CardEntity], bool]] = None,
        count: int = 1,
        minimum: int = 0,
        prompt: str = "Choose a card",
        player_id: Optional[str] = None,
        slot_prompt: str = "",
    ) -> List[CardEntity]:
        """Browses the player's deck for matching cards; does NOT move or
        shuffle -- pair with put_in_hand/bench/attach + shuffle_deck.

        The whole deck shows in the browser (a search reveals the deck);
        only matching cards are selectable and sort to the front."""
        pid = player_id or self.player_id
        deck_cards = list(self.deck(pid))
        matches = [c for c in deck_cards if predicate is None or predicate(c)]
        return await self.choose_cards(
            matches, count, minimum=minimum, prompt=prompt, player_id=pid,
            display_cards=deck_cards, slot_prompt=slot_prompt,
        )

    async def search_deck_groups(
        self,
        groups: Sequence[tuple],
        prompt: str = "Choose a card",
        player_id: Optional[str] = None,
        total: Optional[int] = None,
        any_of: bool = False,
    ) -> List[List[CardEntity]]:
        """One deck-search browser with a labeled pick slot per group
        (Irida: "up to 1 Water Pokemon AND up to 1 Item card").

        Each group is (predicate, count, slot_prompt) with minimum 0 ("up
        to"); a deck card belongs to the first group whose predicate matches.
        any_of picks from any groups under one global `total` cap instead of
        AND-ing every group's own count (Any-composite browser). Returns the
        picked cards per group; pair with put_in_hand + shuffle_deck.

        any_of carousels misrender on the client (slot labels/pick slots) --
        prefer a one-representative-per-group choose_cards instead."""
        pid = player_id or self.player_id
        deck_cards = list(self.deck(pid))
        specs = []
        claimed: set = set()
        for predicate, count, slot_prompt in groups:
            cards = [c for c in deck_cards
                     if c.entity_id not in claimed and (predicate is None or predicate(c))]
            claimed.update(c.entity_id for c in cards)
            specs.append({"cards": cards, "count": count, "minimum": 0,
                          "slot_prompt": slot_prompt})
        picked_ids = await self.session.prompt_card_chooser_groups(
            pid, self.source.entity_id, specs, prompt, display_cards=deck_cards,
            total=total, any_of=any_of,
        )
        by_id = {c.entity_id: c for c in deck_cards}
        return [[by_id[i] for i in ids if i in by_id] for ids in picked_ids]

    async def discard_from_hand(
        self,
        count: int,
        minimum: Optional[int] = None,
        prompt: str = "Choose a card to discard",
        player_id: Optional[str] = None,
        predicate: Optional[Callable[[CardEntity], bool]] = None,
        exclude: Optional[List[CardEntity]] = None,
    ) -> List[CardEntity]:
        """Chooser over the player's hand, then discards the picks."""
        pid = player_id or self.player_id
        if self._trainer_blocked(pid):
            return []
        excluded = set(id(c) for c in (exclude or []))
        cards = [c for c in self.hand(pid)
                 if id(c) not in excluded and (predicate is None or predicate(c))]
        picked = await self.choose_cards(
            cards, count, minimum=minimum, prompt=prompt, player_id=pid
        )
        await self.discard_cards(picked)
        return picked

    # ------------------------------------------------------------------
    # Card movement primitives
    # ------------------------------------------------------------------

    async def draw_cards(self, count: int, player_id: Optional[str] = None) -> int:
        """Draws cards for a player (default: the effect's owner); returns how many."""
        pid = player_id or self.player_id
        if self._trainer_blocked(pid):
            return 0
        moved = self.board.draw_cards(pid, count)
        if moved:
            self.session.stat_add(pid, "cardsdrawn", len(moved))
        deck = self.board.find_player_area(pid, "deck")
        if moved and deck and deck.entity_id not in self._visual_sources:
            self._visual_sources.append(deck.entity_id)
        # Explicit Draw bracket (intros first), moves NESTED in a GroupedMove:
        # flat EntityMoveds get pre-handled by m.c and its S.o fan looks up a
        # bare "Draw" stack, which misses the path table (default linear
        # curve); nested moves animate FromDeck|ToHand with k.z's stagger --
        # the same top-of-deck arc as the initial deal.
        from .game_session import NestedSequence  # circular-import guard
        for move in moved:
            self._queue(self.session._entity_introduced_msg(move["card"]),
                        viewer_id=pid, bracket=GameSequence.DRAW.value)
        self._queue(NestedSequence(GameSequence.GROUPED_MOVE, [
            self.session._entity_moved_msg(
                move["entity_id"], move["destination_id"], move["position"]
            ) for move in moved
        ]), bracket=GameSequence.DRAW.value)
        return len(moved)

    async def draw_until(self, hand_size: int, player_id: Optional[str] = None) -> int:
        """Draws until a player's hand holds `hand_size` cards; returns how many."""
        missing = hand_size - self.hand_size(player_id)
        if missing <= 0:
            return 0
        return await self.draw_cards(missing, player_id)

    async def put_in_hand(self, cards: List[CardEntity], reveal: bool = True):
        """Moves cards (from deck/discard/etc.) into their owner's hand.

        reveal=True presents each card large to the opponent on the way
        ("...reveal it, and put it into your hand").
        """
        for card in cards:
            owner = card.owning_player_id or self.player_id
            hand = self.board.find_player_area(owner, "hand")
            if not hand:
                continue
            if self._energy_removal_blocked(card):
                continue
            self._note_visual_source(card)
            position = len(hand.children)
            if not self.board.move_card(card.entity_id, hand.entity_id):
                continue
            if isinstance(card, PokemonEntity):
                # Special Conditions/attack locks don't survive leaving play;
                # no bracket needed, the move itself clears the on-board marker.
                # Damage counters clear too -- reset before the intro is built
                # so the hand card (and any replay) carries the printed HP.
                self.session.clear_pokemon_effects(card)
                self.session.reset_pokemon_damage(card)
                self.session.reset_ability_usage(card)
            move = self.session._entity_moved_msg(card.entity_id, hand.entity_id, position)
            intro = self.session._entity_introduced_msg(card)
            opponent = self.session._opponent_id(owner)
            if reveal:
                # Both viewers get the k.z reveal delegation: the card
                # presents large-center, then flies into the hand
                # (AcceptRevealOf passes for the owner too on deck cards).
                for vid in (owner, opponent):
                    self._queue(intro, viewer_id=vid,
                                bracket=GameSequence.SERIAL_SEQUENCE.value)
                    self._queue(self.session._reveal_card_msg(card.entity_id, True),
                                viewer_id=vid, bracket=GameSequence.GROUPED_MOVE.value)
                    self._queue(move, viewer_id=vid,
                                bracket=GameSequence.GROUPED_MOVE.value)
            else:
                self._queue(intro, viewer_id=owner)
                self._queue(move, viewer_id=owner)
                self._queue(move, viewer_id=opponent)

    async def reveal_cards(self, cards: Sequence[CardEntity],
                           to_player: Optional[str] = None) -> None:
        """Reveals cards where they SIT ("reveal the top card of your deck"):
        each blind viewer gets the intro (SerialSequence) then a
        [RevealCardToAllEffect(Return=true), same-position move] GroupedMove
        pair -- k.z presents the card large-center and flies it home.

        to_player=None reveals to every viewer the card is currently hidden
        from (own-hand reveals reach the opponent; deck cards reach both).
        """
        for card in cards:
            parent = getattr(card, "parent", None)
            if parent is None:
                continue
            try:
                position = parent.children.index(card)
            except ValueError:
                position = 0
            if to_player is not None:
                viewers = [to_player]
            else:
                viewers = [pid for pid in self.session.players
                           if card.is_hidden_from(pid)]
            if not viewers:
                continue
            intro = self.session._entity_introduced_msg(card)
            move = self.session._entity_moved_msg(card.entity_id, parent.entity_id, position)
            for vid in viewers:
                self._queue(intro, viewer_id=vid,
                            bracket=GameSequence.SERIAL_SEQUENCE.value)
                self._queue(self.session._reveal_card_msg(card.entity_id, True),
                            viewer_id=vid, bracket=GameSequence.GROUPED_MOVE.value)
                self._queue(move, viewer_id=vid,
                            bracket=GameSequence.GROUPED_MOVE.value)

    async def reveal_hand(self, of_player: Optional[str] = None,
                          to_player: Optional[str] = None) -> List[CardEntity]:
        """View-only reveal browser over a player's whole hand ("your opponent
        reveals their hand"); nothing is selectable. Returns the hand cards
        so callers can count matches. AI viewers skip the browser."""
        owner = of_player or self.player_id
        viewer = to_player or self.session._opponent_id(owner)
        cards = self.hand(owner)
        if not cards:
            return []
        await self.session.prompt_view_cards(
            viewer, self.source.entity_id, cards,
            prompt="Your opponent's hand" if viewer != owner else "Revealed cards",
        )
        return cards

    async def present_card_choice(
        self, card: CardEntity, prompt: str, buttons: List[str],
        player_id: Optional[str] = None,
    ) -> int:
        """Show a single card in the ability-select pull-out with choice buttons."""
        from .ai_player import AIPlayer  # circular-import guard
        pid = player_id or self.player_id
        viewer = self.session.players[pid]
        if isinstance(viewer, AIPlayer):
            return 0
        session = self.session
        # R.U pulls the card into abilitySelectArea itself; a Return:false park would never clear
        intro = [session._entity_introduced_msg(card)]
        await session.send_game_sequence([viewer], GameSequence.SERIAL_SEQUENCE, intro)
        return await session.prompt_choice_panel(pid, card, buttons, prompt)

    async def discard_cards(self, cards: List[CardEntity]):
        """Moves cards to their owner's discard pile (a public zone)."""
        await self._move_to_public_pile(cards, "discard")

    async def discard_energy_from(
        self, pokemon: PokemonEntity, count: int,
        predicate: Optional[Callable[[CardEntity], bool]] = None,
        minimum: Optional[int] = None,
        prompt: str = "Choose Energy to discard",
    ) -> List[CardEntity]:
        """Discards `count` Energy attached to `pokemon` (chooser over the pips
        when the player must pick; all matching when count covers them all)."""
        energies = [e for e in self.attached_energies(pokemon)
                    if predicate is None or predicate(e)]
        if not energies or count <= 0:
            return []
        if len(energies) <= count:
            picked = energies
        else:
            picked = await self.choose_cards(
                energies, count, minimum=count if minimum is None else minimum,
                prompt=prompt,
            )
        await self.discard_cards(picked)
        return picked

    async def discard_energy_units_from(
        self, pokemon: PokemonEntity, amount: int,
        predicate: Optional[Callable[[CardEntity], bool]] = None,
        prompt: str = "Choose Energy to discard",
    ) -> List[CardEntity]:
        """Discard cards providing at least ``amount`` attached Energy.

        Use this for card text that counts Energy as a provided value (for
        example, Hyper Potion's "discard 2 Energy"). ``discard_energy_from``
        remains the physical-card-count primitive for text that says "Energy
        cards" or otherwise requires a specific number of card entities.
        """

        energies = [
            energy for energy in self.attached_energies(pokemon)
            if predicate is None or predicate(energy)
        ]
        total = sum(
            energy_provided_count(energy, self.board) for energy in energies
        )
        if amount <= 0 or total < amount:
            return []

        if total <= amount:
            picked = energies
        else:
            picked_ids = await self.session.prompt_energy_unit_picker(
                self.player_id,
                self.source.entity_id,
                energies,
                amount,
                prompt,
            )
            by_id = {energy.entity_id: energy for energy in energies}
            picked = [by_id[entity_id] for entity_id in picked_ids
                      if entity_id in by_id]

        paid = sum(energy_provided_count(energy, self.board) for energy in picked)
        if paid < amount:
            logging.warning(
                f"[Effects {self.game_id}] Energy payment {amount} resolved "
                f"with only {paid}; no cards discarded."
            )
            return []
        await self.discard_cards(picked)
        return picked

    async def move_to_lost_zone(self, cards: List[CardEntity]):
        """Moves cards to their owner's Lost Zone (a public zone)."""
        await self._move_to_public_pile(cards, "lostZone")

    async def _move_to_public_pile(self, cards: List[CardEntity], area_name: str):
        for card in cards:
            owner = card.owning_player_id or self.player_id
            pile = self.board.find_player_area(owner, area_name)
            if not pile:
                continue
            if self._trainer_blocked(card):
                continue
            # Opponent-caused discards can be shielded (Bibarel PGO/Greedent);
            # own discards (costs) always resolve.
            if area_name == "discard" and owner != self.player_id \
                    and discard_blocked(self.board, card):
                logging.info(
                    f"[Effects {self.game_id}] Discard of {card.entity_id} "
                    f"blocked by a passive."
                )
                continue
            if area_name == "discard" and self._energy_removal_blocked(card):
                continue
            holder = self._tool_holder_before_move(card)
            source = getattr(card, "parent", None)
            # deck/prizes are face-down to the owner too, so a card from there
            # needs a face for the owner or the pile shows a card back and the
            # Lost Zone viewer NREs on the missing archetype attr.
            owner_blind = (source is not None
                           and source.get_attribute(AttrID.NAME) in ("deck", "prizePile"))
            position = len(pile.children)
            if not self.board.move_card(card.entity_id, pile.entity_id):
                continue
            if isinstance(card, PokemonEntity):
                self.session.clear_pokemon_effects(card)
                self.session.reset_pokemon_damage(card)
                self.session.reset_ability_usage(card)
            opponent = self.session._opponent_id(owner)
            intro = self.session._entity_introduced_msg(card)
            # Entering a public pile reveals the card to the opponent.
            self._queue(intro, viewer_id=opponent,
                        bracket=GameSequence.SERIAL_SEQUENCE.value)
            if owner_blind:
                self._queue(intro, viewer_id=owner,
                            bracket=GameSequence.SERIAL_SEQUENCE.value)
            move = self.session._entity_moved_msg(card.entity_id, pile.entity_id, position)
            self._queue(move, bracket=GameSequence.GROUPED_MOVE.value)
            if holder is not None:
                await self.session.refresh_granted_abilities(holder)
            if area_name == "discard" and owner != self.player_id \
                    and source is not None \
                    and source.get_attribute(AttrID.NAME) == "hand":
                # Opponent-forced hand discard (Amoonguss "Surprise Spores"):
                # fire deferred so the trigger's brackets follow this flush.
                async def _fire_hand_discard(card=card, owner=owner):
                    await self.session._fire_triggered_abilities(
                        owner, card, Triggers.ON_DISCARDED_FROM_HAND)
                self.deferred_actions.append(_fire_hand_discard)

    async def look_at_prizes_take_basic(self) -> bool:
        """Hisuian Heavy Ball: look at your face-down Prizes; you may reveal a
        Basic Pokemon to your hand and put the source card in its place as a
        face-down Prize. Always shuffles the Prizes (re-hiding them).

        Returns True when a Basic was taken (the source now sits in the Prize
        pile, so the caller must NOT discard it); False when declined.

        Sends immediately (not via the deferred bracket runs) so the reveal,
        pick, hand-in, swap, re-hide and shuffle choreograph in order.
        """
        session = self.session
        prize_area = self.board.find_player_area(self.player_id, "prizePile")
        if not prize_area or not prize_area.children:
            return False
        prizes = list(prize_area.children)
        basics = [c for c in prizes if is_basic_pokemon(c)]
        picked_id = await session.prompt_prize_reveal_pick(
            self.player_id, self.source.entity_id,
            [c.entity_id for c in prizes], [c.entity_id for c in basics],
        )
        picked = self.board.get_entity(picked_id) if picked_id else None
        opponent = self.opponent_id
        both = list(session.players.values())
        took = False
        if isinstance(picked, CardEntity):
            slot = getattr(picked, "board_slot", None)
            if slot is None:
                slot = prizes.index(picked)
            hand = self.board.find_player_area(self.player_id, "hand")
            # Take the Basic to hand via WithOpenPrizeCards: once a Prize is
            # picked, r.B's own cleanup skips the fan teardown and defers to
            # this bracket, which cancels the explore command, flips+flies the
            # taken card to hand and CLOSES the present (blackout off,
            # PrizesDisplayed false). A plain GroupedMove leaves the fan on
            # screen. Both viewers get intro+move so the Basic is revealed
            # (d.t's introduceAndFlipPrizeIfNeeded flips it face-up).
            pos = len(hand.children)
            self.board.move_card(picked.entity_id, hand.entity_id)
            take = [session._entity_introduced_msg(picked),
                    session._entity_moved_msg(picked.entity_id, hand.entity_id, pos)]
            for viewer in both:
                await session.send_game_sequence(
                    [viewer], GameSequence.WITH_OPEN_PRIZE_CARDS, list(take))
            # The source card takes the vacated face-down Prize slot.
            if self.board.move_card(self.source.entity_id, prize_area.entity_id, slot):
                await session.send_game_sequence(
                    both, GameSequence.GROUPED_MOVE,
                    [session._entity_moved_msg(
                        self.source.entity_id, prize_area.entity_id, slot)])
                took = True
        # Re-hide every now-revealed Prize for the picker; the swapped-in source
        # is also face-up to the opponent (it sat on the trainer slot), so reset
        # it there too. Then shuffle -- both viewers see the reshuffle.
        resets = [session._attributes_reset_msg(c.entity_id)
                  for c in prize_area.children]
        if resets:
            await session.send_game_sequence(
                [session.players[self.player_id]], GameSequence.GROUPED_MOVE, resets)
        if took:
            await session.send_game_sequence(
                [session.players[opponent]], GameSequence.GROUPED_MOVE,
                [session._attributes_reset_msg(self.source.entity_id)])
        random.shuffle(prize_area.children)
        await session.send_game_sequence(
            both, GameSequence.GROUPED_MOVE,
            [session._build_msg(OutboundMsg.SHUFFLED.value,
                                {"gameID": self.game_id, "entityID": prize_area.entity_id})])
        return took

    async def shuffle_deck(self, player_id: Optional[str] = None):
        """Shuffles a player's deck and queues the shuffle animation."""
        pid = player_id or self.player_id
        self.board.shuffle_deck(pid)
        deck = self.board.find_player_area(pid, "deck")
        if deck:
            self._queue(self.session._build_msg(
                OutboundMsg.SHUFFLED.value,
                {"gameID": self.game_id, "entityID": deck.entity_id},
            ), bracket=GameSequence.GROUPED_MOVE.value)

    async def shuffle_into_deck(self, cards: List[CardEntity],
                                player_id: Optional[str] = None):
        """Moves cards into their owner's deck, then shuffles it."""
        pid = player_id or self.player_id
        deck = self.board.find_player_area(pid, "deck")
        if not deck:
            return
        for card in cards:
            if self._trainer_blocked(card) or self._energy_removal_blocked(card):
                continue
            holder = self._tool_holder_before_move(card)
            position = len(deck.children)
            if self.board.move_card(card.entity_id, deck.entity_id):
                if isinstance(card, PokemonEntity):
                    # A shuffled-in Pokemon must not carry stale Special
                    # Conditions or damage when it's later drawn/re-introduced
                    # or SGS-serialized.
                    self.session.clear_pokemon_effects(card)
                    self.session.reset_pokemon_damage(card)
                    self.session.reset_ability_usage(card)
                self._queue(
                    self.session._entity_moved_msg(card.entity_id, deck.entity_id, position),
                    bracket=GameSequence.GROUPED_MOVE.value,
                )
                if holder is not None:
                    await self.session.refresh_granted_abilities(holder)
        await self.shuffle_deck(pid)

    async def hand_to_bottom_of_deck(self, player_id: Optional[str] = None) -> int:
        """Shuffles a player's hand and puts it under their deck (Marnie-style).

        Sends the HandShuffledAndMovedToDeck bracket (V.s): moves pile into
        the hand-shuffle area, Shuffled(hand) plays the pile shuffle, then
        PlaceOnBottom lifts the deck; V.s NREs without a PlaceOnBottom.
        """
        pid = player_id or self.player_id
        if self._trainer_blocked(pid):
            return 0
        hand = self.board.find_player_area(pid, "hand")
        deck = self.board.find_player_area(pid, "deck")
        if not hand or not deck or not hand.children:
            return 0
        cards = list(hand.children)
        random.shuffle(cards)
        bracket = GameSequence.HAND_SHUFFLED_AND_MOVED_TO_DECK.value
        # Shuffled on the HAND entity picks the hand-shuffle animator (c.m).
        self._queue(self.session._build_msg(
            OutboundMsg.SHUFFLED.value,
            {"gameID": self.game_id, "entityID": hand.entity_id},
        ), bracket=bracket)
        for card in cards:
            # Bottom of the deck is position 0 (draws take the last child).
            if self.board.move_card(card.entity_id, deck.entity_id, 0):
                self._queue(
                    self.session._entity_moved_msg(card.entity_id, deck.entity_id, 0),
                    bracket=bracket,
                )
        self._queue(self.session._build_msg(
            OutboundMsg.PLACE_ON_BOTTOM.value,
            {"gameID": self.game_id, "entityID": hand.entity_id,
             "target": deck.entity_id},
        ), bracket=bracket)
        return len(cards)

    async def reorder_deck_top(self, count: int,
                               player_id: Optional[str] = None,
                               prompt: str = "Rearrange the cards on top of your deck",
                               ) -> List[CardEntity]:
        """Looks at the top `count` deck cards and puts them back in any
        order (ordered browser, owner-only; the opponent learns nothing --
        hidden-zone browser cards re-hide on close and no moves are sent).
        Returns the new top order (topmost first)."""
        pid = player_id or self.player_id
        top = self.deck_top(count, pid)
        if len(top) <= 1:
            return top
        picked_ids = await self.session.prompt_card_chooser(
            pid, self.source.entity_id, top, len(top), minimum=len(top),
            prompt=prompt, ordered=True,
        )
        by_id = {c.entity_id: c for c in top}
        order = [by_id[i] for i in picked_ids if i in by_id]
        for card in top:
            if card not in order:
                order.append(card)
        deck = self.board.find_player_area(pid, "deck")
        for card in order:
            deck.children.remove(card)
        # First pick = new top; top of the deck is the LAST child.
        for card in reversed(order):
            deck.children.append(card)
        return order

    async def put_on_top_of_deck(self, card: CardEntity) -> bool:
        """Puts a card on top of its owner's deck."""
        owner = card.owning_player_id or self.player_id
        deck = self.board.find_player_area(owner, "deck")
        if not deck or self._energy_removal_blocked(card):
            return False
        position = len(deck.children)
        if not self.board.move_card(card.entity_id, deck.entity_id):
            return False
        self._queue(
            self.session._entity_moved_msg(card.entity_id, deck.entity_id, position),
            bracket=GameSequence.GROUPED_MOVE.value,
        )
        return True

    async def put_on_bottom_of_deck(self, card: CardEntity) -> bool:
        """Puts a card on the bottom of its owner's deck (position 0)."""
        owner = card.owning_player_id or self.player_id
        deck = self.board.find_player_area(owner, "deck")
        if not deck or self._energy_removal_blocked(card):
            return False
        if not self.board.move_card(card.entity_id, deck.entity_id, 0):
            return False
        self._queue(
            self.session._entity_moved_msg(card.entity_id, deck.entity_id, 0),
            bracket=GameSequence.GROUPED_MOVE.value,
        )
        return True

    async def bench_pokemon(self, card: CardEntity) -> bool:
        """Puts a Pokemon from a non-hand zone onto its owner's bench.

        "Put onto your Bench" is not "play from hand": on-play triggered
        abilities deliberately do NOT fire.
        """
        owner = card.owning_player_id or self.player_id
        bench = self.board.find_player_area(owner, "bench")
        if not bench or len(bench.children) >= effective_bench_capacity(self.board, owner):
            return False
        self._note_visual_source(card)
        # Lowest free SLOT (client stamp), not list length -- gaps left by
        # promoted/KO'd Pokemon must be filled or cards render overlapped.
        position = self.board.free_bench_slot(owner)
        if not self.board.move_card(card.entity_id, bench.entity_id):
            return False
        self.session.turn_state.mark_entered_play(card.entity_id)
        # Entering play from any zone is public knowledge.
        self._queue_intro_and_move(card, bench.entity_id, position)
        return True

    async def evolve_pokemon(self, target: PokemonEntity,
                             evolution_card: CardEntity) -> bool:
        """Effect-driven evolution (Rare Candy): bypasses the may-evolve turn
        rules entirely; handles deck-sourced evolution cards (intro to both
        viewers before the Evolve bracket per the wrap-FX rule). Flushes any
        queued choreography first so the brackets land in order."""
        if target is None or evolution_card is None:
            return False
        area_name = evolution_card._containing_area_name() \
            if isinstance(evolution_card, CardEntity) else None
        from_hidden = area_name in CardEntity.HIDDEN_FROM_OWNER_AREAS
        owner = evolution_card.owning_player_id or self.player_id
        await self.flush_choreography()
        return await self.session.perform_evolution(
            owner, evolution_card, target, from_zone_intro=from_hidden
        )

    async def devolve_pokemon(self, pokemon: PokemonEntity, steps: int = 1,
                              destination: str = "hand") -> List[CardEntity]:
        """Devolves an evolved Pokemon `steps` times (highest stage first);
        removed evolution cards go to the owner's `destination` ('hand' or
        'deck'). Damage carries down; a final stage left at 0 HP queues on
        ctx.knockouts (the caller's flow resolves it). Flushes queued
        choreography first so the Devolve brackets land in order."""
        removed: List[CardEntity] = []
        if pokemon is None:
            return removed
        await self.flush_choreography()
        top = pokemon
        for i in range(steps):
            result = await self.session.perform_devolution(
                top, destination_name=destination,
                clamp_nonlethal=(i < steps - 1),
            )
            if result is None:
                break
            top, removed_card = result
            removed.append(removed_card)
            # The removed card left play to hand/deck: any KO queued against
            # it (Rewind Beam's 180 first) follows the remaining stage instead.
            if removed_card in self.knockouts:
                self.knockouts.remove(removed_card)
        if removed and top.get_attribute(AttrID.HP, 0) <= 0 \
                and top not in self.knockouts:
            self.knockouts.append(top)
        return removed

    async def identity_swap(self, outgoing: PokemonEntity, incoming: CardEntity,
                            destination: str = "discard",
                            transfer: bool = True) -> bool:
        """Switches an in-play Pokemon with a hand/discard card; see
        GameSession.perform_identity_swap. transfer=True carries attachments/
        damage/conditions/turn stamps onto the new Pokemon; a transferred
        damage total covering its HP queues a knockout. Flushes queued
        choreography first so the swap brackets land in order."""
        if outgoing is None or incoming is None:
            return False
        await self.flush_choreography()
        result = await self.session.perform_identity_swap(
            outgoing, incoming, destination_name=destination, transfer=transfer)
        if result is None:
            return False
        if outgoing in self.knockouts:
            self.knockouts.remove(outgoing)
        if incoming.get_attribute(AttrID.HP, 0) <= 0 \
                and incoming not in self.knockouts:
            self.knockouts.append(incoming)
        return True

    async def attach_energy(self, energy: CardEntity, pokemon: PokemonEntity,
                            counts_as_attachment: bool = False) -> bool:
        """Attaches an energy card from any zone underneath a Pokemon
        (effect attachments don't consume the once-per-turn manual attach).

        counts_as_attachment=True additionally fires ON_ENERGY_ATTACHED
        observers (deferred until the choreography flushes); most effect
        attaches are NOT "attaching from hand" and leave it False.
        """
        if energy is None or pokemon is None:
            return False
        position = len(pokemon.children)
        if not self.board.attach_card(energy.entity_id, pokemon.entity_id):
            return False
        self._queue_intro_and_move(energy, pokemon.entity_id, position)
        if counts_as_attachment:
            self.deferred_actions.append(
                lambda e=energy, p=pokemon: self.session.fire_energy_attached_triggers(
                    self.player_id, e, p))
        return True

    async def move_energy(self, energy: CardEntity, to_pokemon: PokemonEntity) -> bool:
        """Moves an attached Energy onto another in-play Pokemon: no intro
        (attached cards are already public), the GroupedMove plays the attach
        FX; max-HP bonuses shift with the card, damage taken stays constant."""
        if energy is None or to_pokemon is None:
            return False
        old_holder = carrier_pokemon(energy)
        if old_holder is to_pokemon:
            return False
        granted_holder = self._tool_holder_before_move(energy)
        max_before_old = effective_max_hp(self.board, old_holder) \
            if old_holder is not None else 0
        max_before_new = effective_max_hp(self.board, to_pokemon)
        position = len(to_pokemon.children)
        if not self.board.attach_card(energy.entity_id, to_pokemon.entity_id):
            return False
        self._queue(
            self.session._entity_moved_msg(energy.entity_id, to_pokemon.entity_id, position),
            bracket=GameSequence.GROUPED_MOVE.value,
        )
        if granted_holder is not None:
            await self.session.refresh_granted_abilities(granted_holder)
        if old_holder is not None:
            self._shift_max_hp(old_holder, max_before_old)
        self._shift_max_hp(to_pokemon, max_before_new)
        return True

    def _shift_max_hp(self, pokemon: PokemonEntity, max_before: int) -> None:
        """Keeps damage-taken constant when an attachment's max-HP bonus
        arrives/leaves mid-effect; queues the HP update, enqueues a KO at 0."""
        max_after = effective_max_hp(self.board, pokemon)
        self.session._effective_max_seen[pokemon.entity_id] = max_after
        delta = max_after - max_before
        if delta == 0:
            return
        current = max(0, pokemon.get_attribute(AttrID.HP, 0) + delta)
        pokemon.set_attribute(AttrID.HP, current)
        self._queue_hp_update(pokemon)
        if current <= 0 and pokemon not in self.knockouts:
            self.knockouts.append(pokemon)

    async def move_energy_freely(
        self,
        sources: Sequence[PokemonEntity],
        dest_candidates: Sequence[PokemonEntity],
        predicate: Optional[Callable[[CardEntity], bool]] = None,
        max_count: Optional[int] = None,
        prompt: str = "Choose an Energy to move",
    ) -> List[Tuple[CardEntity, PokemonEntity]]:
        """"Move any amount of Energy ... in any way you like": repeats
        [pick an attached energy pip, minimum 0 = stop] -> [pick its
        destination] until the player declines or the pool is exhausted.
        Each energy moves at most once. Returns the (energy, dest) moves."""
        moved: List[Tuple[CardEntity, PokemonEntity]] = []
        source_list = list(sources)
        while max_count is None or len(moved) < max_count:
            moved_ids = {e.entity_id for e, _ in moved}
            pool = [e for p in source_list for e in self.attached_energies(p)
                    if e.entity_id not in moved_ids
                    and (predicate is None or predicate(e))]
            if not pool:
                break
            picked = await self.choose_cards(pool, 1, minimum=0, prompt=prompt)
            if not picked:
                break
            energy = picked[0]
            holder = carrier_pokemon(energy)
            dests = [d for d in dest_candidates if d is not holder]
            if not dests:
                break
            dest = await self.choose_pokemon(
                dests, "Choose a Pokémon to move the Energy to")
            if dest is None or not await self.move_energy(energy, dest):
                break
            moved.append((energy, dest))
        return moved

    async def switch_active(self, player_id: str, new_active: PokemonEntity) -> bool:
        """Swaps a player's Active with the given benched Pokemon (gust or
        self-switch). Special Conditions on the leaving Active are cured."""
        # Guard on the gusted bench Pokemon: entity-scoped shields (Princess's
        # Curtain) protect the chosen bencher, not the whole side.
        if self._trainer_blocked(new_active):
            return False
        board = self.board
        active_area = board.find_player_area(player_id, "activePokemonArea")
        bench_area = board.find_player_area(player_id, "bench")
        old_active = board.active_pokemon(player_id)
        if not active_area or not bench_area or old_active is None:
            return False
        if new_active not in bench_area.children:
            return False

        # All effects (Special Conditions, attack locks) end when a Pokemon
        # leaves the Active spot; the state-clearing lives in one shared helper.
        had_conditions = bool(old_active.get_attribute(AttrID.SPECIAL_CONDITIONS))
        self.session.clear_pokemon_effects(old_active)
        if had_conditions:
            self._queue(
                self.session._entity_id_data_effect_msg("Target", old_active.entity_id),
                bracket=GameSequence.REMOVE_SPECIAL_CONDITION.value,
            )
            self._queue(
                self.session._condition_attr_msg(old_active),
                bracket=GameSequence.REMOVE_SPECIAL_CONDITION.value,
            )

        # Old active takes the new active's rendered SLOT (client stamp),
        # captured before the active move overwrites the stamp with 0.
        slot = board.bench_slot_of(new_active)
        board.move_card(new_active.entity_id, active_area.entity_id)
        board.move_card(old_active.entity_id, bench_area.entity_id, slot)
        self.session.turn_state.became_active_turn[new_active.entity_id] = \
            self.session.turn_state.turn_number
        # Retreat (N.P) is the only executor that flies both swap moves
        # concurrently; it requires the Retreating/NewActive data effects.
        # NEVER ParallelSequence (r.M's command list is null in this build).
        bracket = GameSequence.RETREAT.value
        self._queue(
            self.session._entity_id_data_effect_msg("Retreating", old_active.entity_id),
            bracket=bracket,
        )
        self._queue(
            self.session._entity_id_data_effect_msg("NewActive", new_active.entity_id),
            bracket=bracket,
        )
        self._queue(
            self.session._entity_moved_msg(new_active.entity_id, active_area.entity_id, 0),
            bracket=bracket,
        )
        self._queue(
            self.session._entity_moved_msg(old_active.entity_id, bench_area.entity_id, slot),
            bracket=bracket,
        )
        # Spikemuth: an Active moving to its owner's Bench during THEIR turn
        # takes counters (a gust during the opponent's turn does not).
        if player_id == self.session.turn_state.active_player_id:
            counters = active_to_bench_counters(board, old_active)
            if counters > 0:
                await self.deal_damage(
                    counters * 10, target=old_active, as_counters=True)
        # ON_MOVE_TO_ACTIVE fires after the swap choreography flushes.
        self.deferred_actions.append(
            lambda p=new_active: self.session.fire_move_to_active_triggers(p))
        return True

    async def flush_choreography(self):
        """Sends and clears the currently queued choreography brackets, so a
        following dialog resolves only after both clients see them land
        (Escape Rope: the opponent's swap shows before the player decides)."""
        await self.session._flush_effect_runs(self)
        self._messages.clear()

    async def take_prizes(self, count: int, player_id: Optional[str] = None,
                          minimum: Optional[int] = None,
                          check_win: bool = True) -> List[CardEntity]:
        """Takes prize cards outside the KO flow (Slowbro PGO): flushes the
        queued choreography first so the prize fan never interleaves, then
        runs the standard pick + WithOpenPrizeCards flow and the win check.
        minimum<count makes it "up to count"; check_win=False skips the
        all-prizes win (Peonia refills the pile). Returns the taken cards."""
        pid = player_id or self.player_id
        if count <= 0:
            return []
        await self.flush_choreography()
        taken = await self.session._take_prizes(pid, count, minimum=minimum)
        prizes = self.board.find_player_area(pid, "prizePile")
        if check_win and prizes is not None and self.board.prizes_dealt.get(pid) \
                and not prizes.children:
            await self.session.end_game(pid, "Took all Prize cards")
        return taken or []

    async def put_in_prizes(self, cards: List[CardEntity],
                            player_id: Optional[str] = None) -> int:
        """Puts hand cards face down into the player's empty Prize slots
        (Peonia): queues the moves, AttributesReset re-hides (the owner knows
        the faces) and the pile's gap refresh; returns how many were placed."""
        pid = player_id or self.player_id
        session = self.session
        prize_area = self.board.find_player_area(pid, "prizePile")
        if prize_area is None or not cards:
            return 0
        dealt = self.board.prizes_dealt.get(pid, 0)
        occupied = {c.board_slot if c.board_slot is not None else i
                    for i, c in enumerate(prize_area.children)}
        slots = [s for s in range(dealt) if s not in occupied]
        placed = 0
        for card in cards:
            slot = slots.pop(0) if slots else dealt + placed
            if not self.board.move_card(card.entity_id, prize_area.entity_id, slot):
                continue
            self._queue(session._entity_moved_msg(
                card.entity_id, prize_area.entity_id, slot),
                bracket=GameSequence.GROUPED_MOVE.value)
            self._queue(session._attributes_reset_msg(card.entity_id),
                        bracket=GameSequence.GROUPED_MOVE.value)
            placed += 1
        if placed:
            self._queue(session._refresh_prize_gaps(pid, prize_area),
                        bracket=GameSequence.GROUPED_MOVE.value)
        return placed

    async def win_game(self, reason: str = "") -> None:
        """Declares the effect's owner the winner (Unown V; raises GameOver)."""
        await self.session.end_game(self.player_id, reason or "Victory")

    async def discard_stadium(self) -> Optional[BoardEntity]:
        """Discards the in-play Stadium to its owner's discard; returns it or None."""
        stadium = self.stadium_in_play()
        if stadium is None:
            return None
        owner_id = stadium.owning_player_id or self.player_id
        discard = self.board.find_player_area(owner_id, "discard")
        if not discard:
            return None
        position = len(discard.children)
        if not self.board.move_card(stadium.entity_id, discard.entity_id):
            return None
        self._queue(self.session._entity_moved_msg(
            stadium.entity_id, discard.entity_id, position
        ))
        return stadium

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _queue(self, msg: Dict[str, Any], viewer_id: Optional[str] = None,
               bracket: Optional[str] = None):
        self._messages.append((viewer_id, msg, bracket))

    def _queue_intro_and_move(self, card: CardEntity, dest_id: str, position: int,
                              intro_viewer_id: Optional[str] = None):
        """Queues the intro (SerialSequence) + move (GroupedMove) bracket pair."""
        self._queue(self.session._entity_introduced_msg(card), viewer_id=intro_viewer_id,
                    bracket=GameSequence.SERIAL_SEQUENCE.value)
        self._queue(self.session._entity_moved_msg(card.entity_id, dest_id, position),
                    bracket=GameSequence.GROUPED_MOVE.value)

    def _tool_holder_before_move(self, card: CardEntity) -> Optional[PokemonEntity]:
        """The Pokemon `card` is about to be moved off of, if it's an
        attached tool with granted_abilities (Forest Seal Stone leaving)."""
        parent = getattr(card, "parent", None)
        if not isinstance(parent, PokemonEntity):
            return None
        if getattr(def_for(card.archetype_id), "granted_abilities", None):
            return parent
        return None

    def _note_visual_source(self, card: CardEntity):
        """Records the pile a card is pulled from as an orb-FX target."""
        parent = getattr(card, "parent", None)
        if (parent is not None and not isinstance(parent, CardEntity)
                and parent.entity_id not in self._visual_sources):
            self._visual_sources.append(parent.entity_id)

    def _queue_hp_update(self, target: PokemonEntity):
        self._queue(self.session._build_msg(
            OutboundMsg.ATTRIBUTE_MODIFIED.value,
            {
                "gameID": self.game_id,
                "entityID": target.entity_id,
                "attribute": {
                    "name": AttrID.HP.value,
                    "value": target.get_attribute(AttrID.HP, 0),
                    "originalValue": self.max_hp(target),
                    "modValue": None,
                },
            },
        ))

    def messages_for(self, viewer_id: str) -> List[Dict[str, Any]]:
        return [msg for vid, msg, _ in self._messages
                if vid is None or vid == viewer_id]

    def bracket_runs_for(
        self, viewer_id: str, default: str = GameSequence.GROUPED_MOVE.value
    ) -> List[Tuple[str, List[Dict[str, Any]]]]:
        """The viewer's messages grouped into consecutive same-bracket runs."""
        runs: List[Tuple[str, List[Dict[str, Any]]]] = []
        for vid, msg, bracket in self._messages:
            if vid is not None and vid != viewer_id:
                continue
            name = bracket or default
            if runs and runs[-1][0] == name:
                runs[-1][1].append(msg)
            else:
                runs.append((name, [msg]))
        return runs


# Attack scripts predate the generalized context; keep the old name working.
AttackContext = EffectContext


# ----------------------------------------------------------------------
# Card filters for search/chooser predicates
# ----------------------------------------------------------------------

def is_pokemon_card(card: CardEntity) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value


def is_basic_pokemon(card: CardEntity) -> bool:
    return (
        is_pokemon_card(card)
        and card.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
    )


def is_evolution_pokemon(card: CardEntity) -> bool:
    return (
        is_pokemon_card(card)
        and card.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value
    )


def is_water_pokemon(card: CardEntity) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.WATER.value in types


def is_trainer_card(card: CardEntity) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value


def is_item_card(card: CardEntity) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.ITEM.value


def is_supporter_card(card: CardEntity) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value


def is_special_energy(card: CardEntity) -> bool:
    return bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def full_stack(pokemon: PokemonEntity) -> List[CardEntity]:
    """A Pokemon plus every card attached under it, depth-first."""
    out: List[CardEntity] = [pokemon]
    queue: List[BoardEntity] = list(pokemon.children)
    while queue:
        entity = queue.pop(0)
        if isinstance(entity, CardEntity):
            out.append(entity)
        queue.extend(entity.children)
    return out


def is_colorless_no_rule_box(card: CardEntity) -> bool:
    """Summoning Star's filter: Colorless Pokemon without a Rule Box."""
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return (
        is_pokemon_card(card)
        and PokemonTypes.COLORLESS.value in types
        and not has_rule_box(card.archetype_id)
    )


# ----------------------------------------------------------------------
# Resolution entry points
# ----------------------------------------------------------------------

async def resolve_attack(session, player_id: str, attacker: PokemonEntity,
                         ability: Optional[Ability], action_id: str):
    """Runs an attack's effect and plays the full client choreography.

    Vanilla attacks (no effect) resolve their printed damage; `unimplemented`
    effects do the same and log the missing text.
    """
    ctx = AttackContext(session, player_id, attacker, ability)
    effect = ability.effect if ability else None
    title = ability.title if ability else action_id
    ctx._copy_chain.append(title)
    session.turn_state.attacks_used.append(
        (attacker.entity_id, attacker.archetype_id, title)
    )

    if effect is None or effect is unimplemented:
        if effect is unimplemented:
            logging.warning(
                f"[Effects {session.game_id}] Attack '{title}' has unimplemented "
                f"text; resolving base damage only."
            )
        await ctx.deal_damage()
    else:
        await effect(ctx)

    await _send_attack_bracket(session, ctx, action_id, title)
    # ON_DAMAGED_BY_ATTACK fires after the attack choreography but BEFORE the
    # knockout stacks move ("even if this Pokemon is Knocked Out").
    await _fire_damaged_by_attack_triggers(session, ctx)
    ctx.knockouts_resolved = list(ctx.knockouts)
    await session.resolve_knockouts(ctx)
    for hook in ctx.deferred_actions:
        await hook()
    # A KO'd/removed carrier may have shrunk a bench (Eternatus VMAX leaving).
    await session.enforce_bench_capacity()
    await _run_attack_followups(session, ctx)
    return ctx


async def _run_attack_followups(session, ctx: EffectContext):
    """End-of-turn attack riders (Blunder Policy): runs each active passive's
    attack_followup with the flushed ctx; new messages flush as own brackets."""
    followups = [(p, c) for p, c in active_passives(session.board_state)
                 if getattr(p, "attack_followup", None) is not None]
    if not followups:
        return
    # The attack bracket already sent ctx's queue; start a fresh one.
    ctx._messages.clear()
    for passive, carrier in followups:
        await passive.attack_followup(ctx, carrier)
    await session._flush_effect_runs(ctx)
    ctx._messages.clear()


async def _fire_damaged_by_attack_triggers(session, ctx: EffectContext):
    """Fires ON_DAMAGED_BY_ATTACK for every Pokemon the attack damaged; the
    trigger ctx carries damaged_by / damage_amount / pre_hit_hp."""
    if not ctx.attack_damage:
        return
    board = session.board_state
    snapshot: List[Tuple[PokemonEntity, str, Ability, int, int]] = []
    for entity_id, (dealt, pre_hit) in ctx.attack_damage.items():
        pokemon = board.get_entity(entity_id)
        if not isinstance(pokemon, PokemonEntity):
            continue
        owner_id = pokemon.owning_player_id
        if owner_id is None:
            continue
        locked = ability_locked(board, pokemon)
        for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
            if not isinstance(entry, dict):
                continue
            ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
            if ability is None or not ability.has_trigger(Triggers.ON_DAMAGED_BY_ATTACK):
                continue
            if locked and not ability.is_granted:
                continue
            snapshot.append((pokemon, owner_id, ability, dealt, pre_hit))
    for pokemon, owner_id, ability, dealt, pre_hit in snapshot:
        def _setup(c, _dealt=dealt, _pre=pre_hit):
            c.damaged_by = ctx.attacker
            c.damage_amount = _dealt
            c.pre_hit_hp = _pre
        await resolve_triggered_ability(session, owner_id, pokemon, ability,
                                        ctx_setup=_setup)


async def resolve_triggered_ability(
    session, player_id: str, pokemon: PokemonEntity, ability: Ability,
    ctx_setup: Optional[Callable[[EffectContext], None]] = None,
    _ko_depth: int = 0,
) -> Optional[EffectContext]:
    """Runs a triggered ability (on-play/on-evolve/on-knocked-out/between-turns)
    with the full activation choreography; returns its ctx, or None when the
    ability didn't run (locked, or no scripted effect)."""
    if ability_locked(session.board_state, pokemon) and not ability.is_granted:
        return None
    if ability.effect is None or ability.effect is unimplemented:
        if ability.effect is unimplemented:
            logging.warning(
                f"[Effects {session.game_id}] Triggered ability '{ability.title}' "
                f"has unimplemented text; skipped."
            )
        return None
    ctx = EffectContext(session, player_id, pokemon, ability)
    if ctx_setup is not None:
        ctx_setup(ctx)
    await ability.effect(ctx)
    # Same rule as activated abilities: a declined "you may" queues no
    # messages and must not end the turn (Climactic Gate).
    if getattr(ability, "ends_turn", False) and ctx._messages:
        ctx.ends_turn = True
    await _send_ability_brackets(session, ctx, pokemon, ability, _ko_depth=_ko_depth)
    return ctx


# Card scripts/tests import the pre-generalization name; same function.
resolve_on_play_ability = resolve_triggered_ability


async def resolve_activated_ability(session, player_id: str, pokemon: PokemonEntity,
                                    ability: Ability) -> EffectContext:
    """Runs a player-activated ability (Activations.ONCE_PER_TURN / VSTAR);
    returns its ctx (the executor reads ctx.ends_turn off it).

    The caller has already validated usability and marked the once-per-turn /
    once-per-game bookkeeping.
    """
    ctx = EffectContext(session, player_id, pokemon, ability)
    if ability.effect is unimplemented:
        logging.warning(
            f"[Effects {session.game_id}] Activated ability '{ability.title}' "
            f"has unimplemented text; announcing only."
        )
    elif ability.effect is not None:
        await ability.effect(ctx)
    # Ability(ends_turn=True) only bites when the effect actually did
    # something (a declined "you may" queues no messages).
    if getattr(ability, "ends_turn", False) and ctx._messages:
        ctx.ends_turn = True
    # Tuck the pulled-back ability panel home on the user's client.
    viewer = session.players.get(player_id)
    if viewer is not None:
        await session.send_game_sequence(
            [viewer], GameSequence.DISMISS_ABILITY_SELECT, []
        )
    await _send_ability_brackets(session, ctx, pokemon, ability)
    return ctx


async def _send_ability_brackets(session, ctx: EffectContext,
                                 pokemon: PokemonEntity, ability: Ability,
                                 _ko_depth: int = 0):
    """Shared ability choreography: an "Attack" bracket pulls the source out
    and shoots the orb-of-light at the visual targets; the "PokeAbility"
    bracket tucks the source home and plays the effect messages."""
    head = session._build_msg(
        OutboundMsg.ABILITY_PLAYED_EFFECT.value,
        {
            "gameID": session.game_id,
            "eID": pokemon.entity_id,
            "abilityID": ability.ability_id,
            "abilityTitle": {"id": ability.title},
            "abilityType": "PokeAbility",
        },
    )
    tail = session._build_msg(
        OutboundMsg.ABILITY_FINISHED_EFFECT.value,
        {"gameID": session.game_id, "eID": pokemon.entity_id},
    )
    extra: List[Dict[str, Any]] = []
    if ability.vstar:
        # Flips the user's playmat VSTAR marker face-down (handler P.Y).
        extra.append(session._build_msg(
            OutboundMsg.VSTAR_POWER_USED_EFFECT.value,
            {"gameID": session.game_id, "user": ctx.player_id},
        ))

    if not ctx._messages:
        # Declined/no-op effect: announce only (popin + gamelog, no orb).
        if not ctx.suppress_announce:
            for pid, viewer in session.players.items():
                await session.send_game_sequence(
                    [viewer], GameSequence.POKE_ABILITY, [head] + extra + [tail]
                )
        # A message-less effect can still grant a bench-capacity passive.
        await session.enforce_bench_capacity()
        return

    # The Attack executor dereferences the playmat's attack-source [0].
    await session._broadcast_attack_sources([pokemon.entity_id])
    # Out-of-zone sources (usable_from hand/discard) default the orb to the
    # source's PILE rather than the card itself.
    fallback = [pokemon.entity_id]
    parent = getattr(pokemon, "parent", None)
    if parent is not None \
            and parent.get_attribute(AttrID.NAME) in ("hand", "discard"):
        fallback = [parent.entity_id]
    orb = session._build_msg(
        OutboundMsg.NON_DAMAGING_TARGETS_EFFECT.value,
        {
            "gameID": session.game_id,
            # Never empty: M.N only injects the r.u orb group when targets
            # exist, and ONLY r.u clears opponentTargetSelectArea -- an empty
            # list leaves the source floating on the opposing client.
            "targets": ctx.visual_targets or ctx._visual_sources
                       or fallback,
        },
    )
    for pid, viewer in session.players.items():
        await session.send_game_sequence(
            [viewer], GameSequence.ATTACK, [head] + extra + [orb, tail]
        )
    # Effect messages flush as their queued bracket runs (attach_energy's
    # SerialSequence intro must precede its GroupedMove so the wrap sees the
    # card's type and plays the attach FX); plain messages default into a
    # PokeAbility bracket. The r.u orb in the Attack bracket already tucked
    # the pulled-out source home on both viewers.
    for pid, viewer in session.players.items():
        for name, msgs in ctx.bracket_runs_for(pid, GameSequence.POKE_ABILITY.value):
            if msgs:
                await session.send_game_sequence([viewer], name, msgs)
    await session.resolve_knockouts(ctx, _ko_depth=_ko_depth)
    for hook in ctx.deferred_actions:
        await hook()
    await session.enforce_bench_capacity()


async def resolve_trainer_effect(session, player_id: str, card) -> Optional[EffectContext]:
    """Runs a trainer card's scripted effect and returns its ctx (None when
    the card has no runnable effect).

    Dialog primitives (ctx.choose/ask_yes_no/choosers) interact with the
    player here, before any choreography is sent; the caller flushes
    ctx.bracket_runs_for into brackets afterwards.
    """
    # Shifty Substitution: a passive may replace a Supporter's effect wholesale
    # (consulted BEFORE the effect registry -- unscripted cards replace too).
    if card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value:
        replacement = supporter_effect_replacement(
            session.board_state, card, player_id)
        if replacement is not None:
            ctx = EffectContext(session, player_id, card, None)
            ctx.is_trainer_effect = True
            await replacement(ctx)
            return ctx
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    if effect is None or effect is unimplemented:
        logging.warning(
            f"[Effects {session.game_id}] Trainer {card.entity_id} "
            f"({card.archetype_id}) has "
            + ("unimplemented effect text" if effect is unimplemented
               else "no scripted effect")
            + "; card plays with no effect."
        )
        return None
    ctx = EffectContext(session, player_id, card, None)
    ctx.is_trainer_effect = True
    await effect(ctx)
    return ctx


async def resolve_energy_attach_cost(session, player_id: str, energy: EnergyEntity,
                                     target: PokemonEntity) -> Optional[EffectContext]:
    """Runs an energy's attach_cost hook (e.g. Aurora Energy's discard).

    Returns the ctx to flush when the cost was paid, or None to cancel the
    attach entirely.
    """
    definition = def_for(energy.archetype_id)
    cost = getattr(definition, "attach_cost", None)
    if cost is None:
        return EffectContext(session, player_id, energy, None, attached_to=target)
    ctx = EffectContext(session, player_id, energy, None, attached_to=target)
    paid = await cost(ctx)
    return ctx if paid else None


async def resolve_energy_on_attach(session, player_id: str, energy: EnergyEntity,
                                   target: PokemonEntity) -> Optional[EffectContext]:
    """Runs an energy's on_attach hook after it attached from hand."""
    definition = def_for(energy.archetype_id)
    hook = getattr(definition, "on_attach", None)
    if hook is None or hook is unimplemented:
        return None
    ctx = EffectContext(session, player_id, energy, None, attached_to=target)
    await hook(ctx)
    return ctx


async def _send_attack_bracket(session, ctx: AttackContext, action_id: str, title: str):
    """One Attack bracket per viewer: begin marker, effect messages, end marker."""
    # AbilityPlayedEffect uses the client's AbilityType enum (Attack/PokeAbility),
    # not the PIE_ABILITIES hint enum; send the member name string.
    ability_type = "PokeAbility" \
        if ctx.ability and ctx.ability.ability_type == AbilityTypes.POKE_ABILITY \
        else "Attack"
    head = session._build_msg(
        OutboundMsg.ABILITY_PLAYED_EFFECT.value,
        {
            "gameID": session.game_id,
            "eID": ctx.attacker.entity_id,
            "abilityID": action_id,
            "abilityTitle": {"id": title},
            "abilityType": ability_type,
        },
    )
    tail = session._build_msg(
        OutboundMsg.ABILITY_FINISHED_EFFECT.value,
        {"gameID": session.game_id, "eID": ctx.attacker.entity_id},
    )
    extra: List[Dict[str, Any]] = []
    if ctx.ability is not None and ctx.ability.vstar:
        extra.append(session._build_msg(
            OutboundMsg.VSTAR_POWER_USED_EFFECT.value,
            {"gameID": session.game_id, "user": ctx.player_id},
        ))
    # The Attack executor dereferences the playmat's attack-source [0].
    await session._broadcast_attack_sources([ctx.attacker.entity_id])
    # Non-damaging attacks (Read the Wind) need the r.u orb: with no damaging
    # CakeAttackEffect, M.N injects it from the NonDamagingTargetsEffect's
    # targets, and ONLY the orb clears the pulled-out attacker on both
    # viewers. Damaging attacks get the lunge group instead -- an orb there
    # would double up (S.j forces the non-damaging path).
    if not ctx._dealt_opponent_damage:
        targets = (ctx.visual_targets or ctx._visual_sources
                   or [k.entity_id for k in ctx.knockouts]
                   or [ctx.attacker.entity_id])
        extra.append(session._build_msg(
            OutboundMsg.NON_DAMAGING_TARGETS_EFFECT.value,
            {"gameID": session.game_id, "targets": targets},
        ))
    # Tuck the attacker's pulled-back ability panel home first; the executor
    # no-ops when no panel is up, so its bracket may be empty.
    attacker_viewer = session.players.get(ctx.player_id)
    if attacker_viewer is not None:
        await session.send_game_sequence(
            [attacker_viewer], GameSequence.DISMISS_ABILITY_SELECT, []
        )
    for pid, viewer in session.players.items():
        # Only untagged messages (CakeAttackEffect, HP mods) ride inside the
        # Attack bracket; tagged runs flush as their own top-level brackets
        # AFTER it, in queue order -- M.N never WrapSequences, so an inlined
        # deck->Pokemon attach ran raw (energies teleported) and inlined
        # Retreat/condition runs lost their executors' choreography.
        inline: List[Dict[str, Any]] = []
        post_runs: List[Tuple[str, List[Dict[str, Any]]]] = []
        for name, msgs in ctx.bracket_runs_for(pid, GameSequence.ATTACK.value):
            if name == GameSequence.ATTACK.value:
                inline.extend(msgs)
            else:
                post_runs.append((name, msgs))
        await session.send_game_sequence(
            [viewer], GameSequence.ATTACK, [head] + extra + inline + [tail],
        )
        for name, msgs in post_runs:
            if msgs:
                await session.send_game_sequence([viewer], name, msgs)
