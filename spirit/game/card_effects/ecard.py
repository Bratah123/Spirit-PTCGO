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
    PokemonTypes,
    SpecialConditions,
    TrainerType,
)
from spirit.game.content.definitions import Attack
from spirit.game.data_utils import def_for
from spirit.game.models.board import PokemonEntity
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import full_stack
from spirit.game.session.legal_actions import (
    attack_cost_satisfied,
    energy_provided_count,
)
from spirit.game.session.passives import (
    Passive,
    carrier_pokemon,
    effective_attack_cost,
    effective_max_hp,
    effective_retreat_cost,
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


async def syncroblast(ctx):
    """80, or 20 if the two Actives don't have the same number of Energy cards."""
    mine = len(ctx.attached_energies(ctx.attacker))
    theirs = len(ctx.attached_energies(ctx.defender)) if ctx.defender else 0
    await ctx.deal_damage(80 if mine == theirs else 20)


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


def unused_energy_bonus(per: int, cap: int, base: Optional[int] = None):
    """Printed (or base) + per for each unused attached Energy, capped."""
    async def effect(ctx):
        total = sum(energy_provided_count(e, ctx.board)
                    for e in ctx.attached_energies(ctx.attacker))
        cost_total = sum((ctx.ability.cost or {}).values()) if ctx.ability else 0
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

async def plasma(ctx):
    """10; if a Lightning Energy is in discard, flip — heads, attach 1."""
    await ctx.deal_damage()
    energy = [c for c in ctx.discard_pile()
              if _typed_basic_energy(c, PokemonTypes.LIGHTNING)]
    if not energy:
        return
    results = await ctx.flip_coins(1, "Plasma")
    if not results or not results[0]:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a Lightning Energy card to attach to Raichu")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


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

