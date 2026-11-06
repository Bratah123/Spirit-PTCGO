"""Shared helpers for WOTC e-Card (Expedition / Aquapolis / Skyridge).

Card scripts stay thin data definitions; put non-trivial behavior here so
reprints across the three sets can import the same effect.
"""

from __future__ import annotations

from typing import Any, Callable, List, Optional

from spirit.game.attributes import (
    AttrID,
    CLIENT_POKEMON_TYPE_NAMES,
    CLIENT_SPECIAL_CONDITION_NAMES,
    GameSequence,
    PokemonStage,
    PokemonTypes,
    SpecialConditions,
    TrainerType,
)
from spirit.game.content.definitions import Attack
from spirit.game.data_utils import def_for, evolves_from
from spirit.game.models.board import PokemonEntity
from spirit.game.card_effects.attacks_common import (
    count_energy,
    damage_counters_on,
    damage_per,
    flip_or_nothing,
    lock_all_attacks,
    lock_defender_attacks,
)
from spirit.game.card_effects.passives_common import (
    ability_lock_passive,
    apply_protection,
    condition_immunity_passive,
    is_in_active_spot,
    opposing_active,
    retreat_free_when,
)
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.pokemon import devolvable, energy_provides_type
from spirit.game.card_effects.support_common import (
    opponent_switches,
    search_attach_energy,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    bench_has_room,
    has_basic_energy_in_hand,
    is_basic_energy_card,
    is_energy_card,
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
    attack_cost_satisfied,
    energy_provided_count,
)
from spirit.game.session.passives import (
    Passive,
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


def copyable_opponent_attacks(board, copier, player_id) -> List:
    """(pokemon, attack) pairs the copier can currently pay to use."""
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
            if attack.condition is not None \
                    and not attack.condition(board, player_id, copier):
                continue
            cost = effective_attack_cost(board, copier, _cost_as_names(attack.cost))
            if attack_cost_satisfied(cost, energies, board):
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
    boosted = bool(lightning) and await ctx.ask_yes_no(
        "Discard all Lightning Energy cards attached to Ampharos?")
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

from spirit.game.card_effects.support_common import requires_hand
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
# Rapidash — Overrun
# ----------------------------------------------------------------------

async def overrun(ctx):
    """20; if the opponent has a Bench, flip — heads, 10 to one Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    results = await ctx.flip_coins(1, "Overrun")
    if not results or not results[0]:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(10, target=target)


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
                               require_energy: bool = True) -> List:
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
        if attack.condition is not None \
                and not attack.condition(board, player_id, copier):
            continue
        if require_energy:
            cost = effective_attack_cost(board, copier, _cost_as_names(attack.cost))
            if not attack_cost_satisfied(cost, energies, board):
                continue
        pairs.append((defending, attack))
    return pairs


def copy_defending_attack(require_energy: bool = True, flip: bool = False):
    """Copy 1 of the Defending Pokémon's attacks (Sudowoodo Copy / Mini-Metronome)."""

    async def effect(ctx):
        if flip:
            results = await ctx.flip_coins(1, ctx.ability.title)
            if not results or not results[0]:
                return
        copier = ctx.attacker or ctx.source
        candidates = copyable_defending_attacks(
            ctx.board, copier, ctx.player_id, require_energy=require_energy)
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


# ----------------------------------------------------------------------
# Tentacool — Recover
# ----------------------------------------------------------------------

def has_typed_basic_energy(energy_type: PokemonTypes):
    """Attack condition: this Pokémon has a basic Energy card of that type."""
    def check(board, player_id, pokemon=None) -> bool:
        if pokemon is None:
            return False
        return any(_typed_basic_energy(e, energy_type)
                   for e in board.attached_energies(pokemon))
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

async def minor_errand_running(ctx):
    """Flip 2; for each heads, search a basic Energy into hand."""
    results = await ctx.flip_coins(2, "Minor Errand-Running")
    heads = sum(1 for result in results if result)
    if heads <= 0:
        return
    picks = await ctx.search_deck(
        is_basic_energy_card, count=heads, minimum=0,
        prompt="Choose basic Energy cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


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
    results = await ctx.flip_coins(1, "Freeze Lock")
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

async def trample(ctx):
    """Printed damage; for each Benched Pokémon, heads deals 20 to that Pokémon."""
    await ctx.deal_damage()
    benched = list(ctx.my_bench()) + list(ctx.opponent_bench())
    if not benched:
        return
    results = await ctx.flip_coins(len(benched), "Trample")
    for poked, heads in zip(benched, results):
        if heads:
            await ctx.deal_damage(20, target=poked)


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

