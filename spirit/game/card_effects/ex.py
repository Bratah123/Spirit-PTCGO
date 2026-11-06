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
    AbilityTypes, AttrID, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.card_effects.attacks_common import (
    count_energy, discard_random_from_hand, lock_all_attacks,
)
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost, is_in_active_spot,
)
from spirit.game.card_effects.pokemon import (
    devolvable, energy_provides_type, is_energy_card,
)
from spirit.game.card_effects.support_common import opponent_switches, search_to_bench
from spirit.game.card_effects.trainers import FossilBodyPassive, is_basic_energy_card
from spirit.game.data_utils import TRAINER_EFFECTS_BY_GUID, def_for, subtypes_for, unimplemented
from spirit.game.session.effects import (
    full_stack, is_basic_pokemon, is_evolution_pokemon, is_supporter_card,
)
from spirit.game.session.passives import (
    Passive, carrier_pokemon, effective_max_hp, effective_pokemon_types,
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
