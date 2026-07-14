"""Continuous (passive) card effects.

A Passive is contributed by a card while it is in play: a Pokemon ability
(Ability(passive=...)), an attached Pokemon Tool, or an attached Special
Energy (both via their CardDefinition's passive=). The engine collects the
active (passive, carrier) pairs each time it computes damage, attack costs,
or max HP, so effects switch on/off purely by board position.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from spirit.game.attributes import AttrID, PokemonTypes, TrainerType
from spirit.game.data_utils import ABILITIES_BY_ID, def_for, subtypes_for
from spirit.game.models.board import (
    BENCH_SLOT_COUNT,
    BoardEntity,
    BoardState,
    CardEntity,
    PokemonEntity,
)

WEAKNESS_MULTIPLIER = 2
RESISTANCE_REDUCTION = 30

# Areas whose top-level cards keep a temporary passive alive.
_IN_PLAY_AREAS = ("activePokemonArea", "bench", "activeStadium")


@dataclass
class TurnDamageModifier:
    """A turn-scoped attacker-side damage boost (Power Tablet: "+30 damage
    during this turn to your Fusion Strike Pokemon's attacks")."""
    amount: int
    player_id: str
    requires_subtype: Optional[str] = None
    opposing_active_only: bool = True
    # None = this turn only; otherwise the last turn number it still applies.
    expires_after_turn: Optional[int] = None
    # Only while THIS entity attacks (Scyther's next-turn self boost).
    source_entity_id: Optional[str] = None
    # Only while resolving this attack title (Metagross' Fullmetal Impact rider).
    attack_title: Optional[str] = None
    # Arbitrary attacker gate (Ludicolo/Rapidash predicates).
    source_predicate: Optional[Callable[[BoardEntity], bool]] = None


@dataclass
class TempPassive:
    """An effect-granted passive with a lifetime. expires_after_turn None =
    until the carrier leaves the Active spot / play (clear_pokemon_effects)."""
    passive: "Passive"
    carrier_entity_id: str
    expires_after_turn: Optional[int] = None


class DamageCalc:
    """One damage computation, mutated in stages by the passive hooks."""

    def __init__(
        self,
        board: BoardState,
        attacker: Optional[BoardEntity],
        target: PokemonEntity,
        base: int,
        is_attack: bool = True,
        apply_modifiers: bool = True,
        ignore_target_effects: bool = False,
        attack_title: Optional[str] = None,
    ):
        self.board = board
        self.attacker = attacker
        self.target = target
        self.base = base
        self.amount = base
        # True for attack damage; False for ability/effect damage.
        self.is_attack = is_attack
        # Weakness/Resistance stage runs only versus the defending Active.
        self.apply_modifiers = apply_modifiers
        # Title of the attack being resolved (matches TurnDamageModifier riders).
        self.attack_title = attack_title
        self.weakness_applies = True
        self.weakness_multiplier = WEAKNESS_MULTIPLIER
        # Rewritable by modify_weakness hooks (Spiritomb/UnownVSTAR overrides).
        self.weak_types: List[Any] = list(
            target.get_attribute(AttrID.WEAKNESS_TYPES) or []
        )
        self.resistance_applies = True
        self.weakness_hit = False
        self.resistance_hit = False
        self.prevented = False
        # Max Miracle-style: skip passives riding the DEFENDING Pokemon in the
        # taken/prevention stages (attacker-side and third-party still run).
        self.ignore_target_effects = ignore_target_effects
        # Scratch set for non-stacking effects (e.g. Lesson in Zeal) to mark
        # themselves applied and skip on a later pass within the same calc.
        self.applied_once: Set[str] = set()

    @property
    def to_active(self) -> bool:
        """Whether the target sits in its owner's Active spot."""
        parent = self.target.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"

    @property
    def is_opposing(self) -> bool:
        """Whether attacker and target belong to different players."""
        return (
            self.attacker is not None
            and self.attacker.owning_player_id != self.target.owning_player_id
        )


class Passive:
    """Override only the hooks a card's continuous effect needs.

    `carrier` is the entity contributing the passive: the Pokemon whose
    ability it is, or the attached tool/energy card (carrier_pokemon gives
    the Pokemon an attachment rides on).
    """

    # Same-key passives count once in effective_max_hp (Abomasnow stacks).
    stacking_key: Optional[str] = None

    # Optional awaitable damage stage: async (ctx, calc, target, carrier) ->
    # Optional[int], consulted in ctx.deal_damage AFTER compute_damage and
    # BEFORE the HP write (None = unchanged, else the new dealt amount).
    # Flip-to-prevent (Infiltrator) and KO-survive (Guts) live here; may queue
    # coin flips via ctx so they choreograph inside the attack bracket.
    damage_interceptor: Optional[Any] = None

    # Optional awaitable post-attack stage: async (ctx, carrier) -> None, run
    # by resolve_attack AFTER knockouts/deferred actions resolve (end-of-turn
    # riders like Blunder Policy); queued messages flush as their own brackets.
    attack_followup: Optional[Any] = None

    def modify_damage_dealt(self, calc: DamageCalc, carrier: BoardEntity):
        """Attacker-side "does more/less damage" step (runs before W/R)."""

    def modify_weakness(self, calc: DamageCalc, carrier: BoardEntity):
        """May clear calc.weakness_applies (e.g. "... have no Weakness"), or
        rewrite calc.weak_types / calc.weakness_multiplier."""

    def modify_resistance(self, calc: DamageCalc, carrier: BoardEntity):
        """May clear calc.resistance_applies ("... has no Resistance")."""

    def modify_damage_taken(self, calc: DamageCalc, carrier: BoardEntity):
        """Defender-side "takes less damage" step (runs after W/R)."""

    def prevents_damage(self, calc: DamageCalc, carrier: BoardEntity) -> bool:
        """True to prevent the hit entirely (calc.amount becomes 0)."""
        return False

    def modify_attack_cost(
        self,
        cost: Dict[str, int],
        pokemon: PokemonEntity,
        carrier: BoardEntity,
        board: BoardState,
    ) -> Dict[str, int]:
        """Returns the (possibly reduced) cost dict, client-name keyed."""
        return cost

    def max_hp_bonus(self, pokemon: PokemonEntity, carrier: BoardEntity) -> int:
        """Extra max HP granted to `pokemon` (e.g. Heat Fire Energy's +20)."""
        return 0

    def modify_retreat_cost(
        self, cost: int, pokemon: PokemonEntity, carrier: BoardEntity,
        board: BoardState,
    ) -> int:
        """Returns the (possibly reduced) retreat cost (Air Balloon's -2);
        `board` lets stadium-gated hooks read global state (Thwackey)."""
        return cost

    def blocks_attack_effects(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to shield `target` from opponents' attack EFFECTS (not damage)."""
        return False

    def blocks_abilities(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to turn off `pokemon`'s Abilities (Path to the Peak style)."""
        return False

    def blocks_retreat(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to forbid `pokemon` from retreating (Octolock, Flygon)."""
        return False

    def attacks_despite_conditions(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to let `pokemon` attack even while Asleep/Paralyzed (Windup Arm)."""
        return False

    def blocks_special_conditions(
        self, target: PokemonEntity, condition: Any, carrier: BoardEntity
    ) -> bool:
        """True to shield `target` from having `condition` applied to it."""
        return False

    def prevents_healing(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to prevent healing damage from `target` (Mimikyu SWSH3)."""
        return False

    def knockout_destination(self, pokemon: PokemonEntity, carrier: BoardEntity) -> Optional[str]:
        """Area name replacing "discard" for a knocked-out Pokemon (e.g. "lostZone")."""
        return None

    def modify_prizes_for_knockout(
        self, pokemon: PokemonEntity, ctx: Any, count: int, carrier: BoardEntity
    ) -> int:
        """Prize count the opponent takes for knocking out `pokemon` (Komala);
        evaluated BEFORE the stack moves, so board/conditions still count."""
        return count

    def prize_destination(
        self, pokemon: PokemonEntity, ctx: Any, carrier: BoardEntity
    ) -> Optional[str]:
        """Area name replacing "hand" for the prizes taken for this knockout
        ("discard" = Billowing Smoke, "lostZone" = Barbaracle)."""
        return None

    def modify_energy_provided(
        self, options: List[List[int]], energy: BoardEntity,
        holder: Optional[PokemonEntity], board: BoardState,
    ) -> List[List[int]]:
        """Rewrites an energy's provided-type options (Charizard PGO doubling)."""
        return options

    def modify_pokemon_types(
        self, types: List[Any], pokemon: BoardEntity, carrier: BoardEntity
    ) -> List[Any]:
        """Rewrites `pokemon`'s live type list (Kecleon's Chromashift)."""
        return types

    def blocks_energy_removal(
        self, energy: BoardEntity, mover_player_id: str, carrier: BoardEntity
    ) -> bool:
        """True to keep an attached Energy from being moved to hand/deck/
        discard by `mover_player_id`'s Item/Supporter effect (Brazen Tail)."""
        return False

    def suppresses_special_energy(self, energy: BoardEntity, carrier: BoardEntity) -> bool:
        """True to neutralize a Special Energy (Temple of Sinnoh): it loses
        its passive and provides only Colorless."""
        return False

    def suppresses_tool(self, tool: BoardEntity, carrier: BoardEntity) -> bool:
        """True to neutralize an attached Pokemon Tool's passive hooks
        (Tool Jammer); evaluated on the unfiltered set like ability locks."""
        return False

    def granted_attacks(
        self, board: BoardState, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> List[Any]:
        """Extra Attack definitions `pokemon` may use (Ditto's Sudden
        Transformation, Memory Capsule); costs/locks still apply normally."""
        return []

    def blocks_trainer_play(
        self, card: BoardEntity, player_id: str, carrier: BoardEntity
    ) -> bool:
        """True to forbid `player_id` playing `card` from hand (Vileplume)."""
        return False

    def may_evolve_early(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to exempt `pokemon` from the just-played/first-turn evolution
        gates (Caterpie's Adaptive Evolution)."""
        return False

    def blocks_evolution(
        self, player_id: str, target: PokemonEntity, carrier: BoardEntity
    ) -> bool:
        """True to forbid `player_id` evolving `target` at all (Dracovish)."""
        return False

    def modify_burn_counters(
        self, counters: int, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Damage counters the Burn checkup tick places (default 2)."""
        return counters

    def blocks_burn_recovery(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to skip the Burn recovery flip entirely (stays Burned)."""
        return False

    def tool_capacity(self, pokemon: PokemonEntity, carrier: BoardEntity) -> int:
        """Pokemon Tools `pokemon` may hold (GarbodorVMAX 2); highest wins."""
        return 1

    def bench_capacity(self, player_id: str, carrier: BoardEntity) -> Optional[int]:
        """Bench size override for `player_id` (Collapsed Stadium 4); None =
        no opinion, the smallest override wins."""
        return None

    def attack_keeps_turn(self, attacker: PokemonEntity, ability: Any,
                          ctx: Any, carrier: BoardEntity) -> bool:
        """True to keep the turn going after `attacker`'s attack resolved
        (Fluffy Barrage); runs after knockouts resolve, so KO evidence rides
        ctx.knockouts_resolved, not ctx.knockouts."""
        return False

    def blocks_ability_effects(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to shield `target` from opponents' Ability effects (Corviknight VMAX)."""
        return False

    def blocks_discard(self, card: BoardEntity, carrier: BoardEntity) -> bool:
        """True to keep `card` from being discarded by an opponent's effect."""
        return False

    def blocks_trainer_effects(
        self, affected_player_id: str, trainer_card: BoardEntity,
        trainer_type: Any, carrier: BoardEntity,
        affected_entity: Optional[BoardEntity] = None,
        board: Optional["BoardState"] = None,
    ) -> bool:
        """True to shield `affected_player_id`'s side from an opposing trainer
        card's effects (Dew Guard); trainer_type is the TrainerType value.
        affected_entity is the primitive's direct object (None for
        player-level effects like draws/hand shuffles)."""
        return False

    def replace_supporter_effect(
        self, card: BoardEntity, player_id: str, carrier: BoardEntity
    ) -> Optional[Any]:
        """Replacement effect coroutine for `player_id`'s Supporter `card`
        (Shifty Substitution); None = no replacement."""
        return None

    def taxes_energy_attach(
        self, attaching_player_id: str, energy: BoardEntity,
        target: PokemonEntity, carrier: BoardEntity,
    ) -> bool:
        """True to coin-flip `attaching_player_id`'s manual energy attach
        (Slimy Room): tails discards the energy instead of attaching."""
        return False

    def retreat_cost_destination(
        self, pokemon: PokemonEntity, energy: BoardEntity, carrier: BoardEntity
    ) -> Optional[str]:
        """Player-area name replacing "discard" for `energy` paid for
        `pokemon`'s retreat (Skaters' Park sends basic Energy to "hand")."""
        return None

    def counters_on_active_to_bench(
        self, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Damage counters put on an Active that moved to its owner's Bench
        during that owner's turn (Spikemuth)."""
        return 0

    def heal_on_evolve(
        self, evolved: PokemonEntity, pre_evolution: BoardEntity,
        player_id: str, carrier: BoardEntity,
    ) -> int:
        """Damage healed from a Pokemon `player_id` just evolved from hand
        (Wyndon Stadium)."""
        return 0

    def offers_attack_coin_reroll(self, player_id: str, carrier: BoardEntity) -> bool:
        """True to let `player_id` re-flip an attack's coins once during
        their turn (Glimwood Tangle)."""
        return False


def carrier_pokemon(carrier: BoardEntity) -> Optional[PokemonEntity]:
    """The in-play Pokemon a passive rides: the carrier itself, or the
    top-level Pokemon its attachment stack hangs under."""
    entity = carrier
    while entity is not None:
        parent = entity.parent
        if isinstance(entity, PokemonEntity) and not isinstance(parent, CardEntity):
            return entity
        entity = parent if isinstance(parent, CardEntity) else None
    return None


def _collect_passives(board: BoardState) -> List[Tuple[Passive, BoardEntity, bool]]:
    """All (passive, carrier, is_ability) triples currently switched on by
    board position, before ability locks are applied. is_ability is True only
    for passives contributed by a Pokemon's own PIE_ABILITIES entry."""
    triples: List[Tuple[Passive, BoardEntity, bool]] = []
    for player_id in board.player_ids:
        for pokemon in board.pokemon_in_play(player_id):
            # Card-level PokemonCardDef(passive=): rules text that is not an
            # Ability, so ability locks never switch it off.
            card_passive = getattr(def_for(pokemon.archetype_id), "passive", None)
            if card_passive is not None:
                triples.append((card_passive, pokemon, False))
            for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
                if not isinstance(entry, dict):
                    continue
                ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
                if ability is not None and ability.passive is not None:
                    # A Tool-granted ability's passive rides the tool, not the
                    # Pokemon, so Path to the Peak can't switch it off.
                    triples.append((ability.passive, pokemon, not ability.is_granted))
            for attachment in _descendants(pokemon):
                if isinstance(attachment, PokemonEntity):
                    continue  # tucked pre-evolutions contribute nothing
                definition = def_for(attachment.archetype_id)
                passive = getattr(definition, "passive", None)
                if passive is not None:
                    triples.append((passive, attachment, False))
    stadium_area = board.find_global_area("activeStadium")
    for stadium in (stadium_area.children if stadium_area else []):
        definition = def_for(stadium.archetype_id)
        passive = getattr(definition, "passive", None)
        if passive is not None:
            triples.append((passive, stadium, False))
    # Effect-granted temporary passives; dead carriers are silently skipped.
    for temp in getattr(board, "temporary_passives", None) or []:
        carrier = board.get_entity(temp.carrier_entity_id)
        if carrier is None or not _carrier_in_play(carrier):
            continue
        triples.append((temp.passive, carrier, False))
    return triples


def _carrier_in_play(entity: BoardEntity) -> bool:
    """Whether an entity (or the stack it is attached under) sits in play."""
    node = entity
    while isinstance(getattr(node, "parent", None), CardEntity):
        node = node.parent
    parent = getattr(node, "parent", None)
    return parent is not None \
        and parent.get_attribute(AttrID.NAME) in _IN_PLAY_AREAS


def ability_locked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive (Path to the Peak) is disabling `pokemon`'s Abilities.

    Evaluated on the UNFILTERED set: a lock contributed by a Pokemon ability
    is never itself disabled by another lock (Garbotoxin-style recursion is
    out of scope -- Path to the Peak rides a Stadium so this is safe).
    """
    return any(p.blocks_abilities(pokemon, c) for p, c, _ in _collect_passives(board))


def _suppressed_special_energy(
    triples: List[Tuple[Passive, BoardEntity, bool]], entity: BoardEntity
) -> bool:
    """Whether `entity` is a Special Energy neutralized by a suppression
    passive (evaluated on the UNFILTERED set, like ability locks)."""
    if not entity.get_attribute(AttrID.IS_SPECIAL_ENERGY):
        return False
    return any(p.suppresses_special_energy(entity, c) for p, c, _ in triples)


def _suppressed_tool(
    triples: List[Tuple[Passive, BoardEntity, bool]], entity: BoardEntity
) -> bool:
    """Whether `entity` is an attached Pokemon Tool neutralized by a
    suppression passive (Tool Jammer), evaluated on the UNFILTERED set."""
    if entity.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.POKEMON_TOOL.value:
        return False
    return any(p.suppresses_tool(entity, c) for p, c, _ in triples)


def active_passives(board: BoardState) -> List[Tuple[Passive, BoardEntity]]:
    """All (passive, carrier) pairs currently switched on by board position.

    Ability passives count only for top-level in-play Pokemon (a tucked
    pre-evolution's ability is off); tool/energy/stadium passives count
    anywhere in an in-play stack. Ability-contributed passives on a Pokemon
    whose own Abilities are locked (Path to the Peak) are excluded, as are
    passives riding a suppressed Special Energy (Temple of Sinnoh).
    """
    triples = _collect_passives(board)

    def blocked(pokemon: PokemonEntity) -> bool:
        return any(p.blocks_abilities(pokemon, c) for p, c, _ in triples)

    return [(p, c) for p, c, is_ability in triples
            if not (is_ability and blocked(c))
            and not _suppressed_special_energy(triples, c)
            and not _suppressed_tool(triples, c)]


def tool_suppressed(board: BoardState, tool: BoardEntity) -> bool:
    """Whether an attached Tool is neutralized (Tool Jammer): gates its
    granted_abilities in PIE_ABILITIES, not just its passive hooks."""
    return _suppressed_tool(_collect_passives(board), tool)


def granted_extra_attacks(board: BoardState, pokemon: PokemonEntity) -> List[Any]:
    """All passive-granted extra attacks for `pokemon`, deduped by ability_id."""
    out: List[Any] = []
    seen = set()
    for passive, carrier in active_passives(board):
        for attack in passive.granted_attacks(board, pokemon, carrier) or []:
            if attack.ability_id and attack.ability_id not in seen:
                seen.add(attack.ability_id)
                out.append(attack)
    return out


def _descendants(entity: BoardEntity) -> List[BoardEntity]:
    out: List[BoardEntity] = []
    for child in entity.children:
        out.append(child)
        out.extend(_descendants(child))
    return out


def compute_damage(
    board: BoardState,
    attacker: Optional[BoardEntity],
    target: PokemonEntity,
    base: int,
    is_attack: bool = True,
    apply_modifiers: bool = True,
    ignore_target_effects: bool = False,
    ignore_weakness: bool = False,
    ignore_resistance: bool = False,
    attack_title: Optional[str] = None,
) -> DamageCalc:
    """Runs the full damage pipeline: dealt-modifiers, W/R, taken-modifiers,
    prevention. Returns the finished DamageCalc.

    ignore_weakness (Cramorant's Spit Innocently) skips the Weakness stage but
    keeps Resistance -- distinct from apply_modifiers, which gates both;
    ignore_resistance (Gallade V's Buster Swing) is the exact mirror.
    """
    calc = DamageCalc(board, attacker, target, base,
                      is_attack=is_attack, apply_modifiers=apply_modifiers,
                      ignore_target_effects=ignore_target_effects,
                      attack_title=attack_title)
    if ignore_weakness:
        calc.weakness_applies = False
    if ignore_resistance:
        calc.resistance_applies = False
    passives = active_passives(board)

    if calc.is_attack:
        for passive, carrier in passives:
            passive.modify_damage_dealt(calc, carrier)
        calc.amount = max(0, calc.amount)
        turn_state = getattr(board, "turn_state", None)
        for mod in (turn_state.damage_modifiers if turn_state else []):
            if attacker is None or attacker.owning_player_id != mod.player_id:
                continue
            if mod.requires_subtype and mod.requires_subtype not in subtypes_for(attacker.archetype_id):
                continue
            if mod.source_entity_id and attacker.entity_id != mod.source_entity_id:
                continue
            if mod.attack_title and calc.attack_title != mod.attack_title:
                continue
            if mod.source_predicate is not None and not mod.source_predicate(attacker):
                continue
            if mod.opposing_active_only and not (calc.is_opposing and calc.to_active):
                continue
            calc.amount += mod.amount
        calc.amount = max(0, calc.amount)

    if calc.apply_modifiers and attacker is not None:
        for passive, carrier in passives:
            passive.modify_weakness(calc, carrier)
            passive.modify_resistance(calc, carrier)
        attacker_types = list(attacker.get_attribute(AttrID.POKEMON_TYPES) or [])
        for passive, carrier in passives:
            attacker_types = passive.modify_pokemon_types(attacker_types, attacker, carrier)
        if calc.weakness_applies and any(t in calc.weak_types for t in attacker_types):
            calc.weakness_hit = True
            calc.amount *= calc.weakness_multiplier
        resist_type = target.get_attribute(AttrID.RESISTANCE_TYPES)
        if calc.resistance_applies and resist_type in attacker_types:
            calc.resistance_hit = True
            calc.amount = max(0, calc.amount - RESISTANCE_REDUCTION)

    for passive, carrier in passives:
        if calc.ignore_target_effects and carrier_pokemon(carrier) is calc.target:
            continue
        passive.modify_damage_taken(calc, carrier)
    calc.amount = max(0, calc.amount)

    for passive, carrier in passives:
        if calc.ignore_target_effects and carrier_pokemon(carrier) is calc.target:
            continue
        if passive.prevents_damage(calc, carrier):
            calc.prevented = True
            calc.amount = 0
            break
    return calc


def effective_attack_cost(
    board: BoardState, pokemon: PokemonEntity, cost: Dict[str, int]
) -> Dict[str, int]:
    """An attack's cost after cost-modifying passives (e.g. Excited Heart)."""
    for passive, carrier in active_passives(board):
        cost = passive.modify_attack_cost(dict(cost), pokemon, carrier, board)
    return cost


def effective_retreat_cost(board: BoardState, pokemon: PokemonEntity) -> int:
    """A Pokemon's retreat cost after cost-modifying passives (Air Balloon's -2)."""
    cost = int(pokemon.get_attribute(AttrID.RETREAT_COST) or 0)
    for passive, carrier in active_passives(board):
        cost = passive.modify_retreat_cost(cost, pokemon, carrier, board)
    return max(0, cost)


def effective_max_hp(board: BoardState, pokemon: PokemonEntity) -> int:
    """Printed max HP plus every max-HP bonus riding the Pokemon's stack;
    passives sharing a stacking_key count once (Abomasnow)."""
    printed = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
    )
    bonus = 0
    seen_keys: Set[str] = set()
    for passive, carrier in active_passives(board):
        key = passive.stacking_key
        if key is not None and key in seen_keys:
            continue
        gained = passive.max_hp_bonus(pokemon, carrier)
        if gained and key is not None:
            seen_keys.add(key)
        bonus += gained
    return printed + bonus


def attack_effects_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive shields `target` from opposing attack effects."""
    return any(
        passive.blocks_attack_effects(target, carrier)
        for passive, carrier in active_passives(board)
    )


def retreat_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive forbids `pokemon` from retreating."""
    return any(
        passive.blocks_retreat(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def can_attack_despite_conditions(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive lets `pokemon` attack while Asleep/Paralyzed."""
    return any(
        passive.attacks_despite_conditions(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def conditions_blocked(board: BoardState, target: PokemonEntity, condition: Any) -> bool:
    """Whether a passive shields `target` from the given Special Condition."""
    return any(
        passive.blocks_special_conditions(target, condition, carrier)
        for passive, carrier in active_passives(board)
    )


def healing_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive prevents healing damage from `target`."""
    return any(
        passive.prevents_healing(target, carrier)
        for passive, carrier in active_passives(board)
    )


def ability_effects_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive shields `target` from opposing Ability effects."""
    return any(
        passive.blocks_ability_effects(target, carrier)
        for passive, carrier in active_passives(board)
    )


def trainer_play_blocked(board: BoardState, player_id: str, card: BoardEntity) -> bool:
    """Whether a continuous passive forbids playing `card` from hand."""
    return any(
        passive.blocks_trainer_play(card, player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def discard_blocked(board: BoardState, card: BoardEntity) -> bool:
    """Whether a passive protects `card` from an opponent-caused discard."""
    return any(
        passive.blocks_discard(card, carrier)
        for passive, carrier in active_passives(board)
    )


def trainer_effects_blocked(board: BoardState, affected_player_id: str,
                            trainer_card: BoardEntity,
                            affected_entity: Optional[BoardEntity] = None) -> bool:
    """Whether a passive shields `affected_player_id` from `trainer_card`'s
    effects (Dew Guard); callers scope this to cross-player effects."""
    trainer_type = trainer_card.get_attribute(AttrID.TRAINER_TYPE)
    return any(
        passive.blocks_trainer_effects(
            affected_player_id, trainer_card, trainer_type, carrier,
            affected_entity=affected_entity, board=board)
        for passive, carrier in active_passives(board)
    )


def supporter_effect_replacement(board: BoardState, card: BoardEntity,
                                 player_id: str) -> Optional[Any]:
    """First replacement coroutine a passive offers for this Supporter play
    (Shifty Substitution), or None."""
    for passive, carrier in active_passives(board):
        replacement = passive.replace_supporter_effect(card, player_id, carrier)
        if replacement is not None:
            return replacement
    return None


def active_to_bench_counters(board: BoardState, pokemon: PokemonEntity) -> int:
    """Damage counters for an Active that moved to its owner's Bench during
    the owner's turn (Spikemuth); callers gate on whose turn it is."""
    return sum(
        passive.counters_on_active_to_bench(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def evolve_heal_amount(board: BoardState, evolved: PokemonEntity,
                       pre_evolution: BoardEntity, player_id: str) -> int:
    """Damage healed from a Pokemon just evolved from hand (Wyndon Stadium)."""
    return sum(
        passive.heal_on_evolve(evolved, pre_evolution, player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def attack_coin_reroll_offered(board: BoardState, player_id: str) -> bool:
    """Whether a passive lets `player_id` re-flip attack coins (Glimwood Tangle)."""
    return any(
        passive.offers_attack_coin_reroll(player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def energy_attach_taxer(board: BoardState, attaching_player_id: str,
                        energy: BoardEntity, target: PokemonEntity) -> Optional[BoardEntity]:
    """The carrier taxing this manual energy attach (Slimy Room), or None."""
    for passive, carrier in active_passives(board):
        if passive.taxes_energy_attach(attaching_player_id, energy, target, carrier):
            return carrier
    return None


def retreat_energy_destination(board: BoardState, pokemon: PokemonEntity,
                               energy: BoardEntity) -> Optional[str]:
    """First non-None area a passive redirects a retreat-cost energy to
    (Skaters' Park), or None for the normal discard."""
    for passive, carrier in active_passives(board):
        dest = passive.retreat_cost_destination(pokemon, energy, carrier)
        if dest is not None:
            return dest
    return None


def evolution_blocked(board: BoardState, player_id: str, target: PokemonEntity) -> bool:
    """Whether a passive forbids `player_id` evolving `target` (Dracovish)."""
    return any(
        passive.blocks_evolution(player_id, target, carrier)
        for passive, carrier in active_passives(board)
    )


def can_evolve_early(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive exempts `pokemon` from the evolution turn gates."""
    return any(
        passive.may_evolve_early(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def burn_recovery_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive skips the Burn recovery flip for `pokemon`."""
    return any(
        passive.blocks_burn_recovery(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def special_energy_suppressed(board: BoardState, energy: BoardEntity) -> bool:
    """Whether `energy` is a Special Energy neutralized by a passive."""
    return _suppressed_special_energy(_collect_passives(board), energy)


def effective_pokemon_types(board: BoardState, pokemon: BoardEntity) -> List[Any]:
    """A Pokemon's live type list after type-rewriting passives (Chromashift)."""
    types = list(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
    for passive, carrier in active_passives(board):
        types = passive.modify_pokemon_types(types, pokemon, carrier)
    return types


def energy_removal_blocked(board: BoardState, mover_player_id: str,
                           card: BoardEntity) -> bool:
    """Whether a passive keeps this attached Energy from being moved to
    hand/deck/discard by `mover_player_id`'s trainer effect (Brazen Tail)."""
    return any(
        passive.blocks_energy_removal(card, mover_player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def energy_provided_options(board: Optional[BoardState], energy: BoardEntity) -> List[List[int]]:
    """An energy card's provided-type options after suppression (a suppressed
    Special Energy provides only Colorless) and modify_energy_provided hooks."""
    info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
    options = [list(option) for option in info.get("options", [])]
    if board is None:
        return options
    if special_energy_suppressed(board, energy):
        options = [[PokemonTypes.COLORLESS.value]]
    holder = carrier_pokemon(energy)
    for passive, carrier in active_passives(board):
        options = passive.modify_energy_provided(options, energy, holder, board)
    return options


def effective_bench_capacity(board: BoardState, player_id: str) -> int:
    """Bench size for `player_id` after capacity passives; the smallest
    override wins (Collapsed Stadium caps an Eternatus board at 4)."""
    values = [
        v for passive, carrier in active_passives(board)
        for v in [passive.bench_capacity(player_id, carrier)] if v is not None
    ]
    return max(1, min(values)) if values else BENCH_SLOT_COUNT


def tool_slots_free(board: Optional[BoardState], pokemon: PokemonEntity) -> int:
    """Open Pokemon Tool slots on `pokemon` (default capacity 1; the highest
    tool_capacity passive wins)."""
    capacity = 1
    if board is not None:
        for passive, carrier in active_passives(board):
            capacity = max(capacity, passive.tool_capacity(pokemon, carrier))
    attached = sum(
        1 for child in pokemon.children
        if child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
    )
    return capacity - attached
