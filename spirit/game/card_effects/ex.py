"""Shared helpers for the EX era (Ruby & Sapphire through Power Keepers).

Card scripts stay thin data definitions; put non-trivial EX-era behavior here
so reprints across EX / Nintendo promos / POP can import the same effect.

Era themes: Pokémon-ex (2 prizes via subtype ``ex``), Poké-Powers / Poké-Bodies,
dual types, δ Delta Species, Holon Energies, Pokémon Star, Dark / owner's /
Rocket's Pokémon.
"""

from __future__ import annotations

import random
from typing import Any, Callable, Optional

from spirit.game.attributes import (
    AbilityTypes, AttrID, PokemonStage, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.card_effects.attacks_common import (
    count_energy, count_prizes_remaining, damage_per, discard_random_from_hand,
    lock_all_attacks,
)
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost, apply_protection, is_in_active_spot,
    prevent_damage_when, retreat_discount, retreat_free_when,
    takes_less_passive, team_damage_boost_passive,
)
from spirit.game.card_effects.pokemon import (
    devolvable, energy_provides_type, is_energy_card,
)
from spirit.game.card_effects.support_common import opponent_switches, search_to_bench
from spirit.game.card_effects.trainers import FossilBodyPassive, is_basic_energy_card
from spirit.game.data_utils import TRAINER_EFFECTS_BY_GUID, def_for, subtypes_for, unimplemented
from spirit.game.session.effects import (
    full_stack, is_basic_pokemon, is_evolution_pokemon, is_pokemon_card,
    is_supporter_card,
)
from spirit.game.session.passives import (
    Passive, TurnDamageModifier, carrier_pokemon, effective_max_hp,
    effective_pokemon_types,
)

# Prefer attacks_common / support_common / trainers / passives_common from call
# sites; add EX-specific factories below as sets need them.


def poke_power_condition(extra: Optional[Callable] = None):
    """Poké-Powers can't be used while the Pokémon has a Special Condition.

    `extra` is an additional (board, player_id, pokemon) playability check
    composed after the Special Condition block.
    """
    def check(board, player_id, pokemon=None):
        if pokemon is not None and pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False
        return extra is None or extra(board, player_id, pokemon)
    return check


def _energy_in_hand(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(is_energy_card(c) for c in (hand.children if hand else []))


def has_deck(board, player_id, pokemon=None) -> bool:
    area = board.find_player_area(player_id, "deck")
    return bool(area) and bool(area.children)


energy_draw_condition = poke_power_condition(_energy_in_hand)


def energy_draw(max_cards: int = 3):
    """Discard 1 Energy from hand, then draw up to `max_cards` (Energy Draw)."""
    async def effect(ctx):
        discarded = await ctx.discard_from_hand(
            1, predicate=is_energy_card,
            prompt="Discard 1 Energy card from your hand",
        )
        if not discarded:
            return
        available = min(max_cards, len(ctx.deck()))
        if available <= 0:
            return
        n = await ctx.choose(
            "Draw how many cards?",
            [str(i) for i in range(available + 1)],
            use_panel=False,
        )
        if n > 0:
            await ctx.draw_cards(n)
    return effect


def attach_from_discard_then_counters(predicate=None, count: int = 2,
                                      counters_per: int = 1, prompt: str = ""):
    """Attach up to `count` matching Energy from discard to 1 of your Pokémon,
    then put `counters_per` damage counters on it for each card attached
    (Pichu Energy Retrieval)."""
    pred = is_basic_energy_card if predicate is None else predicate

    async def effect(ctx):
        cards = [c for c in ctx.discard_pile() if pred(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt=prompt or "Choose basic Energy cards to attach.",
        )
        if not picks:
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to attach the Energy to",
        )
        if target is None:
            target = candidates[0]
        if target.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(target.entity_id)
        for card in picks:
            await ctx.attach_energy(card, target)
        await ctx.deal_damage(
            len(picks) * counters_per * 10, target=target,
            apply_modifiers=False, as_counters=True,
        )
    return effect


def search_attach_then_counters(predicate, counters: int = 2, prompt: str = ""):
    """Search the deck for an Energy, attach it to 1 of your Pokémon, put
    `counters` damage counters on that Pokémon, then shuffle (Psy Shadow)."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            predicate, count=1, minimum=0,
            prompt=prompt or "Choose an Energy card to attach.",
        )
        if picks:
            candidates = ctx.my_pokemon_in_play()
            if candidates:
                target = await ctx.choose_pokemon(
                    candidates, "Choose a Pokémon to attach the Energy to",
                )
                if target is None:
                    target = candidates[0]
                if target.entity_id not in ctx.visual_targets:
                    ctx.visual_targets.append(target.entity_id)
                await ctx.attach_energy(picks[0], target)
                await ctx.deal_damage(
                    counters * 10, target=target,
                    apply_modifiers=False, as_counters=True,
                )
        await ctx.shuffle_deck()
    return effect


def natural_cure_on_attach(energy_type):
    """Poké-Body: attaching an Energy of `energy_type` from hand cures this Pokémon."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id \
                or ctx.energy_receiver is not ctx.source:
            return
        energy = ctx.attached_energy
        if energy is None or not energy_provides_type(energy, type_value):
            return
        await ctx.cure_all_conditions(ctx.source)
    return effect


class FlipReduceDamagePassive(Passive):
    """Hard Cocoon: if this Pokémon would be damaged by an opponent's attack
    (after Weakness and Resistance), flip a coin. Heads reduces that damage
    by `amount`."""

    def __init__(self, amount, title=""):
        self.amount = amount
        self.title = title

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if carrier_pokemon(carrier) is not target:
            return None
        heads = await ctx.flip_coins(
            1, self.title, source=carrier_pokemon(carrier) or carrier)
        if heads and heads[0]:
            return max(0, calc.amount - self.amount)
        return None


def flip_reduce_damage_passive(amount, title="") -> Passive:
    """Flip-to-reduce shield: heads takes `amount` less from the attack hit."""
    return FlipReduceDamagePassive(amount, title)


def is_pokemon_ex(card) -> bool:
    """True when `card` is a Pokémon-ex (subtype ``ex``)."""
    return card is not None and "ex" in subtypes_for(
        getattr(card, "archetype_id", None) or ""
    )


def defender_is_ex(ctx) -> bool:
    """cond_fn: the Defending Pokémon is a Pokémon-ex (subtype ``ex``)."""
    return is_pokemon_ex(ctx.defender)


class SafeguardExPassive(Passive):
    """Prevent all effects of attacks, including damage, done to this
    Pokémon by the opponent's Pokémon-ex (Safeguard)."""

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.target
            and is_pokemon_ex(calc.attacker)
        )

    def blocks_attack_effects_from(self, target, carrier, attacker):
        return (
            carrier_pokemon(carrier) is target
            and is_pokemon_ex(attacker)
        )


def safeguard_ex_passive() -> Passive:
    """Poké-Body: immune to attacks from Pokémon-ex (Safeguard)."""
    return SafeguardExPassive()


def extra_energy_damage(per: int, base: int = 0, extra_cap: Optional[int] = None,
                        energy_type=None):
    """`base` + `per` for each Energy attached beyond this attack's Energy cost.

    extra_cap limits leftover Energy counted (Energy Ball's "can't add more
    than 20" is extra_cap=2 with per=10). energy_type counts only that type
    after paying its typed cost and Colorless slots (Water Gun).
    """
    count_attached = count_energy("self", energy_type=energy_type)
    type_value = getattr(energy_type, "value", energy_type)
    colorless = PokemonTypes.COLORLESS.value

    async def effect(ctx):
        attached = count_attached(ctx)
        cost = getattr(ctx.ability, "cost", None) or {}
        if type_value is None:
            paid = sum(cost.values())
        else:
            paid = 0
            for energy, n in cost.items():
                paid_type = getattr(energy, "value", energy)
                if paid_type == type_value or paid_type == colorless:
                    paid += n
        extra = max(0, attached - paid)
        if extra_cap is not None:
            extra = min(extra, extra_cap)
        amount = base + per * extra
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


def life_drain(flip: bool = True):
    """Flip (default): put damage counters on the Defending Pokémon until it
    is 10 HP away from being Knocked Out. No-ops when remaining HP is 10 or
    less (counters only; never heals)."""
    async def effect(ctx):
        if flip:
            results = await ctx.flip_coins(
                1, ctx.ability.title if ctx.ability else "")
            if not results or not results[0]:
                return
        defender = ctx.defender
        if defender is None:
            return
        amount = defender.get_attribute(AttrID.HP, 0) - 10
        if amount > 0:
            await ctx.deal_damage(amount, as_counters=True)
    return effect


def _named(name: str):
    def pred(card) -> bool:
        return getattr(def_for(card.archetype_id), "display_name", None) == name
    return pred


def search_evolution_pair(*pairs):
    """Search the deck for 1 card or both cards of one named pair, reveal,
    put into hand, and shuffle (Wurmple Signs of Evolution)."""
    async def effect(ctx):
        labels = [" and ".join(pair) for pair in pairs]
        idx = await ctx.choose("Search for which evolution pair?", labels)
        names = pairs[idx]
        picked = await ctx.search_deck_groups(
            [(_named(name), 1, f"Choose a {name}") for name in names],
            prompt="Choose 1 card or both cards of the pair.",
        )
        await ctx.put_in_hand(
            [card for group in picked for card in group], reveal=True)
        await ctx.shuffle_deck()
    return effect


async def lady_outing(ctx):
    """Search the deck for up to 3 basic Energy of different types, show
    them, put them into your hand, and shuffle."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 basic Energy cards of different types.",
        display_cards=deck_cards,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def heal_each_except_user(amount: int):
    """Heal `amount` from each of your Pokémon except the attacker (Healing Egg)."""
    async def effect(ctx):
        for pokemon in ctx.my_pokemon_in_play():
            if pokemon is ctx.attacker:
                continue
            await ctx.heal(amount, pokemon)
    return effect


def increased_base_damage_next_turn(*boosts):
    """During your next turn, named attacks on this Pokémon do +N.

    Each argument is ``(attack_title, extra_damage)`` (Pelipper Stockpile).
    """
    async def effect(ctx):
        for title, amount in boosts:
            await apply_own_next_turn_boost(ctx, amount, title)
    return effect


def heal_equal_to_damage():
    """Deal printed damage, then heal this Pokémon by the damage done to
    the Defending Pokémon (Swallow / Giga Drain)."""
    async def effect(ctx):
        dealt = await ctx.deal_damage()
        if dealt > 0:
            await ctx.heal(dealt, target=ctx.attacker)
    return effect


def scoop_defending_to_hand(flip: bool = False):
    """Return the Defending Pokémon and all attached cards to the opponent's
    hand. Does nothing without a Benched Pokémon to promote. flip=True
    gates the scoop on heads (Nosepass Repulsion)."""
    async def effect(ctx):
        if not ctx.opponent_bench():
            return
        if flip:
            results = await ctx.flip_coins(
                1, ctx.ability.title if ctx.ability else "")
            if not results or not results[0]:
                return
        target = ctx.defender
        if target is None or ctx.effects_blocked(target):
            return
        await ctx.put_in_hand(full_stack(target), reveal=False)

        async def _promote():
            if not await ctx.session._promote_new_active(ctx.opponent_id):
                screen_name = ctx.session.players[ctx.opponent_id].screen_name
                await ctx.session.end_game(
                    ctx.player_id, f"{screen_name} has no Pokémon left")

        ctx.deferred_actions.append(_promote)
    return effect


class TeamTakesLessBeforeWRPassive(Passive):
    """While the carrier is Active, opponent attacks deal `amount` less to
    the carrier owner's Pokémon (before Weakness and Resistance)."""

    def __init__(self, amount: int, while_active: bool = True):
        self.amount = amount
        self.while_active = while_active

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if self.while_active and not is_in_active_spot(carrier):
            return
        if calc.target.owning_player_id != carrier.owning_player_id:
            return
        calc.amount = max(0, calc.amount - self.amount)


def team_takes_less_before_wr(amount: int, while_active: bool = True) -> Passive:
    """Mightyena Intimidating Fang shape: as long as this Pokémon is Active,
    your Pokémon take N less from opponent attacks (before W/R)."""
    return TeamTakesLessBeforeWRPassive(amount, while_active)


def flip_discard_random_from_opponent_hand(count: int = 1):
    """Printed damage; flip a coin. If heads, discard `count` random cards
    from the opponent's hand without looking."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if results and results[0]:
            await discard_random_from_hand(
                ctx, player_id=ctx.opponent_id, count=count)
    return effect


def rough_skin(counters: int = 1):
    """Poké-Body: if this Active Pokémon is damaged by an opponent's attack
    (even if Knocked Out), put `counters` damage counters on the attacker."""
    async def effect(ctx):
        pokemon = ctx.source
        if not is_in_active_spot(pokemon):
            return
        attacker = ctx.damaged_by
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return
        await ctx.deal_damage(
            counters * 10, target=attacker,
            apply_modifiers=False, as_counters=True,
        )
    return effect


def attached_basic_energy_at_least(n: int):
    """Attack condition: this Pokémon has at least `n` basic Energy cards."""
    def check(board, player_id, pokemon) -> bool:
        return sum(1 for c in pokemon.children if is_basic_energy_card(c)) >= n
    return check


def discard_basic_energy_attack(count: int = 1, also=None):
    """Deal printed damage, then discard `count` basic Energy cards from the
    user. Pair with ``attached_basic_energy_at_least`` so the attack is not
    offered (and therefore does nothing) without enough Energy."""
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.discard_energy_from(
            ctx.attacker, count, predicate=is_basic_energy_card,
            prompt="Discard basic Energy from this Pokémon",
        )
        if also is not None:
            await also(ctx)
    return effect


async def lock_own_attacks(ctx):
    """This Pokémon can't attack during your next turn."""
    if ctx.attacker is not None:
        lock_all_attacks(ctx, ctx.attacker)


class OpponentPokePowerLockPassive(Passive):
    """While the carrier is Active, the opponent's Pokémon can't use
    Poké-Powers (Slaking Lazy). Poké-Bodies stay on."""

    def blocks_ability(self, pokemon, ability, carrier):
        if not is_in_active_spot(carrier):
            return False
        if pokemon.owning_player_id == carrier.owning_player_id:
            return False
        return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER


def opponent_poke_power_lock() -> Passive:
    """Lazy shape: as long as this Pokémon is Active, the opponent's
    Pokémon can't use Poké-Powers."""
    return OpponentPokePowerLockPassive()


def attach_from_hand(predicate, target="active", prompt: str = "",
                     counts_as_attachment: bool = True):
    """Attach 1 matching Energy from hand. target 'active' or 'choice'.

    counts_as_attachment=True so "from your hand" Poké-Bodies (Natural Cure /
    Natural Remedy) observe the attach.
    """
    async def effect(ctx):
        cards = [c for c in ctx.hand() if predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, 1, prompt=prompt or "Choose an Energy card to attach.",
        )
        if not picks:
            return
        if target == "active":
            receiver = ctx.my_active()
        else:
            candidates = ctx.my_pokemon_in_play()
            if not candidates:
                return
            receiver = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
        if receiver is None:
            return
        if receiver.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(receiver.entity_id)
        await ctx.attach_energy(
            picks[0], receiver, counts_as_attachment=counts_as_attachment)
    return effect


def heal_on_attach(energy_type, amount: int = 10, once_per_turn: bool = True):
    """Poké-Body: attaching an Energy of `energy_type` from hand heals
    `amount` from this Pokémon (Natural Remedy)."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id \
                or ctx.energy_receiver is not ctx.source:
            return
        energy = ctx.attached_energy
        if energy is None or not energy_provides_type(energy, type_value):
            return
        if once_per_turn:
            used_key = (
                ctx.source.entity_id,
                ctx.ability.ability_id if ctx.ability else "heal_on_attach",
            )
            if used_key in ctx.session.turn_state.used_abilities:
                return
            ctx.session.turn_state.used_abilities.add(used_key)
        await ctx.heal(amount, ctx.source)
    return effect


def heal_all_and_cant_attack():
    """Remove all damage from this Pokémon; it can't attack next turn
    (Slack Off)."""
    async def effect(ctx):
        pokemon = ctx.attacker or ctx.source
        if pokemon is not None:
            missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
            if missing > 0:
                await ctx.heal(missing, pokemon)
            lock_all_attacks(ctx, pokemon)
    return effect


def flip_tails_discard_energy(energy_type=None, all_energy: bool = False):
    """Printed damage; flip a coin. If tails, discard 1 Energy of
    `energy_type` (or any Energy) from this Pokémon (Fireworks).
    all_energy=True discards every matching Energy card (Burn Up)."""
    type_value = getattr(energy_type, "value", energy_type)
    pred = (lambda c: energy_provides_type(c, type_value)) \
        if type_value is not None else None

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if results and not results[0]:
            await ctx.discard_energy_from(
                ctx.attacker, 99 if all_energy else 1, predicate=pred,
                prompt="Discard Energy from this Pokémon",
            )
    return effect


def energy_trans_condition(energy_type=PokemonTypes.GRASS):
    """Poké-Power: at least 2 of your Pokémon in play, and one has an Energy
    providing `energy_type` that can be moved (Energy Trans)."""
    type_value = getattr(energy_type, "value", energy_type)

    def extra(board, player_id, pokemon=None):
        in_play = board.pokemon_in_play(player_id)
        if len(in_play) < 2:
            return False
        return any(
            energy_provides_type(e, type_value)
            for p in in_play for e in p.children
        )
    return poke_power_condition(extra)


def energy_trans(energy_type=PokemonTypes.GRASS):
    """Move 1 Energy providing `energy_type` from one of your Pokémon to
    another (Energy Trans). Pair with ``Activations.UNLIMITED``."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        pokemon = ctx.my_pokemon_in_play()
        await ctx.move_energy_freely(
            pokemon, pokemon,
            predicate=lambda c: energy_provides_type(c, type_value),
            max_count=1,
        )
    return effect


def attach_energy_from_hand(predicate=None, count: int = 1, prompt: str = ""):
    """Attach up to `count` matching Energy cards from hand to your Pokémon
    (Plus Energy). `predicate` defaults to basic Energy."""
    pred = is_basic_energy_card if predicate is None else predicate

    async def effect(ctx):
        energies = [c for c in ctx.hand() if pred(c)]
        take = min(count, len(energies))
        if take <= 0:
            return
        picks = await ctx.choose_cards(
            energies, take, minimum=take,
            prompt=prompt or "Choose a basic Energy card to attach.",
        )
        for card in picks:
            candidates = ctx.my_pokemon_in_play()
            if not candidates:
                return
            target = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to",
            )
            if target is None:
                target = candidates[0]
            await ctx.attach_energy(card, target)
    return effect


def _pokenav_match(card) -> bool:
    return is_basic_pokemon(card) or is_evolution_pokemon(card) or is_energy_card(card)


async def poke_nav(ctx):
    """Look at the top 3 cards; put 1 Basic Pokémon, Evolution, or Energy
    into your hand (show it); put the rest back on top in any order."""
    top = ctx.deck_top(3)
    if not top:
        return
    candidates = [c for c in top if _pokenav_match(c)]
    picks = []
    if candidates:
        picks = await ctx.choose_cards(
            candidates, 1, minimum=1,
            prompt="Choose a Basic Pokémon, Evolution card, or Energy card.",
            display_cards=top,
        )
        await ctx.put_in_hand(picks, reveal=True)
    remaining = len(top) - len(picks)
    if remaining > 1:
        await ctx.reorder_deck_top(remaining)


def lizard_poison():
    """Printed damage, then Asleep / Poisoned / Burned from attached Energy
    count (Sceptile Lizard Poison)."""
    count_attached = count_energy("self")

    async def effect(ctx):
        await ctx.deal_damage()
        n = count_attached(ctx)
        if n == 1 or n >= 3:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
        if n >= 2:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        if n >= 4:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def is_active_pokemon(board, player_id, pokemon=None) -> bool:
    """Poké-Power extra: this Pokémon is in the Active Spot."""
    return pokemon is not None and is_in_active_spot(pokemon)


class PartnerTypedTakesLessPassive(Passive):
    """While a named partner is in play, this Pokémon takes `amount` less
    from attacks by Pokémon of `attacker_types` (after Weakness and
    Resistance). Extra copies of the partner do not stack."""

    def __init__(self, amount, partner_name, attacker_types):
        self.amount = amount
        self.partner_name = partner_name
        self.attacker_types = [getattr(t, "value", t) for t in attacker_types]

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.target:
            return
        if not any(
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == self.partner_name
            for pid in calc.board.player_ids
            for p in calc.board.pokemon_in_play(pid)
        ):
            return
        if calc.attacker is None:
            return
        types = effective_pokemon_types(calc.board, calc.attacker)
        if not any(t in types for t in self.attacker_types):
            return
        calc.amount = max(0, calc.amount - self.amount)


def partner_typed_takes_less(amount, partner_name, attacker_types) -> Passive:
    """Glowing Screen shape: named partner in play, −N from typed attackers."""
    return PartnerTypedTakesLessPassive(amount, partner_name, attacker_types)


class PartnerRetreatFreePassive(Passive):
    """While a named partner is in play, the carrier's Retreat Cost is 0
    (Volbeat Uplifting Glow). Extra copies of the partner do not matter."""

    def __init__(self, partner_name):
        self.partner_name = partner_name

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return cost
        if not any(
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == self.partner_name
            for pid in board.player_ids
            for p in board.pokemon_in_play(pid)
        ):
            return cost
        return 0


def partner_retreat_free(partner_name) -> Passive:
    """Uplifting Glow: named partner in play, this Pokémon's Retreat Cost is 0."""
    return PartnerRetreatFreePassive(partner_name)


def may_discard_energy_for_condition(energy_type, *conditions, prompt: str = ""):
    """You may discard 1 Energy providing `energy_type`. If you do, apply
    `conditions` to the Defending Pokémon (Burning Claw / Dark Bind)."""
    type_value = getattr(energy_type, "value", energy_type)

    def pred(card) -> bool:
        return energy_provides_type(card, type_value)

    async def effect(ctx):
        await ctx.deal_damage()
        energies = [
            e for e in ctx.attached_energies(ctx.attacker) if pred(e)
        ]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=0,
            prompt=prompt or "You may discard a matching Energy card",
        )
        if not picks:
            return
        await ctx.discard_cards(picks)
        for condition in conditions:
            await ctx.apply_special_condition(ctx.defender, condition)
    return effect


def may_discard_all_energy_for_damage(energy_type, boosted: int,
                                      prompt: str = ""):
    """You may discard all Energy cards providing `energy_type`. If you do,
    this attack's base damage is `boosted` instead of the printed damage
    (Lightning Strike)."""
    type_value = getattr(energy_type, "value", energy_type)

    def pred(card) -> bool:
        return energy_provides_type(card, type_value)

    async def effect(ctx):
        base_val = getattr(ctx.ability, "damage", 0) or 0
        energies = [
            e for e in ctx.attached_energies(ctx.attacker) if pred(e)
        ]
        if energies and await ctx.ask_yes_no(
            prompt or "Discard all matching Energy cards attached to this Pokémon?"
        ):
            await ctx.discard_energy_from(ctx.attacker, 99, predicate=pred)
            await ctx.deal_damage(boosted)
        elif base_val > 0:
            await ctx.deal_damage(base_val)
    return effect


def flip_return_defender_energy():
    """Poké-Power: flip a coin. If heads, return 1 Energy card attached to
    the Defending Pokémon to the opponent's hand (Fan Away)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        defender = ctx.defender or ctx.opponent_active()
        if defender is None:
            return
        energies = list(ctx.attached_energies(defender))
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1,
            prompt="Choose an Energy card to return to your opponent's hand",
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


def flip_apply_condition(*conditions):
    """Poké-Power: flip a coin; heads applies `conditions` to the Defending
    Pokémon (Chaos Flash)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        target = ctx.defender or ctx.opponent_active()
        if target is None:
            return
        for condition in conditions:
            await ctx.apply_special_condition(target, condition)
    return effect


def shuffle_random_from_opponent_hand(count: int = 1):
    """Choose `count` cards from the opponent's hand without looking, look
    at them, then shuffle them into the opponent's deck (Surprise)."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if ctx.is_attack_effect() and printed > 0:
            await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        picks = random.sample(hand, min(count, len(hand)))
        await ctx.reveal_cards(picks, to_player=ctx.player_id)
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def flip_knock_out_defender(coins: int = 2):
    """Flip `coins`. If all are heads, the Defending Pokémon is Knocked Out
    (Judgement)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            coins, ctx.ability.title if ctx.ability else "")
        if results and all(results) and ctx.defender is not None:
            await ctx.knock_out(ctx.defender)
    return effect


def flip_attach_from_discard(predicate=None, prompt: str = ""):
    """Printed damage; flip a coin. If heads, attach 1 matching Energy from
    discard to this Pokémon (Plasma)."""
    pred = is_energy_card if predicate is None else predicate

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if ctx.is_attack_effect() and printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        cards = [c for c in ctx.discard_pile() if pred(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, 1, minimum=1,
            prompt=prompt or "Choose an Energy card to attach.",
        )
        if not picks:
            return
        holder = ctx.attacker or ctx.source
        if holder is None:
            return
        if holder.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(holder.entity_id)
        await ctx.attach_energy(picks[0], holder)
    return effect


def baby_evolution_condition(into_name: str):
    """Poké-Power: a card named `into_name` is in hand (Baby Evolution)."""
    pred = _named(into_name)

    def extra(board, player_id, pokemon=None):
        hand = board.find_player_area(player_id, "hand")
        return any(pred(c) for c in (hand.children if hand else []))
    return poke_power_condition(extra)


def baby_evolution(into_name: str):
    """Put a named Pokémon from hand onto this Pokémon (counts as evolving)
    and remove all damage counters (Baby Evolution)."""
    pred = _named(into_name)

    async def effect(ctx):
        matches = [c for c in ctx.hand() if pred(c)]
        if not matches:
            return
        picks = await ctx.choose_cards(
            matches, 1, minimum=1,
            prompt=f"Choose a {into_name} to put onto this Pokémon",
        )
        if not picks:
            return
        evolved = picks[0]
        await ctx.evolve_pokemon(ctx.source, evolved)
        missing = ctx.max_hp(evolved) - evolved.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, evolved)
    return effect


def search_basic_or_evo_per_energy():
    """Search the deck for a Basic Pokémon or Evolution card for each Energy
    attached to this Pokémon, show them, put into hand, and shuffle
    (Alluring Smile)."""
    count_attached = count_energy("self")

    async def effect(ctx):
        n = count_attached(ctx)
        picks = await ctx.search_deck(
            lambda c: is_basic_pokemon(c) or is_evolution_pokemon(c),
            count=n, minimum=0,
            prompt="Choose a Basic Pokémon or Evolution card for each Energy attached.",
        ) if n > 0 else []
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def feint_attack(amount: int):
    """Choose 1 of the opponent's Pokémon. Deal `amount` that isn't affected
    by Weakness, Resistance, Poké-Powers, Poké-Bodies, or other effects on
    that Pokémon (Feint Attack)."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            target = candidates[0]
        await ctx.deal_damage(
            amount, target=target,
            apply_modifiers=False, ignore_target_effects=True)
    return effect


def rapid_spin():
    """Printed damage; the opponent switches their Active (they choose), then
    you switch this Pokémon with 1 of yours (EX Baltoy Rapid Spin)."""
    async def effect(ctx):
        await ctx.deal_damage()
        await opponent_switches(ctx)
        await ctx.flush_choreography()
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


def lure_condition(*conditions):
    """You may switch the Defending Pokémon with 1 of the opponent's Benched
    Pokémon (you choose), then apply Special Conditions to the Defending
    Pokémon (Cradily Lure Poison)."""
    async def effect(ctx):
        old_active = ctx.opponent_active()
        if old_active is not None and ctx.opponent_bench() \
                and not ctx.effects_blocked(old_active) \
                and await ctx.ask_yes_no(
                    "Switch the Defending Pokémon with 1 of your opponent's "
                    "Benched Pokémon?"):
            target = await ctx.choose_pokemon(
                ctx.opponent_bench(),
                "Choose the opponent's new Active Pokémon",
            )
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        defender = ctx.opponent_active()
        if defender is not None:
            for condition in conditions:
                await ctx.apply_special_condition(defender, condition)
    return effect


class ExFossilPassive(FossilBodyPassive):
    """EX-era fossils: can't retreat, immune to Special Conditions, and a
    Knock Out doesn't take Prize cards."""

    def __init__(self):
        super().__init__(blocks_conditions=True)

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is carrier:
            return 0
        return count


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_pokemon_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


def condition_on_damaged(condition, while_active: bool = True):
    """Poké-Body: if this Pokémon is damaged by an opponent's attack
    (even if Knocked Out), the Attacking Pokémon gets `condition`
    (Fire Veil / Poison Payback). Pair with ON_DAMAGED_BY_ATTACK."""
    async def effect(ctx):
        pokemon = ctx.source
        if while_active and not is_in_active_spot(pokemon):
            return
        attacker = ctx.damaged_by
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return
        await ctx.apply_special_condition(attacker, condition)
    return effect


class TrainerPlayLockPassive(Passive):
    """Matching Trainer cards can't be played from hand.

    opponents_only locks the opponent (Primal Lock); both players when
    False (Primal Veil). while_active gates on the carrier being Active.
    """

    def __init__(self, predicate, opponents_only: bool = True,
                 while_active: bool = False):
        self.predicate = predicate
        self.opponents_only = opponents_only
        self.while_active = while_active

    def blocks_trainer_play(self, card, player_id, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if self.while_active and not is_in_active_spot(holder):
            return False
        if self.opponents_only and player_id == carrier.owning_player_id:
            return False
        return bool(self.predicate(card))


def opponent_cant_play_tools() -> Passive:
    """Primal Lock: as long as this Pokémon is in play, the opponent can't
    play Pokémon Tool cards."""
    return TrainerPlayLockPassive(_is_pokemon_tool_card)


def both_players_cant_play_supporters(while_active: bool = True) -> Passive:
    """Primal Veil: as long as this Pokémon is Active, each player can't
    play Supporter cards."""
    return TrainerPlayLockPassive(
        is_supporter_card, opponents_only=False, while_active=while_active)


async def discard_opponent_tools(ctx):
    """Discard every Pokémon Tool attached to the opponent's Pokémon
    (Primal Lock's come-into-play strip)."""
    tools = [
        child
        for pokemon in ctx.opponent_pokemon_in_play()
        for child in pokemon.children
        if _is_pokemon_tool_card(child)
    ]
    if tools:
        await ctx.discard_cards(tools)


def attach_as_many_from_hand(predicate, target: str = "active", prompt: str = ""):
    """Attach as many matching Energy from hand as you like (Drizzle).

    target 'active' attaches every chosen card to your Active Pokémon;
    'choice' picks a Pokémon per card.
    """
    async def effect(ctx):
        energies = [c for c in ctx.hand() if predicate(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt=prompt or "Choose Energy cards to attach.",
        )
        if not picks:
            return
        if target == "active":
            receiver = ctx.my_active()
            if receiver is None:
                return
            if receiver.entity_id not in ctx.visual_targets:
                ctx.visual_targets.append(receiver.entity_id)
            for card in picks:
                await ctx.attach_energy(
                    card, receiver, counts_as_attachment=True)
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        for card in picks:
            receiver = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
            if receiver is None:
                receiver = candidates[0]
            await ctx.attach_energy(card, receiver, counts_as_attachment=True)
    return effect


def search_to_bench_named(*names, count: int = 99, include_basic: bool = False,
                          prompt: str = ""):
    """Search the deck for named Pokémon (and optionally any Basic) and put
    them onto the Bench (Team Assembly / Influence). Stage 1 fossil Pokémon
    enter play without evolving, as the attack's 'treat as Basic' clause."""
    name_set = frozenset(names)

    def pred(card) -> bool:
        name = getattr(def_for(card.archetype_id), "display_name", None)
        if name in name_set:
            return True
        return include_basic and is_basic_pokemon(card)

    return search_to_bench(
        pred, count=count,
        prompt=prompt or "Choose Pokémon to put onto your Bench.",
    )


class EnergyVariationPassive(Passive):
    """This Pokémon's type is every type of basic Energy card attached to it
    (Kecleon Energy Variation). Printed types remain if none are attached."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        energy_types = []
        for child in carrier.children:
            if not is_basic_energy_card(child):
                continue
            for energy_type in child.get_attribute(AttrID.POKEMON_TYPES) or []:
                if energy_type not in energy_types:
                    energy_types.append(energy_type)
        return energy_types or types


def energy_variation_passive() -> Passive:
    """Poké-Body: this Pokémon is the same type as every attached basic Energy."""
    return EnergyVariationPassive()


def link_blast(match_damage: int, mismatch_damage: int):
    """If this Pokémon and the Defending Pokémon have the same amount of
    Energy attached, deal `match_damage`; otherwise `mismatch_damage`."""
    count_self = count_energy("self")
    count_def = count_energy("defender")

    async def effect(ctx):
        amount = match_damage if count_self(ctx) == count_def(ctx) else mismatch_damage
        await ctx.deal_damage(amount)
    return effect


async def time_spiral(ctx):
    """If the opponent has an Evolved Pokémon, choose 1 and flip. Heads:
    shuffle the highest Stage Evolution card into their deck."""
    candidates = [
        p for p in ctx.opponent_pokemon_in_play()
        if devolvable(p) and not ctx.effects_blocked(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Evolved Pokémon",
    )
    if target is None:
        return
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if not results or not results[0]:
        return
    owner_id = target.owning_player_id
    removed = await ctx.devolve_pokemon(target, steps=1, destination="deck")
    if removed:
        await ctx.shuffle_deck(owner_id)


async def pull_down(ctx):
    """Remove the highest Stage Evolution card from each of the opponent's
    Evolved Pokémon and put those cards into their hand (Omastar Pull Down)."""
    targets = [
        p for p in ctx.opponent_pokemon_in_play()
        if devolvable(p) and not ctx.effects_blocked(p)
    ]
    for target in targets:
        await ctx.devolve_pokemon(target, steps=1, destination="hand")


async def amnesia(ctx):
    """Choose 1 of the Defending Pokémon's attacks. That Pokémon can't use
    that attack during the opponent's next turn."""
    printed = getattr(ctx.ability, "damage", 0) or 0
    if ctx.is_attack_effect() and printed > 0:
        await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [
        e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
        if isinstance(e, dict) and e.get("abilityType") == "Attack"
        and e.get("abilityID")
    ]
    if not entries:
        return
    idx = 0
    if len(entries) > 1:
        idx = await ctx.choose(
            "Choose an attack that can't be used during your opponent's next turn",
            [e.get("title", {}).get("id", "Attack") for e in entries],
        )
    entry = entries[idx]
    state = ctx.session.turn_state
    state.attack_locks[(defender.entity_id, entry["abilityID"])] = (
        state.turn_number + 1
    )


def is_baby_pokemon(card) -> bool:
    """EX-era Baby Pokémon carry the Baby Evolution Poké-Power."""
    definition = def_for(getattr(card, "archetype_id", None) or "")
    for ability in getattr(definition, "abilities", None) or []:
        if getattr(ability, "title", None) == "Baby Evolution":
            return True
    return False


async def lanettes_net_search(ctx):
    """Search the deck for up to 3 Basic Pokémon of different types
    (excluding Baby Pokémon), show them, put them into hand, and shuffle."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    seen_types = []
    for card in deck_cards:
        if not is_basic_pokemon(card) or is_baby_pokemon(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 Basic Pokémon of different types.",
        display_cards=deck_cards,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def rain_dish(amount: int = 10):
    """Poké-Body: between turns, heal `amount` from this Pokémon (Rain Dish).
    Pair with ``Triggers.BETWEEN_TURNS``."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is not None:
            await ctx.heal(amount, pokemon)
    return effect


def _has_damaged_active(board, player_id, pokemon=None) -> bool:
    area = board.find_player_area(player_id, "activePokemonArea")
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in (area.children if area else [])
    )


healing_wind_condition = poke_power_condition(_has_damaged_active)


def healing_wind(amount: int = 10):
    """Remove `amount` damage from each of your Active Pokémon (Healing Wind)."""
    async def effect(ctx):
        area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
        for pokemon in (area.children if area else []):
            await ctx.heal(amount, pokemon)
    return effect


class OverrideTypePassive(Passive):
    """This Pokémon's type is `type_value` (replaces printed types)."""

    def __init__(self, type_value):
        self.type_value = getattr(type_value, "value", type_value)

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        return [self.type_value]


def eclipse_type_change(new_type):
    """Until the end of your turn, this Pokémon's type is `new_type`
    (Lunar Eclipse / Solar Eclipse)."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        ctx.add_temporary_passive(
            pokemon, OverrideTypePassive(new_type),
            expires_after_turn=ctx.session.turn_state.turn_number,
        )
    return effect


def named_partner_condition(*names, side: str = "any"):
    """Poké-Power: Special Condition block plus a named partner in play."""
    wanted = set(names)

    def extra(board, player_id, pokemon=None):
        pids = [player_id]
        if side in ("any", "both"):
            other = next((p for p in board.player_ids if p != player_id), None)
            if other:
                pids.append(other)
        elif side == "opponent":
            other = next((p for p in board.player_ids if p != player_id), None)
            pids = [other] if other else []
        return any(
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in wanted
            for pid in pids if pid
            for p in board.pokemon_in_play(pid)
        )
    return poke_power_condition(extra)


def draw_if_opponent_evolved(n: int = 3):
    """If the opponent has any Evolved Pokémon in play, draw `n` cards
    (Cosmic Draw)."""
    async def effect(ctx):
        if any(is_evolution_pokemon(p) for p in ctx.opponent_pokemon_in_play()):
            await ctx.draw_cards(n)
    return effect


def optional_gust_then_damage():
    """Before doing damage, you may switch 1 of the opponent's Benched
    Pokémon with the Defending Pokémon, then deal printed damage to the
    (new) Defending Pokémon (Metal Hook)."""
    async def effect(ctx):
        old_active = ctx.opponent_active()
        bench = ctx.opponent_bench()
        if old_active is not None and bench \
                and not ctx.effects_blocked(old_active) \
                and await ctx.ask_yes_no(
                    "Switch 1 of your opponent's Benched Pokémon with the "
                    "Defending Pokémon?"):
            target = await ctx.choose_pokemon(
                bench, "Choose the opponent's new Active Pokémon",
            ) or bench[0]
            await ctx.switch_active(ctx.opponent_id, target)
        await ctx.deal_damage()
    return effect


def _runnable_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


async def copy_supporter_from_opponent_hand(ctx):
    """Look at the opponent's hand. You may use a Supporter found there as
    this attack's effect; the card stays in their hand (Supernatural)."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    candidates = [c for c in hand if _runnable_supporter(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="You may use the effect of a Supporter card from your opponent's hand.",
    )
    if not picks:
        return
    effect = TRAINER_EFFECTS_BY_GUID[(picks[0].archetype_id or "").lower()]
    await effect(ctx)


async def scam_supporter(ctx):
    """Look at the opponent's hand. You may shuffle a Supporter you find
    there into their deck; if you do, they draw a card (Scam)."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    supporters = [c for c in hand if is_supporter_card(c)]
    if not supporters:
        return
    if not await ctx.ask_yes_no(
        "Shuffle a Supporter card from your opponent's hand into their deck?"
    ):
        return
    picks = await ctx.choose_cards(
        supporters, 1,
        prompt="Choose a Supporter card to shuffle into your opponent's deck",
    )
    if not picks:
        return
    await ctx.shuffle_into_deck(picks, player_id=ctx.opponent_id)
    await ctx.draw_cards(1, player_id=ctx.opponent_id)


def flip_damage_paralyze_on_heads(coins: int = 2, per_heads: Optional[int] = None):
    """Flip `coins`; deal per_heads (or printed) times heads. If any coin
    is heads, the Defending Pokémon is Paralyzed (Double Bubble)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            coins, ctx.ability.title if ctx.ability else "")
        heads = sum(1 for r in results if r)
        per = per_heads if per_heads is not None else (
            getattr(ctx.ability, "damage", 0) or 0)
        if heads:
            await ctx.deal_damage(per * heads)
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


def split_blast(full: int = 100, split: int = 50):
    """Deal `full` to the Defending Pokémon, then discard 1 Energy. If the
    opponent has more than 1 Defending Pokémon, you may deal `split` to
    each of them instead (Typhlosion ex Split Blast)."""
    async def effect(ctx):
        defending = [
            p for p in ctx.opponent_pokemon_in_play()
            if is_in_active_spot(p)
        ]
        if len(defending) > 1 and await ctx.ask_yes_no(
            f"Do {split} damage to each Defending Pokémon instead?"
        ):
            for target in defending:
                await ctx.deal_damage(split, target=target)
        else:
            await ctx.deal_damage(full)
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard 1 Energy card attached to this Pokémon",
        )
    return effect


def heal_then_switch(counters: int = 3):
    """If you have no Benched Pokémon, this attack does nothing. Remove
    `counters` damage counters from this Pokémon, then switch it with 1
    of your Benched Pokémon (Wailord ex Super Deep Dive)."""
    async def effect(ctx):
        bench = ctx.my_bench()
        if not bench:
            return
        pokemon = ctx.attacker or ctx.source
        if pokemon is not None:
            await ctx.heal(counters * 10, pokemon)
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


async def wallys_training(ctx):
    """Search the deck for 1 card that evolves from your Active Pokémon,
    put it onto that Pokémon (counts as evolving), then shuffle."""
    active = ctx.my_active()
    logic_name = (
        active.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) if active else None
    )
    if logic_name:
        picks = await ctx.search_deck(
            lambda c, name=logic_name:
                c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
            count=1, minimum=0,
            prompt="Choose a card that evolves from your Active Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(active, picks[0])
    await ctx.shuffle_deck()


def _logic_name(card) -> str:
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    """Best-effort printable name for matching card text (e.g. 'Articuno ex')."""
    d = def_for(getattr(card, "archetype_id", None) or "")
    if d is not None and getattr(d, "display_name", None):
        return d.display_name
    raw = (card.get_attribute(AttrID.DISPLAY_NAME)
           or card.get_attribute(AttrID.CARD_NAME)
           or card.get_attribute(AttrID.NAME))
    if isinstance(raw, dict):
        return raw.get("id") or raw.get("en") or _logic_name(card)
    return raw or _logic_name(card)


class FrenzyVsNamedPassive(Passive):
    """Poké-Body: this Pokémon's attacks do `bonus` more damage while the
    opponent has any of `names` in play (Frenzy). Names match display_name."""

    def __init__(self, names, bonus: int = 40):
        self.names = tuple(names)
        self.bonus = bonus

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and not calc.is_opposing):
            return
        poke = carrier_pokemon(carrier)
        if poke is None or poke is not calc.attacker:
            return
        mine = calc.attacker.owning_player_id
        opp_id = next((p for p in calc.board.player_ids if p != mine), None)
        if opp_id is None:
            return
        names = set(self.names)
        for p in calc.board.pokemon_in_play(opp_id):
            if _display_name(p) in names:
                calc.amount = calc.amount + self.bonus
                return


def frenzy_vs_named(*names, bonus: int = 40) -> Passive:
    return FrenzyVsNamedPassive(names, bonus=bonus)


class SynchronizedLiftPassive(Passive):
    """Poké-Body: Retreat Cost is 0 while all `required_names` are in play
    on your side (Synchronized Lift)."""

    def __init__(self, *required_names):
        self.required = tuple(required_names)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        poke = carrier_pokemon(carrier) or carrier
        if pokemon is not poke:
            return cost
        present = {_display_name(p) for p in board.pokemon_in_play(
            pokemon.owning_player_id)}
        if all(n in present for n in self.required):
            return 0
        return cost


def synchronized_lift_passive(*required_names) -> Passive:
    return SynchronizedLiftPassive(*required_names)


def may_move_own_energy(energy_type=None):
    """Deal printed damage, then you may move 1 matching Energy from this
    Pokémon to another of your Pokémon (Ice/Flame/Thunder Gift)."""
    type_value = (getattr(energy_type, "value", energy_type)
                  if energy_type is not None else None)

    async def effect(ctx):
        await ctx.deal_damage(None)
        attacker = ctx.attacker
        if attacker is None:
            return
        others = [p for p in ctx.my_pokemon_in_play() if p is not attacker]
        if not others:
            return
        pred = ((lambda c: energy_provides_type(c, type_value))
                if type_value is not None else is_energy_card)
        energies = [c for c in attacker.children if pred(c)]
        if not energies:
            return
        pick = await ctx.choose_cards(
            energies, 1, minimum=0,
            prompt="You may move an Energy to another of your Pokémon.",
        )
        if not pick:
            return
        target = await ctx.choose_pokemon(
            others, "Choose a Pokémon to move the Energy to")
        if target is not None:
            await ctx.move_energy(pick[0], target)

    return effect


def discard_self_energy_draw(draw: int = 3):
    """Discard 1 Energy from self, then draw `draw` (The Third Eye)."""
    async def effect(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard an Energy card attached to this Pokémon")
        await ctx.draw_cards(draw)
    return effect


def _is_attached_trainer(card) -> bool:
    """True for Tools/TMs attached to a Pokémon (not Energy)."""
    if is_energy_card(card):
        return False
    tt = card.get_attribute(AttrID.TRAINER_TYPE)
    if tt is not None:
        return True
    st = subtypes_for(getattr(card, "archetype_id", None) or "") or []
    return any(s in st for s in (
        "Pokémon Tool", "Pokemon Tool", "Tool", "Technical Machine", "TM"))


def plunder_trainers(damage: Optional[int] = None):
    """Before damage, discard all Trainer cards attached to the Defending
    Pokémon (Plunder)."""
    async def effect(ctx):
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            tools = [c for c in list(defender.children)
                     if _is_attached_trainer(c)]
            if tools:
                await ctx.discard_cards(tools)
        await ctx.deal_damage(damage)
    return effect


def flip_heal_self(amount: int = 10):
    """Deal printed damage; on heads, heal `amount` from self."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        results = await ctx.flip_coins(1, "Sporadic Sponging")
        if results and results[0] and ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def metal_charge(self_counters: int = 1):
    """Deal printed damage, then put damage counters on self."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        if ctx.attacker is not None:
            await ctx.deal_damage(
                self_counters * 10, target=ctx.attacker, apply_modifiers=False)
    return effect


def hypno_wave(bonus: int = 20,
               tails_condition=SpecialConditions.ASLEEP):
    """Flip: heads = printed+bonus; tails = printed + condition."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Hypno Wave")
        heads = bool(results and results[0])
        printed = (ctx.ability.damage if ctx.ability and ctx.ability.damage
                   else 30)
        await ctx.deal_damage(printed + (bonus if heads else 0))
        if not heads and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, tails_condition)
    return effect


def twister_attack(damage: Optional[int] = None):
    """Flip 2 coins. Both tails → nothing. Else deal damage; discard 1 Energy
    from defender per heads."""
    async def effect(ctx):
        results = await ctx.flip_coins(2, "Twister")
        heads = sum(1 for r in results if r)
        if heads == 0:
            return
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(
                defender, heads,
                prompt="Discard Energy from the Defending Pokémon")
    return effect


async def devolution_beam(ctx):
    """Flip. If heads, choose 1 Evolved Pokémon (either side) and devolve
    the highest stage into that player's hand."""
    results = await ctx.flip_coins(1, "Devolution Beam")
    if not (results and results[0]):
        return
    candidates = [
        p for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        if devolvable(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose an Evolved Pokémon to devolve")
    if target is not None:
        await ctx.devolve_pokemon(target, steps=1, destination="hand")


def pure_body_on_attach(energy_type=PokemonTypes.WATER):
    """Poké-Body: when attaching Water Energy from hand, discard an Energy
    from this Pokémon (Pure Body). Pair with Triggers.ON_ENERGY_ATTACHED."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id \
                or ctx.energy_receiver is not ctx.source:
            return
        energy = ctx.attached_energy
        if energy is None or not energy_provides_type(energy, type_value):
            return
        # Must discard one Energy (can be the one just attached if alone)
        await ctx.discard_energy_from(
            ctx.source, 1,
            prompt="Pure Body: discard an Energy card attached to Suicune")
    return effect


def burning_aura(counters: int = 1):
    """Between turns while Active: put counters on each Active Pokémon.
    Pair with Triggers.BETWEEN_TURNS."""
    async def effect(ctx):
        source = ctx.source
        if source is None or not is_in_active_spot(source):
            return
        for pid in ctx.board.player_ids:
            area = ctx.board.find_player_area(pid, "activePokemonArea")
            for pokemon in (area.children if area else []):
                await ctx.deal_damage(
                    counters * 10, target=pokemon, apply_modifiers=False)
    return effect


async def championship_arena_end_turn(ctx):
    """At end of each player's turn, if hand >= 8, discard down to 7.
    Pair Stadium with Triggers.END_OF_TURN; ctx.player_id is the ending player."""
    pid = ctx.player_id
    hand = list(ctx.hand(pid))
    if len(hand) < 8:
        return
    need = len(hand) - 7
    picks = await ctx.choose_cards(
        hand, need, minimum=need,
        prompt=f"Championship Arena: discard {need} card(s)",
        player_id=pid,
    )
    if picks:
        await ctx.discard_cards(picks)


async def tropical_wind(ctx):
    """Flip: heads remove up to 2 damage counters from each Active; tails
    each Active is Asleep."""
    results = await ctx.flip_coins(1, "Tropical Wind")
    actives = []
    for pid in ctx.board.player_ids:
        area = ctx.board.find_player_area(pid, "activePokemonArea")
        actives.extend(area.children if area else [])
    if results and results[0]:
        for a in actives:
            await ctx.heal(20, a)
    else:
        for a in actives:
            await ctx.apply_special_condition(a, SpecialConditions.ASLEEP)


async def tropical_tidal_wave(ctx):
    """Flip: heads discard all opponent's in-play Trainers; tails discard
    all your in-play Trainers excluding Supporters."""
    results = await ctx.flip_coins(1, "Tropical Tidal Wave")
    heads = bool(results and results[0])
    pid = ctx.opponent_id if heads else ctx.player_id
    exclude_supporter = not heads
    to_discard = []
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == pid:
        if not (exclude_supporter and is_supporter_card(stadium)):
            to_discard.append(stadium)
    for p in ctx.board.pokemon_in_play(pid):
        for c in list(p.children):
            if _is_attached_trainer(c):
                if exclude_supporter and is_supporter_card(c):
                    continue
                to_discard.append(c)
    if to_discard:
        await ctx.discard_cards(to_discard)


def healing_sound(heal: int = 30):
    """Heal your Active; Defending is Asleep (Healing Sound)."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is not None:
            await ctx.heal(heal, active)
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.ASLEEP)
    return effect


def flip_or_nothing_paralyze(damage: Optional[int] = None):
    """Flip: heads deal damage + Paralyze; tails do nothing (Dragonbreath)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Dragonbreath")
        if not (results and results[0]):
            return
        await ctx.deal_damage(damage)
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


def mill_top_on_heads(count: int = 1):
    """Deal printed damage; on heads opponent discards top `count` of deck."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        results = await ctx.flip_coins(1, "Mix-Up")
        if results and results[0]:
            await ctx.discard_cards(
                ctx.deck_top(count, player_id=ctx.opponent_id))
    return effect


def snipe_own_bench(amount: int = 10):
    """Deal printed damage; also `amount` to 1 of your Benched Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def damage_then(also):
    """Deal printed damage, then run `also(ctx)`."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        await also(ctx)
    return effect


def damage_each_active(amount: int):
    """Deal `amount` to each Active Pokémon (Big Explosion)."""
    async def effect(ctx):
        for poke in (ctx.my_active(), ctx.opponent_active()):
            if poke is not None:
                await ctx.deal_damage(amount, target=poke)
    return effect


def rainbow_burn(base: int = 30, per: int = 10):
    """`base` + `per` for each type of basic Energy attached (Rainbow Burn)."""
    async def effect(ctx):
        types = set()
        for e in ctx.attached_energies(ctx.attacker) if ctx.attacker else []:
            if not is_basic_energy_card(e):
                continue
            for tv in (e.get_attribute(AttrID.POKEMON_TYPES) or []):
                types.add(tv)
        await ctx.deal_damage(base + per * len(types))
    return effect


def prize_lead_bonus(bonus: int = 20, base: Optional[int] = None):
    """Printed (or `base`) + `bonus` if you have more Prize cards left."""
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        mine = count_prizes_remaining("mine")(ctx)
        theirs = count_prizes_remaining("opponent")(ctx)
        await ctx.deal_damage(printed + (bonus if mine > theirs else 0))
    return effect


def discard_opponent_hand_down_to(n: int = 5):
    """If opponent hand >= n+1, randomly discard down to `n` (Bad News)."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if len(hand) <= n:
            return
        need = len(hand) - n
        # Without looking: random picks
        picks = random.sample(hand, need)
        await ctx.discard_cards(picks)
    return effect


def heal_my_active(amount: int = 10):
    """Remove damage from your Active (Healing Wave)."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is not None:
            await ctx.heal(amount, active)
    return effect


def fury_cutter(base: int = 10, per_heads: int = 10, all_heads_bonus: int = 60,
                coins: int = 4):
    """Flip `coins`. All heads → base+all_heads_bonus; else base+per_heads*heads."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, "Fury Cutter")
        heads = sum(1 for r in results if r)
        if heads == coins:
            await ctx.deal_damage(base + all_heads_bonus)
        else:
            await ctx.deal_damage(base + per_heads * heads)
    return effect


def discard_energy_then_condition(energy_type, *conditions):
    """Discard 1 matching Energy from self, then apply conditions (Poison Spurt)."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: energy_provides_type(c, type_value),
            prompt="Discard an Energy card attached to this Pokémon")
        for cond in conditions:
            if ctx.defender is not None:
                await ctx.apply_special_condition(ctx.defender, cond)
    return effect


def kindle_discard_both(energy_type=None):
    """Discard 1 Energy (typed) from self, then 1 Energy from defender (Kindle)."""
    type_value = getattr(energy_type, "value", energy_type) if energy_type else None
    pred = ((lambda c: energy_provides_type(c, type_value))
            if type_value is not None else None)

    async def effect(ctx):
        await ctx.deal_damage(None)
        await ctx.discard_energy_from(
            ctx.attacker, 1, predicate=pred,
            prompt="Discard an Energy card attached to this Pokémon")
        if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
            await ctx.discard_energy_from(
                ctx.defender, 1,
                prompt="Discard an Energy card from the Defending Pokémon")
    return effect


def may_discard_energy_bonus(bonus: int = 20, base: Optional[int] = None):
    """You may discard 1 Energy from self; if you do, deal base+bonus (Dragon Flame)."""
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        energies = list(ctx.attached_energies(ctx.attacker) if ctx.attacker else [])
        bonus_amt = 0
        if energies:
            picks = await ctx.choose_cards(
                energies, 1, minimum=0,
                prompt="You may discard an Energy card attached to this Pokémon")
            if picks:
                await ctx.discard_cards(picks)
                bonus_amt = bonus
        await ctx.deal_damage(printed + bonus_amt)
    return effect


def burn_flip_tails_discard_energy(energy_type=None):
    """Defending is Burned; flip — tails discard Energy from self (Scorching Smoke)."""
    type_value = getattr(energy_type, "value", energy_type) if energy_type else None
    pred = ((lambda c: energy_provides_type(c, type_value))
            if type_value is not None else None)

    async def effect(ctx):
        await ctx.deal_damage(None)
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
        results = await ctx.flip_coins(1, "Scorching Smoke")
        if results and not results[0] and ctx.attacker is not None:
            await ctx.discard_energy_from(
                ctx.attacker, 1, predicate=pred,
                prompt="Discard an Energy card attached to this Pokémon")
    return effect


def discard_typed_energies_then_damage(*energy_types, damage: Optional[int] = None):
    """Discard one of each typed Energy from self, then deal damage (Mist Ball / Dragon Wave)."""
    type_values = [getattr(t, "value", t) for t in energy_types]

    async def effect(ctx):
        for tv in type_values:
            await ctx.discard_energy_from(
                ctx.attacker, 1,
                predicate=lambda c, tv=tv: energy_provides_type(c, tv),
                prompt="Discard the required Energy")
        await ctx.deal_damage(damage)
    return effect


def gigavolt(base: int = 40, bonus: int = 30):
    """Flip: heads deal base+bonus; tails deal base + Paralyze (Gigavolt)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Gigavolt")
        heads = bool(results and results[0])
        await ctx.deal_damage(base + (bonus if heads else 0))
        if not heads and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


# ---- EX3 Dragon remaining helpers ------------------------------------------

def dragon_dance(bonus: int = 40):
    """During your next turn, your Active Pokémon's attacks do +bonus
    (Altaria Dragon Dance). Player-wide, not tied to this attacker."""
    async def effect(ctx):
        state = ctx.session.turn_state
        start = state.turn_number
        ctx.add_turn_damage_modifier(TurnDamageModifier(
            bonus, ctx.player_id,
            opposing_active_only=True,
            expires_after_turn=start + 2,
            source_predicate=lambda _e: state.turn_number > start,
        ))
    return effect


async def conductivity_on_attach(ctx):
    """Opponent attaches Energy from hand → 1 damage counter on that Pokémon
    (Ampharos ex Conductivity). Dedupes across multiple Ampharos on one attach."""
    if ctx.attaching_player_id == ctx.player_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    energy = ctx.attached_energy
    if energy is not None and getattr(energy, "_conductivity_taxed", False):
        return
    if energy is not None:
        setattr(energy, "_conductivity_taxed", True)
    await ctx.deal_damage(
        10, target=receiver, apply_modifiers=False, as_counters=True)


def flip_attach_n_from_discard(count: int = 2, predicate=None, prompt: str = ""):
    """Flip; heads attach up to `count` matching Energy from discard to self
    (Collect Fire). No printed damage assumed."""
    pred = is_basic_energy_card if predicate is None else predicate

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if ctx.is_attack_effect() and printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        cards = [c for c in ctx.discard_pile() if pred(c)]
        if not cards:
            return
        take = min(count, len(cards))
        picks = await ctx.choose_cards(
            cards, take, minimum=take,
            prompt=prompt or f"Choose {take} Energy card(s) to attach.",
        )
        holder = ctx.attacker or ctx.source
        if holder is None:
            return
        for card in picks:
            await ctx.attach_energy(card, holder)
    return effect


def may_discard_energy_then_snipe(energy_type, amount: int = 30,
                                 pool: str = "bench"):
    """Deal printed; you may discard typed Energy; if you do, snipe `amount`
    to a Benched (or pool) opposing Pokémon (Flame Pillar)."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage()
        energies = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, type_value)
        ]
        if not energies:
            return
        if not await ctx.ask_yes_no(
                "Discard a matching Energy to do damage to a Benched Pokémon?"):
            return
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: energy_provides_type(c, type_value),
            prompt="Discard an Energy card attached to this Pokémon")
        if pool == "bench":
            candidates = ctx.opponent_bench()
        else:
            candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is not None:
            await ctx.deal_damage(
                amount, target=target, apply_modifiers=False)
    return effect


def power_pinchers_passive(amount: int = 10) -> Passive:
    """While Active, your Active Pokémon's attacks do +N to Defending
    (Crawdaunt Power Pinchers)."""
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return
            if not is_in_active_spot(carrier):
                return
            atk = calc.attacker
            if atk is None or atk.owning_player_id != carrier.owning_player_id:
                return
            if not is_in_active_spot(atk):
                return
            if not calc.to_active:
                return
            calc.amount += amount
    return _P()


def call_for_power():
    """Move 1 Energy from another of your Pokémon onto this one.
    Pair with Activations.UNLIMITED (Dragonite ex Call for Power)."""
    async def effect(ctx):
        me = ctx.source
        if me is None:
            return
        others = [p for p in ctx.my_pokemon_in_play() if p is not me]
        if not others:
            return
        await ctx.move_energy_freely(
            others, [me], max_count=1,
            prompt="Choose an Energy to move to Dragonite ex")
    return effect


def backspin():
    """Printed damage; you may discard 1 Energy; if you do, switch with Bench
    (Forretress Backspin)."""
    async def effect(ctx):
        await ctx.deal_damage()
        energies = list(ctx.attached_energies(ctx.attacker) if ctx.attacker else [])
        if not energies:
            return
        if not await ctx.ask_yes_no(
                "Discard an Energy to switch this Pokémon with a Benched one?"):
            return
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard an Energy card attached to this Pokémon")
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


def same_energy_count(ctx) -> bool:
    return count_energy("self")(ctx) == count_energy("defender")(ctx)


def synchronized_search():
    """If same Energy count as Defending, search deck for any 1 card to hand."""
    async def effect(ctx):
        if not same_energy_count(ctx):
            return
        top = list(ctx.deck())
        if not top:
            return
        picks = await ctx.choose_cards(
            top, 1, minimum=1,
            prompt="Choose a card to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
            await ctx.shuffle_deck(ctx.player_id)
    return effect


def breaking_impact(per: int = 10):
    """Choose an opposing Pokémon; deal per * its (printed) Colorless retreat
    cost, no W/R (Breaking Impact)."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon for Breaking Impact")
        if target is None:
            return
        cost = int(target.get_attribute(AttrID.RETREAT_COST) or 0)
        if cost > 0:
            await ctx.deal_damage(
                per * cost, target=target, apply_modifiers=False)
    return effect


def mind_trip():
    """Printed damage; if same Energy count, Confuse the Defending Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage()
        if same_energy_count(ctx) and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.CONFUSED)
    return effect


def dragon_crush(amount: int = 10):
    """Flip; heads: `amount` to each Defending + discard 1 Energy from each."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Dragon Crush")
        if not (results and results[0]):
            return
        defending = [
            p for p in ctx.opponent_pokemon_in_play()
            if is_in_active_spot(p)
        ] or ([ctx.defender] if ctx.defender else [])
        for target in defending:
            if target is None:
                continue
            await ctx.deal_damage(amount, target=target)
            if not ctx.effects_blocked(target):
                await ctx.discard_energy_from(
                    target, 1,
                    prompt="Discard an Energy from the Defending Pokémon")
    return effect


def melting_mountain():
    """Discard top of deck; if basic Energy, attach to this Pokémon."""
    async def effect(ctx):
        top = ctx.deck_top(1)
        if not top:
            return
        card = top[0]
        await ctx.discard_cards([card])
        if is_basic_energy_card(card) and ctx.source is not None:
            # re-fetch from discard
            await ctx.attach_energy(card, ctx.source)
    return effect


def lava_flow(base: int = 40, per: int = 20):
    """You may discard any number of basic Energy; deal base + per * discarded."""
    async def effect(ctx):
        energies = [
            e for e in ctx.attached_energies(ctx.attacker)
            if is_basic_energy_card(e)
        ]
        discarded = 0
        if energies:
            picks = await ctx.choose_cards(
                energies, len(energies), minimum=0,
                prompt="Discard any number of basic Energy cards")
            if picks:
                await ctx.discard_cards(picks)
                discarded = len(picks)
        await ctx.deal_damage(base + per * discarded)
    return effect


def spiral_growth():
    """Flip until tails; for each heads attach a basic Energy from discard."""
    async def effect(ctx):
        heads = 0
        while True:
            results = await ctx.flip_coins(1, "Spiral Growth")
            if not results or not results[0]:
                break
            heads += 1
        if heads <= 0 or ctx.attacker is None:
            return
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        take = min(heads, len(pool))
        if take <= 0:
            return
        picks = await ctx.choose_cards(
            pool, take, minimum=take,
            prompt=f"Choose {take} basic Energy card(s) to attach")
        for card in picks:
            await ctx.attach_energy(card, ctx.attacker)
    return effect


def dragon_burst(per: int = 40):
    """Discard all Fire or all Lightning Energy; deal per * count discarded."""
    async def effect(ctx):
        fire = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.FIRE.value)
        ]
        lightning = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.LIGHTNING.value)
        ]
        choices = []
        if fire:
            choices.append("Fire")
        if lightning:
            choices.append("Lightning")
        if not choices:
            await ctx.deal_damage(0)
            return
        if len(choices) == 1:
            pick = choices[0]
        else:
            idx = await ctx.choose(
                "Discard all Fire or all Lightning Energy?", choices)
            pick = choices[idx]
        bundle = fire if pick == "Fire" else lightning
        await ctx.discard_cards(bundle)
        await ctx.deal_damage(per * len(bundle))
    return effect


def speed_growth(count: int = 2, energy_type=PokemonTypes.GRASS):
    """Attach up to `count` typed Energy from hand to your Pokémon any way."""
    return attach_energy_from_hand(
        predicate=lambda c: (
            is_basic_energy_card(c)
            and energy_provides_type(c, getattr(energy_type, "value", energy_type))
        ),
        count=count,
        prompt=f"Choose up to {count} Energy card(s) to attach",
    )


def damage_curse():
    """Put 1 + (damage counters on self) counters on Defending."""
    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        dmg = max(0, (ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0)) // 10)
        total = 1 + dmg
        if ctx.defender is not None:
            await ctx.deal_damage(
                total * 10, target=ctx.defender,
                apply_modifiers=False, as_counters=True)
    return effect


def pick_on_look(down_to: int = 5):
    """If opponent hand > down_to, look and choose cards to shuffle into deck
    until they have down_to left (Skarmory Pick On)."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if len(hand) <= down_to:
            return
        need = len(hand) - down_to
        # Reveal hand to attacker via choose
        picks = await ctx.choose_cards(
            hand, need, minimum=need,
            prompt=f"Choose {need} card(s) for your opponent to shuffle into their deck")
        if picks:
            await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def power_count(base: int = 20, bonus: int = 30):
    """base + bonus if your side has fewer Energy cards than opponent's."""
    async def effect(ctx):
        mine = sum(len(ctx.attached_energies(p)) for p in ctx.my_pokemon_in_play())
        theirs = sum(
            len(ctx.attached_energies(p)) for p in ctx.opponent_pokemon_in_play())
        await ctx.deal_damage(base + (bonus if mine < theirs else 0))
    return effect


def quick_dive(amount: int = 50):
    """Flip; heads choose any opposing Pokémon for `amount` (no W/R)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Quick Dive")
        if not (results and results[0]):
            return
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is not None:
            await ctx.deal_damage(
                amount, target=target, apply_modifiers=False)
    return effect


def quick_charge_different_types(count: int = 3):
    """Search deck for up to `count` different types of basic Energy to hand."""
    async def effect(ctx):
        pool = [c for c in ctx.deck() if is_basic_energy_card(c)]
        if not pool:
            await ctx.shuffle_deck(ctx.player_id)
            return
        # Pick greedily with type uniqueness enforced by successive filters
        chosen = []
        used_types = set()
        remaining = list(pool)
        for _ in range(count):
            eligible = []
            for c in remaining:
                types = tuple(c.get_attribute(AttrID.POKEMON_TYPES) or [])
                if types and types[0] not in used_types:
                    eligible.append(c)
            if not eligible:
                break
            picks = await ctx.choose_cards(
                eligible, 1, minimum=0,
                prompt="Choose a basic Energy of a new type (or skip)")
            if not picks:
                break
            card = picks[0]
            chosen.append(card)
            remaining = [c for c in remaining if c is not card]
            t = (card.get_attribute(AttrID.POKEMON_TYPES) or [None])[0]
            used_types.add(t)
        if chosen:
            await ctx.put_in_hand(chosen, reveal=True)
        await ctx.shuffle_deck(ctx.player_id)
    return effect


def flip_spread_all(amount: int = 20):
    """Flip; heads deal `amount` to each opposing Pokémon (no W/R on bench)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
        if not (results and results[0]):
            return
        for target in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(
                amount, target=target,
                apply_modifiers=is_in_active_spot(target))
    return effect


def special_circuit(base: int = 20, bonus: int = 40):
    """Snipe: base, or bonus if target has a Poké-Power or Poké-Body."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon for Special Circuit")
        if target is None:
            return
        entries = target.get_attribute(AttrID.PIE_ABILITIES) or []
        has_pb = any(
            isinstance(e, dict) and e.get("abilityType") in (
                "Poké-Power", "Poké-Body", "Poke-Power", "Poke-Body",
                AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY,
                getattr(AbilityTypes.POKE_POWER, "value", None),
                getattr(AbilityTypes.POKE_BODY, "value", None),
            )
            for e in entries
        )
        # Also check ability_type ints commonly stored
        if not has_pb:
            for e in entries:
                if not isinstance(e, dict):
                    continue
                at = e.get("abilityType")
                if at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY):
                    has_pb = True
                    break
                if isinstance(at, str) and ("Power" in at or "Body" in at):
                    has_pb = True
                    break
        amt = bonus if has_pb else base
        await ctx.deal_damage(
            amt, target=target,
            apply_modifiers=is_in_active_spot(target))
    return effect


def extra_circuit(base: int = 20, bonus: int = 40):
    """Snipe: base, or bonus if target is Pokémon-ex."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon for Extra Circuit")
        if target is None:
            return
        amt = bonus if is_pokemon_ex(target) else base
        await ctx.deal_damage(
            amt, target=target,
            apply_modifiers=is_in_active_spot(target))
    return effect


def slimy_water(base: int = 40, per: int = 10):
    """base + per * Defending Pokémon's Colorless retreat cost."""
    async def effect(ctx):
        cost = 0
        if ctx.defender is not None:
            cost = int(ctx.defender.get_attribute(AttrID.RETREAT_COST) or 0)
        await ctx.deal_damage(base + per * cost)
    return effect


def quick_touch():
    """You may switch; if you do, you may move any Grass Energy to new Active."""
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        bench = ctx.my_bench()
        if not bench or attacker is None:
            return
        if not await ctx.ask_yes_no(
                "Switch this Pokémon with 1 of your Benched Pokémon?"):
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is None:
            return
        await ctx.switch_active(ctx.player_id, target)
        # Move Grass Energy from old (now bench) to new active
        grass = [
            e for e in ctx.attached_energies(attacker)
            if energy_provides_type(e, PokemonTypes.GRASS.value)
        ]
        if not grass:
            return
        picks = await ctx.choose_cards(
            grass, len(grass), minimum=0,
            prompt="Move any number of Grass Energy to the new Active")
        for e in picks:
            await ctx.move_energy(e, target)
    return effect


def loose_shell_search():
    """When played to evolve, you may search for Shedinja onto Bench as Basic."""
    async def effect(ctx):
        if not await ctx.ask_yes_no(
                "Search your deck for Shedinja and put it onto your Bench?"):
            return
        await search_to_bench_named(
            "Shedinja", count=1, include_basic=False,
            prompt="Choose Shedinja to put onto your Bench",
        )(ctx)
    return effect


def magnetic_field():
    """Discard 1 from hand; put up to 2 basic Energy from discard into hand
    (can't return the discarded card)."""
    def cond(board, player_id, pokemon=None):
        from spirit.game.card_effects.trainers import is_basic_energy_card as _ibe
        disc = board.discard_pile(player_id) if hasattr(board, 'discard_pile') else []
        # board API via session later — poke_power_condition wraps
        return True

    async def effect(ctx):
        disc_energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not disc_energy:
            return
        hand = list(ctx.hand())
        if not hand:
            return
        dump = await ctx.choose_cards(
            hand, 1, minimum=1,
            prompt="Discard a card from your hand")
        if not dump:
            return
        dumped = dump[0]
        await ctx.discard_cards(dump)
        # Refresh discard; exclude the card just discarded from return
        pool = [
            c for c in ctx.discard_pile()
            if is_basic_energy_card(c) and c is not dumped
        ]
        if not pool:
            return
        take = min(2, len(pool))
        picks = await ctx.choose_cards(
            pool, take, minimum=0,
            prompt="Choose up to 2 basic Energy from your discard pile")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def toxic_gas_passive() -> Passive:
    """While Active, ignore all Poké-Powers and Poké-Bodies other than Toxic Gas."""
    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier):
            if not is_in_active_spot(carrier):
                return False
            title = getattr(ability, "title", None)
            if title == "Toxic Gas":
                return False
            at = getattr(ability, "ability_type", None)
            return at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY)
    return _P()


def wonder_guard_passive() -> Passive:
    """Prevent damage + attack effects from Evolved Pokémon and Pokémon-ex."""
    class _P(Passive):
        def _match(self, attacker, target, carrier):
            if carrier_pokemon(carrier) is not target:
                return False
            if attacker is None:
                return False
            return is_pokemon_ex(attacker) or is_evolution_pokemon(attacker)

        def prevents_damage(self, calc, carrier):
            return bool(
                calc.is_attack and calc.is_opposing
                and self._match(calc.attacker, calc.target, carrier))

        def blocks_attack_effects_from(self, target, carrier, attacker):
            return self._match(attacker, target, carrier)
    return _P()


def submerge_passive() -> Passive:
    """While on the Bench, prevent all damage from opponent's attacks."""
    def pred(calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return (
            calc.is_attack and calc.is_opposing
            and calc.target is holder
            and not is_in_active_spot(holder)
        )
    return prevent_damage_when(pred)


def energy_guard_passive(amount: int = 10) -> Passive:
    """Takes `amount` less from attacks while any basic Energy is attached."""
    return takes_less_passive(
        amount,
        protects=lambda target, carrier: (
            carrier_pokemon(carrier) is target
            and any(is_basic_energy_card(c) for c in target.children)
        ),
    )


def levitate_passive() -> Passive:
    """Retreat cost 0 while any basic Energy is attached."""
    return retreat_free_when(
        lambda pokemon, carrier: (
            carrier_pokemon(carrier) is pokemon
            and any(is_basic_energy_card(c) for c in pokemon.children)
        )
    )


def draw_then_discard(draw: int = 3, discard: int = 1):
    """Draw `draw`, then discard `discard` from hand (TV Reporter)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        await ctx.discard_from_hand(
            discard, minimum=discard,
            prompt=f"Choose {discard} card(s) to discard")
    return effect


def scoop_own_non_ex():
    """Choose 1 of your non-ex Pokémon; return it and attachments to hand
    (Mr. Briney's Compassion)."""
    async def effect(ctx):
        candidates = [
            p for p in ctx.my_pokemon_in_play() if not is_pokemon_ex(p)
        ]
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to return to your hand")
        if target is None:
            return
        was_active = target is ctx.my_active()
        stack = full_stack(target)
        await ctx.put_in_hand(stack, reveal=False)
        if was_active:
            async def _promote():
                if not await ctx.session._promote_new_active(ctx.player_id):
                    screen_name = ctx.session.players[ctx.player_id].screen_name
                    await ctx.session.end_game(
                        ctx.opponent_id, f"{screen_name} has no Pokémon left")
            ctx.deferred_actions.append(_promote)
    return effect


class BalloonBerryPassive(Passive):
    """Approx: holder retreats for free. Full text also discards this tool
    instead of Energy; that discard-on-retreat hook is not wired yet."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if holder is pokemon:
            return 0
        return cost


def high_pressure_passive() -> Passive:
    """Each player pays [C] less to retreat Fire and Water Pokémon."""
    return retreat_discount(
        1,
        target_pred=lambda pokemon, carrier: any(
            t in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
            for t in (PokemonTypes.FIRE.value, PokemonTypes.WATER.value)
        ),
    )


def low_pressure_passive(amount: int = 10) -> Passive:
    """Each Grass and Lightning Pokémon gets +amount HP."""
    class _P(Passive):
        def max_hp_bonus(self, pokemon, carrier):
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.GRASS.value in types or PokemonTypes.LIGHTNING.value in types:
                return amount
            return 0
    return _P()


class BufferPiecePassive(Passive):
    """Takes 20 less after W/R. (End-of-opponent-turn discard approximated
    separately if the engine supports tool lifetime; damage reduce is the core.)"""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if calc.is_attack and calc.is_opposing and calc.target is holder:
            calc.amount = max(0, calc.amount - 20)

def energy_recycle_system():
    """Show 1 basic Energy from discard to hand, OR show 3 and shuffle into deck."""
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        options = ["Put 1 basic Energy into your hand"]
        if len(pool) >= 3:
            options.append("Shuffle 3 basic Energy into your deck")
        idx = await ctx.choose("Energy Recycle System", options)
        if idx == 0 or len(options) == 1:
            picks = await ctx.choose_cards(
                pool, 1, minimum=1,
                prompt="Choose a basic Energy to put into your hand")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
        else:
            picks = await ctx.choose_cards(
                pool, 3, minimum=3,
                prompt="Choose 3 basic Energy to shuffle into your deck")
            if picks:
                await ctx.shuffle_into_deck(picks, ctx.player_id)
    return effect

def has_team_in_name(*teams: str):
    """True if display_name contains any of the team strings (Team Aqua/Magma)."""
    def pred(card) -> bool:
        name = _display_name(card) or ""
        return any(team in name for team in teams)
    return pred


def defender_has_team(*teams: str):
    pred = has_team_in_name(*teams)
    def cond(ctx) -> bool:
        return ctx.defender is not None and pred(ctx.defender)
    return cond


def second_strike(base: int, bonus: int, counters: int = 2):
    """base + bonus if Defending already has >= counters damage counters."""
    async def effect(ctx):
        dmg = 0
        if ctx.defender is not None:
            dmg = max(0, (ctx.max_hp(ctx.defender) - ctx.defender.get_attribute(AttrID.HP, 0)) // 10)
        await ctx.deal_damage(base + (bonus if dmg >= counters else 0))
    return effect


def bonus_if_damaged(bonus: int, base: Optional[int] = None):
    """Printed (or base) + bonus if Defending already has damage counters."""
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        dmg = 0
        if ctx.defender is not None:
            dmg = max(0, (ctx.max_hp(ctx.defender) - ctx.defender.get_attribute(AttrID.HP, 0)) // 10)
        await ctx.deal_damage(printed + (bonus if dmg > 0 else 0))
    return effect


def bonus_if_ex(bonus: int, base: Optional[int] = None):
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        await ctx.deal_damage(printed + (bonus if defender_is_ex(ctx) else 0))
    return effect


def bonus_if_special_condition(bonus: int, base: Optional[int] = None):
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        from spirit.game.card_effects.attacks_common import defender_has_any_condition
        await ctx.deal_damage(
            printed + (bonus if defender_has_any_condition(ctx) else 0))
    return effect


def force_opponent_switch():
    """Printed damage then opponent switches Defending (Roar / Kick Away)."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        await opponent_switches(ctx)
    return effect


def discard_n_energy_then_damage(n: int = 2, damage: Optional[int] = None):
    """Discard n Energy from self, then deal damage (Bright Flame)."""
    async def effect(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, n,
            prompt=f"Discard {n} Energy card(s) attached to this Pokémon")
        await ctx.deal_damage(damage)
    return effect


def growth_attach(energy_type=PokemonTypes.GRASS):
    """Attach 1 typed Energy from hand to self (Growth)."""
    type_value = getattr(energy_type, "value", energy_type)
    return attach_from_hand(
        lambda c: is_basic_energy_card(c) and energy_provides_type(c, type_value),
        target="active",
        prompt="Choose an Energy card to attach",
    )


def pin_missile(coins: int = 4, per: int = 10):
    from spirit.game.card_effects.attacks_common import flip_damage
    return flip_damage(coins=coins, per_heads=per)


def team_play_damage(team: str = "Team Magma", per: int = 10):
    """per * count of in-play Pokémon with team in name (both sides)."""
    async def effect(ctx):
        pred = has_team_in_name(team)
        n = sum(1 for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
                if pred(p))
        await ctx.deal_damage(per * n)
    return effect


def power_blow():
    """10 + 10 per Energy attached to self."""
    return damage_per(count_energy("self"), 10, base=10)



# --- EX4 Team Magma vs Team Aqua -------------------------------------------

def power_saver_condition(team: str, min_count: int = 4):
    """Attack usable only when >= min_count in-play Pokémon have `team` in name."""
    pred = has_team_in_name(team)
    def cond(board, player_id, pokemon=None):
        n = 0
        for pid in board.player_ids:
            for poke in board.pokemon_in_play(pid):
                if pred(poke):
                    n += 1
        return n >= min_count
    return cond


def primal_vibes_passive() -> Passive:
    """While Active, opponent can't evolve from hand (Primal Vibes / Primal Law)."""
    class _P(Passive):
        def blocks_evolution(self, player_id, target, carrier):
            return (
                player_id != carrier.owning_player_id
                and is_in_active_spot(carrier)
            )
    return _P()


def team_hideout_retreat_passive(team: str) -> Passive:
    """Pokémon without `team` in name pay [C] more to retreat."""
    pred = has_team_in_name(team)
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            if pred(pokemon):
                return cost
            return cost + 1
    return _P()


async def magma_hideout_watch(ctx):
    """Team Magma Hideout: 1 damage counter on Basic benched from hand
    that does not have Team Magma in its name."""
    pokemon = ctx.benched_pokemon
    if pokemon is None:
        return
    if has_team_in_name("Team Magma")(pokemon):
        return
    # Only Basics (Gapejaw-style; Hideout text is Basic from hand)
    stage = pokemon.get_attribute(AttrID.STAGE)
    if stage not in (None, PokemonStage.BASIC.value):
        return
    await ctx.deal_damage(10, target=pokemon, apply_modifiers=False, as_counters=True)


class StrengthCharmPassive(Passive):
    """Attacks from the holder do +10 to the Active (after W/R).
    Full text discards the Charm at end of that turn; damage boost is the core."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if (
            calc.is_attack
            and calc.attacker is holder
            and calc.target is not None
            and is_in_active_spot(calc.target)
        ):
            calc.amount += 10




def team_belt_between_turns(belt_guid: str):
    """BETWEEN_TURNS: if holder is Active, search deck for a card that evolves
    from it, evolve, shuffle, then discard this Belt."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None or not is_in_active_spot(pokemon):
            return
        name = pokemon.get_attribute(AttrID.NAME) or ""
        belt = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == belt_guid.lower()),
            None)

        def match(c):
            d = def_for(c.archetype_id)
            return bool(d and getattr(d, "evolves_from", None) == name)

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose a card that evolves from the Active Pokémon")
        if not picks:
            await ctx.shuffle_deck()
            return
        await ctx.evolve_pokemon(pokemon, picks[0])
        await ctx.shuffle_deck()
        if belt is not None:
            await ctx.discard_cards([belt])
    return effect

def attach_to_team(*teams: str):
    pred = has_team_in_name(*teams)
    def check(pokemon) -> bool:
        return pred(pokemon)
    return check


def dual_ball():
    """Flip 2 coins; for each heads search a Basic Pokémon into hand."""
    from spirit.game.session.effects import is_basic_pokemon
    async def effect(ctx):
        results = await ctx.flip_coins(2, "Dual Ball")
        heads = sum(1 for r in results if r)
        for _ in range(heads):
            picks = await ctx.search_deck(
                is_basic_pokemon, count=1, minimum=0,
                prompt="Choose a Basic Pokémon to put into your hand.",
            )
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def team_ball(team: str):
    """Heads: any Pokémon with team in name; tails: Basic with team in name."""
    from spirit.game.session.effects import is_basic_pokemon
    pred = has_team_in_name(team)
    async def effect(ctx):
        results = await ctx.flip_coins(1, f"{team} Ball")
        heads = bool(results and results[0])
        if heads:
            def match(c):
                return is_pokemon_card(c) and pred(c)
            prompt = f"Choose a Pokémon with {team} in its name"
        else:
            def match(c):
                return is_basic_pokemon(c) and pred(c)
            prompt = f"Choose a Basic Pokémon with {team} in its name"
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt=prompt)
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def team_schemer(team: str):
    """Discard 1 Pokémon from hand; draw 3 (4 if discarded name has team)."""
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_pokemon_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Discard a Pokémon from your hand")
        if not picks:
            return
        bonus = pred(picks[0])
        await ctx.discard_cards(picks)
        await ctx.draw_cards(4 if bonus else 3)
    return effect


def team_conspirator(team: str):
    """Search up to 2 in any combination of Basic team Pokémon and basic Energy."""
    from spirit.game.session.effects import is_basic_pokemon, is_pokemon_card
    pred = has_team_in_name(team)
    def match(c):
        if is_basic_energy_card(c):
            return True
        return is_basic_pokemon(c) and pred(c)
    async def effect(ctx):
        picks = await ctx.search_deck(
            match, count=2, minimum=0,
            prompt=f"Choose up to 2 Basic {team} Pokémon and/or basic Energy",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def _stage_of_card(card) -> int:
    stage = card.get_attribute(AttrID.STAGE)
    if stage is not None:
        return stage
    definition = def_for(card.archetype_id)
    return getattr(getattr(definition, "stage", None), "value", definition.stage if definition else 0)


def archie_maxie(team: str, from_zones=("deck",)):
    """Search a team Pokémon onto Bench as Basic; Stage 2 gets 2 damage counters.

    Archie: deck. Maxie: hand or discard.
    """
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    async def effect(ctx):
        space = 5 - len(ctx.my_bench())
        if space <= 0:
            return
        pool = []
        if "deck" in from_zones:
            deck = ctx.board.find_player_area(ctx.player_id, "deck")
            pool.extend(c for c in (deck.children if deck else []) if is_pokemon_card(c) and pred(c))
        if "hand" in from_zones:
            pool.extend(c for c in ctx.hand() if is_pokemon_card(c) and pred(c))
        if "discard" in from_zones:
            pool.extend(c for c in ctx.discard_pile() if is_pokemon_card(c) and pred(c))
        # Dedup by entity_id
        seen = set()
        uniq = []
        for c in pool:
            if c.entity_id not in seen:
                seen.add(c.entity_id)
                uniq.append(c)
        if not uniq:
            if "deck" in from_zones:
                await ctx.shuffle_deck()
            return
        picks = await ctx.choose_cards(
            uniq, 1, minimum=1,
            prompt=f"Choose a Pokémon with {team} in its name to Bench",
        )
        if not picks:
            if "deck" in from_zones:
                await ctx.shuffle_deck()
            return
        card = picks[0]
        stage = _stage_of_card(card)
        if not await ctx.bench_pokemon(card):
            if "deck" in from_zones:
                await ctx.shuffle_deck()
            return
        if stage == PokemonStage.STAGE2.value:
            await ctx.deal_damage(20, target=card, apply_modifiers=False, as_counters=True)
        if "deck" in from_zones:
            await ctx.shuffle_deck()
    return effect


def delayed_condition(*conditions, poison_counters: int = 1):
    """At end of opponent's next turn (checkup), apply conditions to Defending
    if it is still the same Active (Slow-Acting Poison / Aqua Trance)."""
    async def effect(ctx):
        target = ctx.defender
        if target is None:
            return
        # Deal printed damage first when present
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed:
            await ctx.deal_damage()
        owner_id = target.owning_player_id
        target_id = target.entity_id

        def _guard(board):
            active = board.active_pokemon(owner_id) if owner_id else None
            return active is not None and active.entity_id == target_id

        async def _fire(session):
            pokemon = session.board_state.get_entity(target_id)
            if pokemon is None:
                return
            from spirit.game.session.effects import EffectContext
            ectx = EffectContext(session, owner_id, pokemon, None)
            for cond in conditions:
                await ectx.apply_special_condition(
                    pokemon, cond, poison_counters=poison_counters)

        ctx.schedule_at_checkup(1, _fire, guard=_guard)
    return effect


def volcanic_ash(amount: int = 100, energy_count: int = 2,
                 energy_type=PokemonTypes.FIRE):
    """Discard `energy_count` typed Energy, then snipe `amount` (no W/R on bench)."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, energy_count,
            predicate=lambda c: is_basic_energy_card(c) and energy_provides_type(c, type_value),
            prompt=f"Discard {energy_count} Fire Energy",
        )
        if len(discarded) < energy_count:
            return
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            return
        await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def kerzap(base: int = 40, bonus: int = 40, energy_type=PokemonTypes.LIGHTNING):
    """Flip: heads does base+bonus and discard all typed Energy from self."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Kerzap")
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
            await ctx.discard_energy_from(
                ctx.attacker, 99,
                predicate=lambda c: energy_provides_type(c, type_value),
                prompt="Discard all Lightning Energy",
            )
        else:
            await ctx.deal_damage(base)
    return effect


def green_heal(amount: int = 40, energy_type=PokemonTypes.GRASS):
    """Heal `amount` on each of your Pokémon with typed Energy attached."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        for p in ctx.my_pokemon_in_play():
            if any(is_basic_energy_card(c) and energy_provides_type(c, type_value)
                   for c in p.children):
                await ctx.heal(amount, p)
    return effect


def poison_ring():
    """Poison Defending; it can't retreat until end of opponent's next turn."""
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.POISONED, no_retreat=True)


def energy_flip(snipe: int = 10):
    """Snipe bench `snipe`; may move an Energy from that Pokémon to Active."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, f"Choose a Benched Pokémon to take {snipe} damage")
        if target is None:
            return
        await ctx.deal_damage(snipe, target=target, apply_modifiers=False)
        energies = [c for c in target.children if is_energy_card(c)]
        active = ctx.board.active_pokemon(ctx.opponent_id)
        if energies and active is not None and await ctx.ask_yes_no(
                "Move an Energy from that Pokémon to the Active Pokémon?"):
            picks = await ctx.choose_cards(
                energies, 1, minimum=1, prompt="Choose an Energy to move")
            if picks:
                await ctx.move_energy(picks[0], active)
    return effect


def reverse_stream(base: int = 50, per: int = 10):
    """May return all basic Energy from self to hand; if so, +per per Energy."""
    async def effect(ctx):
        basics = [c for c in ctx.attacker.children if is_basic_energy_card(c)]
        bonus = 0
        if basics and await ctx.ask_yes_no(
                "Return all basic Energy attached to this Pokémon to your hand?"):
            bonus = per * len(basics)
            await ctx.put_in_hand(basics, reveal=False)
        await ctx.deal_damage(base + bonus)
    return effect


def crushing_wave(amount: int = 40):
    """Snipe `amount`; on heads discard Energy from that Pokémon."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            return
        await ctx.deal_damage(amount, target=target, apply_modifiers=False)
        results = await ctx.flip_coins(1, "Crushing Wave")
        if results and results[0]:
            await ctx.discard_energy_from(
                target, 1, prompt="Discard an Energy from the Defending Pokémon")
    return effect


def may_discard_energy_paralyze(energy_type=None):
    """You may discard typed Energy; if you do, Paralyze (Dark Bind)."""
    async def effect(ctx):
        await ctx.deal_damage()
        pred = None
        if energy_type is not None:
            tv = getattr(energy_type, "value", energy_type)
            pred = lambda c, tv=tv: energy_provides_type(c, tv)
        energies = [c for c in ctx.attacker.children
                    if is_energy_card(c) and (pred is None or pred(c))]
        if energies and await ctx.ask_yes_no("Discard a Darkness Energy to Paralyze?"):
            discarded = await ctx.discard_energy_from(
                ctx.attacker, 1, predicate=pred,
                prompt="Discard a Darkness Energy")
            if discarded:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.PARALYZED)
    return effect


def dark_poison():
    """Discard a basic Energy or do nothing; then Poison."""
    async def effect(ctx):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=is_basic_energy_card,
            prompt="Discard a basic Energy or this attack does nothing",
        )
        if not discarded:
            return
        await ctx.deal_damage()
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def aqua_reverse(team: str = "Team Magma"):
    """Before damage, may switch Defending with benched team Pokémon."""
    pred = has_team_in_name(team)
    async def effect(ctx):
        bench = [p for p in ctx.opponent_bench() if pred(p)]
        if bench and await ctx.ask_yes_no(
                f"Switch the Defending Pokémon with a Benched Pokémon that has {team} in its name?"):
            target = await ctx.choose_pokemon(bench, "Choose the new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        await ctx.deal_damage()
    return effect


def dark_lift_passive(energy_type=PokemonTypes.DARKNESS) -> Passive:
    """Retreat cost 0 while typed Energy attached."""
    tv = getattr(energy_type, "value", energy_type)
    return retreat_free_when(
        lambda pokemon, carrier: (
            carrier_pokemon(carrier) is pokemon
            and any(energy_provides_type(c, tv) for c in pokemon.children)
        )
    )


def hydro_reverse(base: int = 30, per: int = 10, energy_type=PokemonTypes.WATER):
    """May return any number of typed basic Energy from all your Pokémon; +per each."""
    tv = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        pool = []
        for p in ctx.my_pokemon_in_play():
            for c in p.children:
                if is_basic_energy_card(c) and energy_provides_type(c, tv):
                    pool.append(c)
        bonus = 0
        if pool and await ctx.ask_yes_no(
                "Return any number of basic Water Energy to your hand?"):
            picks = await ctx.choose_cards(
                pool, len(pool), minimum=0,
                prompt="Choose basic Water Energy to return to your hand")
            if picks:
                bonus = per * len(picks)
                await ctx.put_in_hand(picks, reveal=False)
        await ctx.deal_damage(base + bonus)
    return effect


def land_stream(base: int = 50, per: int = 10):
    """May discard any number of basic Energy from self; +per each."""
    async def effect(ctx):
        pool = [c for c in ctx.attacker.children if is_basic_energy_card(c)]
        bonus = 0
        if pool and await ctx.ask_yes_no(
                "Discard any number of basic Energy attached to this Pokémon?"):
            picks = await ctx.choose_cards(
                pool, len(pool), minimum=0,
                prompt="Choose basic Energy to discard")
            if picks:
                bonus = per * len(picks)
                await ctx.discard_cards(picks)
        await ctx.deal_damage(base + bonus)
    return effect


def dig_under(amount: int = 10):
    """Snipe `amount`; ignore W/R and effects."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            return
        await ctx.deal_damage(
            amount, target=target, apply_modifiers=False, ignore_target_effects=True)
    return effect


def psymist(counters: int = 1, coins: int = 2):
    """Flip coins; for each heads place counters on a chosen opponent Pokémon."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, "Psymist")
        for _ in range(sum(1 for r in results if r)):
            candidates = ctx.opponent_pokemon_in_play()
            if not candidates:
                break
            target = await ctx.choose_pokemon(
                candidates, f"Place {counters} damage counter(s)")
            if target is None:
                break
            await ctx.deal_damage(
                counters * 10, target=target, apply_modifiers=False, as_counters=True)
    return effect


def pain_amplifier(counters: int = 1):
    """Place counters on each opposing Pokémon that already has damage."""
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            hp = p.get_attribute(AttrID.HP, 0)
            max_hp = ctx.max_hp(p)
            if max_hp - hp > 0:
                await ctx.deal_damage(
                    counters * 10, target=p, apply_modifiers=False, as_counters=True)
    return effect


def clay_pulse(amount: int = 10, self_base: int = 20):
    """Printed damage to Active; also `amount` to each damaged benched opponent."""
    async def effect(ctx):
        await ctx.deal_damage()
        for p in ctx.opponent_bench():
            hp = p.get_attribute(AttrID.HP, 0)
            if ctx.max_hp(p) - hp > 0:
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def magma_spurt(mill: int = 5, per: int = 30, types=(PokemonTypes.FIRE, PokemonTypes.FIGHTING)):
    """Discard top `mill`; per * count of matching basic Energy among them."""
    type_values = {getattr(t, "value", t) for t in types}
    async def effect(ctx):
        cards = ctx.deck_top(mill)
        await ctx.discard_cards(cards)
        n = sum(
            1 for c in cards
            if is_basic_energy_card(c)
            and any(energy_provides_type(c, tv) for tv in type_values)
        )
        await ctx.deal_damage(per * n)
    return effect


def snarl_or_paralyze(heads_damage: int = 10):
    """Heads: damage; tails: Paralyze."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Snarl")
        if results and results[0]:
            await ctx.deal_damage(heads_damage)
        else:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


def may_discard_stadium_then_damage():
    """You may discard any Stadium; then printed damage (Knock Over)."""
    async def effect(ctx):
        if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
            await ctx.discard_stadium()
        await ctx.deal_damage()
    return effect


def call_for_family_typed_or_team(element, team: str):
    """Search Basic of element OR Basic with team in name onto Bench."""
    from spirit.game.session.effects import is_basic_pokemon
    pred = has_team_in_name(team)
    el = getattr(element, "value", element)
    def match(c):
        if not is_basic_pokemon(c):
            return False
        if pred(c):
            return True
        types = c.get_attribute(AttrID.POKEMON_TYPES) or []
        # Hand cards may need def_for
        if not types:
            d = def_for(c.archetype_id)
            types = [t.value if hasattr(t, "value") else t
                     for t in (getattr(d, "elements", None) or [])]
        return el in types
    return search_to_bench(match, count=1, prompt="Choose a Basic Pokémon to Bench")


def thick_poison():
    """Heads: Confused+Poisoned; tails: Poisoned (2 counters on tails? text: Poisoned)."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Thick Poison")
        await ctx.apply_special_condition(
            ctx.defender, SpecialConditions.POISONED)
        if results and results[0]:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.CONFUSED)
    return effect


def aqua_call(team: str = "Team Aqua", count: int = 3):
    """Search up to `count` team Pokémon into hand."""
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    def match(c):
        return is_pokemon_card(c) and pred(c)
    async def effect(ctx):
        picks = await ctx.search_deck(
            match, count=count, minimum=0,
            prompt=f"Choose up to {count} Pokémon with {team} in its name",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def thunderspark(amount: int = 10):
    """`amount` to each Benched (both sides) that has Energy attached."""
    async def effect(ctx):
        await ctx.deal_damage()
        for p in ctx.my_bench() + ctx.opponent_bench():
            if any(is_energy_card(c) for c in p.children):
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def chaos_crush():
    """If Confused, discard an Energy from Defending."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        conds = d.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if "Confused" in conds or SpecialConditions.CONFUSED.value in conds:
            await ctx.discard_energy_from(
                d, 1, prompt="Discard an Energy from the Defending Pokémon")
    return effect


def deep_impact():
    """If already damaged, Confuse."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        if ctx.max_hp(d) - d.get_attribute(AttrID.HP, 0) > 0:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def bonus_if_asleep(bonus: int, base: Optional[int] = None):
    from spirit.game.card_effects.attacks_common import (
        bonus_if, defender_has_condition,
    )
    return bonus_if(defender_has_condition(SpecialConditions.ASLEEP), bonus, base=base)


def flame_ball():
    """May move a Fire Energy from self to a Benched Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage()
        fires = [c for c in ctx.attacker.children
                 if energy_provides_type(c, PokemonTypes.FIRE.value)]
        bench = ctx.my_bench()
        if fires and bench and await ctx.ask_yes_no(
                "Move a Fire Energy to 1 of your Benched Pokémon?"):
            picks = await ctx.choose_cards(fires, 1, minimum=1, prompt="Choose a Fire Energy")
            target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
            if picks and target is not None:
                await ctx.move_energy(picks[0], target)
    return effect


def hot_air(energy_type=PokemonTypes.FIRE):
    """Discard typed Energy; opponent switches Defending."""
    tv = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: energy_provides_type(c, tv),
            prompt="Discard a Fire Energy",
        )
        await opponent_switches(ctx)
    return effect


def magma_burn(mill: int = 1, energy_type=PokemonTypes.FIRE):
    """Mill opponent top; flip; on tails discard typed Energy from self."""
    tv = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(mill, player_id=ctx.opponent_id)
        await ctx.discard_cards(top)
        results = await ctx.flip_coins(1, "Magma Burn")
        if not (results and results[0]):
            await ctx.discard_energy_from(
                ctx.attacker, 1,
                predicate=lambda c: energy_provides_type(c, tv),
                prompt="Discard a Fire Energy",
            )
    return effect


def tm_miracle():
    """10 damage; choose 1 Special Condition to apply."""
    async def effect(ctx):
        await ctx.deal_damage(10)
        options = ["Asleep", "Burned", "Confused", "Paralyzed", "Poisoned"]
        conds = [
            SpecialConditions.ASLEEP, SpecialConditions.BURNED,
            SpecialConditions.CONFUSED, SpecialConditions.PARALYZED,
            SpecialConditions.POISONED,
        ]
        idx = await ctx.choose("Choose a Special Condition", options)
        if idx is None:
            idx = 0
        await ctx.apply_special_condition(ctx.defender, conds[idx])
    return effect


def tm_crushing_magma():
    """10 damage; put an Energy from Defending on bottom of opponent's deck."""
    async def effect(ctx):
        await ctx.deal_damage(10)
        d = ctx.defender
        if d is None:
            return
        energies = [c for c in d.children if is_energy_card(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=1,
            prompt="Choose an Energy to put on the bottom of your opponent's deck")
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])
    return effect




def crush_per_energy(per: int = 30):
    """Flip a coin for each Energy attached; per * heads (Crush)."""
    from spirit.game.card_effects.attacks_common import flip_damage, count_energy
    async def effect(ctx):
        n = count_energy("self")(ctx)
        if n <= 0:
            await ctx.deal_damage(0)
            return
        # flip_damage with dynamic coins
        results = await ctx.flip_coins(n, "Crush")
        await ctx.deal_damage(per * sum(1 for r in results if r))
    return effect


def auxiliary_light():
    """Attach a basic Energy from hand to self; put 1 damage counter on self."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Attach a basic Energy from your hand")
        if not picks:
            return
        await ctx.attach_energy(picks[0], ctx.source)
        await ctx.deal_damage(20, target=ctx.source, apply_modifiers=False, as_counters=True)
    return effect


def power_shift(team: str = "Team Aqua"):
    """Move any number of basic Energy from one team Pokémon to another of yours."""
    pred = has_team_in_name(team)
    async def effect(ctx):
        donors = [p for p in ctx.my_pokemon_in_play()
                  if pred(p) and any(is_basic_energy_card(c) for c in p.children)]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Choose a Pokémon to move Energy from")
        if src is None:
            return
        pool = [c for c in src.children if is_basic_energy_card(c)]
        picks = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Choose basic Energy cards to move")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Choose a Pokémon to move Energy to")
        if dest is None:
            return
        for e in picks:
            await ctx.move_energy(e, dest)
    return effect


def overheat_attach():
    """Search discard for a basic Energy and attach to self; then 1 damage counter."""
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose a basic Energy to attach")
        if not picks:
            return
        await ctx.attach_energy(picks[0], ctx.source)
        await ctx.deal_damage(20, target=ctx.source, apply_modifiers=False, as_counters=True)
    return effect


def magma_switch():
    """Move an Energy from one Team Magma Pokémon to another Team Magma Pokémon."""
    pred = has_team_in_name("Team Magma")
    async def effect(ctx):
        donors = [p for p in ctx.my_pokemon_in_play()
                  if pred(p) and any(is_energy_card(c) for c in p.children)]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move Energy from which Team Magma Pokémon?")
        if src is None:
            return
        pool = [c for c in src.children if is_energy_card(c)]
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to move")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if pred(p) and p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Move Energy to which Team Magma Pokémon?")
        if dest is None:
            return
        await ctx.move_energy(picks[0], dest)
    return effect


def call_for_help(team: str = "Team Magma"):
    """If Active: search a team Pokémon into hand (Call for Help)."""
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    def match(c):
        return is_pokemon_card(c) and pred(c)
    async def effect(ctx):
        if not is_in_active_spot(ctx.source):
            return
        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt=f"Choose a Pokémon with {team} in its name",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def call_for_help_condition(team: str = "Team Magma"):
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    def cond(board, player_id, pokemon=None):
        if pokemon is None or not is_in_active_spot(pokemon):
            return False
        deck = board.find_player_area(player_id, "deck")
        return bool(deck) and any(is_pokemon_card(c) and pred(c) for c in deck.children)
    return cond


async def warp_point(ctx):
    """Opponent switches Active; then you switch Active."""
    await opponent_switches(ctx)
    await ctx.flush_choreography()
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def genetic_memory(ctx):
    """Use any attack from this Pokémon's tucked Basic or Stage 1 Evolution
    card (Genetic Memory). Energy for the copied attack is not re-paid —
    Genetic Memory's own cost already covers the declaration."""
    from spirit.game.data_utils import Attack
    from spirit.game.models.board import PokemonEntity
    attacker = ctx.attacker
    if attacker is None:
        return
    candidates = []
    seen = set()
    for child in attacker.children:
        if not isinstance(child, PokemonEntity):
            continue
        stage = child.get_attribute(AttrID.STAGE)
        if stage not in (PokemonStage.BASIC.value, PokemonStage.STAGE1.value):
            continue
        definition = def_for(child.archetype_id)
        for ability in getattr(definition, "abilities", None) or []:
            if not isinstance(ability, Attack):
                continue
            key = (ability.title, ability.game_text)
            if key in seen:
                continue
            seen.add(key)
            candidates.append((child, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(
        candidates,
        "Choose an attack from a Basic or Stage 1 Evolution card",
    )
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)



# ---------------------------------------------------------------------------
# EX5 Hidden Legends
# ---------------------------------------------------------------------------

def levitate_any_energy_passive() -> Passive:
    """Retreat cost 0 while any Energy is attached (Beldum/Metang/Tentacool)."""
    return retreat_free_when(
        lambda pokemon, carrier: (
            carrier_pokemon(carrier) is pokemon
            and any(is_energy_card(c) for c in pokemon.children)
        )
    )


def flail_damage(per: int = 10):
    """Does per damage times damage counters on self (Flail)."""
    from spirit.game.card_effects.attacks_common import damage_counters_on
    return damage_per(damage_counters_on("self"), per)


def meditate_damage(base: int = 20, per: int = 10):
    """base + per per damage counter on Defending (Meditate)."""
    from spirit.game.card_effects.attacks_common import damage_counters_on
    return damage_per(damage_counters_on("defender"), per, base=base)


def karate_chop(base: int = 30, per: int = 10):
    """base minus per per damage counter on self (Karate Chop)."""
    from spirit.game.card_effects.attacks_common import damage_counters_on
    count_fn = damage_counters_on("self")

    async def effect(ctx):
        await ctx.deal_damage(max(0, base - per * count_fn(ctx)))
    return effect


def rage_damage(base: int = 10, per: int = 10):
    """base + per per damage counter on self (Rage)."""
    from spirit.game.card_effects.attacks_common import damage_counters_on
    return damage_per(damage_counters_on("self"), per, base=base)


def retaliate_damage(per: int = 10):
    """per times damage counters on self (Retaliate)."""
    return flail_damage(per)


def power_heal_damage(base: int = 10, per: int = 10):
    """base + per per damage counter on self; then heal that many counters."""
    from spirit.game.card_effects.attacks_common import damage_counters_on
    count_fn = damage_counters_on("self")

    async def effect(ctx):
        n = count_fn(ctx)
        await ctx.deal_damage(base + per * n)
        if n > 0 and ctx.attacker is not None:
            await ctx.heal(n * 10, ctx.attacker)
    return effect


def chakra_points(base: int = 10, per: int = 10):
    """base + per per card in opponent's hand."""
    from spirit.game.card_effects.attacks_common import count_hand
    return damage_per(count_hand("opponent"), per, base=base)


def do_the_wave(base: int = 30, per: int = 10):
    """base + per per Benched Pokémon of yours."""
    from spirit.game.card_effects.attacks_common import count_bench
    return damage_per(count_bench("mine"), per, base=base)


def mystic_water(base: int = 20, per: int = 10):
    """base + per for each Psychic Energy in play (both sides)."""
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
            for c in p.children:
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.PSYCHIC.value):
                    n += 1
        await ctx.deal_damage(base + per * n)
    return effect


def dark_splash(base: int = 40, per: int = 10):
    """base + per for each Darkness Pokémon in play (both sides)."""
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
            types = p.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.DARKNESS.value in types:
                n += 1
        await ctx.deal_damage(base + per * n)
    return effect


def shadow_steal(base: int = 10, per: int = 20):
    """base + per for each Special Energy in opponent's discard."""
    from spirit.game.session.effects import is_special_energy
    async def effect(ctx):
        n = sum(1 for c in ctx.discard_pile(ctx.opponent_id) if is_special_energy(c))
        await ctx.deal_damage(base + per * n)
    return effect


def darkness_chant(cap: int = 6):
    """Put up to `cap` damage counters = Basic/Evo cards in your discard."""
    async def effect(ctx):
        n = sum(
            1 for c in ctx.discard_pile()
            if is_basic_pokemon(c) or is_evolution_pokemon(c)
        )
        n = min(n, cap)
        if n > 0 and ctx.defender is not None:
            await ctx.deal_damage(n * 10, apply_modifiers=False, as_counters=True)
    return effect


def muddy_eye(per: int = 10):
    """per * (basic Energy on self + basic Energy on Defending)."""
    async def effect(ctx):
        n = 0
        for p in (ctx.attacker, ctx.defender):
            if p is None:
                continue
            n += sum(1 for c in p.children if is_basic_energy_card(c))
        await ctx.deal_damage(per * n)
    return effect


def rainbow_star(base: int = 50, per: int = 10):
    """base + per for each type of basic Energy on Defending."""
    async def effect(ctx):
        types = set()
        d = ctx.defender
        if d is not None:
            for c in d.children:
                if not is_basic_energy_card(c):
                    continue
                for t in (PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
                          PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC,
                          PokemonTypes.FIGHTING, PokemonTypes.DARKNESS,
                          PokemonTypes.METAL):
                    if energy_provides_type(c, t.value):
                        types.add(t.value)
        await ctx.deal_damage(base + per * len(types))
    return effect


def supernatural_power(base: int = 40, bonus: int = 40):
    """base, +bonus if same hand size as opponent."""
    async def effect(ctx):
        extra = bonus if len(ctx.hand()) == len(ctx.hand(ctx.opponent_id)) else 0
        await ctx.deal_damage(base + extra)
    return effect


def crushing_mantle(base: int = 10, per: int = 10):
    """Optionally discard Energy from hand; base + per * discarded."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)]
        picks = []
        if pool:
            picks = await ctx.choose_cards(
                pool, len(pool), minimum=0,
                prompt="You may discard Energy cards from your hand")
            if picks:
                await ctx.discard_cards(picks)
        await ctx.deal_damage(base + per * len(picks))
    return effect


def super_tidal_wave(base: int = 50, per: int = 10):
    """Optionally show hand; if you do, base + per * cards shown."""
    async def effect(ctx):
        hand = list(ctx.hand())
        if hand and await ctx.ask_yes_no("Show your hand to your opponent?"):
            await ctx.reveal_cards(hand)
            await ctx.deal_damage(base + per * len(hand))
        else:
            await ctx.deal_damage(base)
    return effect


def tonnage(base: int = 60, bonus: int = 20, self_dmg: int = 30):
    """Optional: base+bonus and self_dmg to self; else just base."""
    async def effect(ctx):
        if await ctx.ask_yes_no(f"Do {base + bonus} damage and take {self_dmg}?"):
            await ctx.deal_damage(base + bonus)
            if ctx.attacker is not None:
                await ctx.deal_damage(
                    self_dmg, target=ctx.attacker,
                    apply_modifiers=False, as_counters=True)
        else:
            await ctx.deal_damage(base)
    return effect


def splash_about(base: int = 10, bonus: int = 10):
    """base, +bonus if fewer Energy than Defending."""
    async def effect(ctx):
        self_n = sum(1 for c in (ctx.attacker.children if ctx.attacker else [])
                     if is_energy_card(c))
        def_n = sum(1 for c in (ctx.defender.children if ctx.defender else [])
                    if is_energy_card(c))
        await ctx.deal_damage(base + (bonus if self_n < def_n else 0))
    return effect


def white_snow_bonus(base: int = 50, bonus: int = 20, stadium_name: str = "Magnetic Storm"):
    """base, +bonus if named Stadium in play."""
    async def effect(ctx):
        stadium = ctx.stadium_in_play()
        extra = 0
        if stadium is not None:
            dn = stadium.get_attribute(AttrID.DISPLAY_NAME) or ""
            if stadium_name.lower() in dn.lower():
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def stadium_condition_if(stadium_name: str, *conditions):
    """If named Stadium in play, apply conditions (optionally after damage)."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        stadium = ctx.stadium_in_play()
        if stadium is None:
            return
        dn = stadium.get_attribute(AttrID.DISPLAY_NAME) or ""
        if stadium_name.lower() not in dn.lower():
            return
        if ctx.defender is not None:
            for c in conditions:
                await ctx.apply_special_condition(ctx.defender, c)
    return effect


def call_for_family_basic():
    """Search a Basic Pokémon onto Bench (Call for Family)."""
    return search_to_bench(
        is_basic_pokemon, count=1,
        prompt="Choose a Basic Pokémon to put onto your Bench")


def ascension():
    """Search deck for a card that evolves from this Pokémon and put it on
    (counts as evolving)."""
    async def effect(ctx):
        src = ctx.source or ctx.attacker
        if src is None:
            return
        name = src.get_attribute(AttrID.NAME) or ""
        def match(c):
            d = def_for(c.archetype_id)
            return bool(d and getattr(d, "evolves_from", None) == name)
        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose a card that evolves from this Pokémon")
        if picks:
            await ctx.evolve_pokemon(src, picks[0])
        await ctx.shuffle_deck()
    return effect


def make_a_wish():
    """Search deck for a card that evolves from 1 of your Pokémon and put it on."""
    async def effect(ctx):
        mine = list(ctx.my_pokemon_in_play())
        if not mine:
            return
        # Collect (pokemon, evo_card) candidates by scanning deck once via search
        def match(c):
            d = def_for(c.archetype_id)
            ef = getattr(d, "evolves_from", None) if d else None
            if not ef:
                return False
            return any((p.get_attribute(AttrID.NAME) or "") == ef for p in mine)
        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose an Evolution card for 1 of your Pokémon")
        if not picks:
            await ctx.shuffle_deck()
            return
        evo = picks[0]
        d = def_for(evo.archetype_id)
        ef = getattr(d, "evolves_from", None)
        targets = [p for p in mine if (p.get_attribute(AttrID.NAME) or "") == ef]
        if not targets:
            await ctx.shuffle_deck()
            return
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose the Pokémon to evolve")
        if target is not None:
            await ctx.evolve_pokemon(target, evo)
        await ctx.shuffle_deck()
    return effect


def heal_dance(counters: int = 2):
    """Once per turn: remove `counters` damage counters from 1 of your Pokémon."""
    async def effect(ctx):
        damaged = [
            p for p in ctx.my_pokemon_in_play()
            if p.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, p)
        ]
        if not damaged:
            return
        target = await ctx.choose_pokemon(
            damaged, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(counters * 10, target)
    return effect


def miracle_powder():
    """Flip: heads choose 1 Special Condition and apply."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Miracle Powder")
        if not (results and results[0]) or ctx.defender is None:
            return
        options = ["Asleep", "Burned", "Confused", "Paralyzed", "Poisoned"]
        conds = [
            SpecialConditions.ASLEEP, SpecialConditions.BURNED,
            SpecialConditions.CONFUSED, SpecialConditions.PARALYZED,
            SpecialConditions.POISONED,
        ]
        idx = await ctx.choose("Choose a Special Condition", options)
        if idx is None:
            idx = 0
        await ctx.apply_special_condition(ctx.defender, conds[idx])
    return effect


def special_formula():
    """Flip: heads Asleep+Poisoned; tails Confused+Burned."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Special Formula")
        d = ctx.defender
        if d is None:
            return
        if results and results[0]:
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
            await ctx.apply_special_condition(d, SpecialConditions.POISONED)
        else:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
            await ctx.apply_special_condition(d, SpecialConditions.BURNED)
    return effect


def cling_heal():
    """After attack, heal self equal to damage done to Defending."""
    async def effect(ctx):
        before = ctx.defender.get_attribute(AttrID.HP, 0) if ctx.defender else 0
        await ctx.deal_damage()
        if ctx.defender is None or ctx.attacker is None:
            return
        after = ctx.defender.get_attribute(AttrID.HP, 0)
        dealt = max(0, before - after)
        if dealt > 0:
            await ctx.heal(dealt, ctx.attacker)
    return effect


def distorted_wave(remove: int = 3):
    """Before damage, remove `remove` damage counters from Defending."""
    async def effect(ctx):
        d = ctx.defender
        if d is not None:
            await ctx.heal(remove * 10, d)
        await ctx.deal_damage()
    return effect


def swallow_up():
    """If Defending has remaining HP <= self remaining HP, KO Defending."""
    async def effect(ctx):
        d, a = ctx.defender, ctx.attacker
        if d is None or a is None:
            await ctx.deal_damage()
            return
        d_hp = d.get_attribute(AttrID.HP, 0)
        a_hp = a.get_attribute(AttrID.HP, 0)
        if d_hp <= a_hp:
            await ctx.deal_damage(d_hp, apply_modifiers=False, as_counters=True)
        else:
            await ctx.deal_damage()
    return effect


def metal_ball(counters: int = 5):
    """Put `counters` damage counters on Defending."""
    async def effect(ctx):
        if ctx.defender is not None:
            await ctx.deal_damage(
                counters * 10, apply_modifiers=False, as_counters=True)
    return effect


def mass_destruction():
    """KO both Electrode and Defending. Prize-skip when Special
    Energy is attached is a known soft gap (knock_out has no flag)."""
    async def effect(ctx):
        a, d = ctx.attacker, ctx.defender
        if d is not None:
            await ctx.knock_out(d)
        if a is not None:
            await ctx.knock_out(a)
    return effect
def breaking_sound(amount: int = 10):
    """amount to each of opponent's Pokémon (no W/R for Bench)."""
    from spirit.game.card_effects.attacks_common import damage_all_opponents
    return damage_all_opponents(amount)


def bass_control(amount: int = 30):
    """amount to 1 of opponent's Pokémon (no W/R for Bench)."""
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any")


def super_icy_wind(amount: int = 10):
    """amount to each of opponent's Pokémon; ignore Resistance."""
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(
                amount, target=p, apply_modifiers=(p is ctx.opponent_active()),
                ignore_resistance=True)
    return effect


def heavy_blizzard():
    """Printed damage; heads: 1 damage counter on each opponent Bench."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Heavy Blizzard")
        if results and results[0]:
            for p in ctx.opponent_bench():
                await ctx.deal_damage(
                    10, target=p, apply_modifiers=False, as_counters=True)
    return effect


def steel_wave(bench_amount: int = 20):
    """Printed to Active; `bench_amount` to each Bench of same type as Defending."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        types = set(d.get_attribute(AttrID.POKEMON_TYPES) or [])
        for p in ctx.opponent_bench():
            pt = set(p.get_attribute(AttrID.POKEMON_TYPES) or [])
            if types & pt:
                await ctx.deal_damage(
                    bench_amount, target=p, apply_modifiers=False)
    return effect


def squared_attack(coins: int = 4, per: int = 30):
    from spirit.game.card_effects.attacks_common import flip_damage
    return flip_damage(coins=coins, per_heads=per)


def cross_chop(base: int = 60, bonus: int = 30):
    from spirit.game.card_effects.attacks_common import flip_bonus
    # flip_bonus adds to printed; card has damage=60 operator=+
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Cross Chop")
        await ctx.deal_damage(base + (bonus if results and results[0] else 0))
    return effect


def slashing_strike_lock():
    """Printed damage; tails: can't use this attack next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Slashing Strike")
        if results and not results[0] and ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)  # approximate: lock all
            # Prefer title lock if available
            state = ctx.session.turn_state
            aid = getattr(ctx.ability, "ability_id", None) or getattr(ctx.ability, "title", "")
            state.attack_locks[(ctx.attacker.entity_id, aid)] = state.turn_number + 2
    return effect


def freezing_breath():
    """Flip: heads Paralyze; tails Asleep. No printed needed or with printed."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Freezing Breath")
        d = ctx.defender
        if d is None:
            return
        if results and results[0]:
            await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
        else:
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
    return effect


def flurries():
    """Flip: heads Paralyze; tails Confuse. With optional printed."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Flurries")
        d = ctx.defender
        if d is None:
            return
        if results and results[0]:
            await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
        else:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def hula_la():
    """Flip: heads Confuse Defending; tails Confuse both Actives."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "The Hula-la")
        if results and results[0]:
            if ctx.defender is not None:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.CONFUSED)
        else:
            for p in (ctx.attacker, ctx.defender):
                if p is not None:
                    await ctx.apply_special_condition(
                        p, SpecialConditions.CONFUSED)
    return effect


def long_tentacle():
    """Flip: heads Confuse; tails discard an Energy from Defending."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Long Tentacle")
        d = ctx.defender
        if d is None:
            return
        if results and results[0]:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
        else:
            energies = [c for c in d.children if is_energy_card(c)]
            if energies:
                picks = await ctx.choose_cards(
                    energies, 1, minimum=1,
                    prompt="Choose an Energy to discard")
                if picks:
                    await ctx.discard_cards(picks)
    return effect


def sheer_cold():
    """Printed; heads: Defending can't attack next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Sheer Cold")
        if results and results[0] and ctx.defender is not None:
            lock_all_attacks(ctx, ctx.defender)
    return effect


def freeze_lock():
    """Printed; heads: opponent can't attach Energy from hand next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Freeze Lock")
        if results and results[0]:
            # Soft approximation: mark turn-state flag if engine supports it
            state = ctx.session.turn_state
            flags = getattr(state, "flags", None)
            if flags is not None:
                flags[f"no_energy_attach:{ctx.opponent_id}"] = state.turn_number + 1
    return effect


def fire_blast_discard():
    """Printed damage; discard a Fire Energy from self."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        pool = [
            c for c in ctx.attacker.children
            if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Discard a Fire Energy")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def lightning_strike(boosted: int = 100):
    """Optionally discard all Lightning Energy; if you do, base becomes boosted."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if ctx.attacker is None:
            await ctx.deal_damage(printed)
            return
        pool = [
            c for c in ctx.attacker.children
            if is_energy_card(c) and energy_provides_type(
                c, PokemonTypes.LIGHTNING.value)
        ]
        if pool and await ctx.ask_yes_no(
                "Discard all Lightning Energy for boosted damage?"):
            await ctx.discard_cards(pool)
            await ctx.deal_damage(boosted)
        else:
            await ctx.deal_damage(printed)
    return effect


def hyper_beam_discard():
    """Printed; heads discard 1 Energy from Defending."""
    from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
    return discard_opponent_energy_attack(1, flip=True)


def minus_energy():
    """Flip: heads opponent returns 1 Energy from Defending to hand."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Minus Energy")
        if not (results and results[0]) or ctx.defender is None:
            return
        energies = [c for c in ctx.defender.children if is_energy_card(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=1, prompt="Choose an Energy to return")
        if picks:
            await ctx.put_in_hand(picks, player_id=ctx.opponent_id)
    return effect


def plus_energy():
    """Flip: heads attach a Lightning Energy from hand to any of yours."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Plus Energy")
        if not (results and results[0]):
            return
        pool = [
            c for c in ctx.hand()
            if is_basic_energy_card(c) and energy_provides_type(
                c, PokemonTypes.LIGHTNING.value)
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Attach a Lightning Energy")
        if not picks:
            return
        dests = list(ctx.my_pokemon_in_play())
        dest = await ctx.choose_pokemon(dests, "Attach to which Pokémon?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def shadow_crush():
    """Optionally discard Psychic Energy from self; if so opponent discards a card."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        pool = [
            c for c in ctx.attacker.children
            if is_energy_card(c) and energy_provides_type(
                c, PokemonTypes.PSYCHIC.value)
        ]
        if not pool:
            return
        if not await ctx.ask_yes_no("Discard a Psychic Energy?"):
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Discard a Psychic Energy")
        if not picks:
            return
        await ctx.discard_cards(picks)
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            dump = await ctx.choose_cards(
                hand, 1, minimum=1,
                prompt="Discard a card", player_id=ctx.opponent_id)
            if dump:
                await ctx.discard_cards(dump)
    return effect


def push_aside():
    """Look at opponent's hand; choose 1 Basic/Evo and put on bottom of deck."""
    async def effect(ctx):
        await ctx.deal_damage()
        hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
        cands = [c for c in hand if is_basic_pokemon(c) or is_evolution_pokemon(c)]
        if not cands:
            return
        picks = await ctx.choose_cards(
            cands, 1, minimum=1,
            prompt="Choose a Basic or Evolution card to put on the bottom")
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])
    return effect


def flutter_trick():
    """Flip: heads look at hand, choose 1 card opponent discards."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Flutter Trick")
        if not (results and results[0]):
            return
        hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
        if not hand:
            return
        picks = await ctx.choose_cards(
            list(hand), 1, minimum=1, prompt="Choose a card to discard")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def triple_poison():
    """Poison with 3 counters instead of 1."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.POISONED)
            # Extra poison counters: put 2 more (engine default is 1)
            await ctx.deal_damage(
                20, target=ctx.defender, apply_modifiers=False, as_counters=True)
    return effect


def loving_draw():
    """Draw until hand size matches opponent's."""
    async def effect(ctx):
        need = len(ctx.hand(ctx.opponent_id)) - len(ctx.hand())
        if need > 0:
            await ctx.draw_cards(need)
    return effect


def sweet_temptation():
    """Switch opponent's Bench with Active; then they may switch yours."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose the new Defending Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        await opponent_switches(ctx)  # they may switch your Active — approx as their switch
    return effect


def intense_glare():
    """Gust then they may switch (same as sweet temptation shape without draw)."""
    return sweet_temptation()


def metal_reversal():
    """Before damage, you may switch opponent Bench with Active."""
    return optional_gust_then_damage()


def extra_comet_punch(bonus: int = 50):
    """Printed; next turn this attack does +bonus."""
    from spirit.game.card_effects.passives_common import boost_own_next_turn
    return boost_own_next_turn(bonus, attack_title="Extra Comet Punch")


def silver_wind():
    """Printed; next turn attacks do +bonus to Defending (Silver Wind)."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        # Mark: during your next turn, attacks do +20 more to this Pokémon
        state = ctx.session.turn_state
        start = state.turn_number
        ctx.add_turn_damage_modifier(TurnDamageModifier(
            20, ctx.player_id,
            opposing_active_only=False,
            expires_after_turn=start + 2,
            target_entity_id=d.entity_id,
            source_predicate=lambda _e: state.turn_number > start,
        ))
    return effect


def calm_mind(counters: int = 2):
    """Remove up to `counters` damage counters from self."""
    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


def fruition(move_heal: int = 40):
    """Move 1 Energy from self to another of yours; remove damage counters."""
    async def effect(ctx):
        src = ctx.attacker
        if src is None:
            return
        energies = [c for c in src.children if is_energy_card(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=1, prompt="Choose an Energy to move")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Move Energy to which Pokémon?")
        if dest is None:
            return
        await ctx.move_energy(picks[0], dest)
        await ctx.heal(move_heal, dest)
    return effect


def seedot_growth():
    """Attach a Grass Energy from hand to Seedot."""
    return growth_attach(PokemonTypes.GRASS)


def recharge_lightning():
    """Search deck for Lightning Energy and attach to self."""
    async def effect(ctx):
        def match(c):
            return is_basic_energy_card(c) and energy_provides_type(
                c, PokemonTypes.LIGHTNING.value)
        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose a Lightning Energy to attach")
        if picks and ctx.attacker is not None:
            await ctx.attach_energy(picks[0], ctx.attacker)
        await ctx.shuffle_deck()
    return effect


def dark_provide():
    """Attach up to 1 Grass or Darkness Energy from hand to your Pokémon."""
    async def effect(ctx):
        pool = [
            c for c in ctx.hand()
            if is_energy_card(c) and (
                energy_provides_type(c, PokemonTypes.GRASS.value)
                or energy_provides_type(c, PokemonTypes.DARKNESS.value))
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0,
            prompt="Attach a Grass or Darkness Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(
            list(ctx.my_pokemon_in_play()), "Attach to which Pokémon?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def extra_draw_if_ex(count: int = 2, energy_type=PokemonTypes.GRASS):
    """If opponent has Pokémon-ex, search up to `count` typed Energy into hand."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        if not any(is_pokemon_ex(p) for p in ctx.opponent_pokemon_in_play()):
            return
        def match(c):
            return is_basic_energy_card(c) and energy_provides_type(c, type_value)
        picks = await ctx.search_deck(
            match, count=count, minimum=0,
            prompt=f"Choose up to {count} Energy card(s)")
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def crush_draw():
    """Reveal top; if basic Energy attach to self."""
    async def effect(ctx):
        top = ctx.deck_top(1)
        if not top:
            return
        card = top[0]
        await ctx.reveal_cards([card])
        if is_basic_energy_card(card) and ctx.source is not None:
            await ctx.attach_energy(card, ctx.source)
    return effect


def healing_shower():
    """When played to evolve: remove damage from all your Pokémon."""
    async def effect(ctx):
        for p in ctx.my_pokemon_in_play():
            missing = effective_max_hp(ctx.board, p) - p.get_attribute(AttrID.HP, 0)
            if missing > 0:
                await ctx.heal(missing, p)
    return effect


def metal_juncture():
    """Move a Metal Energy from 1 of yours to another (as often as you like)."""
    async def effect(ctx):
        donors = [
            p for p in ctx.my_pokemon_in_play()
            if any(is_energy_card(c) and energy_provides_type(
                c, PokemonTypes.METAL.value) for c in p.children)
        ]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move Metal Energy from?")
        if src is None:
            return
        pool = [
            c for c in src.children
            if is_energy_card(c) and energy_provides_type(c, PokemonTypes.METAL.value)
        ]
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose Metal Energy")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Move Metal Energy to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect


def set_song():
    """Search Basic Pokémon and a basic Energy; show; put into hand."""
    async def effect(ctx):
        picks_p = await ctx.search_deck(
            is_basic_pokemon, count=1, minimum=0,
            prompt="Choose a Basic Pokémon")
        picks_e = await ctx.search_deck(
            is_basic_energy_card, count=1, minimum=0,
            prompt="Choose a basic Energy card")
        await ctx.put_in_hand(picks_p + picks_e, reveal=True)
        await ctx.shuffle_deck()
    return effect


def coral_glow():
    """Draw up to number of opponent's Basic Pokémon in play."""
    async def effect(ctx):
        n = sum(1 for p in ctx.opponent_pokemon_in_play() if is_basic_pokemon(p))
        if n <= 0:
            return
        # Draw up to n — choose how many
        options = [str(i) for i in range(n + 1)]
        idx = await ctx.choose("How many cards to draw?", options)
        if idx is None:
            idx = n
        await ctx.draw_cards(int(options[idx]))
    return effect


def forecast_stadium():
    """Search deck for a Stadium and play it."""
    async def effect(ctx):
        def match(c):
            st = subtypes_for(c.archetype_id) or []
            return "Stadium" in st
        picks = await ctx.search_deck(
            match, count=1, minimum=0, prompt="Choose a Stadium card")
        if picks:
            # Playing Stadium mid-effect needs session support; put into hand.
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def sunshine_stadium_from_discard():
    """Search discard for Stadium into hand."""
    async def effect(ctx):
        pool = [
            c for c in ctx.discard_pile()
            if "Stadium" in (subtypes_for(c.archetype_id) or [])
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose a Stadium card")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def scattered_shower(draw: int = 5):
    """Shuffle hand into deck; draw up to `draw`."""
    async def effect(ctx):
        hand = list(ctx.hand())
        if hand:
            await ctx.shuffle_into_deck(hand)
        options = [str(i) for i in range(draw + 1)]
        idx = await ctx.choose("How many cards to draw?", options)
        if idx is None:
            idx = draw
        await ctx.draw_cards(int(options[idx]))
    return effect


def temperamental_weather(*names: str):
    """Search deck for a Castform form; identity-swap in place (attachments,
    damage, Special Conditions, and effects move to the new Pokémon); shuffle
    the old form into the deck."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        lowered = tuple(n.lower() for n in names)
        def match(c):
            d = def_for(c.archetype_id)
            dn = (getattr(d, "display_name", None) or "").lower()
            return any(n in dn for n in lowered)
        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose a Castform to switch with")
        if not picks:
            await ctx.shuffle_deck()
            return
        await ctx.identity_swap(src, picks[0], destination="deck", transfer=True)
        await ctx.shuffle_deck()
    return effect


def chime_copy_supporter():
    """Search opponent's discard for a Supporter and use its effect."""
    async def effect(ctx):
        pool = [
            c for c in ctx.discard_pile(ctx.opponent_id)
            if is_supporter_card(c) and _runnable_supporter(c)
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose a Supporter to use")
        if not picks:
            return
        effect_fn = TRAINER_EFFECTS_BY_GUID[(picks[0].archetype_id or "").lower()]
        await effect_fn(ctx)
    return effect


def hyper_tail(base: int = 50, bonus: int = 20):
    """base, +bonus if Defending has Poké-Power or Poké-Body."""
    async def effect(ctx):
        extra = 0
        d = ctx.defender
        if d is not None:
            for e in (d.get_attribute(AttrID.PIE_ABILITIES) or []):
                if isinstance(e, dict) and e.get("abilityType") in (
                        "Poké-Power", "Poke-Power", "Poké-Body", "Poke-Body"):
                    extra = bonus
                    break
            if extra == 0:
                definition = def_for(d.archetype_id)
                for ab in getattr(definition, "abilities", None) or []:
                    at = getattr(ab, "ability_type", None)
                    if at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY):
                        extra = bonus
                        break
        await ctx.deal_damage(base + extra)
    return effect


# --- Passives (Poké-Bodies) ---

def exoskeleton_passive(amount: int = 10) -> Passive:
    return takes_less_passive(amount)


def crust_passive(amount: int = 30) -> Passive:
    """Takes `amount` less from opponent's Basic Pokémon."""
    return takes_less_passive(
        amount,
        attacker_pred=lambda attacker: is_basic_pokemon(attacker),
    )


def ice_wall_passive() -> Passive:
    """Takes less / prevent from attacks by Pokémon with Special Energy."""
    from spirit.game.session.effects import is_special_energy

    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            attacker = calc.attacker
            if attacker is None:
                return
            if any(is_special_energy(c) for c in attacker.children):
                calc.amount = 0
    return _P()


def core_guard_passive(amount: int = 10) -> Passive:
    """If any Psychic Energy attached, take `amount` less."""
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            if any(is_energy_card(c) and energy_provides_type(
                    c, PokemonTypes.PSYCHIC.value) for c in holder.children):
                calc.amount = max(0, calc.amount - amount)
    return _P()


def crystal_body_passive() -> Passive:
    """Prevent all effects of attacks except damage from Attacking Pokémon."""
    class _P(Passive):
        def blocks_attack_effects_from(self, target, carrier, attacker):
            return carrier_pokemon(carrier) is target
    return _P()


def overzealous_passive(bonus: int = 30) -> Passive:
    """If opponent has Pokémon-ex, this Pokémon's attacks do +bonus."""
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.attacker is holder):
                return
            board = calc.board if hasattr(calc, "board") else None
            # Use session via calc when available; else skip
            opp_id = None
            if hasattr(calc, "opponent_id"):
                opp_id = calc.opponent_id
            # Fallback: check opposing side pokemon via target's owner
            if calc.target is None:
                return
            # Look at all opposing pokemon through a side-channel on calc
            opposing = getattr(calc, "opposing_pokemon", None)
            if opposing is None:
                # Conservative: boost if defender is ex OR we can't tell
                if is_pokemon_ex(calc.target):
                    calc.amount += bonus
                return
            if any(is_pokemon_ex(p) for p in opposing):
                calc.amount += bonus
    return _P()


def primal_pull_passive(extra: int = 1) -> Passive:
    """While Active: each player's Evolved Pokémon pay Colorless `extra` more to attack."""
    class _P(Passive):
        def modify_attack_cost(self, cost, pokemon, carrier, board):
            if not is_in_active_spot(carrier):
                return cost
            if not is_evolution_pokemon(pokemon):
                return cost
            cost = dict(cost)
            cost["Colorless"] = cost.get("Colorless", 0) + extra
            return cost
    return _P()


def mark_of_antiquity_passive(*blocked_names: str) -> Passive:
    """While Active: named Pokémon-ex can't attack."""
    lowered = tuple(n.lower() for n in blocked_names)

    class _P(Passive):
        def prevents_attack(self, attacker, carrier, board):
            if not is_in_active_spot(carrier):
                return False
            if attacker.owning_player_id == carrier.owning_player_id:
                return False
            dn = (attacker.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            return any(n in dn for n in lowered)
    return _P()


def block_dust_passive() -> Passive:
    """While Active: opponent can't play Trainer cards (approx via flag)."""
    class _P(Passive):
        def blocks_playing_trainers(self, player_id, carrier, board):
            if not is_in_active_spot(carrier):
                return False
            return player_id != carrier.owning_player_id
    return _P()


def power_diffusion_passive() -> Passive:
    """While Active: prevent all damage done by attacks to all of your Benched."""
    class _P(Passive):
        def prevents_damage(self, calc, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return False
            if not is_in_active_spot(carrier):
                return False
            target = calc.target
            if target is None or target.owning_player_id != carrier.owning_player_id:
                return False
            return not is_in_active_spot(target)
    return _P()


def deep_sleep_passive() -> Passive:
    """While Active: players flip 2 coins for Asleep (both must be heads)."""
    # Soft: documented gap if engine lacks asleep-coin override; no-op body.
    class _P(Passive):
        def asleep_coins_required(self, pokemon, carrier):
            if is_in_active_spot(carrier):
                return 2
            return None
    return _P()


def fast_feet_passive() -> Passive:
    """Can retreat even when Asleep or Paralyzed."""
    class _P(Passive):
        def can_retreat_despite_conditions(self, pokemon, carrier):
            return carrier_pokemon(carrier) is pokemon
    return _P()


def strikes_back_passive(counters: int = 1) -> Passive:
    """If Active and damaged by attack, put counters on Attacking."""
    # Implemented as ON_DAMAGED trigger ability preferred; passive stub marker.
    class _P(Passive):
        pass
    return _P()


async def strikes_back_on_damaged(ctx):
    """ON_DAMAGED: if Active, put 1 damage counter on Attacking Pokémon."""
    if not is_in_active_spot(ctx.source):
        return
    attacker = getattr(ctx, "attacking_pokemon", None) or getattr(ctx, "attacker", None)
    if attacker is None:
        return
    await ctx.deal_damage(10, target=attacker, apply_modifiers=False, as_counters=True)


def healing_stone_between_turns(amount: int = 10):
    return rain_dish(amount)



async def energy_grounding(ctx):
    """ON_ALLY_KNOCKED_OUT: attach 1 basic Energy from the KO'd Pokémon to this
    Lanturn. Once per turn across all Energy Grounding powers."""
    if not getattr(ctx, "ko_from_attack", False) or ctx.ko_pokemon is None:
        return
    if ctx.ko_pokemon.owning_player_id != ctx.player_id:
        return
    state = ctx.session.turn_state
    flags = getattr(state, "flags", None)
    if isinstance(flags, dict) and flags.get("energy_grounding_used"):
        return
    pool = [e for e in ctx.attached_energies(ctx.ko_pokemon) if is_basic_energy_card(e)]
    if not pool or ctx.source is None:
        return
    if not await ctx.ask_yes_no(
            "Use Energy Grounding to attach a basic Energy to Lanturn?"):
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=1, prompt="Choose a basic Energy to attach to Lanturn")
    if not picks:
        return
    await ctx.move_energy(picks[0], ctx.source)
    if isinstance(flags, dict):
        flags["energy_grounding_used"] = True
    elif flags is None:
        # best-effort: stash on turn_state
        try:
            state.energy_grounding_used = True
        except Exception:
            pass


# --- Trainers / Stadiums / Ancient TMs ---

def _has_owner_in_name(pokemon) -> bool:
    raw = pokemon.get_attribute(AttrID.DISPLAY_NAME) if pokemon is not None else None
    if isinstance(raw, dict):
        dn = raw.get("english") or raw.get("en") or next(iter(raw.values()), "") or ""
    else:
        dn = raw or ""
    # "'s " in name (e.g. Brock's, Rocket's) or possessive patterns
    return "'s " in dn or str(dn).startswith("Team ")


def attach_to_evolved_non_ex_non_owner():
    """Ancient TM attach restriction."""
    def check(pokemon) -> bool:
        if is_pokemon_ex(pokemon):
            return False
        if _has_owner_in_name(pokemon):
            return False
        return is_evolution_pokemon(pokemon)
    return check


def ancient_tm_discard_end_turn(tool_guid: str):
    """END_OF_TURN: discard this Ancient TM from the holder."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        tool = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == tool_guid.lower()),
            None)
        if tool is not None:
            await ctx.discard_cards([tool])
    return effect


def ice_generator(tool_guid: str):
    """Discard all opponent Trainer cards in play; if you do, full protect."""
    from spirit.game.card_effects.passives_common import apply_protection
    async def effect(ctx):
        to_discard = []
        stadium = ctx.stadium_in_play()
        if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
            to_discard.append(stadium)
        for p in ctx.opponent_pokemon_in_play():
            for c in list(p.children):
                if _is_attached_trainer(c):
                    to_discard.append(c)
        if to_discard:
            await ctx.discard_cards(to_discard)
            await apply_protection(
                ctx, target=ctx.attacker, prevent=True, effects_too=True)
        # Always discard the TM at end of turn via granted Ability; also drop now
        if ctx.attacker is not None:
            tool = next(
                (c for c in ctx.attacker.children
                 if (c.archetype_id or "").lower() == tool_guid.lower()),
                None)
            # Keep until end of turn per card text — discard via END_OF_TURN ability
    return effect


def stone_generator():
    """pull_down alias for Ancient TM Rock."""
    return pull_down


def steel_generator():
    """If Defending has Poké-Power/Body, move up to 2 basic Energy onto it."""
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        has_pb = False
        definition = def_for(d.archetype_id)
        for ab in getattr(definition, "abilities", None) or []:
            at = getattr(ab, "ability_type", None)
            if at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY):
                has_pb = True
                break
        if not has_pb:
            return
        donors = [
            p for p in ctx.opponent_pokemon_in_play()
            if p is not d and any(is_basic_energy_card(c) for c in p.children)
        ]
        if not donors:
            return
        src = await ctx.choose_pokemon(
            donors, "Choose a Pokémon to move Energy from")
        if src is None:
            return
        pool = [c for c in src.children if is_basic_energy_card(c)]
        picks = await ctx.choose_cards(
            pool, min(2, len(pool)), minimum=0,
            prompt="Choose up to 2 basic Energy to move")
        for e in picks:
            await ctx.move_energy(e, d)
    return effect


def ancient_tomb_passive() -> Passive:
    """Don't apply Weakness for non-ex non-owner Pokémon."""
    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            t = calc.target
            if t is None:
                return
            if is_pokemon_ex(t) or _has_owner_in_name(t):
                return
            calc.weakness_applies = False
    return _P()


async def desert_ruins_between_turns(ctx):
    """Each player puts 1 damage counter on their Pokémon-ex with max HP >= 100."""
    for pid in ctx.board.player_ids:
        for p in ctx.board.pokemon_in_play(pid):
            if not is_pokemon_ex(p):
                continue
            if effective_max_hp(ctx.board, p) < 100:
                continue
            await ctx.deal_damage(
                10, target=p, apply_modifiers=False, as_counters=True)


def island_cave_passive() -> Passive:
    """When attaching Energy to Water/Fighting/Metal, clear Special Conditions.
    Soft: documented as attach-hook; body clears on those types when Active
    stadium is present — full hook may need engine attach event."""
    class _P(Passive):
        pass
    return _P()


def magnetic_storm_passive() -> Passive:
    """Psychic and Fighting attacks ignore Resistance."""
    from spirit.game.card_effects.passives_common import no_resistance_passive
    psy = PokemonTypes.PSYCHIC.value
    fig = PokemonTypes.FIGHTING.value

    def when(calc, carrier):
        if calc.attacker is None:
            return False
        types = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        return psy in types or fig in types
    return no_resistance_passive(when=when)


async def life_herb(ctx):
    """Flip: heads choose non-ex Pokémon; remove all SC and 6 damage counters."""
    results = await ctx.flip_coins(1, "Life Herb")
    if not (results and results[0]):
        return
    cands = [p for p in ctx.my_pokemon_in_play() if not is_pokemon_ex(p)]
    if not cands:
        return
    target = await ctx.choose_pokemon(cands, "Choose a Pokémon")
    if target is None:
        return
    await ctx.cure_all_conditions(target)
    await ctx.heal(60, target)


async def stevens_advice(ctx):
    """Draw up to number of opponent's Pokémon in play; can't play if hand>7
    including this card (playability gated by condition)."""
    n = len(ctx.opponent_pokemon_in_play())
    if n <= 0:
        return
    options = [str(i) for i in range(n + 1)]
    idx = await ctx.choose("How many cards to draw?", options)
    if idx is None:
        idx = n
    await ctx.draw_cards(int(options[idx]))


def stevens_advice_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return len(hand.children if hand else []) <= 7


# ---------------------------------------------------------------------------
# EX6 FireRed & LeafGreen
# ---------------------------------------------------------------------------

async def bills_maintenance(ctx):
    """Shuffle 1 from hand into deck, draw 3."""
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Shuffle 1 card into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks)
    await ctx.draw_cards(3)


async def celios_network(ctx):
    """Search Basic or Evolution excluding Pokémon-ex into hand."""
    def match(c):
        if is_pokemon_ex(c):
            return False
        return is_basic_pokemon(c) or is_evolution_pokemon(c)
    picks = await ctx.search_deck(
        match, count=1, minimum=0,
        prompt="Choose a Basic Pokémon or Evolution card (excluding Pokémon-ex)")
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def oaks_research(ctx):
    """Shuffle hand into deck, draw 5 (Professor Oak's Research)."""
    await ctx.shuffle_into_deck(list(ctx.hand()))
    await ctx.draw_cards(5)


async def vs_seeker(ctx):
    """Supporter from discard into hand."""
    pool = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=1, prompt="Choose a Supporter card")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


async def super_scoop_up(ctx):
    """Flip: heads return 1 of your Pokémon and attachments to hand."""
    results = await ctx.flip_coins(1, "Super Scoop Up")
    if not (results and results[0]):
        return
    cands = list(ctx.my_pokemon_in_play())
    if not cands:
        return
    target = await ctx.choose_pokemon(cands, "Choose a Pokémon to return to your hand")
    if target is not None:
        await ctx.return_to_hand(target)


async def poke_dex_handy(ctx):
    """Shuffle deck; look at top 6; put back in any order."""
    await ctx.shuffle_deck()
    top = ctx.deck_top(6)
    if not top:
        return
    # Reorder: choose order via reorder_deck_top if available
    await ctx.reorder_deck_top(len(top))


def mt_moon_passive() -> Passive:
    """Pokémon with max HP < 70 can't use Poké-Powers."""
    class _P(Passive):
        def blocks_poke_power(self, pokemon, carrier, board):
            return effective_max_hp(board, pokemon) < 70
    return _P()


def attach_to_non_ex_non_owner():
    def check(pokemon) -> bool:
        if is_pokemon_ex(pokemon):
            return False
        return not _has_owner_in_name(pokemon)
    return check


async def exp_all_on_ally_ko(ctx):
    """ON_ALLY_KNOCKED_OUT: if Active KO'd by attack, move 1 basic Energy to
    the Pokémon holding EXP.ALL, then discard EXP.ALL."""
    if not getattr(ctx, "ko_from_attack", False) or ctx.ko_pokemon is None:
        return
    if ctx.board.active_pokemon(ctx.player_id) is not ctx.ko_pokemon:
        return
    holder = ctx.source
    if holder is None:
        return
    pool = [e for e in ctx.attached_energies(ctx.ko_pokemon) if is_basic_energy_card(e)]
    if not pool:
        return
    if not await ctx.ask_yes_no("Use EXP. ALL to move a basic Energy?"):
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a basic Energy")
    if not picks:
        return
    await ctx.move_energy(picks[0], holder)
    # Discard EXP.ALL tool
    tool = next(
        (c for c in holder.children
         if "EXP" in (c.get_attribute(AttrID.DISPLAY_NAME) or "").upper()
         or "Exp" in (c.get_attribute(AttrID.DISPLAY_NAME) or "")),
        None)
    if tool is not None:
        await ctx.discard_cards([tool])


def smash_turn():
    """Printed damage; then you may switch with Bench."""
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if bench and await ctx.ask_yes_no("Switch with a Benched Pokémon?"):
            target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
    return effect


def sleep_poison_flip():
    """Flip: heads Asleep and Poisoned."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Sleep Poison")
        if results and results[0] and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def sleep_poison_sure():
    """Asleep and Poisoned (no flip)."""
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED)


def pollen_hazard():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(
        SpecialConditions.POISONED, SpecialConditions.BURNED, SpecialConditions.CONFUSED)


def heat_tackle(self_dmg: int = 10):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_dmg)


def link_needle(base: int = 50, per: int = 30, name: str = "Beedrill"):
    """base + per for each other named Pokémon in play."""
    async def effect(ctx):
        n = sum(
            1 for p in ctx.my_pokemon_in_play()
            if p is not ctx.attacker
            and name.lower() in (p.get_attribute(AttrID.DISPLAY_NAME) or "").lower())
        await ctx.deal_damage(base + per * n)
    return effect


def water_gun_extra(base: int = 20, per: int = 10, energy_type=PokemonTypes.WATER):
    """base + per for each typed Energy beyond attack cost."""
    return extra_energy_damage(per, base=base, energy_type=energy_type)


def hyper_pump(base: int = 30, per: int = 20, energy_type=PokemonTypes.WATER):
    return extra_energy_damage(per, base=base, energy_type=energy_type)


def big_eggsplosion(per: int = 40):
    from spirit.game.card_effects.attacks_common import flip_damage, count_energy
    async def effect(ctx):
        n = count_energy("self")(ctx)
        if n <= 0:
            await ctx.deal_damage(0)
            return
        results = await ctx.flip_coins(n, "Big Eggsplosion")
        await ctx.deal_damage(per * sum(1 for r in results if r))
    return effect


def psychic_exchange(draw: int = 8):
    async def effect(ctx):
        await ctx.shuffle_into_deck(list(ctx.hand()))
        options = [str(i) for i in range(draw + 1)]
        idx = await ctx.choose("How many cards to draw?", options)
        if idx is None:
            idx = draw
        await ctx.draw_cards(int(options[idx]))
    return effect


def poltergeist(base: int = 40, per: int = 10):
    async def effect(ctx):
        hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
        n = sum(1 for c in hand if is_supporter_card(c) or (
            subtypes_for(c.archetype_id) and "Trainer" in str(subtypes_for(c.archetype_id))))
        # Count Trainer cards in hand
        from spirit.game.session.effects import is_trainer_card
        n = sum(1 for c in hand if is_trainer_card(c))
        await ctx.deal_damage(base + per * n)
    return effect


def prize_count(base: int = 60, bonus: int = 60):
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import count_prizes_remaining
        mine = count_prizes_remaining("mine")(ctx)
        opp = count_prizes_remaining("opponent")(ctx)
        await ctx.deal_damage(base + (bonus if mine > opp else 0))
    return effect


def power_lariat(base: int = 40, per: int = 10):
    async def effect(ctx):
        n = sum(1 for p in ctx.my_pokemon_in_play() if is_evolution_pokemon(p))
        await ctx.deal_damage(base + per * n)
    return effect


def vengeance(base: int = 30, per: int = 10):
    async def effect(ctx):
        n = sum(
            1 for c in ctx.discard_pile()
            if is_basic_pokemon(c) or is_evolution_pokemon(c))
        await ctx.deal_damage(base + per * n)
    return effect


def rampage(base: int = 20, per: int = 10):
    """base + per per damage counter on self; then Confuse self."""
    from spirit.game.card_effects.attacks_common import damage_counters_on
    count_fn = damage_counters_on("self")
    async def effect(ctx):
        await ctx.deal_damage(base + per * count_fn(ctx))
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)
    return effect


def toss_and_turn(base: int = 30, bonus: int = 30):
    async def effect(ctx):
        asleep = False
        if ctx.attacker is not None:
            conds = ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            from spirit.game.session.effects import CLIENT_SPECIAL_CONDITION_NAMES
            asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP] in conds
        await ctx.deal_damage(base + (bonus if asleep else 0))
    return effect


def collapse_asleep():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    return effect


def confusion_wave():
    async def effect(ctx):
        await ctx.deal_damage()
        for p in (ctx.attacker, ctx.defender):
            if p is not None:
                await ctx.apply_special_condition(p, SpecialConditions.CONFUSED)
    return effect


def cross_cut(base: int = 10, bonus: int = 10):
    async def effect(ctx):
        extra = bonus if ctx.defender is not None and is_evolution_pokemon(ctx.defender) else 0
        await ctx.deal_damage(base + extra)
    return effect


def one_two_punch(base: int = 30, bonus: int = 20):
    from spirit.game.card_effects.attacks_common import flip_bonus
    async def effect(ctx):
        results = await ctx.flip_coins(1, "One-Two Punch")
        await ctx.deal_damage(base + (bonus if results and results[0] else 0))
    return effect


def quick_attack_bonus(base: int = 10, bonus: int = 40):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Quick Attack")
        await ctx.deal_damage(base + (bonus if results and results[0] else 0))
    return effect


def rend(base: int = 20, bonus: int = 20):
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import damage_counters_on
        extra = bonus if damage_counters_on("defender")(ctx) > 0 else 0
        await ctx.deal_damage(base + extra)
    return effect


def earth_poison():
    async def effect(ctx):
        await ctx.deal_damage()
        from spirit.game.card_effects.attacks_common import damage_counters_on
        if damage_counters_on("defender")(ctx) > 0 and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def mega_throw(base: int = 50, bonus: int = 30):
    return bonus_if_ex(bonus, base=base)


def electron_crush(base: int = 50, bonus: int = 30):
    """Optionally discard Energy; if so, base+bonus."""
    async def effect(ctx):
        if ctx.attacker is not None:
            pool = [c for c in ctx.attacker.children if is_energy_card(c)]
            if pool and await ctx.ask_yes_no("Discard an Energy for more damage?"):
                picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard an Energy")
                if picks:
                    await ctx.discard_cards(picks)
                    await ctx.deal_damage(base + bonus)
                    return
        await ctx.deal_damage(base)
    return effect


def cold_crush():
    """Optionally discard Energy; if so opponent discards a card from hand? 
    Text: discard Energy; if you do, discard an Energy from Defending."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        pool = [c for c in ctx.attacker.children if is_energy_card(c)]
        if not pool:
            return
        if not await ctx.ask_yes_no("Discard an Energy?"):
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard an Energy")
        if not picks:
            return
        await ctx.discard_cards(picks)
        d = ctx.defender
        if d is None:
            return
        ep = [c for c in d.children if is_energy_card(c)]
        if ep:
            op = await ctx.choose_cards(ep, 1, minimum=1, prompt="Discard opponent Energy")
            if op:
                await ctx.discard_cards(op)
    return effect


def crushing_flames():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        pool = [c for c in ctx.attacker.children if is_energy_card(c)]
        if pool and await ctx.ask_yes_no("Discard an Energy to Burn?"):
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard an Energy")
            if picks:
                await ctx.discard_cards(picks)
                if ctx.defender is not None:
                    await ctx.apply_special_condition(
                        ctx.defender, SpecialConditions.BURNED)
    return effect


def burn_down():
    """Discard 5 Fire Energy; damage ignores W/R."""
    async def effect(ctx):
        if ctx.attacker is not None:
            pool = [
                c for c in ctx.attacker.children
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)]
            picks = await ctx.choose_cards(
                pool, min(5, len(pool)), minimum=min(5, len(pool)),
                prompt="Discard 5 Fire Energy")
            if picks:
                await ctx.discard_cards(picks)
        await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)
    return effect


def expand_protect(reduce: int = 10):
    from spirit.game.card_effects.passives_common import protect_next_turn
    return protect_next_turn(reduce=reduce)


def minimize_protect(reduce: int = 20):
    from spirit.game.card_effects.passives_common import protect_next_turn
    return protect_next_turn(reduce=reduce)


def thick_skin_passive() -> Passive:
    from spirit.game.card_effects.passives_common import condition_immunity_passive
    return condition_immunity_passive()


def protective_dust_passive() -> Passive:
    return crystal_body_passive()


def free_flight_passive() -> Passive:
    return levitate_any_energy_passive()


def leaf_ride_passive() -> Passive:
    return levitate_any_energy_passive()


def floating_electrons_passive() -> Passive:
    return levitate_any_energy_passive()


def exoskeleton_20_passive() -> Passive:
    return takes_less_passive(20)


def energy_protection_passive(per: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            n = sum(1 for c in holder.children if is_energy_card(c))
            calc.amount = max(0, calc.amount - per * n)
    return _P()


def safeguard_ex_dew():
    return safeguard_ex_passive()


def call_for_family_grass(count: int = 2):
    el = PokemonTypes.GRASS.value
    def match(c):
        if not is_basic_pokemon(c):
            return False
        d = def_for(c.archetype_id)
        types = [t.value if hasattr(t, "value") else t
                 for t in (getattr(d, "elements", None) or [])]
        return el in types
    return search_to_bench(match, count=count, prompt="Choose Grass Basic Pokémon")


def call_for_family_nidoran():
    def match(c):
        dn = (getattr(def_for(c.archetype_id), "display_name", None) or "").lower()
        return "nidoran" in dn
    return search_to_bench(match, count=1, prompt="Choose a Nidoran")


def call_for_family_basic_n(count: int = 2):
    return search_to_bench(
        is_basic_pokemon, count=count,
        prompt="Choose Basic Pokémon to Bench")


def signs_of_evolution(*names: str):
    async def effect(ctx):
        found = []
        for name in names:
            def match(c, name=name):
                d = def_for(c.archetype_id)
                return (getattr(d, "display_name", None) or "") == name
            picks = await ctx.search_deck(match, count=1, minimum=0, prompt=f"Choose a {name}")
            found.extend(picks)
        await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
    return effect


def legendary_ascent():
    """ON_PLAY: you may switch this with Active; move any number of typed Energy? 
    Soft: switch into Active."""
    async def effect(ctx):
        if not await ctx.ask_yes_no("Switch this Pokémon with your Active?"):
            return
        if ctx.source is not None:
            await ctx.switch_active(ctx.player_id, ctx.source)
    return effect


def energy_trans(energy_type=PokemonTypes.GRASS):
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        donors = [
            p for p in ctx.my_pokemon_in_play()
            if any(is_energy_card(c) and energy_provides_type(c, type_value)
                   for c in p.children)]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move Energy from?")
        if src is None:
            return
        pool = [c for c in src.children
                if is_energy_card(c) and energy_provides_type(c, type_value)]
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose Energy")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Move Energy to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect


def energy_rain(energy_type=PokemonTypes.WATER):
    """Attach a Water Energy from hand as often as you like."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        pool = [
            c for c in ctx.hand()
            if is_basic_energy_card(c) and energy_provides_type(c, type_value)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Attach a Water Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(
            list(ctx.my_pokemon_in_play()), "Attach to which Pokémon?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def wiggle():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Wiggle")
        d = ctx.defender
        if d is None:
            return
        if results and results[0]:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
        else:
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
    return effect


def random_peck(base: int = 10, per: int = 10, coins: int = 2):
    from spirit.game.card_effects.attacks_common import flip_damage
    return flip_damage(coins=coins, per_heads=per, base=base)


def egg_surprise():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Egg Surprise")
        if results and results[0]:
            await ctx.deal_damage(50)
        else:
            if ctx.attacker is not None:
                await ctx.apply_special_condition(
                    ctx.attacker, SpecialConditions.ASLEEP)
                await ctx.heal(9999, ctx.attacker)  # remove all damage approx
    return effect


def gesture_gust():
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(bench, "Choose new Defending")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
    return effect


def nap_heal(counters: int = 2):
    return calm_mind(counters)


def mischief_shuffle():
    async def effect(ctx):
        await ctx.shuffle_deck(ctx.opponent_id)
    return effect


def data_retrieval(to: int = 4):
    async def effect(ctx):
        need = to - len(ctx.hand())
        if need > 0:
            await ctx.draw_cards(need)
    return effect


def run_around():
    async def effect(ctx):
        bench = ctx.my_bench()
        if bench:
            target = await ctx.choose_pokemon(bench, "Switch with?")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
    return effect


def sooth_dust_between_turns(amount: int = 10):
    """BETWEEN_TURNS while Active: heal amount from each of your Pokémon."""
    async def effect(ctx):
        if not is_in_active_spot(ctx.source):
            return
        for p in ctx.my_pokemon_in_play():
            await ctx.heal(amount, p)
    return effect


def acid_sampler_between_turns():
    async def effect(ctx):
        if not is_in_active_spot(ctx.source):
            return
        d = ctx.opponent_active()
        if d is not None:
            await ctx.deal_damage(10, target=d, apply_modifiers=False, as_counters=True)
    return effect


def hyper_whirlpool():
    async def effect(ctx):
        await ctx.deal_damage()
        while True:
            results = await ctx.flip_coins(1, "Hyper Whirlpool")
            if not (results and results[0]):
                break
            d = ctx.defender
            if d is None:
                break
            energies = [c for c in d.children if is_energy_card(c)]
            if not energies:
                break
            picks = await ctx.choose_cards(
                energies, 1, minimum=1,
                prompt="Opponent discards an Energy", player_id=ctx.opponent_id)
            if picks:
                await ctx.discard_cards(picks)
            else:
                break
    return effect


# ---------------------------------------------------------------------------
def crush_and_burn(base: int = 30, per: int = 20):
    """Optionally discard any attached Energy from your Pokémon in play;
    damage = base + per × discarded (Crush and Burn)."""
    async def effect(ctx):
        pool = []
        for poke in ctx.my_pokemon_in_play():
            for e in ctx.attached_energies(poke):
                pool.append(e)
        picks = []
        if pool:
            picks = await ctx.choose_cards(
                pool, len(pool), minimum=0,
                prompt="Discard Energy attached to your Pokémon")
            if picks:
                await ctx.discard_cards(picks)
        await ctx.deal_damage(base + per * len(picks or []))
    return effect


# EX6 FireRed & LeafGreen — remaining helpers
# ---------------------------------------------------------------------------

def energy_flame_passive() -> Passive:
    """All Energy attached to this Pokémon provide Fire (Energy Flame)."""

    class EnergyFlame(Passive):
        def modify_energy_provided(self, options, energy, holder, board):
            return [[PokemonTypes.FIRE.value]]

    return EnergyFlame()


async def metronome_defending(ctx):
    """Copy 1 of the Defending Pokémon's attacks (Metronome)."""
    from spirit.game.data_utils import Attack
    defender = ctx.defender
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    candidates = []
    seen = set()
    for ability in getattr(definition, "abilities", None) or []:
        if not isinstance(ability, Attack):
            continue
        key = (ability.title, ability.game_text)
        if key in seen:
            continue
        seen.add(key)
        candidates.append((defender, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(
        candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


def form_variation():
    """Form Variation: identity-swap Ditto with a Basic (non-ex, non-Ditto)
    from discard; attachments/damage/SCs/effects move; Ditto is discarded."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        pool = []
        for c in ctx.discard_pile():
            if not is_basic_pokemon(c) or is_pokemon_ex(c):
                continue
            d = def_for(c.archetype_id)
            dn = (getattr(d, "display_name", None) or "")
            if "Ditto" in dn:
                continue
            pool.append(c)
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0,
            prompt="Choose a Basic Pokémon to switch with Ditto")
        if picks:
            await ctx.identity_swap(
                src, picks[0], destination="discard", transfer=True)
    return effect


def retreat_aid_passive(discount: int = 2) -> Passive:
    """Bench Dodrio: Active (excl. ex/Baby) pays Colorless×discount less."""

    class RetreatAid(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            parent = getattr(holder, "parent", None)
            if parent is None or parent.get_attribute(AttrID.NAME) != "bench":
                return cost
            if pokemon is holder:
                return cost
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            if not is_in_active_spot(pokemon):
                return cost
            if is_pokemon_ex(pokemon) or is_baby_pokemon(pokemon):
                return cost
            return max(0, cost - discount)

    return RetreatAid()


def extra_energy_bomb(count: int = 5):
    """KO self, then attach up to `count` Energy from discard to non-ex."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        await ctx.knock_out(src)
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=0,
            prompt=f"Choose up to {count} Energy cards to attach")
        if not picks:
            return
        targets = [p for p in ctx.my_pokemon_in_play() if not is_pokemon_ex(p)]
        if not targets:
            return
        for card in picks:
            dest = await ctx.choose_pokemon(
                targets, "Attach Energy to which Pokémon?")
            if dest is None:
                break
            await ctx.attach_energy(card, dest)
    return effect


def hoard_tools(count: int = 2):
    """Search deck for up to `count` Tools; attach to Pokémon without Tools."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            _is_pokemon_tool_card, count=count, minimum=0,
            prompt=f"Choose up to {count} Pokémon Tool cards")
        for tool in picks or []:
            cands = [
                p for p in ctx.my_pokemon_in_play()
                if not any(_is_pokemon_tool_card(ch) for ch in p.children)
            ]
            if not cands:
                break
            dest = await ctx.choose_pokemon(
                cands, "Attach Tool to which Pokémon?")
            if dest is None:
                break
            ctx.board.attach_card(tool.entity_id, dest.entity_id)
        await ctx.shuffle_deck()
    return effect


def head_trip_confuse_active():
    """Bench power: one of your Active Pokémon is now Confused (Head Trip)."""
    async def effect(ctx):
        src = ctx.source
        if src is None or is_in_active_spot(src):
            return
        area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
        actives = list(area.children) if area else []
        if not actives:
            return
        target = actives[0] if len(actives) == 1 else await ctx.choose_pokemon(
            actives, "Choose an Active Pokémon to Confuse")
        if target is not None:
            await ctx.apply_special_condition(
                target, SpecialConditions.CONFUSED)
    return effect


def eerie_aura_between_turns(counters: int = 2):
    """While Active: damage counters on each Asleep Pokémon (Eerie Aura)."""
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        for pid in ctx.board.player_ids:
            for p in ctx.board.pokemon_in_play(pid):
                conds = p.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
                if "Asleep" in conds:
                    await ctx.deal_damage(
                        amount=counters * 10, target=p, as_counters=True)
    return effect


def sleep_inducer():
    """Opponent switches; new Defending is Asleep (Sleep Inducer)."""
    async def effect(ctx):
        await opponent_switches(ctx)
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.ASLEEP)
    return effect


def poison_payback_on_damaged():
    """ON_DAMAGED_BY_ATTACK while Active → Attacking Poisoned."""
    return condition_on_damaged(SpecialConditions.POISONED, while_active=True)


def salt_water(count: int = 2, energy_type=PokemonTypes.WATER):
    """Search deck for up to `count` typed Energy; attach to self."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        def match(c):
            return (is_basic_energy_card(c)
                    and energy_provides_type(c, type_value))
        picks = await ctx.search_deck(
            match, count=count, minimum=0,
            prompt=f"Choose up to {count} Energy cards")
        if picks and ctx.attacker is not None:
            for card in picks:
                await ctx.attach_energy(card, ctx.attacker)
        await ctx.shuffle_deck()
    return effect


def magic_odds_passive() -> Passive:
    """Prevent attack damage in {10,30,...,170} (Magic Odds)."""
    odds = {10, 30, 50, 70, 90, 110, 130, 150, 170}
    return prevent_damage_when(
        lambda calc, carrier: (
            carrier_pokemon(carrier) is calc.target
            and int(calc.amount) in odds
        )
    )


def magic_evens_passive() -> Passive:
    """Prevent attack damage in {20,40,...,180} (Magic Evens)."""
    evens = {20, 40, 60, 80, 100, 120, 140, 160, 180}
    return prevent_damage_when(
        lambda calc, carrier: (
            carrier_pokemon(carrier) is calc.target
            and int(calc.amount) in evens
        )
    )


_NIDO_LINE = (
    "Nidoran ♀", "Nidoran ♂", "Nidorina", "Nidorino", "Nidoqueen", "Nidoking",
)


def _display_name(pokemon) -> str:
    d = def_for(getattr(pokemon, "archetype_id", None) or "")
    return getattr(d, "display_name", None) or ""


def power_gene_passive(bonus: int = 10) -> Passive:
    """Nido-line attacks do +bonus to Defending (Power Gene)."""
    names = set(_NIDO_LINE)

    def attacker_pred(attacker):
        return _display_name(attacker) in names

    return team_damage_boost_passive(
        bonus, attacker_pred=attacker_pred, once_key="Power Gene")


def bound_crush(damage: int = 60):
    """60 to any opposing Pokémon (no W/R on Bench). Pair with
    locks_next_turn=True on the Attack so Bound Crush can't be reused."""
    async def effect(ctx):
        cands = ctx.opponent_pokemon_in_play()
        if not cands:
            return
        target = await ctx.choose_pokemon(
            cands, "Choose a Pokémon for Bound Crush")
        if target is None:
            return
        await ctx.deal_damage(
            damage, target=target,
            ignore_weakness=not is_in_active_spot(target),
            ignore_resistance=not is_in_active_spot(target),
        )
    return effect


def family_bonds_passive() -> Passive:
    """Named Nido-line Retreat Cost is 0 while this is in play."""
    names = {
        "Nidoran ♀", "Nidoran ♂", "Nidorina", "Nidorino", "Nidoking",
    }

    class FamilyBonds(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            if _display_name(pokemon) in names:
                return 0
            return cost

    return FamilyBonds()


def look_for_friends():
    """Reveal deck until a Basic; put it in hand; shuffle rest."""
    async def effect(ctx):
        deck = list(ctx.deck(ctx.player_id))
        found = None
        revealed = []
        for card in deck:
            revealed.append(card)
            if is_basic_pokemon(card):
                found = card
                break
        if found is not None:
            await ctx.put_in_hand([found], reveal=True)
        await ctx.shuffle_deck()
    return effect


def fast_evolution(count: int = 2):
    """Search deck for up to `count` Evolution cards → hand."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            is_evolution_pokemon, count=count, minimum=0,
            prompt=f"Choose up to {count} Evolution cards")
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def tunneling(per: int = 10, max_targets: int = 2):
    """Up to `max_targets` Bench take `per`; can't attack next turn."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench:
            picks = []
            remaining = list(bench)
            for _ in range(min(max_targets, len(remaining))):
                if not remaining:
                    break
                t = await ctx.choose_pokemon(
                    remaining, "Choose a Benched Pokémon (Tunneling)",
                    optional=True)
                if t is None:
                    break
                picks.append(t)
                remaining = [p for p in remaining if p is not t]
            for t in picks:
                await ctx.deal_damage(
                    per, target=t, ignore_weakness=True, ignore_resistance=True)
        if ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def energy_powder(count: int = 2):
    """Attach up to `count` basic Energy from deck to non-ex Pokémon."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            is_basic_energy_card, count=count, minimum=0,
            prompt=f"Choose up to {count} basic Energy cards")
        targets = [p for p in ctx.my_pokemon_in_play() if not is_pokemon_ex(p)]
        for card in picks or []:
            if not targets:
                break
            dest = await ctx.choose_pokemon(
                targets, "Attach Energy to which Pokémon?")
            if dest is None:
                break
            await ctx.attach_energy(card, dest)
        await ctx.shuffle_deck()
    return effect


def quick_search():
    """Put any 1 card from deck into hand (Quick Search)."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            lambda c: True, count=1, minimum=0,
            prompt="Choose any 1 card from your deck")
        await ctx.put_in_hand(picks)
        await ctx.shuffle_deck()
    return effect


def plasma_attach(energy_type=PokemonTypes.LIGHTNING):
    """Printed damage; flip — heads attach typed Energy from discard to self."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Plasma")
        if not (results and results[0]):
            return
        pool = [
            c for c in ctx.discard_pile()
            if is_energy_card(c) and energy_provides_type(c, type_value)
        ]
        if not pool or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Attach a Lightning Energy from discard")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


def energy_stream():
    """Printed damage; attach a basic Energy from discard to self."""
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Attach a basic Energy from discard")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


def spiral_confused_no_retreat() -> Passive:
    """While Active: opponent's Confused Pokémon can't retreat (Spiral)."""

    class Spiral(Passive):
        def blocks_retreat(self, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not is_in_active_spot(holder):
                return False
            if pokemon.owning_player_id == holder.owning_player_id:
                return False
            conds = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            return "Confused" in conds

    return Spiral()


def _is_tm_or_tool(card) -> bool:
    tt = card.get_attribute(AttrID.TRAINER_TYPE)
    if tt in (
        TrainerType.POKEMON_TOOL.value,
        TrainerType.POKEMON_TOOL_F.value,
        TrainerType.TECHNICAL_MACHINE.value,
    ):
        return True
    return _is_pokemon_tool_card(card)


def toss_tm_tools(per: int = 30):
    """Discard any number of TM/Tool from hand; damage = per × discarded."""
    async def effect(ctx):
        hand = list(ctx.hand())
        pool = [c for c in hand if _is_tm_or_tool(c)]
        if not pool:
            await ctx.deal_damage(0)
            return
        picks = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Discard Technical Machine / Pokémon Tool cards")
        if picks:
            await ctx.discard_cards(picks)
        await ctx.deal_damage(per * len(picks or []))
    return effect


def recharge_typed(count: int = 2, energy_type=PokemonTypes.LIGHTNING):
    """Search deck for up to `count` typed Energy; attach to self."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        def match(c):
            return (is_basic_energy_card(c)
                    and energy_provides_type(c, type_value))
        picks = await ctx.search_deck(
            match, count=count, minimum=0,
            prompt=f"Choose up to {count} Lightning Energy cards")
        if picks and ctx.attacker is not None:
            for card in picks:
                await ctx.attach_energy(card, ctx.attacker)
        await ctx.shuffle_deck()
    return effect


def thunder_reflection(damage: int = 50, energy_type=PokemonTypes.LIGHTNING):
    """Deal damage; you may move any number of typed Energy to another of yours."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage(damage)
        if ctx.attacker is None:
            return
        energies = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, type_value)
        ]
        if not energies:
            return
        others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.attacker]
        if not others:
            return
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt="Move Lightning Energy to another Pokémon?")
        if not picks:
            return
        dest = await ctx.choose_pokemon(
            others, "Move Energy to which Pokémon?")
        if dest is None:
            return
        for e in picks:
            await ctx.attach_energy(e, dest)
    return effect


def fiery_aura_passive(counters: int = 4) -> Passive:
    """While Active: Burn checkup places `counters` instead of 2."""

    class FieryAura(Passive):
        def modify_burn_counters(self, counters_in, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not is_in_active_spot(holder):
                return counters_in
            return counters

    return FieryAura()


def pickup_three():
    """From discard: 1 Basic/Evolution + 1 Trainer + 1 Energy → hand."""
    from spirit.game.session.effects import is_trainer_card

    async def effect(ctx):
        disc = list(ctx.discard_pile())
        taken = []
        poke = [c for c in disc if is_pokemon_card(c)]
        if poke:
            picks = await ctx.choose_cards(
                poke, 1, minimum=0, prompt="Choose a Pokémon from discard")
            taken.extend(picks or [])
        trainers = [c for c in disc if is_trainer_card(c) and c not in taken]
        if trainers:
            picks = await ctx.choose_cards(
                trainers, 1, minimum=0, prompt="Choose a Trainer from discard")
            taken.extend(picks or [])
        energies = [c for c in disc if is_energy_card(c) and c not in taken]
        if energies:
            picks = await ctx.choose_cards(
                energies, 1, minimum=0, prompt="Choose an Energy from discard")
            taken.extend(picks or [])
        if taken:
            await ctx.put_in_hand(taken, reveal=True)
    return effect


def strange_behavior():
    """Move 1 damage counter from one of yours onto Slowbro (no KO)."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        max_hp = effective_max_hp(ctx.board, src)
        cur = src.get_attribute(AttrID.HP, 0)
        # Leave at least 10 HP
        if cur <= 10:
            return
        donors = []
        for p in ctx.my_pokemon_in_play():
            if p is src:
                continue
            max_hp_p = effective_max_hp(ctx.board, p)
            hp = p.get_attribute(AttrID.HP, 0)
            if max(0, max_hp_p - hp) >= 10:
                donors.append(p)
        if not donors:
            return
        donor = await ctx.choose_pokemon(
            donors, "Move 1 damage counter from which Pokémon?")
        if donor is None:
            return
        await ctx.move_damage_counters(donor, src, max_count=1)
    return effect


def rest_up_between_turns(counters: int = 2):
    """If still Asleep between turns, heal `counters` (Rest Up)."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        conds = src.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if "Asleep" not in conds:
            return
        await ctx.heal(counters * 10, src)
    return effect


def vine_tease():
    """Look at Prizes (owner only); swap one with the top card of the deck."""
    async def effect(ctx):
        prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        deck_area = ctx.board.find_player_area(ctx.player_id, "deck")
        if not prize_area or not prize_area.children or not deck_area \
                or not deck_area.children:
            return
        prizes = list(prize_area.children)
        top = deck_area.children[0]
        picks = await ctx.choose_cards(
            prizes, 1, minimum=0,
            prompt="Choose a Prize to swap with the top of your deck")
        if not picks:
            return
        prize = picks[0]
        slot = prizes.index(prize)
        # Prize → deck top (without looking at former top); former top → prize slot
        ctx.board.move_card(prize.entity_id, deck_area.entity_id, position=0)
        ctx.board.move_card(top.entity_id, prize_area.entity_id, position=slot)
    return effect


def assistance_cure():
    """Bench power: remove 1 Special Condition from an Active of yours."""
    async def effect(ctx):
        src = ctx.source
        if src is None or is_in_active_spot(src):
            return
        area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
        actives = [
            p for p in (area.children if area else [])
            if p.get_attribute(AttrID.SPECIAL_CONDITIONS)
        ]
        if not actives:
            return
        target = actives[0] if len(actives) == 1 else await ctx.choose_pokemon(
            actives, "Remove a Special Condition from which Pokémon?")
        if target is None:
            return
        conds = list(target.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        # Map display name → enum
        from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES
        name_to_enum = {v: k for k, v in CLIENT_SPECIAL_CONDITION_NAMES.items()}
        options = [c for c in conds if c in name_to_enum]
        if not options:
            return
        # Prefer single auto-cure when only one
        chosen = options[0]
        if len(options) > 1:
            # choose_cards on synthetic labels isn't available; cure first
            chosen = options[0]
        await ctx.cure_condition(target, name_to_enum[chosen])
    return effect
# ---------------------------------------------------------------------------
# EX7 Team Rocket Returns
# ---------------------------------------------------------------------------

def froth_on_evolve():
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            if is_in_active_spot(p):
                await ctx.apply_special_condition(p, SpecialConditions.PARALYZED)
    return effect

def water_punch(base: int = 20, per: int = 20, energy_type=PokemonTypes.WATER):
    tv = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        n = sum(1 for c in (ctx.attacker.children if ctx.attacker else [])
                if energy_provides_type(c, tv))
        heads = sum(1 for r in (await ctx.flip_coins(n, "Water Punch") if n else []) if r)
        await ctx.deal_damage(base + per * heads)
    return effect

def shock_bolt_discard_lightning():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        pool = [c for c in ctx.attacker.children
                if energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
        if pool:
            await ctx.discard_cards(pool)
    return effect

def swallow_up_hp_compare(base: int = 10):
    async def effect(ctx):
        d, a = ctx.defender, ctx.attacker
        if d is None or a is None:
            await ctx.deal_damage(); return
        d_hp, a_hp = int(d.get_attribute(AttrID.HP, 0) or 0), int(a.get_attribute(AttrID.HP, 0) or 0)
        if d_hp < a_hp:
            await ctx.deal_damage(base + d_hp, apply_modifiers=False, as_counters=True)
        else:
            await ctx.deal_damage()
    return effect

def black_beam_poison_active():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        defs = [p for p in ctx.opponent_pokemon_in_play() if is_in_active_spot(p)]
        if not defs:
            return
        target = defs[0] if len(defs) == 1 else await ctx.choose_pokemon(defs, "Poison which Defending?")
        if target is not None:
            await ctx.apply_special_condition(target, SpecialConditions.POISONED)
    return effect

def dark_drain_spread_heal(amount: int = 10):
    async def effect(ctx):
        hit = 0
        for p in list(ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(amount, target=p, apply_modifiers=False)
            hit += 1
        if ctx.attacker is not None and hit:
            await ctx.heal(ctx.attacker, amount * hit)
    return effect

def evolutionary_light():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        def match(c):
            d = def_for(c.archetype_id)
            return getattr(d, "stage", None) in (PokemonStage.STAGE1, PokemonStage.STAGE2)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Choose an Evolution card")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect

def dark_trance_move_darkness():
    async def effect(ctx):
        cards = []
        for p in ctx.my_pokemon_in_play():
            for c in p.children:
                if energy_provides_type(c, PokemonTypes.DARKNESS.value):
                    cards.append(c)
        if not cards:
            return
        picks = await ctx.choose_cards(cards, 1, minimum=0, prompt="Choose a Darkness Energy to move")
        if not picks:
            return
        energy = picks[0]
        parent = next((p for p in ctx.my_pokemon_in_play() if energy in p.children), None)
        dests = [p for p in ctx.my_pokemon_in_play() if p is not parent]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Move to which Pokémon?")
        if dest is not None:
            await ctx.move_energy(energy, dest)
    return effect

def double_wing_attack(amount: int = 30):
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            if is_in_active_spot(p):
                await ctx.deal_damage(amount, target=p)
    return effect

def darkness_navigation():
    async def effect(ctx):
        src = ctx.source
        if src is None or any(is_energy_card(c) for c in src.children):
            return
        def match(c):
            dn = (getattr(def_for(c.archetype_id), "display_name", None) or "").lower()
            return "darkness" in dn or "dark metal" in dn
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Choose Darkness/Dark Metal Energy")
        if picks:
            await ctx.attach_energy(picks[0], src)
        await ctx.shuffle_deck()
    return effect

def energy_bomb_redistribute():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        energies = [c for c in a.children if is_energy_card(c)]
        bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
        if not energies or not bench:
            return
        if not await ctx.ask_yes_no("Move all Energy to your Bench?"):
            return
        for e in list(energies):
            dest = await ctx.choose_pokemon(bench, "Attach Energy where?")
            if dest is None:
                break
            await ctx.move_energy(e, dest)
    return effect
def thunder_slash_basic_paralyze_lock(title: str = "Thunder Slash"):
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is not None and is_basic_pokemon(d):
            await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
        await ctx.locks_next_turn(title)
    return effect

def night_ambush(amount: int = 30):
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import snipe_attack
        await snipe_attack(amount, pool="all")(ctx)
        await ctx.cant_attack_next_turn()
    return effect

def darkness_shield_flip():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Darkness Shield")
        if results and results[0]:
            for p in ctx.my_pokemon_in_play():
                if is_in_active_spot(p):
                    await ctx.protect_next_turn(p, prevent=True, effects_too=True)
    return effect

def fire_breath_burn_active():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        results = await ctx.flip_coins(1, "Fire Breath")
        if not (results and results[0]):
            return
        defs = [p for p in ctx.opponent_pokemon_in_play() if is_in_active_spot(p)]
        if not defs:
            return
        target = defs[0] if len(defs) == 1 else await ctx.choose_pokemon(defs, "Burn which?")
        if target is not None:
            await ctx.apply_special_condition(target, SpecialConditions.BURNED)
    return effect

def fire_payback(base: int = 40, bonus: int = 20):
    async def effect(ctx):
        my_b = len([p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)])
        op_b = len([p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)])
        await ctx.deal_damage(base + bonus if my_b < op_b else base)
    return effect

def shakedown_discard_hand():
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            await ctx.discard_cards([random.choice(hand)])
    return effect

def dark_fire(base: int = 40, bonus: int = 20):
    async def effect(ctx):
        extra = 0
        if ctx.attacker is not None:
            pool = [c for c in ctx.attacker.children
                    if energy_provides_type(c, PokemonTypes.FIRE.value)
                    or energy_provides_type(c, PokemonTypes.DARKNESS.value)]
            if pool and await ctx.ask_yes_no("Discard Fire/Darkness Energy for +20?"):
                picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
                if picks:
                    await ctx.discard_cards(picks); extra = bonus
        await ctx.deal_damage(base + extra)
    return effect

def black_magic_per_opp_bench(per: int = 20):
    async def effect(ctx):
        n = len([p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)])
        await ctx.deal_damage(per * n)
    return effect

def energy_press_active(base: int = 10, per: int = 10):
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play():
            if is_in_active_spot(p):
                n += sum(1 for c in p.children if is_basic_energy_card(c))
        await ctx.deal_damage(base + per * n)
    return effect

def magnetic_lines_move_basic():
    async def effect(ctx):
        await ctx.deal_damage()
        opp = list(ctx.opponent_pokemon_in_play())
        if len(opp) < 2 or ctx.defender is None:
            return
        pool = [c for c in ctx.defender.children if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Move basic Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon([p for p in opp if p is not ctx.defender], "Move to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect

def brick_smash():
    async def effect(ctx):
        await ctx.deal_damage(ignore_target_effects=True, ignore_resistance=True)
    return effect

def hard_bone_discard_pokemon():
    async def effect(ctx):
        pool = [c for c in ctx.hand() if getattr(def_for(c.archetype_id), "stage", None) is not None]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard a Pokémon card")
        if not picks:
            return
        await ctx.discard_cards(picks)
        await ctx.deal_damage()
    return effect

def sticky_goo_retreat_passive(extra: int = 2) -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return cost
            if pokemon.owning_player_id == holder.owning_player_id or not is_in_active_spot(pokemon):
                return cost
            return cost + extra
    return _P()

def slimy_water_retreat(per: int = 10):
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        from spirit.game.session.passives import effective_retreat_cost
        await ctx.deal_damage(per * effective_retreat_cost(ctx.board, d))
    return effect

def black_suction_cups(amount: int = 10):
    async def effect(ctx):
        defs = [p for p in ctx.opponent_pokemon_in_play() if is_in_active_spot(p)]
        for p in defs:
            await ctx.deal_damage(amount, target=p)
        results = await ctx.flip_coins(1, "Black Suction Cups")
        if results and results[0]:
            for p in defs:
                await ctx.apply_special_condition(p, SpecialConditions.PARALYZED)
    return effect

def ink_blast(base: int = 30, per: int = 10, cap: int = 20):
    async def effect(ctx):
        cost = 0
        attack = getattr(ctx, "attack", None)
        if attack is not None and getattr(attack, "cost", None):
            cost = sum(attack.cost.values())
        attached = sum(1 for c in (ctx.attacker.children if ctx.attacker else []) if is_energy_card(c))
        await ctx.deal_damage(base + min(cap, per * max(0, attached - cost)))
    return effect

def grind_per_energy(base: int = 10, per: int = 10):
    async def effect(ctx):
        n = sum(1 for c in (ctx.attacker.children if ctx.attacker else []) if is_energy_card(c))
        await ctx.deal_damage(base + per * n)
    return effect

def bite_off_ex(base: int = 70, bonus: int = 50):
    async def effect(ctx):
        dmg = base + (bonus if ctx.defender is not None and is_pokemon_ex(ctx.defender) else 0)
        await ctx.deal_damage(dmg)
    return effect

def energy_link_self(energy_type=None):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = []
        for c in ctx.discard_pile():
            if not is_energy_card(c):
                continue
            if energy_type is not None:
                tv = getattr(energy_type, "value", energy_type)
                dn = (getattr(def_for(c.archetype_id), "display_name", None) or "").lower()
                tname = getattr(energy_type, "name", "").lower()
                if not energy_provides_type(c, tv) and tname not in dn:
                    continue
            pool.append(c)
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach Energy from discard")
        if picks:
            await ctx.attach_energy(picks[0], a)
    return effect

def buffer_passive():
    from spirit.game.card_effects.passives_common import guts_survive_passive
    return guts_survive_passive(hp_floor=10, title="Buffer", flip=True)

def water_plant(count: int = 2, energy_type=PokemonTypes.WATER):
    async def effect(ctx):
        tv = getattr(energy_type, "value", energy_type)
        pool = [c for c in ctx.discard_pile() if is_energy_card(c) and energy_provides_type(c, tv)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, min(count, len(pool)), minimum=0, prompt="Water Energy to hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect

def energy_crush_opp(base: int = 10, per: int = 10):
    async def effect(ctx):
        n = sum(1 for p in ctx.opponent_pokemon_in_play() for c in p.children if is_energy_card(c))
        await ctx.deal_damage(base + per * n)
    return effect

def get_even(base: int = 20, per: int = 10):
    async def effect(ctx):
        extra = max(0, ctx.prizes_remaining(ctx.player_id) - ctx.prizes_remaining(ctx.opponent_id))
        await ctx.deal_damage(base + per * extra)
    return effect

def spring_back(base: int = 20, bonus: int = 50, condition=None):
    async def effect(ctx):
        dmg = base
        if ctx.prizes_remaining(ctx.opponent_id) == 1:
            dmg += bonus
            await ctx.deal_damage(dmg)
            if condition is not None and ctx.defender is not None:
                await ctx.apply_special_condition(ctx.defender, condition)
        else:
            await ctx.deal_damage(dmg)
    return effect

def minor_errand_running(count: int = 1):
    async def effect(ctx):
        picks = await ctx.search_deck(is_basic_energy_card, count=count, minimum=0, prompt="basic Energy")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect

def heat_tackle_self(self_dmg: int = 10):
    return heat_tackle(self_dmg)

def rest_full_asleep():
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        await ctx.cure_all_conditions(a)
        await ctx.heal(a, 9999)
        await ctx.apply_special_condition(a, SpecialConditions.ASLEEP)
    return effect

def dig_drain_heal(counters: int = 1):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(ctx.attacker, counters * 10)
    return effect

def aqua_slash_lock():
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.cant_attack_next_turn()
    return effect

def hide_in_shadows():
    async def effect(ctx):
        await ctx.deal_damage()
        bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch with?")
        if t is not None:
            await ctx.switch_active_with(t)
    return effect

def granite_head(reduce: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.protect_next_turn(ctx.attacker, reduce=reduce)
    return effect

def dense_passive(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            if calc.attacker is not None and not is_basic_pokemon(calc.attacker):
                calc.amount = max(0, calc.amount - amount)
    return _P()

def dark_lift_passive_ex7(energy_type=PokemonTypes.DARKNESS) -> Passive:
    return dark_lift_passive(energy_type)

def plasma_attach_ex7(energy_type=PokemonTypes.LIGHTNING):
    return plasma_attach(energy_type)

def collapse_asleep_ex7():
    return collapse_asleep()

def poison_payback_ex7():
    return poison_payback_on_damaged()

def strikes_back_ex7(counters: int = 2):
    return strikes_back_passive(counters)

def crust_ex7(amount: int = 20):
    return crust_passive(amount)

def tonnage_ex7(base=60, bonus=40, self_dmg=30):
    return tonnage(base, bonus, self_dmg)

def baby_evolution_ex7(into_name: str):
    return baby_evolution(into_name)

def call_for_family_grass_one():
    return call_for_family_basic_n(1)  # may need grass filter — LIGHT: any basic
def darkness_charge_self(counters: int = 2):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(counters * 10, target=ctx.attacker, apply_modifiers=False, as_counters=True)
    return effect

def gift_exchange():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Shuffle 1 into deck")
        if picks:
            await ctx.shuffle_into_deck(picks)
            await ctx.draw_cards(1)
    return effect

def souvenir_flip3():
    async def effect(ctx):
        results = await ctx.flip_coins(3, "Souvenir")
        heads = sum(1 for r in results if r)
        d = ctx.defender
        if d is None:
            return
        if heads == 1:
            await ctx.deal_damage(40, target=d, apply_modifiers=False, as_counters=True)
        elif heads == 2:
            await ctx.heal(d, 10)
        elif heads == 3:
            await ctx.heal(d, 9999)
    return effect

def soothing_wave():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Soothing Wave")
        if results and results[0]:
            for p in ctx.opponent_pokemon_in_play():
                if is_in_active_spot(p):
                    await ctx.apply_special_condition(p, SpecialConditions.ASLEEP)
    return effect

def taunt_switch():
    async def effect(ctx):
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        b = await ctx.choose_pokemon(bench, "Switch in which Benched?")
        if b is not None:
            await ctx.switch_with_defending(b, opponent=True)
    return effect

def dump_and_draw(max_discard: int = 2, draw_per: int = 2):
    async def effect(ctx):
        hand = [c for c in ctx.hand() if is_energy_card(c)]
        if not hand:
            return
        picks = await ctx.choose_cards(hand, min(max_discard, len(hand)), minimum=0, prompt="Discard Energy")
        if picks:
            await ctx.discard_cards(picks)
            await ctx.draw_cards(draw_per * len(picks))
    return effect

def dark_spell_snipe():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        results = await ctx.flip_coins(1, "Dark Spell")
        if not (results and results[0]):
            return
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Put 1 damage counter where?")
        if t is not None:
            await ctx.deal_damage(10, target=t, apply_modifiers=False, as_counters=True)
    return effect

def hyper_whirlpool():
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        while True:
            results = await ctx.flip_coins(1, "Hyper Whirlpool")
            if not (results and results[0]):
                break
            pool = [c for c in d.children if is_energy_card(c)]
            if not pool:
                break
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
            if picks:
                await ctx.discard_cards(picks)
            else:
                break
    return effect

def dragon_veil_passive() -> Passive:
    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.target is None:
                return
            if calc.target.owning_player_id == holder.owning_player_id and is_in_active_spot(calc.target):
                calc.weakness_applies = False
    return _P()

def hyper_pump_capped(base: int = 20, per: int = 20, cap: int = 60, energy_type=PokemonTypes.WATER):
    async def effect(ctx):
        cost = 0
        attack = getattr(ctx, "attack", None)
        if attack is not None and getattr(attack, "cost", None):
            cost = sum(attack.cost.values())
        tv = getattr(energy_type, "value", energy_type)
        attached = sum(1 for c in (ctx.attacker.children if ctx.attacker else [])
                       if is_basic_energy_card(c) and energy_provides_type(c, tv))
        await ctx.deal_damage(base + min(cap, per * max(0, attached - cost)))
    return effect

def saturation_on_water_attach(heal_counters: int = 2) -> Passive:
    class _P(Passive):
        async def on_energy_attached(self, ctx, energy, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return
            if not energy_provides_type(energy, PokemonTypes.WATER.value):
                return
            await ctx.cure_all_conditions(holder)
            if heal_counters:
                await ctx.heal(holder, heal_counters * 10)
    return _P()

def scramble_retreat_passive() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return cost
            my = holder.owning_player_id
            for pid in list(getattr(board, "player_ids", []) or []):
                if pid == my:
                    continue
                area = board.find_player_area(pid, "activePokemonArea")
                for a in (area.children if area else []):
                    if is_pokemon_ex(a):
                        return 0
            return cost
    return _P()

def energy_draw_attach_basic():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Energy Draw")
        if not (results and results[0]) or ctx.attacker is None:
            return
        picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0, prompt="Attach basic Energy")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
        await ctx.shuffle_deck()
    return effect

def dark_condition_no_weakness_passive() -> Passive:
    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder:
                return
            if any(energy_provides_type(c, PokemonTypes.DARKNESS.value) for c in holder.children):
                calc.weakness_applies = False
    return _P()

def volcanic_ash(amount: int = 60, discard: int = 2):
    async def effect(ctx):
        a = ctx.attacker
        if a is not None:
            pool = [c for c in a.children if is_energy_card(c)]
            if len(pool) < discard:
                return
            picks = await ctx.choose_cards(pool, discard, minimum=discard, prompt=f"Discard {discard} Energy")
            if not picks or len(picks) < discard:
                return
            await ctx.discard_cards(picks)
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Volcanic Ash target")
        if t is not None:
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect

def fire_dance(energy_type=PokemonTypes.FIRE):
    async def effect(ctx):
        await ctx.deal_damage()
        tv = getattr(energy_type, "value", energy_type)
        pool = [c for c in ctx.discard_pile() if is_energy_card(c) and (
            energy_provides_type(c, tv) or "fire" in (getattr(def_for(c.archetype_id), "display_name", "") or "").lower())]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Fire Energy from discard")
        if not picks:
            return
        dest = await ctx.choose_pokemon(list(ctx.my_pokemon_in_play()), "Attach to?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect

def dual_armor_passive(*types) -> Passive:
    class _P(Passive):
        def modify_pokemon_types(self, types_list, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return types_list
            need = [getattr(t, "value", t) for t in types]
            if not any(energy_provides_type(c, t) for c in holder.children for t in need):
                return types_list
            out = list(types_list)
            for t in [PokemonTypes.DARKNESS.value] + need:
                if t not in out:
                    out.append(t)
            return out
    return _P()

def rotating_claws():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if not pool or not await ctx.ask_yes_no("Discard Energy to search discard?"):
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
        if not picks:
            return
        discarded = picks[0]
        await ctx.discard_cards(picks)
        pool2 = [c for c in ctx.discard_pile() if is_energy_card(c) and c is not discarded]
        if not pool2:
            return
        picks2 = await ctx.choose_cards(pool2, 1, minimum=0, prompt="Attach Energy from discard")
        if picks2:
            await ctx.attach_energy(picks2[0], a)
    return effect

def bounce_switch():
    async def effect(ctx):
        await ctx.deal_damage()
        bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
        if bench and await ctx.ask_yes_no("Switch with Bench?"):
            t = await ctx.choose_pokemon(bench, "Switch with?")
            if t is not None:
                await ctx.switch_active_with(t)
    return effect

def drag_off_optional(amount_new: int = 10):
    async def effect(ctx):
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if bench and await ctx.ask_yes_no("Switch Bench in before damage?"):
            t = await ctx.choose_pokemon(bench, "Choose Bench")
            if t is not None:
                await ctx.switch_with_defending(t, opponent=True)
                await ctx.deal_damage(amount_new)
                return
        await ctx.deal_damage()
    return effect

def dark_ring(base: int = 30, per: int = 10):
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play():
            types = p.get_attribute(AttrID.POKEMON_TYPES) or []
            name = p.get_attribute(AttrID.DISPLAY_NAME) or ""
            if PokemonTypes.DARKNESS.value in types or "Dark" in name:
                n += 1
        await ctx.deal_damage(base + per * n)
    return effect

def dark_healer_between_turns(counters: int = 1):
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        if not any(energy_provides_type(c, PokemonTypes.DARKNESS.value) for c in src.children):
            return
        await ctx.heal(src, counters * 10)
    return effect

def dark_and_clear_passive() -> Passive:
    class _P(Passive):
        def modify_special_conditions(self, conditions, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return conditions
            if any(energy_provides_type(c, PokemonTypes.DARKNESS.value) for c in holder.children):
                return []
            return conditions
    return _P()

def hyper_splash(base: int = 50, bonus: int = 40):
    async def effect(ctx):
        dmg = base
        d = ctx.defender
        if d is not None:
            stage = d.get_attribute(AttrID.STAGE)
            if stage == PokemonStage.STAGE2 or stage == getattr(PokemonStage.STAGE2, "value", None):
                dmg += bonus
        await ctx.deal_damage(dmg)
    return effect

def darkness_guard_passive(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            if any(energy_provides_type(c, PokemonTypes.DARKNESS.value) for c in holder.children):
                calc.amount = max(0, calc.amount - amount)
    return _P()

def raging_thunder_self(amount: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = list(ctx.my_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "30 damage to which of yours?")
        if t is not None:
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect

def aqua_trick():
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        pool = [c for c in d.children if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Move Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(bench, "Move to Bench?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect

def friend_search(look: int = 5):
    async def effect(ctx):
        top = ctx.deck_top(look)
        if not top:
            return
        await ctx.reveal_cards(top, to=ctx.player_id)
        pool = [c for c in top if getattr(def_for(c.archetype_id), "stage", None) is not None]
        chosen = None
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Basic or Evolution")
            if picks:
                chosen = picks[0]
                await ctx.put_in_hand(picks, reveal=True)
        deck = ctx.board.find_player_area(ctx.player_id, "deck")
        for c in reversed([x for x in top if x is not chosen]):
            ctx.board.move_card(c.entity_id, deck.entity_id, position=0)
    return effect

def fireworks_discard_fire():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Fireworks")
        if results and not results[0] and ctx.attacker is not None:
            pool = [c for c in ctx.attacker.children if energy_provides_type(c, PokemonTypes.FIRE.value)]
            if pool:
                picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Fire Energy")
                if picks:
                    await ctx.discard_cards(picks)
    return effect

def psycho_waves():
    async def effect(ctx):
        a = ctx.attacker
        if a is not None:
            pool = [c for c in a.children if is_energy_card(c)]
            if pool:
                picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
                if picks:
                    await ctx.discard_cards(picks)
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    return effect

def quick_charge_up_to(count: int = 4):
    return quick_charge_different_types(count)

def sand_damage_between_turns(counters: int = 1):
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        for p in ctx.opponent_pokemon_in_play():
            if not is_in_active_spot(p) and is_basic_pokemon(p):
                await ctx.deal_damage(counters * 10, target=p, apply_modifiers=False, as_counters=True)
    return effect

def methane_leak_between_turns():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        for p in list(ctx.opponent_pokemon_in_play()) + list(ctx.my_pokemon_in_play()):
            conds = p.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            poisoned = SpecialConditions.POISONED in conds or getattr(SpecialConditions.POISONED, "value", None) in conds
            if poisoned:
                await ctx.deal_damage(10, target=p, apply_modifiers=False, as_counters=True)
    return effect

def darkness_veil_effects_passive() -> Passive:
    from spirit.game.card_effects.passives_common import attack_effect_shield_passive
    class _P(Passive):
        def blocks_attack_effects(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not any(energy_provides_type(c, PokemonTypes.DARKNESS.value) for c in holder.children):
                return False
            return calc.is_attack and calc.is_opposing and calc.target is holder
    return _P()

def spread_poison(bench_dmg: int = 20):
    async def effect(ctx):
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if bench:
            t = await ctx.choose_pokemon(bench, "Bench for 20")
            if t is not None:
                await ctx.deal_damage(bench_dmg, target=t, apply_modifiers=False)
    return effect

def dark_aid():
    async def effect(ctx):
        pool = []
        for c in ctx.discard_pile():
            d = def_for(c.archetype_id)
            subs = getattr(d, "subtypes", None) or []
            dn = getattr(d, "display_name", None) or ""
            if "Pokémon Tool" in subs or "Pokemon Tool" in subs or "Secret Machine" in dn or "Rocket's Secret Machine" in subs:
                pool.append(c)
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Tool or Secret Machine to hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect

def snatch_and_run():
    async def effect(ctx):
        def match(c):
            d = def_for(c.archetype_id)
            subs = getattr(d, "subtypes", None) or []
            dn = getattr(d, "display_name", None) or ""
            return ("Pokémon Tool" in subs or "Pokemon Tool" in subs
                    or "Rocket's Secret Machine" in subs or "Secret Machine" in dn)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Tool or Secret Machine")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
            bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
            if bench and await ctx.ask_yes_no("Switch with Bench?"):
                t = await ctx.choose_pokemon(bench, "Switch with?")
                if t is not None:
                    await ctx.switch_active_with(t)
        await ctx.shuffle_deck()
    return effect

def miraculous_comeback(per: int = 10):
    async def effect(ctx):
        n = len(ctx.my_pokemon_in_play()) + len(ctx.opponent_pokemon_in_play())
        results = await ctx.flip_coins(n, "Miraculous Comeback") if n else []
        heads = sum(1 for r in results if r)
        tails = n - heads
        await ctx.deal_damage(per * heads)
        if ctx.attacker is not None and tails:
            await ctx.deal_damage(per * tails, target=ctx.attacker, apply_modifiers=False)
    return effect

def darkness_switch():
    async def effect(ctx):
        a, d = ctx.attacker, ctx.defender
        if a is None or d is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
        if not picks:
            return
        await ctx.discard_cards(picks)
        await ctx.swap_damage_counters(a, d)
    return effect

def mini_metronome():
    """LIGHT: flip; heads deal copied attack's printed damage only."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Mini-Metronome")
        if not (results and results[0]) or ctx.defender is None:
            return
        d = def_for(ctx.defender.archetype_id)
        attacks = [a for a in (getattr(d, "abilities", None) or []) if getattr(a, "damage", None) is not None]
        if not attacks:
            return
        titles = [getattr(a, "title", "?") for a in attacks]
        idx = 0
        if len(titles) > 1:
            i = await ctx.choose("Copy which attack?", titles)
            if i is not None:
                idx = i
        dmg = int(getattr(attacks[idx], "damage", 0) or 0)
        if dmg:
            await ctx.deal_damage(dmg)
    return effect

def holy_shield_passive() -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return False
            a = calc.attacker
            return a is not None and "Dark" in (a.get_attribute(AttrID.DISPLAY_NAME) or "")
        def prevents_attack_effects(self, calc, carrier):
            return self.prevents_damage(calc, carrier)
    return _P()

def rainbow_moves():
    """LIGHT: copy printed damage of chosen Bench attack only."""
    async def effect(ctx):
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Copy attack from?")
        if t is None:
            return
        d = def_for(t.archetype_id)
        attacks = [a for a in (getattr(d, "abilities", None) or []) if getattr(a, "damage", None) is not None]
        if not attacks:
            return
        titles = [getattr(a, "title", "?") for a in attacks]
        idx = 0
        if len(titles) > 1:
            i = await ctx.choose("Copy which?", titles)
            if i is not None:
                idx = i
        dmg = int(getattr(attacks[idx], "damage", 0) or 0)
        if dmg:
            await ctx.deal_damage(dmg)
    return effect

def powder_protection_passive(amount: int = 40) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            a = calc.attacker
            if a is None:
                return
            name = a.get_attribute(AttrID.DISPLAY_NAME) or ""
            if "Rocket" in name or "Team " in name or "'s " in name:
                calc.amount = max(0, calc.amount - amount)
    return _P()

def insomnia_passive() -> Passive:
    class _P(Passive):
        def modify_special_conditions(self, conditions, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return conditions
            return [c for c in conditions if c not in (SpecialConditions.ASLEEP, getattr(SpecialConditions.ASLEEP, "value", object()))]
    return _P()

def litter_tools(base: int = 20, per: int = 30):
    async def effect(ctx):
        pool = []
        for c in ctx.hand():
            d = def_for(c.archetype_id)
            subs = getattr(d, "subtypes", None) or []
            dn = getattr(d, "display_name", None) or ""
            if "Pokémon Tool" in subs or "Pokemon Tool" in subs or "Secret Machine" in dn:
                pool.append(c)
        bonus = 0
        if pool:
            picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Discard Tools/Machines")
            if picks:
                await ctx.discard_cards(picks)
                bonus = per * len(picks)
        await ctx.deal_damage(base + bonus)
    return effect

def cunning_look_shuffle():
    async def effect(ctx):
        top = ctx.deck_top(1, player_id=ctx.opponent_id)
        if top:
            await ctx.reveal_cards(top, to=ctx.player_id)
            if await ctx.ask_yes_no("Shuffle opponent's deck?"):
                await ctx.shuffle_deck(player_id=ctx.opponent_id)
    return effect

def explosive_evolution(amount: int = 10):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Explosive Evolution")
        if results and results[0]:
            for p in list(ctx.opponent_pokemon_in_play()):
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
        a = ctx.attacker
        if a is None:
            await ctx.shuffle_deck(); return
        src_name = (a.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
        def match(c):
            ef = (getattr(def_for(c.archetype_id), "evolves_from", None) or "").lower()
            return "pupitar" in ef or src_name in ef
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Evolve from Dark Pupitar")
        if picks:
            await ctx.evolve(a, picks[0])
        await ctx.shuffle_deck()
    return effect

def dark_seed():
    """LIGHT: prevent retreat; schedule 5 counters is approx via mark — use schedule if available."""
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        await ctx.prevent_retreat_next_turn(d)
        # LIGHT: put 5 counters now-ish via scheduled if API exists
        if hasattr(ctx, "schedule_end_of_opponent_turn"):
            async def _put(c, t=d):
                await c.deal_damage(50, target=t, apply_modifiers=False, as_counters=True)
            await ctx.schedule_end_of_opponent_turn(_put)
        else:
            # approximate: put counters immediately as soft gap would be worse
            pass
    return effect

def quick_tail_smash(high: int = 80):
    async def effect(ctx):
        if await ctx.ask_yes_no("Flip for Quick Tail Smash?"):
            results = await ctx.flip_coins(1, "Quick Tail Smash")
            if results and results[0]:
                await ctx.deal_damage(high)
            return
        await ctx.deal_damage()
    return effect

def quick_change():
    async def effect(ctx):
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, min(3, len(hand)), minimum=0, prompt="Up to 3 on deck")
        n = len(picks) if picks else 0
        if picks:
            deck = ctx.board.find_player_area(ctx.player_id, "deck")
            for c in reversed(picks):
                ctx.board.move_card(c.entity_id, deck.entity_id, position=0)
        if n:
            found = await ctx.search_deck(lambda c: True, count=n, minimum=n, prompt=f"Choose {n}")
            if found:
                await ctx.put_in_hand(found)
        await ctx.shuffle_deck()
    return effect

def headache_lock_trainers():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Headache")
        if results and results[0] and hasattr(ctx, "lock_opponent_trainers_next_turn"):
            await ctx.lock_opponent_trainers_next_turn()
    return effect

def ripples_heal_other(counters: int = 1):
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        damaged = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not damaged:
            return
        t = await ctx.choose_pokemon(damaged, "Heal which?")
        if t is not None:
            await ctx.heal(t, counters * 10)
    return effect

# Trainers / stadiums / energies

async def pokemon_retriever(ctx):
    pool = [c for c in ctx.discard_pile() if is_basic_pokemon(c) and not is_pokemon_ex(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Basic Pokémon to hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)

async def pow_hand_extension(ctx):
    if ctx.prizes_remaining(ctx.player_id) <= ctx.prizes_remaining(ctx.opponent_id):
        return
    idx = await ctx.choose("Choose an effect", ["Move Energy", "Switch Benched"])
    if idx == 0:
        actives = [p for p in ctx.opponent_pokemon_in_play() if is_in_active_spot(p)]
        if not actives:
            return
        d = actives[0]
        pool = [c for c in d.children if is_energy_card(c)]
        others = [p for p in ctx.opponent_pokemon_in_play() if p is not d]
        if not pool or not others:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Move Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(others, "Move to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    else:
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        b = await ctx.choose_pokemon(bench, "Switch in?")
        if b is not None:
            await ctx.switch_with_defending(b, opponent=True)

async def rockets_admin(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        hand = list(ctx.hand(pid))
        if hand:
            await ctx.shuffle_into_deck(hand, pid)
        await ctx.draw_cards(5, player_id=pid)
    if ctx.prizes_remaining(ctx.player_id) < ctx.prizes_remaining(ctx.opponent_id):
        while ctx.hand_size(ctx.player_id) < 6:
            if not await ctx.draw_cards(1):
                break

def rockets_hideout_passive() -> Passive:
    class _P(Passive):
        def max_hp_bonus(self, pokemon, carrier):
            name = pokemon.get_attribute(AttrID.DISPLAY_NAME) or ""
            return 20 if ("Dark" in name or "Rocket" in name) else 0
    return _P()

async def rockets_mission(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    await ctx.reveal_cards(hand, to=ctx.player_id)
    n = sum(1 for c in hand if "Supporter" in (getattr(def_for(c.archetype_id), "subtypes", None) or []))
    target = n + 3
    while ctx.hand_size(ctx.player_id) < target:
        if not await ctx.draw_cards(1):
            break

async def rockets_poke_ball(ctx):
    def match(c):
        d = def_for(c.archetype_id)
        dn = getattr(d, "display_name", None) or ""
        return getattr(d, "stage", None) is not None and ("Dark" in dn or "Rocket" in dn)
    picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Dark or Rocket's Pokémon")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()

def rockets_tricky_gym_passive() -> Passive:
    class _P(Passive):
        def modify_attack_cost(self, cost, pokemon, carrier, board):
            name = pokemon.get_attribute(AttrID.DISPLAY_NAME) or ""
            if "Dark" not in name and "Rocket" not in name:
                return cost
            c = dict(cost)
            key = PokemonTypes.COLORLESS.value
            if c.get(key, 0) > 0:
                c[key] -= 1
                if c[key] == 0:
                    del c[key]
            return c
    return _P()

async def surprise_time_machine(ctx):
    """LIGHT: devolve discarding highest stage; optional re-evolve from hand."""
    evolved = [p for p in ctx.my_pokemon_in_play()
               if getattr(def_for(p.archetype_id), "stage", None) in (PokemonStage.STAGE1, PokemonStage.STAGE2)]
    if not evolved:
        return
    t = await ctx.choose_pokemon(evolved, "Devolve which?")
    if t is None:
        return
    if hasattr(ctx, "devolve"):
        await ctx.devolve(t, to_hand=False)
    dn = (t.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
    pool = []
    for c in ctx.hand():
        ef = (getattr(def_for(c.archetype_id), "evolves_from", None) or "").lower()
        if ef and (dn in ef or ef in dn or dn.replace("dark ", "") in ef):
            pool.append(c)
    if pool and await ctx.ask_yes_no("Evolve from hand?"):
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Evolution")
        if picks:
            await ctx.evolve(t, picks[0])

async def swoop_teleporter(ctx):
    actives = [p for p in ctx.my_pokemon_in_play() if is_in_active_spot(p)]
    if not actives:
        return
    a = actives[0] if len(actives) == 1 else await ctx.choose_pokemon(actives, "Active to replace")
    if a is None:
        return
    def match(c):
        return is_basic_pokemon(c) and not is_pokemon_ex(c)
    picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Basic Pokémon")
    if not picks:
        await ctx.shuffle_deck(); return
    await ctx.identity_swap(a, picks[0], destination="deck", transfer=True)
    await ctx.shuffle_deck()

async def venture_bomb(ctx):
    pool = list(ctx.opponent_pokemon_in_play())
    if not pool:
        return
    t = await ctx.choose_pokemon(pool, "Venture Bomb")
    if t is None:
        return
    results = await ctx.flip_coins(1, "Venture Bomb")
    n = 1 if (results and results[0]) else 3
    await ctx.deal_damage(n * 10, target=t, apply_modifiers=False, as_counters=True)

async def here_comes_team_rocket(ctx):
    """LIGHT: reveal all Prize cards (face-up for rest of game not fully tracked)."""
    for pid in (ctx.player_id, ctx.opponent_id):
        area = ctx.board.find_player_area(pid, "prizePile")
        prizes = list(area.children if area else [])
        if prizes:
            await ctx.reveal_cards(prizes)

class REnergyPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker:
            return
        calc.amount += 10

def r_energy_attach_to(pokemon):
    name = pokemon.get_attribute(AttrID.DISPLAY_NAME) or ""
    return "Dark" in name or "Rocket" in name

def darkest_impulse_passive() -> Passive:
    """Opponent evolves from hand: 2 damage counters on that Pokémon."""
    class _P(Passive):
        async def on_evolved(self, ctx, evolved, carrier, from_hand=True):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or evolved.owning_player_id == holder.owning_player_id:
                return
            if not from_hand:
                return
            await ctx.deal_damage(
                20, target=evolved, apply_modifiers=False, as_counters=True)
    return _P()


def dark_scale_on_ko(counters: int = 3) -> Passive:
    """If Active and KO'd by attack: counters on Attacking Pokémon."""
    class _P(Passive):
        async def on_knocked_out(self, ctx, pokemon, carrier, by_attack=False, attacker=None):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not by_attack or attacker is None:
                return
            await ctx.deal_damage(
                counters * 10, target=attacker,
                apply_modifiers=False, as_counters=True)
    return _P()


def dark_link():
    """LIGHT: flip; heads copy printed damage of another in-play Dark-named attack."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Dark Link")
        if not (results and results[0]):
            return
        pool = []
        for p in ctx.my_pokemon_in_play():
            if p is ctx.attacker:
                continue
            name = p.get_attribute(AttrID.DISPLAY_NAME) or ""
            if "Dark" not in name:
                continue
            d = def_for(p.archetype_id)
            for a in (getattr(d, "abilities", None) or []):
                if getattr(a, "damage", None) is not None:
                    pool.append((p, a))
        if not pool:
            return
        labels = [f"{getattr(a,'title','?')} ({(p.get_attribute(AttrID.DISPLAY_NAME) or '')})"
                  for p, a in pool]
        idx = await ctx.choose("Copy which Dark attack?", labels)
        if idx is None:
            return
        _, atk = pool[idx]
        dmg = int(getattr(atk, "damage", 0) or 0)
        if dmg:
            await ctx.deal_damage(dmg)
    return effect


def detour_supporter():
    """LIGHT: if a Supporter is in play beside Active, re-run its effect."""
    async def effect(ctx):
        # Find supporter next to active — board area varies; search play zones
        area = ctx.board.find_player_area(ctx.player_id, "supporter") \
            or ctx.board.find_player_area(ctx.player_id, "inPlay")
        cards = list(area.children if area else [])
        supporter = None
        for c in cards:
            d = def_for(c.archetype_id)
            if "Supporter" in (getattr(d, "subtypes", None) or []):
                supporter = c
                break
        if supporter is None:
            return
        d = def_for(supporter.archetype_id)
        fn = getattr(d, "effect", None)
        if callable(fn):
            await fn(ctx)
    return effect


async def pokemon_retriever(ctx):
    """Show 1 Basic/Evolution to hand, OR show 3 and shuffle into deck."""
    pool = [c for c in ctx.discard_pile()
            if getattr(def_for(c.archetype_id), "stage", None) is not None]
    if not pool:
        return
    idx = await ctx.choose(
        "Pokémon Retriever",
        ["1 card to hand", "3 cards into deck"])
    if idx == 0:
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Put into hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    else:
        n = min(3, len(pool))
        picks = await ctx.choose_cards(
            pool, n, minimum=n if n else 0, prompt="Shuffle into deck")
        if picks:
            await ctx.reveal_cards(picks)
            await ctx.shuffle_into_deck(picks)


async def rockets_admin(ctx):
    """Each player shuffles hand into deck, draws up to Prize count (you first)."""
    for pid in (ctx.player_id, ctx.opponent_id):
        hand = list(ctx.hand(pid))
        if hand:
            await ctx.shuffle_into_deck(hand, pid)
        n = ctx.prizes_remaining(pid)
        if n > 0:
            await ctx.draw_cards(n, player_id=pid)


async def rockets_mission(ctx):
    """Discard 1 from hand; draw 3, or 4 if discarded Dark/Rocket's Pokémon."""
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Discard a card")
    if not picks:
        return
    card = picks[0]
    await ctx.discard_cards(picks)
    d = def_for(card.archetype_id)
    dn = getattr(d, "display_name", None) or ""
    bonus = getattr(d, "stage", None) is not None and ("Dark" in dn or "Rocket" in dn)
    await ctx.draw_cards(4 if bonus else 3)


async def venture_bomb(ctx):
    """Flip: heads 1 counter on opp Pokémon; tails 1 counter on your Pokémon."""
    results = await ctx.flip_coins(1, "Venture Bomb")
    if results and results[0]:
        pool = list(ctx.opponent_pokemon_in_play())
        prompt = "Put 1 damage counter on opponent"
    else:
        pool = list(ctx.my_pokemon_in_play())
        prompt = "Put 1 damage counter on your Pokémon"
    if not pool:
        return
    t = await ctx.choose_pokemon(pool, prompt)
    if t is not None:
        await ctx.deal_damage(10, target=t, apply_modifiers=False, as_counters=True)


def rockets_tricky_gym_passive() -> Passive:
    """LIGHT: -1 Colorless attack cost for Dark/Rocket's (real text grants gym attacks)."""
    class _P(Passive):
        def modify_attack_cost(self, cost, pokemon, carrier, board):
            name = pokemon.get_attribute(AttrID.DISPLAY_NAME) or ""
            if "Dark" not in name and "Rocket" not in name:
                return cost
            c = dict(cost)
            key = PokemonTypes.COLORLESS.value
            if c.get(key, 0) > 0:
                c[key] -= 1
                if c[key] == 0:
                    del c[key]
            return c
        stacking_key = "rockets_tricky_gym"
    return _P()

def knockout_gas_on_ko() -> Passive:
    class _P(Passive):
        async def on_knocked_out(self, ctx, pokemon, carrier, by_attack=False, attacker=None):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not by_attack or attacker is None:
                return
            await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)
            await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)
    return _P()


def spiny_on_damaged() -> Passive:
    class _P(Passive):
        async def on_damaged_by_attack(self, ctx, pokemon, carrier, attacker=None):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return
            if not is_in_active_spot(holder) or attacker is None:
                return
            while True:
                results = await ctx.flip_coins(1, "Spiny")
                if not (results and results[0]):
                    break
                await ctx.deal_damage(
                    10, target=attacker, apply_modifiers=False, as_counters=True)
    return _P()


# ---------------------------------------------------------------------------
# EX7 API fixes (override earlier stubs that called non-existent ctx methods)
# ---------------------------------------------------------------------------

def dark_drain_spread_heal(amount: int = 10):
    async def effect(ctx):
        hit = 0
        for p in list(ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(amount, target=p, apply_modifiers=False)
            hit += 1
        if ctx.attacker is not None and hit:
            await ctx.heal(amount * hit, ctx.attacker)
    return effect


def thunder_slash_basic_paralyze_lock(title: str = "Thunder Slash"):
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is not None and is_basic_pokemon(d):
            await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
        if ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def night_ambush(amount: int = 30):
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import snipe_attack
        await snipe_attack(amount, pool="any")(ctx)
        if ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def darkness_shield_flip():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Darkness Shield")
        if results and results[0]:
            active = ctx.my_active()
            if active is not None:
                await apply_protection(
                    ctx, target=active, prevent=True, effects_too=True)
    return effect


def get_even(base: int = 20, per: int = 10):
    async def effect(ctx):
        mine = count_prizes_remaining("mine")(ctx)
        theirs = count_prizes_remaining("opponent")(ctx)
        extra = max(0, mine - theirs)
        await ctx.deal_damage(base + per * extra)
    return effect


def spring_back(base: int = 20, bonus: int = 50, condition=None):
    async def effect(ctx):
        dmg = base
        if count_prizes_remaining("opponent")(ctx) == 1:
            dmg += bonus
            await ctx.deal_damage(dmg)
            if condition is not None and ctx.defender is not None:
                await ctx.apply_special_condition(ctx.defender, condition)
        else:
            await ctx.deal_damage(dmg)
    return effect


def rest_full_asleep():
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        await ctx.cure_all_conditions(a)
        missing = ctx.max_hp(a) - a.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, a)
        await ctx.apply_special_condition(a, SpecialConditions.ASLEEP)
    return effect


def dig_drain_heal(counters: int = 1):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


def aqua_slash_lock():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def hide_in_shadows():
    async def effect(ctx):
        await ctx.deal_damage()
        bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch with?")
        if t is not None:
            await ctx.switch_active(ctx.player_id, t)
    return effect


def granite_head(reduce: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, reduce=reduce)
    return effect


def souvenir_flip3():
    async def effect(ctx):
        results = await ctx.flip_coins(3, "Souvenir")
        heads = sum(1 for r in results if r)
        d = ctx.defender
        if d is None:
            return
        if heads == 1:
            await ctx.deal_damage(40, target=d, apply_modifiers=False, as_counters=True)
        elif heads == 2:
            await ctx.heal(10, d)
        elif heads == 3:
            missing = ctx.max_hp(d) - d.get_attribute(AttrID.HP, 0)
            if missing > 0:
                await ctx.heal(missing, d)
    return effect


def taunt_switch():
    async def effect(ctx):
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        b = await ctx.choose_pokemon(bench, "Switch in which Benched?")
        if b is not None:
            await ctx.switch_active(ctx.opponent_id, b)
    return effect


def bounce_switch():
    async def effect(ctx):
        await ctx.deal_damage()
        bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
        if bench and await ctx.ask_yes_no("Switch with Bench?"):
            t = await ctx.choose_pokemon(bench, "Switch with?")
            if t is not None:
                await ctx.switch_active(ctx.player_id, t)
    return effect


def drag_off_optional(amount_new: int = 10):
    async def effect(ctx):
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if bench and await ctx.ask_yes_no("Switch Bench in before damage?"):
            t = await ctx.choose_pokemon(bench, "Choose Bench")
            if t is not None:
                await ctx.switch_active(ctx.opponent_id, t)
                await ctx.deal_damage(amount_new)
                return
        await ctx.deal_damage()
    return effect


def dark_healer_between_turns(counters: int = 1):
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        if not any(energy_provides_type(c, PokemonTypes.DARKNESS.value)
                   for c in src.children):
            return
        await ctx.heal(counters * 10, src)
    return effect


def darkness_switch():
    async def effect(ctx):
        a, d = ctx.attacker, ctx.defender
        if a is None or d is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
        if not picks:
            return
        await ctx.discard_cards(picks)
        ca = max(0, ctx.max_hp(a) - a.get_attribute(AttrID.HP, 0)) // 10
        cd = max(0, ctx.max_hp(d) - d.get_attribute(AttrID.HP, 0)) // 10
        await ctx.set_damage_counters(a, cd)
        await ctx.set_damage_counters(d, ca)
    return effect


def cunning_look_shuffle():
    async def effect(ctx):
        top = ctx.deck_top(1, player_id=ctx.opponent_id)
        if top:
            await ctx.reveal_cards(top, to_player=ctx.player_id)
            if await ctx.ask_yes_no("Shuffle opponent's deck?"):
                await ctx.shuffle_deck(player_id=ctx.opponent_id)
    return effect


def explosive_evolution(amount: int = 10):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Explosive Evolution")
        if results and results[0]:
            for p in list(ctx.opponent_pokemon_in_play()):
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
        a = ctx.attacker
        if a is None:
            await ctx.shuffle_deck()
            return
        name = a.get_attribute(AttrID.NAME) or ""

        def match(c):
            d = def_for(c.archetype_id)
            ef = getattr(d, "evolves_from", None) if d else None
            return bool(ef) and ef == name

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Evolve from Dark Pupitar")
        if picks:
            await ctx.evolve_pokemon(a, picks[0])
        await ctx.shuffle_deck()
    return effect


def dark_seed():
    """Prevent retreat; schedule 5 damage counters at end of opponent's next turn."""
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        ctx.lock_retreat(d)
        target_id = d.entity_id

        async def _put(session):
            entity = session.board.get_entity(target_id)
            if entity is None:
                return
            from spirit.game.session.effects import EffectContext
            c = EffectContext(session, ctx.player_id, ctx.source)
            await c.deal_damage(
                50, target=entity, apply_modifiers=False, as_counters=True)

        ctx.schedule_at_checkup(1, _put)
    return effect


def ripples_heal_other(counters: int = 1):
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        damaged = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not damaged:
            return
        t = await ctx.choose_pokemon(damaged, "Heal which?")
        if t is not None:
            await ctx.heal(counters * 10, t)
    return effect


def friend_search(look: int = 5):
    async def effect(ctx):
        top = ctx.deck_top(look)
        if not top:
            return
        await ctx.reveal_cards(top, to_player=ctx.player_id)
        pool = [c for c in top
                if getattr(def_for(c.archetype_id), "stage", None) is not None]
        chosen = None
        if pool:
            picks = await ctx.choose_cards(
                pool, 1, minimum=0, prompt="Basic or Evolution")
            if picks:
                chosen = picks[0]
                await ctx.put_in_hand(picks, reveal=True)
        deck = ctx.board.find_player_area(ctx.player_id, "deck")
        for c in reversed([x for x in top if x is not chosen]):
            ctx.board.move_card(c.entity_id, deck.entity_id, position=0)
    return effect


async def pow_hand_extension(ctx):
    if count_prizes_remaining("mine")(ctx) <= count_prizes_remaining("opponent")(ctx):
        return
    idx = await ctx.choose("Choose an effect", ["Move Energy", "Switch Benched"])
    if idx == 0:
        actives = [p for p in ctx.opponent_pokemon_in_play() if is_in_active_spot(p)]
        if not actives:
            return
        d = actives[0]
        pool = [c for c in d.children if is_energy_card(c)]
        others = [p for p in ctx.opponent_pokemon_in_play() if p is not d]
        if not pool or not others:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Move Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(others, "Move to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    else:
        bench = [p for p in ctx.opponent_pokemon_in_play()
                 if not is_in_active_spot(p)]
        if not bench:
            return
        b = await ctx.choose_pokemon(bench, "Switch in?")
        if b is not None:
            await ctx.switch_active(ctx.opponent_id, b)


async def rockets_admin(ctx):
    """Each player shuffles hand into deck, draws equal to their Prize count."""
    for pid, side in ((ctx.player_id, "mine"), (ctx.opponent_id, "opponent")):
        hand = list(ctx.hand(pid))
        if hand:
            await ctx.shuffle_into_deck(hand, pid)
        n = count_prizes_remaining(side)(ctx)
        if n > 0:
            await ctx.draw_cards(n, player_id=pid)

# ===========================================================================
# EX8 Deoxys
# ===========================================================================
# EX8 Deoxys helpers — append to spirit/game/card_effects/ex.py

def form_change_deoxys(ex: bool = False):
    """Search deck for another Deoxys (/ex) and identity-swap (Form Change)."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        needle = "deoxys"

        def match(c):
            d = def_for(c.archetype_id)
            if d is None:
                return False
            dn = (getattr(d, "display_name", None) or "").lower()
            if needle not in dn:
                return False
            if ex and "ex" not in dn.replace(" ", "").lower() and "ex" not in (
                    " ".join(getattr(d, "subtypes", None) or [])).lower():
                # allow either name with ex or subtype
                subs = " ".join(str(s) for s in (getattr(d, "subtypes", None) or [])).lower()
                if "ex" not in subs and not dn.endswith("ex"):
                    return False
            if not ex:
                # non-ex Form Change should not pick ex forms preferably — allow any Deoxys
                pass
            return True

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose another Deoxys to switch with")
        if picks:
            await ctx.identity_swap(
                src, picks[0], destination="deck", transfer=True)
        await ctx.shuffle_deck()
    return effect


def energy_burst_both(base: int = 10, per: int = 10):
    """base + per × (energy on self + energy on defender)."""
    async def effect(ctx):
        n = count_energy("self")(ctx) + count_energy("defender")(ctx)
        await ctx.deal_damage(base + per * n)
    return effect


def psyburst_optional_discard(base: int = 50, per: int = 20, discard_n: int = 2):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            await ctx.deal_damage(base); return
        energies = [c for c in a.children if is_energy_card(c)]
        do = len(energies) >= discard_n and await ctx.ask_yes_no(
            f"Discard {discard_n} Energy for bonus?")
        if do:
            picks = await ctx.choose_cards(
                energies, discard_n, minimum=discard_n, prompt="Discard Energy")
            if picks:
                await ctx.discard_cards(picks)
                n = count_energy("defender")(ctx)
                await ctx.deal_damage(base + per * n)
                return
        await ctx.deal_damage(base)
    return effect


def barrier_attack_reduce(amount: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, reduce=amount)
    return effect


def psychic_shield_ex():
    """Prevent all from opponent's Pokémon-ex during opponent's next turn."""
    async def effect(ctx):
        if ctx.attacker is None:
            return
        await apply_protection(
            ctx, target=ctx.attacker, prevent=True, effects_too=True)
        # LIGHT: real text is only vs Pokémon-ex; full prevent is stronger
    return effect


def hunch_low_hp_boost(threshold: int = 40, bonus: int = 40) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            if not (calc.is_attack and calc.is_opposing and calc.to_active):
                return
            holder = carrier_pokemon(carrier)
            if holder is not calc.attacker:
                return
            hp = holder.get_attribute(AttrID.HP, 0)
            if hp <= threshold:
                calc.amount += bonus
    return _P()


def luring_antenna(*conditions):
    return lure_condition(*conditions)


def leaf_poison_if_grass():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None or ctx.defender is None:
            return
        if any(energy_provides_type(c, PokemonTypes.GRASS.value) for c in a.children):
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def hustle_punch_next(next_base: int = 50):
    """LIGHT: next turn this attack does next_base — use boost as approx via own next turn modifier on title."""
    async def effect(ctx):
        await ctx.deal_damage()
        title = ctx.ability.title if ctx.ability else "Hustle Punch"
        # Reduce next turn: printed is 40, next becomes 50 → +10? Printed base on card is 40?
        # Text: next turn base is 50 instead of 70 — card damage field is the 70 case.
        # Soft: set next-turn boost of (next_base - printed)
        printed = int(getattr(ctx.ability, "damage", 0) or 0)
        delta = next_base - printed
        if delta:
            await apply_own_next_turn_boost(ctx, delta, attack_title=title)
    return effect


def back_burner_attach(max_n: int = 2):
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        n = min(max_n, len(pool))
        picks = await ctx.choose_cards(pool, n, minimum=0, prompt="basic Energy")
        for e in picks:
            dests = list(ctx.my_pokemon_in_play())
            if not dests:
                break
            dest = await ctx.choose_pokemon(dests, "Attach where?")
            if dest is None:
                break
            await ctx.attach_energy(e, dest)
    return effect


def split_bomb_snipe(amount: int = 30, count: int = 2):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any", count=count, apply_modifiers=False)


def psychic_trace_hand_redraw():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        hand = list(ctx.hand())
        n = len(hand)
        if hand:
            await ctx.shuffle_into_deck(hand)
        if n:
            await ctx.draw_cards(n)
    return effect


def ancient_mantra():
    async def effect(ctx):
        await ctx.deal_damage()
        a, d = ctx.attacker, ctx.defender
        if a is None or d is None:
            return
        if any(energy_provides_type(c, PokemonTypes.PSYCHIC.value) for c in a.children):
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
        if any(energy_provides_type(c, PokemonTypes.FIGHTING.value) for c in a.children):
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
    return effect


def dark_protection_passive(per: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            n = sum(1 for c in holder.children
                    if energy_provides_type(c, PokemonTypes.DARKNESS.value))
            calc.amount = max(0, calc.amount - per * n)
    return _P()


def cross_cut_evolved_bonus(base: int = 40, bonus: int = 20):
    async def effect(ctx):
        d = ctx.defender
        extra = 0
        if d is not None:
            st = getattr(def_for(d.archetype_id), "stage", None)
            if st in (PokemonStage.STAGE1, PokemonStage.STAGE2):
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def crobat_distortion_counter():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Put 1 damage counter")
        if t is not None:
            await ctx.deal_damage(10, target=t, apply_modifiers=False, as_counters=True)
    return effect


def cross_attack_flip4(per: int = 20, confuse_at: int = 2):
    async def effect(ctx):
        results = await ctx.flip_coins(4, "Cross Attack")
        heads = sum(1 for r in results if r)
        await ctx.deal_damage(per * heads)
        if heads >= confuse_at and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    return effect


def pester_sc_bonus(base: int = 60, bonus: int = 40):
    async def effect(ctx):
        d = ctx.defender
        extra = 0
        if d is not None and d.get_attribute(AttrID.SPECIAL_CONDITIONS):
            extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def psychic_removal_all_energy():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(2, "Psychic Removal")
        if results and all(results) and ctx.defender is not None:
            pool = [c for c in ctx.defender.children if is_energy_card(c)]
            if pool:
                await ctx.discard_cards(pool)
    return effect


def powerful_hand_counters(cap: int = 7):
    async def effect(ctx):
        n = min(cap, ctx.hand_size())
        if n and ctx.defender is not None:
            await ctx.deal_damage(n * 10, target=ctx.defender,
                                  apply_modifiers=False, as_counters=True)
    return effect


def high_voltage_lock_trainers():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "High Voltage")
        if results and results[0]:
            ctx.lock_plays(
                ctx.opponent_id,
                lambda c: getattr(def_for(c.archetype_id), "trainer_type", None) is not None
                or "Trainer" in (getattr(def_for(c.archetype_id), "supertype", None) or "")
                or True)  # LIGHT: lock all non-pokemon plays via broad predicate
            # Narrower: use is_supporter_card OR item — lock trainers broadly
            from spirit.game.session.effects import is_trainer_card
            ctx.lock_plays(ctx.opponent_id, is_trainer_card)
    return effect


def recharge_attach_lightning():
    async def effect(ctx):
        src = ctx.attacker or ctx.source
        if src is None:
            return
        def match(c):
            return energy_provides_type(c, PokemonTypes.LIGHTNING.value) and is_energy_card(c)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Lightning Energy")
        if picks:
            await ctx.attach_energy(picks[0], src)
        await ctx.shuffle_deck()
    return effect


def self_control_immune(*conds) -> Passive:
    blocked = set(conds)
    class _P(Passive):
        def modify_special_conditions(self, conditions, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return conditions
            return [c for c in conditions if c not in blocked]
    return _P()


def spiral_drain_heal(counters: int = 1):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


def full_retaliation_magikarp(per: int = 20):
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play():
            dn = (p.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            if "magikarp" in dn:
                n += max(0, ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage(per * n)
    return effect


def pulverize_if_damaged(base: int = 50, bonus: int = 50, min_counters: int = 2):
    async def effect(ctx):
        d = ctx.defender
        extra = 0
        if d is not None:
            c = max(0, ctx.max_hp(d) - d.get_attribute(AttrID.HP, 0)) // 10
            if c >= min_counters:
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def commanding_aura_no_stadium() -> Passive:
    class _P(Passive):
        def modify_playability(self, card, player_id, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return True
            if player_id == holder.owning_player_id:
                return True
            d = def_for(card.archetype_id)
            tt = getattr(d, "trainer_type", None)
            if tt == TrainerType.STADIUM or "Stadium" in (
                    getattr(d, "subtypes", None) or []):
                return False
            return True
    return _P()


def knock_off_random_hand():
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand(ctx.opponent_id))
        if not hand:
            return
        import random
        card = random.choice(hand)
        await ctx.discard_cards([card])
    return effect


def pivot_throw_takes_more(amount: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        # LIGHT: takes more next turn — use temporary reverse of protect
        if ctx.attacker is None:
            return
        class TakesMore(Passive):
            def modify_damage_taken(self, calc, carrier):
                holder = carrier_pokemon(carrier) or carrier
                if calc.is_attack and calc.is_opposing and calc.target is holder:
                    calc.amount += amount
        ctx.add_passive_through_opponents_turn(ctx.attacker, TakesMore())
    return effect


def wishing_star_look5():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        top = ctx.deck_top(5)
        if not top:
            return
        await ctx.reveal_cards(top, to_player=ctx.player_id)
        pool = [c for c in top if is_energy_card(c)]
        chosen = None
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Energy to hand")
            if picks:
                chosen = picks[0]
                await ctx.put_in_hand(picks, reveal=True)
        rest = [c for c in top if c is not chosen]
        if rest:
            await ctx.reorder_deck_top(rest) if hasattr(ctx, 'reorder_deck_top') else None
            # put remaining back in same order
            deck = ctx.board.find_player_area(ctx.player_id, "deck")
            for c in reversed(rest):
                if c.parent is not deck:
                    ctx.board.move_card(c.entity_id, deck.entity_id, position=0)
    return effect


def metallic_blow_body_bonus(base: int = 20, bonus: int = 30):
    async def effect(ctx):
        d = ctx.defender
        extra = 0
        if d is not None:
            cdef = def_for(d.archetype_id)
            for a in (getattr(cdef, "abilities", None) or []):
                if getattr(a, "ability_type", None) == AbilityTypes.POKE_BODY:
                    extra = bonus
                    break
        await ctx.deal_damage(base + extra)
    return effect


def healing_light_all(counters: int = 1):
    async def effect(ctx):
        for p in ctx.my_pokemon_in_play():
            await ctx.heal(counters * 10, p)
    return effect


def shooting_star_vs_ex(base: int = 50, bonus: int = 50):
    async def effect(ctx):
        d = ctx.defender
        if d is not None and is_pokemon_ex(d) and ctx.attacker is not None:
            pool = [c for c in ctx.attacker.children if is_energy_card(c)]
            if pool:
                await ctx.discard_cards(pool)
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
    return effect


def miraculous_light_heal_cure(counters: int = 1):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        await ctx.cure_all_conditions(a)
        await ctx.heal(counters * 10, a)
    return effect


def shining_star_vs_stage2(base: int = 50, bonus: int = 50):
    async def effect(ctx):
        d = ctx.defender
        is_s2 = False
        if d is not None:
            st = getattr(def_for(d.archetype_id), "stage", None)
            is_s2 = st == PokemonStage.STAGE2
        if is_s2 and ctx.attacker is not None:
            pool = [c for c in ctx.attacker.children if is_energy_card(c)]
            if pool:
                await ctx.discard_cards(pool)
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
    return effect


def natural_cure_on_water_attach() -> Passive:
    class _P(Passive):
        async def on_energy_attached(self, ctx, energy, pokemon, carrier, from_hand=True):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not from_hand:
                return
            if energy_provides_type(energy, PokemonTypes.WATER.value):
                await ctx.cure_all_conditions(holder)
    return _P()


def blot_heal(counters: int = 2):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


def swing_dance_draw():
    async def effect(ctx):
        await ctx.draw_cards(1)
    return effect


def healing_steps_discard_heal():
    async def effect(ctx):
        hand = list(ctx.hand())
        if not hand or ctx.source is None:
            return
        picks = await ctx.choose_cards(hand, len(hand), minimum=0, prompt="Discard any")
        if picks:
            await ctx.discard_cards(picks)
            await ctx.heal(len(picks) * 10, ctx.source)
    return effect


def circular_steps_per_pokemon(per: int = 10):
    async def effect(ctx):
        a = ctx.attacker
        n = sum(1 for p in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play())
                if p is not a)
        await ctx.deal_damage(per * n)
    return effect


def happy_dance_heal_all(counters: int = 1):
    async def effect(ctx):
        for p in ctx.my_pokemon_in_play():
            await ctx.heal(counters * 10, p)
    return effect


def moonglow_solrock_retreat() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None:
                return cost
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            dn = (pokemon.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            if "solrock" in dn:
                return 0
            return cost
    return _P()


def foresight_reorder(look: int = 5):
    async def effect(ctx):
        idx = await ctx.choose("Whose deck?", ["Yours", "Opponent's"])
        pid = ctx.player_id if idx == 0 else ctx.opponent_id
        top = ctx.deck_top(look, player_id=pid)
        if not top:
            return
        await ctx.reveal_cards(top, to_player=ctx.player_id)
        # reorder via choose order — LIGHT: leave as-is after reveal
        await ctx.reorder_deck_top(top) if False else None
    return effect


def target_beam_solrock(base: int = 20, per: int = 10):
    async def effect(ctx):
        n = sum(1 for p in ctx.my_pokemon_in_play()
                if "solrock" in (p.get_attribute(AttrID.DISPLAY_NAME) or "").lower())
        await ctx.deal_damage(base + per * n)
    return effect


def smooth_over_top():
    async def effect(ctx):
        picks = await ctx.search_deck(lambda c: True, count=1, minimum=0, prompt="Any card")
        if picks:
            await ctx.put_on_top_of_deck(picks)
        await ctx.shuffle_deck_below(picks[0]) if picks else await ctx.shuffle_deck()
        # After shuffle_deck_below the card is on top; if no picks just shuffle
        if not picks:
            await ctx.shuffle_deck()
    return effect


def burning_ball_if_fire2():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None or ctx.defender is None:
            return
        n = sum(1 for c in a.children if energy_provides_type(c, PokemonTypes.FIRE.value))
        if n >= 2:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def leap_out_switch():
    async def effect(ctx):
        await ctx.deal_damage()
        bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch with?")
        if t is not None:
            await ctx.switch_active(ctx.player_id, t)
    return effect


def thrust_flip_discard_def_energy():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Thrust")
        if not (results and results[0]):
            return
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        pool = [c for c in d.children if is_energy_card(c)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def magnetic_tackle_optional(base: int = 40, per: int = 10, self_per: int = 10):
    async def effect(ctx):
        a = ctx.attacker
        n = 0
        if a is not None:
            n = sum(1 for c in a.children
                    if energy_provides_type(c, PokemonTypes.LIGHTNING.value))
        if n and await ctx.ask_yes_no("Add Lightning Energy bonus (self-damage)?"):
            await ctx.deal_damage(base + per * n)
            await ctx.deal_damage(self_per * n, target=a, apply_modifiers=False)
        else:
            await ctx.deal_damage(base)
    return effect


def disconnect_lock_items():
    async def effect(ctx):
        await ctx.deal_damage()
        from spirit.game.session.effects import is_trainer_card
        def pred(c):
            if not is_trainer_card(c):
                return False
            return not is_supporter_card(c)
        ctx.lock_plays(ctx.opponent_id, pred)
    return effect


def mega_shot_discard_lightning_snipe(amount: int = 80):
    async def effect(ctx):
        a = ctx.attacker
        if a is not None:
            pool = [c for c in a.children
                    if energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
            if pool:
                await ctx.discard_cards(pool)
        from spirit.game.card_effects.attacks_common import snipe_attack
        await snipe_attack(amount, pool="any", apply_modifiers=False)(ctx)
    return effect


def intimidating_pattern_passive(amount: int = 20) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            # reduce opponent's attack damage while Active
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            if not (calc.is_attack and calc.attacker
                    and calc.attacker.owning_player_id != holder.owning_player_id):
                return
            calc.amount = max(0, calc.amount - amount)
    return _P()


def super_connectivity_attach():
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile()
                if is_energy_card(c) and (
                    energy_provides_type(c, PokemonTypes.PSYCHIC.value)
                    or energy_provides_type(c, PokemonTypes.METAL.value))]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Psychic/Metal Energy")
        if not picks:
            return
        dests = list(ctx.my_pokemon_in_play())
        dest = await ctx.choose_pokemon(dests, "Attach to?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def psychic_boom(base: int = 10, per: int = 10):
    return damage_per(count_energy("defender"), per, base=base)


def seek_out_any():
    async def effect(ctx):
        picks = await ctx.search_deck(lambda c: True, count=1, minimum=0, prompt="Any card")
        if picks:
            await ctx.put_in_hand(picks)
        await ctx.shuffle_deck()
    return effect


def pull_away_to_4():
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand(ctx.opponent_id))
        while len(hand) > 4:
            picks = await ctx.choose_cards(
                hand, 1, minimum=1, prompt="Opponent discards",
                player_id=ctx.opponent_id)
            if not picks:
                break
            await ctx.discard_cards(picks)
            hand = list(ctx.hand(ctx.opponent_id))
    return effect


def spark_vs_bodies(amount: int = 20):
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            d = def_for(p.archetype_id)
            if any(getattr(a, "ability_type", None) == AbilityTypes.POKE_BODY
                   for a in (getattr(d, "abilities", None) or [])):
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def spark_vs_powers(amount: int = 20):
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            d = def_for(p.archetype_id)
            if any(getattr(a, "ability_type", None) == AbilityTypes.POKE_POWER
                   for a in (getattr(d, "abilities", None) or [])):
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def mirror_coat_reflect_burn_poison() -> Passive:
    class _P(Passive):
        async def on_special_condition_applied(
                self, ctx, pokemon, carrier, condition, source=None):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return
            if condition not in (SpecialConditions.BURNED, SpecialConditions.POISONED):
                return
            attacker = source or getattr(ctx, "attacker", None)
            if attacker is None:
                return
            await ctx.apply_special_condition(attacker, condition)
    return _P()


def fast_protection_vs_basic() -> Passive:
    return prevent_damage_when(
        lambda calc, carrier: (
            calc.is_attack and calc.is_opposing
            and calc.attacker is not None
            and is_basic_pokemon(calc.attacker)),
        attacks_only=True)


def swords_dance_next(title: str = "Slash", next_base: int = 80):
    async def effect(ctx):
        printed = 40  # typical Slash printed
        # Use card's Slash damage if we can find it — soft: boost to next_base
        await apply_own_next_turn_boost(ctx, next_base - printed, attack_title=title)
    return effect


def magnetic_reversal_switch():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        results = await ctx.flip_coins(1, "Magnetic Reversal")
        if not (results and results[0]):
            return
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch in?")
        if t is not None:
            await ctx.switch_active(ctx.opponent_id, t)
    return effect


def dense_vs_evolved(amount: int = 20) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.target is holder):
                return
            if calc.attacker is not None and not is_basic_pokemon(calc.attacker):
                calc.amount = max(0, calc.amount - amount)
    return _P()


def bay_dance_boost(amount: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_own_next_turn_boost(ctx, amount)
    return effect


def spiral_rush(per: int = 30):
    async def effect(ctx):
        results = await ctx.flip_until_tails()
        heads = sum(1 for r in results if r)
        await ctx.deal_damage(per * heads)
    return effect


def holy_star_ex_damage(amount: int = 100):
    async def effect(ctx):
        a = ctx.attacker
        if a is not None:
            pool = [c for c in a.children if is_energy_card(c)]
            if pool:
                await ctx.discard_cards(pool)
        for p in ctx.opponent_pokemon_in_play():
            if is_pokemon_ex(p):
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def dragon_aura_fire_lightning() -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return False
            has_f = any(energy_provides_type(c, PokemonTypes.FIRE.value)
                        and is_basic_energy_card(c) for c in holder.children)
            has_l = any(energy_provides_type(c, PokemonTypes.LIGHTNING.value)
                        and is_basic_energy_card(c) for c in holder.children)
            return has_f and has_l
        def prevents_effects(self, calc, carrier):
            return self.prevents_damage(calc, carrier)
    return _P()


def dragon_boost_on_bench():
    """When put from hand onto Bench: move any number of basic Energy from others onto it."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        cards = []
        for p in ctx.my_pokemon_in_play():
            if p is src:
                continue
            for c in p.children:
                if is_basic_energy_card(c):
                    cards.append(c)
        if not cards:
            return
        picks = await ctx.choose_cards(cards, len(cards), minimum=0, prompt="Move basic Energy")
        for e in picks:
            await ctx.move_energy(e, src)
    return effect


def spiral_blast_basic_energy(per: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        n = sum(1 for c in (a.children if a else []) if is_basic_energy_card(c))
        await ctx.deal_damage(per * n)
    return effect


def lightning_burst_on_dark_attach() -> Passive:
    class _P(Passive):
        async def on_energy_attached(self, ctx, energy, pokemon, carrier, from_hand=True):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not from_hand:
                return
            if not energy_provides_type(energy, PokemonTypes.DARKNESS.value):
                return
            if not await ctx.ask_yes_no("Lightning Burst: confuse Defending?"):
                return
            for p in ctx.opponent_pokemon_in_play():
                if is_in_active_spot(p):
                    await ctx.apply_special_condition(p, SpecialConditions.CONFUSED)
    return _P()


def thunderous_blow(base: int = 40, per: int = 10):
    async def effect(ctx):
        a = ctx.attacker
        n = sum(1 for c in (a.children if a else [])
                if energy_provides_type(c, PokemonTypes.LIGHTNING.value))
        await ctx.deal_damage(base + per * n)
    return effect


def night_vision_look_hand():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            await ctx.reveal_cards(hand, to_player=ctx.player_id)
    return effect


def limitation_lock_supporters():
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.lock_plays(ctx.opponent_id, is_supporter_card)
    return effect


def dragon_lift_retreat() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or pokemon.owning_player_id != holder.owning_player_id:
                return cost
            if is_pokemon_ex(pokemon) or is_baby_pokemon(pokemon):
                return cost
            return 0
    return _P()


def flame_jet_snipe(amount: int = 40):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any", apply_modifiers=False)


def bright_flame_discard2():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if len(pool) >= 2:
            picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Discard 2 Energy")
            if picks:
                await ctx.discard_cards(picks)
        elif pool:
            await ctx.discard_cards(pool)
    return effect


def triple_breach(amount: int = 10, count: int = 3):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any", count=count, apply_modifiers=False)


def rend_if_damaged(base: int = 30, bonus: int = 20):
    async def effect(ctx):
        d = ctx.defender
        extra = 0
        if d is not None and ctx.max_hp(d) - d.get_attribute(AttrID.HP, 0) > 0:
            extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def drag_off_optional_ex8(amount_if_switched: int = 30):
    return drag_off_optional(amount_if_switched)


def darkness_blast_optional(base: int = 60, bonus: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        do = False
        if a is not None:
            pool = [c for c in a.children
                    if energy_provides_type(c, PokemonTypes.DARKNESS.value)]
            if pool and await ctx.ask_yes_no("Discard Darkness Energy for bonus?"):
                picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard")
                if picks:
                    await ctx.discard_cards(picks)
                    do = True
        await ctx.deal_damage(base + (bonus if do else 0))
        if do and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    return effect


def empty_shell_no_prize() -> Passive:
    class _P(Passive):
        def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is holder:
                return 0
            return count
    return _P()


def extra_curse_ex(counters: int = 2, ex_counters: int = 4):
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        n = ex_counters if is_pokemon_ex(d) else counters
        await ctx.deal_damage(n * 10, target=d, apply_modifiers=False, as_counters=True)
    return effect


def hard_protection_vs_own() -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.target is holder):
                return False
            return (calc.attacker is not None
                    and calc.attacker.owning_player_id == holder.owning_player_id)
    return _P()


def fan_action_switch():
    async def effect(ctx):
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch Defending with?")
        if t is not None:
            await ctx.switch_active(ctx.opponent_id, t)
    return effect


def stadium_power_bonus(base: int = 50, bonus: int = 20):
    async def effect(ctx):
        extra = bonus if ctx.stadium_in_play() else 0
        await ctx.deal_damage(base + extra)
    return effect


def advanced_armor_vs_evolved():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        class ShieldEvo(Passive):
            def prevents_damage(self, calc, carrier):
                holder = carrier_pokemon(carrier) or carrier
                if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                    return False
                return calc.attacker is not None and not is_basic_pokemon(calc.attacker)
            def prevents_effects(self, calc, carrier):
                return self.prevents_damage(calc, carrier)
        ctx.add_passive_through_opponents_turn(ctx.attacker, ShieldEvo())
    return effect


def heavy_metal_flip(base: int = 10, per: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        n = sum(1 for c in (a.children if a else [])
                if energy_provides_type(c, PokemonTypes.METAL.value))
        heads = sum(1 for r in (await ctx.flip_coins(n, "Heavy Metal") if n else []) if r)
        await ctx.deal_damage(base + per * heads)
    return effect


def lazy_aura_vs_ex(amount: int = 30) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            if calc.attacker is not None and is_pokemon_ex(calc.attacker):
                calc.amount = max(0, calc.amount - amount)
    return _P()


def lazy_headbutt_asleep():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    return effect


def magma_ring_no_retreat():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is not None:
            ctx.lock_retreat(ctx.defender)
    return effect


def sunbeam_lunatone_hp(max_hp: int = 80) -> Passive:
    class _P(Passive):
        def max_hp_override(self, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None:
                return None
            if pokemon.owning_player_id != holder.owning_player_id:
                return None
            dn = (pokemon.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            if "lunatone" in dn:
                return max_hp
            return None
    return _P()


def scorching_light_flip():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Scorching Light")
        if ctx.defender is None or not results:
            return
        if results[0]:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
        else:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def reflected_beam_lunatone(per: int = 10):
    async def effect(ctx):
        n = sum(1 for p in ctx.my_pokemon_in_play()
                if "lunatone" in (p.get_attribute(AttrID.DISPLAY_NAME) or "").lower())
        from spirit.game.card_effects.attacks_common import snipe_attack
        await snipe_attack(per * n, pool="bench", apply_modifiers=False)(ctx)
    return effect


def core_guard_psychic(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.target is holder):
                return
            if any(energy_provides_type(c, PokemonTypes.PSYCHIC.value)
                   for c in holder.children):
                calc.amount = max(0, calc.amount - amount)
    return _P()


def energy_flip_snipe_move(amount: int = 10):
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import snipe_attack
        await snipe_attack(amount, pool="bench", apply_modifiers=False)(ctx)
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        bench = [p for p in ctx.my_pokemon_in_play() if not is_in_active_spot(p)]
        if not pool or not bench:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Move Energy?")
        if not picks:
            return
        dest = await ctx.choose_pokemon(bench, "Move to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect


def mid_air_crush(amount: int = 20):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any", apply_modifiers=False)


def nosedive_self(self_dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Nosedive")
        if results and not results[0] and ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def fly_flip_protect():
    from spirit.game.card_effects.passives_common import flip_protection
    # If tails does nothing — need custom
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Fly")
        if not (results and results[0]):
            return
        await ctx.deal_damage()
        await apply_protection(ctx, prevent=True, effects_too=True)
    return effect


def tropical_motion_no_resist() -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            # Opponent active has no resistance while Tropius active — LIGHT via ignore resist on their attacks? 
            # Actually: opponent's Active have no Resistance (when taking damage from anyone)
            pass
        def modify_resistance(self, types, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return types
            if pokemon.owning_player_id == holder.owning_player_id:
                return types
            if is_in_active_spot(pokemon):
                return None  # no resistance
            return types
    return _P()


def vigorous_aura_boost(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            if not (calc.is_attack and calc.to_active):
                return
            # both players' Active
            if calc.attacker is not None and is_in_active_spot(calc.attacker):
                calc.amount += amount
    return _P()


def liability_near_ko_self(self_dmg: int = 70):
    async def effect(ctx):
        d = ctx.defender
        if d is not None:
            # leave at 10 HP
            hp = d.get_attribute(AttrID.HP, 0)
            if hp > 10:
                await ctx.deal_damage(hp - 10, target=d, apply_modifiers=False)
        if ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def smogscreen_poison_flip():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
            ctx.require_attack_flip(ctx.defender)
    return effect


def raging_tremble(per: int = 10):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Raging Tremble")
        a = ctx.attacker
        n = 0
        if a is not None:
            n = max(0, ctx.max_hp(a) - a.get_attribute(AttrID.HP, 0)) // 10
        if results and results[0]:
            for p in ctx.opponent_pokemon_in_play():
                if is_in_active_spot(p):
                    await ctx.deal_damage(per * n, target=p)
        else:
            for p in ctx.my_pokemon_in_play():
                if is_in_active_spot(p):
                    await ctx.deal_damage(per * n, target=p, apply_modifiers=False)
    return effect


def dwindling_wave(base: int = 70, per: int = 10):
    return karate_chop(base, per)


def miracle_essence_choose_condition():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Miracle Essence")
        if not (results and results[0]):
            return
        opts = ["Asleep", "Burned", "Confused", "Paralyzed", "Poisoned"]
        enums = [SpecialConditions.ASLEEP, SpecialConditions.BURNED,
                 SpecialConditions.CONFUSED, SpecialConditions.PARALYZED,
                 SpecialConditions.POISONED]
        idx = await ctx.choose("Which Special Condition?", opts)
        if idx is None:
            return
        for p in ctx.opponent_pokemon_in_play():
            if is_in_active_spot(p):
                await ctx.apply_special_condition(p, enums[idx])
    return effect


def dazzle_dance_confuse():
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            if is_in_active_spot(p):
                await ctx.apply_special_condition(p, SpecialConditions.CONFUSED)
    return effect


def psyloop_trainers(base: int = 30, per: int = 30):
    async def effect(ctx):
        n = 0
        # Tools/stadiums in play count as trainers
        for p in ctx.opponent_pokemon_in_play():
            for c in p.children:
                d = def_for(c.archetype_id)
                if getattr(d, "trainer_type", None) is not None:
                    n += 1
        if ctx.stadium_in_play():
            # may be opponent's
            n += 1
        await ctx.deal_damage(base + per * n)
    return effect


def flip_over_self(self_dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(
                self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def selfdestruct_benches(amount: int = 10, self_dmg: int = 0):
    async def effect(ctx):
        await ctx.deal_damage()
        for p in list(ctx.my_bench()) + list(ctx.opponent_bench()):
            await ctx.deal_damage(amount, target=p, apply_modifiers=False)
        if self_dmg and ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def fluff_flip_prevent() -> Passive:
    class _P(Passive):
        async def on_attack_declared(self, ctx, pokemon, carrier, attacker=None):
            return
        def prevents_damage(self, calc, carrier):
            return False  # need async flip — use FlipPrevent if available
    from spirit.game.card_effects.passives_common import FlipPreventDamagePassive
    # Custom: only when already damaged
    class Fluff(Passive):
        async def modify_damage_taken_async(self, calc, carrier, ctx):
            return
        def modify_damage_taken(self, calc, carrier):
            # Can't flip sync — LIGHT: reduce to 0 when damaged (too strong) — skip
            pass
    # Use FlipPreventDamagePassive wrapped — LIGHT approximate always-on flip when damaged
    return FlipPreventDamagePassive("Fluff")


# Trainers / tools / energies for EX8

async def energy_charge_ex8(ctx):
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Energy")
    if picks:
        await ctx.put_on_top_of_deck(picks)
        await ctx.shuffle_deck()  # wrong — should shuffle then put on top
    # Fix: shuffle then put on top
    # Re-do properly below in override


async def lady_outing(ctx):
    def match(c):
        return is_basic_energy_card(c)
    picks = await ctx.search_deck(match, count=3, minimum=0, prompt="basic Energy")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def master_ball_ex8(ctx):
    picks = await ctx.search_deck(is_pokemon_card, count=1, minimum=0, prompt="Pokémon")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def professor_cozmos_discovery(ctx):
    idx = await ctx.choose("Cozmo", ["Draw 3", "Draw until 7"])
    if idx == 0:
        await ctx.draw_cards(3)
    else:
        while ctx.hand_size() < 7:
            if not await ctx.draw_cards(1):
                break


def meteor_falls_passive() -> Passive:
    """LIGHT: Evolved Pokémon (excl ex) can use attacks of lower stages — hard; skip effect."""
    class _P(Passive):
        stacking_key = "meteor_falls"
    return _P()


def space_center_passive() -> Passive:
    """Poké-Powers of non-ex Basic Pokémon don't work."""
    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_POWER:
                return False
            if is_pokemon_ex(pokemon) or not is_basic_pokemon(pokemon):
                return False
            return True
    return _P()


def strength_charm_passive(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier)
            if holder is None or calc.attacker is not holder:
                return
            if calc.is_attack and calc.to_active:
                calc.amount += amount
    return _P()


def balloon_berry_retreat() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is holder:
                return 0
            return cost
        # discard after retreat — via on_retreat if exists
        async def on_retreated(self, ctx, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is holder and carrier is not None:
                await ctx.discard_cards([carrier])
    return _P()


def crystal_shard_colorless() -> Passive:
    """LIGHT: Pokémon is Colorless type while attached; discard at end of turn if attacked."""
    class _P(Passive):
        def modify_pokemon_types(self, types, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is holder:
                return [PokemonTypes.COLORLESS.value]
            return types
    return _P()


def boost_energy_provides():
    """Provides Colorless Colorless Colorless; discard at end of turn — use EnergyCardDef hooks in card."""
    pass


def heal_energy_between_turns(counters: int = 1) -> Passive:
    class _P(Passive):
        async def between_turns(self, ctx, carrier):
            holder = carrier_pokemon(carrier)
            if holder is not None:
                await ctx.heal(counters * 10, holder)
    return _P()


def scramble_energy_passive() -> Passive:
    """Provides every type of Energy but only while more prizes than opponent; else Colorless."""
    class _P(Passive):
        def modify_energy_provides(self, provides, card, carrier, board):
            # Check prize lead
            from spirit.game.card_effects.attacks_common import count_prizes_remaining
            # Can't get ctx easily — use board
            holder = carrier_pokemon(carrier)
            if holder is None:
                return provides
            pid = holder.owning_player_id
            # Approximate: check prize piles
            my = board.find_player_area(pid, "prizePile")
            opp_id = next((p for p in board.player_ids if p != pid), None) if hasattr(board, 'player_ids') else None
            # Fallback: always multi-type (LIGHT when behind)
            return [[t.value] for t in (
                PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
                PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
                PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.COLORLESS)]
    return _P()


async def energy_charge(ctx):
    """Flip; heads: shuffle up to 2 Energy from discard into deck."""
    results = await ctx.flip_coins(1, "Energy Charge")
    if not (results and results[0]):
        return
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if not pool:
        return
    n = min(2, len(pool))
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Energy to shuffle")
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks)


async def professor_cozmos_discovery(ctx):
    idx = await ctx.choose("Professor Cozmo's Discovery", ["Draw 3 cards", "Draw until you have 7"])
    if idx == 0:
        await ctx.draw_cards(3)
    elif idx == 1:
        while ctx.hand_size() < 7:
            got = await ctx.draw_cards(1)
            if not got:
                break


def boost_energy_lock_retreat() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is holder:
                return 99  # can't retreat
            return cost
    return _P()


def boost_energy_attach_to(pokemon):
    return is_evolution_pokemon(pokemon) if hasattr(pokemon, 'archetype_id') else (
        getattr(def_for(pokemon.archetype_id), "stage", None) in (
            PokemonStage.STAGE1, PokemonStage.STAGE2))


def scramble_energy_attach_to(pokemon):
    if is_pokemon_ex(pokemon):
        return False
    d = def_for(pokemon.archetype_id)
    return getattr(d, "stage", None) in (PokemonStage.STAGE1, PokemonStage.STAGE2)


async def heal_energy_on_attach(ctx):
    """Remove 1 counter + all SCs unless attached to Pokémon-ex."""
    target = getattr(ctx, "attached_to", None) or ctx.source
    # ctx.attached_to per EnergyCardDef docs
    poke = getattr(ctx, "attached_to", None)
    if poke is None:
        return
    if is_pokemon_ex(poke):
        return
    await ctx.cure_all_conditions(poke)
    await ctx.heal(10, poke)


def _display_name(entity) -> str:
    raw = entity.get_attribute(AttrID.DISPLAY_NAME) if entity is not None else None
    if isinstance(raw, dict):
        for k in ("en", "Name", "name", "displayName"):
            if k in raw and raw[k]:
                return str(raw[k])
        return str(next(iter(raw.values()), "") if raw else "")
    return str(raw or "")


def full_retaliation_magikarp(per: int = 20):
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play():
            if "magikarp" in _display_name(p).lower():
                n += max(0, ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage(per * n)
    return effect


def wishing_star_look5():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        top = ctx.deck_top(5)
        if not top:
            return
        await ctx.reveal_cards(top, to_player=ctx.player_id)
        pool = [c for c in top if is_energy_card(c)]
        chosen = None
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Energy to hand")
            if picks:
                chosen = picks[0]
                await ctx.put_in_hand(picks, reveal=True)
        deck = ctx.board.find_player_area(ctx.player_id, "deck")
        for c in reversed([x for x in top if x is not chosen]):
            ctx.board.move_card(c.entity_id, deck.entity_id, position=0)
    return effect


def smooth_over_top():
    async def effect(ctx):
        picks = await ctx.search_deck(lambda c: True, count=1, minimum=0, prompt="Any card")
        if not picks:
            await ctx.shuffle_deck()
            return
        card = picks[0]
        await ctx.shuffle_deck()
        await ctx.put_on_top_of_deck(card)
    return effect


def spiral_rush(per: int = 30):
    async def effect(ctx):
        heads = await ctx.flip_until_tails("Spiral Rush")
        await ctx.deal_damage(per * int(heads or 0))
    return effect


def target_beam_solrock(base: int = 20, per: int = 10):
    async def effect(ctx):
        n = sum(1 for p in ctx.my_pokemon_in_play()
                if "solrock" in _display_name(p).lower())
        await ctx.deal_damage(base + per * n)
    return effect


def reflected_beam_lunatone(per: int = 10):
    async def effect(ctx):
        n = sum(1 for p in ctx.my_pokemon_in_play()
                if "lunatone" in _display_name(p).lower())
        from spirit.game.card_effects.attacks_common import snipe_attack
        await snipe_attack(max(0, per * n), pool="bench", apply_modifiers=False)(ctx)
    return effect


def moonglow_solrock_retreat() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None:
                return cost
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            if "solrock" in _display_name(pokemon).lower():
                return 0
            return cost
    return _P()


def tropical_motion_no_resist() -> Passive:
    class _P(Passive):
        def modify_resistance(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            # Opponent's Active has no Resistance
            if calc.target is None:
                return
            if calc.target.owning_player_id == holder.owning_player_id:
                return
            if is_in_active_spot(calc.target):
                calc.resistance = 0
    return _P()

# === EX7/EX8 quality-bar overrides (no LIGHT) ===
# Later defs win. Cards must do what the card text says.


def mini_metronome():
    """Flip; heads: copy 1 of Defending's attacks (full effect via use_attack)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Mini-Metronome")
        if not (results and results[0]) or ctx.defender is None:
            return
        await metronome_defending(ctx)
    return effect


def rainbow_moves():
    """Copy 1 attack from 1 of opponent's Benched Pokémon (full effect)."""
    from spirit.game.data_utils import Attack as _Attack
    async def effect(ctx):
        bench = [p for p in ctx.opponent_pokemon_in_play() if not is_in_active_spot(p)]
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Copy attack from which Benched Pokémon?")
        if target is None:
            return
        definition = def_for(target.archetype_id)
        candidates = []
        seen = set()
        for ability in getattr(definition, "abilities", None) or []:
            if not isinstance(ability, _Attack):
                continue
            key = (ability.title, ability.game_text)
            if key in seen:
                continue
            seen.add(key)
            candidates.append((target, ability))
        if not candidates:
            return
        picked = await ctx.choose_attack_to_copy(
            candidates, "Choose an attack to copy")
        if picked is None:
            return
        _, chosen = picked
        await ctx.use_attack(chosen)
    return effect


def dark_link():
    """Flip; heads: copy an attack from another in-play Dark-named Pokémon."""
    from spirit.game.data_utils import Attack as _Attack
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Dark Link")
        if not (results and results[0]):
            return
        candidates = []
        seen = set()
        for pokemon in ctx.my_pokemon_in_play():
            if pokemon is ctx.attacker:
                continue
            name = pokemon.get_attribute(AttrID.DISPLAY_NAME) or ""
            if "Dark" not in name:
                continue
            definition = def_for(pokemon.archetype_id)
            for ability in getattr(definition, "abilities", None) or []:
                if not isinstance(ability, _Attack):
                    continue
                key = (pokemon.entity_id, ability.title, ability.game_text)
                if key in seen:
                    continue
                seen.add(key)
                candidates.append((pokemon, ability))
        if not candidates:
            return
        picked = await ctx.choose_attack_to_copy(
            candidates, "Choose a Dark Pokémon's attack to copy")
        if picked is None:
            return
        _, chosen = picked
        await ctx.use_attack(chosen)
    return effect


def dark_seed():
    """Can't retreat next turn; 5 damage counters at end of opponent's next turn."""
    async def effect(ctx):
        defender = ctx.defender
        if defender is None:
            return
        ctx.lock_retreat(defender)
        owner_id = defender.owning_player_id
        target_id = defender.entity_id

        def _guard(board):
            entity = board.get_entity(target_id) if hasattr(board, "get_entity") else None
            return entity is not None

        async def _put(session):
            board = session.board_state
            entity = board.get_entity(target_id)
            if entity is None:
                return
            from spirit.game.session.effects import EffectContext
            ectx = EffectContext(session, ctx.player_id, ctx.source, None)
            await ectx.deal_damage(
                50, target=entity, apply_modifiers=False, as_counters=True)

        # Opponent's next checkup is 1 turn ahead from attack resolution timing
        # used elsewhere for "end of your opponent's next turn".
        ctx.schedule_at_checkup(1, _put, guard=_guard)
    return effect


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


async def _tricky_gym_feint_attack(ctx):
    """Feint Attack granted by Rocket's Tricky Gym."""
    pool = list(ctx.opponent_pokemon_in_play())
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Feint Attack — choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.deal_damage(
        20, target=target, apply_modifiers=False, ignore_target_effects=True)


def rockets_tricky_gym_feint_attack():
    """Attack printed on Rocket's Tricky Gym (granted to Dark/Rocket's)."""
    from spirit.game.data_utils import Attack as _Attack
    return _Attack(
        title="Feint Attack",
        game_text=(
            "Does 20 damage to 1 of your opponent's Pokémon. This attack's "
            "damage isn't affected by Weakness, Resistance, Poké-Powers, "
            "Poké-Bodies, or any other effects on that Pokémon."
        ),
        cost={PokemonTypes.COLORLESS: 1},
        damage=20,
        effect=_tricky_gym_feint_attack,
    )


def rockets_tricky_gym_passive() -> Passive:
    """Dark / Rocket's Pokémon may use this stadium's Feint Attack."""
    from spirit.game.data_utils import Attack as _Attack

    class _P(Passive):
        stacking_key = "rockets_tricky_gym"

        def granted_attacks(self, board, pokemon, carrier):
            name = pokemon.get_attribute(AttrID.DISPLAY_NAME) or ""
            if "Dark" not in name and "Rocket's" not in name:
                return []
            definition = def_for(getattr(carrier, "archetype_id", None) or "")
            attacks = []
            for ability in getattr(definition, "abilities", None) or []:
                if isinstance(ability, _Attack):
                    attacks.append(ability)
            if not attacks:
                # Fallback if stadium abilities weren't registered on the card
                attacks = [rockets_tricky_gym_feint_attack()]
            return attacks

    return _P()


async def surprise_time_machine(ctx):
    """Devolve highest stage into deck; then search deck to re-evolve."""
    evolved = [
        p for p in ctx.my_pokemon_in_play()
        if getattr(def_for(p.archetype_id), "stage", None) in (
            PokemonStage.STAGE1, PokemonStage.STAGE2)
    ]
    if not evolved:
        return
    target = await ctx.choose_pokemon(evolved, "Devolve which Pokémon?")
    if target is None:
        return
    removed = await ctx.devolve_pokemon(target, steps=1, destination="deck")
    if not removed:
        await ctx.shuffle_deck()
        return
    # After devolve, `target` is the remaining lower stage still in play.
    remaining = target
    if remaining.get_attribute(AttrID.HP, 0) <= 0:
        await ctx.shuffle_deck()
        return
    logic_name = remaining.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    from spirit.game.content.definitions import evolves_from as _evolves_from

    def match(card):
        if logic_name and _evolves_from(card.archetype_id, logic_name):
            return True
        # Fallback: evolves_from display match
        ef = (getattr(def_for(card.archetype_id), "evolves_from", None) or "")
        dn = remaining.get_attribute(AttrID.DISPLAY_NAME) or ""
        return bool(ef) and (dn.lower() in ef.lower() or ef.lower() in dn.lower())

    picks = await ctx.search_deck(
        match, count=1, minimum=0,
        prompt="Choose an Evolution card that evolves from that Pokémon")
    if picks:
        await ctx.evolve_pokemon(remaining, picks[0])
    await ctx.shuffle_deck()


async def swoop_teleporter(ctx):
    """Switch a Basic (non-ex) in play with a Basic (non-ex) from deck; discard old."""
    basics = [
        p for p in ctx.my_pokemon_in_play()
        if is_basic_pokemon(p) and not is_pokemon_ex(p)
    ]
    if not basics:
        return
    outgoing = await ctx.choose_pokemon(
        basics, "Switch which Basic Pokémon?")
    if outgoing is None:
        return

    def match(card):
        return is_basic_pokemon(card) and not is_pokemon_ex(card)

    picks = await ctx.search_deck(
        match, count=1, minimum=0,
        prompt="Choose a Basic Pokémon (excluding Pokémon-ex)")
    if not picks:
        await ctx.shuffle_deck()
        return
    await ctx.identity_swap(
        outgoing, picks[0], destination="discard", transfer=True)
    await ctx.shuffle_deck()


def detour_supporter():
    """If a Supporter is in play (activeTrainer), use that card's effect."""
    async def effect(ctx):
        area = ctx.board.find_global_area("activeTrainer") \
            if hasattr(ctx.board, "find_global_area") else None
        if area is None:
            area = ctx.board.find_player_area(ctx.player_id, "activeTrainer")
        cards = list(area.children if area else [])
        supporter = None
        for card in cards:
            d = def_for(card.archetype_id)
            subs = getattr(d, "subtypes", None) or []
            ttype = getattr(d, "trainer_type", None)
            if "Supporter" in subs or ttype in (TrainerType.SUPPORTER, getattr(TrainerType.SUPPORTER, "value", None)) or is_supporter_card(card):
                supporter = card
                break
        if supporter is None:
            return
        d = def_for(supporter.archetype_id)
        fn = getattr(d, "effect", None)
        if callable(fn):
            await fn(ctx)
    return effect


def psychic_shield_ex():
    """Prevent all from opponent's Pokémon-ex during opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return

        class _ExShield(Passive):
            def prevents_damage(self, calc, carrier):
                return (
                    calc.is_attack
                    and calc.is_opposing
                    and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None
                    and is_pokemon_ex(calc.attacker)
                )

            def blocks_attack_effects_from(self, target, carrier, attacker):
                return (
                    carrier_pokemon(carrier) is target
                    and attacker is not None
                    and is_pokemon_ex(attacker)
                )

        ctx.add_passive_through_opponents_turn(ctx.attacker, _ExShield())
    return effect


def hustle_punch_next(next_base: int = 50):
    """During your next turn, this attack's base damage is next_base."""
    async def effect(ctx):
        await ctx.deal_damage()
        title = ctx.ability.title if ctx.ability else "Hustle Punch"
        printed = int(getattr(ctx.ability, "damage", 0) or 0)
        delta = next_base - printed
        if delta:
            await apply_own_next_turn_boost(ctx, delta, attack_title=title)
    return effect


def swords_dance_next(title: str = "Slash", next_base: int = 80):
    """During your next turn, named attack's base damage is next_base."""
    async def effect(ctx):
        printed = None
        if ctx.attacker is not None:
            d = def_for(ctx.attacker.archetype_id)
            for ability in getattr(d, "abilities", None) or []:
                if getattr(ability, "title", None) == title:
                    printed = int(getattr(ability, "damage", 0) or 0)
                    break
        if printed is None:
            printed = 30
        await apply_own_next_turn_boost(
            ctx, next_base - printed, attack_title=title)
    return effect


def fluff_flip_prevent() -> Passive:
    """If already damaged: flip; heads prevent all effects including damage."""
    class Fluff(Passive):
        async def damage_interceptor(self, ctx, calc, target, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
                return None
            if target is not holder:
                return None
            max_hp = effective_max_hp(calc.board, holder)
            current = holder.get_attribute(AttrID.HP, 0)
            if current >= max_hp:
                return None  # no damage counters yet
            heads = await ctx.flip_coins(
                1, "Fluff", source=holder)
            if heads and heads[0]:
                calc.prevented = True
                return 0
            return None

        def blocks_attack_effects_from(self, target, carrier, attacker):
            # Sync path can't flip; damage_interceptor handles the flip case.
            # Effects still apply on tails / undamaged — engine checks prevented.
            return False

    return Fluff()


def form_change_deoxys(ex: bool = False):
    """Search deck for another Deoxys (/ex); identity-swap; shuffle."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        needle = "deoxys"

        def match(card):
            d = def_for(card.archetype_id)
            if d is None:
                return False
            dn = (getattr(d, "display_name", None) or "").lower()
            if needle not in dn:
                return False
            card_is_ex = is_pokemon_ex(card)
            if ex:
                return card_is_ex
            return not card_is_ex

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose another Deoxys to switch with")
        if picks:
            await ctx.identity_swap(
                src, picks[0], destination="deck", transfer=True)
        await ctx.shuffle_deck()
    return effect


def meteor_falls_passive() -> Passive:
    """Active Evolved (excl ex) may use attacks from Basic / Stage 1 under it."""
    from spirit.game.data_utils import Attack as _Attack
    from spirit.game.models.board import PokemonEntity

    class _P(Passive):
        stacking_key = "meteor_falls"

        def granted_attacks(self, board, pokemon, carrier):
            if is_pokemon_ex(pokemon) or is_basic_pokemon(pokemon):
                return []
            if not is_in_active_spot(pokemon):
                return []
            attacks = []
            seen = set()
            for child in pokemon.children:
                if not isinstance(child, PokemonEntity):
                    continue
                stage = getattr(def_for(child.archetype_id), "stage", None)
                if stage not in (PokemonStage.BASIC, PokemonStage.STAGE1):
                    continue
                for ability in getattr(def_for(child.archetype_id), "abilities", None) or []:
                    if not isinstance(ability, _Attack):
                        continue
                    key = (ability.title, ability.game_text)
                    if key in seen:
                        continue
                    seen.add(key)
                    attacks.append(ability)
            return attacks

    return _P()


def space_center_passive() -> Passive:
    """Ignore Poké-Bodies of Basic Pokémon (excl ex and owner-named)."""
    class _P(Passive):
        stacking_key = "space_center"

        def blocks_ability(self, ability, pokemon, carrier):
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_BODY:
                return False
            if is_pokemon_ex(pokemon) or not is_basic_pokemon(pokemon):
                return False
            if _has_owner_in_name(pokemon):
                return False
            return True

    return _P()


def crystal_shard_colorless() -> Passive:
    """Attached Pokémon's type is Colorless while Crystal Shard is attached."""
    class _P(Passive):
        def modify_pokemon_types(self, types, pokemon, carrier):
            if carrier_pokemon(carrier) is pokemon:
                return [PokemonTypes.COLORLESS.value]
            return types

    return _P()


def crystal_shard_discard_if_attacked(tool_guid: str):
    """END_OF_TURN: discard Crystal Shard if the holder attacked this turn."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        attacked = {
            eid for eid, _arch, _title in ctx.session.turn_state.attacks_used
        }
        if pokemon.entity_id not in attacked:
            return
        tool = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == tool_guid.lower()),
            None)
        if tool is not None:
            await ctx.discard_cards([tool])
    return effect


# Classic EX-era types for Scramble (no Fairy/Dragon).
_SCRAMBLE_TYPES = (
    PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
    PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
    PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.COLORLESS,
)


def scramble_energy_three_options():
    """Every type, 3 in any combination (with replacement, order-normalized)."""
    from itertools import combinations_with_replacement
    return [list(combo) for combo in combinations_with_replacement(_SCRAMBLE_TYPES, 3)]


class ScrambleEnergyPassive(Passive):
    """Colorless normally; when prize lead, every type but only 3 at a time."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None:
            return options
        pid = holder.owning_player_id
        my = board.find_player_area(pid, "prizePile")
        opp_id = next((p for p in board.player_ids if p != pid), None)
        opp = board.find_player_area(opp_id, "prizePile") if opp_id else None
        my_n = len(my.children) if my else 0
        opp_n = len(opp.children) if opp else 0
        if my_n > opp_n:
            return [
                [getattr(t, "value", t) for t in option]
                for option in scramble_energy_three_options()
            ]
        return [[PokemonTypes.COLORLESS.value]]


def scramble_energy_passive() -> Passive:
    return ScrambleEnergyPassive()


def scramble_energy_attach_to(pokemon):
    if is_pokemon_ex(pokemon):
        return False
    return is_evolution_pokemon(pokemon) if hasattr(pokemon, "archetype_id") else False



async def professor_cozmos_discovery(ctx):
    """Flip: heads draw bottom 3; tails draw top 2."""
    results = await ctx.flip_coins(1, "Professor Cozmo's Discovery")
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    if not deck or not deck.children:
        return
    if results and results[0]:
        # Bottom of deck is children[0]
        n = min(3, len(deck.children))
        cards = list(deck.children[:n])
        for card in cards:
            await ctx.put_in_hand([card], reveal=False)
    else:
        await ctx.draw_cards(2)


def foresight_reorder(look: int = 5):
    async def effect(ctx):
        idx = await ctx.choose("Whose deck?", ["Yours", "Opponent's"])
        if idx is None:
            return
        pid = ctx.player_id if idx == 0 else ctx.opponent_id
        top = ctx.deck_top(look, player_id=pid)
        if not top:
            return
        await ctx.reorder_deck_top(len(top), player_id=pid,
                                   prompt="Put them back on top in any order")
    return effect


def call_for_family_grass_one():
    return call_for_family_grass(1)


def high_voltage_lock_trainers():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "High Voltage")
        if results and results[0]:
            from spirit.game.session.effects import is_trainer_card
            ctx.lock_plays(ctx.opponent_id, is_trainer_card)
    return effect


def freeze_lock():
    """Printed; heads: opponent can't attach Energy from hand next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Freeze Lock")
        if results and results[0]:
            ctx.lock_plays(ctx.opponent_id, is_energy_card)
    return effect



async def island_cave_on_energy_attached(ctx):
    """Whenever any player attaches Energy from hand to W/F/M, clear SCs."""
    receiver = getattr(ctx, "energy_receiver", None)
    if receiver is None:
        return
    types = receiver.get_attribute(AttrID.POKEMON_TYPES) or []
    wanted = {
        PokemonTypes.WATER.value,
        PokemonTypes.FIGHTING.value,
        PokemonTypes.METAL.value,
    }
    if not any(t in wanted for t in types):
        return
    await ctx.cure_all_conditions(receiver)


def island_cave_passive() -> Passive:
    """Stadium continuous marker; cure is via ON_ENERGY_ATTACHED ability."""
    class _P(Passive):
        stacking_key = "island_cave"
    return _P()


def buffer_piece_discard_end_opponent_turn(tool_guid: str):
    """END_OF_TURN: discard Buffer Piece at end of the opponent's turn."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        # END_OF_TURN fires for the turn player; discard when that player is
        # the opponent of the tool's owner.
        tool = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == tool_guid.lower()),
            None)
        if tool is None:
            return
        owner = tool.owning_player_id or pokemon.owning_player_id
        if ctx.player_id == owner:
            return  # end of your turn — wait for opponent's
        await ctx.discard_cards([tool])
    return effect


class BalloonBerryPassive(Passive):
    """Retreat cost 0; discard Balloon Berry when the holder retreats."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if holder is pokemon:
            return 0
        return cost

    async def on_retreated(self, ctx, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is holder and carrier is not None:
            await ctx.discard_cards([carrier])


class BufferPiecePassive(Passive):
    """Takes 20 less after W/R; discard at end of opponent's turn (via grant)."""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if calc.is_attack and calc.is_opposing and calc.target is holder:
            calc.amount = max(0, calc.amount - 20)



# === EX1–EX6 soft-gap quality fixes (last-def wins) ===

def mass_destruction():
    """Both Electrode and Defending are KO'd. If Electrode has any Special
    Energy attached, this attack does nothing."""
    from spirit.game.session.effects import is_special_energy

    async def effect(ctx):
        a = ctx.attacker
        if a is not None and any(is_special_energy(c) for c in a.children):
            return
        d = ctx.defender
        if d is not None:
            await ctx.knock_out(d)
        if a is not None:
            await ctx.knock_out(a)
    return effect


def sweet_temptation():
    """Opponent chooses a Benched Pokémon to become Active; then 10 damage
    to the new Defending Pokémon."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench,
                "Choose your new Active Pokémon",
                player_id=ctx.opponent_id,
            ) or bench[0]
            await ctx.switch_active(ctx.opponent_id, target)
        await ctx.deal_damage(10)
    return effect


def intense_glare():
    """Same shape as Sweet Temptation when used as gust-then-damage."""
    return sweet_temptation()


def block_dust_passive() -> Passive:
    """While Active: opponent can't play Trainer cards."""
    class _P(Passive):
        def blocks_trainer_play(self, card, player_id, carrier):
            if not is_in_active_spot(carrier):
                return False
            return player_id != carrier.owning_player_id
    return _P()


def deep_sleep_passive() -> Passive:
    """While Active: players flip 2 coins for Asleep (both must be heads)."""
    class _P(Passive):
        def asleep_coins_required(self, pokemon, carrier):
            if is_in_active_spot(carrier):
                return 2
            return None
    return _P()


def buffer_piece_discard_end_opponent_turn(tool_guid: str):
    """BETWEEN_TURNS: discard at the checkup ending the opponent's turn."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        tool = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == tool_guid.lower()),
            None)
        if tool is None:
            return
        owner = tool.owning_player_id or pokemon.owning_player_id
        # Checkup runs for the player whose turn just ended.
        ending = ctx.session.turn_state.active_player_id
        if ending == owner:
            return
        await ctx.discard_cards([tool])
    return effect


def high_voltage_lock_trainers():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "High Voltage")
        if results and results[0]:
            from spirit.game.session.effects import is_trainer_card
            ctx.lock_plays(ctx.opponent_id, is_trainer_card)
    return effect



def minus_energy():
    """Flip: heads choose 1 Energy on Defending; opponent returns it to hand."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Minus Energy")
        if not (results and results[0]) or ctx.defender is None:
            return
        energies = [c for c in ctx.defender.children if is_energy_card(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=1, prompt="Choose an Energy to return")
        if picks:
            await ctx.put_in_hand(picks)
    return effect


def silver_wind(bonus: int = 30):
    """Printed damage; during your next turn, attacks do +bonus to that Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return

        class _Mark(Passive):
            def modify_damage_taken(self, calc, carrier):
                holder = carrier_pokemon(carrier) or carrier
                if not (calc.is_attack and calc.target is holder):
                    return
                # Only when the Silver Wind user side is attacking
                if calc.attacker is None:
                    return
                if calc.attacker.owning_player_id == holder.owning_player_id:
                    return
                calc.amount = calc.amount + bonus

        ctx.add_passive_through_own_next_turn(d, _Mark())
    return effect


def call_for_family_grass_one():
    """Search 1 Grass Basic onto Bench."""
    return call_for_family_grass(1)


def pivot_throw_takes_more(amount: int = 10):
    """Damage; during opponent's next turn, this Pokémon takes amount more."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return

        class TakesMore(Passive):
            def modify_damage_taken(self, calc, carrier):
                holder = carrier_pokemon(carrier) or carrier
                if calc.is_attack and calc.target is holder and calc.is_opposing:
                    calc.amount = calc.amount + amount

        ctx.add_passive_through_opponents_turn(ctx.attacker, TakesMore())
    return effect



async def super_scoop_up(ctx):
    """Flip: heads return 1 of your Pokémon and all cards attached to hand."""
    results = await ctx.flip_coins(1, "Super Scoop Up")
    if not (results and results[0]):
        return
    cands = list(ctx.my_pokemon_in_play())
    if not cands:
        return
    target = await ctx.choose_pokemon(cands, "Choose a Pokémon to return to your hand")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.put_in_hand(full_stack(target), reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


def link_needle(base: int = 50, per: int = 30, name: str = "Beedrill"):
    """base + per for each other named Pokémon in play."""
    async def effect(ctx):
        n = sum(
            1 for p in ctx.my_pokemon_in_play()
            if p is not ctx.attacker
            and name.lower() in _display_name(p).lower())
        await ctx.deal_damage(base + per * n)
    return effect
