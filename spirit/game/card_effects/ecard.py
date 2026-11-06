"""Shared helpers for WOTC e-Card (Expedition / Aquapolis / Skyridge).

Card scripts stay thin data definitions; put non-trivial behavior here so
reprints across the three sets can import the same effect.
"""

from __future__ import annotations

import random
from typing import Any, Callable, List, Optional

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
from spirit.game.content.definitions import (
    ABILITIES_BY_ID,
    Ability,
    Activations,
    Attack,
    ability_id_for,
)
from spirit.game.data_utils import (
    CARD_DEFS_BY_GUID, TRAINER_EFFECTS_BY_GUID, def_for, evolves_from,
    is_baby_pokemon, unimplemented,
)
from spirit.game.models.board import EnergyEntity, PokemonEntity
from spirit.game.card_effects.attacks_common import (
    count_energy,
    damage_counters_on,
    damage_per,
    flip_damage,
    flip_or_nothing,
    lock_all_attacks,
    lock_defender_attacks,
    self_energy_discard_attack,
    snipe_attack,
    spread_damage,
)
from spirit.game.card_effects.passives_common import (
    ability_lock_passive,
    apply_own_next_turn_boost,
    apply_protection,
    attack_effect_shield_passive,
    condition_immunity_passive,
    GutsSurvivePassive,
    is_in_active_spot,
    no_resistance_passive,
    opposing_active,
    prevent_damage_when,
    retreat_free_when,
    takes_less_passive,
)
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.pokemon import devolvable, energy_provides_type
from spirit.game.card_effects.support_common import (
    attach_from_discard,
    look_at_top,
    opponent_switches,
    recover_from_discard,
    requires_discard,
    requires_hand,
    search_attach_energy,
    search_to_bench,
    search_to_hand,
    switch_self_attack,
)
from spirit.game.card_effects.trainers import (
    FossilBodyPassive,
    bench_has_room,
    deck_nonempty,
    escape_rope,
    fossil_discard_ability,
    hand_size_at_least,
    has_basic_energy_in_hand,
    is_basic_energy_card,
    is_energy_card,
    is_psychic_energy_card,
)
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_evolution_pokemon,
    is_pokemon_card,
    is_special_energy,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.legal_actions import (
    LOCK_UNTIL_LEAVES_ACTIVE,
    _energy_provided_types,
    attack_cost_satisfied,
    energy_provided_count,
)
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    ability_locked,
    carrier_pokemon,
    effective_attack_cost,
    effective_bench_capacity,
    effective_max_hp,
    effective_pokemon_types,
    effective_retreat_cost,
    energy_provided_options,
    granted_extra_attacks,
)


def no_special_conditions(board, player_id, pokemon=None) -> bool:
    """Poké-Power gate: unusable while the Pokemon has any Special Condition."""
    if pokemon is None:
        return False
    return not bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def is_basic_non_baby(card) -> bool:
    """Dual Ball / similar: Basic Pokémon other than a Baby Pokémon."""
    from spirit.game.session.effects import is_basic_pokemon
    from spirit.game.data_utils import is_baby_pokemon
    return is_basic_pokemon(card) and not is_baby_pokemon(card.archetype_id)


class TechnicalMachinePassive(Passive):
    """Grants the TM's Attack(s) to the holder; discarded at end of owner turn.

    Pass the Attack (or list) that the TM printed. The Attack must already be
    registered on the TM card (ability_id assigned) — typically via putting it
    in TrainerCardDef.abilities so ABILITIES_BY_ID is populated.
    """

    def __init__(self, attacks: Any):
        if isinstance(attacks, (list, tuple)):
            self._attacks = list(attacks)
        else:
            self._attacks = [attacks]

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        # Only while this TM is still attached as the carrier.
        if carrier.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.TECHNICAL_MACHINE.value:
            return []
        return list(self._attacks)


def pokemon_has_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return pokemon_type.value in types


# ----------------------------------------------------------------------
# Ability-condition helpers
# ----------------------------------------------------------------------

def all_conditions(*predicates: Callable) -> Callable:
    """AND of (board, player_id, pokemon) predicates."""
    def check(board, player_id, pokemon=None) -> bool:
        return all(pred(board, player_id, pokemon) for pred in predicates)
    return check


def is_active(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and pokemon is board.active_pokemon(player_id)


def is_benched(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and pokemon is not board.active_pokemon(player_id)


def _has_bench(board, player_id) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


def has_bench(board, player_id, pokemon=None) -> bool:
    return _has_bench(board, player_id)


def opponent_has_benched(board, player_id, pokemon=None) -> bool:
    """Attack/ability gate: the opponent has at least one Benched Pokémon."""
    opponent = _opponent_id(board, player_id)
    return bool(opponent) and _has_bench(board, opponent)


def _opponent_id(board, player_id):
    return next((pid for pid in board.player_ids if pid != player_id), None)


def _is_damaged(board, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def self_is_damaged(board, player_id, pokemon=None) -> bool:
    """Attack/ability gate: this Pokémon has at least one damage counter."""
    return pokemon is not None and _is_damaged(board, pokemon)


def self_has_damage_counters(minimum: int = 1):
    """Attack/ability gate: this Pokémon has at least `minimum` damage counters."""
    def check(board, player_id, pokemon=None) -> bool:
        if pokemon is None:
            return False
        hp = pokemon.get_attribute(AttrID.HP, 0)
        counters = max(0, (effective_max_hp(board, pokemon) - hp) // 10)
        return counters >= minimum
    return check


def _typed_basic_energy(card, pokemon_type: PokemonTypes) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(card, pokemon_type.value)


def _energy_cards_of_type(ctx, pokemon, pokemon_type: PokemonTypes) -> list:
    return [e for e in ctx.attached_energies(pokemon)
            if _typed_basic_energy(e, pokemon_type)]


# ----------------------------------------------------------------------
# Alakazam — Psymimic / Syncroblast
# ----------------------------------------------------------------------

def _cost_as_names(cost) -> dict:
    named = {}
    for key, count in (cost or {}).items():
        if key in CLIENT_POKEMON_TYPE_NAMES:
            named[CLIENT_POKEMON_TYPE_NAMES[key]] = count
        else:
            named[key] = count
    return named


def copyable_opponent_attacks(board, copier, player_id,
                              require_energy: bool = True,
                              skip_requirements: bool = False) -> List:
    """(pokemon, attack) pairs from the opponent's in-play Pokémon the copier
    may use (Psymimic pays Energy; Super Metronome skips the Energy cost)."""
    opponent = _opponent_id(board, player_id)
    if copier is None or opponent is None:
        return []
    energies = board.attached_energies(copier)
    pairs = []
    seen = set()
    for pokemon in board.pokemon_in_play(opponent):
        definition = def_for(pokemon.archetype_id)
        attacks = [a for a in (getattr(definition, "abilities", None) or [])
                   if isinstance(a, Attack)]
        attacks.extend(granted_extra_attacks(board, pokemon))
        for attack in attacks:
            key = attack.ability_id or (attack.title, attack.game_text)
            if key in seen:
                continue
            seen.add(key)
            if not skip_requirements:
                if attack.condition is not None \
                        and not attack.condition(board, player_id, copier):
                    continue
                if require_energy:
                    cost = effective_attack_cost(
                        board, copier, _cost_as_names(attack.cost))
                    if not attack_cost_satisfied(cost, energies, board):
                        continue
            pairs.append((pokemon, attack))
    return pairs


def psymimic_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    return bool(copyable_opponent_attacks(board, pokemon, player_id))


async def psymimic(ctx):
    """Copy 1 of the opponent's in-play Pokémon's attacks, paying its cost.

    Used instead of Alakazam's normal attack (Ability.ends_turn).
    """
    candidates = copyable_opponent_attacks(ctx.board, ctx.source, ctx.player_id)
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(
        candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    ctx.ends_turn = True
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(
                    ctx.attacker.entity_id, entry["abilityID"])


def syncroblast_damage(matched: int = 80, mismatched: int = 20):
    """Deal `matched` if both Actives have the same number of Energy cards,
    otherwise `mismatched` (Alakazam 80/20, Girafarig 40/10)."""
    async def effect(ctx):
        mine = len(ctx.attached_energies(ctx.attacker))
        theirs = len(ctx.attached_energies(ctx.defender)) if ctx.defender else 0
        await ctx.deal_damage(matched if mine == theirs else mismatched)
    return effect


syncroblast = syncroblast_damage()


# ----------------------------------------------------------------------
# Ampharos — Energy Connect / Lightning Strike
# ----------------------------------------------------------------------

def energy_connect_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if board.active_pokemon(player_id) is None:
        return False
    bench = board.find_player_area(player_id, "bench")
    for poked in (bench.children if bench else []):
        if not isinstance(poked, PokemonEntity):
            continue
        if any(is_basic_energy_card(e) for e in board.attached_energies(poked)):
            return True
    return False


async def energy_connect(ctx):
    """Move 1 basic Energy from a Benched Pokémon onto the Active."""
    active = ctx.my_active()
    if active is None:
        return
    pool = [e for poked in ctx.my_bench()
            for e in ctx.attached_energies(poked)
            if is_basic_energy_card(e)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, prompt="Choose a basic Energy card to attach to your Active Pokémon")
    if picks:
        await ctx.move_energy(picks[0], active)


async def lightning_strike(ctx):
    """You may discard all Lightning Energy cards; if you do, 80 instead of 40."""
    lightning = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    name = "this Pokémon"
    if ctx.attacker is not None:
        definition = def_for(ctx.attacker.archetype_id)
        if definition is not None and definition.display_name:
            name = definition.display_name
    boosted = bool(lightning) and await ctx.ask_yes_no(
        f"Discard all Lightning Energy cards attached to {name}?")
    if boosted:
        await ctx.discard_cards(lightning)
        await ctx.deal_damage(80)
    else:
        await ctx.deal_damage(40)


# ----------------------------------------------------------------------
# Blastoise — Jet Stream / Energy Cannon
# ----------------------------------------------------------------------

def jet_stream_condition(board, player_id, pokemon=None) -> bool:
    return no_special_conditions(board, player_id, pokemon) \
        and is_active(board, player_id, pokemon)


async def jet_stream(ctx):
    """Flip: heads discards 1 Energy from Blastoise, then 1 from the Defending."""
    results = await ctx.flip_coins(1, "Jet Stream")
    if not results or not results[0]:
        return
    if ctx.attached_energies(ctx.source):
        await ctx.discard_energy_from(
            ctx.source, 1,
            prompt="Choose an Energy card to discard from Blastoise")
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    if ctx.attached_energies(defender):
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose an Energy card to discard from the Defending Pokémon")


def unused_energy_bonus(per: int, cap: int, base: Optional[int] = None,
                        energy_type=None):
    """Printed (or base) + per for each unused attached Energy, capped.

    energy_type limits both the attached count and the printed cost subtracted
    (Water Gun: only Water Energy vs the Water in the attack cost).
    """
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if type_value is None:
            total = sum(energy_provided_count(e, ctx.board)
                        for e in ctx.attached_energies(ctx.attacker))
        else:
            total = count_energy("self", energy_type=energy_type)(ctx)
        cost = (ctx.ability.cost or {}) if ctx.ability else {}
        cost_total = 0
        for key, n in cost.items():
            if type_value is None or getattr(key, "value", key) == type_value:
                cost_total += n
        extra = max(0, total - cost_total)
        bonus = min(extra * per, cap)
        base_val = base if base is not None else (getattr(ctx.ability, "damage", 0) or 0)
        amount = base_val + bonus
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


# ----------------------------------------------------------------------
# Butterfree — Miraculous Powder / Spiral Drain
# ----------------------------------------------------------------------

def miraculous_powder_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    active = board.active_pokemon(player_id)
    return active is not None and bool(
        active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def miraculous_powder(ctx):
    """Remove all Special Conditions from your Active Pokémon."""
    active = ctx.my_active()
    if active is not None:
        await ctx.cure_all_conditions(active)


async def spiral_drain(ctx):
    """40; flip — heads heals 20 from Butterfree."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Spiral Drain")
    if results and results[0]:
        await ctx.heal(20, ctx.attacker)


# ----------------------------------------------------------------------
# Charizard — Burning Energy / Scorching Whirlwind
# ----------------------------------------------------------------------

class BurningEnergyPassive(Passive):
    """All of the owner's basic Energy provide Fire for the rest of the turn."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or not is_basic_energy_card(energy):
            return options
        mine = any(
            isinstance(passive, BurningEnergyPassive)
            and carrier.owning_player_id == holder.owning_player_id
            for passive, carrier in _active_passives(board)
        )
        if not mine:
            return options
        fire = PokemonTypes.FIRE.value
        if not options:
            return [[fire]]
        return [[fire] * max(1, len(option)) for option in options]


def _active_passives(board):
    from spirit.game.session.passives import active_passives
    return active_passives(board)


def burning_energy_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return any(
        is_basic_energy_card(e)
        for poked in board.pokemon_in_play(player_id)
        for e in board.attached_energies(poked)
    )


async def burning_energy(ctx):
    """Turn all of your basic Energy into Fire Energy for the rest of the turn."""
    ctx.add_temporary_passive(
        ctx.source, BurningEnergyPassive(),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


async def scorching_whirlwind(ctx):
    """120; 1 tails discards 2 Energy, 2 tails discards all Energy."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Scorching Whirlwind")
    tails = sum(1 for result in results if not result)
    if tails >= 2:
        await ctx.discard_cards(list(ctx.attached_energies(ctx.attacker)))
    elif tails == 1:
        await ctx.discard_energy_from(
            ctx.attacker, 2,
            prompt="Choose 2 Energy cards to discard from Charizard")


# ----------------------------------------------------------------------
# Clefable — Moonlight
# ----------------------------------------------------------------------

def moonlight_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and hand.children)


async def moonlight(ctx):
    """Put a card from hand onto the deck, then search a basic Energy into hand."""
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, prompt="Choose a card to put on top of your deck")
    if not picks:
        return
    await ctx.put_on_top_of_deck(picks[0])
    found = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card to put into your hand.",
    )
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Dragonite — Tailwind
# ----------------------------------------------------------------------

def tailwind_condition(board, player_id, pokemon=None) -> bool:
    if not is_benched(board, player_id, pokemon):
        return False
    active = board.active_pokemon(player_id)
    return active is not None and effective_retreat_cost(board, active) > 0


async def tailwind(ctx):
    """Reduce your Active Pokémon's Retreat Cost to 0 (rest of this turn)."""
    active = ctx.my_active()
    if active is None:
        return
    ctx.add_temporary_passive(
        active, retreat_free_when(lambda pokemon, carrier: pokemon is carrier),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


# ----------------------------------------------------------------------
# Feraligatr — Major Tsunami / Rending Jaws
# ----------------------------------------------------------------------

def major_tsunami_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    return _has_bench(board, player_id) or (
        opponent is not None and _has_bench(board, opponent))


async def major_tsunami(ctx):
    """Opponent switches if they can; you switch Feraligatr if you can."""
    if ctx.opponent_bench():
        await opponent_switches(ctx)
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def rending_jaws(ctx):
    """70, or 40 if the Defending Pokémon has no damage counters."""
    defender = ctx.defender
    damaged = defender is not None and _is_damaged(ctx.board, defender)
    await ctx.deal_damage(70 if damaged else 40)


# ----------------------------------------------------------------------
# Gengar — Chaos Move
# ----------------------------------------------------------------------

def chaos_move_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    prizes = board.find_player_area(opponent, "prizePile")
    if prizes is None or len(prizes.children) > 3:
        return False
    everyone = []
    for pid in board.player_ids:
        everyone.extend(board.pokemon_in_play(pid))
    if len(everyone) < 2:
        return False
    return any(_is_damaged(board, poked) for poked in everyone)


async def chaos_move(ctx):
    """Move 1 damage counter from any Pokémon to another."""
    everyone = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    damaged = [poked for poked in everyone if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to move a damage counter from")
    if source is None:
        return
    dests = [poked for poked in everyone if poked is not source]
    if not dests:
        return
    dest = await ctx.choose_pokemon(
        dests, "Choose a Pokémon to move the damage counter to")
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)


# ----------------------------------------------------------------------
# Machamp — Terraforming / Iron Fist
# ----------------------------------------------------------------------

def terraforming_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    deck = board.find_player_area(player_id, "deck")
    return deck is not None and len(deck.children) >= 2


async def terraforming(ctx):
    """Look at the top 4 cards of your deck and put them back in any order."""
    top = ctx.deck_top(4)
    if len(top) <= 1:
        return
    picks = await ctx.choose_cards(
        top, len(top), minimum=len(top), ordered=True,
        prompt="Put these cards back on top of your deck, in order.",
    )
    for card in picks:
        await ctx.put_on_top_of_deck(card)


async def iron_fist(ctx):
    """50; heads adds 10 for each of your Pokémon that has damage counters."""
    damaged = sum(1 for poked in ctx.my_pokemon_in_play()
                  if _is_damaged(ctx.board, poked))
    results = await ctx.flip_coins(1, "Iron Fist")
    bonus = damaged * 10 if results and results[0] else 0
    await ctx.deal_damage(50 + bonus)


# ----------------------------------------------------------------------
# Magby / Pichu
# ----------------------------------------------------------------------

async def energy_catch(ctx):
    """Flip: heads, put a basic Energy from discard into hand."""
    results = await ctx.flip_coins(1, "Energy Catch")
    if not results or not results[0]:
        return
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a basic Energy card to put into your hand")
    await ctx.put_in_hand(picks, reveal=True)


async def energy_patch(ctx):
    """Move 1 basic Energy from one of your Pokémon to another."""
    if len(ctx.my_pokemon_in_play()) < 2:
        return
    await ctx.move_energy_freely(
        ctx.my_pokemon_in_play(), ctx.my_pokemon_in_play(),
        predicate=is_basic_energy_card, max_count=1,
        prompt="Choose a basic Energy card to move",
    )


# ----------------------------------------------------------------------
# Meganium — Soothing Aroma
# ----------------------------------------------------------------------

def soothing_aroma_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return any(_is_damaged(board, poked)
               for poked in board.pokemon_in_play(player_id))


async def soothing_aroma(ctx):
    """Flip: heads, remove 1 damage counter from each of your damaged Pokémon."""
    results = await ctx.flip_coins(1, "Soothing Aroma")
    if not results or not results[0]:
        return
    for poked in ctx.my_pokemon_in_play():
        if _is_damaged(ctx.board, poked):
            await ctx.heal(10, poked)


# ----------------------------------------------------------------------
# Mew — Super Psywave
# ----------------------------------------------------------------------

async def super_psywave(ctx):
    """Put 1 damage counter on a chosen opposing Pokémon per Energy card on it."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    count = len(ctx.attached_energies(target))
    if count > 0:
        await ctx.deal_damage(count * 10, target=target, as_counters=True)


# ----------------------------------------------------------------------
# Ninetales — Ethereal Flame
# ----------------------------------------------------------------------

async def ethereal_flame(ctx):
    """Discard all Fire Energy cards; 30 + 20 per card discarded."""
    fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
    await ctx.discard_cards(fire)
    amount = 30 + 20 * len(fire)
    if amount > 0:
        await ctx.deal_damage(amount)


# ----------------------------------------------------------------------
# Pidgeot — Beating Wings
# ----------------------------------------------------------------------

def beating_wings_condition(board, player_id, pokemon=None) -> bool:
    return no_special_conditions(board, player_id, pokemon) \
        and is_active(board, player_id, pokemon) \
        and _has_bench(board, player_id)


async def beating_wings(ctx):
    """Shuffle 1 of your Benched Pokémon and all attached cards into your deck."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to shuffle into your deck")
    if target is None:
        return
    await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)


# ----------------------------------------------------------------------
# Poliwrath — Plunge
# ----------------------------------------------------------------------

def plunge_condition(board, player_id, pokemon=None) -> bool:
    return is_benched(board, player_id, pokemon) \
        and board.active_pokemon(player_id) is not None


async def plunge(ctx):
    """Flip: heads, move the Active's Energy onto Poliwrath and switch in."""
    results = await ctx.flip_coins(1, "Plunge")
    if not results or not results[0]:
        return
    active = ctx.my_active()
    poliwrath = ctx.source
    if active is None or active is poliwrath:
        return
    for energy in list(ctx.attached_energies(active)):
        await ctx.move_energy(energy, poliwrath)
    await ctx.switch_active(ctx.player_id, poliwrath)


# ----------------------------------------------------------------------
# Raichu — Plasma / Shock Bolt
# ----------------------------------------------------------------------

def collect_energy_from_discard(energy_type: PokemonTypes):
    """Printed damage; if that basic Energy is in discard, flip — heads, attach 1."""
    type_name = CLIENT_POKEMON_TYPE_NAMES.get(energy_type, "Energy")

    async def effect(ctx):
        await ctx.deal_damage()
        energy = [c for c in ctx.discard_pile()
                  if _typed_basic_energy(c, energy_type)]
        if not energy:
            return
        title = ctx.ability.title if ctx.ability else type_name
        results = await ctx.flip_coins(1, title)
        if not results or not results[0]:
            return
        picks = await ctx.choose_cards(
            energy, 1,
            prompt=f"Choose a {type_name} Energy card to attach")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


# Raichu / Zapdos Plasma is the Lightning form.
plasma = collect_energy_from_discard(PokemonTypes.LIGHTNING)


async def shock_bolt(ctx):
    """Discard all Lightning Energy cards or this attack does nothing; 60."""
    lightning = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    if not lightning:
        return
    await ctx.discard_cards(lightning)
    await ctx.deal_damage()


# ----------------------------------------------------------------------
# Golem — Rock Tumble
# ----------------------------------------------------------------------

async def rock_tumble(ctx):
    """Don't apply Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


# --- Trainers also printed in later eras (ported so ECARD1 needs no SM modules) ---

from spirit.game.card_effects.support_common import requires_discard, requires_hand
from spirit.game.session.effects import full_stack


async def bills_maintenance(ctx):
    """Shuffle 1 card from hand into deck, then draw 3."""
    picks = await ctx.choose_cards(
        list(ctx.hand()), 1,
        prompt="Shuffle a card from your hand into your deck.")
    if not picks:
        return
    await ctx.shuffle_into_deck(picks)
    await ctx.draw_cards(3)


bills_maintenance_condition = requires_hand(n=1)


async def moomoo_milk(ctx):
    """Flip 2 coins; heal 30 per heads from 1 of your Pokémon."""
    targets = ctx.my_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to heal")
    if target is None:
        return
    results = await ctx.flip_coins(2, "Moo-Moo Milk")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.heal(30 * heads, target)


async def super_scoop_up(ctx):
    """Flip a coin. If heads, put 1 of your Pokémon and all cards into your hand."""
    results = await ctx.flip_coins(1, "Super Scoop Up")
    if not results or not results[0]:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to put into your hand")
    if target is None:
        return
    owner = target.owning_player_id or ctx.player_id
    was_active = target is ctx.board.active_pokemon(owner)
    stack = full_stack(target)
    await ctx.put_in_hand(stack, reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(owner):
                screen_name = ctx.session.players[owner].screen_name
                await ctx.session.end_game(
                    ctx.session._opponent_id(owner),
                    f"{screen_name} has no Pokémon left",
                )
        ctx.deferred_actions.append(_promote)


# ----------------------------------------------------------------------
# Tyranitar — Dark Aura / Venusaur — Harvest Bounty
# ----------------------------------------------------------------------

def _is_in_active_area(pokemon) -> bool:
    parent = getattr(pokemon, "parent", None)
    while parent is not None:
        name = parent.get_attribute(AttrID.NAME) if hasattr(parent, "get_attribute") else None
        if isinstance(name, dict):
            name = name.get("id")
        if name == "activePokemonArea":
            return True
        parent = getattr(parent, "parent", None)
    return False


class DarkAuraPassive(Passive):
    """All Energy attached to the carrier provides Darkness instead."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or getattr(energy, "parent_id", None) != holder.entity_id:
            return options
        dark = PokemonTypes.DARKNESS.value
        if not options:
            return [[dark]]
        return [[dark] * max(1, len(option)) for option in options]


class HarvestBountyPassive(Passive):
    """Second Energy attach to Active after first manual attach this turn.
    Off while Venusaur has a Special Condition (Poké-Power restriction)."""

    def allows_second_energy_attach(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return False
        if carrier.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False
        return _is_in_active_area(pokemon)


# ----------------------------------------------------------------------
# Rapidash / Blaine's Rhyhorn — Overrun
# ----------------------------------------------------------------------

def overrun(bench_damage: int = 10):
    """Printed damage; if the opponent has a Bench, flip — heads,
    `bench_damage` to one Benched Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if not bench:
            return
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "Overrun")
        if not results or not results[0]:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(bench_damage, target=target)
    return effect


# ----------------------------------------------------------------------
# Typhlosion — Heat Up
# ----------------------------------------------------------------------

def _energy_card_count(board, player_id) -> int:
    return sum(len(board.attached_energies(poked))
               for poked in board.pokemon_in_play(player_id))


def heat_up_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not _has_bench(board, player_id):
        return False
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    return _energy_card_count(board, opponent) > _energy_card_count(board, player_id)


async def heat_up(ctx):
    """If the opponent has more Energy cards attached, search a Fire Energy onto a Benched Pokémon."""
    mine = sum(len(ctx.attached_energies(poked)) for poked in ctx.my_pokemon_in_play())
    theirs = sum(len(ctx.attached_energies(poked))
                 for poked in ctx.opponent_pokemon_in_play())
    if theirs <= mine:
        return
    found = await ctx.search_deck(
        lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        count=1, minimum=0,
        prompt="Choose a Fire Energy card to attach to 1 of your Benched Pokémon.",
    )
    bench = ctx.my_bench()
    if found and bench:
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(found[0], target)
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Tyranitar — Stamp
# ----------------------------------------------------------------------

async def stamp(ctx):
    """50; heads, +10 and 10 to each opposing Benched Pokémon."""
    results = await ctx.flip_coins(1, "Stamp")
    heads = bool(results and results[0])
    base = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(base + (10 if heads else 0))
    if not heads:
        return
    for poked in ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)


# ----------------------------------------------------------------------
# Vileplume — Poison Pollen
# ----------------------------------------------------------------------

async def poison_pollen(ctx):
    """Flip: heads, Poison the Defending Pokémon."""
    results = await ctx.flip_coins(1, "Poison Pollen")
    if not results or not results[0]:
        return
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


# ----------------------------------------------------------------------
# Weezing — Misfire
# ----------------------------------------------------------------------

async def misfire(ctx):
    """60; flip — tails, put 6 damage counters on Weezing."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Misfire")
    if results and not results[0]:
        await ctx.deal_damage(60, target=ctx.attacker, as_counters=True)


# ----------------------------------------------------------------------
# Typhlosion — Thermal Blast
# ----------------------------------------------------------------------

async def thermal_blast(ctx):
    """40; heads, 10 to each opposing Benched Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Thermal Blast")
    if not results or not results[0]:
        return
    for poked in ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)


# ----------------------------------------------------------------------
# Venusaur — Leech Seed
# ----------------------------------------------------------------------

async def leech_seed(ctx):
    """20; if it damages the Defending Pokémon, heal 10 from the attacker."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(10, ctx.attacker)


# ----------------------------------------------------------------------
# Chansey — Bind Wound / Dogpile
# ----------------------------------------------------------------------

async def bind_wound(ctx):
    """Flip: heads, heal 20 from 1 of your Pokémon."""
    results = await ctx.flip_coins(1, "Bind Wound")
    if not results or not results[0]:
        return
    damaged = [poked for poked in ctx.my_pokemon_in_play()
               if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal")
    if target is not None:
        await ctx.heal(20, target)


async def dogpile(ctx):
    """10× your Bench count to the Defending Pokémon and to Chansey."""
    amount = 10 * len(ctx.my_bench())
    if amount <= 0:
        return
    await ctx.deal_damage(amount)
    await ctx.deal_damage(amount, target=ctx.attacker, apply_modifiers=False)


# ----------------------------------------------------------------------
# Electabuzz — Reflect Energy
# ----------------------------------------------------------------------

async def reflect_energy(ctx):
    """20; move 1 basic Energy from Electabuzz onto a Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [e for e in ctx.attached_energies(ctx.attacker)
            if is_basic_energy_card(e)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1,
        prompt="Choose a basic Energy card to attach to 1 of your Benched Pokémon")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is not None:
        await ctx.move_energy(picks[0], target)


# ----------------------------------------------------------------------
# Haunter — Dream Eater
# ----------------------------------------------------------------------

def defending_is_asleep(board, player_id, pokemon=None) -> bool:
    """Attack gate: the opponent's Active Pokémon is Asleep."""
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    active = board.active_pokemon(opponent)
    if active is None:
        return False
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    return asleep in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def dream_eater(ctx):
    """50 only if the Defending Pokémon is Asleep; otherwise nothing."""
    defender = ctx.defender
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    if defender is None or asleep not in (
            defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        return
    await ctx.deal_damage()


# ----------------------------------------------------------------------
# Pidgeotto — Whirlwind
# ----------------------------------------------------------------------

async def whirlwind(ctx):
    """20, then the opponent switches their Active with a Benched Pokémon."""
    await ctx.deal_damage()
    await opponent_switches(ctx)


# ----------------------------------------------------------------------
# Wartortle — Giant Wave
# ----------------------------------------------------------------------

async def giant_wave(ctx):
    """Printed damage; this Pokémon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


async def tunneling(ctx):
    """Choose up to 2 of the opponent's Benched Pokémon; 20 to each (no W/R).
    This Pokémon can't attack during your next turn."""
    await snipe_attack(
        20, count=2, optional=True,
        prompt="Choose up to 2 of your opponent's Benched Pokémon",
    )(ctx)
    lock_all_attacks(ctx, ctx.attacker)


# ----------------------------------------------------------------------
# Strength Charm
# ----------------------------------------------------------------------

class StrengthCharmPassive(Passive):
    """Holder's attacks do +10. Marked for end-of-turn discard after dealing
    attack damage (Strength Charm text: discard at end of that turn)."""

    def __init__(self):
        self._hit_this_turn = False

        async def _intercept(ctx, calc, target, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return None
            if carrier_pokemon(carrier) is not calc.attacker:
                return None
            if calc.amount <= 0:
                return None
            # +10 after W/R (interceptor runs after compute_damage)
            self._hit_this_turn = True
            carrier.set_attribute("_strength_charm_spent", True)
            return calc.amount + 10

        self.damage_interceptor = _intercept


# ----------------------------------------------------------------------
# Classic Darkness / Metal Energy (e-Card)
# ----------------------------------------------------------------------

class ClassicDarknessEnergyPassive(Passive):
    """+10 attack damage after W/R. EOT self-damage handled in game_session."""

    def __init__(self):
        async def _intercept(ctx, calc, target, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return None
            if carrier_pokemon(carrier) is not calc.attacker:
                return None
            if calc.amount <= 0:
                return None
            return calc.amount + 10
        self.damage_interceptor = _intercept


class ClassicMetalEnergyPassive(Passive):
    """-10 damage taken after W/R; if holder is not Metal, also -10 damage dealt."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.target:
            return
        calc.amount = max(0, calc.amount - 10)

    def modify_damage_dealt(self, calc, carrier):
        # Penalty for non-Metal holders (before W/R approx; text says after W/R)
        pokemon = carrier_pokemon(carrier)
        if pokemon is None or pokemon is not calc.attacker:
            return
        if not (calc.is_attack and calc.is_opposing):
            return
        if pokemon_has_type(pokemon, PokemonTypes.METAL):
            return
        calc.amount = max(0, calc.amount - 10)




# ----------------------------------------------------------------------
# Swift
# ----------------------------------------------------------------------

async def swift(ctx):
    """Damage isn't affected by Weakness, Resistance, or effects on the target."""
    await ctx.deal_damage(apply_modifiers=False, ignore_target_effects=True)


# ----------------------------------------------------------------------
# Electrode — Super Dynamo
# ----------------------------------------------------------------------

def super_dynamo_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    discard = board.find_player_area(player_id, "discard")
    return any(_typed_basic_energy(c, PokemonTypes.LIGHTNING)
               for c in (discard.children if discard else []))


async def super_dynamo(ctx):
    """Flip: heads, attach a Lightning Energy from discard to 1 of your Pokémon."""
    results = await ctx.flip_coins(1, "Super Dynamo")
    if not results or not results[0]:
        return
    energy = [c for c in ctx.discard_pile()
              if _typed_basic_energy(c, PokemonTypes.LIGHTNING)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a Lightning Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


# ----------------------------------------------------------------------
# Elekid — Energy Kick
# ----------------------------------------------------------------------

async def energy_kick(ctx):
    """Heads: you choose an Energy on the Defending; opponent moves it to the Bench."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    results = await ctx.flip_coins(1, "Energy Kick")
    if not results or not results[0]:
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1,
        prompt="Choose an Energy card attached to the Defending Pokémon")
    if not picks:
        return
    dest = await ctx.choose_pokemon(
        bench, "Choose a Pokémon to move the Energy to",
        player_id=ctx.opponent_id)
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


# ----------------------------------------------------------------------
# Entei / Suicune / Raikou — Pure Body
# ----------------------------------------------------------------------

def pure_body_on_energy_attached(energy_type: PokemonTypes):
    """ON_ENERGY_ATTACHED: after attaching that basic Energy from hand, discard 1 Energy."""

    async def watch(ctx):
        if ctx.energy_receiver is not ctx.source:
            return
        if ctx.attaching_player_id != ctx.player_id:
            return
        energy = ctx.attached_energy
        if energy is None or not _typed_basic_energy(energy, energy_type):
            return
        if not ctx.attached_energies(ctx.source):
            return
        await ctx.discard_energy_from(
            ctx.source, 1,
            prompt="Choose an Energy card to discard")

    return watch


# ----------------------------------------------------------------------
# Entei — Burning Fang
# ----------------------------------------------------------------------

async def burning_fang(ctx):
    """40; you may flip — heads discards a Fire Energy and Burns the Defending."""
    await ctx.deal_damage()
    if not await ctx.ask_yes_no(
            "Flip a coin? If heads, discard a Fire Energy and the Defending Pokémon is Burned."):
        return
    results = await ctx.flip_coins(1, "Burning Fang")
    if not results or not results[0]:
        return
    fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
    if fire:
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
            prompt="Choose a Fire Energy card to discard from Entei")
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


# ----------------------------------------------------------------------
# Espeon — Energy Return
# ----------------------------------------------------------------------

def energy_return_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return any(board.attached_energies(poked)
               for poked in board.pokemon_in_play(player_id))


async def energy_return(ctx):
    """Return 1 Energy attached to any of your Pokémon to your hand."""
    pool = [e for poked in ctx.my_pokemon_in_play()
            for e in ctx.attached_energies(poked)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, prompt="Choose an Energy card to return to your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


# ----------------------------------------------------------------------
# Exeggcute — Growth Spurt / Energy Support
# ----------------------------------------------------------------------

def attach_hand_energy(count: int = 1, predicate=None, minimum: Optional[int] = None):
    """Attach matching Energy cards from hand to this Pokémon.

    minimum defaults to 1 when attaching exactly one card, else 0 ("up to").
    """
    pred = predicate or is_energy_card
    min_count = 1 if minimum is None and count == 1 else (
        0 if minimum is None else minimum)

    async def effect(ctx):
        energy = [c for c in ctx.hand() if pred(c)]
        if not energy:
            return
        picks = await ctx.choose_cards(
            energy, min(count, len(energy)), minimum=min_count,
            prompt="Choose Energy cards to attach")
        holder = ctx.attacker if ctx.is_attack_effect() else ctx.source
        for card in picks:
            await ctx.attach_energy(card, holder)
    return effect


attach_hand_energy_to_self = attach_hand_energy(count=1, minimum=1)


def energy_support(energy_type: PokemonTypes):
    """Flip: heads, search that basic Energy onto 1 of your Benched Pokémon."""
    return flip_or_nothing(then=search_attach_energy(
        predicate=lambda c, t=energy_type: _typed_basic_energy(c, t),
        target_pred=lambda p: not _is_in_active_area(p),
    ))


# ----------------------------------------------------------------------
# Exeggutor — Super Eggsplosion / Called Shot
# ----------------------------------------------------------------------

async def super_eggsplosion(ctx):
    """Discard any number of Energy from your Pokémon; 40× heads of that many flips."""
    pool = [e for poked in ctx.my_pokemon_in_play()
            for e in ctx.attached_energies(poked)]
    discarded = []
    if pool:
        discarded = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Discard any number of Energy cards attached to your Pokémon")
        if discarded:
            await ctx.discard_cards(discarded)
    results = await ctx.flip_coins(len(discarded), "Super Eggsplosion") if discarded else []
    heads = sum(1 for result in results if result)
    amount = 40 * heads
    if amount > 0:
        await ctx.deal_damage(amount)


async def called_shot(ctx):
    """10× Grass Energy on the attacker to 1 of the opponent's Benched Pokémon."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    amount = 10 * count_energy("self", PokemonTypes.GRASS)(ctx)
    if target is not None and amount > 0:
        await ctx.deal_damage(amount, target=target)


def count_benched_energy(ctx) -> int:
    """Provided Energy attached to all of your Benched Pokémon."""
    return sum(energy_provided_count(e, ctx.board)
               for poked in ctx.my_bench()
               for e in ctx.attached_energies(poked))


# ----------------------------------------------------------------------
# Furret — Scavenger Hunt
# ----------------------------------------------------------------------

def scavenger_hunt_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) >= 2


async def scavenger_hunt(ctx):
    """Put 2 cards from hand into deck, then search an Energy into hand."""
    hand = ctx.hand()
    if len(hand) < 2:
        return
    picks = await ctx.choose_cards(
        hand, 2, prompt="Choose 2 cards to put into your deck")
    if not picks or len(picks) < 2:
        return
    await ctx.shuffle_into_deck(picks)
    found = await ctx.search_deck(
        is_energy_card, count=1, minimum=0,
        prompt="Choose an Energy card to put into your hand.",
    )
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Gloom — Enervating Pollen
# ----------------------------------------------------------------------

class EnervatingPollenPassive(Passive):
    """Resistance on each player's Active Pokémon only reduces damage by 10."""

    def modify_resistance(self, calc, carrier):
        if calc.to_active:
            calc.resistance_reduction = 10


# --- Aquapolis / Skyridge Crystal Type + special Energies ---

_CRYSTAL_TYPE_ATTR = "_crystal_type"


class CrystalTypePassive(Passive):
    """Poké-Power Crystal Type: while `_crystal_type` is set on the holder,
    that value replaces the Pokémon's printed types (until end of turn)."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        override = pokemon.get_attribute(_CRYSTAL_TYPE_ATTR)
        if override is None:
            return types
        return [override]


def crystal_type_on_energy_attached(*allowed: PokemonTypes):
    """ON_ENERGY_ATTACHED watcher: attaching an allowed basic Energy from hand
    to this Pokémon sets its live type to that Energy's type until EOT."""
    allowed_values = {t.value for t in allowed}

    async def watch(ctx):
        if ctx.energy_receiver is not ctx.source:
            return
        if ctx.attaching_player_id != ctx.player_id:
            return
        energy = ctx.attached_energy
        if energy is None:
            return
        from spirit.game.card_effects.trainers import is_basic_energy_card
        if not is_basic_energy_card(energy):
            return
        etypes = energy.get_attribute(AttrID.POKEMON_TYPES) or []
        match = next((t for t in etypes if t in allowed_values), None)
        if match is None:
            return
        ctx.source.set_attribute(_CRYSTAL_TYPE_ATTR, match)

    return watch


def clear_crystal_types(board, player_id):
    """End-of-turn: drop Crystal Type overrides on `player_id`'s Pokémon."""
    for pokemon in list(board.pokemon_in_play(player_id)):
        if pokemon.get_attribute(_CRYSTAL_TYPE_ATTR) is not None:
            pokemon.set_attribute(_CRYSTAL_TYPE_ATTR, None)


class CrystalEnergyPassive(Passive):
    """Provides 1 Energy of each type among basic Energies on the holder;
    Colorless alone if none."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None:
            return [[PokemonTypes.COLORLESS.value]]
        from spirit.game.card_effects.trainers import is_basic_energy_card
        found = []
        for child in holder.children:
            if child is energy or not is_basic_energy_card(child):
                continue
            for t in child.get_attribute(AttrID.POKEMON_TYPES) or []:
                if t not in found:
                    found.append(t)
        return [found] if found else [[PokemonTypes.COLORLESS.value]]


class BoostEnergyPassive(Passive):
    """Provides CCC; holder can't retreat. Discarded at EOT of attach turn
    via discard_end_of_attach_turn, and when holder is no longer Evolved."""

    def blocks_retreat(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon

    def modify_energy_provided(self, options, energy, holder, board):
        return [[
            PokemonTypes.COLORLESS.value,
            PokemonTypes.COLORLESS.value,
            PokemonTypes.COLORLESS.value,
        ]]


def is_evolved_pokemon(pokemon) -> bool:
    stage = pokemon.get_attribute(AttrID.STAGE)
    return stage not in (None, PokemonStage.BASIC.value)


def evolved_of_types(*types: PokemonTypes):
    """attach_to predicate: Evolved Pokémon whose printed type is one of `types`."""
    wanted = {t.value for t in types}

    def check(pokemon) -> bool:
        if not is_evolved_pokemon(pokemon):
            return False
        ptypes = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        return bool(wanted & set(ptypes))
    return check


async def warp_energy_on_attach(ctx):
    """When attached from hand to the Active, switch it with a Benched Pokémon."""
    target = ctx.attached_to
    if target is None or target is not ctx.my_active():
        return
    bench = ctx.my_bench()
    if not bench:
        return
    pick = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to switch into the Active Spot"
    ) or bench[0]
    await ctx.switch_active(ctx.player_id, pick)


async def rainbow_energy_on_attach(ctx):
    """Put 1 damage counter on the Pokémon this is attached to."""
    target = ctx.attached_to
    if target is None:
        return
    await ctx.deal_damage(10, target=target, as_counters=True, apply_modifiers=False)


async def full_heal_energy_on_attach(ctx):
    """Full Heal Energy: cure Asleep/Confused/Paralyzed/Poisoned on attach from hand."""
    target = ctx.attached_to
    if target is None:
        return
    await ctx.cure_all_conditions(target)


async def potion_energy_on_attach(ctx):
    """Potion Energy: remove 1 damage counter from the Pokémon attached to."""
    target = ctx.attached_to
    if target is None:
        return
    await ctx.heal(10, target=target)


class WeaknessGuardPassive(Passive):
    """Attached Pokémon has no Weakness. Discarded at end of opponent's next turn
    (tracked via `_weakness_guard_until_turn` on the tool)."""

    def modify_weakness(self, calc, carrier):
        pokemon = carrier_pokemon(carrier)
        if pokemon is None or pokemon is not calc.target:
            return
        calc.weakness_applies = False


# ----------------------------------------------------------------------
# Hoppip / Skiploom — Lightweight
# ----------------------------------------------------------------------

class LightweightPassive(Passive):
    """Retreat costs Colorless less for each Grass Energy attached."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        grass = PokemonTypes.GRASS.value
        n = sum(1 for energy in board.attached_energies(pokemon)
                if energy_provides_type(energy, grass))
        return max(0, cost - n)


# ----------------------------------------------------------------------
# Jumpluff — Fluff
# ----------------------------------------------------------------------

_FLUFF_ATTR = "_fluff_prevented"


class FluffPassive(Passive):
    """If already damaged, flip to prevent an opposing attack's damage
    (and that attack's effects, once heads has been flipped)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if carrier_pokemon(carrier) is not target:
            return None
        target.set_attribute(_FLUFF_ATTR, False)
        if not _is_damaged(ctx.board, target):
            return None
        heads = await ctx.flip_coins(
            1, "Fluff", source=carrier_pokemon(carrier) or carrier)
        if heads and heads[0]:
            target.set_attribute(_FLUFF_ATTR, True)
            calc.prevented = True
            return 0
        return None

    def blocks_attack_effects(self, target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return bool(target.get_attribute(_FLUFF_ATTR))


# ----------------------------------------------------------------------
# Hitmontop — Triple Spin
# ----------------------------------------------------------------------

async def triple_spin(ctx):
    """20× heads (3 coins); 2+ heads switches this Pokémon with a Bench Pokémon."""
    results = await ctx.flip_coins(3, "Triple Spin")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(20 * heads)
    if heads < 2:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


# ----------------------------------------------------------------------
# Houndoom — Burn Up / Fireworks / Dark Impact
# ----------------------------------------------------------------------

async def burn_up(ctx):
    """Printed damage; tails discards all Fire Energy cards attached."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Burn Up")
    if results and not results[0]:
        await ctx.discard_cards(
            _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE))


async def fireworks(ctx):
    """Printed damage; tails discards 1 Fire Energy card attached."""
    await ctx.deal_damage()
    title = ctx.ability.title if ctx.ability else "Fireworks"
    results = await ctx.flip_coins(1, title)
    if not results or results[0]:
        return
    await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        prompt="Choose a Fire Energy card to discard")


async def dark_impact(ctx):
    """Printed damage; the Defending Pokémon can't use Poké-Powers through
    the opponent's next turn (engine ability-lock)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(
        defender,
        ability_lock_passive(
            lambda pokemon, carrier: carrier_pokemon(carrier) is pokemon),
    )


# ----------------------------------------------------------------------
# Houndour — Feint Attack
# ----------------------------------------------------------------------

async def feint_attack(ctx, amount: int = 20):
    """20 to a chosen opposing Pokémon, ignoring W/R and effects on it."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.deal_damage(
        amount, target=target,
        ignore_weakness=True, ignore_resistance=True,
        ignore_target_effects=True,
    )


# ----------------------------------------------------------------------
# Hypno — Sleep Pendulum / Spiral Aura
# ----------------------------------------------------------------------

sleep_pendulum_condition = all_conditions(no_special_conditions, is_active)


async def sleep_pendulum(ctx):
    """Make the Defending Pokémon Asleep."""
    await ctx.apply_special_condition(
        ctx.opponent_active(), SpecialConditions.ASLEEP)


async def spiral_aura(ctx):
    """Printed damage; if the Defending Pokémon wasn't KO'd, you may gust."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or defender in ctx.knockouts:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no(
            "Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon?"):
        return
    if ctx.effects_blocked(defender):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


# ----------------------------------------------------------------------
# Juggler
# ----------------------------------------------------------------------

async def juggler(ctx):
    """Discard up to 2 basic Energy from hand; draw 3 for 1, or 5 for 2."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, predicate=is_basic_energy_card,
        prompt="Discard up to 2 basic Energy cards from your hand")
    n = len(discarded)
    if n == 1:
        await ctx.draw_cards(3)
    elif n >= 2:
        await ctx.draw_cards(5)


juggler_condition = requires_hand(is_basic_energy_card, n=1)


# ----------------------------------------------------------------------
# Kangaskhan — Baby Outing
# ----------------------------------------------------------------------

async def baby_outing(ctx):
    """Look at the top 3, put 1 into hand, shuffle the rest into the deck."""
    top = ctx.deck_top(3)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1,
        prompt="Choose 1 of those cards to put into your hand.",
        display_cards=top,
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Kingdra — Dual Burn / Water Cyclone / Rapids
# ----------------------------------------------------------------------

async def dual_burn(ctx):
    """Printed damage; discard 1 attached Energy card per tails (2 coins)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Dual Burn")
    tails = sum(1 for result in results if not result)
    if tails:
        await ctx.discard_energy_from(
            ctx.attacker, tails,
            prompt="Choose Energy cards to discard from Kingdra")


def water_cyclone_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not _has_bench(board, player_id):
        return False
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    return any(energy_provides_type(e, PokemonTypes.WATER.value)
               for e in board.attached_energies(active))


async def water_cyclone(ctx):
    """Move 1 Water Energy from the Active onto a Benched Pokémon."""
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    pool = [e for e in ctx.attached_energies(active)
            if energy_provides_type(e, PokemonTypes.WATER.value)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, prompt="Choose a Water Energy card to move to the Bench")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is not None:
        await ctx.move_energy(picks[0], target)


async def rapids(ctx):
    """Printed damage; heads discards 1 Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Rapids")
    if not results or not results[0]:
        return
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    if ctx.attached_energies(defender):
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose an Energy card to discard from the Defending Pokémon")


# ----------------------------------------------------------------------
# Lanturn — Conduction / Ion Coating / Electric Tackle
# ----------------------------------------------------------------------

async def conduction(ctx):
    """Discard all Lightning Energy cards; 30 + 40 per heads among that many coins."""
    lightning = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    await ctx.discard_cards(lightning)
    results = await ctx.flip_coins(len(lightning), "Conduction") if lightning else []
    heads = sum(1 for result in results if result)
    await ctx.deal_damage(30 + 40 * heads)


class IonCoatingPassive(Passive):
    """Lightning Energy on the carrier provides Water instead."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None:
            return options
        coated = any(
            isinstance(passive, IonCoatingPassive)
            and carrier_pokemon(carrier) is holder
            for passive, carrier in _active_passives(board)
        )
        if not coated:
            return options
        lightning = PokemonTypes.LIGHTNING.value
        water = PokemonTypes.WATER.value
        return [[water if t == lightning else t for t in option]
                for option in (options or [])]


def ion_coating_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    return any(energy_provides_type(e, PokemonTypes.LIGHTNING.value)
               for e in board.attached_energies(active))


async def ion_coating(ctx):
    """Active's Lightning Energy becomes Water for the rest of this turn."""
    active = ctx.my_active()
    if active is None:
        return
    ctx.add_temporary_passive(
        active, IonCoatingPassive(),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


async def electric_tackle(ctx):
    """20 + 10 per Lightning Energy; tails, that much self-damage as well."""
    n = sum(1 for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.LIGHTNING.value))
    await ctx.deal_damage(20 + 10 * n)
    results = await ctx.flip_coins(1, "Electric Tackle")
    if results and not results[0] and n:
        await ctx.deal_damage(10 * n, target=ctx.attacker, apply_modifiers=False)


# ----------------------------------------------------------------------
# Aipom — Skedaddle
# ----------------------------------------------------------------------

async def skedaddle(ctx):
    """20; return this Pokémon and its basic Energy to hand. Does nothing
    with no Bench."""
    if not ctx.my_bench():
        return
    await ctx.deal_damage()
    pokemon = ctx.attacker
    if pokemon is None:
        return
    basic = [e for e in ctx.attached_energies(pokemon) if is_basic_energy_card(e)]
    leftovers = [c for c in full_stack(pokemon) if c is not pokemon and c not in basic]
    if leftovers:
        await ctx.discard_cards(leftovers)
    await ctx.put_in_hand([pokemon, *basic], reveal=False)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.session._opponent_id(ctx.player_id),
                f"{screen_name} has no Pokémon left",
            )
    ctx.deferred_actions.append(_promote)


# ----------------------------------------------------------------------
# Arcanine — Extreme Speed / Fire Blow
# ----------------------------------------------------------------------

class ExtremeSpeedPassive(Passive):
    """Retreat cost Colorless less for each Energy attached to the holder."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        return max(0, cost - len(board.attached_energies(pokemon)))


async def fire_blow(ctx):
    """You may discard any number of Fire Energy; +30 per heads among that many flips."""
    fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
    discarded = []
    if fire:
        discarded = await ctx.choose_cards(
            fire, len(fire), minimum=0,
            prompt="Choose any number of Fire Energy cards to discard")
        if discarded:
            await ctx.discard_cards(discarded)
    bonus = 0
    if discarded:
        results = await ctx.flip_coins(len(discarded), "Fire Blow")
        bonus = 30 * sum(1 for result in results if result)
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)


async def wildfire(ctx):
    """You may discard any number of Fire Energy cards; mill that many from
    the opponent's deck."""
    fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
    discarded = []
    if fire:
        discarded = await ctx.choose_cards(
            fire, len(fire), minimum=0,
            prompt="Choose any number of Fire Energy cards to discard")
        if discarded:
            await ctx.discard_cards(discarded)
    if discarded:
        await ctx.discard_cards(
            ctx.deck_top(len(discarded), player_id=ctx.opponent_id))


# ----------------------------------------------------------------------
# Ariados — Gluey Slime
# ----------------------------------------------------------------------

class GlueySlimePassive(Passive):
    """Each Active Pokémon costs Colorless more to retreat; copies don't stack."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if not is_in_active_spot(pokemon):
            return cost
        carriers = [
            c for p, c in _active_passives(board)
            if isinstance(p, GlueySlimePassive)
        ]
        if not carriers or carrier is not min(carriers, key=lambda c: c.entity_id):
            return cost
        return cost + 1


# ----------------------------------------------------------------------
# Bellossom — Flower Supplement
# ----------------------------------------------------------------------

def flower_supplement_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not _has_bench(board, player_id):
        return False
    return has_basic_energy_in_hand(board, player_id)


async def flower_supplement(ctx):
    """Flip: heads, attach a basic Energy from hand to a Benched Pokémon."""
    results = await ctx.flip_coins(1, "Flower Supplement")
    if not results or not results[0]:
        return
    energy = [c for c in ctx.hand() if is_basic_energy_card(c)]
    bench = ctx.my_bench()
    if not energy or not bench:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a basic Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


# ----------------------------------------------------------------------
# Blissey — Happy Healing
# ----------------------------------------------------------------------

def happy_healing_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if pokemon is None or not board.attached_energies(pokemon):
        return False
    bench = board.find_player_area(player_id, "bench")
    return any(
        isinstance(poked, PokemonEntity) and _is_damaged(board, poked)
        for poked in (bench.children if bench else [])
    )


async def happy_healing(ctx):
    """Choose a Benched Pokémon, flip: heads, heal 1 counter per Energy on Blissey."""
    damaged = [poked for poked in ctx.my_bench() if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(
        damaged, "Choose a Benched Pokémon to heal")
    if target is None:
        return
    results = await ctx.flip_coins(1, "Happy Healing")
    if not results or not results[0]:
        return
    count = len(ctx.attached_energies(ctx.source))
    if count:
        await ctx.heal(count * 10, target)


# ----------------------------------------------------------------------
# Dodrio — Peck Attack
# ----------------------------------------------------------------------

async def peck_attack(ctx):
    """2 coins: 1 heads = 20, 2 heads = 50, 2 tails = Confused."""
    results = await ctx.flip_coins(2, "Peck Attack")
    heads = sum(1 for result in results if result)
    if heads >= 2:
        await ctx.deal_damage(50)
    elif heads == 1:
        await ctx.deal_damage(20)
    else:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)


# ----------------------------------------------------------------------
# Drowzee / Parasect — Sleep Inducer
# ----------------------------------------------------------------------

def sleep_inducer(flip: bool = False):
    """Gust a Benched Pokémon Active; it is now Asleep. flip=True gates on heads."""
    async def effect(ctx):
        if flip:
            title = ctx.ability.title if ctx.ability else "Sleep Inducer"
            results = await ctx.flip_coins(1, title)
            if not results or not results[0]:
                return
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon")
        if target is None:
            return
        await ctx.switch_active(ctx.opponent_id, target)
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
    return effect


# ----------------------------------------------------------------------
# Apricorn Forest
# ----------------------------------------------------------------------

def apricorn_forest_condition(board, player_id, stadium=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if bench is None or len(bench.children) >= effective_bench_capacity(board, player_id):
        return False
    return has_basic_energy_in_hand(board, player_id)


async def apricorn_forest(ctx):
    """Flip: heads, reveal a basic Energy from hand, bench a Basic of that type."""
    results = await ctx.flip_coins(1, "Apricorn Forest")
    if not results or not results[0]:
        return
    energy = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a basic Energy card to show your opponent")
    if not picks:
        return
    revealed = picks[0]
    await ctx.reveal_cards([revealed])
    types = set(revealed.get_attribute(AttrID.POKEMON_TYPES) or [])

    def pred(card):
        if not is_basic_non_baby(card):
            return False
        return bool(types & set(card.get_attribute(AttrID.POKEMON_TYPES) or []))

    found = await ctx.search_deck(
        pred, count=1, minimum=0,
        prompt="Choose a Basic Pokémon of the same type to put onto your Bench.",
    )
    if found:
        await ctx.bench_pokemon(found[0])
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Larvitar — Mountain Eater
# ----------------------------------------------------------------------

async def mountain_eater(ctx):
    """Opponent discards the top card of their deck; then heal 10 from Larvitar."""
    await ctx.discard_cards(ctx.deck_top(1, player_id=ctx.opponent_id))
    await ctx.heal(10, ctx.attacker)


# ----------------------------------------------------------------------
# Magnemite — Conductive Body / Magnetic Bomb
# ----------------------------------------------------------------------

class ConductiveBodyPassive(Passive):
    """Retreat costs Colorless less for each Magnemite on the owner's Bench."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        bench = board.find_player_area(pokemon.owning_player_id, "bench")
        n = sum(
            1 for poked in (bench.children if bench else [])
            if isinstance(poked, PokemonEntity)
            and poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Magnemite"
        )
        return max(0, cost - n)


# ----------------------------------------------------------------------
# Magneton — Magnetic Flow / Steel Wave
# ----------------------------------------------------------------------

def magnetic_flow_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    with_energy = [poked for poked in board.pokemon_in_play(opponent)
                   if board.attached_energies(poked)]
    return len(with_energy) >= 2


async def magnetic_flow(ctx):
    """Flip: heads, swap 1 Energy each between 2 opposing Pokémon that have Energy."""
    results = await ctx.flip_coins(1, "Magnetic Flow")
    if not results or not results[0]:
        return
    candidates = [poked for poked in ctx.opponent_pokemon_in_play()
                  if ctx.attached_energies(poked)]
    if len(candidates) < 2:
        return
    picks = await ctx.choose_cards(
        candidates, 2,
        prompt="Choose 2 of your opponent's Pokémon that have Energy attached")
    if len(picks) < 2:
        return
    first, second = picks[0], picks[1]
    energy_a = await ctx.choose_cards(
        ctx.attached_energies(first), 1,
        prompt="Choose an Energy card attached to the first Pokémon")
    energy_b = await ctx.choose_cards(
        ctx.attached_energies(second), 1,
        prompt="Choose an Energy card attached to the second Pokémon")
    if not energy_a or not energy_b:
        return
    await ctx.move_energy(energy_a[0], second)
    await ctx.move_energy(energy_b[0], first)


async def steel_wave(ctx):
    """Printed damage; 10 to each opposing Benched Pokémon of the Defending's type."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    types = set(defender.get_attribute(AttrID.POKEMON_TYPES) or [])
    if not types:
        return
    for poked in ctx.opponent_bench():
        if types & set(poked.get_attribute(AttrID.POKEMON_TYPES) or []):
            await ctx.deal_damage(10, target=poked)


# ----------------------------------------------------------------------
# Mankey — Mug
# ----------------------------------------------------------------------

async def mug(ctx):
    """Before damage, discard all Trainer cards attached to the Defending Pokémon."""
    defending = ctx.opponent_active()
    if defending is not None and not ctx.effects_blocked(defending):
        trainers = [child for child in list(defending.children)
                    if is_trainer_card(child)]
        if trainers:
            await ctx.discard_cards(trainers)
    await ctx.deal_damage()


# ----------------------------------------------------------------------
# Marowak — Triple Bone
# ----------------------------------------------------------------------

async def triple_bone(ctx):
    """10× heads (3 coins) to 1 opposing Benched Pokémon; no W/R."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is None:
        return
    results = await ctx.flip_coins(3, "Triple Bone")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(10 * heads, target=target)


# ----------------------------------------------------------------------
# Mr. Mime — Energy Barrier / Mind Shock
# ----------------------------------------------------------------------

class EnergyBarrierPassive(Passive):
    """Reduce attack damage by 10 per basic Energy card attached, max 20."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack:
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.target:
            return
        n = sum(1 for child in pokemon.children if is_basic_energy_card(child))
        calc.amount = max(0, calc.amount - min(20, 10 * n))


async def no_weakness_or_resistance(ctx):
    """Don't apply Weakness and Resistance."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)


# ----------------------------------------------------------------------
# Muk — Heavyweight / Burning Sludge
# ----------------------------------------------------------------------

class HeavyweightPassive(Passive):
    """If any Grass Energy is attached, retreat costs ColorlessColorless more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        grass = PokemonTypes.GRASS.value
        if any(energy_provides_type(energy, grass)
               for energy in board.attached_energies(pokemon)):
            return cost + 2
        return cost


async def burning_sludge(ctx):
    """Printed damage; flip 1 coin per Grass Energy — any heads Poisons and Burns."""
    await ctx.deal_damage()
    n = count_energy("self", PokemonTypes.GRASS)(ctx)
    if n <= 0:
        return
    results = await ctx.flip_coins(n, "Burning Sludge")
    if any(results):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


# ----------------------------------------------------------------------
# Nidoking — Earth Rage
# ----------------------------------------------------------------------

def earth_rage_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    return opponent is not None and _has_bench(board, opponent)


async def earth_rage(ctx):
    """Flip: heads, put a damage counter on each opposing Benched Pokémon."""
    results = await ctx.flip_coins(1, "Earth Rage")
    if not results or not results[0]:
        return
    for poked in ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked, as_counters=True)


# ----------------------------------------------------------------------
# Ninetales — Miracle Tail
# ----------------------------------------------------------------------

_CONDITION_CHOICES = [
    ("Asleep", SpecialConditions.ASLEEP),
    ("Burned", SpecialConditions.BURNED),
    ("Confused", SpecialConditions.CONFUSED),
    ("Paralyzed", SpecialConditions.PARALYZED),
    ("Poisoned", SpecialConditions.POISONED),
]


async def miracle_tail(ctx):
    """Printed damage; heads, choose a Special Condition for the Defending Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Miracle Tail")
    if not results or not results[0]:
        return
    target = ctx.defender
    if target is None:
        return
    idx = await ctx.choose(
        "Choose a Special Condition", [name for name, _ in _CONDITION_CHOICES],
    )
    await ctx.apply_special_condition(target, _CONDITION_CHOICES[idx][1])



# ----------------------------------------------------------------------
# Rapidash — Gallop
# ----------------------------------------------------------------------

async def gallop(ctx):
    """Flip: heads discards a Fire Energy card and does +20."""
    results = await ctx.flip_coins(1, "Gallop")
    bonus = 20 if results and results[0] else 0
    if bonus:
        fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
        if fire:
            await ctx.discard_energy_from(
                ctx.attacker, 1,
                predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
                prompt="Choose a Fire Energy card to discard from Rapidash")
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)


# ----------------------------------------------------------------------
# Scizor — Snatch
# ----------------------------------------------------------------------

async def snatch(ctx):
    """Before damage, you may gust an undamaged opposing Benched Pokémon."""
    defender = ctx.opponent_active()
    undamaged = [poked for poked in ctx.opponent_bench()
                 if not _is_damaged(ctx.board, poked)]
    if undamaged and defender is not None and not ctx.effects_blocked(defender):
        if await ctx.ask_yes_no(
                "Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon?"):
            target = await ctx.choose_pokemon(
                undamaged, "Choose the opponent's new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
    await ctx.deal_damage()


# ----------------------------------------------------------------------
# Seer / Sentret — Spy / Slowking — Shuffle Attack
# ----------------------------------------------------------------------

async def seer(ctx):
    """Look at the top 6; show all basic Energy found there and put them into hand."""
    top = ctx.deck_top(6)
    if not top:
        return
    energy = [c for c in top if is_basic_energy_card(c)]
    if energy:
        await ctx.choose_cards(
            energy, len(energy), minimum=len(energy),
            prompt="Take all basic Energy cards you find there.",
            display_cards=top,
        )
        await ctx.put_in_hand(energy, reveal=True)
    else:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, list(top),
            prompt="No basic Energy cards found.",
        )
    await ctx.shuffle_deck()


async def look_at_opponent_deck(ctx, count: int, reorder: bool = False):
    """Look at the top `count` of the opponent's deck; optionally rearrange them."""
    top = ctx.deck_top(count, ctx.opponent_id)
    if not top:
        return
    if not reorder:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, list(top),
            prompt="Top cards of your opponent's deck",
        )
        return
    picks = await ctx.choose_cards(
        top, len(top), minimum=len(top), ordered=True,
        prompt="Put these cards back on top of your opponent's deck, in order.",
    )
    for card in reversed(picks):
        await ctx.put_on_top_of_deck(card)


async def spy(ctx):
    """Look at the top 3 of the opponent's deck; put them back in the same order."""
    await look_at_opponent_deck(ctx, 3)


async def bursting_hand(ctx):
    """Look at the opponent's hand; 10× Energy cards there."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    count = sum(1 for c in hand if is_energy_card(c))
    amount = 10 * count
    if amount:
        await ctx.deal_damage(amount)


async def shuffle_attack(ctx):
    """Printed damage; reorder the top of the opponent's deck equal to Energy cards on the Defending."""
    await ctx.deal_damage()
    n = len(ctx.attached_energies(ctx.defender)) if ctx.defender else 0
    if n:
        await look_at_opponent_deck(ctx, n, reorder=True)


def is_pokemon_or_basic_energy(card) -> bool:
    """Baby / Basic / Evolution Pokémon, or a basic Energy card."""
    return is_pokemon_card(card) or is_basic_energy_card(card)


# ----------------------------------------------------------------------
# Sneasel — Rob
# ----------------------------------------------------------------------

def is_tm_or_tool(card) -> bool:
    ttype = card.get_attribute(AttrID.TRAINER_TYPE)
    return ttype in (
        TrainerType.TECHNICAL_MACHINE.value,
        TrainerType.POKEMON_TOOL.value,
        TrainerType.POKEMON_TOOL_F.value,
    )


async def rob(ctx):
    """Look at the opponent's hand; shuffle all TMs and Tools into their deck."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    matches = [c for c in hand if is_tm_or_tool(c)]
    if matches:
        await ctx.shuffle_into_deck(matches, ctx.opponent_id)


# ----------------------------------------------------------------------
# Octillery — Suction Cups
# ----------------------------------------------------------------------

class SuctionCupsPassive(Passive):
    """While this Pokémon is Active, the Defending Pokémon discards remaining
    Energy when it retreats to the Bench."""

    def discard_energy_on_retreat(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder):
            return False
        return pokemon.owning_player_id != holder.owning_player_id


# ----------------------------------------------------------------------
# Paras — Spore Evolution
# ----------------------------------------------------------------------

async def search_evolve_self(ctx):
    """Search the deck for a card that evolves from the attacker and evolve it."""
    logic_name = ctx.attacker.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda c: bool(logic_name) and evolves_from(c.archetype_id, logic_name),
        count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.attacker, picks[0])
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Parasect — Rapture Pollen
# ----------------------------------------------------------------------

async def rapture_pollen(ctx):
    """Printed damage; heads Asleep, tails heal 2 damage counters from self."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Rapture Pollen")
    if not results:
        return
    if results[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    else:
        await ctx.heal(20, ctx.attacker)


# ----------------------------------------------------------------------
# Porygon2 — Backup
# ----------------------------------------------------------------------

def backup_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) <= 2


# ----------------------------------------------------------------------
# Porygon — Data Sort
# ----------------------------------------------------------------------

async def data_sort(ctx):
    """Flip: heads, show a Trainer from the discard pile and shuffle it into the deck."""
    results = await ctx.flip_coins(1, "Data Sort")
    if not results or not results[0]:
        return
    cards = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose a Trainer card to shuffle into your deck")
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks)


# ----------------------------------------------------------------------
# Pokémon Park
# ----------------------------------------------------------------------

async def pokemon_park_on_energy_attached(ctx):
    """Once per turn: attaching Energy from hand to a Benched Pokémon heals 10."""
    receiver = ctx.energy_receiver
    if receiver is None or is_in_active_spot(receiver):
        return
    await ctx.heal(10, receiver)


# ----------------------------------------------------------------------
# Power Plant
# ----------------------------------------------------------------------

def power_plant_condition(board, player_id, stadium=None) -> bool:
    return has_basic_energy_in_hand(board, player_id)


async def power_plant(ctx):
    """Discard a basic Energy from hand, then put a basic Energy from discard into hand."""
    energy = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a basic Energy card to discard")
    if not picks:
        return
    await ctx.discard_cards(picks)
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not pool:
        return
    chosen = await ctx.choose_cards(
        pool, 1, minimum=1,
        prompt="Choose a basic Energy card to put into your hand")
    if chosen:
        await ctx.put_in_hand(chosen, reveal=True)


# ----------------------------------------------------------------------
# Tyrogue / Umbreon / Undersea Ruins / Victreebel / Vileplume
# ----------------------------------------------------------------------

def dark_moon_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    if pokemon is None:
        return False
    dark = PokemonTypes.DARKNESS.value
    if not any(energy_provides_type(e, dark)
               for e in board.attached_energies(pokemon)):
        return False
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    hand = board.find_player_area(opponent, "hand")
    return bool(hand and hand.children)


async def dark_moon(ctx):
    """Look at the opponent's hand; shuffle up to N cards into their deck,
    then they draw that many (N = Darkness Energy on Umbreon)."""
    dark = PokemonTypes.DARKNESS.value
    n = sum(1 for e in ctx.attached_energies(ctx.source)
            if energy_provides_type(e, dark))
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    if not hand or n <= 0:
        return
    picks = await ctx.choose_cards(
        hand, min(n, len(hand)), minimum=0,
        prompt="Choose cards to shuffle into your opponent's deck")
    if not picks:
        return
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    await ctx.draw_cards(len(picks), player_id=ctx.opponent_id)


def undersea_ruins_condition(board, player_id, stadium=None) -> bool:
    return any(devolvable(poked) for poked in board.pokemon_in_play(player_id))


async def undersea_ruins(ctx):
    """Flip: heads, discard the top Evolution card from 1 of your Evolved Pokémon."""
    results = await ctx.flip_coins(1, "Undersea Ruins")
    if not results or not results[0]:
        return
    evolved = [poked for poked in ctx.my_pokemon_in_play() if devolvable(poked)]
    if not evolved:
        return
    target = await ctx.choose_pokemon(
        evolved, "Choose an Evolved Pokémon to devolve")
    if target is not None:
        await ctx.devolve_pokemon(target, steps=1, destination="discard")


def fragrance_trap_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    return opponent is not None and _has_bench(board, opponent)


async def fragrance_trap(ctx):
    """Flip: heads, switch the Defending Pokémon with 1 of the opponent's Bench."""
    results = await ctx.flip_coins(1, "Fragrance Trap")
    if not results or not results[0]:
        return
    defender = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def addictive_pollen(ctx):
    """Printed damage; heads, the opponent can't play Supporters next turn."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Addictive Pollen")
    if results and results[0]:
        ctx.lock_plays(ctx.opponent_id, is_supporter_card)


# ----------------------------------------------------------------------
# Wooper — Deep Dive / Zapdos — Anti-Lightning / Lightning Storm
# ----------------------------------------------------------------------

async def deep_dive(ctx):
    """Flip 3 coins; heal 1 damage counter from this Pokémon per heads."""
    results = await ctx.flip_coins(3, "Deep Dive")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.heal(10 * heads, ctx.attacker)


class SlimePassive(Passive):
    """If an opposing attack would damage this Pokémon, the opponent flips:
    tails, prevent that damage (other effects still happen)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return None
        results = await ctx.flip_coins(1, "Slime", source=holder)
        if results and not results[0]:
            calc.prevented = True
            return 0
        return None


async def slime(ctx):
    """During the opponent's next turn, each attack that would damage this
    Pokémon makes the opponent flip; tails prevents the damage."""
    if ctx.attacker is None:
        return
    ctx.add_passive_through_opponents_turn(ctx.attacker, SlimePassive())


class AntiLightningPassive(Passive):
    """Can't attach Lightning Energy cards from hand to the holder."""

    def blocks_energy_attach(self, attaching_player_id, energy, target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return _typed_basic_energy(energy, PokemonTypes.LIGHTNING)


class AntiWaterPassive(Passive):
    """Can't attach Water Energy cards from hand to the holder."""

    def blocks_energy_attach(self, attaching_player_id, energy, target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return _typed_basic_energy(energy, PokemonTypes.WATER)


class AntiFirePassive(Passive):
    """Can't attach Fire Energy cards from hand to the holder."""

    def blocks_energy_attach(self, attaching_player_id, energy, target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return _typed_basic_energy(energy, PokemonTypes.FIRE)


async def lightning_storm(ctx):
    """Printed damage; tails puts 2 damage counters on Zapdos."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Lightning Storm")
    if results and not results[0]:
        await ctx.deal_damage(20, target=ctx.attacker, as_counters=True)


# ----------------------------------------------------------------------
# Steelix — Earth Rift / Iron Smash
# ----------------------------------------------------------------------

async def earth_rift(ctx):
    """Printed damage; 10 to each opposing Benched Pokémon; tails locks this attack."""
    await ctx.deal_damage()
    for poked in ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)
    results = await ctx.flip_coins(1, "Earth Rift")
    if results and not results[0]:
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id, ctx.ability.ability_id)


async def iron_smash(ctx):
    """Flip 2: both heads printed+20, mixed printed, both tails nothing."""
    results = await ctx.flip_coins(2, "Iron Smash")
    heads = sum(1 for result in results if result)
    if heads == 0:
        return
    bonus = 20 if heads == 2 else 0
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)


# ----------------------------------------------------------------------
# Sudowoodo / Togetic — Copy / Mini-Metronome
# ----------------------------------------------------------------------

def copyable_defending_attacks(board, copier, player_id,
                               require_energy: bool = True,
                               skip_requirements: bool = False) -> List:
    """(pokemon, attack) pairs from the opponent's Active the copier may use."""
    opponent = _opponent_id(board, player_id)
    if copier is None or opponent is None:
        return []
    defending = board.active_pokemon(opponent)
    if defending is None:
        return []
    energies = board.attached_energies(copier)
    pairs = []
    seen = set()
    definition = def_for(defending.archetype_id)
    attacks = [a for a in (getattr(definition, "abilities", None) or [])
               if isinstance(a, Attack)]
    attacks.extend(granted_extra_attacks(board, defending))
    for attack in attacks:
        key = attack.ability_id or (attack.title, attack.game_text)
        if key in seen:
            continue
        seen.add(key)
        if not skip_requirements:
            if attack.condition is not None \
                    and not attack.condition(board, player_id, copier):
                continue
            if require_energy:
                cost = effective_attack_cost(
                    board, copier, _cost_as_names(attack.cost))
                if not attack_cost_satisfied(cost, energies, board):
                    continue
        pairs.append((defending, attack))
    return pairs


def copy_defending_attack(require_energy: bool = True, flip: bool = False,
                          skip_requirements: bool = False):
    """Copy 1 of the Defending Pokémon's attacks (Sudowoodo Copy / Mini-Metronome).

    skip_requirements ignores Energy costs and other attack gates (Base Set
    Metronome: "except for its Energy costs and anything else required").
    """

    async def effect(ctx):
        if flip:
            results = await ctx.flip_coins(1, ctx.ability.title)
            if not results or not results[0]:
                return
        copier = ctx.attacker or ctx.source
        candidates = copyable_defending_attacks(
            ctx.board, copier, ctx.player_id, require_energy=require_energy,
            skip_requirements=skip_requirements)
        if not candidates:
            return
        picked = await ctx.choose_attack_to_copy(
            candidates, "Choose an attack to copy")
        if picked is None:
            return
        _, chosen = picked
        if not await ctx.use_attack(chosen):
            return
        if getattr(chosen, "locks_next_turn", False):
            attacker = ctx.attacker
            if attacker is None:
                return
            for entry in attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
                if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                    ctx.session.turn_state.lock_attack(
                        attacker.entity_id, entry["abilityID"])

    return effect


def copy_opponent_attack(require_energy: bool = True, flip: bool = False,
                         skip_requirements: bool = False):
    """Copy 1 attack from any of the opponent's Pokémon (Super Metronome).

    skip_requirements ignores Energy costs and other attack gates; with
    require_energy=False only the Energy cost is waived ("you must still do
    anything else in order to use that attack").
    """

    async def effect(ctx):
        if flip:
            results = await ctx.flip_coins(1, ctx.ability.title)
            if not results or not results[0]:
                return
        copier = ctx.attacker or ctx.source
        candidates = copyable_opponent_attacks(
            ctx.board, copier, ctx.player_id, require_energy=require_energy,
            skip_requirements=skip_requirements)
        if not candidates:
            return
        picked = await ctx.choose_attack_to_copy(
            candidates, "Choose an attack to copy")
        if picked is None:
            return
        _, chosen = picked
        if not await ctx.use_attack(chosen):
            return
        if getattr(chosen, "locks_next_turn", False):
            attacker = ctx.attacker
            if attacker is None:
                return
            for entry in attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
                if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                    ctx.session.turn_state.lock_attack(
                        attacker.entity_id, entry["abilityID"])

    return effect


super_metronome = copy_opponent_attack(require_energy=False, flip=True)


# ----------------------------------------------------------------------
# Tentacool — Recover
# ----------------------------------------------------------------------

def has_typed_basic_energy(energy_type: PokemonTypes, n: int = 1):
    """Attack condition: this Pokémon has at least `n` basic Energy cards of
    that type."""
    def check(board, player_id, pokemon=None) -> bool:
        if pokemon is None:
            return False
        return sum(1 for e in board.attached_energies(pokemon)
                   if _typed_basic_energy(e, energy_type)) >= n
    return check


def recover_discarding_energy(energy_type: PokemonTypes):
    """Discard 1 basic Energy of that type, then remove all damage counters."""
    type_name = CLIENT_POKEMON_TYPE_NAMES.get(energy_type, "Energy")

    async def effect(ctx):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c, t=energy_type: _typed_basic_energy(c, t),
            prompt=f"Choose a {type_name} Energy card to discard")
        if not discarded:
            return
        pokemon = ctx.attacker
        heal_amount = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if heal_amount > 0:
            await ctx.heal(heal_amount, pokemon)

    return effect


async def scavenge(ctx):
    """Discard 1 Psychic Energy card, then put a Trainer from discard into hand."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.PSYCHIC),
        prompt="Choose a Psychic Energy card to discard")
    if not discarded:
        return
    trainers = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1,
        prompt="Choose a Trainer card from your discard pile")
    if picks:
        await ctx.put_in_hand(picks)


async def spacing_out(ctx):
    """Flip: heads removes 1 damage counter from this Pokémon."""
    results = await ctx.flip_coins(1, "Spacing Out")
    if results and results[0]:
        await ctx.heal(10, ctx.attacker)


# ----------------------------------------------------------------------
# Tentacruel — Strange Tentacles
# ----------------------------------------------------------------------

def strange_tentacles_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    mine = board.active_pokemon(player_id)
    theirs = board.active_pokemon(opponent)
    if mine is None or theirs is None:
        return False
    if len(board.attached_energies(theirs)) >= len(board.attached_energies(mine)):
        return False
    discard = board.find_player_area(opponent, "discard")
    return any(is_energy_card(c) for c in (discard.children if discard else []))


async def strange_tentacles(ctx):
    """Attach 1 Energy from the opponent's discard pile to the Defending Pokémon."""
    pool = [c for c in ctx.discard_pile(ctx.opponent_id) if is_energy_card(c)]
    defending = ctx.opponent_active()
    if not pool or defending is None:
        return
    picks = await ctx.choose_cards(
        pool, 1, prompt="Choose an Energy card from your opponent's discard pile")
    if picks:
        await ctx.attach_energy(picks[0], defending)


# ----------------------------------------------------------------------
# Togepi — Minor Errand-Running
# ----------------------------------------------------------------------

def flip_search_basic_energy(coins: int = 2, title: str = ""):
    """Flip `coins`; for each heads, search a basic Energy into hand and show it."""
    async def effect(ctx):
        flip_title = title or (ctx.ability.title if ctx.ability else "")
        results = await ctx.flip_coins(coins, flip_title)
        heads = sum(1 for result in results if result)
        if heads <= 0:
            return
        picks = await ctx.search_deck(
            is_basic_energy_card, count=heads, minimum=0,
            prompt="Choose basic Energy cards to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


async def minor_errand_running(ctx):
    """Flip 2; for each heads, search a basic Energy into hand."""
    await flip_search_basic_energy(2, "Minor Errand-Running")(ctx)


energy_ark = flip_search_basic_energy(2, "Energy Ark")


# ----------------------------------------------------------------------
# Togetic — Miracle Shift
# ----------------------------------------------------------------------

def miracle_shift_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return any(
        is_basic_energy_card(e)
        for poked in board.pokemon_in_play(player_id)
        for e in board.attached_energies(poked)
    )


async def miracle_shift(ctx):
    """Discard a basic Energy from 1 of your Pokémon; attach a basic Energy from discard to it."""
    holders = [
        poked for poked in ctx.my_pokemon_in_play()
        if any(is_basic_energy_card(e) for e in ctx.attached_energies(poked))
    ]
    if not holders:
        return
    pokemon = await ctx.choose_pokemon(
        holders, "Choose a Pokémon with a basic Energy card attached")
    if pokemon is None:
        return
    basics = [e for e in ctx.attached_energies(pokemon) if is_basic_energy_card(e)]
    picks = await ctx.choose_cards(
        basics, 1, prompt="Choose a basic Energy card to discard")
    if not picks:
        return
    await ctx.discard_cards(picks)
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not pool:
        return
    chosen = await ctx.choose_cards(
        pool, 1, minimum=1,
        prompt="Choose a basic Energy card from your discard pile to attach")
    if chosen:
        await ctx.attach_energy(chosen[0], pokemon)


# ----------------------------------------------------------------------
# Super Energy Removal 2
# ----------------------------------------------------------------------

async def super_energy_removal_2(ctx):
    """Flip 2: both heads strip the Defending, both tails strip your Active."""
    results = await ctx.flip_coins(2, "Super Energy Removal 2")
    heads = sum(1 for result in results if result)
    if heads == 2:
        target = ctx.opponent_active()
    elif heads == 0:
        target = ctx.my_active()
    else:
        return
    if target is None:
        return
    energies = ctx.attached_energies(target)
    if energies:
        await ctx.discard_energy_from(target, len(energies))


# ----------------------------------------------------------------------
# Town Volunteers
# ----------------------------------------------------------------------

async def town_volunteers(ctx):
    """Shuffle up to 5 Baby/Basic/Evolution/basic Energy from discard into deck."""
    cards = [c for c in ctx.discard_pile() if is_pokemon_or_basic_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 5, minimum=1,
        prompt="Choose up to 5 Baby Pokémon, Basic Pokémon, Evolution, and/or basic Energy cards")
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks)


# ----------------------------------------------------------------------
# Tyranitar — Destructive Roar / Gigacrush
# ----------------------------------------------------------------------

async def destructive_roar(ctx):
    """Flip: heads, discard 1 Energy from 1 of the opponent's Pokémon."""
    results = await ctx.flip_coins(1, "Destructive Roar")
    if not results or not results[0]:
        return
    candidates = [poked for poked in ctx.opponent_pokemon_in_play()
                  if ctx.attached_energies(poked)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon")
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose an Energy card to discard")


async def gigacrush(ctx):
    """Printed damage; each player discards the top 3 cards of their deck."""
    await ctx.deal_damage()
    await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))
    await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.player_id))


# ----------------------------------------------------------------------
# Friend Ball
# ----------------------------------------------------------------------

async def friend_ball(ctx):
    """Search the deck for a Pokémon matching a chosen opposing Pokémon's type."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    chosen = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if chosen is None:
        return
    types = set(effective_pokemon_types(ctx.board, chosen))

    def pred(card):
        if not is_pokemon_card(card):
            return False
        return bool(types & set(card.get_attribute(AttrID.POKEMON_TYPES) or []))

    found = await ctx.search_deck(
        pred, count=1, minimum=0,
        prompt="Choose a Baby Pokémon, Basic Pokémon, or Evolution card of the same type.",
    )
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Gengar — Manipulate
# ----------------------------------------------------------------------

async def manipulate(ctx):
    """ON_EVOLVE (Active): bench a Basic non-Baby from discard; attach 1 basic
    Energy from discard to it per heads among 3 coins."""
    if ctx.source is not ctx.my_active():
        return
    basics = [c for c in ctx.discard_pile() if is_basic_non_baby(c)]
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    space = (effective_bench_capacity(ctx.board, ctx.player_id)
             - (len(bench.children) if bench else 0))
    if not basics or space <= 0:
        return
    if not await ctx.ask_yes_no(
            "Put a Basic Pokémon (excluding Baby Pokémon) from your discard "
            "pile onto your Bench?"):
        return
    picks = await ctx.choose_cards(
        basics, 1, prompt="Choose a Basic Pokémon to put onto your Bench")
    if not picks:
        return
    benched = picks[0]
    if not await ctx.bench_pokemon(benched):
        return
    results = await ctx.flip_coins(3, "Manipulate")
    heads = sum(1 for result in results if result)
    for _ in range(heads):
        energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not energy:
            break
        chosen = await ctx.choose_cards(
            energy, 1,
            prompt="Choose a basic Energy card to attach to that Pokémon")
        if not chosen:
            break
        await ctx.attach_energy(chosen[0], benched)


# ----------------------------------------------------------------------
# Golbat — Strength in Numbers
# ----------------------------------------------------------------------

_ZUBAT_LINE = frozenset(("Zubat", "Golbat", "Crobat"))


def _zubat_line_on_bench(ctx) -> int:
    return sum(
        1 for poked in ctx.my_bench()
        if poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _ZUBAT_LINE
    )


strength_in_numbers = damage_per(_zubat_line_on_bench, 10, base=30)


# ----------------------------------------------------------------------
# Gyarados — Flame Vapor
# ----------------------------------------------------------------------

async def flame_vapor(ctx):
    """ON_EVOLVE (Active): you may flip 2 coins; discard 1 Energy from the
    Defending Pokémon per heads."""
    if ctx.source is not ctx.my_active():
        return
    if not await ctx.ask_yes_no(
            "Flip 2 coins and discard an Energy card from the Defending "
            "Pokémon for each heads?"):
        return
    results = await ctx.flip_coins(2, "Flame Vapor")
    heads = sum(1 for result in results if result)
    if not heads:
        return
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(
        defender, heads,
        prompt="Choose Energy to discard from the Defending Pokémon")


# ----------------------------------------------------------------------
# Ho-oh — Scalding Steam
# ----------------------------------------------------------------------

async def scalding_steam(ctx):
    """Printed damage; discard 1 Energy from self; heads Burns the Defending."""
    await ctx.deal_damage()
    if ctx.attached_energies(ctx.attacker):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Choose an Energy card to discard from Ho-oh")
    results = await ctx.flip_coins(1, "Scalding Steam")
    if results and results[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


# ----------------------------------------------------------------------
# Houndoom — Lonely Fang
# ----------------------------------------------------------------------

async def lonely_fang(ctx):
    """Printed + 20 for each of the opponent's Benched Pokémon beyond yours."""
    extra = max(0, len(ctx.opponent_bench()) - len(ctx.my_bench()))
    base = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(base + 20 * extra)


# ----------------------------------------------------------------------
# Abra — Psychoflow
# ----------------------------------------------------------------------

class PsychoflowPassive(Passive):
    """Retreat cost is 0 while a Psychic Energy card is attached."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if any(_typed_basic_energy(energy, PokemonTypes.PSYCHIC)
               for energy in board.attached_energies(pokemon)):
            return 0
        return cost


# ----------------------------------------------------------------------
# Aerodactyl — Ancient Wind
# ----------------------------------------------------------------------

class IgnorePokeBodiesPassive(Passive):
    """All Poké-Bodies are ignored while this temp passive is in play."""

    ignores_poke_bodies = True


ancient_wind_condition = all_conditions(no_special_conditions, is_active)


async def ancient_wind(ctx):
    """Ignore all Poké-Bodies until the end of this turn."""
    ctx.add_temporary_passive(
        ctx.source, IgnorePokeBodiesPassive(),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


# ----------------------------------------------------------------------
# Alakazam — Energy Jump
# ----------------------------------------------------------------------

def energy_jump_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    in_play = list(board.pokemon_in_play(player_id))
    if len(in_play) < 2:
        return False
    return any(board.attached_energies(poked) for poked in in_play)


async def energy_jump(ctx):
    """Move 1 Energy card from 1 of your Pokémon to another."""
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(pokemon, pokemon, max_count=1)


# ----------------------------------------------------------------------
# Ancient Ruins
# ----------------------------------------------------------------------

def ancient_ruins_condition(board, player_id, stadium=None) -> bool:
    state = getattr(board, "turn_state", None)
    return state is None or not state.supporter_played


async def ancient_ruins(ctx):
    """If no Supporter was played this turn, reveal your hand; draw 1 if none."""
    if ctx.session.turn_state.supporter_played:
        return
    await ctx.reveal_hand(of_player=ctx.player_id, to_player=ctx.opponent_id)
    if any(is_supporter_card(card) for card in ctx.hand()):
        return
    await ctx.draw_cards(1)


# ----------------------------------------------------------------------
# Apricorn Maker
# ----------------------------------------------------------------------

def is_ball_trainer(card) -> bool:
    """Trainer card whose display name contains 'Ball'."""
    if not is_trainer_card(card):
        return False
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return bool(definition and "ball" in (definition.display_name or "").lower())


def is_stadium_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


def is_supporter_or_stadium(card) -> bool:
    """Relic Hunter: up to 2 Supporter and/or Stadium cards."""
    return is_supporter_card(card) or is_stadium_card(card)


# ----------------------------------------------------------------------
# Arcanine — Energy Recharge / Shake
# ----------------------------------------------------------------------

async def energy_recharge(ctx):
    """ON_EVOLVE (Active): you may flip 3 coins; attach 1 basic Energy from
    discard per heads."""
    if ctx.source is not ctx.my_active():
        return
    if not await ctx.ask_yes_no(
            "Flip 3 coins and attach a basic Energy card from your discard "
            "pile to Arcanine for each heads?"):
        return
    results = await ctx.flip_coins(3, "Energy Recharge")
    heads = sum(1 for result in results if result)
    if not heads:
        return
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    take = min(heads, len(energy))
    picks = await ctx.choose_cards(
        energy, take, minimum=take,
        prompt="Choose basic Energy cards to attach to Arcanine")
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


async def shake(ctx):
    """Printed damage; opponent switches the Defending Pokémon."""
    await ctx.deal_damage()
    await opponent_switches(ctx)


# ----------------------------------------------------------------------
# Articuno — Ice Cyclone
# ----------------------------------------------------------------------

async def ice_cyclone(ctx):
    """Printed damage; heads 10 to each opposing Bench, tails 10 to each of
    your Pokémon in play (no W/R on Benched Pokémon)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Ice Cyclone")
    heads = bool(results and results[0])
    if heads:
        for poked in ctx.opponent_bench():
            await ctx.deal_damage(10, target=poked, apply_modifiers=False)
        return
    for poked in ctx.my_pokemon_in_play():
        if poked is ctx.attacker:
            await ctx.deal_damage(10, target=poked)
        else:
            await ctx.deal_damage(10, target=poked, apply_modifiers=False)


# ----------------------------------------------------------------------
# Beedrill — Venom Spray / Needle Rush
# ----------------------------------------------------------------------

async def venom_spray(ctx):
    """ON_EVOLVE (Active): the Defending Pokémon is Paralyzed and Poisoned."""
    if ctx.source is not ctx.my_active():
        return
    await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)
    await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.POISONED)


_NEEDLE_RUSH_BONUS = {0: 0, 1: 10, 2: 20, 3: 50, 4: 90}


async def needle_rush(ctx):
    """Flip 4; +10 / +20 / +50 / +90 for 1 / 2 / 3 / 4 heads."""
    results = await ctx.flip_coins(4, "Needle Rush")
    heads = sum(1 for result in results if result)
    await ctx.deal_damage(10 + _NEEDLE_RUSH_BONUS.get(heads, 0))


# ----------------------------------------------------------------------
# Bounce Energy
# ----------------------------------------------------------------------

def bounce_energy_attach_to(pokemon) -> bool:
    """Attach only to a Pokémon that already has a basic Energy card."""
    return any(is_basic_energy_card(child) for child in pokemon.children)


async def bounce_energy_on_attach(ctx):
    """Return 1 basic Energy attached to the Pokémon to your hand."""
    target = ctx.attached_to
    if target is None:
        return
    basic = [energy for energy in ctx.attached_energies(target)
             if is_basic_energy_card(energy)]
    if not basic:
        return
    picks = await ctx.choose_cards(
        basic, 1, prompt="Choose a basic Energy card to return to your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


# ----------------------------------------------------------------------
# Buried Fossil — Reconstruction
# ----------------------------------------------------------------------

_FOSSIL_EVOS = frozenset(("Omanyte", "Kabuto"))


def reconstruction_condition(board, player_id, pokemon=None) -> bool:
    return has_basic_energy_in_hand(board, player_id)


async def reconstruction(ctx):
    """Search for Omanyte or Kabuto, then put a basic Energy from hand into deck."""
    found = await ctx.search_deck(
        lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _FOSSIL_EVOS,
        count=1, minimum=0,
        prompt="Choose an Omanyte or Kabuto card.",
    )
    if found:
        await ctx.put_in_hand(found, reveal=True)
    energy = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if energy:
        picks = await ctx.choose_cards(
            energy, 1, minimum=1,
            prompt="Choose a basic Energy card to put into your deck")
        if picks:
            await ctx.shuffle_into_deck(picks)
            return
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Celebi — Empathic Healing
# ----------------------------------------------------------------------

async def empathic_healing(ctx):
    """Remove 2 damage counters from Celebi and each Pokémon of the same type."""
    types = set(effective_pokemon_types(ctx.board, ctx.attacker))
    for poked in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
        if poked is ctx.attacker or types & set(effective_pokemon_types(ctx.board, poked)):
            await ctx.heal(20, poked)


# ----------------------------------------------------------------------
# Crobat — Carry Off / Double Cross
# ----------------------------------------------------------------------

carry_off_condition = no_special_conditions


async def carry_off(ctx):
    """Flip: heads, look at the opponent's hand and shuffle 1 Pokémon into deck."""
    results = await ctx.flip_coins(1, "Carry Off")
    if not results or not results[0]:
        return
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    matches = [c for c in hand if is_pokemon_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1,
        prompt="Choose a Pokémon card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def double_cross(ctx):
    """Flip 2; 40× heads. Both tails: Confused and Poisoned."""
    results = await ctx.flip_coins(2, "Double Cross")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(40 * heads)
    if heads == 0:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


# ----------------------------------------------------------------------
# Crystal Shard
# ----------------------------------------------------------------------

class CrystalShardPassive(Passive):
    """Attached Pokémon's type is Colorless."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        return [PokemonTypes.COLORLESS.value]


# ----------------------------------------------------------------------
# Cyclone Energy
# ----------------------------------------------------------------------

async def cyclone_energy_on_attach(ctx):
    """When attached from hand to the Active, the opponent switches theirs."""
    target = ctx.attached_to
    if target is None or target is not ctx.my_active():
        return
    await opponent_switches(ctx)


# ----------------------------------------------------------------------
# Ditto — Prismatic Body
# ----------------------------------------------------------------------

class PrismaticBodyPassive(Passive):
    """Each basic Energy attached to the carrier provides every type, 1 at a time."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or not is_basic_energy_card(energy):
            return options
        mine = any(
            isinstance(passive, PrismaticBodyPassive)
            and carrier_pokemon(carrier) is holder
            for passive, carrier in _active_passives(board)
        )
        if not mine:
            return options
        return [[getattr(t, "value", t) for t in option]
                for option in ALL_TYPES_ONE_AT_A_TIME]


# ----------------------------------------------------------------------
# Dunsparce — Slippery Skin
# ----------------------------------------------------------------------

class SlipperySkinPassive(Passive):
    """Retreat cost is 0 while the opponent's Active is an Evolved Pokémon."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        opponent = _opponent_id(board, pokemon.owning_player_id)
        if opponent is None:
            return cost
        defending = board.active_pokemon(opponent)
        if defending is not None and is_evolved_pokemon(defending):
            return 0
        return cost


# ----------------------------------------------------------------------
# Flareon / Jolteon / Vaporeon — Self-healing
# ----------------------------------------------------------------------

def self_healing_on_energy_attached(energy_type: PokemonTypes):
    """ON_ENERGY_ATTACHED: attaching that basic Energy from hand cures conditions."""

    async def watch(ctx):
        if ctx.energy_receiver is not ctx.source:
            return
        if ctx.attaching_player_id != ctx.player_id:
            return
        energy = ctx.attached_energy
        if energy is None or not _typed_basic_energy(energy, energy_type):
            return
        await ctx.cure_all_conditions(ctx.source)

    return watch


def has_attached_energy(board, player_id, pokemon=None) -> bool:
    """Attack condition: this Pokémon has at least 1 Energy attached."""
    if pokemon is None:
        return False
    return bool(board.attached_energies(pokemon))


async def burn_booster(ctx):
    """Discard 1 Energy to attack; +10 if the discarded card is basic Fire."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        prompt="Choose an Energy card to discard from Flareon")
    if not discarded:
        return
    bonus = 10 if _typed_basic_energy(discarded[0], PokemonTypes.FIRE) else 0
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)


# ----------------------------------------------------------------------
# Dewgong — Freeze Lock / Crushing Ice
# ----------------------------------------------------------------------

async def freeze_lock(ctx):
    """Printed damage; heads, opponent can't attach Energy to the Defending
    Pokémon during their next turn."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Freeze Lock")
    defender = ctx.defender
    if results and results[0] and defender is not None \
            and not ctx.effects_blocked(defender):
        ctx.restrict_attachments(defender)


async def crushing_ice(ctx):
    """Printed + 10 per Colorless in the Defending Pokémon's effective Retreat Cost."""
    n = 0
    if ctx.defender is not None:
        n = effective_retreat_cost(ctx.board, ctx.defender)
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + 10 * n)


# ----------------------------------------------------------------------
# Electrode — Selfdestruct
# ----------------------------------------------------------------------

def selfdestruct_attack(bench_damage: int = 20, self_damage: int = 100):
    """Printed damage; `bench_damage` to each Benched Pokémon (both sides);
    then `self_damage` to the attacker (no W/R)."""

    async def effect(ctx):
        await ctx.deal_damage()
        if bench_damage:
            for poked in ctx.my_bench() + ctx.opponent_bench():
                await ctx.deal_damage(bench_damage, target=poked)
        if self_damage:
            await ctx.deal_damage(
                self_damage, target=ctx.attacker, apply_modifiers=False)

    return effect


# ----------------------------------------------------------------------
# Forretress (Metal) — Spinning Blow / Scatterbomb
# ----------------------------------------------------------------------

async def spinning_blow(ctx):
    """20× heads among 2 coins; both heads switches this Pokémon with a Bench Pokémon."""
    results = await ctx.flip_coins(2, "Spinning Blow")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(20 * heads)
    if heads < 2:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def scatterbomb(ctx):
    """Printed damage; 2 coins: 10×heads to each opposing Bench, 10×tails to own Bench."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Scatterbomb")
    heads = sum(1 for result in results if result)
    tails = len(results) - heads
    if heads:
        for poked in ctx.opponent_bench():
            await ctx.deal_damage(10 * heads, target=poked)
    if tails:
        for poked in ctx.my_bench():
            await ctx.deal_damage(10 * tails, target=poked)


# ----------------------------------------------------------------------
# Desert Shaman / Fast Ball / Fisherman
# ----------------------------------------------------------------------

async def desert_shaman(ctx):
    """Shuffle your hand into your deck and draw up to 4; the opponent does the same."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    n = await ctx.choose(
        "Draw up to 4 cards.",
        [str(i) for i in range(5)],
        use_panel=False,
    )
    if n > 0:
        await ctx.draw_cards(n)
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    n = await ctx.choose(
        "Draw up to 4 cards.",
        [str(i) for i in range(5)],
        player_id=ctx.opponent_id,
        use_panel=False,
    )
    if n > 0:
        await ctx.draw_cards(n, ctx.opponent_id)


async def fast_ball(ctx):
    """Reveal deck cards until an Evolution; put it into hand and shuffle the rest."""
    deck = ctx.deck()
    if not deck:
        return
    revealed = []
    found = None
    for card in ctx.deck_top(len(deck)):
        revealed.append(card)
        if is_evolution_pokemon(card):
            found = card
            break
    if revealed:
        await ctx.reveal_cards(revealed)
    if found:
        await ctx.put_in_hand([found], reveal=False)
    await ctx.shuffle_deck()


async def fisherman(ctx):
    """Put 4 basic Energy from discard into hand (or all, if fewer)."""
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not cards:
        return
    take = min(4, len(cards))
    picks = await ctx.choose_cards(
        cards, take, minimum=take,
        prompt="Choose basic Energy cards to put into your hand")
    await ctx.put_in_hand(picks, reveal=True)


# ----------------------------------------------------------------------
# Igglybuff — Energy Heal
# ----------------------------------------------------------------------

async def energy_heal(ctx):
    """Choose 1 of your Pokémon with Energy attached; remove 1 damage counter."""
    candidates = [poked for poked in ctx.my_pokemon_in_play()
                  if ctx.attached_energies(poked)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokémon with an Energy card attached to it")
    if target is not None:
        await ctx.heal(10, target)


# ----------------------------------------------------------------------
# Jolteon — Thunderspark
# ----------------------------------------------------------------------

async def thunderspark(ctx):
    """Printed damage; 10 to each Benched Pokémon (both sides) that has Energy."""
    await ctx.deal_damage()
    for poked in ctx.my_bench() + ctx.opponent_bench():
        if ctx.attached_energies(poked):
            await ctx.deal_damage(10, target=poked)


# ----------------------------------------------------------------------
# Kabutops — Primal Aura
# ----------------------------------------------------------------------

class PrimalAuraPassive(Passive):
    """While Active, neither player can evolve Benched Pokémon from hand."""

    def blocks_evolution(self, player_id, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if not is_in_active_spot(holder):
            return False
        return not is_in_active_spot(target)


# ----------------------------------------------------------------------
# Ledian — Pollen Shield
# ----------------------------------------------------------------------

async def pollen_shield(ctx):
    """Printed damage; immune to Special Conditions during the opponent's next turn."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, condition_immunity_passive())


# ----------------------------------------------------------------------
# Lure Ball
# ----------------------------------------------------------------------

async def lure_ball(ctx):
    """Flip 3 coins; put that many Evolution cards from discard into hand."""
    results = await ctx.flip_coins(3, "Lure Ball")
    heads = sum(1 for result in results if result)
    if not heads:
        return
    cards = [c for c in ctx.discard_pile() if is_evolution_pokemon(c)]
    if not cards:
        return
    take = min(heads, len(cards))
    picks = await ctx.choose_cards(
        cards, take, minimum=take,
        prompt="Choose Evolution cards to put into your hand")
    await ctx.put_in_hand(picks, reveal=True)


# ----------------------------------------------------------------------
# Machamp — Drag Off
# ----------------------------------------------------------------------

async def drag_off(ctx):
    """Before damage, switch a chosen opposing Benched Pokémon into Active."""
    old_active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old_active is not None and bench and not ctx.effects_blocked(old_active):
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon") or bench[0]
        await ctx.switch_active(ctx.opponent_id, target)
    await ctx.deal_damage()


async def optional_drag_off(ctx):
    """Before damage, you may switch a Benched Pokémon with the Defending."""
    old_active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old_active is not None and bench and not ctx.effects_blocked(old_active):
        target = await ctx.choose_pokemon(
            bench, "You may choose a Benched Pokémon to switch into the Active Spot",
            optional=True,
        )
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
    await ctx.deal_damage()


# ----------------------------------------------------------------------
# Mystery Plates
# ----------------------------------------------------------------------

def _prize_count(ctx, player_id=None) -> int:
    pid = player_id if player_id is not None else ctx.opponent_id
    area = ctx.board.find_player_area(pid, "prizePile")
    return len(area.children) if area else 0


async def mystery_plate_beta(ctx):
    """Stone Crush: 5+ Prizes draws 3; 1 Prize shuffles 2 Energy into the deck."""
    remaining = _prize_count(ctx)
    if remaining >= 5:
        await ctx.draw_cards(3)
        return
    if remaining != 1:
        return
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    take = min(2, len(energies))
    picks = await ctx.choose_cards(
        energies, take, minimum=take,
        prompt="Choose Energy cards to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def mystery_plate_gamma(ctx):
    """Retro Cave: 5+ Prizes refreshes the hand to 6; exactly 2 devolves one."""
    remaining = _prize_count(ctx)
    if remaining >= 5:
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        await ctx.draw_cards(6)
        return
    if remaining != 2:
        return
    evolved = [poked for poked in ctx.opponent_pokemon_in_play()
               if devolvable(poked) and not ctx.effects_blocked(poked)]
    if not evolved:
        return
    target = await ctx.choose_pokemon(
        evolved, "Choose 1 of your opponent's Evolved Pokémon")
    if target is None:
        return
    removed = await ctx.devolve_pokemon(target, steps=1, destination="deck")
    for card in removed:
        await ctx.put_on_bottom_of_deck(card)


async def mystery_plate_delta(ctx):
    """Healing Oasis: 5+ Prizes searches 3 basic Energy; exactly 2 heals one."""
    remaining = _prize_count(ctx)
    if remaining >= 5:
        picks = await ctx.search_deck(
            is_basic_energy_card, count=3, minimum=0,
            prompt="Choose up to 3 basic Energy cards.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        return
    if remaining != 2:
        return
    damaged = [poked for poked in ctx.my_pokemon_in_play()
               if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to remove all damage from")
    if target is None:
        return
    amount = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
    if amount > 0:
        await ctx.heal(amount, target)


# ----------------------------------------------------------------------
# Mystery Zone
# ----------------------------------------------------------------------

def mystery_zone_condition(board, player_id, stadium=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_evolution_pokemon(c) for c in hand.children)


async def mystery_zone(ctx):
    """Search a basic Energy into hand, then put an Evolution from hand into the deck."""
    picks = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    evolutions = [c for c in ctx.hand() if is_evolution_pokemon(c)]
    if evolutions:
        chosen = await ctx.choose_cards(
            evolutions, 1, minimum=1,
            prompt="Choose an Evolution card to put into your deck")
        if chosen:
            await ctx.reveal_cards(chosen)
            await ctx.shuffle_into_deck(chosen)
            return
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Natu — Foresight / Removal Beam
# ----------------------------------------------------------------------

async def rearrange_deck_top(ctx, count: int, player_id=None):
    """Look at the top `count` of a deck and put them back in any order."""
    pid = player_id or ctx.player_id
    top = ctx.deck_top(count, pid)
    if not top:
        return
    if len(top) == 1:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, list(top),
            prompt="Top card of the deck",
        )
        return
    picks = await ctx.choose_cards(
        top, len(top), minimum=len(top), ordered=True,
        prompt="Put these cards back on top of the deck, in order.",
    )
    for card in picks:
        await ctx.put_on_top_of_deck(card)


async def foresight(ctx, count: int = 3):
    """Look at the top `count` of either player's deck and rearrange them."""
    options = []
    labels = []
    if ctx.deck():
        options.append(ctx.player_id)
        labels.append("Your deck")
    if ctx.deck(ctx.opponent_id):
        options.append(ctx.opponent_id)
        labels.append("Opponent's deck")
    if not options:
        return
    idx = 0 if len(options) == 1 else await ctx.choose(
        "Choose a deck to look at.", labels)
    await rearrange_deck_top(ctx, count, options[idx])


async def removal_beam(ctx):
    """Printed damage; if Energy is attached, heads discards one Energy card."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    if not ctx.attached_energies(defender):
        return
    results = await ctx.flip_coins(1, "Removal Beam")
    if results and results[0]:
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose an Energy card to discard from the Defending Pokémon")


# ----------------------------------------------------------------------
# Nidoqueen — Evolution Helper
# ----------------------------------------------------------------------

def evolution_helper_condition(board, player_id, pokemon=None) -> bool:
    if not is_benched(board, player_id, pokemon):
        return False
    if board.active_pokemon(player_id) is None:
        return False
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def evolution_helper(ctx):
    """Search the deck for a card that evolves from the Active and evolve it."""
    active = ctx.my_active()
    if active is None:
        return
    logic_name = active.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda c, name=logic_name: bool(name)
        and c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0,
        prompt="Choose a card that evolves from your Active Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(active, picks[0])
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Nidoran — Call for Family
# ----------------------------------------------------------------------

def is_nidoran_basic(card) -> bool:
    if not is_basic_pokemon(card):
        return False
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return name.startswith("Nidoran")


# ----------------------------------------------------------------------
# Noctowl — Investigate
# ----------------------------------------------------------------------

async def _look_at_prizes(ctx, player_id, count: int = 2):
    """Pick up to `count` face-down Prizes, look at them, then re-hide."""
    session = ctx.session
    prize_area = ctx.board.find_player_area(player_id, "prizePile")
    prizes = list(prize_area.children) if prize_area else []
    if not prizes:
        return
    take = min(count, len(prizes))
    picked_ids = await session._prompt_prize_pick(
        ctx.player_id, [c.entity_id for c in prizes], take,
        prompt="Choose Prize cards to look at.",
        minimum=0,
        prize_area=prize_area,
    )
    picked = [ctx.board.get_entity(eid) for eid in picked_ids]
    picked = [card for card in picked if card is not None]
    if not picked:
        return
    viewer = session.players.get(ctx.player_id)
    if viewer is not None:
        intros = [session._entity_introduced_msg(card) for card in picked]
        if intros:
            await session.send_game_sequence(
                [viewer], GameSequence.SERIAL_SEQUENCE, intros)
    await session.prompt_view_cards(
        ctx.player_id, ctx.source.entity_id, picked,
        prompt="Looked-at Prize cards",
    )
    if viewer is not None:
        resets = [session._attributes_reset_msg(card.entity_id) for card in picked]
        if resets:
            await session.send_game_sequence(
                [viewer], GameSequence.GROUPED_MOVE, resets)


async def investigate(ctx):
    """Look at the top 2 of any deck, or up to 2 of any player's Prizes."""
    options = []
    labels = []
    if ctx.deck():
        options.append(("deck", ctx.player_id))
        labels.append("Your deck")
    if ctx.deck(ctx.opponent_id):
        options.append(("deck", ctx.opponent_id))
        labels.append("Opponent's deck")
    my_prizes = ctx.board.find_player_area(ctx.player_id, "prizePile")
    if my_prizes and my_prizes.children:
        options.append(("prizes", ctx.player_id))
        labels.append("Your Prizes")
    opp_prizes = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
    if opp_prizes and opp_prizes.children:
        options.append(("prizes", ctx.opponent_id))
        labels.append("Opponent's Prizes")
    if not options:
        return
    idx = 0 if len(options) == 1 else await ctx.choose("Investigate", labels)
    kind, pid = options[idx]
    if kind == "deck":
        top = ctx.deck_top(2, pid)
        if top:
            await ctx.session.prompt_view_cards(
                ctx.player_id, ctx.source.entity_id, list(top),
                prompt="Top cards of the deck",
            )
        return
    await _look_at_prizes(ctx, pid, 2)


# ----------------------------------------------------------------------
# Omanyte — Water of Evolution
# ----------------------------------------------------------------------

def evolve_from_hand(display_name: str):
    """Put a named Evolution from hand onto the attacker (counts as evolving)."""
    async def effect(ctx):
        pokemon = ctx.attacker or ctx.source
        if pokemon is None:
            return
        candidates = [
            card for card in ctx.hand()
            if getattr(def_for(card.archetype_id), "display_name", None) == display_name
        ]
        if not candidates:
            return
        picks = await ctx.choose_cards(
            candidates, 1, minimum=1,
            prompt=f"Choose a {display_name} to evolve this Pokémon",
        )
        if picks:
            await ctx.evolve_pokemon(pokemon, picks[0])
    return effect


# ----------------------------------------------------------------------
# Omastar — Primal Stare
# ----------------------------------------------------------------------

class PrimalStarePassive(Passive):
    """While Active, the opponent can't evolve their Active Pokémon from hand."""

    def blocks_evolution(self, player_id, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if not is_in_active_spot(holder):
            return False
        if player_id == holder.owning_player_id:
            return False
        return is_in_active_spot(target)


# ----------------------------------------------------------------------
# Oracle
# ----------------------------------------------------------------------

async def oracle(ctx):
    """Choose 2 deck cards, shuffle the rest, put the chosen cards on top."""
    deck = ctx.deck()
    take = min(2, len(deck))
    if take <= 0:
        return
    picks = await ctx.search_deck(
        None, count=take, minimum=take,
        prompt="Choose 2 cards to put on top of your deck.",
    )
    await ctx.shuffle_deck()
    if len(picks) > 1:
        picks = await ctx.choose_cards(
            picks, len(picks), minimum=len(picks), ordered=True,
            prompt="Put these cards on top of your deck, in order.",
        )
    for card in picks:
        await ctx.put_on_top_of_deck(card)


# ----------------------------------------------------------------------
# Persian — Surprise Slash
# ----------------------------------------------------------------------

async def surprise_slash(ctx):
    """Printed damage; heads looks at the hand and shuffles a Trainer into the deck."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Surprise Slash")
    if not results or not results[0]:
        return
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    trainers = [card for card in hand if is_trainer_card(card)]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1,
        prompt="Choose a Trainer card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


# ----------------------------------------------------------------------
# Pikachu — Max Voltage
# ----------------------------------------------------------------------

async def max_voltage(ctx):
    """Discard all Lightning Energy cards; 20 plus 10 per discarded card."""
    lightning = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    await ctx.discard_cards(lightning)
    await ctx.deal_damage(20 + 10 * len(lightning))


# ----------------------------------------------------------------------
# Piloswine — Trample
# ----------------------------------------------------------------------

def trample(bench_damage: int = 20):
    """Printed damage; for each Benched Pokémon, heads deals `bench_damage`
    with no Weakness or Resistance (Piloswine 20 / Tyranitar 30)."""

    async def effect(ctx):
        await ctx.deal_damage()
        benched = list(ctx.my_bench()) + list(ctx.opponent_bench())
        if not benched:
            return
        results = await ctx.flip_coins(
            len(benched), ctx.ability.title if ctx.ability else "Trample")
        for poked, heads in zip(benched, results):
            if heads:
                await ctx.deal_damage(
                    bench_damage, target=poked, apply_modifiers=False)

    return effect


async def thunderstorm(ctx):
    """Printed damage; per opposing Bench Pokémon, heads deals 20 to it, then
    10×tails self-damage (no W/R)."""
    await ctx.deal_damage()
    bench = list(ctx.opponent_bench())
    if not bench:
        return
    results = await ctx.flip_coins(len(bench), "Thunderstorm")
    tails = 0
    for poked, heads in zip(bench, results):
        if heads:
            await ctx.deal_damage(20, target=poked)
        else:
            tails += 1
    if tails:
        await ctx.deal_damage(
            10 * tails, target=ctx.attacker, apply_modifiers=False)


async def continuous_charge(ctx):
    """Flip 4: printed +20 per heads; put a damage counter on self per heads."""
    results = await ctx.flip_coins(4, "Continuous Charge")
    heads = sum(1 for result in results if result)
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + 20 * heads)
    if heads:
        await ctx.deal_damage(10 * heads, target=ctx.attacker, as_counters=True)



# ----------------------------------------------------------------------
# Magcargo (Fire) — Eruption / Fire Stream
# ----------------------------------------------------------------------

async def eruption(ctx):
    """Each player mills 1; 20 + 20 per Fire Energy card discarded that way."""
    milled = ctx.deck_top(1) + ctx.deck_top(1, player_id=ctx.opponent_id)
    await ctx.discard_cards(milled)
    extra = sum(1 for c in milled if _typed_basic_energy(c, PokemonTypes.FIRE))
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + 20 * extra)


async def fire_stream(ctx):
    """Discard 1 Fire Energy card, printed damage, 10 to each opposing Bench."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        prompt="Choose a Fire Energy card to discard from Magcargo")
    if not discarded:
        return
    await ctx.deal_damage()
    for poked in ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)


# ----------------------------------------------------------------------
# Magcargo (Fighting) — Streaming Mantle / Crushing Lava
# ----------------------------------------------------------------------

async def _mill_then_recycle_energy(ctx, player_id, mill_count=3, recycle=3):
    await ctx.discard_cards(ctx.deck_top(mill_count, player_id=player_id))
    energy = [c for c in ctx.discard_pile(player_id) if is_basic_energy_card(c)]
    if not energy:
        return
    take = min(recycle, len(energy))
    picks = await ctx.choose_cards(
        energy, take, minimum=take, player_id=player_id,
        prompt="Choose basic Energy cards to shuffle into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, player_id)


async def streaming_mantle(ctx):
    """ON_EVOLVE (Active): you may mill 3 then shuffle 3 basic Energy from
    discard into deck; if you do, the opponent does the same."""
    if ctx.source is not ctx.my_active():
        return
    if not await ctx.ask_yes_no(
            "Discard the top 3 cards of your deck, then shuffle 3 basic "
            "Energy cards from your discard pile into your deck? Your "
            "opponent will do the same."):
        return
    await _mill_then_recycle_energy(ctx, ctx.player_id)
    await _mill_then_recycle_energy(ctx, ctx.opponent_id)


async def crushing_lava(ctx):
    """You may discard a Fire or Fighting basic Energy; Fire Burns, Fighting +20."""
    pool = [
        e for e in ctx.attached_energies(ctx.attacker)
        if _typed_basic_energy(e, PokemonTypes.FIRE)
        or _typed_basic_energy(e, PokemonTypes.FIGHTING)
    ]
    picked = []
    if pool and await ctx.ask_yes_no(
            "Discard a Fire or Fighting basic Energy card attached to Magcargo?"):
        picked = await ctx.choose_cards(
            pool, 1,
            prompt="Choose a Fire or Fighting basic Energy card to discard")
        await ctx.discard_cards(picked)
    bonus = 0
    burned = False
    if picked:
        energy = picked[0]
        if _typed_basic_energy(energy, PokemonTypes.FIGHTING):
            bonus = 20
        if _typed_basic_energy(energy, PokemonTypes.FIRE):
            burned = True
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)
    if burned:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


# ----------------------------------------------------------------------
# Magnemite — Magnetic Lines
# ----------------------------------------------------------------------

async def magnetic_lines(ctx):
    """Printed damage; heads, move 1 basic Energy from the Defending Pokémon
    to 1 of the opponent's Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    defender = ctx.defender
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = [e for e in ctx.attached_energies(defender)
                if is_basic_energy_card(e)]
    if not energies:
        return
    results = await ctx.flip_coins(1, "Magnetic Lines")
    if not results or not results[0]:
        return
    picks = await ctx.choose_cards(
        energies, 1,
        prompt="Choose a basic Energy card attached to the Defending Pokémon")
    if not picks:
        return
    dest = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to")
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


# ----------------------------------------------------------------------
# Magneton (Lightning) — Attract Energy / Electric Blast
# ----------------------------------------------------------------------

async def attract_energy(ctx):
    """ON_EVOLVE (any): you may move any number of basic Energy from your
    other Pokémon onto Magneton."""
    sources = [poked for poked in ctx.my_pokemon_in_play() if poked is not ctx.source]
    if not any(is_basic_energy_card(energy)
               for poked in sources for energy in ctx.attached_energies(poked)):
        return
    if not await ctx.ask_yes_no(
            "Move any number of basic Energy cards attached to your other "
            "Pokémon to Magneton?"):
        return
    await ctx.move_energy_freely(
        sources, [ctx.source], predicate=is_basic_energy_card,
        prompt="Choose a basic Energy card to move to Magneton")


async def electric_blast(ctx):
    """Printed damage; you may discard all Lightning Energy cards and place
    that many damage counters on the opponent's Bench."""
    await ctx.deal_damage()
    lightning = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    if not lightning:
        return
    if not await ctx.ask_yes_no(
            "Discard all Lightning Energy cards attached to Magneton?"):
        return
    await ctx.discard_cards(lightning)
    bench = ctx.opponent_bench()
    if bench:
        await ctx.place_damage_counters(len(lightning), bench)


# ----------------------------------------------------------------------
# Magneton (Metal) — Bounce Off
# ----------------------------------------------------------------------

async def bounce_off(ctx):
    """Printed damage; the Active with fewer Energy cards switches (if any)."""
    await ctx.deal_damage()
    mine = len(ctx.attached_energies(ctx.attacker))
    defender = ctx.defender
    theirs = len(ctx.attached_energies(defender)) if defender is not None else 0
    if mine == theirs:
        return
    if mine < theirs:
        bench = ctx.my_bench()
        if not bench:
            return
        pick = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if pick is not None:
            await ctx.switch_active(ctx.player_id, pick)
        return
    if defender is None or defender in ctx.knockouts:
        return
    await opponent_switches(ctx)


# ----------------------------------------------------------------------
# Meowth — Sudden Swipe
# ----------------------------------------------------------------------

async def sudden_swipe(ctx):
    """Printed damage; heads, look at the opponent's hand and shuffle 1 Energy."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Sudden Swipe")
    if not results or not results[0]:
        return
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    matches = [c for c in hand if is_energy_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1,
        prompt="Choose an Energy card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


# ----------------------------------------------------------------------
# Miracle Spheres
# ----------------------------------------------------------------------

def _has_basic_energy_types(ctx, *types: PokemonTypes) -> bool:
    energies = ctx.attached_energies(ctx.attacker)
    return all(any(_typed_basic_energy(e, t) for e in energies) for t in types)


async def fire_force(ctx):
    """30; Fire+Lightning Confuses; Fire+Fighting +10 and heal 3 counters."""
    bonus = 10 if _has_basic_energy_types(
        ctx, PokemonTypes.FIRE, PokemonTypes.FIGHTING) else 0
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)
    if _has_basic_energy_types(ctx, PokemonTypes.FIRE, PokemonTypes.LIGHTNING):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    if bonus:
        await ctx.heal(30, ctx.attacker)


async def freezing_force(ctx):
    """30; Fire+Water +10 and Burn; Water+Psychic shuffle 1 Energy from defender."""
    bonus = 10 if _has_basic_energy_types(
        ctx, PokemonTypes.FIRE, PokemonTypes.WATER) else 0
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)
    if bonus:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    if not _has_basic_energy_types(ctx, PokemonTypes.WATER, PokemonTypes.PSYCHIC):
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1,
        prompt="Choose an Energy card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def thunder_force(ctx):
    """30; Grass+Lightning Asleep+Poisoned; Water+Lightning +10 and 1 counter
    on each opposing Bench Pokémon."""
    bonus = 10 if _has_basic_energy_types(
        ctx, PokemonTypes.WATER, PokemonTypes.LIGHTNING) else 0
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)
    if _has_basic_energy_types(ctx, PokemonTypes.GRASS, PokemonTypes.LIGHTNING):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    if bonus:
        for poked in ctx.opponent_bench():
            await ctx.deal_damage(10, target=poked, as_counters=True)


# ----------------------------------------------------------------------
# Mystery Plate α — Desert Burn
# ----------------------------------------------------------------------

async def desert_burn(ctx):
    """5+ opponent prizes: search a Trainer; exactly 1: Burned, Paralyzed, Poisoned."""
    area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
    prizes = len(area.children) if area else 0
    if prizes >= 5:
        picks = await ctx.search_deck(
            is_trainer_card, count=1, minimum=0,
            prompt="Choose a Trainer card to put into your hand.")
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        return
    if prizes != 1:
        return
    defender = ctx.defender
    if defender is None:
        return
    await ctx.apply_special_condition(defender, SpecialConditions.BURNED)
    await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    await ctx.apply_special_condition(defender, SpecialConditions.POISONED)


# ----------------------------------------------------------------------
# Misdreavus — Gift of Spite
# ----------------------------------------------------------------------

async def gift_of_spite(ctx):
    """Put 1 damage counter on the Defending Pokémon per damaged Pokémon you have."""
    n = sum(1 for poked in ctx.my_pokemon_in_play() if _is_damaged(ctx.board, poked))
    if n and ctx.defender is not None:
        await ctx.deal_damage(n * 10, target=ctx.defender, as_counters=True)


# ----------------------------------------------------------------------
# Murkrow — Blindside
# ----------------------------------------------------------------------

async def blindside(ctx, amount: int = 20):
    """`amount` to 1 damaged opposing Pokémon; ignore W/R."""
    candidates = [poked for poked in ctx.opponent_pokemon_in_play()
                  if _is_damaged(ctx.board, poked)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon that has a damage counter on it")
    if target is None:
        return
    await ctx.deal_damage(
        amount, target=target, ignore_weakness=True, ignore_resistance=True)


# ----------------------------------------------------------------------
# Mirage Stadium
# ----------------------------------------------------------------------

class MirageStadiumPassive(Passive):
    """Players flip a coin when they try to retreat; tails, that Pokémon
    can't retreat this turn."""

    def requires_retreat_flip(self, pokemon, carrier):
        return True


# ----------------------------------------------------------------------
# Umbreon — Dark Gaze
# ----------------------------------------------------------------------

def _dark_gaze_target(pokemon, carrier) -> bool:
    holder = carrier_pokemon(carrier)
    if holder is None or not is_in_active_spot(holder):
        return False
    return not is_in_active_spot(pokemon)


dark_gaze_passive = ability_lock_passive(_dark_gaze_target)


# ----------------------------------------------------------------------
# Vaporeon — Aqua Trick
# ----------------------------------------------------------------------

async def aqua_trick(ctx):
    """Printed damage; heads, move 1 Energy from the Defending Pokémon to
    1 of the opponent's Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    defender = ctx.defender
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    results = await ctx.flip_coins(1, "Aqua Trick")
    if not results or not results[0]:
        return
    picks = await ctx.choose_cards(
        energies, 1,
        prompt="Choose an Energy card attached to the Defending Pokémon")
    if not picks:
        return
    dest = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to")
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


# ----------------------------------------------------------------------
# Venomoth — Healing Dust
# ----------------------------------------------------------------------

async def healing_dust(ctx):
    """Flip 2 coins; heal 1 damage counter from each of your Pokémon per heads."""
    results = await ctx.flip_coins(2, "Healing Dust")
    heads = sum(1 for result in results if result)
    if not heads:
        return
    for poked in ctx.my_pokemon_in_play():
        await ctx.heal(10 * heads, poked)


# ----------------------------------------------------------------------
# Wigglytuff — Good Neighbor
# ----------------------------------------------------------------------

async def good_neighbor(ctx):
    """Flip: heads, each player heals up to 20 from their Active."""
    results = await ctx.flip_coins(1, "Good Neighbor")
    if not results or not results[0]:
        return
    for poked in (ctx.my_active(), ctx.opponent_active()):
        if poked is not None:
            await ctx.heal(20, poked)


# ----------------------------------------------------------------------
# Underground Expedition
# ----------------------------------------------------------------------

async def underground_expedition(ctx):
    """Look at the bottom 4 cards; put 2 into hand, rest back on the bottom."""
    bottom = ctx.deck()[:4]
    if not bottom:
        return
    take = min(2, len(bottom))
    picks = await ctx.choose_cards(
        bottom, take, minimum=take,
        prompt="Choose 2 cards to put into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    rest = [card for card in bottom if card not in picks]
    if len(rest) <= 1:
        return
    ordered = await ctx.choose_cards(
        rest, len(rest), minimum=len(rest), ordered=True,
        prompt="Put remaining cards on the bottom of your deck, in order.",
    )
    for card in ordered:
        await ctx.put_on_bottom_of_deck(card)


# ----------------------------------------------------------------------
# Underground Lake
# ----------------------------------------------------------------------

def underground_lake_condition(board, player_id, stadium=None) -> bool:
    if not bench_has_room(board, player_id):
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(
        c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _FOSSIL_EVOS
        for c in discard.children
    )


async def underground_lake(ctx):
    """Put an Omanyte or Kabuto from discard onto the Bench (as a Basic)."""
    pool = [c for c in ctx.discard_pile()
            if c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _FOSSIL_EVOS]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1,
        prompt="Choose an Omanyte or Kabuto card to put onto your Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])


# ----------------------------------------------------------------------
# Politoed — Energy Splash
# ----------------------------------------------------------------------

async def energy_splash(ctx):
    """Printed damage; move 2 Water Energy cards onto 1 or 2 Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    take = min(2, len(_energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.WATER)))
    for _ in range(take):
        pool = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.WATER)
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, prompt="Choose a Water Energy card to move to the Bench")
        if not picks:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to attach the Energy to")
        if target is not None:
            await ctx.move_energy(picks[0], target)


# ----------------------------------------------------------------------
# Poliwrath — Strange Spiral
# ----------------------------------------------------------------------

def strange_spiral_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    return any(is_basic_energy_card(e) for e in board.attached_energies(pokemon))


async def strange_spiral(ctx):
    """Discard a basic Energy; the Defending Pokémon is now Confused."""
    discarded = await ctx.discard_energy_from(
        ctx.source, 1, predicate=is_basic_energy_card,
        prompt="Choose a basic Energy card to discard from Poliwrath")
    if discarded:
        await ctx.apply_special_condition(
            ctx.opponent_active(), SpecialConditions.CONFUSED)


# ----------------------------------------------------------------------
# Raichu — Zzzap
# ----------------------------------------------------------------------

_POKE_POWER_OR_BODY = ("PokePower", "PokeBody")


def _has_poke_power_or_body(pokemon) -> bool:
    abilities = pokemon.get_attribute(AttrID.PIE_ABILITIES) or []
    return any(isinstance(entry, dict)
               and entry.get("abilityType") in _POKE_POWER_OR_BODY
               for entry in abilities)


async def zzzap(ctx):
    """20 to each Pokémon (both sides) with a Poké-Power or Poké-Body; no W/R."""
    for poked in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if _has_poke_power_or_body(poked):
            await ctx.deal_damage(20, target=poked, apply_modifiers=False)


# ----------------------------------------------------------------------
# Raikou — Lightning Sphere
# ----------------------------------------------------------------------

async def lightning_sphere(ctx):
    """You may flip; heads discards all Lightning Energy, +20 per discarded card."""
    bonus = 0
    lightning = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    if lightning and await ctx.ask_yes_no(
            "Flip a coin? If heads, discard all Lightning Energy cards "
            "attached to Raikou."):
        results = await ctx.flip_coins(1, "Lightning Sphere")
        if results and results[0]:
            await ctx.discard_cards(lightning)
            bonus = 20 * len(lightning)
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)


# ----------------------------------------------------------------------
# Raticate — Continuous Bite
# ----------------------------------------------------------------------

_CONTINUOUS_BITE_BONUS = {0: 0, 1: 10, 2: 30, 3: 60}


async def continuous_bite(ctx):
    """Flip 3: +10 / +30 / +60 for 1 / 2 / 3 heads."""
    results = await ctx.flip_coins(3, "Continuous Bite")
    heads = sum(1 for result in results if result)
    await ctx.deal_damage(
        (getattr(ctx.ability, "damage", 0) or 0)
        + _CONTINUOUS_BITE_BONUS.get(heads, 0))


# ----------------------------------------------------------------------
# Retro Energy
# ----------------------------------------------------------------------

async def retro_energy_on_attach(ctx):
    """When attached from hand to an Evolved Pokémon, you may heal up to 20
    and devolve it (discard the highest Stage Evolution card)."""
    target = ctx.attached_to
    if target is None or not devolvable(target):
        return
    if not await ctx.ask_yes_no(
            "Remove up to 2 damage counters from this Pokémon and devolve it?"):
        return
    damage = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
    available = min(2, max(0, damage // 10))
    if available > 0:
        n = await ctx.choose(
            "Remove up to 2 damage counters.",
            [str(i) for i in range(available + 1)],
            use_panel=False,
        )
        if n > 0:
            await ctx.heal(n * 10, target)
    await ctx.devolve_pokemon(target, steps=1, destination="discard")


# ----------------------------------------------------------------------
# Sandslash — Poison Needle Rush
# ----------------------------------------------------------------------

async def poison_needle_rush(ctx):
    """3 coins: 20× heads; Poisoned if at least 1 heads."""
    results = await ctx.flip_coins(3, "Poison Needle Rush")
    heads = sum(1 for result in results if result)
    if not heads:
        return
    await ctx.deal_damage(20 * heads)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


# ----------------------------------------------------------------------
# Skarmory — Spinning Head
# ----------------------------------------------------------------------

async def spinning_head(ctx):
    """Printed damage; heads, switch this Pokémon with a Benched one."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Spinning Head")
    if not results or not results[0]:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


# ----------------------------------------------------------------------
# Slugma — Scorching Lava
# ----------------------------------------------------------------------

async def scorching_lava(ctx):
    """Discard 1 Fire Energy card; the Defending Pokémon is Burned."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        prompt="Choose a Fire Energy card to discard from Slugma")
    if not discarded:
        return
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


# ----------------------------------------------------------------------
# Snorlax — Lolling About
# ----------------------------------------------------------------------

async def lolling_about(ctx):
    """Remove 1 damage counter from Snorlax; it is now Asleep."""
    await ctx.heal(10, ctx.source)
    await ctx.apply_special_condition(ctx.source, SpecialConditions.ASLEEP)


# ----------------------------------------------------------------------
# Snubbull — Scary Face
# ----------------------------------------------------------------------

async def scary_face(ctx):
    """Heads: the Defending Pokémon can't attack or retreat next turn."""
    results = await ctx.flip_coins(1, "Scary Face")
    if not results or not results[0]:
        return
    if lock_defender_attacks(ctx):
        ctx.lock_retreat(ctx.defender)


# ----------------------------------------------------------------------
# Stantler — Threaten / Antler Swipe
# ----------------------------------------------------------------------

async def threaten(ctx):
    """Heads: look at the hand and shuffle 1 Trainer into the opponent's deck."""
    results = await ctx.flip_coins(1, "Threaten")
    if not results or not results[0]:
        return
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    trainers = [card for card in hand if is_trainer_card(card)]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1,
        prompt="Choose a Trainer card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def antler_swipe(ctx):
    """Heads: 20 to the Defending (no W/R). Tails: 20 to 1 Benched (no W/R)."""
    results = await ctx.flip_coins(1, "Antler Swipe")
    if results and results[0]:
        await ctx.deal_damage(20, ignore_weakness=True, ignore_resistance=True)
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to take 20 damage")
    if target is not None:
        await ctx.deal_damage(20, target=target)


# ----------------------------------------------------------------------
# Star Piece
# ----------------------------------------------------------------------

async def star_piece_between_turns(ctx):
    """If the holder is Benched with 2+ damage counters, search-evolve it
    from the deck, shuffle, then discard Star Piece."""
    pokemon = ctx.source
    if pokemon is None or is_in_active_spot(pokemon):
        return
    damage = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
    if damage < 20:
        return
    tool = next((t for t, p in ctx.tools_in_play() if p is pokemon), None)
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda c: bool(logic_name) and evolves_from(c.archetype_id, logic_name),
        count=1, minimum=0,
        prompt="Choose an Evolution card that this Pokémon evolves into.",
    )
    if picks:
        await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()
    if tool is not None:
        await ctx.discard_cards([tool])


# ----------------------------------------------------------------------
# Starmie — Core Blast
# ----------------------------------------------------------------------

def special_energy_on_defender(ctx) -> int:
    """Special Energy cards attached to the Defending Pokémon."""
    defender = ctx.defender
    if defender is None:
        return 0
    return sum(1 for energy in ctx.attached_energies(defender)
               if is_special_energy(energy))


# ----------------------------------------------------------------------
# Staryu — Energy Healing
# ----------------------------------------------------------------------

async def energy_healing(ctx):
    """Heal 2 damage counters from this Pokémon per attached Energy card."""
    n = len(ctx.attached_energies(ctx.attacker))
    if n:
        await ctx.heal(n * 20, ctx.attacker)


# ----------------------------------------------------------------------
# Steelix — Rare Metal / Metal Tail
# ----------------------------------------------------------------------

class RareMetalPassive(Passive):
    """Basic Energy cards on the carrier provide Metal instead of their usual types."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or not is_basic_energy_card(energy):
            return options
        mine = any(
            isinstance(passive, RareMetalPassive)
            and carrier_pokemon(carrier) is holder
            for passive, carrier in _active_passives(board)
        )
        if not mine:
            return options
        metal = PokemonTypes.METAL.value
        if not options:
            return [[metal]]
        return [[metal] * max(1, len(option)) for option in options]


async def metal_tail(ctx):
    """You may flip before damage: heads 80, tails nothing; otherwise printed."""
    if await ctx.ask_yes_no(
            "Flip a coin? If heads, this attack does 80 damage. If tails, this attack does nothing."):
        results = await ctx.flip_coins(1, "Metal Tail")
        if not results or not results[0]:
            return
        await ctx.deal_damage(80)
        return
    await ctx.deal_damage()


# ----------------------------------------------------------------------
# Wobbuffet — Mirror Coat / Return Attack
# ----------------------------------------------------------------------

class MirrorCoatPassive(Passive):
    """If this Pokémon becomes Poisoned or Burned by the Defending Pokémon's
    attack during the opponent's turn, that Pokémon gets the same condition."""

    async def after_condition_applied(self, ctx, target, condition, carrier):
        if condition not in (SpecialConditions.POISONED, SpecialConditions.BURNED):
            return
        if carrier_pokemon(carrier) is not target:
            return
        if not ctx.is_attack_effect():
            return
        if ctx.player_id == target.owning_player_id:
            return
        attacker = ctx.attacker
        if attacker is None or attacker is target:
            return
        if attacker.owning_player_id == target.owning_player_id:
            return
        await ctx.apply_special_condition(attacker, condition)


async def return_attack(ctx):
    """Flip 2 coins. If either is heads, 10× damage counters on self."""
    results = await ctx.flip_coins(2, "Return Attack")
    if not any(results):
        return
    await damage_per(damage_counters_on("self"), 10)(ctx)


class CounterPassive(Passive):
    """If an attack damages this Pokémon, flip: heads, attack the Defending
    Pokémon for an equal amount (even if this Pokémon is Knocked Out)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return None
        attacker = calc.attacker
        if attacker is None:
            return None
        results = await ctx.flip_coins(1, "Counter", source=holder)
        if not (results and results[0]):
            return None
        saved = ctx.attacker
        ctx.attacker = holder
        try:
            await ctx.deal_damage(
                calc.amount, target=attacker, apply_modifiers=True)
        finally:
            ctx.attacker = saved
        return None


async def counter(ctx):
    """During the opponent's next turn, a hit on this Pokémon may reflect
    as an equal-damage attack with W/R (even if this Pokémon is KO'd)."""
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(ctx.attacker, CounterPassive())


# ----------------------------------------------------------------------
# Xatu — Synchronicity / Warp Hole
# ----------------------------------------------------------------------

class SynchronicityPassive(Passive):
    """You may attach any Technical Machine to this Pokémon."""

    def allows_any_technical_machine(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


async def warp_hole(ctx):
    """Printed damage; heads puts a discard-pile card on top of the deck."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Warp Hole")
    if not results or not results[0]:
        return
    pile = ctx.discard_pile()
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1,
        prompt="Choose a card from your discard pile to put on top of your deck.",
    )
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


async def energy_cycle(ctx):
    """Heads: move 1 Energy from the Defending Pokémon to 1 of the opponent's
    Benched Pokémon (you choose both)."""
    results = await ctx.flip_coins(1, "Energy Cycle")
    if not results or not results[0]:
        return
    bench = ctx.opponent_bench()
    defender = ctx.defender
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1,
        prompt="Choose an Energy card attached to the Defending Pokémon")
    if not picks:
        return
    dest = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to")
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


# ----------------------------------------------------------------------
# Yanma — Shockwave
# ----------------------------------------------------------------------

async def shockwave(ctx):
    """Heads: 10 to each opposing Pokémon (no W/R), then the opponent switches."""
    results = await ctx.flip_coins(1, "Shockwave")
    if not results or not results[0]:
        return
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage(
            10, target=pokemon, ignore_weakness=True, ignore_resistance=True)
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    await opponent_switches(ctx)


# ----------------------------------------------------------------------
# Best of Game (BP)
# ----------------------------------------------------------------------

async def vine_pull(ctx):
    """When this Pokémon retreats, switch the opponent's Active with a Bench
    Pokémon of your choice (Dark Ivysaur Vine Pull)."""
    retreated = getattr(ctx, "retreated_pokemon", None)
    if retreated is not None and retreated is not ctx.source:
        ctx.suppress_announce = True
        return
    old_active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old_active is None or not bench or ctx.effects_blocked(old_active):
        ctx.suppress_announce = True
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def fury_strikes(ctx):
    """The opponent distributes 3 damage counters among their Pokémon
    (Dark Ivysaur Fury Strikes markers, no W/R)."""
    await ctx.place_damage_counters(
        3, ctx.opponent_pokemon_in_play(),
        player_id=ctx.opponent_id,
        prompt="Place 3 damage counters on your Pokémon.",
    )


async def horrid_pollen(ctx):
    """30; flip 2. Always Poisoned; 2 heads Confused, 1 heads Asleep,
    both tails Paralyzed."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Horrid Pollen")
    heads = sum(1 for result in results if result)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    if heads == 2:
        extra = SpecialConditions.CONFUSED
    elif heads == 1:
        extra = SpecialConditions.ASLEEP
    else:
        extra = SpecialConditions.PARALYZED
    await ctx.apply_special_condition(ctx.defender, extra)


async def professor_elm(ctx):
    """Shuffle your hand into your deck, draw 7, then no more Trainers
    this turn."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(7)
    ctx.lock_plays(
        ctx.player_id, is_trainer_card,
        through_turn=ctx.session.turn_state.turn_number,
    )


async def endure(ctx):
    """Heads: if this Pokémon would be Knocked Out by an attack during the
    opponent's next turn, it isn't, and remaining HP becomes 10."""
    title = ctx.ability.title if ctx.ability else "Endure"
    results = await ctx.flip_coins(1, title)
    if not results or not results[0]:
        return
    attacker = ctx.attacker
    if attacker is None:
        return
    ctx.add_passive_through_opponents_turn(
        attacker, GutsSurvivePassive(hp_floor=10, title=title, flip=False))
    if attacker.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(attacker.entity_id)


class ScreechVulnerabilityPassive(Passive):
    """Attacks that deal damage to this Pokémon do +N after W/R."""

    def __init__(self, amount=20):
        self.amount = amount

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack:
            return
        if carrier_pokemon(carrier) is not calc.target:
            return
        if calc.amount <= 0:
            return
        calc.amount += self.amount


def screech(amount=20):
    """Until the end of your next turn, attacks that damage the Defending
    Pokémon do `amount` more (after W/R). Benching or evolving ends it."""

    async def effect(ctx):
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        ctx.add_passive_through_own_next_turn(
            defender, ScreechVulnerabilityPassive(amount))
        if defender.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(defender.entity_id)

    return effect


async def freeze(ctx):
    """Printed damage; heads, the Defending Pokémon can't attack during the
    opponent's next turn. Benching or evolving ends this effect."""
    await ctx.deal_damage()
    title = ctx.ability.title if ctx.ability else "Freeze"
    results = await ctx.flip_coins(1, title)
    if results and results[0]:
        lock_defender_attacks(ctx)


async def poke_gear(ctx):
    """Look at the top 7; you may reveal 1 Trainer into hand; shuffle; no
    more Trainers this turn."""
    await look_at_top(
        7, take=1, predicate=is_trainer_card, rest="shuffle",
        minimum=0, reveal=True,
        prompt="You may choose a Trainer card to put into your hand.",
    )(ctx)
    ctx.lock_plays(
        ctx.player_id, is_trainer_card,
        through_turn=ctx.session.turn_state.turn_number,
    )


async def pokemon_march(ctx):
    """Opponent may bench a Basic from their deck, then you may; then each
    player shuffles. A player with a full Bench skips the search."""
    for pid in (ctx.opponent_id, ctx.player_id):
        bench = ctx.board.find_player_area(pid, "bench")
        cap = effective_bench_capacity(ctx.board, pid)
        if bench is None or len(bench.children) >= cap:
            continue
        if not ctx.deck(pid):
            continue
        if not await ctx.ask_yes_no(
                "Search your deck for a Basic Pokémon and put it onto your Bench?",
                player_id=pid):
            continue
        picks = await ctx.search_deck(
            is_basic_pokemon, count=1, minimum=0,
            prompt="Choose a Basic Pokémon to put onto your Bench.",
            player_id=pid,
        )
        for card in picks:
            await ctx.bench_pokemon(card)
    for pid in (ctx.opponent_id, ctx.player_id):
        await ctx.shuffle_deck(pid)


class CrosscounterPassive(Passive):
    """If this Pokémon is damaged by an attack (even if Knocked Out), flip:
    heads, deal double that damage to the attacking Pokémon."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return None
        attacker = calc.attacker
        if attacker is None:
            return None
        results = await ctx.flip_coins(1, "Crosscounter", source=holder)
        if results and results[0]:
            await ctx.deal_damage(
                calc.amount * 2, target=attacker,
                apply_modifiers=False, as_counters=True,
            )
        return None


async def crosscounter(ctx):
    """During the opponent's next turn, a hit on this Pokémon may reflect
    double that damage onto the attacker (even if this Pokémon is KO'd)."""
    ctx.add_passive_through_opponents_turn(ctx.attacker, CrosscounterPassive())


async def juxtapose(ctx):
    """Flip: heads, swap damage-counter counts with the Defending Pokémon."""
    results = await ctx.flip_coins(1, "Juxtapose")
    if not results or not results[0]:
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    self_counters = damage_counters_on("self")(ctx)
    opp_counters = damage_counters_on("defender")(ctx)
    await ctx.set_damage_counters(ctx.attacker, opp_counters)
    await ctx.set_damage_counters(defender, self_counters)


# ----------------------------------------------------------------------
# Southern Islands (SI1)
# ----------------------------------------------------------------------

async def rainbow_wave(ctx):
    """Choose a non-Colorless Energy type attached to Mew; 20 to each opposing
    Pokémon of that type (including the Bench), no Weakness or Resistance."""
    types = set()
    attacker = ctx.attacker
    if attacker is None:
        return
    for energy in ctx.attached_energies(attacker):
        for option in energy_provided_options(ctx.board, energy):
            types.update(option)
    types.discard(PokemonTypes.COLORLESS.value)
    types.discard(PokemonTypes.NO_COLOR.value)
    if not types:
        return
    ordered = sorted(types)
    names = [CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(t)] for t in ordered]
    idx = 0 if len(ordered) == 1 else await ctx.choose(
        "Choose a type of Energy other than Colorless.", names)
    chosen = ordered[idx]
    for poked in ctx.opponent_pokemon_in_play():
        if chosen in effective_pokemon_types(ctx.board, poked):
            await ctx.deal_damage(20, target=poked, apply_modifiers=False)


async def _remove_up_to_counters(ctx, pokemon_list, count, player_id):
    """Remove up to `count` damage counters from among `pokemon_list`."""
    damaged = [poked for poked in pokemon_list if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    total = sum(
        (ctx.max_hp(poked) - poked.get_attribute(AttrID.HP, 0)) // 10
        for poked in damaged)
    if total <= count:
        for poked in damaged:
            dmg = ctx.max_hp(poked) - poked.get_attribute(AttrID.HP, 0)
            if dmg > 0:
                await ctx.heal(dmg, poked)
        return
    remaining = count
    while remaining > 0:
        damaged = [poked for poked in pokemon_list if _is_damaged(ctx.board, poked)]
        if not damaged:
            return
        target = damaged[0] if len(damaged) == 1 else await ctx.choose_pokemon(
            damaged, "Choose a Pokémon to remove a damage counter from",
            player_id=player_id)
        if target is None:
            return
        await ctx.heal(10, target)
        remaining -= 1


async def strange_scent(ctx):
    """Each player flips a coin; heads removes 3 damage counters from among
    that player's Pokémon."""
    mine = await ctx.flip_coins(1, "Strange Scent")
    theirs = await ctx.flip_coins(1, "Strange Scent")
    if mine and mine[0]:
        await _remove_up_to_counters(
            ctx, ctx.my_pokemon_in_play(), 3, ctx.player_id)
    if theirs and theirs[0]:
        await _remove_up_to_counters(
            ctx, ctx.opponent_pokemon_in_play(), 3, ctx.opponent_id)


async def tentacle_grip(ctx):
    """Flip a coin per Water Energy attached; draw 2 cards per heads."""
    n = count_energy("self", energy_type=PokemonTypes.WATER)(ctx)
    results = await ctx.flip_coins(n, "Tentacle Grip") if n else []
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.draw_cards(heads * 2)


async def gentle_song(ctx):
    """Heal 20 from Lapras and the Defending Pokémon; that Pokémon is Asleep."""
    if ctx.attacker is not None:
        await ctx.heal(20, ctx.attacker)
    defender = ctx.defender
    if defender is not None:
        await ctx.heal(20, defender)
        await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)


async def sharpshooter(ctx):
    """Choose 1 opposing Pokémon; 10× heads of Grass-Energy coin flips, no W/R."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    n = count_energy("self", energy_type=PokemonTypes.GRASS)(ctx)
    results = await ctx.flip_coins(n, "Sharpshooter") if n else []
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(10 * heads, target=target, apply_modifiers=False)


async def lick_wounds(ctx):
    """Heads: heal 20 from 1 damaged Pokémon in play (either player's)."""
    results = await ctx.flip_coins(1, "Lick Wounds")
    if not results or not results[0]:
        return
    damaged = [poked for poked in
               ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
               if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal")
    if target is not None:
        await ctx.heal(20, target)


async def paradise_pollen(ctx):
    """Heads: heal 20 from Vileplume, then 20 from 1 damaged Benched Pokémon."""
    results = await ctx.flip_coins(1, "Paradise Pollen")
    if not results or not results[0]:
        return
    if ctx.attacker is not None:
        await ctx.heal(20, ctx.attacker)
    damaged_bench = [poked for poked in ctx.my_bench()
                     if _is_damaged(ctx.board, poked)]
    if not damaged_bench:
        return
    target = await ctx.choose_pokemon(
        damaged_bench, "Choose a Benched Pokémon to heal")
    if target is not None:
        await ctx.heal(20, target)


async def rampage(ctx):
    """20 + 10 per damage counter on self; tails, this Pokémon is Confused."""
    await damage_per(damage_counters_on("self"), 10, base=20)(ctx)
    results = await ctx.flip_coins(1, "Rampage")
    if results and not results[0]:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


# ----------------------------------------------------------------------
# Team Rocket (BASE5)
# ----------------------------------------------------------------------

_ACP_NAMES = (
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP],
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED],
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.PARALYZED],
)


def _asleep_confused_or_paralyzed(pokemon) -> bool:
    current = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    return any(name in current for name in _ACP_NAMES)


async def sneak_attack(ctx):
    """Dark Golbat: when played from hand, you may snipe 10 with W/R."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no(
            "Use Sneak Attack to do 10 damage to 1 of your opponent's Pokémon?"):
        ctx.suppress_announce = True
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.deal_damage(10, target=target, apply_modifiers=True)


async def third_eye(ctx):
    """Dark Golduck: discard 1 attached Energy, then draw up to 3 cards."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        prompt="Choose 1 Energy card to discard from Dark Golduck")
    if not discarded:
        return
    n = await ctx.choose(
        "Draw up to 3 cards.",
        [str(i) for i in range(4)],
        use_panel=False,
    )
    if n > 0:
        await ctx.draw_cards(n)


async def final_beam(ctx):
    """Dark Gyarados: on lethal attack damage, heads deals 20×Water Energy
    (with W/R) to the attacker. Fires on ON_DAMAGED_BY_ATTACK so attached
    Energy and Special Conditions are still present (ON_KNOCKED_OUT runs
    after the stack is discarded)."""
    gyarados = ctx.source
    if gyarados is None or gyarados.get_attribute(AttrID.HP, 0) > 0:
        ctx.suppress_announce = True
        return
    if _asleep_confused_or_paralyzed(gyarados):
        ctx.suppress_announce = True
        return
    water = count_energy("self", energy_type=PokemonTypes.WATER)(ctx)
    attacker = ctx.damaged_by
    if water <= 0 or attacker is None:
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(1, "Final Beam")
    if not results or not results[0]:
        return
    await ctx.deal_damage(20 * water, target=attacker, apply_modifiers=True)


async def bench_manipulation(ctx):
    """Dark Hypno: opponent's Bench size in coins; 20×tails, no W/R."""
    n = len(ctx.opponent_bench())
    results = await ctx.flip_coins(n, "Bench Manipulation") if n else []
    tails = sum(1 for result in results if not result)
    if tails:
        await ctx.deal_damage(20 * tails, apply_modifiers=False)


async def thunder_attack(ctx):
    """Dark Jolteon: printed damage; heads Paralyzes, tails 10 to self."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Thunder Attack")
    if results and results[0]:
        await ctx.apply_special_condition(
            ctx.defender, SpecialConditions.PARALYZED)
    else:
        await ctx.deal_damage(
            10, target=ctx.attacker, apply_modifiers=False)


async def no_wr_damage(ctx):
    """Printed damage; don't apply Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


fling_condition = opponent_has_benched


async def fling(ctx):
    """Shuffle the opponent's Active and all attached cards into their deck."""
    target = ctx.opponent_active()
    if target is None or not ctx.opponent_bench() or ctx.effects_blocked(target):
        return
    await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


def has_fire_energy_attached(board, player_id, pokemon=None) -> bool:
    """Attack gate: this Pokémon has a Fire Energy card attached."""
    if pokemon is None:
        return False
    return any(energy_provides_type(e, PokemonTypes.FIRE.value)
               for e in board.attached_energies(pokemon))


def _fire_energy_pred(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def continuous_fireball(ctx):
    """50× heads among coins equal to attached Fire Energy cards; discard that
    many Fire Energy cards from Dark Charizard."""
    fire = [e for e in ctx.attached_energies(ctx.attacker) if _fire_energy_pred(e)]
    results = await ctx.flip_coins(len(fire), "Continuous Fireball") if fire else []
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(50 * heads)
        await ctx.discard_energy_from(
            ctx.attacker, heads, predicate=_fire_energy_pred,
            prompt="Choose Fire Energy cards to discard")


async def _fireball_heads(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=_fire_energy_pred,
        prompt="Choose a Fire Energy card to discard")


fireball = flip_or_nothing(then=_fireball_heads)


async def summon_minions(ctx):
    """ON_EVOLVE from hand: search up to 2 Basic Pokémon onto the Bench."""
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    take = min(2, space)
    if take <= 0:
        ctx.suppress_announce = True
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=take, minimum=0,
        prompt="Choose up to 2 Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def sinkhole(ctx):
    """When the opponent's Active Pokémon retreats, they flip; tails, 20
    damage to that Pokémon (no W/R). Stops while Asleep, Confused, or Paralyzed."""
    holder = ctx.source
    retreated = getattr(ctx, "retreated_pokemon", None)
    if (holder is None or retreated is None or retreated is holder
            or retreated.owning_player_id == holder.owning_player_id
            or _asleep_confused_or_paralyzed(holder)
            or retreated not in ctx.board.pokemon_in_play(
                retreated.owning_player_id)):
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(1, "Sinkhole", source=holder)
    if results and results[0]:
        return
    await ctx.deal_damage(20, target=retreated, apply_modifiers=False)


async def knock_down(ctx):
    """20; opponent flips — tails, +20 more."""
    results = await ctx.flip_coins(1, "Knock Down")
    bonus = 20 if results and not results[0] else 0
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)


async def energy_bomb(ctx):
    """30; move all Energy from this Pokémon onto the Bench (or discard them
    if there is no Bench)."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    if attacker is None:
        return
    energies = list(ctx.attached_energies(attacker))
    if not energies:
        return
    bench = ctx.my_bench()
    if not bench:
        await ctx.discard_cards(energies)
        return
    for energy in energies:
        dest = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to attach the Energy to")
        if dest is None:
            dest = bench[0]
        await ctx.move_energy(energy, dest)


async def playing_with_fire(ctx):
    """30; heads, +20 and discard 1 Fire Energy card."""
    results = await ctx.flip_coins(1, "Playing with Fire")
    heads = bool(results and results[0])
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + (20 if heads else 0))
    if heads:
        await ctx.discard_energy_from(
            ctx.attacker, 1, predicate=_fire_energy_pred,
            prompt="Choose a Fire Energy card to discard")


async def pollen_stench(ctx):
    """Flip: heads Confuses the Defending Pokémon; tails Confuses your Active."""
    results = await ctx.flip_coins(1, "Pollen Stench")
    if results and results[0]:
        await ctx.apply_special_condition(
            ctx.opponent_active(), SpecialConditions.CONFUSED)
    else:
        await ctx.apply_special_condition(
            ctx.my_active(), SpecialConditions.CONFUSED)


async def long_distance_hypnosis(ctx):
    """Flip: heads the Defending Pokémon is Asleep; tails your Active is."""
    results = await ctx.flip_coins(1, "Long-Distance Hypnosis")
    if results and results[0]:
        await ctx.apply_special_condition(
            ctx.opponent_active(), SpecialConditions.ASLEEP)
    else:
        await ctx.apply_special_condition(
            ctx.my_active(), SpecialConditions.ASLEEP)


async def dark_magnetic_lines(ctx):
    """Printed damage; move 1 basic Energy from the Defending Pokémon to 1
    of the opponent's Benched Pokémon. No coin flip (Dark Magneton)."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    defender = ctx.defender
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = [e for e in ctx.attached_energies(defender)
                if is_basic_energy_card(e)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1,
        prompt="Choose a basic Energy card attached to the Defending Pokémon")
    if not picks:
        return
    dest = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to")
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


class StickyGooPassive(Passive):
    """While Active and not Asleep/Confused/Paralyzed, the opponent's Active
    Pokémon costs ColorlessColorless more to retreat."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if not is_in_active_spot(holder) or _asleep_confused_or_paralyzed(holder):
            return cost
        if not opposing_active(pokemon, holder):
            return cost
        return cost + 2


async def fascinate(ctx):
    """Heads: switch a chosen opposing Benched Pokémon with the Defending."""
    results = await ctx.flip_coins(1, "Fascinate")
    if not results or not results[0]:
        return
    old_active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old_active is None or not bench or ctx.effects_blocked(old_active):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon") or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)


class FrenzyPassive(Passive):
    """If this Pokémon does any damage while Confused (even to itself),
    it does 30 more damage."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker or calc.amount <= 0:
            return
        confused = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED]
        if confused not in (holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return
        calc.amount += 30


async def surprise_thunder(ctx):
    """Printed damage; heads, flip again: heads 20 / tails 10 to each
    opposing Benched Pokémon."""
    await ctx.deal_damage()
    first = await ctx.flip_coins(1, "Surprise Thunder")
    if not first or not first[0]:
        return
    second = await ctx.flip_coins(1, "Surprise Thunder")
    amount = 20 if second and second[0] else 10
    for poked in ctx.opponent_bench():
        await ctx.deal_damage(amount, target=poked)


async def flame_pillar(ctx):
    """Printed damage; you may discard 1 Fire Energy to snipe 10 to a Bench."""
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _fire_energy_pred(e)]
    if not pool:
        return
    if not await ctx.ask_yes_no(
            "Discard 1 Fire Energy card attached to Dark Rapidash?"):
        return
    picked = await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=_fire_energy_pred,
        prompt="Choose a Fire Energy card to discard")
    if not picked:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(10, target=target)


def gather_fire_condition(board, player_id, pokemon=None) -> bool:
    """Charmander: Fire Energy on another of your Pokémon, no Special Conditions."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    fire = PokemonTypes.FIRE.value
    return any(
        energy_provides_type(energy, fire)
        for poked in board.pokemon_in_play(player_id)
        if poked is not pokemon
        for energy in board.attached_energies(poked)
    )


async def gather_fire(ctx):
    """Move 1 Fire Energy card from another of your Pokémon onto this one."""
    source = ctx.source
    others = [poked for poked in ctx.my_pokemon_in_play() if poked is not source]
    if not others or source is None:
        return
    await ctx.move_energy_freely(
        others, [source], max_count=1,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.FIRE.value),
        prompt="Choose a Fire Energy card to attach to Charmander",
    )


async def stare(ctx):
    """10 to a chosen opposing Pokémon, no W/R; lock its Pokémon Powers
    through the opponent's next turn."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.deal_damage(10, target=target, apply_modifiers=False)
    if ctx.effects_blocked(target):
        return
    ctx.add_passive_through_opponents_turn(
        target,
        ability_lock_passive(
            lambda pokemon, carrier: carrier_pokemon(carrier) is pokemon),
    )


async def rocket_tackle(ctx):
    """Printed damage; 10 to self; heads prevents attack damage next opponent turn."""
    await ctx.deal_damage()
    await ctx.deal_damage(10, target=ctx.attacker, apply_modifiers=False)
    results = await ctx.flip_coins(1, "Rocket Tackle")
    if results and results[0]:
        await apply_protection(ctx, prevent=True)


async def challenge(ctx):
    """Opponent may accept: both bench any number of Basics. Decline or full
    benches: draw 2."""
    my_space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    opp_space = (effective_bench_capacity(ctx.board, ctx.opponent_id)
                 - len(ctx.opponent_bench()))
    if my_space <= 0 and opp_space <= 0:
        await ctx.draw_cards(2)
        return
    if not await ctx.ask_yes_no(
            "Accept the challenge? If you decline, your opponent draws 2 cards.",
            player_id=ctx.opponent_id):
        await ctx.draw_cards(2)
        return

    async def _bench_basics(player_id, space):
        if space <= 0:
            return
        picks = await ctx.search_deck(
            is_basic_pokemon, count=space, minimum=0,
            prompt="Choose any number of Basic Pokémon to put onto your Bench.",
            player_id=player_id,
        )
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck(player_id)

    await _bench_basics(ctx.player_id, my_space)
    await _bench_basics(ctx.opponent_id, opp_space)


async def goop_gas_attack(ctx):
    """All Pokémon Powers stop working until the end of the opponent's next turn."""
    ctx.add_passive_through_opponents_turn(
        ctx.board.playmat,
        ability_lock_passive(lambda pokemon, carrier: True),
    )


def here_comes_team_rocket_condition(board, player_id, pokemon=None) -> bool:
    """Unplayable once Prize cards are already face-up for the rest of the game."""
    return not getattr(board.playmat, "prizes_face_up", False)


async def here_comes_team_rocket(ctx):
    """Each player plays with Prize cards face-up for the rest of the game."""
    prizes = []
    for pid in ctx.board.player_ids:
        area = ctx.board.find_player_area(pid, "prizePile")
        if area:
            prizes.extend(list(area.children))
    if prizes:
        await ctx.reveal_cards(prizes)
    ctx.board.playmat.prizes_face_up = True


async def imposter_oaks_revenge(ctx):
    """Discard 1 other card; opponent shuffles their hand into their deck and draws 4."""
    discarded = await ctx.discard_from_hand(
        1, prompt="Discard a card to play Imposter Oak's Revenge")
    if not discarded:
        return
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    await ctx.draw_cards(4, ctx.opponent_id)


def rockets_sneak_attack_condition(board, player_id, pokemon=None) -> bool:
    """Opponent has at least one card in hand."""
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    hand = board.find_player_area(opponent, "hand")
    return bool(hand and hand.children)


async def rockets_sneak_attack(ctx):
    """Look at the opponent's hand; shuffle 1 Trainer into their deck."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    trainers = [card for card in hand if is_trainer_card(card)]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1,
        prompt="Choose a Trainer card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


def is_dark_evolution(card) -> bool:
    """Evolution Pokémon whose display name contains 'Dark ' (The Boss's Way)."""
    if not is_evolution_pokemon(card):
        return False
    definition = def_for(getattr(card, "archetype_id", None) or "")
    name = (definition.display_name or "") if definition else ""
    return "Dark " in name


the_bosss_way = search_to_hand(
    is_dark_evolution, count=1, reveal=True,
    prompt="Choose an Evolution card with Dark in its name to put into your hand.",
)


async def sleep(ctx):
    """Flip: heads, the Defending Pokémon is now Asleep."""
    results = await ctx.flip_coins(1, "Sleep!")
    if results and results[0]:
        await ctx.apply_special_condition(
            ctx.opponent_active(), SpecialConditions.ASLEEP)


async def rapid_evolution(ctx):
    """Search the deck for Gyarados or Dark Gyarados and evolve Magikarp."""
    pokemon = ctx.attacker
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) if pokemon else None
    names = frozenset(("Gyarados", "Dark Gyarados"))

    def pred(card):
        if not logic_name or not evolves_from(card.archetype_id, logic_name):
            return False
        return getattr(def_for(card.archetype_id), "display_name", None) in names

    picks = await ctx.search_deck(
        pred, count=1, minimum=0,
        prompt="Choose a Gyarados or Dark Gyarados to put on Magikarp.",
    )
    if picks and pokemon is not None:
        await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()


_MAGNET_LINE = frozenset(("Magnemite", "Magneton", "Dark Magneton"))


def _magnet_line_on_bench(ctx) -> int:
    return sum(
        1 for poked in ctx.my_bench()
        if getattr(def_for(poked.archetype_id), "display_name", None) in _MAGNET_LINE
    )


magnetism = damage_per(_magnet_line_on_bench, 10, base=10)


async def coin_hurl(ctx):
    """Choose 1 opposing Pokémon; heads, 20 damage with no W/R."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    results = await ctx.flip_coins(1, "Coin Hurl")
    if results and results[0]:
        await ctx.deal_damage(20, target=target, apply_modifiers=False)


def is_garbage_run_card(card) -> bool:
    """Nightly Garbage Run: Basic Pokémon, Evolution, or basic Energy."""
    return (is_basic_pokemon(card) or is_evolution_pokemon(card)
            or is_basic_energy_card(card))


def nightly_garbage_run_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return any(is_garbage_run_card(c) for c in (discard.children if discard else []))


async def nightly_garbage_run(ctx):
    """Show up to 3 Basic Pokémon, Evolutions, and/or basic Energy from the
    discard pile and shuffle them into the deck."""
    cards = [c for c in ctx.discard_pile() if is_garbage_run_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 3, minimum=0,
        prompt="Choose up to 3 Basic Pokémon, Evolution, and/or basic Energy cards.",
    )
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks)


_CONVERSION_TYPES = (
    PokemonTypes.FIRE,
    PokemonTypes.FIGHTING,
    PokemonTypes.GRASS,
    PokemonTypes.WATER,
    PokemonTypes.PSYCHIC,
    PokemonTypes.LIGHTNING,
    PokemonTypes.METAL,
    PokemonTypes.DARKNESS,
    PokemonTypes.FAIRY,
    PokemonTypes.DRAGON,
)


class ConversionWeaknessPassive(Passive):
    """Overrides the carrier's Weakness type until it leaves the Active Spot."""

    def __init__(self, weak_type):
        self.weak_type = weak_type

    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not calc.target:
            return
        calc.weak_types = [self.weak_type]


class ConversionResistancePassive(Passive):
    """Overrides the carrier's Resistance type until it leaves the Active Spot."""

    def __init__(self, resist_type):
        self.resist_type = resist_type

    def modify_resistance(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not calc.target:
            return
        calc.resist_type = self.resist_type


async def conversion_1(ctx):
    """If the Defending Pokémon has a Weakness, change it to a chosen type
    other than Colorless until it leaves the Active Spot."""
    defender = ctx.opponent_active()
    if defender is None or not (defender.get_attribute(AttrID.WEAKNESS_TYPES) or []):
        return
    if ctx.effects_blocked(defender):
        return
    names = [CLIENT_POKEMON_TYPE_NAMES[t] for t in _CONVERSION_TYPES]
    idx = await ctx.choose(
        "Select the new Weakness for the Defending Pokémon.", names)
    ctx.add_temporary_passive(
        defender, ConversionWeaknessPassive(_CONVERSION_TYPES[idx].value))


async def conversion_2(ctx):
    """Change this Pokémon's Resistance to a chosen type other than Colorless
    until it leaves the Active Spot."""
    attacker = ctx.attacker
    if attacker is None:
        return
    names = [CLIENT_POKEMON_TYPE_NAMES[t] for t in _CONVERSION_TYPES]
    idx = await ctx.choose(
        "Select the new Resistance for this Pokémon.", names)
    ctx.add_temporary_passive(
        attacker, ConversionResistancePassive(_CONVERSION_TYPES[idx].value))


def trickery_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    prizes = board.find_player_area(player_id, "prizePile")
    deck = board.find_player_area(player_id, "deck")
    return bool(prizes and prizes.children and deck and deck.children)


async def trickery(ctx):
    """Switch 1 of your Prizes with the top card of your deck (both stay
    face down)."""
    session = ctx.session
    prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    if not prize_area or not prize_area.children or not deck or not deck.children:
        return
    await ctx.flush_choreography()
    prize_ids = [c.entity_id for c in prize_area.children]
    picked = await session._prompt_prize_pick(
        ctx.player_id, prize_ids, 1,
        prompt="Choose 1 of your Prize cards to switch with the top card of your deck.",
        prize_area=prize_area,
    )
    prize_card = ctx.board.get_entity(picked[0]) if picked else None
    if prize_card is None:
        return
    slot = prize_card.board_slot
    if slot is None:
        slot = list(prize_area.children).index(prize_card)
    top_card = deck.children[-1]
    moves = []
    if ctx.board.move_card(prize_card.entity_id, deck.entity_id):
        moves.append(session._entity_moved_msg(
            prize_card.entity_id, deck.entity_id, len(deck.children) - 1))
    if ctx.board.move_card(top_card.entity_id, prize_area.entity_id, slot):
        moves.append(session._entity_moved_msg(
            top_card.entity_id, prize_area.entity_id, slot))
    if moves:
        await session.send_game_sequence(
            list(session.players.values()),
            GameSequence.WITH_OPEN_PRIZE_CARDS, moves)
    ctx.visual_targets = [prize_area.entity_id, deck.entity_id]


async def reel_in(ctx):
    """When played from hand: put up to 3 Pokémon from discard into hand."""
    cards = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if not cards:
        ctx.suppress_announce = True
        return
    picks = await ctx.choose_cards(
        cards, 3, minimum=0,
        prompt="Choose up to 3 Basic Pokémon and/or Evolution cards from your discard pile",
    )
    if picks:
        await ctx.put_in_hand(picks)


class HayFeverPassive(Passive):
    """No Trainer cards can be played. Stops while Asleep, Confused, or Paralyzed."""

    def blocks_trainer_play(self, card, player_id, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return not _asleep_confused_or_paralyzed(holder)


class MindGamesPassive(Passive):
    """Whenever the opponent plays a Trainer card, you may flip a coin.
    Heads: that card does nothing and is put on top of their deck.
    Stops while Asleep, Confused, or Paralyzed (Slowking)."""

    def intercepts_trainer_play(self, card, player_id, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder.owning_player_id == player_id:
            return False
        return not _asleep_confused_or_paralyzed(holder)


mind_games_passive = MindGamesPassive()


async def petal_whirlwind(ctx):
    """30× heads among 3 coins; 2 or more heads Confuses this Pokémon."""
    results = await ctx.flip_coins(3, "Petal Whirlwind")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(30 * heads)
    if heads >= 2:
        await ctx.apply_special_condition(
            ctx.attacker, SpecialConditions.CONFUSED)


_MASS_EXPLOSION_NAMES = frozenset(("Koffing", "Weezing", "Dark Weezing"))


def _is_koffing_line(pokemon) -> bool:
    return getattr(def_for(pokemon.archetype_id), "display_name", None) \
        in _MASS_EXPLOSION_NAMES


async def mass_explosion(ctx):
    """20× Koffing/Weezing/Dark Weezing in play (W/R), then 20 to each of
    those Pokémon with no W/R (including your own)."""
    matches = [
        poked for poked in (
            ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play())
        if _is_koffing_line(poked)
    ]
    if matches:
        await ctx.deal_damage(20 * len(matches))
    for poked in matches:
        await ctx.deal_damage(20, target=poked, apply_modifiers=False)


class MirrorShellPassive(Passive):
    """If an attack damages this Pokémon, attack back for an equal amount
    (even if this Pokémon is Knocked Out)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return None
        attacker = calc.attacker
        if attacker is None:
            return None
        saved = ctx.attacker
        ctx.attacker = holder
        try:
            await ctx.deal_damage(
                calc.amount, target=attacker, apply_modifiers=True)
        finally:
            ctx.attacker = saved
        return None


async def mirror_shell(ctx):
    """During the opponent's next turn, a hit on this Pokémon is reflected
    as an equal-damage attack with W/R (even if this Pokémon is KO'd)."""
    ctx.add_passive_through_opponents_turn(ctx.attacker, MirrorShellPassive())


async def digger(ctx):
    """Alternate coin flips until tails; 10 to that player's Active."""
    hit_self = True
    while True:
        results = await ctx.flip_coins(1, "Digger")
        if not results or not results[0]:
            target = ctx.my_active() if hit_self else ctx.opponent_active()
            if target is not None:
                await ctx.deal_damage(
                    10, target=target, apply_modifiers=False, as_counters=True)
            return
        hit_self = not hit_self


# ----------------------------------------------------------------------
# Base Set (BASE1)
# ----------------------------------------------------------------------

def has_cards_in_deck(board, player_id, pokemon=None) -> bool:
    """Trainer/ability gate: the player's deck is not empty."""
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


def has_energy_cards_attached(n=1):
    """Attack gate: this Pokémon has at least `n` Energy cards attached."""
    def check(board, player_id, pokemon=None) -> bool:
        return pokemon is not None and len(board.attached_energies(pokemon)) >= n
    return check


def damage_swap_condition(board, player_id, pokemon=None) -> bool:
    """A damaged Pokémon can give a counter to another without Knocking it Out."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    mine = board.pokemon_in_play(player_id)
    if len(mine) < 2:
        return False
    damaged = [poked for poked in mine if _is_damaged(board, poked)]
    if not damaged:
        return False
    can_take = [poked for poked in mine if poked.get_attribute(AttrID.HP, 0) > 10]
    return any(any(dest is not source for dest in can_take) for source in damaged)


async def damage_swap(ctx):
    """Move 1 damage counter from 1 of your Pokémon to another without KO."""
    mine = ctx.my_pokemon_in_play()
    damaged = [poked for poked in mine if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to move a damage counter from")
    if source is None:
        return
    dests = [poked for poked in mine
             if poked is not source and poked.get_attribute(AttrID.HP, 0) > 10]
    if not dests:
        return
    dest = await ctx.choose_pokemon(
        dests, "Choose a Pokémon to move the damage counter to")
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)


def strange_behavior_condition(board, player_id, pokemon=None) -> bool:
    """A damaged teammate can give Slowbro a counter without Knocking it Out."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if pokemon is None or pokemon.get_attribute(AttrID.HP, 0) <= 10:
        return False
    return any(
        poked is not pokemon and _is_damaged(board, poked)
        for poked in board.pokemon_in_play(player_id)
    )


async def strange_behavior(ctx):
    """Move 1 damage counter from 1 of your other Pokémon onto this Pokémon."""
    dest = ctx.source
    if dest is None or dest.get_attribute(AttrID.HP, 0) <= 10:
        return
    damaged = [
        poked for poked in ctx.my_pokemon_in_play()
        if poked is not dest and _is_damaged(ctx.board, poked)
    ]
    if not damaged:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to move a damage counter from")
    if source is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)


def rain_dance_condition(board, player_id, pokemon=None) -> bool:
    """Water Energy in hand and a Water Pokémon in play; no Special Conditions."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(
            _typed_basic_energy(c, PokemonTypes.WATER) for c in hand.children):
        return False
    return any(
        pokemon_has_type(poked, PokemonTypes.WATER)
        for poked in board.pokemon_in_play(player_id)
    )


async def rain_dance(ctx):
    """Attach 1 Water Energy from hand to 1 of your Water Pokémon."""
    energies = [c for c in ctx.hand() if _typed_basic_energy(c, PokemonTypes.WATER)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Water Energy card to attach")
    if not picks:
        return
    targets = [poked for poked in ctx.my_pokemon_in_play()
               if pokemon_has_type(poked, PokemonTypes.WATER)]
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Water Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


class EnergyBurnPassive(Passive):
    """Marked Energy cards attached to Charizard provide Fire this turn."""

    def __init__(self):
        self.energy_ids = set()

    def modify_energy_provided(self, options, energy, holder, board):
        if energy.entity_id not in self.energy_ids:
            return options
        fire = PokemonTypes.FIRE.value
        if not options:
            return [[fire]]
        return [[fire] * max(1, len(option)) for option in options]


def energy_burn_condition(board, player_id, pokemon=None) -> bool:
    """Unburned Energy on this Pokémon; no Special Conditions."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if pokemon is None:
        return False
    energies = list(board.attached_energies(pokemon))
    if not energies:
        return False
    burned = set()
    for passive, carrier in _active_passives(board):
        if isinstance(passive, EnergyBurnPassive) \
                and carrier_pokemon(carrier) is pokemon:
            burned = passive.energy_ids
            break
    return any(energy.entity_id not in burned for energy in energies)


async def energy_burn(ctx):
    """Turn all Energy attached to this Pokémon into Fire for the rest of the turn."""
    holder = ctx.source
    if holder is None:
        return
    existing = None
    for passive, carrier in _active_passives(ctx.board):
        if isinstance(passive, EnergyBurnPassive) \
                and carrier_pokemon(carrier) is holder:
            existing = passive
            break
    if existing is None:
        existing = EnergyBurnPassive()
        ctx.add_temporary_passive(
            holder, existing,
            expires_after_turn=ctx.session.turn_state.turn_number,
        )
    existing.energy_ids.update(
        energy.entity_id for energy in ctx.attached_energies(holder))


metronome = copy_defending_attack(require_energy=False, skip_requirements=True)


class DummyPokemonPassive(FossilBodyPassive):
    """Clefairy Doll / Mysterious Fossil: can't retreat, immune to Special
    Conditions, and gives no Prize cards when Knocked Out."""

    def __init__(self):
        super().__init__(blocks_conditions=True)

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is holder:
            return 0
        return count


def dummy_pokemon_abilities():
    """Discard-from-play action shared by Clefairy Doll / Mysterious Fossil."""
    return [fossil_discard_ability()]


def computer_search_condition(board, player_id):
    return (hand_size_at_least(3)(board, player_id)
            and deck_nonempty(board, player_id))


async def computer_search(ctx):
    """Discard 2 other cards, then put any card from the deck into the hand."""
    discarded = await ctx.discard_from_hand(
        2, prompt="Discard 2 of the other cards from your hand")
    if len(discarded) < 2:
        return
    await search_to_hand(
        count=1, minimum=1, reveal=False,
        prompt="Choose a card to put into your hand.",
    )(ctx)


defender_passive = takes_less_passive(20)


async def defender(ctx):
    """Attach this card to 1 of your Pokémon; that Pokémon takes 20 less
    damage from attacks (after W/R). Discard it at the end of the opponent's
    next turn."""
    target = await ctx.choose_play_target(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Defender to")
    if target is None:
        return
    card = ctx.source
    await ctx.attach_energy(card, target)
    card_id = card.entity_id
    owner = ctx.player_id

    async def _discard(session):
        attached = session.board_state.get_entity(card_id)
        if attached is None:
            return
        from spirit.game.session.effects import EffectContext
        discard_ctx = EffectContext(session, owner, attached, None)
        await discard_ctx.discard_cards([attached])
        await session._flush_effect_runs(discard_ctx)

    ctx.schedule_at_checkup(1, _discard)


def devolution_spray_condition(board, player_id):
    return any(devolvable(poked) for poked in board.pokemon_in_play(player_id))


def devolution_spray_targets(board, player_id, card=None):
    return [poked for poked in board.pokemon_in_play(player_id)
            if devolvable(poked)]


def _evolution_underlays(pokemon):
    """Previous stages tucked under `pokemon`, highest first."""
    stages = []
    current = pokemon
    while True:
        evolves_from = current.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
        nxt = next(
            (child for child in current.children
             if isinstance(child, PokemonEntity)
             and child.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == evolves_from),
            None,
        ) if evolves_from else None
        if nxt is None:
            return stages
        stages.append(nxt)
        current = nxt


async def devolution_spray(ctx):
    """Devolve 1 of your Pokémon, discarding that Stage or higher; conditions
    and attack effects clear as if it had just evolved."""
    evolved = devolution_spray_targets(ctx.board, ctx.player_id)
    if not evolved:
        return
    target = await ctx.choose_play_target(
        evolved, "Choose a Pokémon to devolve")
    if target is None:
        return
    underlays = _evolution_underlays(target)
    if not underlays:
        return
    steps = 1
    if len(underlays) > 1:
        labels = [
            getattr(def_for(stage.archetype_id), "display_name", None) or "Pokémon"
            for stage in underlays
        ]
        steps = 1 + await ctx.choose(
            "Choose a Stage of Evolution to devolve to.", labels)
    await ctx.devolve_pokemon(target, steps=steps, destination="discard")


async def impostor_professor_oak(ctx):
    """Opponent shuffles their hand into their deck, then draws 7 cards."""
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    await ctx.draw_cards(7, ctx.opponent_id)


def item_finder_condition(board, player_id, pokemon=None) -> bool:
    """2 other cards in hand and a Trainer in the discard pile."""
    return (requires_hand(n=2)(board, player_id, pokemon)
            and requires_discard(is_trainer_card)(board, player_id, pokemon))


async def item_finder(ctx):
    """Discard 2 other cards, then put a Trainer from discard into hand.
    Cards discarded as the cost cannot be the Trainer retrieved."""
    discarded = await ctx.discard_from_hand(
        2, prompt="Discard 2 cards for Item Finder")
    if len(discarded) < 2:
        return
    cards = [c for c in ctx.discard_pile()
             if is_trainer_card(c) and c not in discarded]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1,
        prompt="Choose a Trainer card from your discard pile")
    if picks:
        await ctx.put_in_hand(picks)


async def lass(ctx):
    """Both players reveal their hands, then shuffle Trainer cards into decks."""
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    await ctx.reveal_hand(of_player=ctx.player_id, to_player=ctx.opponent_id)
    for pid in (ctx.player_id, ctx.opponent_id):
        trainers = [c for c in ctx.hand(pid) if is_trainer_card(c)]
        if trainers:
            await ctx.shuffle_into_deck(trainers, pid)


class BenchGuardPassive(Passive):
    """While this Pokémon is Benched, you may do 10 of each other Benched
    Pokémon's damage to this Pokémon instead (Brock's Rhydon)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if getattr(ctx, "_bench_guard_redirecting", False) or calc.amount <= 0:
            return None
        holder = carrier_pokemon(carrier) or carrier
        if holder is None or target is holder:
            return None
        if holder.owning_player_id != target.owning_player_id:
            return None
        if is_in_active_spot(holder) or is_in_active_spot(target):
            return None
        redirected = min(10, calc.amount)
        name = getattr(def_for(holder.archetype_id), "display_name", None) \
            or "this Pokémon"
        if not await ctx.ask_yes_no(
                f"Do {redirected} of that damage to {name} instead?",
                player_id=holder.owning_player_id):
            return None
        ctx._bench_guard_redirecting = True
        was = ctx._in_interceptor
        try:
            ctx._in_interceptor = False
            await ctx.deal_damage(
                redirected, target=holder, apply_modifiers=False)
        finally:
            ctx._in_interceptor = was
            ctx._bench_guard_redirecting = False
        return calc.amount - redirected


bench_guard_passive = BenchGuardPassive()


async def strikes_back(ctx):
    """When damaged by an opponent's attack (even if Knocked Out), do 10
    damage to the attacker with no W/R. Stops while Asleep, Confused, or
    Paralyzed."""
    holder = ctx.source
    attacker = ctx.damaged_by
    if (holder is None or attacker is None
            or _asleep_confused_or_paralyzed(holder)
            or attacker.owning_player_id == holder.owning_player_id):
        ctx.suppress_announce = True
        return
    await ctx.deal_damage(10, target=attacker, apply_modifiers=False)


async def energy_removal(ctx):
    """Discard 1 Energy card attached to 1 of the opponent's Pokémon."""
    candidates = [
        poked for poked in ctx.opponent_pokemon_in_play()
        if ctx.attached_energies(poked)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.discard_energy_from(
        target, 1, prompt="Choose an Energy card to discard")


_LEEK_SLAP_USED = "_leek_slap_used"
_LEEK_SLAP_USED_TURN = "_leek_slap_used_turn"


def leek_slap_available(board, player_id, pokemon=None) -> bool:
    """Leek Slap can't be used again while this Farfetch'd stays in play."""
    if pokemon is None:
        return False
    if not pokemon.get_attribute(_LEEK_SLAP_USED):
        return True
    state = getattr(board, "turn_state", None)
    if state is None:
        return False
    entered = state.entered_play_turn.get(pokemon.entity_id)
    used_turn = pokemon.get_attribute(_LEEK_SLAP_USED_TURN)
    return (entered is not None and used_turn is not None
            and entered > used_turn)


async def leek_slap(ctx):
    """Flip: heads deals printed damage. Either way, lock this attack in play."""
    title = ctx.ability.title if ctx.ability else "Leek Slap"
    results = await ctx.flip_coins(1, title)
    attacker = ctx.attacker
    if attacker is not None:
        attacker.set_attribute(_LEEK_SLAP_USED, True)
        attacker.set_attribute(
            _LEEK_SLAP_USED_TURN, ctx.session.turn_state.turn_number)
    if results and results[0]:
        await ctx.deal_damage()


class DestinyBondPassive(Passive):
    """If this Pokémon is Knocked Out by an attack during the opponent's
    next turn, Knock Out the attacking Pokémon."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return None
        current = target.get_attribute(AttrID.HP, 0)
        if calc.amount < current:
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.knock_out(attacker)
        return None


async def destiny_bond(ctx):
    """Discard 1 Psychic Energy; if this Pokémon is KO'd by an attack during
    the opponent's next turn, KO that Pokémon."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: _typed_basic_energy(card, PokemonTypes.PSYCHIC),
        prompt="Choose a Psychic Energy card to discard")
    if not discarded:
        return
    ctx.add_passive_through_opponents_turn(ctx.attacker, DestinyBondPassive())


def buzzap_condition(board, player_id, pokemon=None) -> bool:
    """Another of your Pokémon is in play; no Special Conditions."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return any(poked is not pokemon for poked in board.pokemon_in_play(player_id))


async def buzzap(ctx):
    """Knock Out Electrode, attach it as a Special Energy providing 2 of a
    chosen type to 1 of your other Pokémon."""
    electrode = ctx.source
    others = [poked for poked in ctx.my_pokemon_in_play() if poked is not electrode]
    if electrode is None or not others:
        return
    types = [option[0] for option in ALL_TYPES_ONE_AT_A_TIME]
    names = [CLIENT_POKEMON_TYPE_NAMES[energy_type] for energy_type in types]
    idx = await ctx.choose("Choose a type of Energy.", names)
    chosen = types[idx]
    target = await ctx.choose_pokemon(
        others, "Choose a Pokémon to attach Electrode to")
    if target is None:
        return
    electrode_id = electrode.entity_id
    target_id = target.entity_id
    await ctx.knock_out(electrode)

    async def _attach_as_energy():
        card = ctx.board.get_entity(electrode_id)
        holder = ctx.board.get_entity(target_id)
        if card is None or not isinstance(holder, PokemonEntity):
            return
        if holder not in ctx.my_pokemon_in_play():
            return
        card.__class__ = EnergyEntity
        info = {"options": [[chosen.value, chosen.value]]}
        card.set_attribute(AttrID.CARD_TYPE, CardType.ENERGY.value)
        card.set_attribute(AttrID.IS_SPECIAL_ENERGY, True)
        card.set_attribute(AttrID.ENERGY_INFO, info)
        session = ctx.session
        await session._broadcast_entity_attribute(
            card, AttrID.CARD_TYPE, CardType.ENERGY.value)
        await session._broadcast_entity_attribute(
            card, AttrID.IS_SPECIAL_ENERGY, True)
        await session._broadcast_entity_attribute(
            card, AttrID.ENERGY_INFO, info)
        position = len(holder.children)
        if not ctx.board.attach_card(card.entity_id, holder.entity_id):
            return
        intro = session._entity_introduced_msg(card)
        move = session._entity_moved_msg(
            card.entity_id, holder.entity_id, position)
        players = list(session.players.values())
        await session.send_game_sequence(
            players, GameSequence.SERIAL_SEQUENCE, [intro])
        await session.send_game_sequence(
            players, GameSequence.GROUPED_MOVE, [move])

    ctx.deferred_actions.append(_attach_as_energy)


async def amnesia(ctx):
    """Choose 1 of the Defending Pokémon's attacks; it can't use that attack
    during the opponent's next turn."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
               if isinstance(e, dict) and e.get("abilityType") == "Attack"
               and e.get("abilityID")]
    if not entries:
        return
    titles = [e.get("title", {}).get("id", "Attack") for e in entries]
    idx = await ctx.choose("Choose an attack to lock", titles)
    entry = entries[idx]
    ctx.session.turn_state.attack_locks[(defender.entity_id, entry["abilityID"])] = \
        ctx.session.turn_state.turn_number + 1


pokemon_trader_condition = requires_hand(is_pokemon_card)


async def pokemon_trader(ctx):
    """Trade 1 Pokémon in hand for 1 Pokémon from the deck; show both, shuffle."""
    matches = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1, prompt="Choose a Pokémon to put into your deck")
    if not picks:
        return
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks)
    found = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=1,
        prompt="Choose a Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


async def super_fang(ctx):
    """Damage equal to half the Defending Pokémon's remaining HP, rounded up
    to the nearest 10."""
    defender = ctx.defender
    if defender is None:
        return
    hp = defender.get_attribute(AttrID.HP, 0)
    amount = ((hp // 10 + 1) // 2) * 10
    if amount > 0:
        await ctx.deal_damage(amount)


async def false_swipe(ctx):
    """Damage equal to half the Defending Pokémon's remaining HP, rounded
    down to the nearest 10 (Neo Discovery Scizor)."""
    defender = ctx.defender
    if defender is None:
        return
    hp = defender.get_attribute(AttrID.HP, 0)
    amount = (hp // 20) * 10
    if amount > 0:
        await ctx.deal_damage(amount)


def revive_condition(board, player_id, pokemon=None) -> bool:
    return (requires_discard(is_basic_pokemon)(board, player_id, pokemon)
            and bench_has_room(board, player_id))


async def revive(ctx):
    """Put 1 Basic Pokémon from discard onto the Bench with damage counters
    equal to half its HP (rounded down to the nearest 10)."""
    cards = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your discard pile")
    if not picks:
        return
    card = picks[0]
    if not await ctx.bench_pokemon(card):
        return
    counters = ctx.max_hp(card) // 20
    if counters:
        await ctx.set_damage_counters(card, counters)


def maintenance_condition(board, player_id, pokemon=None) -> bool:
    """2 other cards in hand to shuffle in for Maintenance."""
    return requires_hand(n=2)(board, player_id, pokemon)


async def maintenance(ctx):
    """Shuffle 2 other cards from hand into the deck, then draw 1."""
    picks = await ctx.choose_cards(
        list(ctx.hand()), 2,
        prompt="Shuffle 2 of the other cards from your hand into your deck.")
    if len(picks) < 2:
        return
    await ctx.shuffle_into_deck(picks)
    await ctx.draw_cards(1)


def has_psychic_energy_attached(board, player_id, pokemon=None) -> bool:
    """Attack gate: this Pokémon has a Psychic Energy card attached."""
    if pokemon is None:
        return False
    return any(energy_provides_type(e, PokemonTypes.PSYCHIC.value)
               for e in board.attached_energies(pokemon))


async def barrier(ctx):
    """Discard 1 Psychic Energy; prevent all effects of attacks, including
    damage, done to this Pokémon during the opponent's next turn."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: energy_provides_type(
            card, PokemonTypes.PSYCHIC.value),
        prompt="Choose a Psychic Energy card to discard")
    if not discarded:
        return
    await apply_protection(ctx, prevent=True, effects_too=True)


def _player_has_energy_attached(board, player_id) -> bool:
    return any(board.attached_energies(poked)
               for poked in board.pokemon_in_play(player_id))


async def scoop_up(ctx):
    """Return the Basic Pokémon card to hand; discard all other attached cards."""
    mine = ctx.my_pokemon_in_play()
    if not mine:
        return
    target = await ctx.choose_pokemon(
        mine, "Choose 1 of your Pokémon")
    if target is None:
        return
    owner = target.owning_player_id or ctx.player_id
    was_active = target is ctx.board.active_pokemon(owner)
    underlays = _evolution_underlays(target)
    basic = underlays[-1] if underlays else target
    leftovers = [c for c in full_stack(target) if c is not basic]
    if leftovers:
        await ctx.discard_cards(leftovers)
    await ctx.put_in_hand([basic], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(owner):
                screen_name = ctx.session.players[owner].screen_name
                await ctx.session.end_game(
                    ctx.session._opponent_id(owner),
                    f"{screen_name} has no Pokémon left",
                )
        ctx.deferred_actions.append(_promote)


def _entered_play_this_turn(board, pokemon) -> bool:
    state = getattr(board, "turn_state", None)
    if state is None or pokemon is None:
        return False
    return state.entered_play_turn.get(pokemon.entity_id, 0) >= state.turn_number


def cowardice_condition(board, player_id, pokemon=None) -> bool:
    """Return-to-hand gate: another Pokémon in play, not the turn this
    Pokémon entered play, and no Special Conditions."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    if _entered_play_this_turn(board, pokemon):
        return False
    return has_bench(board, player_id, pokemon)


async def cowardice(ctx):
    """Return this Pokémon to hand; discard all cards attached to it."""
    pokemon = ctx.source
    if pokemon is None:
        return
    owner = pokemon.owning_player_id or ctx.player_id
    was_active = pokemon is ctx.board.active_pokemon(owner)
    leftovers = [c for c in full_stack(pokemon) if c is not pokemon]
    if leftovers:
        await ctx.discard_cards(leftovers)
    await ctx.put_in_hand([pokemon], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(owner):
                screen_name = ctx.session.players[owner].screen_name
                await ctx.session.end_game(
                    ctx.session._opponent_id(owner),
                    f"{screen_name} has no Pokémon left",
                )
        ctx.deferred_actions.append(_promote)


def super_energy_removal_condition(board, player_id, pokemon=None) -> bool:
    """Both players have an Energy card attached to a Pokémon."""
    opponent = _opponent_id(board, player_id)
    return (opponent is not None
            and _player_has_energy_attached(board, player_id)
            and _player_has_energy_attached(board, opponent))


async def super_energy_removal(ctx):
    """Discard 1 Energy from yours, then up to 2 Energy from 1 of theirs."""
    mine = [poked for poked in ctx.my_pokemon_in_play()
            if ctx.attached_energies(poked)]
    if not mine:
        return
    source = await ctx.choose_pokemon(
        mine, "Choose 1 of your Pokémon")
    if source is None:
        return
    discarded = await ctx.discard_energy_from(
        source, 1, prompt="Choose an Energy card to discard")
    if not discarded:
        return
    theirs = [poked for poked in ctx.opponent_pokemon_in_play()
              if ctx.attached_energies(poked)]
    if not theirs:
        return
    target = await ctx.choose_pokemon(
        theirs, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    energies = ctx.attached_energies(target)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 Energy cards to discard")
    if picks:
        await ctx.discard_cards(picks)


def super_potion_condition(board, player_id, pokemon=None) -> bool:
    """A damaged Pokémon of yours has an Energy card attached."""
    return any(
        _is_damaged(board, poked) and board.attached_energies(poked)
        for poked in board.pokemon_in_play(player_id)
    )


async def super_potion(ctx):
    """Discard 1 Energy from 1 of your Pokémon, then heal 40 from it."""
    candidates = [
        poked for poked in ctx.my_pokemon_in_play()
        if _is_damaged(ctx.board, poked) and ctx.attached_energies(poked)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to heal")
    if target is None:
        return
    discarded = await ctx.discard_energy_from(
        target, 1, prompt="Choose an Energy card to discard")
    if not discarded:
        return
    await ctx.heal(40, target)


def energy_trans_condition(board, player_id, pokemon=None) -> bool:
    """Grass Energy on 1 of your Pokémon and another Pokémon to take it;
    no Special Conditions."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    mine = board.pokemon_in_play(player_id)
    if len(mine) < 2:
        return False
    return any(
        any(_typed_basic_energy(energy, PokemonTypes.GRASS)
            for energy in board.attached_energies(poked))
        for poked in mine
    )


async def energy_trans(ctx):
    """Move 1 Grass Energy card from 1 of your Pokémon to another."""
    sources = [
        poked for poked in ctx.my_pokemon_in_play()
        if any(_typed_basic_energy(energy, PokemonTypes.GRASS)
               for energy in ctx.attached_energies(poked))
    ]
    if not sources:
        return
    source = await ctx.choose_pokemon(
        sources, "Choose a Pokémon with Grass Energy attached")
    if source is None:
        return
    energies = [
        energy for energy in ctx.attached_energies(source)
        if _typed_basic_energy(energy, PokemonTypes.GRASS)
    ]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Grass Energy card to move")
    if not picks:
        return
    dests = [poked for poked in ctx.my_pokemon_in_play() if poked is not source]
    if not dests:
        return
    dest = await ctx.choose_pokemon(
        dests, "Choose a Pokémon to attach the Energy to")
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


def harden(threshold: int = 30):
    """During the opponent's next turn, prevent attack damage of
    `threshold` or less after Weakness and Resistance."""
    async def effect(ctx):
        holder = ctx.attacker or ctx.source
        if holder is None:
            return
        ctx.add_passive_through_opponents_turn(
            holder, prevent_damage_when(lambda calc, _c: calc.amount <= threshold)
        )
    return effect


def mirror_move_condition(board, player_id, pokemon=None) -> bool:
    """This Pokémon took attack damage from the opponent last turn."""
    if pokemon is None:
        return False
    state = getattr(board, "turn_state", None)
    if state is None:
        return False
    return state.damage_taken_last_turn.get(pokemon.entity_id, 0) > 0


async def mirror_move(ctx):
    """Do last turn's damage taken by this Pokémon to the Defending Pokémon."""
    attacker = ctx.attacker
    if attacker is None:
        return
    amount = ctx.damage_taken_last_turn(attacker)
    if amount > 0:
        await ctx.deal_damage(amount)


class PlusPowerPassive(Passive):
    """Holder's attacks do +10 to the Defending Pokémon after W/R, if they
    already do damage."""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if holder is not calc.attacker or calc.amount <= 0:
            return
        calc.amount += 10


plus_power_passive = PlusPowerPassive()


async def plus_power(ctx):
    """Attach to your Active Pokémon; discard at the end of this turn."""
    target = ctx.my_active()
    if target is None:
        return
    card = ctx.source
    await ctx.attach_energy(card, target)
    card_id = card.entity_id
    owner = ctx.player_id

    async def _discard(session):
        attached = session.board_state.get_entity(card_id)
        if attached is None:
            return
        from spirit.game.session.effects import EffectContext
        discard_ctx = EffectContext(session, owner, attached, None)
        await discard_ctx.discard_cards([attached])
        await session._flush_effect_runs(discard_ctx)

    ctx.schedule_at_checkup(0, _discard)


async def pokedex(ctx):
    """Look at up to 5 cards from the top of your deck and rearrange them."""
    await ctx.reorder_deck_top(5)


def _breeder_map(board, player_id):
    """Stage 2 in hand -> matching Basics that may evolve this turn."""
    hand = board.find_player_area(player_id, "hand")
    turn_state = getattr(board, "turn_state", None)
    if not hand or turn_state is None:
        return {}
    basics = [
        poked for poked in board.pokemon_in_play(player_id)
        if is_basic_pokemon(poked) and turn_state.may_evolve_target(poked.entity_id)
    ]
    mapping = {}
    for card in hand.children:
        if not is_pokemon_card(card):
            continue
        if card.get_attribute(AttrID.STAGE) != PokemonStage.STAGE2.value:
            continue
        matches = [
            poked for poked in basics
            if evolves_from(
                card.archetype_id,
                poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or "",
            )
        ]
        if matches:
            mapping[card] = matches
    return mapping


def pokemon_breeder_condition(board, player_id) -> bool:
    """A Stage 2 in hand matches a Basic you would be allowed to evolve."""
    return bool(_breeder_map(board, player_id))


async def pokemon_breeder(ctx):
    """Put a Stage 2 from hand onto a matching Basic you may evolve."""
    mapping = _breeder_map(ctx.board, ctx.player_id)
    if not mapping:
        return
    picks = await ctx.choose_cards(
        list(mapping), 1, minimum=1,
        prompt="Choose a Stage 2 Evolution card",
    )
    if not picks:
        return
    stage2 = picks[0]
    basics = mapping.get(stage2) or []
    if not basics:
        return
    target = basics[0] if len(basics) == 1 else await ctx.choose_pokemon(
        basics, "Choose a Basic Pokémon to evolve")
    if target is None:
        return
    await ctx.evolve_pokemon(target, stage2)


async def pokemon_center(ctx):
    """Heal all damage from each of your damaged Pokémon, then discard all
    Energy cards attached to those Pokémon."""
    damaged = [
        poked for poked in ctx.my_pokemon_in_play()
        if _is_damaged(ctx.board, poked)
    ]
    for poked in damaged:
        amount = ctx.max_hp(poked) - poked.get_attribute(AttrID.HP, 0)
        if amount > 0:
            await ctx.heal(amount, poked)
        await ctx.discard_energy_from(
            poked, 99, prompt="Discard all Energy attached to this Pokémon")


def pokemon_flute_condition(board, player_id) -> bool:
    """Opponent has a Basic in the discard pile and room on the Bench."""
    opponent = _opponent_id(board, player_id)
    if not opponent:
        return False
    discard = board.find_player_area(opponent, "discard")
    if not discard or not any(is_basic_pokemon(c) for c in discard.children):
        return False
    return bench_has_room(board, opponent)


async def pokemon_flute(ctx):
    """Put a Basic from the opponent's discard pile onto their Bench."""
    candidates = [
        c for c in ctx.discard_pile(ctx.opponent_id) if is_basic_pokemon(c)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your opponent's discard pile",
    )
    for card in picks:
        await ctx.bench_pokemon(card)


# ----------------------------------------------------------------------
# Jungle (BASE2)
# ----------------------------------------------------------------------

def named_basic(*names):
    """Deck-search predicate: a Basic Pokémon whose evolution-logic name is
    one of `names` (Oddish Sprout, Bellsprout Call for Family)."""
    wanted = set(names)

    def pred(card) -> bool:
        return (is_basic_pokemon(card)
                and card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in wanted)
    return pred


def call_for_family_condition(board, player_id, pokemon=None) -> bool:
    """Sprout / Call for Family: deck nonempty and Bench not full."""
    return has_cards_in_deck(board, player_id, pokemon) and bench_has_room(
        board, player_id)


def reduce_if_defending_attacks(amount: int):
    """Printed damage, then: if that Defending Pokémon attacks this Pokémon
    during the opponent's next turn, reduce that damage by `amount` after
    W/R. Benching either Pokémon ends the effect (Pounce, Snivel)."""
    async def effect(ctx):
        await ctx.deal_damage()
        user = ctx.attacker
        defending = ctx.defender
        if user is None or defending is None:
            return
        defending_id = defending.entity_id
        ctx.add_passive_through_opponents_turn(
            user,
            takes_less_passive(
                amount,
                attacker_pred=lambda attacker: attacker.entity_id == defending_id,
            ),
        )
    return effect


async def hurricane(ctx):
    """Printed damage; unless that Knocks Out the Defending Pokémon, return
    it and all attached cards to the opponent's hand (needs a Bench to
    promote)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    if defender.get_attribute(AttrID.HP, 0) <= 0:
        return
    if ctx.effects_blocked(defender):
        return
    if not ctx.opponent_bench():
        return
    owner = defender.owning_player_id or ctx.opponent_id
    await ctx.put_in_hand(full_stack(defender), reveal=False)

    async def _promote():
        if not await ctx.session._promote_new_active(owner):
            screen_name = ctx.session.players[owner].screen_name
            await ctx.session.end_game(
                ctx.session._opponent_id(owner),
                f"{screen_name} has no Pokémon left",
            )
    ctx.deferred_actions.append(_promote)


async def poke_ball(ctx):
    """Flip a coin. If heads, you may search the deck for a Basic Pokémon or
    Evolution card, show it, and put it into your hand; then shuffle."""
    if (await ctx.flip_coins(1, "Poké Ball"))[0]:
        await search_to_hand(
            is_pokemon_card, count=1, reveal=True,
            prompt="Choose a Basic Pokémon or Evolution card.",
        )(ctx)


def basic_of_type(pokemon_type: PokemonTypes):
    """Deck-search predicate: a Basic Pokémon of `pokemon_type`."""
    def pred(card) -> bool:
        return is_basic_pokemon(card) and pokemon_has_type(card, pokemon_type)
    return pred


def _invisible_wall_blocks(calc, carrier) -> bool:
    holder = carrier_pokemon(carrier) or carrier
    if not calc.is_attack or calc.target is not holder or calc.amount < 30:
        return False
    return not _asleep_confused_or_paralyzed(holder)


invisible_wall = prevent_damage_when(_invisible_wall_blocks, attacks_only=False)


def _peek_choices(board, player_id):
    opponent = _opponent_id(board, player_id)
    options = []
    labels = []
    my_deck = board.find_player_area(player_id, "deck")
    if my_deck and my_deck.children:
        options.append(("deck", player_id))
        labels.append("Top of your deck")
    if opponent:
        opp_deck = board.find_player_area(opponent, "deck")
        if opp_deck and opp_deck.children:
            options.append(("deck", opponent))
            labels.append("Top of your opponent's deck")
        opp_hand = board.find_player_area(opponent, "hand")
        if opp_hand and opp_hand.children:
            options.append(("hand", opponent))
            labels.append("A random card from your opponent's hand")
    my_prizes = board.find_player_area(player_id, "prizePile")
    if my_prizes and my_prizes.children:
        options.append(("prizes", player_id))
        labels.append("Your Prizes")
    if opponent:
        opp_prizes = board.find_player_area(opponent, "prizePile")
        if opp_prizes and opp_prizes.children:
            options.append(("prizes", opponent))
            labels.append("Opponent's Prizes")
    return options, labels


def peek_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    options, _labels = _peek_choices(board, player_id)
    return bool(options)


async def peek(ctx):
    """Look at the top of either deck, a random card from the opponent's
    hand, or one of either player's Prizes."""
    options, labels = _peek_choices(ctx.board, ctx.player_id)
    if not options:
        return
    idx = 0 if len(options) == 1 else await ctx.choose("Peek", labels)
    kind, pid = options[idx]
    if kind == "deck":
        top = ctx.deck_top(1, pid)
        if top:
            await ctx.session.prompt_view_cards(
                ctx.player_id, ctx.source.entity_id, list(top),
                prompt="Top card of the deck",
            )
        return
    if kind == "hand":
        hand = ctx.hand(pid)
        if not hand:
            return
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, [random.choice(hand)],
            prompt="A random card from your opponent's hand",
        )
        return
    await _look_at_prizes(ctx, pid, 1)


async def pay_day(ctx):
    """Printed damage; heads, draw a card."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Pay Day")
    if results and results[0]:
        await ctx.draw_cards(1)


_SHIFT_TYPE_ATTR = "_shift_type"


class ShiftPassive(Passive):
    """Venomoth Shift: while `_shift_type` is set, that value replaces
    the Pokémon's printed types."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        override = pokemon.get_attribute(_SHIFT_TYPE_ATTR)
        if override is None:
            return types
        return [override]


def _other_in_play_types(board, self_pokemon) -> list:
    """Non-Colorless types among every other Pokémon in play."""
    skip = {PokemonTypes.COLORLESS.value, PokemonTypes.NO_COLOR.value}
    found = set()
    for player_id in board.player_ids:
        for poked in board.pokemon_in_play(player_id):
            if poked is self_pokemon:
                continue
            for type_value in effective_pokemon_types(board, poked):
                if type_value not in skip:
                    found.add(type_value)
    return sorted(found)


def shift_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return bool(_other_in_play_types(board, pokemon))


async def shift(ctx):
    """Change this Pokémon's type to a non-Colorless type of any other
    Pokémon in play."""
    holder = ctx.source
    if holder is None:
        return
    types = _other_in_play_types(ctx.board, holder)
    if not types:
        return
    names = [CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(t)] for t in types]
    idx = 0 if len(types) == 1 else await ctx.choose(
        "Select the new type of Venomoth", names)
    holder.set_attribute(_SHIFT_TYPE_ATTR, types[idx])


def vileplume_heal_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return any(_is_damaged(board, poked)
               for poked in board.pokemon_in_play(player_id))


async def vileplume_heal(ctx):
    """Flip: heads, remove 1 damage counter from 1 of your Pokémon."""
    results = await ctx.flip_coins(1, "Heal")
    if not results or not results[0]:
        return
    damaged = [poked for poked in ctx.my_pokemon_in_play()
               if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(
        damaged, "Select 1 Pokémon to remove 1 damage")
    if target is not None:
        await ctx.heal(10, target)


async def petal_dance(ctx):
    """Printed × heads among 3 coins; then this Pokémon is Confused."""
    results = await ctx.flip_coins(3, "Petal Dance")
    heads = sum(1 for result in results if result)
    per = getattr(ctx.ability, "damage", 0) or 40
    if heads:
        await ctx.deal_damage(per * heads)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


async def leech_life(ctx):
    """Deal printed damage; heal the attacker by the damage actually done
    (after Weakness and Resistance)."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)


class ThickSkinnedPassive(Passive):
    """Can't become Asleep, Confused, Paralyzed, or Poisoned. Stops while
    already Asleep, Confused, or Paralyzed."""

    _blocked = (
        SpecialConditions.ASLEEP,
        SpecialConditions.CONFUSED,
        SpecialConditions.PARALYZED,
        SpecialConditions.POISONED,
    )

    def blocks_special_conditions(self, target, condition, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder or condition not in self._blocked:
            return False
        return not _asleep_confused_or_paralyzed(holder)


class CantAttackThisPokemonPassive(Passive):
    """The locked Pokémon can't attack this Pokémon (Leer / Tail Wag).
    Benching either Pokémon ends the effect: this passive rides the user
    (cleared on bench), and the locked Pokémon must still be Active."""

    def __init__(self, locked_pokemon):
        self.locked = locked_pokemon

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not calc.target or not calc.is_attack:
            return False
        attacker = calc.attacker
        return attacker is not None and attacker.entity_id == self.locked.entity_id

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not target:
            return False
        return is_in_active_spot(self.locked)


async def cant_attack_this_pokemon(ctx):
    """Heads: the Defending Pokémon can't attack this Pokémon during the
    opponent's next turn. Benching either Pokémon ends the effect."""
    title = ctx.ability.title if ctx.ability else ""
    results = await ctx.flip_coins(1, title)
    if not results or not results[0]:
        return
    attacker = ctx.attacker
    defender = ctx.defender
    if attacker is None or defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(
        attacker, CantAttackThisPokemonPassive(defender)
    )


class GrowlReducePassive(Passive):
    """Damage this Pokémon takes from the locked attacker is reduced by
    `amount` before W/R (Growl). Benching either Pokémon ends the effect:
    this rides the user, and the locked Pokémon must still be Active."""

    def __init__(self, locked_pokemon, amount=10):
        self.locked = locked_pokemon
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        if calc.ignore_target_effects:
            return
        holder = carrier_pokemon(carrier)
        if holder is not calc.target or not calc.is_attack:
            return
        attacker = calc.attacker
        if attacker is None or attacker.entity_id != self.locked.entity_id:
            return
        if not is_in_active_spot(self.locked):
            return
        calc.amount = max(0, calc.amount - self.amount)


async def growl(ctx):
    """If the Defending Pokémon attacks this Pokémon next turn, damage is
    reduced by 10 before W/R. Benching or evolving either ends this."""
    attacker = ctx.attacker
    defender = ctx.defender
    if attacker is None or defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(
        attacker, GrowlReducePassive(defender, 10)
    )


async def tantrum(ctx):
    """Printed damage; tails, this Pokémon is Confused."""
    await ctx.deal_damage()
    title = ctx.ability.title if ctx.ability else "Tantrum"
    results = await ctx.flip_coins(1, title)
    if results and not results[0]:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


async def ram(ctx):
    """Printed damage; 20 to self; opponent then switches if they have a Bench
    (even if this Pokémon is Knocked Out)."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    old_active = ctx.opponent_active()
    if old_active is None or not ctx.opponent_bench() \
            or ctx.effects_blocked(old_active):
        return
    await opponent_switches(ctx)


async def mega_drain(ctx):
    """Deal printed damage; heal half of that damage (after W/R), rounded
    up to the nearest 10, from the attacker."""
    dealt = await ctx.deal_damage()
    if dealt <= 0:
        return
    heal_amount = (((dealt + 1) // 2 + 9) // 10) * 10
    if heal_amount > 0:
        await ctx.heal(heal_amount, ctx.attacker)


class RetreatAidPassive(Passive):
    """While this Pokémon is Benched, your Active Pokémon costs Colorless
    less to retreat."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if holder is None or is_in_active_spot(holder):
            return cost
        if not is_in_active_spot(pokemon):
            return cost
        if pokemon.owning_player_id != holder.owning_player_id:
            return cost
        return max(0, cost - 1)


async def chain_lightning(ctx):
    """Printed damage; if the Defending Pokémon isn't Colorless, 10 to each
    Benched Pokémon of the same type as the Defending Pokémon (both sides)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    types = set(effective_pokemon_types(ctx.board, defender))
    if not types or PokemonTypes.COLORLESS.value in types:
        return
    for poked in list(ctx.opponent_bench()) + list(ctx.my_bench()):
        if types & set(effective_pokemon_types(ctx.board, poked)):
            await ctx.deal_damage(10, target=poked)


# ----------------------------------------------------------------------
# Fossil (BASE3)
# ----------------------------------------------------------------------

def curse_condition(board, player_id, pokemon=None) -> bool:
    """Gengar Curse: opponent has 2+ Pokémon and at least one is damaged."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    opp = board.pokemon_in_play(opponent)
    if len(opp) < 2:
        return False
    return any(_is_damaged(board, poked) for poked in opp)


async def curse(ctx):
    """Move 1 damage counter from 1 of the opponent's Pokémon to another
    (may Knock Out the destination)."""
    damaged = [poked for poked in ctx.opponent_pokemon_in_play()
               if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to move a damage counter from")
    if source is None:
        return
    dests = [poked for poked in ctx.opponent_pokemon_in_play()
             if poked is not source]
    if not dests:
        return
    dest = await ctx.choose_pokemon(
        dests, "Choose a Pokémon to move the damage counter to")
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)


async def energy_conversion(ctx):
    """Put up to 2 Energy cards from discard into hand; 10 damage to self."""
    energies = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if energies:
        picks = await ctx.choose_cards(
            energies, 2, minimum=0,
            prompt="Choose up to 2 Energy cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    await ctx.deal_damage(10, target=ctx.attacker, apply_modifiers=False)


async def gambler(ctx):
    """Shuffle your hand into your deck; heads draw 8, tails draw 1."""
    await ctx.shuffle_into_deck(ctx.hand())
    results = await ctx.flip_coins(1, "Gambler")
    await ctx.draw_cards(8 if results and results[0] else 1)


async def mr_fuji(ctx):
    """Shuffle 1 of your Benched Pokémon and all attached cards into your deck."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_play_target(
        bench, "Choose a Benched Pokémon to shuffle into your deck")
    if target is None:
        return
    await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)


async def recycle(ctx):
    """Flip a coin. If heads, put a discard-pile card on top of your deck."""
    results = await ctx.flip_coins(1, "Recycle")
    if not results or not results[0]:
        return
    pile = ctx.discard_pile()
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1,
        prompt="Choose a card from your discard pile to put on top of your deck.",
    )
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


def _toxic_gas_target(pokemon, carrier) -> bool:
    holder = carrier_pokemon(carrier) or carrier
    if _asleep_confused_or_paralyzed(holder):
        return False
    # Fossil discards are trainer rules text, not Pokémon Powers.
    return not getattr(def_for(pokemon.archetype_id), "plays_as_pokemon", False)


toxic_gas_passive = ability_lock_passive(_toxic_gas_target)


class ClairvoyancePassive(Passive):
    """Opponent plays with their hand face up. Stops while Asleep, Confused,
    or Paralyzed."""

    def reveals_hand(self, owner_id, viewer_id, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is None or _asleep_confused_or_paralyzed(holder):
            return False
        return (viewer_id == holder.owning_player_id
                and owner_id != holder.owning_player_id)


async def headache(ctx):
    """The opponent can't play Trainer cards during their next turn."""
    ctx.lock_plays(ctx.opponent_id, is_trainer_card)


_TRANSPARENCY_ATTR = "_transparency_prevented"


class TransparencyPassive(Passive):
    """Whenever an opposing attack does anything to this Pokémon, flip:
    heads prevents all effects of that attack, including damage.
    Stops while Asleep, Confused, or Paralyzed."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not target:
            return None
        holder.set_attribute(_TRANSPARENCY_ATTR, False)
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if _asleep_confused_or_paralyzed(holder):
            return None
        heads = await ctx.flip_coins(1, "Transparency", source=holder)
        if heads and heads[0]:
            holder.set_attribute(_TRANSPARENCY_ATTR, True)
            calc.prevented = True
            return 0
        return None

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not target:
            return False
        if _asleep_confused_or_paralyzed(holder):
            return False
        return bool(target.get_attribute(_TRANSPARENCY_ATTR))


transparency = TransparencyPassive()


class KabutoArmorPassive(Passive):
    """Halve attack damage after W/R, rounded down to the nearest 10
    (including your own attacks). Stops while Asleep, Confused, or Paralyzed."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack:
            return
        holder = carrier_pokemon(carrier) or carrier
        if calc.target is not holder:
            return
        if _asleep_confused_or_paralyzed(holder):
            return
        calc.amount = (calc.amount // 20) * 10


kabuto_armor = KabutoArmorPassive()


class PrehistoricPowerPassive(Passive):
    """No Evolution cards can be played. Stops while Asleep, Confused, or
    Paralyzed (Aerodactyl)."""

    def blocks_evolution(self, player_id, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return not _asleep_confused_or_paralyzed(holder)


prehistoric_power = PrehistoricPowerPassive()


async def terror_strike(ctx):
    """Printed damage; heads, the opponent switches if they have a Bench."""
    await ctx.deal_damage()
    if ctx.opponent_bench():
        await flip_or_nothing(then=opponent_switches)(ctx)


async def blizzard(ctx):
    """Printed damage; heads 10 to each opposing Benched Pokémon, tails 10
    to each of your own Benched Pokémon (no W/R on the Bench)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Blizzard")
    bench = ctx.opponent_bench() if results and results[0] else ctx.my_bench()
    for poked in bench:
        await ctx.deal_damage(10, target=poked)


def _opposing_active_via_tree(pokemon):
    """The opposing Active Pokémon, found by walking the playmat tree
    (hooks that do not receive `board`)."""
    area = getattr(pokemon, "parent", None)
    player = getattr(area, "parent", None)
    playmat = getattr(player, "parent", None)
    if playmat is None:
        return None
    owner = pokemon.owning_player_id
    for sibling in playmat.children:
        if getattr(sibling, "owning_player_id", None) in (None, owner):
            continue
        for sub in sibling.children:
            if sub.get_attribute(AttrID.NAME) == "activePokemonArea":
                kids = sub.children
                return kids[0] if kids else None
    return None


def _transform_template(holder, board=None):
    """The Defending Pokémon Ditto is copying, or None if Transform is off."""
    if holder is None or not is_in_active_spot(holder):
        return None
    if _asleep_confused_or_paralyzed(holder):
        return None
    if board is not None:
        opponent = _opponent_id(board, holder.owning_player_id)
        if opponent is None:
            return None
        return board.active_pokemon(opponent)
    return _opposing_active_via_tree(holder)


class TransformPassive(Passive):
    """While Active and not Asleep/Confused/Paralyzed, treat this Pokémon as
    the Defending Pokémon's printed card (type, HP, Weakness, Resistance,
    retreat, attacks) and treat attached Energy as any type. Can't evolve."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return types
        defending = _transform_template(holder)
        if defending is None:
            return types
        return list(defending.get_attribute(AttrID.POKEMON_TYPES) or types)

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return 0
        defending = _transform_template(holder)
        if defending is None:
            return 0
        copied = defending.attribute_originals.get(
            AttrID.HP.value, defending.get_attribute(AttrID.HP, 0))
        printed = pokemon.attribute_originals.get(
            AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0))
        return int(copied or 0) - int(printed or 0)

    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not calc.target:
            return
        defending = _transform_template(holder, calc.board)
        if defending is None:
            return
        calc.weak_types = list(defending.get_attribute(AttrID.WEAKNESS_TYPES) or [])

    def modify_resistance(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not calc.target:
            return
        defending = _transform_template(holder, calc.board)
        if defending is None:
            return
        calc.resist_type = defending.get_attribute(AttrID.RESISTANCE_TYPES)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return cost
        defending = _transform_template(holder, board)
        if defending is None:
            return cost
        return int(defending.get_attribute(AttrID.RETREAT_COST) or 0)

    def granted_attacks(self, board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return []
        defending = _transform_template(holder, board)
        if defending is None:
            return []
        definition = def_for(defending.archetype_id)
        return [ability for ability in (getattr(definition, "abilities", None) or [])
                if isinstance(ability, Attack)]

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None:
            return options
        mine = any(
            isinstance(passive, TransformPassive)
            and carrier_pokemon(carrier) is holder
            for passive, carrier in _active_passives(board)
        )
        if not mine or _transform_template(holder, board) is None:
            return options
        width = max((len(option) for option in options), default=1)
        return [[getattr(type_row[0], "value", type_row[0])] * width
                for type_row in ALL_TYPES_ONE_AT_A_TIME]

    def blocks_evolution(self, player_id, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return target is holder


ditto_transform = TransformPassive()


async def step_in(ctx):
    """Switch this Benched Pokémon with your Active Pokémon."""
    if ctx.source is not None:
        await ctx.switch_active(ctx.player_id, ctx.source)


# ----------------------------------------------------------------------
# Gym Heroes (GYM1)
# ----------------------------------------------------------------------

def gym_named_basic(owner: str):
    """Deck-search predicate: a Basic Pokémon whose display name contains
    `owner` (Call for Friend — 'Brock', 'Misty', …)."""
    needle = owner.lower()

    def pred(card) -> bool:
        if not is_basic_pokemon(card):
            return False
        name = getattr(def_for(card.archetype_id), "display_name", "") or ""
        return needle in name.lower()
    return pred


def heads_and_tails_damage(coins: int, per_heads: int, per_tails_self: int):
    """Flip `coins`: per_heads×heads to the Defending Pokémon, per_tails_self
    ×tails to the attacker (Full Speed Charge)."""
    async def effect(ctx):
        title = ctx.ability.title if ctx.ability else ""
        results = await ctx.flip_coins(coins, title)
        heads = sum(1 for result in results if result)
        tails = len(results) - heads
        if heads:
            await ctx.deal_damage(per_heads * heads)
        if tails:
            await ctx.deal_damage(
                per_tails_self * tails, target=ctx.attacker,
                apply_modifiers=False)
    return effect


async def natural_healing(ctx):
    """Remove 1 damage counter from this Pokémon (Blaine's Vulpix)."""
    target = ctx.source or ctx.attacker
    if target is not None:
        await ctx.heal(10, target)


def damage_all_unmodified(amount: int):
    """Deal `amount` to each of the opponent's Pokémon with no Weakness or
    Resistance (Spiral Dive)."""
    async def effect(ctx):
        for poked in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(
                amount, target=poked,
                ignore_weakness=True, ignore_resistance=True)
    return effect


def damage_each_in_play_unmodified(amount: int, exclude_type=None):
    """Deal `amount` to each Pokémon in play, no Weakness or Resistance.
    Pokémon that have `exclude_type` are skipped (Dust Devil)."""
    async def effect(ctx):
        for poked in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
            if exclude_type is not None and pokemon_has_type(poked, exclude_type):
                continue
            await ctx.deal_damage(
                amount, target=poked,
                ignore_weakness=True, ignore_resistance=True)
    return effect


def good_manners_condition(board, player_id, pokemon=None) -> bool:
    """No Basic Pokémon in hand; the deck has cards to search."""
    return (not board.has_basic_pokemon_in_hand(player_id)
            and has_cards_in_deck(board, player_id, pokemon))


async def good_manners(ctx):
    """Reveal the hand, then search the deck for a Basic Pokémon into hand."""
    await ctx.reveal_hand(of_player=ctx.player_id, to_player=ctx.opponent_id)
    await search_to_hand(
        predicate=is_basic_pokemon, count=1, minimum=0, reveal=True,
        prompt="Choose a Basic Pokémon card to put into your hand.",
    )(ctx)


def lt_surge_condition(board, player_id, pokemon=None) -> bool:
    """A Basic Pokémon in hand and room on the Bench for the old Active."""
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(is_basic_pokemon(c) for c in hand.children):
        return False
    return bench_has_room(board, player_id)


async def lt_surge(ctx):
    """Put a Basic from hand into play as the Active; the old Active benches."""
    basics = [c for c in ctx.hand() if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(
        basics, 1, minimum=1,
        prompt="Choose a Basic Pokémon to put into play as your Active Pokémon")
    if not picks:
        return
    card = picks[0]
    if not await ctx.bench_pokemon(card):
        return
    await ctx.switch_active(ctx.player_id, card)


async def electric_current(ctx):
    """Printed damage, then move 1 Lightning Energy to a Benched Pokémon
    (or discard it if the Bench is empty)."""
    await ctx.deal_damage()
    lightning = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    if not lightning:
        return
    bench = ctx.my_bench()
    if not bench:
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: _typed_basic_energy(c, PokemonTypes.LIGHTNING),
            prompt="Choose a Lightning Energy card to discard")
        return
    picks = await ctx.choose_cards(
        lightning, 1, minimum=1,
        prompt="Choose a Lightning Energy card to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is not None:
        await ctx.move_energy(picks[0], target)


def discard_all_typed_energy_flip_damage(energy_type: PokemonTypes, per_heads: int):
    """Discard all basic Energy of that type, then flip that many coins ×
    per_heads (Discharge)."""
    async def effect(ctx):
        cards = _energy_cards_of_type(ctx, ctx.attacker, energy_type)
        if cards:
            await ctx.discard_cards(cards)
        title = ctx.ability.title if ctx.ability else ""
        results = await ctx.flip_coins(len(cards), title) if cards else []
        heads = sum(1 for result in results if result)
        amount = per_heads * heads
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


async def removal_pulse(ctx):
    """Printed damage; if the Defending Pokémon has Energy, flip — heads,
    discard 1 of those Energy cards (Removal Pulse / Rapids)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    if not ctx.attached_energies(defender):
        return
    title = ctx.ability.title if ctx.ability else "Removal Pulse"
    results = await ctx.flip_coins(1, title)
    if not results or not results[0]:
        return
    await ctx.discard_energy_from(
        defender, 1,
        prompt="Choose an Energy card to discard from the Defending Pokémon")


def energy_charge_condition(board, player_id, pokemon=None) -> bool:
    """Active, not Asleep/Confused/Paralyzed, and another of your Pokémon
    has a Lightning Energy card to pull over."""
    if pokemon is None or _asleep_confused_or_paralyzed(pokemon):
        return False
    if not is_active(board, player_id, pokemon):
        return False
    return any(
        poked is not pokemon and any(
            _typed_basic_energy(energy, PokemonTypes.LIGHTNING)
            for energy in board.attached_energies(poked))
        for poked in board.pokemon_in_play(player_id)
    )


async def energy_charge(ctx):
    """Move 1 Lightning Energy card from 1 of your other Pokémon onto this one."""
    holder = ctx.source
    if holder is None:
        return
    sources = [
        poked for poked in ctx.my_pokemon_in_play()
        if poked is not holder and any(
            _typed_basic_energy(energy, PokemonTypes.LIGHTNING)
            for energy in ctx.attached_energies(poked))
    ]
    if not sources:
        return
    source = await ctx.choose_pokemon(
        sources, "Choose a Pokémon with Lightning Energy attached")
    if source is None:
        return
    energies = [
        energy for energy in ctx.attached_energies(source)
        if _typed_basic_energy(energy, PokemonTypes.LIGHTNING)
    ]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Lightning Energy card to move")
    if picks:
        await ctx.move_energy(picks[0], holder)


def _defer_promote(ctx, player_id):
    async def _promote():
        if not await ctx.session._promote_new_active(player_id):
            screen_name = ctx.session.players[player_id].screen_name
            await ctx.session.end_game(
                ctx.session._opponent_id(player_id),
                f"{screen_name} has no Pokémon left",
            )
    ctx.deferred_actions.append(_promote)


class StrangeBarrierPassive(Passive):
    """If a Basic Pokémon's attack would do 20 or more after W/R, that
    damage becomes 10. Stops while Asleep, Confused, or Paralyzed."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack or calc.amount < 20:
            return
        holder = carrier_pokemon(carrier) or carrier
        if calc.target is not holder:
            return
        if _asleep_confused_or_paralyzed(holder):
            return
        attacker = calc.attacker
        if attacker is None or not is_basic_pokemon(attacker):
            return
        calc.amount = 10


strange_barrier = StrangeBarrierPassive()


class DeflectorPassive(Passive):
    """Halve attack damage after W/R, rounded down to the nearest 10."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack:
            return
        holder = carrier_pokemon(carrier) or carrier
        if calc.target is not holder:
            return
        calc.amount = (calc.amount // 20) * 10


async def deflector(ctx):
    """During the opponent's next turn, this Pokémon takes half attack
    damage (rounded down to the nearest 10)."""
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(ctx.attacker, DeflectorPassive())


async def fairy_power(ctx):
    """Heads: you may return any number of your Pokémon (and attached cards)
    to your hand."""
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Fairy Power")
    if not results or not results[0]:
        return
    mine = list(ctx.my_pokemon_in_play())
    if not mine:
        return
    picks = await ctx.choose_cards(
        mine, len(mine), minimum=0,
        prompt="Choose any number of your Pokémon to return to your hand")
    if not picks:
        return
    owner = ctx.player_id
    active = ctx.board.active_pokemon(owner)
    scooped_active = active is not None and any(poked is active for poked in picks)
    cards = []
    for poked in picks:
        cards.extend(full_stack(poked))
    await ctx.put_in_hand(cards, reveal=False)
    if scooped_active:
        _defer_promote(ctx, owner)


async def take_away(ctx):
    """Shuffle this Pokémon and attached cards into your deck; then shuffle
    the opponent's Active Pokémon and attached cards into their deck."""
    attacker = ctx.attacker
    defender = ctx.defender
    my_id = ctx.player_id
    opp_id = (defender.owning_player_id or ctx.opponent_id) if defender is not None \
        else ctx.opponent_id
    blocked = defender is None or ctx.effects_blocked(defender)
    if attacker is not None:
        await ctx.shuffle_into_deck(full_stack(attacker), my_id)
        _defer_promote(ctx, my_id)
    if defender is not None and not blocked:
        await ctx.shuffle_into_deck(full_stack(defender), opp_id)
        _defer_promote(ctx, opp_id)


_GYM_CONDITION_CHOICES = [
    ("Asleep", SpecialConditions.ASLEEP),
    ("Confused", SpecialConditions.CONFUSED),
    ("Paralyzed", SpecialConditions.PARALYZED),
    ("Poisoned", SpecialConditions.POISONED),
]


async def magic_pollen(ctx):
    """Printed damage; heads, choose Asleep, Confused, Paralyzed, or Poisoned."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Magic Pollen")
    if not results or not results[0]:
        return
    target = ctx.defender
    if target is None:
        return
    idx = await ctx.choose(
        "Choose a Special Condition",
        [name for name, _ in _GYM_CONDITION_CHOICES],
    )
    await ctx.apply_special_condition(target, _GYM_CONDITION_CHOICES[idx][1])


async def flip_heal_self(ctx):
    """Flip a coin. If heads, remove 4 damage counters from this Pokémon."""
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if results and results[0] and ctx.attacker is not None:
        await ctx.heal(40, ctx.attacker)


# ----------------------------------------------------------------------
# Gym Heroes (GYM1)
# ----------------------------------------------------------------------

def pokemon_name_contains(fragment: str):
    """Basic/Evolution Pokémon whose display name contains `fragment`."""
    def pred(card) -> bool:
        if card is None or not is_pokemon_card(card):
            return False
        definition = def_for(getattr(card, "archetype_id", None) or "")
        name = (definition.display_name or "") if definition else ""
        return fragment in name
    return pred


def gym_owner(owner: str):
    """Stadium protects pred: the Pokémon's name contains `owner`."""
    named = pokemon_name_contains(owner)

    def pred(pokemon, carrier) -> bool:
        return named(pokemon)
    return pred


async def alert(ctx):
    """Draw a card, then switch this Pokémon with a Benched Pokémon."""
    await ctx.draw_cards(1)
    await switch_self_attack()(ctx)


def celadon_city_gym_condition(board, player_id, stadium=None) -> bool:
    return any(
        pokemon_name_contains("Erika")(poked) and board.attached_energies(poked)
        for poked in board.pokemon_in_play(player_id)
    )


async def celadon_city_gym(ctx):
    """Discard an Energy from an Erika Pokémon; it recovers Asleep,
    Confused, Paralyzed, and Poisoned."""
    named = pokemon_name_contains("Erika")
    candidates = [
        poked for poked in ctx.my_pokemon_in_play()
        if named(poked) and ctx.attached_energies(poked)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon with Erika in its name")
    if target is None:
        return
    discarded = await ctx.discard_energy_from(
        target, 1, prompt="Choose an Energy card to discard")
    if not discarded:
        return
    for condition in (
        SpecialConditions.ASLEEP,
        SpecialConditions.CONFUSED,
        SpecialConditions.PARALYZED,
        SpecialConditions.POISONED,
    ):
        await ctx.cure_condition(target, condition)


class CharityPassive(Passive):
    """Holder's attack damage to the Defending Pokémon may be reduced by any
    amount, in 10s, after Weakness and Resistance."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return None
        if holder is not calc.attacker or calc.amount <= 0:
            return None
        if not await ctx.ask_yes_no("Reduce this attack's damage?"):
            return None
        caps = list(range(0, (calc.amount // 10) * 10 + 1, 10))
        if calc.amount not in caps:
            caps.append(calc.amount)
        idx = await ctx.choose(
            "How much damage should this attack do?",
            [str(n) for n in caps],
            use_panel=False,
        )
        return caps[idx]


charity_passive = CharityPassive()


async def charity(ctx):
    """Attach to your Active Pokémon; return to hand at end of turn unless
    that Pokémon is Knocked Out."""
    target = ctx.my_active()
    if target is None:
        return
    card = ctx.source
    await ctx.attach_energy(card, target)
    card_id = card.entity_id
    owner = ctx.player_id

    async def _return(session):
        attached = session.board_state.get_entity(card_id)
        if attached is None or carrier_pokemon(attached) is None:
            return
        from spirit.game.session.effects import EffectContext
        return_ctx = EffectContext(session, owner, attached, None)
        await return_ctx.put_in_hand([attached], reveal=False)
        await session._flush_effect_runs(return_ctx)

    ctx.schedule_at_checkup(0, _return)


def energy_flow_condition(board, player_id, pokemon=None) -> bool:
    return _player_has_energy_attached(board, player_id)


async def energy_flow(ctx):
    """For each of your Pokémon, you may return any number of attached
    Energy cards to your hand."""
    for poked in ctx.my_pokemon_in_play():
        energies = ctx.attached_energies(poked)
        if not energies:
            continue
        label = getattr(def_for(poked.archetype_id), "display_name", None) or "this Pokémon"
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt=f"Choose Energy cards attached to {label} to return to your hand",
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=False)


async def erika(ctx):
    """You may draw up to 3 cards, then your opponent may draw up to 3."""
    n = await ctx.choose(
        "Draw up to 3 cards.",
        [str(i) for i in range(4)],
        use_panel=False,
    )
    if n > 0:
        await ctx.draw_cards(n)
    n = await ctx.choose(
        "Draw up to 3 cards.",
        [str(i) for i in range(4)],
        player_id=ctx.opponent_id,
        use_panel=False,
    )
    if n > 0:
        await ctx.draw_cards(n, ctx.opponent_id)


class PhotosynthesisPassive(Passive):
    """All Energy cards attached to the holder provide Grass instead of
    their usual type (Erika's Oddish). Works through Special Conditions."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None:
            return options
        mine = any(
            isinstance(passive, PhotosynthesisPassive)
            and carrier_pokemon(carrier) is holder
            for passive, carrier in _active_passives(board)
        )
        if not mine:
            return options
        grass = PokemonTypes.GRASS.value
        if not options:
            return [[grass]]
        return [[grass] * max(1, len(option)) for option in options]


async def sporadic_sponging(ctx):
    """Printed damage; if this Pokémon is damaged, heads removes 1 counter."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    if attacker is None or not _is_damaged(ctx.board, attacker):
        return
    results = await ctx.flip_coins(1, "Sporadic Sponging")
    if results and results[0]:
        await ctx.heal(10, attacker)


async def pollen_defense(ctx):
    """When this Active Pokémon is damaged by an attack (even if Knocked
    Out), flip: heads, the opponent's Active is Confused. Works through
    Special Conditions."""
    holder = ctx.source
    if holder is None or not is_in_active_spot(holder):
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(1, "Pollen Defense", source=holder)
    if not results or not results[0]:
        return
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


def erikas_maids_condition(board, player_id, pokemon=None) -> bool:
    """Two other cards in hand to trade into the deck."""
    return hand_size_at_least(3)(board, player_id)


async def erikas_maids(ctx):
    """Shuffle 2 other cards from hand into the deck; search up to 2
    Pokémon with Erika in their names."""
    if len(ctx.hand()) < 2:
        return
    picks = await ctx.choose_cards(
        ctx.hand(), 2, minimum=2,
        prompt="Choose 2 cards to put into your deck")
    if len(picks) < 2:
        return
    await ctx.shuffle_into_deck(picks)
    found = await ctx.search_deck(
        pokemon_name_contains("Erika"), count=2, minimum=0,
        prompt="Choose up to 2 Pokémon with Erika in their names.",
    )
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


async def erikas_perfume(ctx):
    """Look at the opponent's hand; you may put any number of Basic Pokémon
    there onto their Bench (space permitting)."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    basics = [c for c in hand if is_basic_pokemon(c)]
    if not basics:
        return
    space = (effective_bench_capacity(ctx.board, ctx.opponent_id)
             - len(ctx.opponent_bench()))
    if space <= 0:
        return
    picks = await ctx.choose_cards(
        basics, min(space, len(basics)), minimum=0,
        prompt="Choose Basic Pokémon to put onto your opponent's Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


async def _discard_defending_energy(ctx):
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose Energy to discard from the Defending Pokémon")


kindle = self_energy_discard_attack(
    count=1, before_damage=True, also=_discard_defending_energy)


def damage_typed_bench(amount: int, pokemon_type: PokemonTypes,
                       also_base: bool = True):
    """Printed damage, then `amount` to each opposing Benched Pokémon of
    `pokemon_type` (Blaine's Growlithe — Blaze)."""
    async def effect(ctx):
        if also_base:
            await ctx.deal_damage()
        for poked in ctx.opponent_bench():
            if pokemon_has_type(poked, pokemon_type):
                await ctx.deal_damage(amount, target=poked)
    return effect


async def phoenix_flame(ctx):
    """Printed damage, then tails shuffles this Pokémon and attachments
    into the deck (Blaine's Moltres)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Phoenix Flame")
    if not results or results[0]:
        return
    pokemon = ctx.attacker
    if pokemon is None:
        return
    await ctx.shuffle_into_deck(full_stack(pokemon), ctx.player_id)
    _defer_promote(ctx, ctx.player_id)


def only_card_in_hand(board, player_id, pokemon=None) -> bool:
    """Playable only when this trainer is the sole card in the hand."""
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) == 1


async def blaines_last_resort(ctx):
    """Show your hand, then draw 5 (playable only as the last card)."""
    await ctx.reveal_hand(of_player=ctx.player_id, to_player=ctx.opponent_id)
    await ctx.draw_cards(5)


async def blaines_gamble(ctx):
    """Discard any number of other cards, then heads: draw twice that many."""
    hand = ctx.hand()
    discarded = await ctx.discard_from_hand(
        len(hand), minimum=0,
        prompt="Discard any number of cards from your hand",
    ) if hand else []
    results = await ctx.flip_coins(1, "Blaine's Gamble")
    if results and results[0] and discarded:
        await ctx.draw_cards(2 * len(discarded))


# Pokémon Red/Blue Pokédex heights in decimeters (national dex 1–151).
# Used to judge Blaine's Quiz #1 guesses against printed WOTC lengths.
_GEN1_HEIGHT_DM = (
    7, 10, 20, 6, 11, 17, 5, 10, 16, 3,
    7, 11, 3, 6, 10, 3, 11, 15, 3, 7,
    3, 12, 20, 35, 4, 8, 6, 10, 4, 8,
    13, 5, 9, 14, 6, 13, 6, 11, 5, 10,
    8, 16, 5, 8, 12, 3, 10, 10, 15, 2,
    7, 4, 10, 8, 17, 5, 10, 7, 19, 6,
    10, 13, 9, 13, 15, 8, 15, 16, 7, 10,
    17, 9, 16, 4, 10, 14, 10, 17, 12, 16,
    3, 10, 8, 14, 18, 11, 17, 9, 12, 3,
    15, 13, 16, 15, 88, 10, 16, 4, 13, 5,
    12, 4, 20, 4, 10, 15, 14, 12, 6, 12,
    10, 19, 11, 10, 22, 4, 12, 6, 13, 8,
    11, 13, 15, 14, 11, 13, 15, 14, 9, 65,
    25, 3, 3, 10, 8, 9, 8, 4, 10, 5,
    13, 18, 21, 17, 16, 20, 18, 40, 22, 20, 4,
)


def _length_ft_in(family_id):
    if not family_id:
        return None
    try:
        idx = int(family_id) - 1
    except (TypeError, ValueError):
        return None
    if idx < 0 or idx >= len(_GEN1_HEIGHT_DM):
        return None
    inches = int(round(_GEN1_HEIGHT_DM[idx] * 3.937))
    return divmod(inches, 12)


def _family_id_of(card) -> int:
    fid = card.get_attribute(AttrID.FAMILY_ID)
    if fid:
        return int(fid)
    definition = def_for(card.archetype_id)
    extra = getattr(definition, "extra_attributes", {}) or {}
    raw = extra.get(str(AttrID.FAMILY_ID.value), {})
    value = raw.get("value") if isinstance(raw, dict) else raw
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


blaines_quiz_1_condition = requires_hand(is_pokemon_card)


async def blaines_quiz_1(ctx):
    """Name a Pokémon from hand; opponent guesses its length; winner draws 2."""
    matches = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1, minimum=1,
        prompt="Choose a Basic Pokémon or Evolution card")
    if not picks:
        return
    chosen = picks[0]
    definition = def_for(chosen.archetype_id)
    name = getattr(definition, "display_name", None) or "Pokémon"
    feet = await ctx.choose(
        f"The Pokémon is named {name}. Guess its length (feet).",
        [str(i) for i in range(41)],
        player_id=ctx.opponent_id, use_panel=False,
    )
    inches = await ctx.choose(
        f"Guess {name}'s length: {feet} feet and how many inches?",
        [str(i) for i in range(12)],
        player_id=ctx.opponent_id, use_panel=False,
    )
    await ctx.reveal_cards([chosen], to_player=ctx.opponent_id)
    actual = _length_ft_in(_family_id_of(chosen))
    if actual is None:
        correct = await ctx.ask_yes_no(
            f"Your opponent guessed {feet}'{inches:02}\". "
            f"Does that match {name}'s printed length?",
        )
    else:
        correct = actual == (feet, inches)
    if correct:
        await ctx.draw_cards(2, ctx.opponent_id)
    else:
        await ctx.draw_cards(2)


blaines_quiz_2_condition = requires_hand()

_QUIZ2_KINDS = ("Energy card", "Trainer card", "Pokémon card")


def _quiz2_kind(card) -> int:
    if is_energy_card(card):
        return 0
    if is_trainer_card(card):
        return 1
    if is_pokemon_card(card):
        return 2
    return -1


async def blaines_quiz_2(ctx):
    """Opponent guesses Energy / Trainer / Pokémon; winner draws 2."""
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Choose a card from your hand")
    if not picks:
        return
    chosen = picks[0]
    guess = await ctx.choose(
        "Guess whether the face-down card is an Energy card, a Trainer card, "
        "or a Pokémon card.",
        list(_QUIZ2_KINDS),
        player_id=ctx.opponent_id, use_panel=False,
    )
    await ctx.reveal_cards([chosen], to_player=ctx.opponent_id)
    if guess == _quiz2_kind(chosen):
        await ctx.draw_cards(2, ctx.opponent_id)
    else:
        await ctx.draw_cards(2)


def _attack_titles_of(card) -> list:
    definition = def_for(getattr(card, "archetype_id", None))
    return [ability.title for ability in getattr(definition, "abilities", None) or []
            if isinstance(ability, Attack) and ability.title]


def _pokemon_with_attacks(card) -> bool:
    return is_pokemon_card(card) and bool(_attack_titles_of(card))


blaines_quiz_3_condition = requires_hand(_pokemon_with_attacks)

_WOTC_QUIZ_SETS = frozenset({
    "BASE1", "BASE2", "BASE3", "BASE4", "BASE5", "GYM1", "GYM2", "SI1",
})


def _pokemon_names_with_attack(title: str, extra: Optional[str] = None) -> list:
    names = []
    seen = set()
    if extra:
        seen.add(extra)
        names.append(extra)
    for definition in CARD_DEFS_BY_GUID.values():
        if getattr(definition, "set_code", None) not in _WOTC_QUIZ_SETS:
            continue
        name = getattr(definition, "display_name", None)
        if not name or name in seen:
            continue
        for ability in getattr(definition, "abilities", None) or []:
            if isinstance(ability, Attack) and ability.title == title:
                seen.add(name)
                names.append(name)
                break
    return names


async def blaines_quiz_3(ctx):
    """Name an attack from a Pokémon in hand; opponent guesses the card; winner draws 3."""
    matches = [c for c in ctx.hand() if _pokemon_with_attacks(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1, minimum=1,
        prompt="Choose a Basic Pokémon or Evolution card")
    if not picks:
        return
    chosen = picks[0]
    titles = _attack_titles_of(chosen)
    attack_idx = 0 if len(titles) == 1 else await ctx.choose(
        "Tell your opponent the name of an attack of that card.", titles)
    attack_name = titles[attack_idx]
    definition = def_for(chosen.archetype_id)
    actual = getattr(definition, "display_name", None) or "Pokémon"
    names = _pokemon_names_with_attack(attack_name, extra=actual)
    guess = await ctx.choose(
        f"The attack is named {attack_name}. Guess the name of that card.",
        names,
        player_id=ctx.opponent_id, use_panel=False,
    )
    await ctx.reveal_cards([chosen], to_player=ctx.opponent_id)
    if names[guess] == actual:
        await ctx.draw_cards(3, ctx.opponent_id)
    else:
        await ctx.draw_cards(3)


# ----------------------------------------------------------------------
# Blaine's Ninetales — Healing Fire / Blaine's Ponyta — Hind Kick /
# Blaine's Vulpix — Call Will-o'-the-wisp / Brock's Dugtrio — Earthdrill
# ----------------------------------------------------------------------

def heal_on_energy_attached(energy_type: PokemonTypes, amount: int = 10):
    """ON_ENERGY_ATTACHED: attaching that basic Energy from hand heals
    `amount`. Off while Asleep, Confused, or Paralyzed (Healing Fire)."""

    async def watch(ctx):
        holder = ctx.source
        if holder is None or _asleep_confused_or_paralyzed(holder):
            return
        if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not holder:
            return
        energy = ctx.attached_energy
        if energy is None or not _typed_basic_energy(energy, energy_type):
            return
        if _is_damaged(ctx.board, holder):
            await ctx.heal(amount, holder)

    return watch


healing_fire = heal_on_energy_attached(PokemonTypes.FIRE, 10)


async def energy_evolution(ctx):
    """ON_ENERGY_ATTACHED: heads, search a same-type evolution of this Pokémon
    and evolve it (Eevee — Energy Evolution). Off while Asleep, Confused, or
    Paralyzed."""
    holder = ctx.source
    if holder is None or _asleep_confused_or_paralyzed(holder):
        return
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not holder:
        return
    energy = ctx.attached_energy
    if energy is None:
        return
    wanted = _energy_provided_types(energy, ctx.board)
    if not wanted:
        return
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Energy Evolution")
    if not results or not results[0]:
        return
    logic_name = holder.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def pred(card, name=logic_name, types=wanted):
        if not name or card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) != name:
            return False
        return bool(types & set(card.get_attribute(AttrID.POKEMON_TYPES) or []))

    picks = await ctx.search_deck(
        pred, count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon of the Energy's type.",
    )
    if picks:
        await ctx.evolve_pokemon(holder, picks[0])
    await ctx.shuffle_deck()


async def hind_kick(ctx):
    """Printed damage; if you have a Bench, heads switches this Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Hind Kick")
    if not results or not results[0]:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def call_will_o_the_wisp(ctx):
    """Flip 3 coins; put that many Fire Energy cards from discard into hand."""
    results = await ctx.flip_coins(
        3, ctx.ability.title if ctx.ability else "Call Will-o'-the-wisp")
    heads = sum(1 for result in results if result)
    if not heads:
        return
    cards = [c for c in ctx.discard_pile()
             if _typed_basic_energy(c, PokemonTypes.FIRE)]
    if not cards:
        return
    take = min(heads, len(cards))
    picks = await ctx.choose_cards(
        cards, take, minimum=take,
        prompt="Choose Fire Energy cards to put into your hand")
    await ctx.put_in_hand(picks, reveal=True)


def used_named_attack_last_turn(title: str):
    """Attack condition: this player declared `title` during their last turn
    (Brock's Dugtrio — Earthdrill)."""
    def check(board, player_id, pokemon=None) -> bool:
        state = getattr(board, "turn_state", None)
        if state is None:
            return False
        prev = state.attack_titles_prev_turn_by_player.get(player_id) or []
        return title in prev
    return check


def double_named_attack_next_turn(attack_title: str, printed: int):
    """During your next turn, `attack_title`'s printed base damage is doubled
    (Focus Energy)."""
    async def effect(ctx):
        await apply_own_next_turn_boost(ctx, printed, attack_title)
    return effect


async def lt_surges_treaty(ctx):
    """Opponent chooses: everyone takes 1 of their own Prizes, or you draw."""
    idx = await ctx.choose(
        "Choose 1:",
        [
            "Everyone takes 1 of their own Prize cards",
            "Your opponent draws a card",
        ],
        player_id=ctx.opponent_id,
        use_panel=False,
    )
    if idx == 0:
        await ctx.take_prizes(1, ctx.player_id)
        await ctx.take_prizes(1, ctx.opponent_id)
        return
    await ctx.draw_cards(1)


async def minion_of_team_rocket(ctx):
    """Flip 2 coins. Both heads: return 1 opposing Benched Pokémon and
    attachments to hand. Any tails: your turn ends immediately."""
    results = await ctx.flip_coins(2, "Minion of Team Rocket")
    if results and all(results):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon")
        if target is not None:
            await ctx.put_in_hand(full_stack(target), reveal=False)
        return
    ctx.ends_turn = True


class NamedAttackBonusAfterWR(Passive):
    """This turn, attacks from Pokémon named with `owner` do `amount` more
    to the Defending Pokémon after Weakness and Resistance (Misty)."""

    def __init__(self, owner: str, amount: int, player_id: str):
        self.amount = amount
        self.player_id = player_id
        self._named = pokemon_name_contains(owner)

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.amount <= 0:
            return
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != self.player_id:
            return
        if not self._named(attacker):
            return
        calc.amount += self.amount


def gym_leader_this_turn_bonus(owner: str, amount: int = 20):
    """Discard 2 other cards; this turn, Pokémon with `owner` in their name
    do `amount` more to the Defending Pokémon after Weakness and Resistance."""
    async def effect(ctx):
        discarded = await ctx.discard_from_hand(
            2, prompt="Discard 2 of the other cards from your hand")
        if len(discarded) < 2:
            return
        ctx.add_temporary_passive(
            ctx.board.playmat,
            NamedAttackBonusAfterWR(owner, amount, ctx.player_id),
            expires_after_turn=ctx.session.turn_state.turn_number,
        )
    return effect


misty = gym_leader_this_turn_bonus("Misty")
misty_condition = hand_size_at_least(3)


class ShellArmorPassive(Passive):
    """Reduce all attack damage to this Pokémon by 10 after W/R. Stops
    while Asleep, Confused, or Paralyzed (Misty's Cloyster)."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack or calc.amount <= 0:
            return
        holder = carrier_pokemon(carrier) or carrier
        if calc.target is not holder:
            return
        if _asleep_confused_or_paralyzed(holder):
            return
        calc.amount = max(0, calc.amount - 10)


shell_armor = ShellArmorPassive()


async def water_ring(ctx):
    """Printed damage to the Defending Pokémon, then 10 to each non-Water
    Pokémon on either Bench (no W/R)."""
    await ctx.deal_damage()
    water = PokemonTypes.WATER.value
    for poked in ctx.my_bench() + ctx.opponent_bench():
        if water in effective_pokemon_types(ctx.board, poked):
            continue
        await ctx.deal_damage(10, target=poked)


_RPS = ["Rock", "Paper", "Scissors"]


async def mistys_duel(ctx):
    """Rock-Paper-Scissors until someone wins; that player shuffles their
    hand into their deck and draws 5."""
    prompt = "Rock-Paper-Scissors: choose your play."
    winner = None
    for _ in range(100):
        mine = await ctx.choose(prompt, _RPS)
        order = random.sample(_RPS, 3)
        pick = await ctx.choose(prompt, order, player_id=ctx.opponent_id)
        theirs = _RPS.index(order[pick])
        if mine != theirs:
            winner = ctx.player_id if (mine - theirs) % 3 == 1 else ctx.opponent_id
            break
        prompt = "It's a tie! Rock-Paper-Scissors: choose your play."
    if winner is None:
        return
    await ctx.shuffle_into_deck(ctx.hand(winner), winner)
    await ctx.draw_cards(5, winner)


# ----------------------------------------------------------------------
# Sabrina's Pokémon and trainers (GYM1)
# ----------------------------------------------------------------------

async def suggestion(ctx):
    """Heads: the Defending Pokémon can't attack during the opponent's next turn."""
    results = await ctx.flip_coins(1, "Suggestion")
    if results and results[0]:
        lock_defender_attacks(ctx)


async def pain_amplifier(ctx):
    """Put a damage counter on each of the opponent's Pokémon that already
    has damage counters on it."""
    for poked in ctx.opponent_pokemon_in_play():
        if _is_damaged(ctx.board, poked):
            await ctx.deal_damage(10, target=poked, as_counters=True)


async def call_of_the_night(ctx):
    """Printed damage; unless that Knocks Out the Defending Pokémon, flip 2
    coins — both heads shuffles it and attachments into the opponent's deck."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or defender in ctx.knockouts:
        return
    results = await ctx.flip_coins(2, "Call of the Night")
    if not results or not all(results):
        return
    if ctx.effects_blocked(defender):
        return
    opp_id = defender.owning_player_id or ctx.opponent_id
    await ctx.shuffle_into_deck(full_stack(defender), opp_id)
    _defer_promote(ctx, opp_id)


_SABRINA_GHOSTS = frozenset((
    "Sabrina's Gastly", "Sabrina's Haunter", "Sabrina's Gengar",
))


def _sabrina_ghost_line(pokemon) -> bool:
    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    name = (definition.display_name or "") if definition else ""
    return name in _SABRINA_GHOSTS


async def night_spirits(ctx):
    """Flip 1 coin per Sabrina's Gastly/Haunter/Gengar in play; 30×heads."""
    n = sum(1 for poked in ctx.my_pokemon_in_play() if _sabrina_ghost_line(poked))
    results = await ctx.flip_coins(n, "Night Spirits") if n else []
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(30 * heads)


async def good_morning(ctx):
    """Printed damage; if the Defending Pokémon is Asleep, it wakes."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.cure_condition(defender, SpecialConditions.ASLEEP)


async def sleight_of_hand(ctx):
    """Put up to 3 hand cards on top of the deck, then search that many
    basic Energy into the hand and shuffle."""
    hand = ctx.hand()
    take = min(3, len(hand))
    picks = await ctx.choose_cards(
        hand, take, minimum=0,
        prompt="Choose up to 3 cards to put on top of your deck",
    ) if take else []
    n = len(picks)
    if n > 1:
        picks = await ctx.choose_cards(
            picks, n, minimum=n, ordered=True,
            prompt="Put these cards on top of your deck, in order.",
        )
    for card in picks:
        await ctx.put_on_top_of_deck(card)
    if n <= 0:
        return
    found = await ctx.search_deck(
        is_basic_energy_card, count=n, minimum=0,
        prompt="Choose that many basic Energy cards.",
    )
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


async def naptime(ctx):
    """Heads: remove 3 damage counters from this Pokémon and it is Asleep."""
    results = await ctx.flip_coins(1, "Naptime")
    if not results or not results[0]:
        return
    attacker = ctx.attacker
    if attacker is None:
        return
    await ctx.heal(30, attacker)
    await ctx.apply_special_condition(attacker, SpecialConditions.ASLEEP)


async def sabrinas_gaze(ctx):
    """Each player shuffles their hand into their deck and draws the same number."""
    mine = ctx.hand_size()
    theirs = ctx.hand_size(ctx.opponent_id)
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    if mine:
        await ctx.draw_cards(mine)
    if theirs:
        await ctx.draw_cards(theirs, ctx.opponent_id)


def sabrinas_esp_targets(board, player_id, card=None):
    named = pokemon_name_contains("Sabrina")
    return [poked for poked in board.pokemon_in_play(player_id) if named(poked)]


def sabrinas_esp_condition(board, player_id, pokemon=None) -> bool:
    return bool(sabrinas_esp_targets(board, player_id))


class SabrinasESPPassive(Passive):
    """If the holder uses an attack that flips coins, you may re-flip those
    coins once (all of them together)."""

    def offers_attack_coin_reroll(self, player_id, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder.owning_player_id != player_id:
            return False
        return is_in_active_spot(holder)


sabrinas_esp_passive = SabrinasESPPassive()


async def sabrinas_esp(ctx):
    """Attach to a Pokémon with Sabrina in its name; discard at end of turn."""
    candidates = sabrinas_esp_targets(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_play_target(
        candidates, "Choose a Pokémon with Sabrina in its name")
    if target is None:
        return
    card = ctx.source
    await ctx.attach_energy(card, target)
    card_id = card.entity_id
    owner = ctx.player_id

    async def _discard(session):
        attached = session.board_state.get_entity(card_id)
        if attached is None:
            return
        from spirit.game.session.effects import EffectContext
        discard_ctx = EffectContext(session, owner, attached, None)
        await discard_ctx.discard_cards([attached])
        await session._flush_effect_runs(discard_ctx)

    ctx.schedule_at_checkup(0, _discard)


_FLEE_ATTR = "_flee_prevented_effects"


class FleePassive(Passive):
    """If an opposing attack damages this Active Pokémon, you may switch it
    with a Benched Pokémon, preventing remaining effects of that attack.
    Stops while Asleep, Confused, or Paralyzed (Misty's Tentacruel)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not target:
            return None
        holder.set_attribute(_FLEE_ATTR, False)
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if not is_in_active_spot(holder):
            return None
        if _asleep_confused_or_paralyzed(holder):
            return None
        owner_id = holder.owning_player_id
        if owner_id is None:
            return None
        bench = ctx.my_bench() if owner_id == ctx.player_id else ctx.opponent_bench()
        if not bench:
            return None
        name = getattr(def_for(holder.archetype_id), "display_name", None) \
            or "this Pokémon"
        if not await ctx.ask_yes_no(
                f"Use Flee to switch {name} with 1 of your Benched Pokémon?",
                player_id=owner_id):
            return None
        replacement = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to switch into the Active Spot",
            player_id=owner_id)
        if replacement is None:
            return None
        holder.set_attribute(_FLEE_ATTR, True)
        await ctx.switch_active(owner_id, replacement)
        return None

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not target:
            return False
        return bool(target.get_attribute(_FLEE_ATTR))


flee_passive = FleePassive()


async def mud_splash(ctx):
    """Printed damage; if the opponent has a Bench, choose 1 and flip —
    heads, 10 damage to that Benched Pokémon (no W/R)."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is None:
        return
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Mud Splash")
    if results and results[0]:
        await ctx.deal_damage(10, target=target)


async def fire_wind(ctx):
    """Printed damage; if the opponent has a Bench, choose 1, then flip 2 —
    10 damage to that Benched Pokémon per heads (no W/R)."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is None:
        return
    results = await ctx.flip_coins(
        2, ctx.ability.title if ctx.ability else "Fire Wind")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(10 * heads, target=target)


_CHAR_ATTR = "_char_counter"


def _char_holder(session, entity_id):
    """The in-play Pokémon still carrying a Char counter, or None."""
    pokemon = session.board_state.get_entity(entity_id)
    if pokemon is None or not pokemon.get_attribute(_CHAR_ATTR):
        return None
    parent = getattr(pokemon, "parent", None)
    area = parent.get_attribute(AttrID.NAME) if parent is not None else None
    if area not in ("activePokemonArea", "bench"):
        return None
    return pokemon


async def _char_counter_tick(session, entity_id: str):
    """After each turn: Char's owner flips; tails, 2 damage counters."""
    from spirit.game.session.effects import EffectContext
    pokemon = _char_holder(session, entity_id)
    if pokemon is None:
        return
    owner = pokemon.owning_player_id
    if owner is None:
        return
    ctx = EffectContext(session, owner, pokemon, None)
    results = await ctx.flip_coins(1, "Char", source=pokemon)
    if results and not results[0]:
        await ctx.deal_damage(20, target=pokemon, as_counters=True)
    await session._flush_effect_runs(ctx)
    await session.resolve_knockouts(ctx)
    if _char_holder(session, entity_id) is None:
        return

    async def _tick(session_):
        await _char_counter_tick(session_, entity_id)

    session.scheduled_effects.append({
        "fire_at_checkup_of_turn": session.turn_state.turn_number + 1,
        "guard": None,
        "effect": _tick,
    })


async def char_attack(ctx):
    """Printed damage; if the Defending Pokémon has no Char counter, flip —
    heads, put a Char counter on it (Quilava)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    if defender.get_attribute(_CHAR_ATTR):
        return
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Char")
    if not (results and results[0]):
        return
    defender.set_attribute(_CHAR_ATTR, True)
    target_id = defender.entity_id

    async def _tick(session):
        await _char_counter_tick(session, target_id)

    ctx.schedule_at_checkup(0, _tick)


async def crystal_beam(ctx):
    """Printed damage; heads, opponent can't attach Energy to the Defending
    Pokémon during their next turn (Misty's Tentacool)."""
    await freeze_lock(ctx)


def heal_each_per_heads(coins: int, per: int = 10):
    """Flip `coins`; remove `per` damage from each of your Pokémon per heads
    (Sabrina's Venomoth — Healing Pollen)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            coins, ctx.ability.title if ctx.ability else "")
        heads = sum(1 for result in results if result)
        if not heads:
            return
        for poked in ctx.my_pokemon_in_play():
            await ctx.heal(per * heads, poked)
    return effect


healing_pollen = heal_each_per_heads(3)


async def secret_mission(ctx):
    """Look at the opponent's hand, then you may discard any number of cards
    from your hand and draw that many."""
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    hand = ctx.hand()
    discarded = await ctx.discard_from_hand(
        len(hand), minimum=0,
        prompt="Discard any number of cards from your hand",
    ) if hand else []
    if discarded:
        await ctx.draw_cards(len(discarded))


class RocketsTrainingGymPassive(Passive):
    """Each player pays [C] more to retreat their Active Pokémon."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if is_in_active_spot(pokemon):
            return cost + 1
        return cost


rockets_training_gym_passive = RocketsTrainingGymPassive()


async def the_rockets_trap(ctx):
    """Heads: shuffle up to 3 random cards from the opponent's hand into
    their deck without looking at them."""
    results = await ctx.flip_coins(1, "The Rocket's Trap")
    if not results or not results[0]:
        return
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    picks = random.sample(hand, min(3, len(hand)))
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def tickling_machine(ctx):
    """Heads: set the opponent's hand aside face down until the end of their
    next turn. Tails: this turn ends immediately."""
    results = await ctx.flip_coins(1, "Tickling Machine")
    if not results:
        return
    if not results[0]:
        ctx.ends_turn = True
        return
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    owner = ctx.opponent_id
    staging = ctx.board.find_global_area("outOfPlay")
    if staging is None:
        return
    ids = []
    for card in hand:
        owner_id = card.owning_player_id or owner
        position = len(staging.children)
        if not ctx.board.move_card(card.entity_id, staging.entity_id):
            continue
        card.owning_player_id = owner_id
        ids.append(card.entity_id)
        ctx._queue(
            ctx.session._entity_moved_msg(
                card.entity_id, staging.entity_id, position),
            bracket=GameSequence.GROUPED_MOVE.value,
        )
        ctx._queue(
            ctx.session._attributes_reset_msg(card.entity_id),
            bracket=GameSequence.GROUPED_MOVE.value,
        )

    async def _return(session):
        cards = [session.board_state.get_entity(eid) for eid in ids]
        cards = [card for card in cards if card is not None]
        if not cards:
            return
        from spirit.game.session.effects import EffectContext
        return_ctx = EffectContext(session, owner, cards[0], None)
        await return_ctx.put_in_hand(cards, reveal=False)
        await session._flush_effect_runs(return_ctx)

    ctx.schedule_at_checkup(1, _return)


async def trash_exchange(ctx):
    """Shuffle the discard pile into the deck, then mill that many cards."""
    pile = list(ctx.discard_pile())
    count = len(pile)
    if count:
        await ctx.shuffle_into_deck(pile)
        await ctx.discard_cards(ctx.deck_top(count))


class VermilionCityGymPassive(Passive):
    """When a Pokémon with Lt. Surge in its name attacks, its owner may
    flip: heads, +10 to the Defending Pokémon after W/R if the attack did
    damage; tails, 10 damage to the attacker."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if getattr(ctx, "_vermilion_gym_resolved", False):
            return None
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return None
        attacker = calc.attacker
        if attacker is None or not pokemon_name_contains("Lt. Surge")(attacker):
            return None
        if not await ctx.ask_yes_no(
                "Flip a coin for Vermilion City Gym?",
                player_id=attacker.owning_player_id):
            ctx._vermilion_gym_resolved = True
            return None
        ctx._vermilion_gym_resolved = True
        results = await ctx.flip_coins(1, "Vermilion City Gym")
        if results and results[0]:
            return calc.amount + 10 if calc.amount > 0 else None
        was = ctx._in_interceptor
        try:
            ctx._in_interceptor = False
            await ctx.deal_damage(
                10, target=attacker, apply_modifiers=False)
        finally:
            ctx._in_interceptor = was
        return None


vermilion_city_gym_passive = VermilionCityGymPassive()


# ----------------------------------------------------------------------
# Narrow Gym / No Removal Gym / Pewter City Gym / Recall
# ----------------------------------------------------------------------

_NARROW_GYM_BENCH = 4
_ENERGY_REMOVAL_NAMES = frozenset(("Energy Removal", "Super Energy Removal"))


class NarrowGymPassive(Passive):
    """No player may have more than 4 Pokémon on the Bench."""

    def bench_capacity(self, player_id, carrier):
        return _NARROW_GYM_BENCH


narrow_gym_passive = NarrowGymPassive()


async def narrow_gym_on_play(ctx):
    """Each player over the 4-Bench cap returns 1 Benched Pokémon (and
    attachments) to hand; the opponent returns first."""
    moved = False
    for pid in (ctx.opponent_id, ctx.player_id):
        if not pid:
            continue
        while True:
            bench = ctx.board.find_player_area(pid, "bench")
            pokemon = [
                child for child in (bench.children if bench else [])
                if isinstance(child, PokemonEntity)
            ]
            extra = len(pokemon) - _NARROW_GYM_BENCH
            if extra <= 0:
                break
            target = await ctx.choose_pokemon(
                pokemon,
                "Choose a Benched Pokémon to return to your hand",
                player_id=pid,
            )
            if target is None:
                target = pokemon[0]
            await ctx.put_in_hand(full_stack(target), reveal=False)
            moved = True
    if not moved:
        ctx.suppress_announce = True


def _is_energy_removal_card(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None) or "")
    name = (definition.display_name or "") if definition else ""
    return name in _ENERGY_REMOVAL_NAMES


class NoRemovalGymPassive(Passive):
    """Playing Energy Removal or Super Energy Removal costs 2 extra hand cards."""

    def blocks_trainer_play(self, card, player_id, carrier):
        if not _is_energy_removal_card(card):
            return False
        parent = getattr(card, "parent", None)
        others = [
            child for child in (parent.children if parent else [])
            if child is not card
        ]
        return len(others) < 2

    def trainer_play_tax(self, card, player_id, carrier):
        return 2 if _is_energy_removal_card(card) else 0


no_removal_gym_passive = NoRemovalGymPassive()


def _pewter_city_gym_when(calc, carrier):
    attacker = calc.attacker
    return bool(
        calc.is_attack and attacker is not None
        and pokemon_name_contains("Brock")(attacker)
    )


pewter_city_gym_passive = no_resistance_passive(_pewter_city_gym_when)


class RecallPassive(Passive):
    """This turn, the holder may use attacks printed on attached Basic or
    Evolution cards (energy costs still apply)."""

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        attacks = []
        for child in pokemon.children:
            if not isinstance(child, PokemonEntity):
                continue
            for ability in getattr(def_for(child.archetype_id), "abilities", None) or []:
                if isinstance(ability, Attack):
                    attacks.append(ability)
        return attacks


async def recall(ctx):
    """For this attack this turn, the Active Pokémon may use attacks from
    its attached Basic or Evolution cards."""
    active = ctx.my_active()
    if active is None:
        return
    ctx.add_temporary_passive(
        active, RecallPassive(),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


# ----------------------------------------------------------------------
# Rocket's Hitmonchan / Moltres / Scyther / Snorlax
# ----------------------------------------------------------------------

_REBIRTH_OK = "_rebirth_ok"
_REBIRTH_BLOCKED = "_rebirth_blocked"


async def rebirth(ctx):
    """When Knocked Out, you may return this Pokémon to hand unless it was
    Asleep, Confused, or Paralyzed. ON_DAMAGED_BY_ATTACK snapshots that
    gate (conditions are cleared before ON_KNOCKED_OUT runs)."""
    holder = ctx.source
    if holder is None:
        ctx.suppress_announce = True
        return
    ok = getattr(ctx.session, _REBIRTH_OK, None)
    if ok is None:
        setattr(ctx.session, _REBIRTH_OK, set())
        ok = getattr(ctx.session, _REBIRTH_OK)
    blocked = getattr(ctx.session, _REBIRTH_BLOCKED, None)
    if blocked is None:
        setattr(ctx.session, _REBIRTH_BLOCKED, set())
        blocked = getattr(ctx.session, _REBIRTH_BLOCKED)

    if ctx.damage_amount > 0:
        if holder.get_attribute(AttrID.HP, 0) > 0:
            ctx.suppress_announce = True
            return
        if _asleep_confused_or_paralyzed(holder):
            blocked.add(holder.entity_id)
        else:
            ok.add(holder.entity_id)
        ctx.suppress_announce = True
        return

    if holder.entity_id in blocked:
        blocked.discard(holder.entity_id)
        ctx.suppress_announce = True
        return
    ok.discard(holder.entity_id)
    name = getattr(def_for(holder.archetype_id), "display_name", None) or "this Pokémon"
    if not await ctx.ask_yes_no(f"Return {name} to your hand?"):
        return
    await ctx.put_in_hand([holder], reveal=False)


class FireWallPassive(Passive):
    """If an attack damages this Pokémon (even if Knocked Out), attack the
    opponent's Active for 10 with Weakness and Resistance."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return None
        attacker = calc.attacker
        if attacker is None:
            return None
        dest = ctx.board.active_pokemon(attacker.owning_player_id) or attacker
        saved = ctx.attacker
        ctx.attacker = holder
        try:
            await ctx.deal_damage(10, target=dest, apply_modifiers=True)
        finally:
            ctx.attacker = saved
        return None


async def fire_wall(ctx):
    """Printed damage; during the opponent's next turn, a hit reflects 10
    with Weakness and Resistance (even if this Pokémon is Knocked Out)."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(ctx.attacker, FireWallPassive())


def _remove_temp_passive(board, carrier, cls):
    eid = getattr(carrier, "entity_id", None)
    board.temporary_passives = [
        temp for temp in board.temporary_passives
        if not (temp.carrier_entity_id == eid and isinstance(temp.passive, cls))
    ]


class ShadowImagesPassive(Passive):
    """Whenever this Pokémon is attacked, the opponent flips: tails, no
    damage (other effects still happen). Ends when it takes damage."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder or calc.amount <= 0:
            return None
        if calc.is_attack and calc.is_opposing:
            results = await ctx.flip_coins(
                1, "Shadow Images", source=holder)
            if results and not results[0]:
                calc.prevented = True
                return 0
        _remove_temp_passive(ctx.board, holder, ShadowImagesPassive)
        return None


async def shadow_images(ctx):
    """Until this Pokémon takes damage, is Benched, or evolves, attacks
    against it flip: tails, no damage."""
    if ctx.attacker is None:
        return
    ctx.add_temporary_passive(ctx.attacker, ShadowImagesPassive())


async def restless_sleep(ctx):
    """When damaged by an opponent's attack while already Asleep (even if
    Knocked Out), do 20 to the attacker with no Weakness or Resistance."""
    holder = ctx.source
    attacker = ctx.damaged_by
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    if (holder is None or attacker is None
            or asleep not in (holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
            or attacker.owning_player_id == holder.owning_player_id):
        ctx.suppress_announce = True
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False)


def return_energy_attack(energy_type=None, count: int = 1):
    """Return attached Energy to hand as a cost, then printed damage
    (Sabrina's Abra — Energy Loop)."""

    async def effect(ctx):
        energies = ctx.attached_energies(ctx.attacker)
        if energy_type is not None:
            energies = [
                energy for energy in energies
                if _typed_basic_energy(energy, energy_type)
            ]
        if len(energies) < count:
            return
        picks = await ctx.choose_cards(
            energies, count,
            prompt="Choose an Energy card to return to your hand")
        if len(picks) < count:
            return
        await ctx.put_in_hand(picks, reveal=False)
        await ctx.deal_damage()
    return effect


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Giovanni
# ----------------------------------------------------------------------

def has_named_pokemon_in_play(fragment: str, damaged: bool = False):
    """Playability: a Pokémon named with `fragment` is in play (optionally damaged)."""
    named = pokemon_name_contains(fragment)

    def check(board, player_id, pokemon=None) -> bool:
        return any(
            named(poked) and (not damaged or _is_damaged(board, poked))
            for poked in board.pokemon_in_play(player_id)
        )
    return check


class EvolveLineEarlyPassive(Passive):
    """This turn, `root` and Pokémon it evolves into may evolve even if just
    played or evolved, or if this is the first turn (Giovanni)."""

    def __init__(self, root_id: str):
        self.root_id = root_id

    def may_evolve_early(self, pokemon, carrier):
        if pokemon.entity_id == self.root_id:
            return True
        return any(
            getattr(card, "entity_id", None) == self.root_id
            for card in full_stack(pokemon)
        )


def gym_evolve_early(owner: str):
    """Choose a Pokémon named with `owner`. For the rest of this turn it
    (and what it evolves into) may evolve ignoring the just-played / first
    turn gates."""
    named = pokemon_name_contains(owner)

    async def effect(ctx):
        candidates = [poked for poked in ctx.my_pokemon_in_play() if named(poked)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon with {owner} in its name")
        if target is None:
            return
        ctx.add_temporary_passive(
            ctx.board.playmat,
            EvolveLineEarlyPassive(target.entity_id),
            expires_after_turn=ctx.session.turn_state.turn_number,
        )
    return effect


giovanni = gym_evolve_early("Giovanni")
giovanni_condition = has_named_pokemon_in_play("Giovanni")


def heal_named_then_discard_hand(owner: str):
    """Remove all damage from 1 of your Pokémon named with `owner`, then
    discard your hand (Giovanni's Last Resort)."""
    named = pokemon_name_contains(owner)

    async def effect(ctx):
        candidates = [
            poked for poked in ctx.my_pokemon_in_play()
            if named(poked) and _is_damaged(ctx.board, poked)
        ]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon with {owner} in its name")
        if target is None:
            return
        amount = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
        if amount > 0:
            await ctx.heal(amount, target)
        await ctx.discard_cards(list(ctx.hand()))
    return effect


giovannis_last_resort = heal_named_then_discard_hand("Giovanni")
giovannis_last_resort_condition = has_named_pokemon_in_play(
    "Giovanni", damaged=True)


async def summon_storm(ctx):
    """Flip 2 coins. Both heads: 20 to each other Pokémon, no Weakness or
    Resistance (Giovanni's Gyarados)."""
    results = await ctx.flip_coins(2, "Summon Storm")
    if not results or not all(results):
        return
    attacker = ctx.attacker
    for poked in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if attacker is not None and poked is attacker:
            continue
        await ctx.deal_damage(
            20, target=poked,
            ignore_weakness=True, ignore_resistance=True)


async def dragon_tornado(ctx):
    """Printed damage; unless that Knocks Out the Defending Pokémon, switch
    it with a Benched Pokémon you choose (Giovanni's Gyarados)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or defender in ctx.knockouts:
        return
    bench = ctx.opponent_bench()
    if not bench or ctx.effects_blocked(defender):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


class FortitudePassive(GutsSurvivePassive):
    """If this Pokémon would be KO'd by an opponent's attack, heads: remaining
    HP becomes 10. Off while Asleep, Confused, or Paralyzed."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is None or _asleep_confused_or_paralyzed(holder):
            return None
        return await super().damage_interceptor(ctx, calc, target, carrier)


fortitude_passive = FortitudePassive(hp_floor=10, title="Fortitude", flip=True)


async def false_charity(ctx):
    """Heads: look at the top of the opponent's deck; Trainer goes to their
    discard, otherwise into their hand (Giovanni's Meowth)."""
    results = await ctx.flip_coins(1, "False Charity")
    if not results or not results[0]:
        return
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    card = top[0]
    await ctx.session.prompt_view_cards(
        ctx.player_id, ctx.source.entity_id, [card],
        prompt="Top card of your opponent's deck",
    )
    if is_trainer_card(card):
        await ctx.discard_cards([card])
    else:
        await ctx.put_in_hand([card], reveal=False)


async def intimidate(ctx):
    """If the Defending Pokémon's max HP is 50 or less, it can't attack this
    Pokémon during the opponent's next turn. Benching or evolving either
    Pokémon ends the effect (Giovanni's Nidoking)."""
    defender = ctx.defender
    if defender is None or effective_max_hp(ctx.board, defender) > 50:
        return
    attacker = ctx.attacker
    if attacker is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(
        attacker, CantAttackThisPokemonPassive(defender)
    )


# ----------------------------------------------------------------------
# Gym Challenge (GYM2)
# ----------------------------------------------------------------------

def named_on_bench(fragment: str):
    """cond_fn: a Pokémon whose name contains `fragment` is on your Bench."""
    named = pokemon_name_contains(fragment)

    def cond(ctx) -> bool:
        return any(named(poked) for poked in ctx.my_bench())
    return cond


def is_named_trainer(name: str):
    """Deck/hand predicate: a Trainer whose display name is exactly `name`."""
    def pred(card) -> bool:
        if not is_trainer_card(card):
            return False
        return getattr(def_for(card.archetype_id), "display_name", None) == name
    return pred


async def call_the_boss(ctx):
    """When Giovanni's Persian is played from hand, you may search for Giovanni."""
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    if not deck or not deck.children:
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no(
            "Search your deck for the Trainer card named Giovanni?"):
        ctx.suppress_announce = True
        return
    await search_to_hand(
        is_named_trainer("Giovanni"), count=1, minimum=0, reveal=True,
        prompt="Choose the Trainer card named Giovanni.",
    )(ctx)


async def overhead_toss(ctx):
    """Printed damage to the Defending Pokémon; if you have a Bench, flip:
    tails, 20 to one of your Benched Pokémon (no W/R)."""
    await ctx.deal_damage()
    if not ctx.my_bench():
        return
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Overhead Toss")
    if results and results[0]:
        return
    await snipe_attack(
        20, side="mine",
        prompt="Choose 1 of your Benched Pokémon",
    )(ctx)


async def poison_power(ctx):
    """If this Pokémon is Poisoned, 40 instead of 20 and Poison the defender."""
    attacker = ctx.attacker
    poisoned_name = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
    is_poisoned = attacker is not None and poisoned_name in (
        attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage(40 if is_poisoned else 20)
    if is_poisoned:
        await ctx.apply_special_condition(
            ctx.defender, SpecialConditions.POISONED)


class KogaPoisonOnHitPassive(Passive):
    """This turn, if a Pokémon with Koga in its name does attack damage to a
    Defending Pokémon, that Pokémon is then Poisoned."""

    def __init__(self, player_id: str):
        self.player_id = player_id
        self._named = pokemon_name_contains("Koga")

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return None
        if calc.amount <= 0:
            return None
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != self.player_id:
            return None
        if not self._named(attacker):
            return None
        await ctx.apply_special_condition(target, SpecialConditions.POISONED)
        return None


async def koga(ctx):
    """This turn, Koga-named Pokémon that damage the Defending Pokémon Poison it."""
    ctx.add_temporary_passive(
        ctx.board.playmat,
        KogaPoisonOnHitPassive(ctx.player_id),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


class GiantGrowthPassive(Passive):
    """Koga's Ditto: max HP is 80 and Pound's base damage is 30. Ends when
    this Pokémon leaves the Active spot."""

    stacking_key = "kogas_ditto_giant_growth"

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return 0
        return 40

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not calc.attacker:
            return
        if not (calc.is_attack and calc.to_active):
            return
        if calc.attack_title != "Pound":
            return
        calc.amount += 20


async def giant_growth(ctx):
    """Heads: this Pokémon's max HP is 80 and Pound does 30. Benching ends it."""
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Giant Growth")
    if not results or not results[0]:
        return
    pokemon = ctx.attacker
    if pokemon is None:
        return
    max_before = effective_max_hp(ctx.board, pokemon)
    _remove_temp_passive(ctx.board, pokemon, GiantGrowthPassive)
    ctx.add_temporary_passive(pokemon, GiantGrowthPassive())
    ctx._shift_max_hp(pokemon, max_before)


async def sludge_grip(ctx):
    """If the opponent has a Bench, heads: you gust, then Poison the new Active."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Sludge Grip")
    if not results or not results[0]:
        return
    old_active = ctx.opponent_active()
    if old_active is None or ctx.effects_blocked(old_active):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon") or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)
    new_active = ctx.opponent_active()
    if new_active is not None:
        await ctx.apply_special_condition(new_active, SpecialConditions.POISONED)


def emerge_into(display_name: str):
    """Poké-Power: flip; heads, search the deck for `display_name` and evolve."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "Emerge")
        if not results or not results[0]:
            return
        pokemon = ctx.source
        logic_name = (
            pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            if pokemon is not None else None
        )

        def pred(card):
            if getattr(def_for(card.archetype_id), "display_name", None) != display_name:
                return False
            return bool(logic_name) and evolves_from(card.archetype_id, logic_name)

        picks = await ctx.search_deck(
            pred, count=1, minimum=0,
            prompt=f"Choose an Evolution card named {display_name}.",
        )
        if picks and pokemon is not None:
            await ctx.evolve_pokemon(pokemon, picks[0])
        await ctx.shuffle_deck()
    return effect


def shuffle_self_into_deck_on_flip(heads: bool = True):
    """Printed damage, then heads (or tails) shuffles this Pokémon and
    attachments into the deck (Obscuring Gas / Phoenix Flame shape)."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or bool(results[0]) != heads:
            return
        pokemon = ctx.attacker
        if pokemon is None:
            return
        await ctx.shuffle_into_deck(full_stack(pokemon), ctx.player_id)
        _defer_promote(ctx, ctx.player_id)
    return effect


obscuring_gas = shuffle_self_into_deck_on_flip(heads=True)


def return_self_to_hand_on_flip(heads: bool = True):
    """Printed damage, then heads (or tails) returns this Pokémon and
    attachments to hand (Star Boomerang)."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or bool(results[0]) != heads:
            return
        pokemon = ctx.attacker
        if pokemon is None:
            return
        was_active = pokemon is ctx.my_active()
        await ctx.put_in_hand(full_stack(pokemon), reveal=False)
        if was_active:
            _defer_promote(ctx, ctx.player_id)
    return effect


async def smelly_gas(ctx):
    """Printed damage; heads, 10 to each Benched Pokémon (both sides, no W/R)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Smelly Gas")
    if not results or not results[0]:
        return
    for poked in ctx.my_bench() + ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)


async def energy_drain(ctx):
    """When damaged by an opponent's attack (even if Knocked Out), flip:
    heads, discard 1 Energy from the attacker. Stops while Asleep, Confused,
    or Paralyzed."""
    holder = ctx.source
    attacker = ctx.damaged_by
    if (holder is None or attacker is None
            or _asleep_confused_or_paralyzed(holder)
            or attacker.owning_player_id == holder.owning_player_id):
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(1, "Energy Drain", source=holder)
    if not results or not results[0]:
        return
    if not ctx.attached_energies(attacker):
        return
    await ctx.discard_energy_from(
        attacker, 1, prompt="Choose an Energy card to discard")


def kogas_ninja_trick_targets(board, player_id, card=None):
    """Attach only to your Active Pokémon with Koga in its name."""
    named = pokemon_name_contains("Koga")
    active = board.active_pokemon(player_id)
    if active is not None and named(active):
        return [active]
    return []


def kogas_ninja_trick_condition(board, player_id, pokemon=None) -> bool:
    return bool(kogas_ninja_trick_targets(board, player_id))


class KogasNinjaTrickPassive(Passive):
    """When the opponent attacks this Active Pokémon, you may switch it with
    a Benched Pokémon before this damage (and later effects via ctx.defender).
    Discarded when the holder leaves the Active spot."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not target:
            return None
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if not is_in_active_spot(holder):
            return None
        owner_id = holder.owning_player_id
        if owner_id is None:
            return None
        bench = ctx.my_bench() if owner_id == ctx.player_id else ctx.opponent_bench()
        if not bench:
            return None
        name = getattr(def_for(holder.archetype_id), "display_name", None) \
            or "this Pokémon"
        if not await ctx.ask_yes_no(
                f"Use Koga's Ninja Trick to switch {name} with 1 of your "
                f"Benched Pokémon?",
                player_id=owner_id):
            return None
        replacement = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to switch into the Active Spot",
            player_id=owner_id)
        if replacement is None:
            return None
        await ctx.switch_active(owner_id, replacement)
        if carrier is not None and carrier is not holder:
            await ctx.discard_cards([carrier])
        was = ctx._in_interceptor
        try:
            ctx._in_interceptor = False
            await ctx.deal_damage(calc.base, target=replacement)
        finally:
            ctx._in_interceptor = was
        return 0


kogas_ninja_trick_passive = KogasNinjaTrickPassive()


def _ninja_trick_discard_tick(card_id, owner):
    """Discard the attached Ninja Trick once its holder is no longer Active;
    if it is still Active, check again at the next Pokémon Checkup."""
    async def _tick(session):
        attached = session.board_state.get_entity(card_id)
        if attached is None:
            return
        holder = carrier_pokemon(attached)
        if holder is not None and is_in_active_spot(holder):
            from spirit.game.session.effects import EffectContext
            tick_ctx = EffectContext(session, owner, attached, None)
            tick_ctx.schedule_at_checkup(1, _tick)
            return
        from spirit.game.session.effects import EffectContext
        discard_ctx = EffectContext(session, owner, attached, None)
        await discard_ctx.discard_cards([attached])
        await session._flush_effect_runs(discard_ctx)
    return _tick


async def kogas_ninja_trick(ctx):
    """Attach to your Active Pokémon with Koga in its name."""
    candidates = kogas_ninja_trick_targets(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_play_target(
        candidates, "Choose a Pokémon with Koga in its name")
    if target is None:
        return
    card = ctx.source
    await ctx.attach_energy(card, target)
    ctx.schedule_at_checkup(
        0, _ninja_trick_discard_tick(card.entity_id, ctx.player_id))



# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Blaine
# ----------------------------------------------------------------------

def _fire_provided_count(energy) -> int:
    """How much Fire an attached Energy card provides (0 if none)."""
    fire = PokemonTypes.FIRE.value
    if not energy_provides_type(energy, fire):
        return 0
    info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
    best = max((option.count(fire) for option in info.get("options", [])),
               default=0)
    return best or 1


class BlainePassive(Passive):
    """This turn, attaching a Fire Energy card from hand to a Blaine Pokémon
    may be followed by a second Fire Energy card onto the same Pokémon
    (replacing the free Energy attach)."""

    def __init__(self, player_id: str):
        self.player_id = player_id
        self._named = pokemon_name_contains("Blaine")
        self._second_armed = False

    def allows_second_energy_attach(self, pokemon, carrier):
        if pokemon.owning_player_id != self.player_id:
            return False
        if not self._named(pokemon):
            return False
        energies = [c for c in pokemon.children if isinstance(c, EnergyEntity)]
        if not energies or not _typed_basic_energy(
                energies[-1], PokemonTypes.FIRE):
            return False
        self._second_armed = True
        return True

    def blocks_energy_attach(self, attaching_player_id, energy, target, carrier):
        if not self._second_armed or attaching_player_id != self.player_id:
            return False
        return not _typed_basic_energy(energy, PokemonTypes.FIRE)


def blaine_condition(board, player_id, card=None) -> bool:
    """Unplayable after the free Energy attach, or if Blaine already resolved."""
    state = getattr(board, "turn_state", None)
    if state is None:
        return True
    if state.energy_attached:
        return False
    return all(name != "Blaine" for _arch, name, _tt in state.trainers_played)


async def blaine(ctx):
    """This turn, a Fire Energy attach to a Blaine Pokémon may include a
    second Fire Energy card onto the same Pokémon."""
    ctx.add_temporary_passive(
        ctx.board.playmat,
        BlainePassive(ctx.player_id),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


async def roaring_flames(ctx):
    """Discard Fire Energy cards (or all Energy if each provides 2 Fire);
    20 plus 20 per Fire Energy discarded (Blaine's Charizard)."""
    attacker = ctx.attacker
    if attacker is None:
        return
    energies = list(ctx.attached_energies(attacker))
    fire_cards = [e for e in energies if _typed_basic_energy(e, PokemonTypes.FIRE)]
    all_double_fire = bool(energies) and all(
        _fire_provided_count(e) >= 2 for e in energies)
    to_discard = list(energies) if all_double_fire else fire_cards
    units = sum(_fire_provided_count(e) for e in to_discard)
    if to_discard:
        await ctx.discard_cards(to_discard)
    amount = 20 + 20 * units
    if amount > 0:
        await ctx.deal_damage(amount)


async def flame_jet(ctx):
    """Heads: 40 to one opposing Pokémon, no Weakness or Resistance."""
    results = await ctx.flip_coins(1, "Flame Jet")
    if not results or not results[0]:
        return
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(
            40, target=target,
            ignore_weakness=True, ignore_resistance=True)


async def bonfire(ctx):
    """Flip 3 coins; discard 1 Fire Energy per heads (else nothing); then
    10×heads to each opposing Pokémon with no Weakness or Resistance."""
    results = await ctx.flip_coins(3, "Bonfire")
    heads = sum(1 for result in results if result)
    if heads == 0:
        return
    fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
    if len(fire) < heads:
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, heads,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        prompt="Choose Fire Energy cards to discard")
    if len(discarded) < heads:
        return
    amount = 10 * heads
    for poked in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(
            amount, target=poked,
            ignore_weakness=True, ignore_resistance=True)


stoke = search_attach_energy(
    predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
    count=1, to_self=True,
    prompt="Choose a Fire Energy card to attach.",
)


async def pranks(ctx):
    """Heads: put a card from the opponent's discard pile on top of their deck."""
    results = await ctx.flip_coins(1, "Pranks")
    if not results or not results[0]:
        return
    pile = ctx.discard_pile(ctx.opponent_id)
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, prompt="Choose a card from your opponent's discard pile")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


async def lunar_power(ctx):
    """Heads: search for a card that evolves from 1 of your Benched Pokémon
    and evolve that Pokémon; shuffle (Erika's Clefairy)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Lunar Power")
    if not results or not results[0]:
        return
    bench = ctx.my_bench()
    names = {
        poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        for poked in bench
        if poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    }
    picks = await ctx.search_deck(
        lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) in names,
        count=1, minimum=0,
        prompt="Choose a card that evolves from 1 of your Benched Pokémon.",
    )
    if picks:
        evo = picks[0]
        from_name = evo.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
        candidates = [
            poked for poked in bench
            if poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == from_name
        ]
        target = None
        if len(candidates) == 1:
            target = candidates[0]
        elif candidates:
            target = await ctx.choose_pokemon(
                candidates, "Choose the Pokémon to evolve")
        if target is not None:
            await ctx.evolve_pokemon(target, evo)
    await ctx.shuffle_deck()


class RelaxingScentPassive(Passive):
    """While this Pokémon is Active, attack damage to any Pokémon is halved
    after W/R, rounded up to the nearest 10. Stops while Asleep, Confused,
    or Paralyzed (Erika's Ivysaur)."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack or calc.amount <= 0:
            return
        holder = carrier_pokemon(carrier) or carrier
        if not is_in_active_spot(holder):
            return
        if _asleep_confused_or_paralyzed(holder):
            return
        calc.amount = (((calc.amount + 1) // 2 + 9) // 10) * 10


relaxing_scent = RelaxingScentPassive()


def heal_damaged_in_play(amount: int):
    """Remove `amount` damage from each damaged Pokémon in play (both sides).
    Erika's Jigglypuff — Group Therapy (10); Erika's Kindness (20)."""
    async def effect(ctx):
        for poked in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
            if _is_damaged(ctx.board, poked):
                await ctx.heal(amount, poked)
    return effect


group_therapy = heal_damaged_in_play(10)
erikas_kindness = heal_damaged_in_play(20)


async def growth(ctx):
    """Heads: you may attach up to 2 Grass Energy from hand to the attacker
    (Erika's Venusaur)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Growth")
    if not results or not results[0]:
        return
    grass = [
        card for card in ctx.hand()
        if _typed_basic_energy(card, PokemonTypes.GRASS)
    ]
    if not grass:
        return
    picks = await ctx.choose_cards(
        grass, min(2, len(grass)), minimum=0,
        prompt="Choose up to 2 Grass Energy cards to attach",
    )
    attacker = ctx.attacker
    if attacker is None:
        return
    for energy in picks:
        await ctx.attach_energy(energy, attacker)


async def fervor(ctx):
    """Show the top 3 cards; put Fire Energy into your hand and discard the rest."""
    top = ctx.deck_top(3)
    if not top:
        return
    await ctx.reveal_cards(top)
    energy = [card for card in top if _typed_basic_energy(card, PokemonTypes.FIRE)]
    rest = [card for card in top if card not in energy]
    if energy:
        await ctx.put_in_hand(energy, reveal=True)
    if rest:
        await ctx.discard_cards(rest)


def gym_flip_shuffle_named(owner: str):
    """Stadium: flip; heads, you may shuffle 1 of your Pokémon named with
    `owner` and its attachments into your deck (Fuchsia City Gym)."""
    named = pokemon_name_contains(owner)

    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        candidates = [
            poked for poked in ctx.my_pokemon_in_play() if named(poked)
        ]
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates,
            f"Choose a Pokémon with {owner} in its name to shuffle into your deck",
            optional=True,
        )
        if target is None:
            return
        was_active = target is ctx.my_active()
        await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)
        if was_active:
            _defer_promote(ctx, ctx.player_id)
    return effect


fuchsia_city_gym = gym_flip_shuffle_named("Koga")
fuchsia_city_gym_condition = has_named_pokemon_in_play("Koga")


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Brock / Erika / Chaos Gym / Cinnabar City Gym
# ----------------------------------------------------------------------

async def detonate(ctx):
    """Printed damage; 10 to each Benched Pokémon (both sides, no W/R);
    50 to the attacker (no W/R); discard a Stadium in play."""
    await ctx.deal_damage()
    for poked in ctx.my_bench() + ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)
    await ctx.deal_damage(50, target=ctx.attacker, apply_modifiers=False)
    await ctx.discard_stadium()


async def mega_thrash(ctx):
    """Printed damage; 20 to the attacker (no W/R); discard a Stadium."""
    await ctx.deal_damage()
    await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    await ctx.discard_stadium()


_SHAPESHIFT_ATTR = "_shapeshift"
_SHAPESHIFT_ATTACH_TURN = "_shapeshift_attach_turn"


def _shapeshift_cards(pokemon):
    return [
        child for child in pokemon.children
        if isinstance(child, PokemonEntity)
        and child.get_attribute(_SHAPESHIFT_ATTR)
    ]


def _shapeshift_template(holder):
    cards = _shapeshift_cards(holder)
    return cards[-1] if cards else None


def shapeshift_condition(board, player_id, pokemon=None) -> bool:
    """Not Asleep/Confused/Paralyzed, and either an Evolution is in hand
    (once per turn) or a Shapeshift Evolution is already attached."""
    if pokemon is None or _asleep_confused_or_paralyzed(pokemon):
        return False
    if _shapeshift_cards(pokemon):
        return True
    turn = getattr(getattr(board, "turn_state", None), "turn_number", None)
    if pokemon.get_attribute(_SHAPESHIFT_ATTACH_TURN) == turn:
        return False
    hand = board.find_player_area(player_id, "hand")
    return any(is_evolution_pokemon(card) for card in (hand.children if hand else []))


async def shapeshift(ctx):
    """Attach an Evolution from hand (once per turn) and/or discard one
    already attached via Shapeshift."""
    holder = ctx.source
    if holder is None or _asleep_confused_or_paralyzed(holder):
        return
    turn = ctx.session.turn_state.turn_number
    can_attach = (
        holder.get_attribute(_SHAPESHIFT_ATTACH_TURN) != turn
        and any(is_evolution_pokemon(card) for card in ctx.hand())
    )
    attached = _shapeshift_cards(holder)
    options = []
    if can_attach:
        options.append("Attach an Evolution card from your hand")
    if attached:
        options.append("Discard the Evolution card attached")
    if not options:
        return
    if len(options) == 1:
        choice = 0
    else:
        choice = await ctx.choose("Shapeshift", options)
    max_before = effective_max_hp(ctx.board, holder)
    if options[choice].startswith("Attach"):
        evolutions = [card for card in ctx.hand() if is_evolution_pokemon(card)]
        picks = await ctx.choose_cards(
            evolutions, 1,
            prompt="Choose an Evolution card to attach to Brock's Ninetales")
        if not picks:
            return
        evo = picks[0]
        evo.set_attribute(_SHAPESHIFT_ATTR, True)
        await ctx.attach_energy(evo, holder)
        holder.set_attribute(_SHAPESHIFT_ATTACH_TURN, turn)
    else:
        top = attached[-1]
        await ctx.discard_cards([top])
    ctx._shift_max_hp(holder, max_before)
    await ctx.session.refresh_granted_abilities(holder)


class ShapeshiftPassive(Passive):
    """Treat this Pokémon as the attached Evolution (type, HP, Weakness,
    Resistance, retreat, attacks). Can't evolve, devolve, or use that
    Pokémon's Pokémon Power. Discards the Evolution cards if A/C/P."""

    def _template(self, holder):
        if holder is None or _asleep_confused_or_paralyzed(holder):
            return None
        return _shapeshift_template(holder)

    def modify_pokemon_types(self, types, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return types
        template = self._template(holder)
        if template is None:
            return types
        return list(template.get_attribute(AttrID.POKEMON_TYPES) or types)

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return 0
        template = self._template(holder)
        if template is None:
            return 0
        copied = template.attribute_originals.get(
            AttrID.HP.value, template.get_attribute(AttrID.HP, 0))
        printed = pokemon.attribute_originals.get(
            AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0))
        return int(copied or 0) - int(printed or 0)

    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not calc.target:
            return
        template = self._template(holder)
        if template is None:
            return
        calc.weak_types = list(template.get_attribute(AttrID.WEAKNESS_TYPES) or [])

    def modify_resistance(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not calc.target:
            return
        template = self._template(holder)
        if template is None:
            return
        calc.resist_type = template.get_attribute(AttrID.RESISTANCE_TYPES)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return cost
        template = self._template(holder)
        if template is None:
            return cost
        return int(template.get_attribute(AttrID.RETREAT_COST) or 0)

    def granted_attacks(self, board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return []
        template = self._template(holder)
        if template is None:
            return []
        definition = def_for(template.archetype_id)
        return [ability for ability in (getattr(definition, "abilities", None) or [])
                if isinstance(ability, Attack)]

    def hides_printed_attacks(self, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return pokemon is holder and self._template(holder) is not None

    def blocks_evolution(self, player_id, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return target is holder and self._template(holder) is not None

    def blocks_devolution(self, target, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return target is holder and self._template(holder) is not None

    async def after_condition_applied(self, ctx, target, condition, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return
        if condition not in (
            SpecialConditions.ASLEEP,
            SpecialConditions.CONFUSED,
            SpecialConditions.PARALYZED,
        ):
            return
        attached = _shapeshift_cards(holder)
        if not attached:
            return
        max_before = effective_max_hp(ctx.board, holder)
        await ctx.discard_cards(attached)
        ctx._shift_max_hp(holder, max_before)
        await ctx.session.refresh_granted_abilities(holder)


shapeshift_passive = ShapeshiftPassive()


class ScramPassive(Passive):
    """If remaining HP is exactly 10, shuffle this Pokémon and attachments
    into the deck. Stops while Asleep, Confused, or Paralyzed."""

    async def after_hp_changed(self, ctx, target, remaining, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder or remaining != 10:
            return
        if _asleep_confused_or_paralyzed(holder):
            return
        owner = holder.owning_player_id
        if owner is None:
            return
        was_active = holder is ctx.board.active_pokemon(owner)
        await ctx.shuffle_into_deck(full_stack(holder), owner)
        if was_active:
            _defer_promote(ctx, owner)


scram_passive = ScramPassive()


def brocks_protection_targets(board, player_id, card=None):
    named = pokemon_name_contains("Brock")
    return [poked for poked in board.pokemon_in_play(player_id) if named(poked)]


def brocks_protection_condition(board, player_id, pokemon=None) -> bool:
    return bool(brocks_protection_targets(board, player_id))


class BrocksProtectionPassive(Passive):
    """Energy on the holder can't be removed by the opponent's attacks or
    Trainer cards."""

    def _protects(self, card, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or carrier_pokemon(card) is not holder:
            return False
        return is_energy_card(card)

    def blocks_energy_removal(self, energy, mover_player_id, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or mover_player_id == holder.owning_player_id:
            return False
        return self._protects(energy, carrier)

    def blocks_discard(self, card, carrier):
        return self._protects(card, carrier)


brocks_protection_passive = BrocksProtectionPassive()


async def brocks_protection(ctx):
    """Attach to 1 of your Pokémon with Brock in its name."""
    candidates = brocks_protection_targets(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_play_target(
        candidates, "Choose a Pokémon with Brock in its name")
    if target is None:
        return
    await ctx.attach_energy(ctx.source, target)


class ChaosGymPassive(Passive):
    """Whenever a player plays a Trainer other than a Stadium, they flip:
    heads plays normally; tails the opponent may use it instead."""

    def taxes_trainer_play(self, card, player_id, carrier):
        return True


chaos_gym_passive = ChaosGymPassive()


class CinnabarCityGymPassive(Passive):
    """Ignore Weakness when a Water Pokémon damages a Pokémon with Blaine
    in its name."""

    def modify_weakness(self, calc, carrier):
        attacker = calc.attacker
        target = calc.target
        if attacker is None or target is None:
            return
        if PokemonTypes.WATER.value not in effective_pokemon_types(
                calc.board, attacker):
            return
        if not pokemon_name_contains("Blaine")(target):
            return
        calc.weakness_applies = False


cinnabar_city_gym_passive = CinnabarCityGymPassive()


def soak_up_condition(board, player_id, pokemon=None) -> bool:
    """Not Asleep/Confused/Paralyzed, and another of your Pokémon has Grass
    Energy attached."""
    if pokemon is None or _asleep_confused_or_paralyzed(pokemon):
        return False
    return any(
        poked is not pokemon and any(
            _typed_basic_energy(energy, PokemonTypes.GRASS)
            for energy in board.attached_energies(poked))
        for poked in board.pokemon_in_play(player_id)
    )


async def soak_up(ctx):
    """Move up to 2 Grass Energy cards from your other Pokémon onto this one."""
    holder = ctx.source
    if holder is None:
        return
    sources = [poked for poked in ctx.my_pokemon_in_play() if poked is not holder]
    await ctx.move_energy_freely(
        sources, [holder],
        predicate=lambda card: _typed_basic_energy(card, PokemonTypes.GRASS),
        max_count=2,
        prompt="Choose up to 2 Grass Energy cards to attach to Erika's Bellsprout",
    )


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Sabrina's Psyduck / Psychic Control / stadiums
# ----------------------------------------------------------------------

async def random_esp(ctx):
    """Heads: printed damage and Confuse the Defending Pokémon. Tails: no
    damage, this Pokémon is Confused (Sabrina's Psyduck)."""
    results = await ctx.flip_coins(1, "Random ESP")
    if results and results[0]:
        await ctx.deal_damage()
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
        return
    if ctx.attacker is not None:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


_STAYS_IN_PLAY_TRAINER_TYPES = (
    TrainerType.STADIUM.value,
    TrainerType.POKEMON_TOOL.value,
    TrainerType.POKEMON_TOOL_F.value,
    TrainerType.TECHNICAL_MACHINE.value,
)


def _trainer_stays_in_play(card) -> bool:
    """PlusPower, Mysterious Fossil, Stadiums, Tools, TMs stay in play."""
    ttype = card.get_attribute(AttrID.TRAINER_TYPE)
    if ttype in _STAYS_IN_PLAY_TRAINER_TYPES:
        return True
    definition = def_for(getattr(card, "archetype_id", None) or "")
    if definition is None:
        return True
    if getattr(definition, "plays_as_pokemon", False):
        return True
    return getattr(definition, "passive", None) is not None


def _psychic_control_runnable(card) -> bool:
    if not is_trainer_card(card) or _trainer_stays_in_play(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


def sabrinas_psychic_control_candidates(board, player_id):
    opponent_id = _opponent_id(board, player_id)
    if opponent_id is None:
        return []
    discard = board.find_player_area(opponent_id, "discard")
    if discard is None:
        return []
    return [card for card in discard.children if _psychic_control_runnable(card)]


def sabrinas_psychic_control_condition(board, player_id, pokemon=None) -> bool:
    return bool(sabrinas_psychic_control_candidates(board, player_id))


async def sabrinas_psychic_control(ctx):
    """Heads: you may use a one-shot Trainer from the opponent's discard as
    if it were in your hand; the card stays there (Sabrina's Psychic Control)."""
    results = await ctx.flip_coins(1, "Sabrina's Psychic Control")
    if not results or not results[0]:
        return
    candidates = sabrinas_psychic_control_candidates(ctx.board, ctx.player_id)
    if not candidates:
        return
    picked = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a Trainer card to use from your opponent's discard pile",
    )
    if not picked:
        return
    effect = TRAINER_EFFECTS_BY_GUID.get((picked[0].archetype_id or "").lower())
    if effect is None or effect is unimplemented:
        return
    await effect(ctx)


def gym_return_named_basic_energy(owner: str):
    """Stadium: return 1 basic Energy from a Pokémon named with `owner`
    (Saffron City Gym)."""
    named = pokemon_name_contains(owner)

    def condition(board, player_id, stadium=None) -> bool:
        return any(
            named(poked) and any(
                is_basic_energy_card(energy)
                for energy in board.attached_energies(poked)
            )
            for poked in board.pokemon_in_play(player_id)
        )

    async def effect(ctx):
        pool = [
            energy
            for poked in ctx.my_pokemon_in_play() if named(poked)
            for energy in ctx.attached_energies(poked)
            if is_basic_energy_card(energy)
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1,
            prompt="Choose a basic Energy card to return to your hand",
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=False)

    return condition, effect


saffron_city_gym_condition, saffron_city_gym = gym_return_named_basic_energy(
    "Sabrina")


class NamedHealOnEvolvePassive(Passive):
    """Whenever a Pokémon named with `owner` evolves, heal `amount`
    (Viridian City Gym — 2 damage counters)."""

    def __init__(self, owner: str, amount: int = 20):
        self._named = pokemon_name_contains(owner)
        self.amount = amount

    def heal_on_evolve(self, evolved, pre_evolution, player_id, carrier):
        if not self._named(evolved):
            return 0
        return self.amount


viridian_city_gym_passive = NamedHealOnEvolvePassive("Giovanni", 20)


async def transparent_walls(ctx):
    """Until the end of the opponent's next turn, prevent attack damage to
    this player's Benched Pokémon (other attack effects still happen)."""
    player_id = ctx.player_id

    def pred(calc, carrier):
        return (
            calc.is_attack
            and calc.target is not None
            and calc.target.owning_player_id == player_id
            and not calc.to_active
        )

    ctx.add_passive_through_opponents_turn(
        ctx.board.playmat,
        prevent_damage_when(pred, attacks_only=False),
    )


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Rocket / Sabrina
# ----------------------------------------------------------------------

async def electroburn(ctx):
    """Printed damage, then 10 self-damage per Lightning Energy card attached
    (Rocket's Zapdos)."""
    await ctx.deal_damage()
    n = count_energy("self", PokemonTypes.LIGHTNING, cards=True)(ctx)
    if n:
        await ctx.deal_damage(10 * n, target=ctx.attacker, apply_modifiers=False)


async def rockets_minefield_gym_watch(ctx):
    """Flip; tails, 2 damage counters on the Basic just benched from hand."""
    pokemon = ctx.benched_pokemon
    if pokemon is None:
        return
    results = await ctx.flip_coins(1, "Rocket's Minefield Gym", source=pokemon)
    if results and not results[0]:
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                              as_counters=True)


async def rockets_secret_experiment(ctx):
    """Heads: search any card into hand. Tails: no Trainers until the end of
    your next turn."""
    results = await ctx.flip_coins(1, "Rocket's Secret Experiment")
    if results and results[0]:
        await search_to_hand(
            count=1, reveal=False,
            prompt="Choose a card to put into your hand.",
        )(ctx)
        return
    ctx.lock_plays(
        ctx.player_id, is_trainer_card,
        through_turn=ctx.session.turn_state.turn_number + 2,
    )


def sabrina_condition(board, player_id, pokemon=None) -> bool:
    """Two Pokémon named Sabrina in play, and at least one has Energy."""
    named = pokemon_name_contains("Sabrina")
    named_pokemon = [poked for poked in board.pokemon_in_play(player_id)
                     if named(poked)]
    if len(named_pokemon) < 2:
        return False
    return any(board.attached_energies(poked) for poked in named_pokemon)


async def sabrina(ctx):
    """Move all Energy from 1 Sabrina Pokémon onto another."""
    named = pokemon_name_contains("Sabrina")
    named_pokemon = [poked for poked in ctx.my_pokemon_in_play() if named(poked)]
    sources = [poked for poked in named_pokemon if ctx.attached_energies(poked)]
    if not sources or len(named_pokemon) < 2:
        return
    source = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
        sources, "Choose a Pokémon with Sabrina in its name")
    if source is None:
        return
    dests = [poked for poked in named_pokemon if poked is not source]
    if not dests:
        return
    dest = dests[0] if len(dests) == 1 else await ctx.choose_pokemon(
        dests, "Choose another Pokémon with Sabrina in its name")
    if dest is None:
        return
    for energy in list(ctx.attached_energies(source)):
        await ctx.move_energy(energy, dest)


def same_attached_energy_count(board, player_id, pokemon=None) -> bool:
    """This Pokémon and the Defending Pokémon have the same number of Energy
    cards attached (Sabrina's Abra — Synchronize)."""
    opponent = _opponent_id(board, player_id)
    defending = board.active_pokemon(opponent) if opponent else None
    if pokemon is None or defending is None:
        return False
    return (len(board.attached_energies(pokemon))
            == len(board.attached_energies(defending)))


async def look_at_opponent_hand(ctx):
    """Look at your opponent's hand (Sabrina's Abra — Psyscan)."""
    await ctx.reveal_hand(of_player=ctx.opponent_id)


class PsylinkPassive(Passive):
    """This Pokémon has a copy of every attack your other Psychic Pokémon in
    play have. Off while Asleep, Confused, or Paralyzed."""

    def granted_attacks(self, board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return []
        if _asleep_confused_or_paralyzed(holder):
            return []
        owner = holder.owning_player_id
        attacks = []
        seen = set()
        for poked in board.pokemon_in_play(owner):
            if poked is holder or not pokemon_has_type(poked, PokemonTypes.PSYCHIC):
                continue
            definition = def_for(poked.archetype_id)
            for attack in getattr(definition, "abilities", None) or []:
                if not isinstance(attack, Attack):
                    continue
                key = attack.ability_id or (attack.title, attack.game_text)
                if key in seen:
                    continue
                seen.add(key)
                attacks.append(attack)
        return attacks


psylink_passive = PsylinkPassive()


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Koga / Lt. Surge
# ----------------------------------------------------------------------

async def aerial_maneuvers(ctx):
    """10; heads, +30 and prevent all effects of attacks, including damage."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Aerial Maneuvers")
    heads = bool(results and results[0])
    base = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(base + (30 if heads else 0))
    if heads:
        await apply_protection(ctx, prevent=True, effects_too=True)


def messenger(exclude_name: str = "Koga's Pidgey"):
    """Put this Pokémon and attachments on top of the deck, then search for
    a Basic or Evolution not named `exclude_name` into hand and shuffle."""
    async def effect(ctx):
        pokemon = ctx.attacker
        if pokemon is None:
            return
        was_active = pokemon is ctx.my_active()
        stack = full_stack(pokemon)
        for card in stack[1:]:
            await ctx.put_on_top_of_deck(card)
        ctx.session.clear_pokemon_effects(pokemon)
        ctx.session.reset_pokemon_damage(pokemon)
        ctx.session.reset_ability_usage(pokemon)
        await ctx.put_on_top_of_deck(pokemon)
        if was_active:
            _defer_promote(ctx, ctx.player_id)

        def pred(card):
            if not (is_basic_pokemon(card) or is_evolution_pokemon(card)):
                return False
            definition = def_for(getattr(card, "archetype_id", None) or "")
            return getattr(definition, "display_name", None) != exclude_name

        picks = await ctx.search_deck(
            pred, count=1, minimum=0,
            prompt="Choose a Basic Pokémon or Evolution card "
                   f"not named {exclude_name}.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def flip_draw(n: int = 1):
    """Flip a coin. If heads, draw `n` cards."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if results and results[0]:
            await ctx.draw_cards(n)
    return effect


async def spontaneous_explosion(ctx):
    """10; heads, +30 and 30 damage to self (no W/R)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Spontaneous Explosion")
    heads = bool(results and results[0])
    base = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(base + (30 if heads else 0))
    if heads:
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)


def group_attack(display_name: str = "Koga's Zubat", per: int = 10):
    """May bench any number of Basics named `display_name`, then `per` times
    the number of those Pokémon in play."""
    named = pokemon_name_contains(display_name)

    def pred(card) -> bool:
        return is_basic_pokemon(card) and named(card)

    async def effect(ctx):
        space = effective_bench_capacity(ctx.board, ctx.player_id) - len(
            ctx.my_bench())
        if space > 0 and ctx.deck() and await ctx.ask_yes_no(
                f"Search your deck for any number of Basic Pokémon named "
                f"{display_name}?"):
            picks = await ctx.search_deck(
                pred, count=space, minimum=0,
                prompt=f"Choose Basic Pokémon named {display_name} "
                       "to put onto your Bench.",
            )
            for card in picks:
                await ctx.bench_pokemon(card)
            await ctx.shuffle_deck()
        count = sum(1 for poked in ctx.my_pokemon_in_play() if named(poked))
        amount = per * count
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


async def surprise(ctx):
    """Look at a random card from the opponent's hand; they shuffle it in."""
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    card = random.choice(hand)
    source = ctx.source or ctx.attacker
    if source is not None:
        await ctx.session.prompt_view_cards(
            ctx.player_id, source.entity_id, [card],
            prompt="A random card from your opponent's hand",
        )
    await ctx.shuffle_into_deck([card], ctx.opponent_id)


async def shock_blast(ctx):
    """If Active and damaged (even if Knocked Out), tails: 20 to each Active
    (no W/R). Works while Asleep, Confused, or Paralyzed."""
    holder = ctx.source
    if holder is None or not is_in_active_spot(holder):
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(1, "Shock Blast", source=holder)
    if not results or results[0]:
        return
    for poked in (ctx.my_active(), ctx.opponent_active()):
        if poked is not None:
            await ctx.deal_damage(20, target=poked, apply_modifiers=False)


async def high_voltage(ctx):
    """Printed damage; heads, the opponent can't play Trainer cards next turn."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "High Voltage")
    if not results or not results[0]:
        return
    defender = ctx.defender
    if defender is not None and ctx.effects_blocked(defender):
        return
    await headache(ctx)


async def thunder_flare(ctx):
    """30 + 10 per damage counter on self; then tails, 30 to self."""
    await damage_per(damage_counters_on("self"), 10, base=30)(ctx)
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Thunder Flare")
    if results and not results[0]:
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Sabrina
# ----------------------------------------------------------------------

async def fade_out(ctx):
    """Printed damage; return this Pokémon and its Energy to hand, discarding
    other attached cards (Sabrina's Gastly — Fade Out)."""
    await ctx.deal_damage()
    pokemon = ctx.attacker
    if pokemon is None:
        return
    was_active = pokemon is ctx.my_active()
    energies = list(ctx.attached_energies(pokemon))
    others = [card for card in full_stack(pokemon)
              if card is not pokemon and card not in energies]
    if others:
        await ctx.discard_cards(others)
    await ctx.put_in_hand([pokemon, *energies], reveal=False)
    if was_active:
        _defer_promote(ctx, ctx.player_id)


class HpPerEnergyCardPassive(Passive):
    """Holder gets +`per` max HP for each basic Energy card of `energy_type`
    attached (Gaseous Form). Does not shut off for Asleep/Confused/Paralyzed."""

    def __init__(self, energy_type, per: int = 10):
        self.energy_type = energy_type
        self.per = per

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return 0
        return self.per * sum(
            1 for child in holder.children
            if _typed_basic_energy(child, self.energy_type)
        )


def hp_per_energy_card_passive(energy_type, per: int = 10) -> Passive:
    return HpPerEnergyCardPassive(energy_type, per)


gaseous_form_passive = hp_per_energy_card_passive(PokemonTypes.PSYCHIC, 10)


async def dark_wave(ctx):
    """Printed damage; all Pokémon Powers stop working through the opponent's
    next turn (Sabrina's Gengar — Dark Wave)."""
    await ctx.deal_damage()
    await goop_gas_attack(ctx)


async def damage_shift(ctx):
    """Move 1 damage counter from each of your damaged Pokémon onto the
    Defending Pokémon (no Weakness or Resistance)."""
    defender = ctx.defender
    if defender is None:
        return
    for source in ctx.my_pokemon_in_play():
        if _is_damaged(ctx.board, source):
            await ctx.move_damage_counters(source, defender, max_count=1)


async def invigorate(ctx):
    """Put 1 Basic from either discard onto that player's Bench, with damage
    counters equal to half its HP rounded down to the nearest 10."""
    candidates = []
    for player_id in ctx.board.player_ids:
        if not bench_has_room(ctx.board, player_id):
            continue
        candidates.extend(
            card for card in ctx.discard_pile(player_id) if is_basic_pokemon(card)
        )
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon in any player's discard pile",
    )
    if not picks:
        return
    card = picks[0]
    if not await ctx.bench_pokemon(card):
        return
    counters = ctx.max_hp(card) // 20
    if counters:
        await ctx.set_damage_counters(card, counters)


async def helping_hand(ctx):
    """Choose 1 of the opponent's Pokémon, remove any number of damage
    counters, then draw that many cards."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    available = max(0, (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10)
    if available <= 0:
        return
    n = await ctx.choose(
        "Remove any number of damage counters.",
        [str(i) for i in range(available + 1)],
        use_panel=False,
    )
    if n <= 0:
        return
    healed = await ctx.heal(n * 10, target)
    if healed > 0:
        await ctx.draw_cards(healed // 10)


async def life_drain(ctx):
    """Heads: put damage counters on the Defending Pokémon so its remaining
    HP is 10."""
    title = ctx.ability.title if ctx.ability else "Life Drain"
    results = await ctx.flip_coins(1, title)
    if not results or not results[0]:
        return
    target = ctx.defender
    if target is None:
        return
    hp = target.get_attribute(AttrID.HP, 0)
    if hp > 10:
        await ctx.deal_damage(hp - 10, target=target, as_counters=True)


async def magic_darts(ctx):
    """Choose 1 of the opponent's Pokémon; 10×heads of 3 coins, no W/R."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    title = ctx.ability.title if ctx.ability else "Magic Darts"
    results = await ctx.flip_coins(3, title)
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(
            10 * heads, target=target,
            ignore_weakness=True, ignore_resistance=True,
        )


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Misty's Gyarados / Horsea / Poliwag / Psyduck
# Misty's Tears / Misty's Wish / Resistance Gym
# ----------------------------------------------------------------------

async def rebellion(ctx):
    """Whenever this Pokémon attacks, flip 2 coins. Both tails: the attack
    does nothing; shuffle this Pokémon and attachments into the deck.
    (Misty's Gyarados — Rebellion; works even if Confused.)"""
    results = await ctx.flip_coins(2, "Rebellion")
    if results and not any(results):
        pokemon = ctx.attacker
        if pokemon is None:
            return
        await ctx.shuffle_into_deck(full_stack(pokemon), ctx.player_id)
        _defer_promote(ctx, ctx.player_id)
        return
    await ctx.deal_damage()


async def ink_spurt(ctx):
    """Printed damage; heads, the Defending Pokémon must flip to attack
    until it evolves or is Benched (Misty's Horsea — Ink Spurt)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Ink Spurt")
    if not results or not results[0]:
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.require_attack_flip(
        defender,
        through_turn=ctx.session.turn_state.turn_number + 1000,
        title=ctx.ability.title if ctx.ability else "Ink Spurt",
    )


def lock_this_attack_on_flip(heads: bool = False):
    """Printed damage, then lock this attack through your next turn when
    the coin is heads (or tails if heads=False). Bubbles / similar."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or bool(results[0]) != heads:
            return
        attacker = ctx.attacker
        ability = ctx.ability
        if attacker is None or ability is None or not ability.ability_id:
            return
        ctx.session.turn_state.lock_attack(attacker.entity_id, ability.ability_id)
    return effect


async def mistys_esp(ctx):
    """Flip 3 coins: 1 heads draws; 2 heads deals 20; 3 heads copies an
    attack except Energy costs (Misty's Psyduck — ESP)."""
    results = await ctx.flip_coins(3, ctx.ability.title if ctx.ability else "ESP")
    heads = sum(1 for result in results if result)
    if heads == 1:
        await ctx.draw_cards(1)
    elif heads == 2:
        await ctx.deal_damage(20)
    elif heads == 3:
        await copy_defending_attack(require_energy=False)(ctx)


def mistys_tears_condition(board, player_id, pokemon=None) -> bool:
    return (hand_size_at_least(2)(board, player_id)
            and deck_nonempty(board, player_id))


async def mistys_tears(ctx):
    """Discard 1 other card, then search up to 2 Water Energy into hand."""
    discarded = await ctx.discard_from_hand(
        1, prompt="Discard 1 of the other cards from your hand")
    if len(discarded) < 1:
        return
    await search_to_hand(
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.WATER),
        count=2, minimum=0, reveal=True,
        prompt="Choose up to 2 Water Energy cards to put into your hand.",
    )(ctx)


def mistys_wish_condition(board, player_id, pokemon=None) -> bool:
    prizes = board.find_player_area(player_id, "prizePile")
    return bool(prizes and prizes.children)


async def mistys_wish(ctx):
    """Look at 1 Prize, then ask the opponent to switch it with a hand card.
    If they decline, draw a card (Misty's Wish)."""
    session = ctx.session
    pid = ctx.player_id
    prize_area = ctx.board.find_player_area(pid, "prizePile")
    prizes = list(prize_area.children) if prize_area else []
    if not prizes:
        return
    await ctx.flush_choreography()
    picked_ids = await session._prompt_prize_pick(
        pid, [card.entity_id for card in prizes], 1,
        prompt="Choose a Prize card to look at.",
        prize_area=prize_area,
    )
    prize_card = ctx.board.get_entity(picked_ids[0]) if picked_ids else None
    if prize_card is None:
        return
    viewer = session.players.get(pid)
    if viewer is not None:
        await session.send_game_sequence(
            [viewer], GameSequence.SERIAL_SEQUENCE,
            [session._entity_introduced_msg(prize_card)])
    await session.prompt_view_cards(
        pid, ctx.source.entity_id, [prize_card],
        prompt="Looked-at Prize card",
    )
    if viewer is not None:
        await session.send_game_sequence(
            [viewer], GameSequence.GROUPED_MOVE,
            [session._attributes_reset_msg(prize_card.entity_id)])

    accepted = await ctx.ask_yes_no(
        "Allow your opponent to switch that Prize with a card in their hand?",
        player_id=ctx.opponent_id,
    )
    if not accepted:
        await ctx.draw_cards(1)
        return
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, prompt="Choose a card to switch with the Prize")
    if not picks:
        return
    await ctx.put_in_hand([prize_card], reveal=False)
    await ctx.put_in_prizes(picks)


class ResistanceGymPassive(Passive):
    """Each Pokémon's Resistance is reduced by 20 (-30 becomes -10)."""

    def modify_resistance(self, calc, carrier):
        calc.resistance_reduction = max(0, calc.resistance_reduction - 20)


resistance_gym_passive = ResistanceGymPassive()


# ----------------------------------------------------------------------
# Gym Challenge (GYM2) — Lt. Surge / Misty / Items
# ----------------------------------------------------------------------

def defender_has_type(pokemon_type):
    """cond_fn: the Defending Pokémon currently has this type."""
    type_value = getattr(pokemon_type, "value", pokemon_type)

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and type_value in effective_pokemon_types(
            ctx.board, defender)
    return cond


def _own_named_attack_boosted(ctx, attack_title: str) -> bool:
    attacker = ctx.attacker
    if attacker is None:
        return False
    for mod in ctx.session.turn_state.damage_modifiers:
        if getattr(mod, "source_entity_id", None) != attacker.entity_id:
            continue
        if getattr(mod, "attack_title", None) != attack_title:
            continue
        pred = getattr(mod, "source_predicate", None)
        if pred is not None and not pred(attacker):
            continue
        return True
    return False


def recoil_maybe_doubled(self_damage: int, attack_title: str):
    """Printed damage, then self-damage; Focus Energy doubles both."""
    async def effect(ctx):
        await ctx.deal_damage()
        amount = self_damage * 2 if _own_named_attack_boosted(ctx, attack_title) \
            else self_damage
        if amount > 0:
            await ctx.deal_damage(
                amount, target=ctx.attacker, apply_modifiers=False)
    return effect


async def kerzap(ctx):
    """Heads: +30 and discard all Lightning Energy from self; tails: printed."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Kerzap")
    heads = bool(results and results[0])
    printed = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(printed + (30 if heads else 0))
    if not heads:
        return
    cards = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.LIGHTNING)
    if cards:
        await ctx.discard_cards(cards)


def paralyze_or_recoil(self_damage: int):
    """Printed damage; heads Paralyzes, tails the attacker takes self-damage."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        await ctx.deal_damage()
        if results and results[0]:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
            return
        if self_damage:
            await ctx.deal_damage(
                self_damage, target=ctx.attacker, apply_modifiers=False)
    return effect


def discard_all_self_energy_on_tails():
    """Printed damage; tails discards every Energy card on this Pokémon."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        await ctx.deal_damage()
        if results and not results[0]:
            await ctx.discard_energy_from(
                ctx.attacker, 99,
                prompt="Discard all Energy attached to this Pokémon")
    return effect


async def super_removal(ctx):
    """Heads: discard 1 Energy from each opposing Pokémon that has any."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Super Removal")
    if not results or not results[0]:
        return
    for poked in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(poked):
            continue
        if not ctx.attached_energies(poked):
            continue
        await ctx.discard_energy_from(
            poked, 1,
            prompt="Choose an Energy card to discard")


master_ball = look_at_top(
    7, take=1, predicate=is_pokemon_card, rest="shuffle", minimum=0,
    reveal=True,
    prompt="You may choose a Basic Pokémon or Evolution card.",
)


def max_revive_condition(board, player_id, pokemon=None) -> bool:
    return (
        requires_discard(is_basic_pokemon)(board, player_id)
        and bench_has_room(board, player_id)
        and requires_hand(is_energy_card, n=2)(board, player_id)
    )


async def max_revive(ctx):
    """Discard 2 Energy from hand, then bench 1 Basic from the discard."""
    discarded = await ctx.discard_from_hand(
        2, predicate=is_energy_card,
        prompt="Discard 2 Energy cards from your hand")
    if len(discarded) < 2:
        return
    cards = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your discard pile")
    if picks:
        await ctx.bench_pokemon(picks[0])


_SECRET_PLAN_FACE_DOWN = "_secret_plan_face_down"
_SECRET_PLAN_DUMMY_HP = 40


def _definition_is_basic(card) -> bool:
    """Printed Basic (not the face-down dummy overlay)."""
    definition = def_for(card.archetype_id)
    if definition is None:
        return False
    stage = getattr(definition, "stage", None)
    if stage is not None:
        return getattr(stage, "value", stage) == PokemonStage.BASIC.value
    extras = getattr(definition, "extra_attributes", None) or {}
    spec = extras.get(str(AttrID.STAGE.value)) or extras.get(AttrID.STAGE.value)
    if isinstance(spec, dict):
        return spec.get("value") == PokemonStage.BASIC.value
    return False


def _recast_as_pokemon(board, card) -> PokemonEntity:
    if isinstance(card, PokemonEntity):
        return card
    parent = card.parent
    children = list(card.children)
    pokemon = PokemonEntity(card.card_obj, card.owning_player_id, card.entity_id)
    board._entity_cache[card.entity_id] = pokemon
    if parent is not None:
        try:
            idx = parent.children.index(card)
        except ValueError:
            idx = None
        else:
            parent.children[idx] = pokemon
        pokemon.parent = parent
        pokemon.parent_id = parent.entity_id
    for child in children:
        child.parent = pokemon
        child.parent_id = pokemon.entity_id
        pokemon.children.append(child)
    return pokemon


def _apply_secret_plan_dummy(pokemon) -> None:
    pokemon.set_attribute(_SECRET_PLAN_FACE_DOWN, True)
    pokemon.set_attribute(AttrID.CARD_TYPE, CardType.POKEMON.value)
    pokemon.set_attribute(AttrID.STAGE, PokemonStage.BASIC.value)
    pokemon.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.COLORLESS.value])
    pokemon.set_attribute(AttrID.RETREAT_COST, 0)
    pokemon.set_attribute(AttrID.WEAKNESS_TYPES, [])
    pokemon.set_attribute(AttrID.RESISTANCE_TYPES, None)
    pokemon.set_attribute(AttrID.HP, _SECRET_PLAN_DUMMY_HP)


def _restore_printed_pokemon_stats(pokemon) -> None:
    card_obj = pokemon.card_obj
    hp = pokemon.attribute_originals.get(AttrID.HP.value)
    if hp is None:
        hp = card_obj.get_attribute_value(AttrID.HP, 0)
    pokemon.set_attribute(AttrID.HP, hp)
    for key in (
        AttrID.CARD_TYPE, AttrID.STAGE, AttrID.POKEMON_TYPES,
        AttrID.RETREAT_COST, AttrID.WEAKNESS_TYPES, AttrID.RESISTANCE_TYPES,
    ):
        printed = pokemon.attribute_originals.get(key.value)
        if printed is None:
            printed = card_obj.get_attribute_value(key)
        if printed is not None:
            pokemon.set_attribute(key, printed)


def _secret_plan_attachment(pokemon):
    for child in list(pokemon.children):
        if getattr(def_for(child.archetype_id), "display_name", None) \
                == "Lt. Surge's Secret Plan":
            return child
    return None


async def _flip_secret_plan(ctx, holder) -> None:
    if not holder.get_attribute(_SECRET_PLAN_FACE_DOWN):
        return
    await ctx.reveal_cards([holder])
    holder.set_attribute(_SECRET_PLAN_FACE_DOWN, False)
    if _definition_is_basic(holder):
        max_before = effective_max_hp(ctx.board, holder)
        _restore_printed_pokemon_stats(holder)
        ctx._shift_max_hp(holder, max_before)
        plan = _secret_plan_attachment(holder)
        if plan is not None:
            await ctx.discard_cards([plan])
        await ctx.session.refresh_granted_abilities(holder)
        return
    owner = holder.owning_player_id
    was_active = owner is not None and holder is ctx.board.active_pokemon(owner)
    await ctx.discard_cards(full_stack(holder))
    if was_active and owner is not None:
        _defer_promote(ctx, owner)


async def secret_plan_flip(ctx):
    """Owner may flip the face-down Secret Plan card during their turn."""
    holder = ctx.source
    if holder is None:
        return
    await _flip_secret_plan(ctx, holder)


secret_plan_flip_ability = Ability(
    title="Flip",
    game_text="At any time during your turn, you may flip this card over. "
              "When you flip that card over, if it isn't a Basic Pokémon, "
              "discard it and all cards attached to it.",
    ability_type=AbilityTypes.POKE_POWER,
    activation=Activations.UNLIMITED,
    effect=secret_plan_flip,
)
secret_plan_flip_ability.ability_id = ability_id_for(
    "gym2-lt-surges-secret-plan-flip", 0)
secret_plan_flip_ability.is_granted = True
ABILITIES_BY_ID[secret_plan_flip_ability.ability_id] = secret_plan_flip_ability
secret_plan_granted_abilities = [secret_plan_flip_ability]


class SecretPlanPassive(Passive):
    """Face-down dummy: hide printed attacks, flip before attack damage."""

    def hides_printed_attacks(self, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return pokemon is holder and bool(
            holder.get_attribute(_SECRET_PLAN_FACE_DOWN))

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not target:
            return None
        if not holder.get_attribute(_SECRET_PLAN_FACE_DOWN):
            return None
        if not calc.is_attack or calc.amount <= 0:
            return None
        entity_id = holder.entity_id
        await _flip_secret_plan(ctx, holder)
        revealed = ctx.board.get_entity(entity_id)
        if revealed is None:
            return 0
        was = getattr(ctx, "_in_interceptor", False)
        try:
            ctx._in_interceptor = False
            await ctx.deal_damage(calc.base, target=revealed)
        finally:
            ctx._in_interceptor = was
        return 0


secret_plan_passive = SecretPlanPassive()


def lt_surges_secret_plan_condition(board, player_id, pokemon=None) -> bool:
    return (bench_has_room(board, player_id)
            and hand_size_at_least(2)(board, player_id))


async def lt_surges_secret_plan(ctx):
    """Put 1 card from hand face down onto the Bench as a Basic Pokémon."""
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card to put face down onto your Bench")
    if not picks:
        return
    dummy = _recast_as_pokemon(ctx.board, picks[0])
    _apply_secret_plan_dummy(dummy)
    if not await ctx.bench_pokemon(dummy):
        return
    await ctx.attach_energy(ctx.source, dummy)
    await ctx.session.refresh_granted_abilities(dummy)


# ----------------------------------------------------------------------
# Neo Genesis (NEO1)
# ----------------------------------------------------------------------

async def pilfer(ctx):
    """Shuffle this Pokémon and attachments into the deck. Heads: shuffle
    1 card from the discard pile into the deck (Aipom — Pilfer)."""
    pokemon = ctx.attacker
    if pokemon is not None:
        await ctx.shuffle_into_deck(full_stack(pokemon), ctx.player_id)
        _defer_promote(ctx, ctx.player_id)
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Pilfer")
    if not results or not results[0]:
        return
    pile = list(ctx.discard_pile())
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, minimum=1,
        prompt="Choose a card to shuffle into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks)


def flip_paralyze_and_bench(bench_damage: int = 10):
    """Printed damage; heads, Paralyze the Defending Pokémon and deal
    `bench_damage` to each of the opponent's Benched Pokémon (no W/R).
    Ampharos — Gigaspark / Azumarill — Bubble Shower."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        heads = bool(results and results[0])
        await ctx.deal_damage()
        if not heads:
            return
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
        for poked in ctx.opponent_bench():
            await ctx.deal_damage(bench_damage, target=poked)
    return effect


async def arcade_game(ctx):
    """Shuffle, reveal the top 3. If 2+ share a name, put those into hand
    and shuffle the rest; otherwise shuffle all 3 back (Arcade Game)."""
    await ctx.shuffle_deck()
    top = ctx.deck_top(3)
    if not top:
        return
    await ctx.reveal_cards(top)
    names = [
        getattr(def_for(card.archetype_id), "display_name", None) or ""
        for card in top
    ]
    match_name = next((name for name in names if names.count(name) >= 2), None)
    if match_name is None:
        await ctx.shuffle_deck()
        return
    takes = [card for card, name in zip(top, names) if name == match_name]
    await ctx.put_in_hand(takes, reveal=True)
    await ctx.shuffle_deck()


async def spider_web(ctx):
    """Heads: the Defending Pokémon can't retreat until it leaves Active
    (Ariados — Spider Web)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Spider Web")
    if not results or not results[0]:
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.lock_retreat(defender, LOCK_UNTIL_LEAVES_ACTIVE)


def poison_bite_attack(always_poison=False):
    """If this attack damages the Defending Pokémon, Poison it and heal the
    attacker for half that damage, rounded up to the nearest 10
    (Ariados — Poison Bite). always_poison=True also Poisons on a 0-damage
    hit (Golbat — Poison Bite's "either way" clause)."""
    async def effect(ctx):
        dealt = await ctx.deal_damage()
        if ctx.defender is not None and (dealt > 0 or always_poison):
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.POISONED)
        if dealt > 0 and ctx.attacker is not None:
            heal = ((dealt + 19) // 20) * 10
            if heal > 0:
                await ctx.heal(heal, ctx.attacker)
    return effect


poison_bite = poison_bite_attack()


async def hyper_reverse(ctx):
    """10× Energy cards on the Defending Pokémon; heal the attacker for the
    damage actually dealt after Weakness and Resistance (Butterfree)."""
    n = count_energy("defender", cards=True)(ctx)
    dealt = await ctx.deal_damage(10 * n) if n else 0
    if dealt > 0 and ctx.attacker is not None:
        await ctx.heal(dealt, ctx.attacker)


async def sweet_scent(ctx):
    """Heads: heal 20 from 1 of your damaged Pokémon. Tails: the same for
    1 of your opponent's (Bayleef — Sweet Scent)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Sweet Scent")
    heads = bool(results and results[0])
    pool = ctx.my_pokemon_in_play() if heads else ctx.opponent_pokemon_in_play()
    damaged = [poked for poked in pool if _is_damaged(ctx.board, poked)]
    if not damaged:
        return
    whose = "your" if heads else "your opponent's"
    target = await ctx.choose_pokemon(
        damaged, f"Choose {whose} Pokémon to heal")
    if target is not None:
        await ctx.heal(20, target)


def flip_heal_one(amount: Optional[int] = None, all_damage: bool = False):
    """Heads: heal `amount` (or all damage) from 1 of your damaged Pokémon
    (Bellossom — Sweet Nectar)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        damaged = [poked for poked in ctx.my_pokemon_in_play()
                   if _is_damaged(ctx.board, poked)]
        if not damaged:
            return
        target = await ctx.choose_pokemon(
            damaged, "Choose a Pokémon to heal")
        if target is None:
            return
        heal = (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
                ) if all_damage else (amount or 0)
        if heal > 0:
            await ctx.heal(heal, target)
    return effect


def neo_berry_heal(amount: int = 20):
    """Between turns: if the holder has at least `amount` damage, heal that
    much and discard this tool (Berry / Gold Berry)."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        damage = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if damage < amount:
            return
        await ctx.heal(amount, target=pokemon)
        tool = next((t for t, p in ctx.tools_in_play() if p is pokemon), None)
        if tool is not None:
            await ctx.discard_cards([tool])
    return effect


async def herbal_scent(ctx):
    """When played from hand: you may flip — heads, heal all Grass Pokémon
    in play (Meganium — Herbal Scent)."""
    grass = [
        poked for poked in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        if pokemon_has_type(poked, PokemonTypes.GRASS) and _is_damaged(ctx.board, poked)
    ]
    if not grass:
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no(
            "Flip a coin? If heads, remove all damage counters from all "
            "Grass Pokémon in play."):
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Herbal Scent")
    if not results or not results[0]:
        return
    for poked in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if not pokemon_has_type(poked, PokemonTypes.GRASS):
            continue
        damage = ctx.max_hp(poked) - poked.get_attribute(AttrID.HP, 0)
        if damage > 0:
            await ctx.heal(damage, poked)


class WildGrowthPassive(Passive):
    """Grass Energy cards on your Grass Pokémon provide GrassGrass. Stops
    while Meganium is Asleep, Confused, or Paralyzed (Meganium — Wild Growth)."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or not _typed_basic_energy(energy, PokemonTypes.GRASS):
            return options
        if not pokemon_has_type(holder, PokemonTypes.GRASS):
            return options
        owner = holder.owning_player_id
        if not any(
            isinstance(passive, WildGrowthPassive)
            and not _asleep_confused_or_paralyzed(
                carrier_pokemon(carrier) or carrier)
            and (carrier_pokemon(carrier) or carrier).owning_player_id == owner
            for passive, carrier in _active_passives(board)
        ):
            return options
        grass = PokemonTypes.GRASS.value
        return [[grass, grass]]


wild_growth = WildGrowthPassive()


def flip_heal(coins: int, per_heads: int, target="self"):
    """Flip `coins`; heal `per_heads` per heads from this Pokémon (`self`)
    or a chosen in-play Pokémon (`choice`) (Miltank — Milk Drink /
    Moo-Moo Milk)."""
    async def effect(ctx):
        if target == "choice":
            pool = ctx.my_pokemon_in_play()
            if not pool:
                return
            poked = await ctx.choose_pokemon(pool, "Choose a Pokémon to heal")
            if poked is None:
                return
        else:
            poked = ctx.attacker if ctx.attacker is not None else ctx.source
        if poked is None:
            return
        title = ctx.ability.title if ctx.ability else (
            getattr(def_for(getattr(ctx.source, "archetype_id", None) or ""),
                    "display_name", None) or "")
        results = await ctx.flip_coins(coins, title)
        heads = sum(1 for result in results if result)
        if heads:
            await ctx.heal(per_heads * heads, poked)
    return effect


milk_drink = flip_heal(2, 20)
neo_moomoo_milk = flip_heal(2, 20, target="choice")


class MeanLookPassive(Passive):
    """The locked Defending Pokémon can't retreat while the carrier remains
    Active (Murkrow — Mean Look)."""

    def __init__(self, target_id: str):
        self.target_id = target_id

    def blocks_retreat(self, pokemon, carrier):
        if pokemon.entity_id != self.target_id:
            return False
        return is_in_active_spot(carrier) and is_in_active_spot(pokemon)


async def mean_look(ctx):
    """The Defending Pokémon can't retreat as long as this Pokémon remains
    Active; benching or evolving either Pokémon ends it."""
    defender = ctx.defender
    attacker = ctx.attacker
    if defender is None or attacker is None or ctx.effects_blocked(defender):
        return
    ctx.add_temporary_passive(attacker, MeanLookPassive(defender.entity_id))


async def miracle_berry_checkup(ctx):
    """BETWEEN_TURNS: if the holder has a Special Condition, cure them all
    and discard Miracle Berry."""
    pokemon = ctx.source
    if pokemon is None:
        return
    if not (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        return
    await ctx.cure_all_conditions(pokemon)
    tool = next((t for t, p in ctx.tools_in_play() if p is pokemon), None)
    if tool is not None:
        await ctx.discard_cards([tool])


def mary_playable(board, player_id, pokemon=None) -> bool:
    """After playing Mary, drawing 2 must leave 2 cards to shuffle back."""
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    hand_n = len(hand.children) if hand else 0
    deck_n = len(deck.children) if deck else 0
    return (hand_n - 1) + min(2, deck_n) >= 2


async def mary(ctx):
    """Draw 2, then shuffle 2 cards from your hand into your deck."""
    await ctx.draw_cards(2)
    hand = list(ctx.hand())
    take = min(2, len(hand))
    if take <= 0:
        return
    picks = await ctx.choose_cards(
        hand, take, minimum=take,
        prompt="Shuffle 2 cards from your hand into your deck.")
    if picks:
        await ctx.shuffle_into_deck(picks)


async def new_pokedex(ctx):
    """Shuffle your deck, then rearrange the top 5 (New Pokédex)."""
    await ctx.shuffle_deck()
    await ctx.reorder_deck_top(5)


async def glaring_gaze(ctx):
    """Heads: look at the opponent's hand and shuffle 1 Trainer into their
    deck (Noctowl — Glaring Gaze)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Glaring Gaze")
    if not results or not results[0]:
        return
    await rockets_sneak_attack(ctx)


async def floodlight(ctx):
    """20, plus optional unused-Water bonus from Hydroelectric Power; heads,
    Paralyze (Lanturn — Floodlight)."""
    extra = 0
    attacker = ctx.attacker
    if (attacker is not None
            and not _asleep_confused_or_paralyzed(attacker)
            and not ability_locked(ctx.board, attacker)):
        total = count_energy("self", energy_type=PokemonTypes.WATER)(ctx)
        cost = (ctx.ability.cost or {}) if ctx.ability else {}
        cost_water = sum(
            n for key, n in cost.items()
            if getattr(key, "value", key) == PokemonTypes.WATER.value
        )
        unused = max(0, total - cost_water)
        if unused > 0 and await ctx.ask_yes_no(
                "Use Hydroelectric Power to do 10 more damage for each "
                "unused Water Energy?"):
            extra = 10 * unused
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + extra)
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Floodlight")
    if results and results[0]:
        await ctx.apply_special_condition(
            ctx.defender, SpecialConditions.PARALYZED)


async def baton_pass(ctx):
    """Printed damage; move all Grass Energy onto a benched Grass Pokémon
    and switch with it (Ledian — Baton Pass)."""
    await ctx.deal_damage()
    grass = PokemonTypes.GRASS.value
    bench = [
        poked for poked in ctx.my_bench()
        if grass in effective_pokemon_types(ctx.board, poked)
    ]
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Grass Pokémon to attach Ledian's Grass Energy to")
    if target is None:
        return
    for energy in list(ctx.attached_energies(ctx.attacker)):
        if _typed_basic_energy(energy, PokemonTypes.GRASS):
            await ctx.move_energy(energy, target)
    await ctx.switch_active(ctx.player_id, target)


_ELEMENTAL_BLAST_TYPES = (
    PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING,
)

elemental_blast_condition = all_conditions(
    *(has_typed_basic_energy(t) for t in _ELEMENTAL_BLAST_TYPES)
)


async def elemental_blast(ctx):
    """Printed damage; discard 1 Fire, 1 Water, and 1 Lightning Energy card
    (Lugia — Elemental Blast)."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    if attacker is None:
        return
    for energy_type in _ELEMENTAL_BLAST_TYPES:
        type_name = CLIENT_POKEMON_TYPE_NAMES.get(energy_type, "Energy")
        await ctx.discard_energy_from(
            attacker, 1,
            predicate=lambda c, t=energy_type: _typed_basic_energy(c, t),
            prompt=f"Choose a {type_name} Energy card to discard from Lugia",
        )


async def sputter(ctx):
    """Printed damage; all Pokémon Powers stop working until the end of your
    next turn (Magby — Sputter)."""
    await ctx.deal_damage()
    ctx.add_passive_through_own_next_turn(
        ctx.board.playmat,
        ability_lock_passive(lambda pokemon, carrier: True),
    )


async def static_electricity(ctx):
    """For each Mareep in play, you may search for a Lightning Energy card
    and attach it to this Pokémon (Mareep — Static Electricity)."""
    n = sum(
        1 for poked in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        if getattr(def_for(poked.archetype_id), "display_name", None) == "Mareep"
    )
    await search_attach_energy(
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.LIGHTNING),
        count=n,
        to_self=True,
        prompt="Choose Lightning Energy cards to attach to Mareep.",
    )(ctx)


# ----------------------------------------------------------------------
# Neo Genesis — Donphan / Double Gust / Ecogym / Elekid / Energy Charge /
# Feraligatr / Focus Band / Sprout Tower
# ----------------------------------------------------------------------

async def rapid_spin(ctx):
    """Printed damage, then each player switches (opponent first) — Donphan."""
    await ctx.deal_damage()
    await escape_rope(ctx)


async def spikes(ctx):
    """During the opponent's turn, 10 to their Pokémon that just became
    Active (no W/R). Stops while Asleep, Confused, or Paralyzed
    (Forretress — Spikes)."""
    holder = ctx.source
    moved = getattr(ctx, "moved_to_active", None)
    if (holder is None or moved is None
            or moved.owning_player_id == holder.owning_player_id
            or ctx.session.turn_state.active_player_id == holder.owning_player_id
            or _asleep_confused_or_paralyzed(holder)):
        ctx.suppress_announce = True
        return
    await ctx.deal_damage(10, target=moved, apply_modifiers=False)


async def double_gust(ctx):
    """Opponent switches your Active (they choose), then you switch theirs."""
    my_bench = ctx.my_bench()
    if my_bench:
        target = await ctx.choose_pokemon(
            my_bench, "Choose your new Active Pokémon",
            player_id=ctx.opponent_id,
        )
        await ctx.switch_active(ctx.player_id, target or my_bench[0])
        await ctx.flush_choreography()
    opp_bench = ctx.opponent_bench()
    if opp_bench:
        target = await ctx.choose_pokemon(
            opp_bench, "Choose the opponent's new Active Pokémon")
        await ctx.switch_active(ctx.opponent_id, target or opp_bench[0])


class EcogymPassive(Passive):
    """Non-Colorless Energy discarded from another player's Pokémon returns
    to its owner's hand. Knock Out discards never consult this hook."""

    def energy_discard_destination(self, energy, mover_player_id, source, carrier):
        if not isinstance(source, PokemonEntity):
            return None
        owner = energy.owning_player_id
        if owner is None or owner == mover_player_id:
            return None
        if not is_energy_card(energy):
            return None
        types = energy.get_attribute(AttrID.POKEMON_TYPES) or []
        if not any(t != PokemonTypes.COLORLESS.value for t in types):
            return None
        return "hand"


ecogym_passive = EcogymPassive()


sprout_tower_passive = takes_less_passive(
    30,
    protects=lambda target, carrier: True,
    attacker_pred=lambda attacker: pokemon_has_type(
        attacker, PokemonTypes.COLORLESS),
)


async def playful_punch(ctx):
    """Flip: heads deals 20 with W/R. Either way, this ends your turn."""
    results = await ctx.flip_coins(1, "Playful Punch")
    if results and results[0]:
        await ctx.deal_damage(20)
    ctx.ends_turn = True


async def energy_charge_item(ctx):
    """Flip a coin. If heads, shuffle up to 2 Energy cards from discard
    into the deck (Energy Charge)."""
    results = await ctx.flip_coins(1, "Energy Charge")
    if not results or not results[0]:
        return
    await recover_from_discard(
        is_energy_card, count=2, minimum=1, to="deck_shuffle",
        prompt="Choose up to 2 Energy cards to shuffle into your deck",
    )(ctx)


async def berserk(ctx):
    """Flip: mill 5 from the opponent's deck on heads, yours on tails."""
    results = await ctx.flip_coins(1, "Berserk")
    if not results:
        return
    pid = ctx.opponent_id if results[0] else ctx.player_id
    await ctx.discard_cards(ctx.deck_top(5, player_id=pid))


def downpour_condition(board, player_id, pokemon=None) -> bool:
    """Water Energy in hand; no Special Conditions (Feraligatr — Downpour)."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and any(
        _typed_basic_energy(c, PokemonTypes.WATER) for c in hand.children))


async def downpour(ctx):
    """Discard 1 Water Energy card from hand."""
    await ctx.discard_from_hand(
        1, predicate=lambda c: _typed_basic_energy(c, PokemonTypes.WATER),
        prompt="Discard a Water Energy card from your hand")


async def riptide(ctx):
    """10 + 10 per Water Energy card in discard, then shuffle those back."""
    waters = [
        c for c in ctx.discard_pile()
        if _typed_basic_energy(c, PokemonTypes.WATER)
    ]
    await ctx.deal_damage(10 + 10 * len(waters))
    if waters:
        await ctx.shuffle_into_deck(waters)


class FocusBandPassive(GutsSurvivePassive):
    """Survive a KO at 10 HP on heads, then discard this tool."""

    def __init__(self):
        super().__init__(hp_floor=10, title="Focus Band", flip=True)

    async def damage_interceptor(self, ctx, calc, target, carrier):
        result = await super().damage_interceptor(ctx, calc, target, carrier)
        if result is not None:
            await ctx.discard_cards([carrier])
        return result


focus_band_passive = FocusBandPassive()


_PRIZE_FACE_UP = "_prize_face_up"
_CARD_FLIP_GUESSES = ["Energy card", "Trainer card", "Pokémon card"]


def _prize_is_face_down(card) -> bool:
    if card.get_attribute(_PRIZE_FACE_UP):
        return False
    root = card
    while getattr(root, "parent", None) is not None:
        root = root.parent
    return not getattr(root, "prizes_face_up", False)


def card_flip_game_condition(board, player_id, pokemon=None) -> bool:
    """Opponent has at least one face-down Prize (Card-Flip Game)."""
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return False
    area = board.find_player_area(opponent, "prizePile")
    return any(_prize_is_face_down(card) for card in (area.children if area else []))


async def card_flip_game(ctx):
    """Guess a face-down Prize's type, leave it face up, draw 2 if correct."""
    prize_area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
    prizes = [card for card in (prize_area.children if prize_area else [])
              if _prize_is_face_down(card)]
    if not prizes:
        return
    await ctx.flush_choreography()
    picked_ids = await ctx.session._prompt_prize_pick(
        ctx.player_id, [card.entity_id for card in prizes], 1,
        prompt="Choose 1 of your opponent's face-down Prize cards.",
        prize_area=prize_area,
    )
    prize = ctx.board.get_entity(picked_ids[0]) if picked_ids else None
    if prize is None:
        return
    guess = await ctx.choose(
        "Guess whether that Prize is an Energy card, a Trainer card, "
        "or a Pokémon card.",
        _CARD_FLIP_GUESSES,
    )
    await ctx.reveal_cards([prize])
    prize.set_attribute(_PRIZE_FACE_UP, True)
    if guess == 0:
        correct = is_energy_card(prize)
    elif guess == 1:
        correct = is_trainer_card(prize)
    else:
        correct = is_pokemon_card(prize)
    if correct:
        await ctx.draw_cards(2)


async def squaredance(ctx):
    """Flip 1 coin per Pokémon in play; for each heads, you may search a
    basic Energy into hand (Clefairy — Squaredance)."""
    n = len(ctx.my_pokemon_in_play()) + len(ctx.opponent_pokemon_in_play())
    results = await ctx.flip_coins(
        n, ctx.ability.title if ctx.ability else "Squaredance") if n else []
    heads = sum(1 for result in results if result)
    if heads <= 0:
        return
    picks = await ctx.search_deck(
        is_basic_energy_card, count=heads, minimum=0,
        prompt="Choose basic Energy cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


class JawClampPassive(Passive):
    """While this Pokémon is Active, the opponent's Active can't retreat
    and can't be switched by attack, Power, or Trainer effects."""

    def _traps(self, pokemon, carrier) -> bool:
        holder = carrier_pokemon(carrier) or carrier
        return is_in_active_spot(holder) and opposing_active(pokemon, holder)

    def blocks_retreat(self, pokemon, carrier):
        return self._traps(pokemon, carrier)

    def blocks_switch(self, pokemon, carrier):
        return self._traps(pokemon, carrier)


async def jaw_clamp(ctx):
    """Printed damage; until the end of the opponent's next turn, as long
    as this Pokémon is Active, the Defending Pokémon can't retreat or be
    switched by effects (Croconaw — Jaw Clamp)."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    defender = ctx.defender
    if attacker is None or defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(attacker, JawClampPassive())


def sticky_nectar(bonus: int = 10):
    """Flip; heads: printed + bonus and Jaw Clamp until the end of your
    next turn. Tails: printed damage only (Gloom — Sticky Nectar)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        heads = bool(results and results[0])
        printed = getattr(ctx.ability, "damage", 0) or 0
        amount = printed + (bonus if heads else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if not heads:
            return
        attacker = ctx.attacker
        defender = ctx.defender
        if attacker is None or defender is None or ctx.effects_blocked(defender):
            return
        ctx.add_passive_through_own_next_turn(attacker, JawClampPassive())
    return effect


def remaining_hp_at_most(hp: int):
    """Ability gate: this Pokémon's remaining HP is `hp` or less."""
    def check(board, player_id, pokemon=None) -> bool:
        return pokemon is not None and pokemon.get_attribute(AttrID.HP, 0) <= hp
    return check


def boost_named_attack_this_turn(title: str, amount: int):
    """This Pokémon's attack named `title` does +amount this turn
    (Heracross — Final Blow: Megahorn 60 → 120)."""
    async def effect(ctx):
        holder = ctx.source
        if holder is None:
            return
        ctx.add_turn_damage_modifier(TurnDamageModifier(
            amount, ctx.player_id,
            source_entity_id=holder.entity_id,
            attack_title=title,
        ))
    return effect


def took_damage_last_turn(ctx) -> bool:
    """cond_fn: this Pokémon took opposing damage last turn (Horsea — Fin Slap)."""
    attacker = ctx.attacker
    return attacker is not None and ctx.damage_taken_last_turn(attacker) > 0


async def flip_tails_discard_energy(ctx):
    """Printed damage; tails discards 1 Energy card attached to the attacker
    (Cyndaquil — Fireworks)."""
    await ctx.deal_damage()
    title = ctx.ability.title if ctx.ability else ""
    results = await ctx.flip_coins(1, title)
    if not results or results[0]:
        return
    if ctx.attacker is not None:
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Choose an Energy card to discard")


def fire_recharge_condition(board, player_id, pokemon=None) -> bool:
    """Fire Energy in discard; no Special Conditions (Typhlosion — Fire Recharge)."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    discard = board.find_player_area(player_id, "discard")
    return any(_typed_basic_energy(c, PokemonTypes.FIRE)
               for c in (discard.children if discard else []))


async def fire_recharge(ctx):
    """Flip; heads, attach a Fire Energy from discard to 1 of your Fire Pokémon."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Fire Recharge")
    if not results or not results[0]:
        return
    pool = [c for c in ctx.discard_pile()
            if _typed_basic_energy(c, PokemonTypes.FIRE)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=1,
        prompt="Choose a Fire Energy card from your discard pile to attach")
    if not picks:
        return
    fire_pokemon = [poked for poked in ctx.my_pokemon_in_play()
                    if pokemon_has_type(poked, PokemonTypes.FIRE)]
    if not fire_pokemon:
        return
    target = fire_pokemon[0] if len(fire_pokemon) == 1 else await ctx.choose_pokemon(
        fire_pokemon, "Choose a Fire Pokémon to attach the Energy to")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


async def fire_boost(ctx):
    """ON_EVOLVE: you may flip — heads, attach up to 4 Fire Energy from deck
    (Typhlosion — Fire Boost)."""
    if not ctx.deck():
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no(
            "Flip a coin? If heads, search your deck for up to 4 Fire Energy "
            "cards and attach them to Typhlosion."):
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Fire Boost")
    if not results or not results[0]:
        return
    await search_attach_energy(
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        count=4,
        to_self=True,
        prompt="Choose up to 4 Fire Energy cards to attach to Typhlosion.",
    )(ctx)


async def flame_burst(ctx):
    """60; heads, +20 and 20 damage to this Pokémon (Typhlosion — Flame Burst)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Flame Burst")
    extra = 20 if results and results[0] else 0
    printed = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(printed + extra)
    if extra:
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)


# ----------------------------------------------------------------------
# Neo Genesis — Super Energy Retrieval / Super Rod / Time Capsule
# ----------------------------------------------------------------------

super_energy_retrieval_condition = all_conditions(
    requires_hand(n=2),
    requires_discard(is_basic_energy_card),
)


async def super_energy_retrieval(ctx):
    """Discard 2 other cards from hand; put 4 basic Energy from discard
    into hand (all of them if fewer than 4)."""
    discarded = await ctx.discard_from_hand(
        2, prompt="Choose 2 other cards in your hand to discard")
    if len(discarded) < 2:
        return
    discarded_ids = {card.entity_id for card in discarded}
    pool = [
        card for card in ctx.discard_pile()
        if is_basic_energy_card(card) and card.entity_id not in discarded_ids
    ]
    if not pool:
        return
    if len(pool) <= 4:
        picks = pool
    else:
        picks = await ctx.choose_cards(
            pool, 4, minimum=4,
            prompt="Choose 4 basic Energy cards from your discard pile")
    if picks:
        await ctx.put_in_hand(picks)


super_rod_condition = requires_discard(is_pokemon_card)


async def super_rod(ctx):
    """Heads: an Evolution from discard into hand. Tails: a Basic Pokémon."""
    results = await ctx.flip_coins(1, "Super Rod")
    if not results:
        return
    heads = results[0]
    pred = is_evolution_pokemon if heads else is_basic_pokemon
    kind = "an Evolution card" if heads else "a Basic Pokémon card"
    cards = [card for card in ctx.discard_pile() if pred(card)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt=f"Choose {kind} to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


async def _time_capsule_shuffle(ctx, player_id):
    """May shuffle 5 matching discard cards into deck, or all/none if fewer."""
    cards = [card for card in ctx.discard_pile(player_id) if is_garbage_run_card(card)]
    if not cards:
        return
    if len(cards) >= 5:
        if not await ctx.ask_yes_no(
            "Shuffle 5 Basic Pokémon, Evolution, and/or basic Energy cards "
            "from your discard pile into your deck?",
            player_id=player_id,
        ):
            return
        picks = await ctx.choose_cards(
            cards, 5, player_id=player_id,
            prompt="Choose 5 cards to shuffle into your deck",
        )
    else:
        if not await ctx.ask_yes_no(
            "Shuffle all Basic Pokémon, Evolution, and/or basic Energy cards "
            "from your discard pile into your deck?",
            player_id=player_id,
        ):
            return
        picks = list(cards)
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks, player_id)


async def time_capsule(ctx):
    """Opponent may recycle 5 (or all/none) Basic/Evolution/basic Energy
    from discard; then you may. No more Trainer cards this turn."""
    await _time_capsule_shuffle(ctx, ctx.opponent_id)
    await _time_capsule_shuffle(ctx, ctx.player_id)
    ctx.lock_plays(
        ctx.player_id, is_trainer_card,
        through_turn=ctx.session.turn_state.turn_number,
    )


# ----------------------------------------------------------------------
# Neo Discovery (NEO2)
# ----------------------------------------------------------------------

collect_fire = attach_from_discard(
    predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
    prompt="Choose a Fire Energy card from your discard pile to attach",
)


def _has_poke_power(pokemon) -> bool:
    abilities = pokemon.get_attribute(AttrID.PIE_ABILITIES) or []
    return any(isinstance(entry, dict) and entry.get("abilityType") == "PokePower"
               for entry in abilities)


def gaze_condition(board, player_id, pokemon=None) -> bool:
    """Igglybuff — Gaze: a Benched opposing Pokémon has a Pokémon Power."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    if not opponent:
        return False
    bench = board.find_player_area(opponent, "bench")
    return any(
        isinstance(poked, PokemonEntity) and _has_poke_power(poked)
        for poked in (bench.children if bench else [])
    )


async def gaze(ctx):
    """Until the end of this turn, one opposing Benched Pokémon Power is
    off. The lock ends if that Pokémon leaves the Bench."""
    bench = [poked for poked in ctx.opponent_bench() if _has_poke_power(poked)]
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench,
        "Choose 1 of your opponent's Benched Pokémon that has a Pokémon Power",
    )
    if target is None:
        return
    ctx.add_temporary_passive(
        target,
        ability_lock_passive(
            lambda pokemon, carrier: (
                pokemon is carrier and not is_in_active_spot(pokemon)
            )
        ),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


class SecretePoisonPassive(Passive):
    """If an attack damages this Pokémon (even if Knocked Out), Poison the
    opponent's Active and deal 10 to each of their Benched Pokémon."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder:
            return None
        attacker = calc.attacker
        if attacker is None:
            return None
        owner = attacker.owning_player_id
        active = ctx.board.active_pokemon(owner) or attacker
        await ctx.apply_special_condition(active, SpecialConditions.POISONED)
        bench = ctx.board.find_player_area(owner, "bench")
        for poked in list(bench.children if bench else []):
            if isinstance(poked, PokemonEntity):
                await ctx.deal_damage(
                    10, target=poked, apply_modifiers=False, is_attack=False)
        return None


async def secrete_poison(ctx):
    """During the opponent's next turn, a hit on this Pokémon Poisons their
    Active and spreads 10 to their Bench (Kakuna — Secrete Poison)."""
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, SecretePoisonPassive())


def revive_friends_condition(board, player_id, pokemon=None) -> bool:
    """Kabuto — Revive Friends: no Special Conditions, deck and Bench room."""
    if not no_special_conditions(board, player_id, pokemon):
        return False
    return has_cards_in_deck(board, player_id, pokemon) and bench_has_room(
        board, player_id)


async def _treat_benched_as_basic(ctx, benched):
    for card in benched:
        card.set_attribute(AttrID.STAGE, PokemonStage.BASIC.value)


async def revive_friends(ctx):
    """Flip; heads, search for Kabuto, bench it as a Basic, then shuffle."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Revive Friends")
    if not results or not results[0]:
        return
    await search_to_bench(
        lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Kabuto",
        prompt="Choose a card named Kabuto.",
        then=_treat_benched_as_basic,
    )(ctx)


_NEO_FOSSIL_LINE = frozenset(("Omanyte", "Omastar", "Kabuto", "Kabutops"))


def _neo_fossil_line_on_bench(ctx) -> int:
    return sum(
        1 for poked in ctx.my_bench()
        if poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _NEO_FOSSIL_LINE
    )


async def work_together(ctx):
    """10; heads, +10 for each Omanyte, Omastar, Kabuto, and Kabutops on
    the Bench (Kabuto — Work Together)."""
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Work Together")
    amount = 10
    if results and results[0]:
        amount += 10 * _neo_fossil_line_on_bench(ctx)
    await ctx.deal_damage(amount)


def _hydrocutter_coins(ctx) -> int:
    return min(3, count_energy("self", cards=True)(ctx))


hydrocutter = flip_damage(per_heads=40, coins_from=_hydrocutter_coins)


class LockOnPassive(Passive):
    """During your next turn, Electric Bolt treats tails as heads.
    Benching or evolving either Pokémon ends this effect."""

    def __init__(self, defender_id: str, start_turn: int):
        self.defender_id = defender_id
        self.start_turn = start_turn


def _lock_on_active(ctx) -> bool:
    attacker = ctx.attacker
    defender = ctx.defender
    if attacker is None or not is_in_active_spot(attacker):
        return False
    turn = ctx.session.turn_state.turn_number
    for temp in getattr(ctx.board, "temporary_passives", None) or []:
        if temp.carrier_entity_id != attacker.entity_id:
            continue
        passive = temp.passive
        if not isinstance(passive, LockOnPassive):
            continue
        if turn <= passive.start_turn:
            continue
        if defender is None or defender.entity_id != passive.defender_id:
            continue
        if not is_in_active_spot(defender):
            continue
        return True
    return False


async def lock_on(ctx):
    """Mark this Magnemite and the Defending Pokémon for Electric Bolt
    next turn (Lock-on)."""
    attacker = ctx.attacker
    defender = ctx.defender
    if attacker is None or defender is None:
        return
    ctx.add_passive_through_own_next_turn(
        attacker,
        LockOnPassive(defender.entity_id, ctx.session.turn_state.turn_number),
    )


async def electric_bolt(ctx):
    """Flip 2 coins. Both heads: 50 and Paralyze. Any tails: nothing.
    Lock-on treats tails as heads."""
    results = await ctx.flip_coins(
        2, ctx.ability.title if ctx.ability else "Electric Bolt")
    if _lock_on_active(ctx):
        results = [True] * len(results)
    if not results or not all(results):
        return
    await ctx.deal_damage()
    await ctx.apply_special_condition(
        ctx.defender, SpecialConditions.PARALYZED)


async def hyper_devolution_spray(ctx):
    """Put the highest Stage Evolution card of 1 of your evolved Pokémon
    into your hand. That Pokémon can't evolve this turn."""
    evolved = devolution_spray_targets(ctx.board, ctx.player_id)
    if not evolved:
        return
    target = await ctx.choose_play_target(
        evolved, "Choose an evolved Pokémon")
    if target is None:
        return
    underlays = _evolution_underlays(target)
    remaining = underlays[0] if underlays else None
    await ctx.devolve_pokemon(target, steps=1, destination="hand")
    if remaining is not None:
        ctx.session.turn_state.mark_entered_play(remaining.entity_id)


# ----------------------------------------------------------------------
# Neo Discovery (NEO2)
# ----------------------------------------------------------------------

_POLI_LINE = frozenset(("Poliwag", "Poliwhirl", "Poliwrath", "Politoed"))


def evolves_from_mysterious_fossil(card) -> bool:
    """Omanyte / Kabuto / Aerodactyl (and reprints) — direct Fossil evolutions."""
    return (is_pokemon_card(card)
            and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == "MysteriousFossil")


def revive_fossil_condition(board, player_id, pokemon=None) -> bool:
    """Deck nonempty, Bench not full, and not Asleep/Confused/Paralyzed
    (Omanyte — Revive Fossil)."""
    return (no_special_conditions(board, player_id, pokemon)
            and bench_has_room(board, player_id)
            and has_cards_in_deck(board, player_id, pokemon))


revive_fossil = flip_or_nothing(then=search_to_bench(
    predicate=evolves_from_mysterious_fossil,
    prompt="Choose a card that evolves from Mysterious Fossil "
           "to put onto your Bench.",
))


async def _hatch_heads(ctx):
    pokemon = ctx.attacker
    if pokemon is not None:
        heal_amount = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if heal_amount > 0:
            await ctx.heal(heal_amount, pokemon)
    await search_evolve_self(ctx)


hatch = flip_or_nothing(then=_hatch_heads)


async def _pineco_burst_hit(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Burst")
    if not results or not results[0]:
        return
    for poked in ctx.my_bench() + ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)
    await ctx.deal_damage(40, target=ctx.attacker, apply_modifiers=False)


pineco_burst = flip_or_nothing(then=_pineco_burst_hit)


def _is_poli_line(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return any(fragment in name for fragment in _POLI_LINE)


class FrogSongPassive(Passive):
    """If more than 3 Poliwag-line Pokémon are in play, this Pokémon's
    attacks do +40 after W/R to the Defending Pokémon. Stops while Asleep,
    Confused, or Paralyzed (Politoed — Frog Song)."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.amount <= 0:
            return
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker:
            return
        if _asleep_confused_or_paralyzed(holder):
            return
        line = sum(
            1
            for player_id in calc.board.player_ids
            for poked in calc.board.pokemon_in_play(player_id)
            if _is_poli_line(poked)
        )
        if line > 3:
            calc.amount += 40


frog_song = FrogSongPassive()


is_unown = pokemon_name_contains("Unown")


def unown_letter(letter: str):
    """Pokémon whose display name contains `Unown [letter]`."""
    return pokemon_name_contains(f"Unown [{letter}]")


def _unown_in_play(board, player_id, letter: str):
    named = unown_letter(letter)
    return [poked for poked in board.pokemon_in_play(player_id) if named(poked)]


def _unown_damage_counters(board, pokemon) -> int:
    return max(0, (effective_max_hp(board, pokemon)
                   - pokemon.get_attribute(AttrID.HP, 0)) // 10)


def unown_letters_on_bench(*letters):
    """Ability gate: each Unown letter is on your Bench (FIND / UNDO)."""
    named = [unown_letter(letter) for letter in letters]

    def check(board, player_id, pokemon=None) -> bool:
        bench = board.find_player_area(player_id, "bench")
        benched = [
            child for child in (bench.children if bench else [])
            if isinstance(child, PokemonEntity)
        ]
        return all(any(pred(poked) for poked in benched) for pred in named)
    return check


class UnownAngerPassive(Passive):
    """Hidden Power from your Unown does +10 per damage counter on one
    Unown [A]. Use only 1 [Anger] per attack; stops while Asleep,
    Confused, or Paralyzed."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.attack_title != "Hidden Power":
            return
        attacker = calc.attacker
        if attacker is None or not is_unown(attacker):
            return
        holder = carrier_pokemon(carrier) or carrier
        owner = holder.owning_player_id
        if attacker.owning_player_id != owner:
            return
        working = [
            poked for poked in _unown_in_play(calc.board, owner, "A")
            if not _asleep_confused_or_paralyzed(poked)
        ]
        if not working:
            return
        chosen = max(
            working,
            key=lambda poked: (
                _unown_damage_counters(calc.board, poked),
                poked.entity_id,
            ),
        )
        if chosen is not holder:
            return
        bonus = 10 * _unown_damage_counters(calc.board, chosen)
        if bonus:
            calc.amount += bonus


unown_anger_passive = UnownAngerPassive()


class UnownTypeReducePassive(Passive):
    """Your Pokémon take `amount` less from attacks by Pokémon of
    `pokemon_type` after W/R. Stops if more than one Unown [letter] is in
    play; works even while Asleep, Confused, or Paralyzed."""

    def __init__(self, pokemon_type: PokemonTypes, letter: str, amount: int = 30):
        self.pokemon_type = pokemon_type
        self.letter = letter
        self.amount = amount

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack:
            return
        holder = carrier_pokemon(carrier) or carrier
        owner = holder.owning_player_id
        if calc.target.owning_player_id != owner:
            return
        if len(_unown_in_play(calc.board, owner, self.letter)) != 1:
            return
        attacker = calc.attacker
        if attacker is None:
            return
        types = effective_pokemon_types(calc.board, attacker)
        if self.pokemon_type.value not in types:
            return
        calc.amount = max(0, calc.amount - self.amount)


def unown_type_reduce_passive(pokemon_type: PokemonTypes, letter: str,
                              amount: int = 30) -> Passive:
    """[Darkness] / [Metal] / [Normal] — 30 less from that type's attacks."""
    return UnownTypeReducePassive(pokemon_type, letter, amount)


async def unown_engage(ctx):
    """On play: opponent may shuffle their hand into their deck and draw 4;
    then you may do the same (Unown [E] — [Engage])."""
    if await ctx.ask_yes_no(
            "Shuffle your hand into your deck and draw 4 cards?",
            player_id=ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
        await ctx.draw_cards(4, ctx.opponent_id)
    if await ctx.ask_yes_no(
            "Shuffle your hand into your deck and draw 4 cards?"):
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        await ctx.draw_cards(4)


unown_find = search_to_hand(
    is_trainer_card, count=1, reveal=True,
    prompt="Choose a Trainer card.",
)


unown_yield = flip_or_nothing(then=search_attach_energy(
    predicate=is_psychic_energy_card, count=1, target_pred=is_unown,
    distribute=False,
    prompt="Choose a Psychic Energy card to attach.",
))


async def unown_increase(ctx):
    """On play: you may search for an Unown and put it onto your Bench
    (Unown [I] — [Increase]). Can't be used if the Bench is full."""
    if not bench_has_room(ctx.board, ctx.player_id) or not ctx.deck():
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no(
            "Search your deck for a card with Unown in its name "
            "and put it onto your Bench?"):
        ctx.suppress_announce = True
        return
    await search_to_bench(
        is_unown,
        prompt="Choose a card with Unown in its name to put onto your Bench.",
    )(ctx)


async def unown_observe(ctx):
    """Look at the top 5 of the opponent's deck; put them back in order
    (Unown [O] — [Observe])."""
    await look_at_opponent_deck(ctx, 5)


def unown_observe_condition(board, player_id, pokemon=None) -> bool:
    if not no_special_conditions(board, player_id, pokemon):
        return False
    opponent = _opponent_id(board, player_id)
    return opponent is not None and has_cards_in_deck(board, opponent)


async def unown_undo(ctx):
    """Return your Active Pokémon and all attached cards to your hand
    (Unown [U] — [Undo])."""
    pokemon = ctx.my_active()
    if pokemon is None:
        return
    await ctx.put_in_hand(full_stack(pokemon), reveal=False)
    _defer_promote(ctx, ctx.player_id)


def unown_bear_condition(board, player_id, pokemon=None) -> bool:
    """[Bear]: remaining HP above 10, and a damaged Unown is in play."""
    if pokemon is None or pokemon.get_attribute(AttrID.HP, 0) <= 10:
        return False
    return any(
        is_unown(poked) and _is_damaged(board, poked)
        for poked in board.pokemon_in_play(player_id)
    )


async def unown_bear(ctx):
    """Move 1 damage counter from an Unown onto this Unown [B]."""
    holder = ctx.source
    if holder is None:
        return
    sources = [
        poked for poked in ctx.my_pokemon_in_play()
        if is_unown(poked) and _is_damaged(ctx.board, poked)
    ]
    if not sources:
        return
    source = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
        sources, "Choose a Pokémon with Unown in its name")
    if source is None:
        return
    await ctx.move_damage_counters(source, holder, max_count=1)


class UnownKeepPassive(Passive):
    """Opponent effects can't discard Energy from your Unown (Unown [K] —
    [Keep]). Works even while Asleep, Confused, or Paralyzed."""

    def blocks_discard(self, card, carrier):
        if not is_energy_card(card):
            return False
        holder = carrier_pokemon(card)
        return (
            holder is not None
            and is_unown(holder)
            and holder.owning_player_id == carrier.owning_player_id
        )


unown_keep_passive = UnownKeepPassive()


async def belly_drum(ctx):
    """Put 3 damage counters on self. If that doesn't Knock Out, search
    the deck for 2 Basic Energy and attach them here."""
    attacker = ctx.attacker
    if attacker is None:
        return
    await ctx.deal_damage(
        30, target=attacker, apply_modifiers=False, as_counters=True)
    if attacker.get_attribute(AttrID.HP, 0) <= 0:
        return
    await search_attach_energy(
        is_basic_energy_card, count=2, to_self=True,
        prompt="Choose 2 Basic Energy cards to attach.",
    )(ctx)


def fury_cutter(bonuses=None, coins=4):
    """Flip `coins`; printed damage plus bonuses[heads].

    Neo Discovery Scyther: +10 / +20 / +40 / +80 for exactly 1 / 2 / 3 / 4
    heads.
    """
    table = bonuses if bonuses is not None else {1: 10, 2: 20, 3: 40, 4: 80}

    async def effect(ctx):
        results = await ctx.flip_coins(
            coins, ctx.ability.title if ctx.ability else "Fury Cutter")
        heads = sum(1 for r in results if r)
        amount = (getattr(ctx.ability, "damage", 0) or 0) + table.get(heads, 0)
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


_MYSTERIOUS_FOSSIL = "MysteriousFossil"


def evolves_from_mysterious_fossil(card) -> bool:
    """Direct evolutions of Mysterious Fossil (Omanyte, Kabuto, Aerodactyl)."""
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == _MYSTERIOUS_FOSSIL


async def fossil_egg(ctx):
    """Heads: bench a Mysterious Fossil evolution from hand or deck, treated
    as a Basic. Shuffle only if the deck was searched. Unplayable if the
    Bench is full (Fossil Egg)."""
    results = await ctx.flip_coins(1, "Fossil Egg")
    if not results or not results[0]:
        return
    hand_matches = [c for c in ctx.hand() if evolves_from_mysterious_fossil(c)]
    can_search = bool(ctx.deck())
    if hand_matches and can_search:
        from_deck = await ctx.choose(
            "Put a card that evolves from Mysterious Fossil onto your Bench "
            "from your hand, or search your deck?",
            ["Hand", "Deck"],
        ) == 1
    else:
        from_deck = can_search and not hand_matches
    if from_deck:
        picks = await ctx.search_deck(
            evolves_from_mysterious_fossil, count=1, minimum=0,
            prompt="Choose a card that evolves from Mysterious Fossil.",
        )
        if picks:
            await ctx.bench_pokemon(picks[0])
        await ctx.shuffle_deck()
        return
    if not hand_matches:
        return
    picks = await ctx.choose_cards(
        hand_matches, 1, minimum=1,
        prompt="Choose a card that evolves from Mysterious Fossil from your hand")
    if picks:
        await ctx.bench_pokemon(picks[0])


async def discard_fire_or_nothing(ctx):
    """Discard 1 Fire Energy card attached, or this attack does nothing
    (Houndoom — Flamethrower)."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        prompt="Choose a Fire Energy card to discard")
    if discarded:
        await ctx.deal_damage()


collect_fire = attach_from_discard(
    predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
    prompt="Choose a Fire Energy card to attach",
)


plunder = mug


async def sketch(ctx):
    """Copy the Defending Pokémon's last-turn attack, ignoring Energy costs
    and other requirements, if this Pokémon was already in play then
    (Smeargle — Sketch)."""
    copier = ctx.attacker or ctx.source
    defender = ctx.defender
    if copier is None or defender is None:
        return
    state = ctx.session.turn_state
    if state.entered_play_turn.get(copier.entity_id, 0) >= state.turn_number:
        return
    title = None
    for used_id, _archetype, used_title in state.attacks_used_last_turn:
        if used_id == defender.entity_id:
            title = used_title
    if not title:
        return
    matches = [
        attack for _, attack in copyable_defending_attacks(
            ctx.board, copier, ctx.player_id,
            require_energy=False, skip_requirements=True)
        if attack.title == title
    ]
    if not matches:
        return
    chosen = matches[0]
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        attacker = ctx.attacker
        if attacker is None:
            return
        for entry in attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(
                    attacker.entity_id, entry["abilityID"])


async def nap_time(ctx):
    """Remove all damage counters from this Pokémon; it is now Asleep
    (Teddiursa — Nap Time)."""
    pokemon = ctx.attacker
    if pokemon is None:
        return
    amount = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
    if amount > 0:
        await ctx.heal(amount, pokemon)
    await ctx.apply_special_condition(pokemon, SpecialConditions.ASLEEP)


class PursuitPassive(Passive):
    """If the marked Pokémon leaves Active during its owner's turn, put 1
    damage counter on it (Umbreon — Pursuit)."""

    def __init__(self, target_id: str):
        self.target_id = target_id

    def counters_on_active_to_bench(self, pokemon, carrier):
        return 1 if pokemon.entity_id == self.target_id else 0


async def pursuit(ctx):
    """Printed damage; during the opponent's next turn, if that Pokémon
    tries to retreat, do 10 (no Weakness or Resistance)."""
    await ctx.deal_damage()
    defender = ctx.defender
    attacker = ctx.attacker
    if defender is None or attacker is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(
        attacker, PursuitPassive(defender.entity_id))


# ----------------------------------------------------------------------
# Neo Revelation (NEO3)
# ----------------------------------------------------------------------

_MAGNE_LINE = frozenset(("Magnemite", "Magneton", "Dark Magneton"))


def _is_magne_line(pokemon) -> bool:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _MAGNE_LINE


def electromagnetic_power_condition(board, player_id, pokemon=None) -> bool:
    """A Magnemite/Magneton/Dark Magneton has Energy, and another can take it."""
    if pokemon is None or _asleep_confused_or_paralyzed(pokemon):
        return False
    magne = [
        poked for poked in board.pokemon_in_play(player_id)
        if _is_magne_line(poked)
    ]
    if len(magne) < 2:
        return False
    return any(board.attached_energies(poked) for poked in magne)


async def electromagnetic_power(ctx):
    """Move 1 Energy card from one Magne-line Pokémon to a different one."""
    magne = [poked for poked in ctx.my_pokemon_in_play() if _is_magne_line(poked)]
    await ctx.move_energy_freely(
        magne, magne, max_count=1,
        prompt="Choose an Energy card to move",
    )


class NightEyesMarker(Passive):
    """Marks a Pokémon that was hit by Night Eyes (Misdreavus — Perish Song)."""


async def night_eyes(ctx):
    """The Defending Pokémon is now Asleep; remember it was hit this turn."""
    defender = ctx.defender
    await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_own_next_turn(defender, NightEyesMarker())


def _has_night_eyes_marker(ctx, pokemon) -> bool:
    for temp in getattr(ctx.board, "temporary_passives", None) or []:
        if temp.carrier_entity_id != pokemon.entity_id:
            continue
        if isinstance(temp.passive, NightEyesMarker):
            return True
    return False


async def perish_song(ctx):
    """KO the Defending Pokémon if it is Asleep and took Night Eyes last turn."""
    defender = ctx.defender
    if defender is None:
        return
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    if asleep not in (defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        return
    if not ctx.attack_used_last_turn(title="Night Eyes"):
        return
    if not _has_night_eyes_marker(ctx, defender):
        return
    await ctx.knock_out(defender)


class AllergicPollenPassive(Passive):
    """Discard-pile cards are unaffected by attacks or Pokémon Powers while
    this Pokémon is in play and not Asleep, Confused, or Paralyzed."""

    def blocks_discard_pile_effects(self, source_kind, carrier):
        if source_kind not in ("attack", "ability"):
            return False
        holder = carrier_pokemon(carrier) or carrier
        if holder is None or _asleep_confused_or_paralyzed(holder):
            return False
        return True


allergic_pollen_passive = AllergicPollenPassive()


old_rod_condition = requires_discard(
    lambda c: is_pokemon_card(c) or is_trainer_card(c)
)


async def old_rod(ctx):
    """Flip 2 coins. Both heads: a Pokémon from discard to hand. Both tails:
    a Trainer from discard to hand."""
    results = await ctx.flip_coins(2, "Old Rod")
    if not results or len(results) < 2:
        return
    heads = sum(1 for r in results if r)
    if heads == 2:
        pred = is_pokemon_card
        prompt = ("Choose a Baby Pokémon, Basic Pokémon, or Evolution card "
                  "to put into your hand")
    elif heads == 0:
        pred = is_trainer_card
        prompt = "Choose a Trainer card to put into your hand"
    else:
        return
    cards = [card for card in ctx.discard_pile() if pred(card)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, prompt=prompt)
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


def _can_evolve_non_baby(pokemon) -> bool:
    if is_baby_pokemon(pokemon.archetype_id):
        return False
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return False
    return any(evolves_from(guid, logic_name) for guid in CARD_DEFS_BY_GUID)


def pokemon_breeder_fields_condition(board, player_id, pokemon=None) -> bool:
    """A non-Baby Pokémon in play can evolve, and the deck is nonempty."""
    if not deck_nonempty(board, player_id):
        return False
    return any(
        _can_evolve_non_baby(poked)
        for poked in board.pokemon_in_play(player_id)
    )


async def pokemon_breeder_fields(ctx):
    """Flip a coin for 1 or 2 evolvable non-Baby Pokémon; heads searches a
    later-Stage card of that line into the hand, then shuffle."""
    candidates = [
        poked for poked in ctx.my_pokemon_in_play()
        if _can_evolve_non_baby(poked)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, min(2, len(candidates)), minimum=1,
        prompt="Choose 1 or 2 of your non-Baby Pokémon that can evolve",
    )
    if not picks:
        return
    results = await ctx.flip_coins(len(picks), "Pokémon Breeder Fields")
    searched = False
    for poked, heads in zip(picks, results):
        if not heads:
            continue
        from_name = poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        searched = True
        found = await ctx.search_deck(
            lambda c, name=from_name: bool(name) and evolves_from(
                c.archetype_id, name),
            count=1, minimum=0,
            prompt="Choose a later-Stage card that matches that Pokémon.",
        )
        if found:
            await ctx.put_in_hand(found, reveal=True)
    if searched:
        await ctx.shuffle_deck()


def energy_converter_condition(board, player_id, pokemon=None) -> bool:
    """A basic Energy is attached to 1 of your Pokémon; not A/C/P."""
    return miracle_shift_condition(board, player_id, pokemon)


class EnergyConverterPassive(Passive):
    """Treat one Energy card as a chosen type until EOT; reverts if the
    Porygon2 that converted it is Asleep, Confused, or Paralyzed (or
    leaves play)."""

    def __init__(self, energy_id: str, energy_type: int, source_id: str):
        self.energy_id = energy_id
        self.energy_type = energy_type
        self.source_id = source_id

    def modify_energy_provided(self, options, energy, holder, board):
        if energy is None or energy.entity_id != self.energy_id:
            return options
        source = board.get_entity(self.source_id)
        if source is None or not isinstance(source, PokemonEntity):
            return options
        if source not in board.pokemon_in_play(source.owning_player_id):
            return options
        if _asleep_confused_or_paralyzed(source):
            return options
        return [[self.energy_type]]


async def energy_converter(ctx):
    """Choose 1 basic Energy on 1 of your Pokémon and treat it as a chosen
    type until the end of the turn (Porygon2 — Energy Converter)."""
    pool = [
        energy
        for poked in ctx.my_pokemon_in_play()
        for energy in ctx.attached_energies(poked)
        if is_basic_energy_card(energy)
    ]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, prompt="Choose a basic Energy card")
    if not picks:
        return
    types = [option[0] for option in ALL_TYPES_ONE_AT_A_TIME]
    names = [CLIENT_POKEMON_TYPE_NAMES[energy_type] for energy_type in types]
    idx = await ctx.choose("Choose an Energy type", names)
    chosen = types[idx]
    energy = picks[0]
    source = ctx.source
    if source is None:
        return
    ctx.add_temporary_passive(
        energy,
        EnergyConverterPassive(
            energy.entity_id, chosen.value, source.entity_id),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )


_DELTA_BEAM_CHOICES = (
    ("Asleep", SpecialConditions.ASLEEP),
    ("Confused", SpecialConditions.CONFUSED),
    ("Paralyzed", SpecialConditions.PARALYZED),
)


async def delta_beam(ctx):
    """Printed damage; heads, choose Asleep, Confused, or Paralyzed."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(
        1, ctx.ability.title if ctx.ability else "Delta Beam")
    if not results or not results[0]:
        return
    target = ctx.defender
    if target is None:
        return
    idx = await ctx.choose(
        "Choose a Special Condition",
        [name for name, _ in _DELTA_BEAM_CHOICES],
    )
    await ctx.apply_special_condition(target, _DELTA_BEAM_CHOICES[idx][1])


async def lightning_burst(ctx):
    """ON_ENERGY_ATTACHED: attaching Lightning Energy from hand to this
    Pokémon makes the opponent switch (Raikou — Lightning Burst). Off while
    Asleep, Confused, or Paralyzed."""
    holder = ctx.source
    if holder is None or _asleep_confused_or_paralyzed(holder):
        ctx.suppress_announce = True
        return
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not holder:
        ctx.suppress_announce = True
        return
    energy = ctx.attached_energy
    if energy is None or not _typed_basic_energy(energy, PokemonTypes.LIGHTNING):
        ctx.suppress_announce = True
        return
    if not ctx.opponent_bench():
        ctx.suppress_announce = True
        return
    await opponent_switches(ctx)


class LegendaryBodyPassive(Passive):
    """While Active, this Pokémon and its Energy aren't affected by Trainer
    cards other than Stadiums; attached Trainers are discarded. Works even
    while Asleep, Confused, or Paralyzed (Entei / Raikou / Suicune)."""

    def _active_holder(self, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if not is_in_active_spot(holder):
            return None
        return holder

    def _protects(self, affected, carrier):
        holder = self._active_holder(carrier)
        if holder is None or affected is None:
            return False
        if affected is holder:
            return True
        return is_energy_card(affected) and carrier_pokemon(affected) is holder

    def _blocks_trainer(self, trainer_type, affected, carrier):
        if trainer_type == TrainerType.STADIUM.value:
            return False
        return self._protects(affected, carrier)

    def blocks_trainer_effects(self, affected_player_id, trainer_card,
                               trainer_type, carrier, affected_entity=None,
                               board=None):
        holder = self._active_holder(carrier)
        if holder is None or affected_player_id != holder.owning_player_id:
            return False
        return self._blocks_trainer(trainer_type, affected_entity, carrier)

    def blocks_own_trainer_effects(self, affected_player_id, trainer_card,
                                   trainer_type, carrier, affected_entity=None,
                                   board=None):
        return self.blocks_trainer_effects(
            affected_player_id, trainer_card, trainer_type, carrier,
            affected_entity, board)

    def blocks_energy_removal(self, energy, mover_player_id, carrier):
        return self._protects(energy, carrier)

    def discards_attached_trainers(self, pokemon, carrier):
        holder = self._active_holder(carrier)
        return holder is not None and pokemon is holder


legendary_body_passive = LegendaryBodyPassive()


async def legendary_body_discard_trainers(ctx):
    """While Active, discard any Trainer cards attached (Legendary Body)."""
    holder = ctx.source
    if holder is None or not is_in_active_spot(holder):
        ctx.suppress_announce = True
        return
    trainers = [child for child in list(holder.children)
                if is_trainer_card(child)]
    if not trainers:
        ctx.suppress_announce = True
        return
    await ctx.discard_cards(trainers)


class RocketsHideoutPassive(Passive):
    """Each in-play Pokémon with Dark in its name gets +20 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        return 20 if pokemon_name_contains("Dark")(pokemon) else 0


rockets_hideout_passive = RocketsHideoutPassive()


class HardShellPassive(Passive):
    """If an attack would do 40 or less after W/R, that damage becomes 10.
    Stops while Asleep, Confused, or Paralyzed (Shuckle — Hard Shell)."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack or calc.amount <= 0 or calc.amount > 40:
            return
        holder = carrier_pokemon(carrier) or carrier
        if calc.target is not holder:
            return
        if _asleep_confused_or_paralyzed(holder):
            return
        calc.amount = 10


hard_shell = HardShellPassive()


async def devastate(ctx):
    """Discard 2 Fire Energy or nothing; 50 plus 10 to the Bench; heads,
    discard 1 Energy from each of the opponent's Pokémon that has Energy
    (Shining Gyarados — Devastate)."""
    fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
    if len(fire) < 2:
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 2,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        prompt="Choose 2 Fire Energy cards to discard")
    if len(discarded) < 2:
        return
    await ctx.deal_damage()
    for poked in ctx.opponent_bench():
        await ctx.deal_damage(10, target=poked)
    results = await ctx.flip_coins(1, "Devastate")
    if not results or not results[0]:
        return
    for poked in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(poked) or not ctx.attached_energies(poked):
            continue
        await ctx.discard_energy_from(
            poked, 1, prompt="Choose an Energy card to discard")


async def gold_scale(ctx):
    """Opponent may draw 2; either way, you may draw 2 (Shining Magikarp)."""
    if await ctx.ask_yes_no("Draw 2 cards?", player_id=ctx.opponent_id):
        await ctx.draw_cards(2, ctx.opponent_id)
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)


_GYARADOS_SEARCH_NAMES = frozenset(
    ("Gyarados", "Dark Gyarados", "Shining Gyarados"))


async def dragon_bond(ctx):
    """Search the deck for Gyarados, Dark Gyarados, or Shining Gyarados."""
    def pred(card):
        return getattr(def_for(card.archetype_id), "display_name", None) \
            in _GYARADOS_SEARCH_NAMES
    await search_to_hand(
        pred, prompt="Choose a Gyarados, Dark Gyarados, or Shining Gyarados.",
    )(ctx)


async def psykiss(ctx):
    """Heads: shuffle a Special Energy attached to 1 of the opponent's
    Pokémon into their deck (Smoochum — Psykiss)."""
    results = await ctx.flip_coins(1, "Psykiss")
    if not results or not results[0]:
        return
    candidates = []
    for poked in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(poked):
            continue
        if any(is_special_energy(energy) for energy in ctx.attached_energies(poked)):
            candidates.append(poked)
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates,
        "Choose 1 of your opponent's Pokémon with a Special Energy attached")
    if target is None:
        return
    specials = [energy for energy in ctx.attached_energies(target)
                if is_special_energy(energy)]
    if not specials:
        return
    picks = specials if len(specials) == 1 else await ctx.choose_cards(
        specials, 1, minimum=1,
        prompt="Choose a Special Energy card to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def swipe(ctx):
    """Heads: discard all Trainer cards attached to the opponent's Pokémon
    (Sneasel — Swipe)."""
    results = await ctx.flip_coins(1, "Swipe")
    if not results or not results[0]:
        return
    trainers = []
    for poked in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(poked):
            continue
        trainers.extend(
            child for child in list(poked.children) if is_trainer_card(child))
    if trainers:
        await ctx.discard_cards(trainers)


async def raging_headbutt(ctx):
    """Heads: 10 plus 10 per damage counter; tails: 10 (Snubbull)."""
    results = await ctx.flip_coins(1, "Raging Headbutt")
    extra = 0
    if results and results[0]:
        extra = 10 * damage_counters_on("self")(ctx)
    await ctx.deal_damage(10 + extra)


async def terrorize(ctx):
    """If the Defending Pokémon is Basic, lock one of its attacks through
    the opponent's next turn (Stantler — Terrorize)."""
    defender = ctx.defender
    if defender is None or not is_basic_pokemon(defender):
        return
    await amnesia(ctx)


async def overhead_toss(ctx):
    """Printed damage; if you have a Bench, flip — tails, 10 to one of
    yours (Stantler — Overhead Toss)."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    results = await ctx.flip_coins(1, "Overhead Toss")
    if results and results[0]:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to take 10 damage")
    if target is not None:
        await ctx.deal_damage(10, target=target, apply_modifiers=False)


async def core_stream(ctx):
    """Choose a non-Colorless Energy type; 20 to each opposing Pokémon with
    that type of Energy attached, no Weakness or Resistance (Starmie)."""
    names = [CLIENT_POKEMON_TYPE_NAMES[t] for t in _CONVERSION_TYPES]
    idx = await ctx.choose(
        "Choose an Energy type other than Colorless.", names)
    chosen = _CONVERSION_TYPES[idx].value
    for poked in ctx.opponent_pokemon_in_play():
        if any(energy_provides_type(energy, chosen)
               for energy in ctx.attached_energies(poked)):
            await ctx.deal_damage(20, target=poked, apply_modifiers=False)


class MimicPassive(Passive):
    """While Active and not Asleep/Confused/Paralyzed, this Pokémon may use
    the Defending Pokémon's printed attacks, including their costs
    (Sudowoodo — Mimic)."""

    def granted_attacks(self, board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return []
        if not is_in_active_spot(holder) or _asleep_confused_or_paralyzed(holder):
            return []
        opponent = _opponent_id(board, holder.owning_player_id)
        defending = board.active_pokemon(opponent) if opponent else None
        if defending is None:
            return []
        definition = def_for(defending.archetype_id)
        return [ability for ability in (getattr(definition, "abilities", None) or [])
                if isinstance(ability, Attack)]


mimic_passive = MimicPassive()


def _crystal_body_protects(target, carrier):
    holder = carrier_pokemon(carrier) or carrier
    return holder is target and not _asleep_confused_or_paralyzed(holder)


crystal_body_passive = attack_effect_shield_passive(
    protects=_crystal_body_protects)


async def aurora_wave(ctx):
    """Printed damage; 2 coins: both heads Paralyzes, one heads Asleep
    (Suicune — Aurora Wave)."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    results = await ctx.flip_coins(2, "Aurora Wave")
    heads = sum(1 for result in results if result)
    if heads == 2:
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    elif heads == 1:
        await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)


async def crystal_wave(ctx):
    """Flip: heads printed+10; tails printed then the opponent switches
    (Suicune — Crystal Wave). Damage happens before the switch."""
    results = await ctx.flip_coins(1, "Crystal Wave")
    bonus = 10 if results and results[0] else 0
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)
    if results and not results[0]:
        await opponent_switches(ctx)


async def present(ctx):
    """Flip 3 coins: 1 heads deals 40; 2 heads heals 30 from the Defending
    Pokémon; 3 heads deals 60; 3 tails heals all damage from it (Delibird)."""
    results = await ctx.flip_coins(3, "Present")
    heads = sum(1 for result in results if result)
    defender = ctx.defender
    if heads == 1:
        await ctx.deal_damage(40)
        return
    if heads == 3:
        await ctx.deal_damage(60)
        return
    if defender is None or ctx.effects_blocked(defender):
        return
    if heads == 2:
        await ctx.heal(30, defender)
        return
    amount = ctx.max_hp(defender) - defender.get_attribute(AttrID.HP, 0)
    if amount > 0:
        await ctx.heal(amount, defender)


async def howl(ctx):
    """ON_PLAY: you may mill 5; attach any milled Fire Energy to your Fire
    Pokémon. Using this power ends your turn (Entei — Howl)."""
    if not ctx.deck():
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no(
            "Discard the top 5 cards of your deck? If any are Fire Energy "
            "cards, attach them to your Fire Pokémon. Using this power "
            "ends your turn."):
        ctx.suppress_announce = True
        return
    milled = ctx.deck_top(5)
    await ctx.discard_cards(milled)
    fires = [card for card in milled
             if _typed_basic_energy(card, PokemonTypes.FIRE)]
    fire_pokemon = [poked for poked in ctx.my_pokemon_in_play()
                    if pokemon_has_type(poked, PokemonTypes.FIRE)]
    for energy in fires:
        if not fire_pokemon:
            break
        target = fire_pokemon[0] if len(fire_pokemon) == 1 else (
            await ctx.choose_pokemon(
                fire_pokemon, "Choose a Fire Pokémon to attach the Energy to")
        )
        if target is None:
            target = fire_pokemon[0]
        await ctx.attach_energy(energy, target)


def discard_typed_energy_or_nothing(energy_type, count=1):
    """Discard `count` basic Energy of that type, or the attack does nothing."""
    type_name = CLIENT_POKEMON_TYPE_NAMES.get(energy_type, "Energy")

    async def effect(ctx):
        available = _energy_cards_of_type(ctx, ctx.attacker, energy_type)
        if len(available) < count:
            return
        discarded = await ctx.discard_energy_from(
            ctx.attacker, count,
            predicate=lambda c, t=energy_type: _typed_basic_energy(c, t),
            prompt=f"Choose {count} {type_name} Energy card(s) to discard")
        if len(discarded) < count:
            return
        await ctx.deal_damage()
    return effect


def discard_energy_per_tails(coins, energy_type=None):
    """Printed damage, then flip `coins`; discard that many Energy (optionally
    of `energy_type`) for each tails (Entei — Mega Flame)."""
    type_name = (CLIENT_POKEMON_TYPE_NAMES.get(energy_type, "Energy")
                 if energy_type is not None else "Energy")

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            coins, ctx.ability.title if ctx.ability else "")
        tails = sum(1 for result in results if not result)
        if not tails:
            return
        pred = (lambda c, t=energy_type: _typed_basic_energy(c, t)
                ) if energy_type is not None else None
        await ctx.discard_energy_from(
            ctx.attacker, tails, predicate=pred,
            prompt=f"Choose {type_name} Energy card(s) to discard")
    return effect


def flip_spread_bench(amount, side="opponent"):
    """Printed damage, then flip: heads, `amount` to each Benched Pokémon
    on `side` (Flaaffy — Tail Shock)."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if results and results[0]:
            await spread_damage(amount, side=side)(ctx)
    return effect


def healing_field_condition(board, player_id, stadium=None) -> bool:
    active = board.active_pokemon(player_id)
    return active is not None and _is_damaged(board, active)


async def healing_field(ctx):
    """Heads: heal 20 from your Active Pokémon (1 counter if it only has 1)."""
    results = await ctx.flip_coins(1, "Healing Field")
    if not results or not results[0]:
        return
    active = ctx.my_active()
    if active is None:
        return
    await ctx.heal(20, active)


def count_basic_energy_types(ctx) -> int:
    """Distinct types among basic Energy cards attached to the attacker
    (Ho-oh — Rainbow Burn)."""
    types = set()
    attacker = ctx.attacker
    if attacker is None:
        return 0
    for energy in ctx.attached_energies(attacker):
        if not is_basic_energy_card(energy):
            continue
        for energy_type in energy.get_attribute(AttrID.POKEMON_TYPES) or []:
            types.add(energy_type)
    return len(types)


def _is_darkness_energy_card(card) -> bool:
    """Darkness Energy cards, including Neo's Special Darkness Energy."""
    if energy_provides_type(card, PokemonTypes.DARKNESS.value):
        return True
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == "Darkness Energy"


def count_darkness_energy_cards(ctx) -> int:
    """Darkness Energy cards attached to the attacker (Houndoom — Black Fang)."""
    attacker = ctx.attacker
    if attacker is None:
        return 0
    return sum(1 for energy in ctx.attached_energies(attacker)
               if _is_darkness_energy_card(energy))


async def dark_flame(ctx):
    """Discard 1 Fire Energy or nothing; then attach 1 Darkness Energy from
    discard if any (Houndoom — Dark Flame)."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.FIRE),
        prompt="Choose a Fire Energy card to discard")
    if not discarded:
        return
    await ctx.deal_damage()
    darkness = [card for card in ctx.discard_pile()
                if _is_darkness_energy_card(card)]
    if not darkness:
        return
    picks = await ctx.choose_cards(
        darkness, 1, minimum=1,
        prompt="Choose a Darkness Energy card to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


_HOPPIP_SKIPLOOM = frozenset(("Hoppip", "Skiploom"))


async def evolutionary_spore(ctx):
    """Choose any number of Hoppips and Skiplooms; evolve each from the deck
    (Jumpluff — Evolutionary Spore)."""
    targets = [
        poked for poked in ctx.my_pokemon_in_play()
        if poked.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _HOPPIP_SKIPLOOM
    ]
    if not targets:
        return
    chosen = await ctx.choose_cards(
        targets, len(targets), minimum=0,
        prompt="Choose any number of your Hoppips and Skiplooms")
    searched = False
    for pokemon in chosen:
        logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        picks = await ctx.search_deck(
            lambda c, name=logic_name: (
                c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name),
            count=1, minimum=0,
            prompt=f"Choose a card that evolves from {logic_name}.",
        )
        searched = True
        if picks:
            await ctx.evolve_pokemon(pokemon, picks[0])
    if searched:
        await ctx.shuffle_deck()


def copyable_stacked_attacks(board, copier, player_id) -> List:
    """(card, attack) pairs from Basic / Evolution cards under `copier`
    (Kingdra — Genetic Memory). Energy cost is waived; other gates remain."""
    if copier is None:
        return []
    pairs = []
    seen = set()
    for card in _evolution_underlays(copier):
        definition = def_for(card.archetype_id)
        for attack in getattr(definition, "abilities", None) or []:
            if not isinstance(attack, Attack):
                continue
            key = attack.ability_id or (attack.title, attack.game_text)
            if key in seen:
                continue
            seen.add(key)
            if attack.condition is not None \
                    and not attack.condition(board, player_id, copier):
                continue
            pairs.append((card, attack))
    return pairs


def genetic_memory_condition(board, player_id, pokemon=None) -> bool:
    return bool(copyable_stacked_attacks(board, pokemon, player_id))


async def genetic_memory(ctx):
    """Use an attack from a Basic or Evolution card under this Pokémon
    without paying its Energy cost (Kingdra — Genetic Memory)."""
    copier = ctx.attacker or ctx.source
    candidates = copyable_stacked_attacks(ctx.board, copier, ctx.player_id)
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(
        candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


async def twister(ctx):
    """Flip 2: each heads discards 1 Energy from the Defending Pokémon;
    both tails does nothing (Kingdra — Twister)."""
    results = await ctx.flip_coins(2, ctx.ability.title if ctx.ability else "Twister")
    heads = sum(1 for result in results if result)
    if heads == 0:
        return
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    await ctx.discard_energy_from(
        defender, min(heads, len(energies)),
        prompt="Choose Energy to discard from the Defending Pokémon")


async def aerowing(ctx):
    """You may flip: heads deals 80, tails does nothing; skip the flip for
    printed damage (Lugia — Aerowing)."""
    if await ctx.ask_yes_no(
            "Flip a coin? If heads, this attack does 80 damage. "
            "If tails, this attack does nothing."):
        results = await ctx.flip_coins(1, "Aerowing")
        if not results or not results[0]:
            return
        await ctx.deal_damage(80)
        return
    await ctx.deal_damage()


class SubmergePassive(Passive):
    """While `_crystal_type` is set, that type replaces printed types until
    EOT; Asleep/Confused/Paralyzed clears it (Lanturn — Submerge)."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        if _asleep_confused_or_paralyzed(pokemon):
            if pokemon.get_attribute(_CRYSTAL_TYPE_ATTR) is not None:
                pokemon.set_attribute(_CRYSTAL_TYPE_ATTR, None)
            return types
        override = pokemon.get_attribute(_CRYSTAL_TYPE_ATTR)
        if override is None:
            return types
        return [override]


submerge_passive = SubmergePassive()


async def submerge(ctx):
    """Change this Pokémon's type to Water until the end of the turn."""
    holder = ctx.source
    if holder is None:
        return
    holder.set_attribute(_CRYSTAL_TYPE_ATTR, PokemonTypes.WATER.value)


async def magma_pool(ctx):
    """When Magcargo leaves Active for the Bench, move 1 remaining Fire
    Energy to the new Active (retreat-cost Energy is already gone)."""
    holder = ctx.source
    retreated = getattr(ctx, "retreated_pokemon", None)
    if holder is None or retreated is not holder:
        ctx.suppress_announce = True
        return
    owner = holder.owning_player_id
    new_active = ctx.board.active_pokemon(owner) if owner else None
    if new_active is None or new_active is holder:
        ctx.suppress_announce = True
        return
    fire = _energy_cards_of_type(ctx, holder, PokemonTypes.FIRE)
    if not fire:
        ctx.suppress_announce = True
        return
    picks = fire if len(fire) == 1 else await ctx.choose_cards(
        fire, 1, minimum=1,
        prompt="Choose a Fire Energy card to attach to the new Active Pokémon")
    if picks:
        await ctx.move_energy(picks[0], new_active)


async def lava_flow(ctx):
    """You may discard any number of Fire Energy; +20 per card discarded
    (Magcargo — Lava Flow)."""
    fire = _energy_cards_of_type(ctx, ctx.attacker, PokemonTypes.FIRE)
    discarded = []
    if fire:
        discarded = await ctx.choose_cards(
            fire, len(fire), minimum=0,
            prompt="Choose any number of Fire Energy cards to discard")
        if discarded:
            await ctx.discard_cards(discarded)
    bonus = 20 * len(discarded)
    await ctx.deal_damage((getattr(ctx.ability, "damage", 0) or 0) + bonus)


# ----------------------------------------------------------------------
# Neo Revelation (NEO3)
# ----------------------------------------------------------------------

class PrehistoricMemoryPassive(Passive):
    """Evolved Pokémon (both sides) may use attacks from Basic and Evolution
    cards underneath them. Stops while Aerodactyl is Asleep, Confused, or
    Paralyzed."""

    def granted_attacks(self, board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if _asleep_confused_or_paralyzed(holder):
            return []
        if not is_evolved_pokemon(pokemon):
            return []
        attacks = []
        for stage in _evolution_underlays(pokemon):
            definition = def_for(stage.archetype_id)
            for ability in getattr(definition, "abilities", None) or []:
                if isinstance(ability, Attack):
                    attacks.append(ability)
        return attacks


prehistoric_memory = PrehistoricMemoryPassive()


async def grab(ctx):
    """Choose a Trainer attached to 1 of the opponent's Pokémon; they shuffle
    it into their deck (Aipom — Grab)."""
    trainers = []
    for poked in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(poked):
            continue
        trainers.extend(
            child for child in list(poked.children) if is_trainer_card(child))
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1,
        prompt="Choose a Trainer card attached to 1 of your opponent's Pokémon")
    if picks:
        owner = picks[0].owning_player_id or ctx.opponent_id
        await ctx.shuffle_into_deck(picks, owner)


async def attract_current(ctx):
    """Printed damage; flip 3, and for each heads search a Lightning Energy
    and attach it to 1 of your Lightning Pokémon (Ampharos — Attract Current)."""
    results = await ctx.flip_coins(3, "Attract Current")
    heads = sum(1 for result in results if result)
    if heads <= 0:
        await ctx.deal_damage()
        return
    await search_attach_energy(
        predicate=lambda c: _typed_basic_energy(c, PokemonTypes.LIGHTNING),
        count=heads,
        target_pred=lambda p: pokemon_has_type(p, PokemonTypes.LIGHTNING),
        prompt="Choose a Lightning Energy card to attach.",
    )(ctx)


balloon_berry_passive = retreat_free_when(
    lambda pokemon, carrier: carrier_pokemon(carrier) is pokemon
)


async def balloon_berry_on_retreat(ctx):
    """When the holder retreats, discard Balloon Berry instead of Energy."""
    retreated = getattr(ctx, "retreated_pokemon", None)
    holder = ctx.source
    if holder is None or retreated is not holder:
        ctx.suppress_announce = True
        return
    tool = next(
        (t for t, p in ctx.tools_in_play()
         if p is holder
         and getattr(def_for(t.archetype_id), "display_name", None)
         == "Balloon Berry"),
        None,
    )
    if tool is None:
        ctx.suppress_announce = True
        return
    await ctx.discard_cards([tool])


async def softboiled(ctx):
    """When played from hand: you may flip — heads heal 80, tails heal 40
    (Blissey — Softboiled)."""
    pokemon = ctx.source
    if pokemon is None:
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no(
            "Flip a coin? If heads, remove 8 damage counters from Blissey. "
            "If tails, remove 4 damage counters from Blissey."):
        ctx.suppress_announce = True
        return
    results = await ctx.flip_coins(1, "Softboiled")
    amount = 80 if results and results[0] else 40
    await ctx.heal(amount, pokemon)


async def psychic_leaf(ctx):
    """10 plus 10 per heads among coins equal to Energy on the Defending
    Pokémon; heal that much after W/R (Celebi — Psychic Leaf)."""
    defender = ctx.defender
    n = len(ctx.attached_energies(defender)) if defender is not None else 0
    results = await ctx.flip_coins(n, "Psychic Leaf") if n > 0 else []
    heads = sum(1 for result in results if result)
    dealt = await ctx.deal_damage(10 + 10 * heads)
    if dealt > 0 and ctx.attacker is not None:
        await ctx.heal(dealt, ctx.attacker)


class TimeTravelPassive(Passive):
    """If an opponent's attack would KO this Pokémon, flip: heads, it isn't
    Knocked Out and you shuffle it and attachments into the deck. Stops
    while Asleep, Confused, or Paralyzed (Celebi — Time Travel)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        holder = carrier_pokemon(carrier) or carrier
        if target is not holder or _asleep_confused_or_paralyzed(holder):
            return None
        current = holder.get_attribute(AttrID.HP, 0)
        if calc.amount < current:
            return None
        heads = await ctx.flip_coins(1, "Time Travel", source=holder)
        if not (heads and heads[0]):
            return None
        owner = holder.owning_player_id
        was_active = owner is not None and holder is ctx.board.active_pokemon(owner)
        await ctx.shuffle_into_deck(full_stack(holder), owner)
        if was_active and owner is not None:
            _defer_promote(ctx, owner)
        calc.prevented = True
        return 0


time_travel_passive = TimeTravelPassive()


async def psychic_damage(ctx):
    """Flip 3 coins; put 1 damage counter on the Defending Pokémon per heads
    (Celebi — Psychic Damage)."""
    results = await ctx.flip_coins(3, "Psychic Damage")
    heads = sum(1 for result in results if result)
    if heads and ctx.defender is not None:
        await ctx.deal_damage(heads * 10, target=ctx.defender, as_counters=True)


class TriggeredPoisonPassive(Passive):
    """If this Pokémon's owner attaches Energy from hand to it, it becomes
    Poisoned (Crobat — Triggered Poison)."""

    async def after_energy_attached(self, ctx, attaching_player_id, energy,
                                    receiver, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if receiver is not holder:
            return
        if attaching_player_id != holder.owning_player_id:
            return
        await ctx.apply_special_condition(holder, SpecialConditions.POISONED)


async def triggered_poison(ctx):
    """Printed damage; if the opponent attaches Energy to that Pokémon during
    their next turn, it becomes Poisoned."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(defender, TriggeredPoisonPassive())


async def cross_attack(ctx):
    """20× heads among 4 coins; 2 or more heads, the Defending Pokémon is
    Confused (Crobat — Cross Attack)."""
    results = await ctx.flip_coins(4, "Cross Attack")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(20 * heads)
    if heads >= 2 and ctx.defender is not None:
        await ctx.apply_special_condition(
            ctx.defender, SpecialConditions.CONFUSED)


async def negative_ion(ctx):
    """Printed damage, then if that Pokémon attacks this one next turn,
    damage is reduced by 10 before W/R (Chinchou — Negative Ion)."""
    await ctx.deal_damage()
    await growl(ctx)

