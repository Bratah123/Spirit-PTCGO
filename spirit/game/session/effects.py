"""Card-effect execution engine.

Card scripts receive an EffectContext (`ctx`) and act through its primitives
(deal_damage, draw_cards, search_deck, switch_active, ...); every primitive
updates the server board state and queues the wire messages that ride the
play's sequence brackets. Interactive primitives (choosers, dialogs) resolve
inline before any choreography is flushed.
"""

import asyncio
import logging
import random
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, cast

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
    TRAINER_EFFECTS_BY_GUID,
    Ability,
    def_for,
    has_rule_box,
    unimplemented,
)
from spirit.game.models.board import BoardEntity, CardEntity, EnergyEntity, PokemonEntity
from spirit.network.message_names import OutboundMsg
from .constants import BENCH_CAPACITY, PROMPT_NO, PROMPT_YES
from .passives import (
    ability_locked,
    attack_effects_blocked,
    compute_damage,
    effective_max_hp,
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
        # Attack titles already resolving in this attack (copy-loop guard).
        self._copy_chain: List[str] = []
        self._messages: List[Tuple[Optional[str], Dict[str, Any], Optional[str]]] = []
        # Set by resolve_knockouts before firing an ON_KNOCKED_OUT trigger:
        # True iff the causing damage was an opposing Pokemon's attack.
        self.ko_from_attack: bool = False
        self.ko_attacker: Optional[PokemonEntity] = None

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

    def effects_blocked(self, target: PokemonEntity) -> bool:
        """Whether an opposing attack EFFECT on `target` is shielded (e.g.
        Unfazed Fat). Only attack effects against the other side count."""
        if not self.is_attack_effect() or target.owning_player_id == self.player_id:
            return False
        return attack_effects_blocked(self.board, target)

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
        as_counters: bool = False,
    ) -> int:
        """Damages a Pokemon (default: the attack's printed damage onto the
        opponent's Active) and returns the final amount after modifiers.

        Weakness/Resistance apply only to the opponent's Active by default
        (bench damage in the TCG is unmodified unless the card says otherwise).
        ignore_target_effects (Max Miracle) skips passives riding the target.
        ignore_weakness (Spit Innocently) skips only the Weakness stage.
        as_counters plays the counter-drop FX (PlaceDamageEffect, m.p) instead
        of the attack lunge (CakeAttackEffect) -- "put N damage counters"
        effects (Lost Mine, Glistening Droplets).
        """
        target = target if target is not None else self.defender
        if target is None:
            logging.warning(f"[Effects {self.game_id}] deal_damage with no target; skipped.")
            return 0
        base = amount if amount is not None else getattr(self.ability, "damage", 0)
        if base <= 0:
            return 0
        if apply_modifiers is None:
            apply_modifiers = target is self.opponent_active()
        if is_attack is None:
            is_attack = self.is_attack_effect()

        calc = compute_damage(
            self.board, self.attacker, target, base,
            is_attack=is_attack, apply_modifiers=apply_modifiers,
            ignore_target_effects=ignore_target_effects,
            ignore_weakness=ignore_weakness,
        )
        if calc.prevented:
            logging.info(
                f"[Effects {self.game_id}] Damage to {target.entity_id} "
                f"prevented by a passive effect."
            )
            return 0

        current = target.get_attribute(AttrID.HP, 0)
        remaining = max(0, current - calc.amount)
        target.set_attribute(AttrID.HP, remaining)

        # m.p/m.m both read current HP when they play, so the damage FX must
        # precede the HP AttributeModified for the knockout check to see
        # pre-hit HP.
        if as_counters:
            # PlaceDamageEffect (UNSET condition => generic counter-drop, not
            # the poison/burn overlay); leave _dealt_opponent_damage False so
            # the attacker tucks via the non-damaging orb aimed at the targets.
            self._queue(self.session._place_damage_effect_msg(
                target.entity_id, calc.amount))
            if target.entity_id not in self.visual_targets:
                self.visual_targets.append(target.entity_id)
        else:
            title = self.ability.title if self.ability else ""
            attacker_types = self.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
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
                    "damageAmount": calc.amount,
                    "damageModification": 0,
                    "visualType": VISUAL_DAMAGING,
                },
            ))
        if target.owning_player_id != self.attacker.owning_player_id:
            if not as_counters:
                self._dealt_opponent_damage = True
            self.session.stat_add(self.player_id, "damagedealt", calc.amount)
            self.session.credit_card_damage(self.player_id, self.attacker, calc.amount)
            if is_attack:
                self.session.stat_max(self.player_id, "biggestattack", calc.amount)
        self._queue_hp_update(target)

        if remaining <= 0 and target not in self.knockouts:
            self.knockouts.append(target)
        return calc.amount

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
        current = target.get_attribute(AttrID.HP, 0)
        healed = min(self.max_hp(target), current + amount) - current
        if healed <= 0:
            return 0
        target.set_attribute(AttrID.HP, current + healed)
        self.session.stat_add(self.player_id, "damagehealed", healed)
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
        if self.effects_blocked(target):
            logging.info(
                f"[Effects {self.game_id}] {condition.name} on {target.entity_id} "
                f"blocked by an effect shield."
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

    def add_turn_damage_modifier(self, mod) -> None:
        """Registers a TurnDamageModifier for the rest of the current turn."""
        self.session.turn_state.damage_modifiers.append(mod)

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

    async def flip_coins(self, count: int, title: str = "") -> List[bool]:
        """Flips `count` coins for a card effect ("Flip 2 coins..."); returns
        the results, True = heads."""
        if count <= 0:
            return []
        results = [random.choice([0, 1]) for _ in range(count)]
        heads = results.count(0)
        self.session.stat_add(self.player_id, "headsflipped", heads)
        self.session.stat_add(self.player_id, "tailsflipped", count - heads)
        msg = self.session._build_msg(
            OutboundMsg.MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT.value,
            {
                "gameID": self.game_id,
                "resultLst": results,
                "title": {"id": title or _display_name(self.source)},
                "gameText": {"id": f"{heads} heads"},
                "source": self.source.entity_id,
                "targets": [self.source.entity_id],
            },
        )
        if self.ability is not None:
            # Attack/PokeAbility brackets play the coin flip natively inline.
            self._queue(msg)
        else:
            # Trainer context: PokeAbility, NOT FlipToWakeUp -- d.s stamps the
            # "Asleep" pop-in (abilitypopin.asleep.label) onto every L.x it runs.
            await self.session.send_game_sequence(
                list(self.session.players.values()),
                GameSequence.POKE_ABILITY, [msg],
            )
            await asyncio.sleep(2.5)
        return [r == 0 for r in results]

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
                amount=counters * 10, target=by_id[entity_id],
                apply_modifiers=False, is_attack=False, as_counters=True,
            )

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

    async def move_to_lost_zone(self, cards: List[CardEntity]):
        """Moves cards to their owner's Lost Zone (a public zone)."""
        await self._move_to_public_pile(cards, "lostZone")

    async def _move_to_public_pile(self, cards: List[CardEntity], area_name: str):
        for card in cards:
            owner = card.owning_player_id or self.player_id
            pile = self.board.find_player_area(owner, area_name)
            if not pile:
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

    async def put_on_top_of_deck(self, card: CardEntity) -> bool:
        """Puts a card on top of its owner's deck."""
        owner = card.owning_player_id or self.player_id
        deck = self.board.find_player_area(owner, "deck")
        if not deck:
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
        if not deck:
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
        if not bench or len(bench.children) >= BENCH_CAPACITY:
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

    async def attach_energy(self, energy: CardEntity, pokemon: PokemonEntity) -> bool:
        """Attaches an energy card from any zone underneath a Pokemon
        (effect attachments don't consume the once-per-turn manual attach)."""
        if energy is None or pokemon is None:
            return False
        position = len(pokemon.children)
        if not self.board.attach_card(energy.entity_id, pokemon.entity_id):
            return False
        self._queue_intro_and_move(energy, pokemon.entity_id, position)
        return True

    async def switch_active(self, player_id: str, new_active: PokemonEntity) -> bool:
        """Swaps a player's Active with the given benched Pokemon (gust or
        self-switch). Special Conditions on the leaving Active are cured."""
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
        return True

    async def flush_choreography(self):
        """Sends and clears the currently queued choreography brackets, so a
        following dialog resolves only after both clients see them land
        (Escape Rope: the opponent's swap shows before the player decides)."""
        await self.session._flush_effect_runs(self)
        self._messages.clear()

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
    await session.resolve_knockouts(ctx)
    for hook in ctx.deferred_actions:
        await hook()


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
    await _send_ability_brackets(session, ctx, pokemon, ability, _ko_depth=_ko_depth)
    return ctx


# Card scripts/tests import the pre-generalization name; same function.
resolve_on_play_ability = resolve_triggered_ability


async def resolve_activated_ability(session, player_id: str, pokemon: PokemonEntity,
                                    ability: Ability):
    """Runs a player-activated ability (Activations.ONCE_PER_TURN / VSTAR).

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
    # Tuck the pulled-back ability panel home on the user's client.
    viewer = session.players.get(player_id)
    if viewer is not None:
        await session.send_game_sequence(
            [viewer], GameSequence.DISMISS_ABILITY_SELECT, []
        )
    await _send_ability_brackets(session, ctx, pokemon, ability)


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
        for pid, viewer in session.players.items():
            await session.send_game_sequence(
                [viewer], GameSequence.POKE_ABILITY, [head] + extra + [tail]
            )
        return

    # The Attack executor dereferences the playmat's attack-source [0].
    await session._broadcast_attack_sources([pokemon.entity_id])
    orb = session._build_msg(
        OutboundMsg.NON_DAMAGING_TARGETS_EFFECT.value,
        {
            "gameID": session.game_id,
            # Never empty: M.N only injects the r.u orb group when targets
            # exist, and ONLY r.u clears opponentTargetSelectArea -- an empty
            # list leaves the source floating on the opposing client.
            "targets": ctx.visual_targets or ctx._visual_sources
                       or [pokemon.entity_id],
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


async def resolve_trainer_effect(session, player_id: str, card) -> Optional[EffectContext]:
    """Runs a trainer card's scripted effect and returns its ctx (None when
    the card has no runnable effect).

    Dialog primitives (ctx.choose/ask_yes_no/choosers) interact with the
    player here, before any choreography is sent; the caller flushes
    ctx.bracket_runs_for into brackets afterwards.
    """
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
        # Draw runs flush as their own top-level Draw brackets after the
        # attack (m.c's flip fan only plays for brackets named "Draw");
        # everything else rides inside the Attack bracket as before.
        inline: List[Dict[str, Any]] = []
        draw_runs: List[List[Dict[str, Any]]] = []
        for name, msgs in ctx.bracket_runs_for(pid, GameSequence.ATTACK.value):
            if name == GameSequence.DRAW.value:
                draw_runs.append(msgs)
            else:
                inline.extend(msgs)
        await session.send_game_sequence(
            [viewer], GameSequence.ATTACK, [head] + extra + inline + [tail],
        )
        for msgs in draw_runs:
            await session.send_game_sequence([viewer], GameSequence.DRAW, msgs)
