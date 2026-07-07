"""Continuous (passive) card effects.

A Passive is contributed by a card while it is in play: a Pokemon ability
(Ability(passive=...)), an attached Pokemon Tool, or an attached Special
Energy (both via their CardDefinition's passive=). The engine collects the
active (passive, carrier) pairs each time it computes damage, attack costs,
or max HP, so effects switch on/off purely by board position.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Set, Tuple

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import ABILITIES_BY_ID, def_for, subtypes_for
from spirit.game.models.board import (
    BoardEntity,
    BoardState,
    CardEntity,
    PokemonEntity,
)

WEAKNESS_MULTIPLIER = 2
RESISTANCE_REDUCTION = 30


@dataclass
class TurnDamageModifier:
    """A turn-scoped attacker-side damage boost (Power Tablet: "+30 damage
    during this turn to your Fusion Strike Pokemon's attacks")."""
    amount: int
    player_id: str
    requires_subtype: Optional[str] = None
    opposing_active_only: bool = True


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
        self.weakness_applies = True
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

    def modify_damage_dealt(self, calc: DamageCalc, carrier: BoardEntity):
        """Attacker-side "does more/less damage" step (runs before W/R)."""

    def modify_weakness(self, calc: DamageCalc, carrier: BoardEntity):
        """May clear calc.weakness_applies (e.g. "... have no Weakness")."""

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
        self, cost: int, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Returns the (possibly reduced) retreat cost (Air Balloon's -2)."""
        return cost

    def blocks_attack_effects(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to shield `target` from opponents' attack EFFECTS (not damage)."""
        return False

    def blocks_abilities(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to turn off `pokemon`'s Abilities (Path to the Peak style)."""
        return False

    def knockout_destination(self, pokemon: PokemonEntity, carrier: BoardEntity) -> Optional[str]:
        """Area name replacing "discard" for a knocked-out Pokemon (e.g. "lostZone")."""
        return None


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
    return triples


def ability_locked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive (Path to the Peak) is disabling `pokemon`'s Abilities.

    Evaluated on the UNFILTERED set: a lock contributed by a Pokemon ability
    is never itself disabled by another lock (Garbotoxin-style recursion is
    out of scope -- Path to the Peak rides a Stadium so this is safe).
    """
    return any(p.blocks_abilities(pokemon, c) for p, c, _ in _collect_passives(board))


def active_passives(board: BoardState) -> List[Tuple[Passive, BoardEntity]]:
    """All (passive, carrier) pairs currently switched on by board position.

    Ability passives count only for top-level in-play Pokemon (a tucked
    pre-evolution's ability is off); tool/energy/stadium passives count
    anywhere in an in-play stack. Ability-contributed passives on a Pokemon
    whose own Abilities are locked (Path to the Peak) are excluded.
    """
    triples = _collect_passives(board)

    def blocked(pokemon: PokemonEntity) -> bool:
        return any(p.blocks_abilities(pokemon, c) for p, c, _ in triples)

    return [(p, c) for p, c, is_ability in triples
            if not (is_ability and blocked(c))]


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
) -> DamageCalc:
    """Runs the full damage pipeline: dealt-modifiers, W/R, taken-modifiers,
    prevention. Returns the finished DamageCalc.

    ignore_weakness (Cramorant's Spit Innocently) skips the Weakness stage but
    keeps Resistance -- distinct from apply_modifiers, which gates both.
    """
    calc = DamageCalc(board, attacker, target, base,
                      is_attack=is_attack, apply_modifiers=apply_modifiers,
                      ignore_target_effects=ignore_target_effects)
    if ignore_weakness:
        calc.weakness_applies = False
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
            if mod.opposing_active_only and not (calc.is_opposing and calc.to_active):
                continue
            calc.amount += mod.amount
        calc.amount = max(0, calc.amount)

    if calc.apply_modifiers and attacker is not None:
        for passive, carrier in passives:
            passive.modify_weakness(calc, carrier)
        attacker_types = attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        weak_types = target.get_attribute(AttrID.WEAKNESS_TYPES) or []
        if calc.weakness_applies and any(t in weak_types for t in attacker_types):
            calc.weakness_hit = True
            calc.amount *= WEAKNESS_MULTIPLIER
        resist_type = target.get_attribute(AttrID.RESISTANCE_TYPES)
        if resist_type in attacker_types:
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
        cost = passive.modify_retreat_cost(cost, pokemon, carrier)
    return max(0, cost)


def effective_max_hp(board: BoardState, pokemon: PokemonEntity) -> int:
    """Printed max HP plus every max-HP bonus riding the Pokemon's stack."""
    printed = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
    )
    bonus = sum(
        passive.max_hp_bonus(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )
    return printed + bonus


def attack_effects_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive shields `target` from opposing attack effects."""
    return any(
        passive.blocks_attack_effects(target, carrier)
        for passive, carrier in active_passives(board)
    )
