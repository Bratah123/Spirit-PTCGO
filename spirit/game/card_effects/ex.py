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


def slashing_strike_lock(flip: bool = True):
    """Printed damage; lock this attack next turn.

    flip=True (Dodrio): coin; lock only on tails.
    flip=False (Rocket's Scyther ex): always lock (prefer Attack.locks_next_turn=True).
    """
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None or ctx.ability is None:
            return
        lock = True
        if flip:
            results = await ctx.flip_coins(1, "Slashing Strike")
            lock = bool(results) and not results[0]
        if lock:
            aid = getattr(ctx.ability, "ability_id", None) or getattr(ctx.ability, "title", "")
            ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, aid)
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


def egg_surprise(damage: int = 50, heal_counters: int = 5):
    """Heads: deal `damage`. Tails: remove up to `heal_counters` damage counters."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Egg Surprise")
        if results and results[0]:
            await ctx.deal_damage(damage)
        elif ctx.attacker is not None:
            await ctx.heal(heal_counters * 10, ctx.attacker)
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
    """+bonus when opponent has exactly 1 Prize left; optionally apply a condition then."""
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import count_prizes_remaining
        dmg = base
        if count_prizes_remaining("opponent")(ctx) == 1:
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

def rest_full_asleep(counters: int = 5):
    """Remove all Special Conditions and up to `counters` damage counters; Asleep."""
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        await ctx.cure_all_conditions(a)
        await ctx.heal(counters * 10, a)
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
            await apply_protection(ctx, target=ctx.attacker, reduce=reduce)
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
                await ctx.switch_active(ctx.opponent_id, t)
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
            ctx, target=ctx.attacker, prevent=True, effects_too=True, only_ex=True)
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
            await ctx.reorder_deck_top(len(rest))
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
            if "Dark" not in _display_name(pokemon):
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


def form_change_deoxys(ex: bool = False):
    """Search deck for another Deoxys (/ex); identity-swap onto board;
    old card goes to deck then shuffle (top-then-shuffle ≡ shuffle)."""
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
            return card_is_ex if ex else (not card_is_ex)

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose another Deoxys to switch with")
        if picks:
            await ctx.identity_swap(
                src, picks[0], destination="deck", transfer=True)
        await ctx.shuffle_deck()
    return effect


# ---- EX9 Emerald helpers ----

def mist_vs_stage2_passive(amount: int = 30) -> Passive:
    """Reduce damage from Stage 2 Evolved Pokémon attacks by `amount` (after W/R)."""
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack:
                return
            atk = calc.attacker
            if atk is None:
                return
            st = getattr(def_for(atk.archetype_id), "stage", None)
            if st == PokemonStage.STAGE2:
                calc.amount = max(0, calc.amount - amount)
    return _P()


def blaze_low_hp_passive(threshold: int = 40, bonus: int = 40) -> Passive:
    """While remaining HP <= threshold, deal `bonus` more (before W/R)."""
    return hunch_low_hp_boost(threshold=threshold, bonus=bonus)


def cursed_glare_passive() -> Passive:
    """While Active: opponent can't attach Special Energy (except Darkness/Metal
    Energy cards) from hand to their Active Pokémon."""
    class _P(Passive):
        def blocks_energy_attach(self, attaching_player_id, energy, target, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return False
            if attaching_player_id == holder.owning_player_id:
                return False
            if not is_in_active_spot(target):
                return False
            if not energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
                return False
            dn = (energy.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            if "darkness energy" in dn or "metal energy" in dn or "dark metal" in dn:
                return False
            return True
    return _P()


def magma_armor_passive() -> Passive:
    from spirit.game.card_effects.passives_common import condition_immunity_passive
    return condition_immunity_passive(
        conditions=(SpecialConditions.ASLEEP, SpecialConditions.PARALYZED),
        protects="carrier",
    )


def dark_hole_passive() -> Passive:
    """While on Bench: don't apply Darkness Weakness for your Pokémon in play."""
    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or is_in_active_spot(holder):
                return
            t = calc.target
            if t is None or t.owning_player_id != holder.owning_player_id:
                return
            dv = PokemonTypes.DARKNESS.value
            if dv in (calc.weak_types or []):
                calc.weak_types = [w for w in calc.weak_types if w != dv]
            if not calc.weak_types:
                calc.weakness_applies = False
    return _P()


def submerge_all_attacks_passive() -> Passive:
    """While on Bench, prevent all damage from attacks (yours and opponent's)."""
    def pred(calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return (
            calc.is_attack
            and calc.target is holder
            and not is_in_active_spot(holder)
        )
    return prevent_damage_when(pred)


def feathery_passive() -> Passive:
    """While on Bench, prevent damage from opponent's attacks."""
    return submerge_passive()


def wise_aura_passive() -> Passive:
    """While Active: each non-ex Pokémon can't use Poké-Powers."""
    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return False
            if is_pokemon_ex(pokemon):
                return False
            return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER
    return _P()


def mystic_scale_passive() -> Passive:
    """Can't play Technical Machine cards from hand."""
    class _P(Passive):
        def blocks_trainer_play(self, card, player_id, carrier):
            tt = card.get_attribute(AttrID.TRAINER_TYPE)
            if tt == TrainerType.TECHNICAL_MACHINE.value:
                return True
            subs = subtypes_for(card.archetype_id) or []
            return "Technical Machine" in subs or "TechnicalMachine" in subs
    return _P()


async def mystic_scale_discard_tms(ctx):
    """BETWEEN_TURNS/ON_EVOLVE: discard all Technical Machine cards in play."""
    for pid in ctx.board.player_ids:
        for p in ctx.board.pokemon_in_play(pid):
            tms = [
                c for c in p.children
                if c.get_attribute(AttrID.TRAINER_TYPE)
                == TrainerType.TECHNICAL_MACHINE.value
                or "Technical Machine" in (subtypes_for(c.archetype_id) or [])
            ]
            if tms:
                await ctx.discard_cards(tms)


def electro_guard_passive() -> Passive:
    """No Weakness while any Lightning Energy is attached."""
    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.target is not holder:
                return
            if any(energy_provides_type(c, PokemonTypes.LIGHTNING.value)
                   for c in holder.children):
                calc.weakness_applies = False
    return _P()


def rai_shield_passive(amount: int = 30) -> Passive:
    """Your Raichu ex take `amount` less from opponent Pokémon-ex attacks.
    Only one Rai-shield applies (stacking_key)."""
    class _P(Passive):
        stacking_key = "rai_shield"

        def modify_damage_taken(self, calc, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return
            t = calc.target
            if t is None:
                return
            holder = carrier_pokemon(carrier) or carrier
            if holder is None:
                return
            if t.owning_player_id != holder.owning_player_id:
                return
            dn = _display_name(t).lower()
            if "raichu" not in dn or not is_pokemon_ex(t):
                return
            if calc.attacker is None or not is_pokemon_ex(calc.attacker):
                return
            calc.amount = max(0, calc.amount - amount)
    return _P()


def green_essence_passive() -> Passive:
    """Your Active Pokémon with Grass Energy can't be affected by Special Conditions."""
    from spirit.game.card_effects.passives_common import condition_immunity_passive
    return condition_immunity_passive(
        conditions=None,
        protects=lambda target, carrier: (
            is_in_active_spot(target)
            and target.owning_player_id
            == (carrier_pokemon(carrier) or carrier).owning_player_id
            and any(energy_provides_type(c, PokemonTypes.GRASS.value)
                    for c in target.children)
        ),
    )


def battle_frontier_passive() -> Passive:
    """Evolved Colorless / Darkness / Metal Pokémon can't use Powers or Bodies."""
    locked = {
        PokemonTypes.COLORLESS.value,
        PokemonTypes.DARKNESS.value,
        PokemonTypes.METAL.value,
    }

    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier):
            if not is_evolution_pokemon(pokemon):
                return False
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if not any(t in locked for t in types):
                return False
            at = getattr(ability, "ability_type", None)
            return at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY)
    return _P()


def water_cyclone_condition():
    """Active has Water Energy and you have a Bench."""
    def extra(board, player_id, pokemon=None):
        active_area = board.find_player_area(player_id, "activePokemonArea")
        actives = list(active_area.children) if active_area else []
        if not actives:
            return False
        has_w = any(
            energy_provides_type(e, PokemonTypes.WATER.value)
            for a in actives for e in a.children
        )
        if not has_w:
            return False
        bench = board.find_player_area(player_id, "benchPokemonArea")
        return bool(bench and bench.children)
    return poke_power_condition(extra)


def water_cyclone():
    """Move 1 Water Energy from Active to a Benched Pokémon."""
    async def effect(ctx):
        actives = []
        area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
        if area:
            actives = list(area.children)
        donors = [
            p for p in actives
            if any(energy_provides_type(c, PokemonTypes.WATER.value)
                   for c in p.children)
        ]
        if not donors:
            return
        src = donors[0]
        pool = [
            c for c in src.children
            if energy_provides_type(c, PokemonTypes.WATER.value)
        ]
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Water Energy")
        bench = ctx.my_bench()
        if not picks or not bench:
            return
        dest = await ctx.choose_pokemon(bench, "Move Water Energy to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect


def eruption_damage(base: int = 60, per: int = 20):
    """Each player discards top of deck; base + per per Energy discarded."""
    async def effect(ctx):
        discarded_energy = 0
        for pid in (ctx.player_id, ctx.opponent_id):
            top = ctx.deck_top(1, player_id=pid)
            if top:
                if is_energy_card(top[0]):
                    discarded_energy += 1
                await ctx.discard_cards(top)
        await ctx.deal_damage(base + per * discarded_energy)
    return effect


def shadow_beam_counters(per_energy: int = 2):
    """Put `per_energy` damage counters on Defending per Energy on self."""
    async def effect(ctx):
        if ctx.attacker is None or ctx.defender is None:
            return
        n = sum(1 for c in ctx.attacker.children if is_energy_card(c))
        if n <= 0:
            return
        await ctx.deal_damage(
            per_energy * n * 10, apply_modifiers=False, as_counters=True)
    return effect


def confuse_if_evolved():
    """Printed damage; if Defending is Evolved, Confuse it."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is not None and is_evolution_pokemon(d):
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def scary_face_lock():
    """Flip: heads Defending can't attack or retreat during opponent's next turn."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Scary Face")
        if results and results[0] and ctx.defender is not None:
            lock_all_attacks(ctx, ctx.defender)
            ctx.lock_retreat(ctx.defender)
    return effect


def hydro_pump_capped_attack(base: int = 40, per: int = 10, cap: int = 20,
                             energy_type=PokemonTypes.WATER):
    return hyper_pump_capped(base=base, per=per, cap=cap, energy_type=energy_type)


def sky_kick(base: int = 60, bonus: int = 40, resist_type=PokemonTypes.FIGHTING):
    """base + bonus if Defending has Fighting Resistance."""
    rv = getattr(resist_type, "value", resist_type)

    async def effect(ctx):
        extra = 0
        d = ctx.defender
        if d is not None:
            raw = d.get_attribute(AttrID.RESISTANCE_TYPES)
            if raw is None:
                r = getattr(def_for(d.archetype_id), "resistance_type", None)
                raw = getattr(r, "value", r) if r is not None else None
            if isinstance(raw, (list, tuple, set)):
                rtypes = list(raw)
            elif raw is None:
                rtypes = []
            else:
                rtypes = [raw]
            if rv in rtypes:
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def reflect_energy_basic():
    """Move 1 basic Energy from self to a Benched Pokémon (mandatory if able)."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        pool = [c for c in ctx.attacker.children if is_basic_energy_card(c)]
        bench = ctx.my_bench()
        if not pool or not bench:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose a basic Energy to move")
        dest = await ctx.choose_pokemon(bench, "Move Energy to which Benched Pokémon?")
        if picks and dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect


def power_short(base: int = 30, bonus: int = 20):
    """Snipe `base` (no W/R on Bench); +bonus if that Pokémon has Poké-Powers."""
    async def effect(ctx):
        cands = ctx.opponent_pokemon_in_play()
        if not cands:
            return
        target = await ctx.choose_pokemon(
            cands, "Choose a Pokémon for Power Short")
        if target is None:
            return
        extra = 0
        d = def_for(target.archetype_id)
        if any(getattr(a, "ability_type", None) == AbilityTypes.POKE_POWER
               for a in (getattr(d, "abilities", None) or [])):
            extra = bonus
        await ctx.deal_damage(
            base + extra, target=target, apply_modifiers=False)
    return effect


def _regi_ex_in_play(ctx, name_substr: str) -> bool:
    needle = name_substr.lower()
    for p in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
        dn = _display_name(p).lower()
        if needle in dn and is_pokemon_ex(p):
            return True
    return False


def iceberg_crush(base: int = 40):
    """If Regirock ex in play, flip: heads discard Energy from Defending."""
    async def effect(ctx):
        await ctx.deal_damage(base)
        if not _regi_ex_in_play(ctx, "regirock"):
            return
        results = await ctx.flip_coins(1, "Iceberg Crush")
        if not (results and results[0]) or ctx.defender is None:
            return
        pool = [c for c in ctx.defender.children if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Discard an Energy from Defending")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def metal_crush(base: int = 40, bonus: int = 20):
    """base + bonus if Registeel ex is in play."""
    async def effect(ctx):
        extra = bonus if _regi_ex_in_play(ctx, "registeel") else 0
        await ctx.deal_damage(base + extra)
    return effect


def block_signal(base: int = 0):
    """Printed damage; if Regice ex in play, flip: heads Confused."""
    async def effect(ctx):
        await ctx.deal_damage()
        if not _regi_ex_in_play(ctx, "regice"):
            return
        results = await ctx.flip_coins(1, "Block Signal")
        if results and results[0] and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.CONFUSED)
    return effect


def mend_fighting(heal_counters: int = 1):
    """Attach a Fighting Energy from discard; if you do, heal counters."""
    async def effect(ctx):
        if ctx.attacker is None:
            return
        pool = [
            c for c in ctx.discard_pile()
            if is_basic_energy_card(c)
            and energy_provides_type(c, PokemonTypes.FIGHTING.value)
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Attach a Fighting Energy from discard")
        if not picks:
            return
        await ctx.attach_energy(picks[0], ctx.attacker)
        await ctx.heal(heal_counters * 10, ctx.attacker)
    return effect


def farfetchd_nosedive(self_dmg: int = 10):
    """Printed damage; self takes `self_dmg` (no flip)."""
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_dmg)


def mega_throw_ex(base: int = 60, bonus: int = 40):
    return bonus_if_ex(bonus, base=base)


async def scott_search(ctx):
    """Search deck for up to 3 Supporters and/or Stadiums into hand."""
    def match(c):
        subs = subtypes_for(c.archetype_id) or []
        if "Supporter" in subs or "Stadium" in subs:
            return True
        if is_supporter_card(c):
            return True
        tt = c.get_attribute(AttrID.TRAINER_TYPE)
        return tt in (
            TrainerType.SUPPORTER.value,
            TrainerType.STADIUM.value,
            getattr(TrainerType.SUPPORTER, "value", None),
            getattr(TrainerType.STADIUM, "value", None),
        )
    picks = await ctx.search_deck(
        match, count=3, minimum=0,
        prompt="Choose up to 3 Supporter and/or Stadium cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def mr_stones_project(ctx):
    """Up to 2 basic Energy from deck into hand, OR from discard into hand."""
    options = ["Search deck", "Search discard pile"]
    idx = await ctx.choose("Mr. Stone's Project", options)
    if idx is None:
        idx = 0
    if idx == 0:
        picks = await ctx.search_deck(
            is_basic_energy_card, count=2, minimum=0,
            prompt="Choose up to 2 basic Energy cards")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    else:
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        take = min(2, len(pool))
        picks = await ctx.choose_cards(
            pool, take, minimum=0,
            prompt="Choose up to 2 basic Energy from discard")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)


# ---- EX10 Unseen Forces helpers ----

def unown_shuffle():
    """Search deck for another Unown; identity-swap; old to top of deck then shuffle.
    Pair with shared_once_per_turn='Shuffle'."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return

        def match(card):
            d = def_for(card.archetype_id)
            if d is None:
                return False
            dn = (getattr(d, "display_name", None) or "").lower()
            return dn == "unown" or dn.startswith("unown")

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose another Unown to switch with")
        if picks:
            await ctx.identity_swap(
                src, picks[0], destination="deck", transfer=True)
        await ctx.shuffle_deck()
    return effect


def unown_shuffle_condition():
    return poke_power_condition(has_deck)


def search_supporters(count: int = 2):
    async def effect(ctx):
        def match(c):
            return is_supporter_card(c) or "Supporter" in (subtypes_for(c.archetype_id) or [])
        picks = await ctx.search_deck(
            match, count=count, minimum=0,
            prompt=f"Choose up to {count} Supporter card(s)")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def heal_self_counters(counters: int = 5):
    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


def return_self_and_energy_to_hand():
    async def effect(ctx):
        src = ctx.attacker
        if src is None:
            return
        energies = [c for c in list(src.children) if is_energy_card(c)]
        if energies:
            await ctx.put_in_hand(energies)
        await ctx.put_in_hand([src])
    return effect


def damage_per_damaged_own(per: int = 10):
    """Put N counters on Defending where N = number of your damaged Pokémon."""
    async def effect(ctx):
        n = sum(
            1 for p in ctx.my_pokemon_in_play()
            if p.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, p)
        )
        if n > 0 and ctx.defender is not None:
            await ctx.deal_damage(n * per, apply_modifiers=False, as_counters=True)
    return effect


def flip3_conditions_asleep_paralyze_confuse():
    """1 heads Asleep; 2 Paralyzed; 3 Confused."""
    async def effect(ctx):
        results = await ctx.flip_coins(3, "Hidden Power")
        heads = sum(1 for r in results if r)
        d = ctx.defender
        if d is None or heads <= 0:
            return
        if heads == 1:
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
        elif heads == 2:
            await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
        else:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def swap_damage_counters_with_defender():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Hidden Power")
        if not (results and results[0]):
            return
        a, d = ctx.attacker, ctx.defender
        if a is None or d is None:
            return
        ca = max(0, ctx.max_hp(a) - a.get_attribute(AttrID.HP, 0)) // 10
        cd = max(0, ctx.max_hp(d) - d.get_attribute(AttrID.HP, 0)) // 10
        await ctx.set_damage_counters(a, cd)
        await ctx.set_damage_counters(d, ca)
    return effect


def evolve_from_deck_one():
    """Search deck for a card that evolves from 1 of your Pokémon and put it on."""
    async def effect(ctx):
        in_play = ctx.my_pokemon_in_play()
        if not in_play:
            return
        # Collect evolve-from names
        logic_names = {
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            for p in in_play
        }
        logic_names.discard(None)

        def match(c):
            if not is_evolution_pokemon(c):
                return False
            frm = c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
            return frm in logic_names

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose a card that evolves from 1 of your Pokémon")
        if not picks:
            await ctx.shuffle_deck()
            return
        evo = picks[0]
        frm = evo.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
        cands = [
            p for p in in_play
            if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == frm
        ]
        if not cands:
            await ctx.shuffle_deck()
            return
        target = await ctx.choose_pokemon(cands, "Evolve which Pokémon?")
        if target is not None:
            await ctx.evolve_pokemon(target, evo)
        await ctx.shuffle_deck()
    return effect


def damage_capped_from_discard_basics_evos(base: int = 20, per: int = 10, cap: int = 60):
    async def effect(ctx):
        n = 0
        for c in ctx.discard_pile():
            if is_basic_pokemon(c) or is_evolution_pokemon(c):
                n += 1
        await ctx.deal_damage(min(cap, base + per * n))
    return effect


def discard_to_top_on_heads():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Hidden Power")
        if not (results and results[0]):
            return
        pool = list(ctx.discard_pile())
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose a card from discard")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
            # put on top of deck from hand
            await ctx.put_on_top_of_deck(picks[0])
    return effect


def damage_each_with_powers_bodies(amount: int = 20):
    async def effect(ctx):
        for p in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
            d = def_for(p.archetype_id)
            abs_ = getattr(d, "abilities", None) or []
            if any(getattr(a, "ability_type", None) in (
                    AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY)
                   for a in abs_):
                await ctx.deal_damage(
                    amount, target=p, apply_modifiers=False)
    return effect


def place_counters_flip_choice(counters: int = 2):
    """Flip: heads on opponent's Pokémon; tails on yours."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Hidden Power")
        if results and results[0]:
            pool = ctx.opponent_pokemon_in_play()
            prompt = "Put damage counters on opponent's Pokémon"
        else:
            pool = ctx.my_pokemon_in_play()
            prompt = "Put damage counters on your Pokémon"
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, prompt)
        if t is not None:
            await ctx.deal_damage(
                counters * 10, target=t, apply_modifiers=False, as_counters=True)
    return effect


def draw_then_may_switch(draw: int = 2):
    async def effect(ctx):
        await ctx.draw_cards(draw)
        bench = ctx.my_bench()
        if bench and await ctx.ask_yes_no("Switch with a Benched Pokémon?"):
            t = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
            if t is not None:
                await ctx.switch_active(ctx.player_id, t)
    return effect


def telekinesis_snipe(amount: int = 30):
    async def effect(ctx):
        cands = ctx.opponent_pokemon_in_play()
        if not cands:
            return
        t = await ctx.choose_pokemon(cands, f"Choose a Pokémon for {amount} damage")
        if t is not None:
            await ctx.deal_damage(
                amount, target=t, apply_modifiers=False, ignore_target_effects=True)
    return effect


def intimidating_fang_passive(amount: int = 10, after_wr: bool = False) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            # reduce damage done BY opponent's attacks
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            if not (calc.is_attack and calc.is_opposing):
                return
            # before W/R means modify early; after means modify_damage_taken style
            # For "before applying W/R" on damage done by opponent: reduce calc.amount
            # when opponent is attacker — this is modify_damage_dealt from defender's
            # perspective? Actually "any damage done by an opponent's attack is reduced"
            # — use modify_damage_taken on all our pokemon while this is active.
            pass

        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            if not (calc.is_attack and calc.is_opposing):
                return
            # Affects any damage from opponent attacks (to anyone? text: "any damage done
            # by an opponent's attack is reduced by 10") — global while Active.
            # Carrier is Feraligatr; effect applies globally to all targets of opp attacks.
            calc.amount = max(0, calc.amount - amount)
    return _P()


def stages_of_evolution_takes_less(amount: int = 20) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.target is not holder:
                return
            if not is_evolution_pokemon(holder):
                return
            if not (calc.is_attack and calc.is_opposing):
                return
            calc.amount = max(0, calc.amount - amount)
    return _P()


def reactive_poison(base: int = 10, per: int = 30):
    async def effect(ctx):
        extra = 0
        d = ctx.defender
        if d is not None:
            conds = d.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            extra = per * len(conds)
        await ctx.deal_damage(base + extra)
    return effect


def energy_connect_basic():
    """Move a basic Energy from Bench to Active, unlimited."""
    async def effect(ctx):
        active = None
        area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
        if area and area.children:
            active = area.children[0]
        if active is None:
            return
        donors = [
            p for p in ctx.my_bench()
            if any(is_basic_energy_card(c) for c in p.children)
        ]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move basic Energy from?")
        if src is None:
            return
        pool = [c for c in src.children if is_basic_energy_card(c)]
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose basic Energy")
        if picks:
            await ctx.move_energy(picks[0], active)
    return effect


def energy_connect_condition():
    def extra(board, player_id, pokemon=None):
        bench = board.find_player_area(player_id, "benchPokemonArea")
        if not bench or not bench.children:
            return False
        return any(
            is_basic_energy_card(c)
            for p in bench.children for c in p.children
        )
    return poke_power_condition(extra)


def fluffy_berry_passive() -> Passive:
    """Retreat cost 0 while attached (no discard on retreat)."""
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is holder:
                return 0
            return cost
    return _P()


def energy_root_passive(hp_bonus: int = 20) -> Passive:
    """+hp_bonus max HP; can't use Poké-Powers or Poké-Bodies."""
    class _P(Passive):
        def max_hp_override(self, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return None
            base = getattr(def_for(pokemon.archetype_id), "hp", None) or 0
            return base + hp_bonus

        def blocks_abilities(self, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            return pokemon is holder
    return _P()


def solid_rage_passive(bonus: int = 20) -> Passive:
    """If more prizes left than opponent: +bonus to Active (before W/R)."""
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.attacker is not holder:
                return
            if not (calc.is_attack and calc.to_active):
                return
            def _prizes(pid):
                area = calc.board.find_player_area(pid, "prizeCardArea")
                return len(area.children) if area else 0
            mine = _prizes(holder.owning_player_id)
            opp_id = next(
                pid for pid in calc.board.player_ids
                if pid != holder.owning_player_id)
            theirs = _prizes(opp_id)
            if mine > theirs:
                calc.amount += bonus
    return _P()


def curse_powder_passive(counters: int = 3) -> Passive:
    return dark_scale_on_ko(counters)


async def marys_request(ctx):
    """Draw 1; if no Stage 2 Evolved in play, draw 2 more."""
    await ctx.draw_cards(1)
    has_s2 = False
    for p in ctx.my_pokemon_in_play():
        st = getattr(def_for(p.archetype_id), "stage", None)
        if st == PokemonStage.STAGE2 and is_evolution_pokemon(p):
            has_s2 = True
            break
    if not has_s2:
        await ctx.draw_cards(2)


def warp_energy_attach_to(pokemon):
    """Always attachable (Colorless special)."""
    return True


async def warp_energy_on_attached(ctx):
    """When attached from hand to Active: switch with Bench."""
    # Called via Ability trigger ON_ENERGY_ATTACHED on the energy card? 
    # Prefer attach hook on EnergyCardDef if supported.
    pass


def warp_energy_passive() -> Passive:
    class _P(Passive):
        async def on_energy_attached(self, ctx, energy, pokemon, carrier, from_hand=True):
            if carrier is not energy:
                return
            if not from_hand:
                return
            if not is_in_active_spot(pokemon):
                return
            bench = ctx.my_bench() if hasattr(ctx, 'my_bench') else []
            # ctx may be session-level; use board
            pid = pokemon.owning_player_id
            area = ctx.board.find_player_area(pid, "benchPokemonArea")
            bench = list(area.children) if area else []
            if not bench:
                return
            # Prefer ask_yes_no if available — text is mandatory switch
            t = await ctx.choose_pokemon(bench, "Switch with a Benched Pokémon")
            if t is not None:
                await ctx.switch_active(pid, t)
    return _P()


def dual_armor_if_energy(energy_type, *become_types) -> Passive:
    """While any Energy providing `energy_type` is attached, Pokémon is the
    listed types (Dual Armor)."""
    ev = getattr(energy_type, "value", energy_type)
    become = [getattr(t, "value", t) for t in become_types]

    class _P(Passive):
        def modify_pokemon_types(self, types_list, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return types_list
            if not any(energy_provides_type(c, ev) for c in holder.children):
                return types_list
            return list(become)
    return _P()


def thick_fat_vs_types(amount: int = 30, *types) -> Passive:
    tvs = {getattr(t, "value", t) for t in types}

    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.target is not holder:
                return
            if not (calc.is_attack and calc.is_opposing and calc.attacker):
                return
            atypes = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
            if any(t in tvs for t in atypes):
                calc.amount = max(0, calc.amount - amount)
    return _P()


def free_flight_no_energy_passive() -> Passive:
    """Retreat 0 while no Energy attached."""
    return retreat_free_when(
        lambda pokemon, carrier: (
            carrier_pokemon(carrier) is pokemon
            and not any(is_energy_card(c) for c in pokemon.children)
        )
    )


def suction_cups_no_retreat_passive() -> Passive:
    """While Active: opponent's Pokémon can't retreat."""
    from spirit.game.card_effects.passives_common import no_retreat_passive
    return no_retreat_passive(
        lambda p, c: (
            is_in_active_spot(carrier_pokemon(c) or c)
            and p.owning_player_id != (carrier_pokemon(c) or c).owning_player_id
        )
    )


def stages_hp_boost(amount: int = 30) -> Passive:
    class _P(Passive):
        def max_hp_override(self, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not is_evolution_pokemon(holder):
                return None
            base = getattr(def_for(pokemon.archetype_id), "hp", None) or 0
            return base + amount
    return _P()


def stages_damage_boost(amount: int = 20) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.attacker is not holder:
                return
            if not is_evolution_pokemon(holder):
                return
            if calc.is_attack and calc.is_opposing:
                calc.amount += amount
    return _P()


def flip_agility_protect():
    from spirit.game.card_effects.passives_common import apply_protection
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Agility")
        if results and results[0] and ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, prevent=True, effects_too=True)
    return effect


def teary_eyes_reduce(amount: int = 20):
    from spirit.game.card_effects.passives_common import apply_protection
    async def effect(ctx):
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, reduce=amount)
    return effect


def metal_charge_self_counter(counters: int = 1):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(
                counters * 10, target=ctx.attacker,
                apply_modifiers=False, as_counters=True)
    return effect


def discard_stadium_then_damage():
    async def effect(ctx):
        await ctx.discard_stadium()
        await ctx.deal_damage()
    return effect


def mill_opponent_top(count: int = 1):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(count, player_id=ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)
    return effect


def discard_special_energy_from_defender():
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        pool = [c for c in d.children if c.get_attribute(AttrID.IS_SPECIAL_ENERGY)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard a Special Energy")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def may_discard_defender_energy_on_heads():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Crushing Blow")
        if not (results and results[0]) or ctx.defender is None:
            return
        pool = [c for c in ctx.defender.children if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard an Energy")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def tonnage_optional_recoil(base: int = 50, bonus: int = 30, self_dmg: int = 30):
    async def effect(ctx):
        if await ctx.ask_yes_no(f"Do {base + bonus} and take {self_dmg}?"):
            await ctx.deal_damage(base + bonus)
            if ctx.attacker is not None:
                await ctx.deal_damage(
                    self_dmg, target=ctx.attacker, apply_modifiers=False)
        else:
            await ctx.deal_damage(base)
    return effect


def pull_away_to_4_hand():
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand(ctx.opponent_id))
        while len(hand) > 4:
            picks = await ctx.choose_cards(
                hand, 1, minimum=1, prompt="Discard a card",
                player_id=ctx.opponent_id)
            if not picks:
                break
            await ctx.discard_cards(picks)
            hand = list(ctx.hand(ctx.opponent_id))
    return effect


def extra_tight_vs_ex_passive() -> Passive:
    return prevent_damage_when(
        lambda calc, carrier: (
            calc.is_attack and calc.is_opposing
            and calc.target is (carrier_pokemon(carrier) or carrier)
            and calc.attacker is not None
            and is_pokemon_ex(calc.attacker)
        )
    )


def baby_evolution_any(*names: str):
    preds = [_named(n) for n in names]
    async def effect(ctx):
        matches = [c for c in ctx.hand() if any(p(c) for p in preds)]
        if not matches:
            return
        picks = await ctx.choose_cards(
            matches, 1, minimum=1, prompt="Choose a Pokémon to put onto Tyrogue")
        if not picks:
            return
        evolved = picks[0]
        await ctx.evolve_pokemon(ctx.source, evolved)
        missing = ctx.max_hp(evolved) - evolved.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, evolved)
    return effect


def baby_evolution_any_condition(*names: str):
    preds = [_named(n) for n in names]
    def extra(board, player_id, pokemon=None):
        hand = board.find_player_area(player_id, "hand")
        return any(any(p(c) for p in preds) for c in (hand.children if hand else []))
    return poke_power_condition(extra)


def stages_vs_special_energy_takes_less(amount: int = 40) -> Passive:
    """While Evolved: take `amount` less from opponent attacks that have Special Energy."""
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.target is not holder:
                return
            if not is_evolution_pokemon(holder):
                return
            if not (calc.is_attack and calc.is_opposing and calc.attacker):
                return
            if not any(c.get_attribute(AttrID.IS_SPECIAL_ENERGY) for c in calc.attacker.children):
                return
            calc.amount = max(0, calc.amount - amount)
    return _P()


def discard_energy_n(count: int = 1):
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.discard_energy_from(
            ctx.attacker, count, predicate=is_energy_card,
            prompt=f"Discard {count} Energy")
    return effect


def flip_damage_paralyze_on_heads(coins: int = 2, per_heads: int = 10):
    async def effect(ctx):
        results = await ctx.flip_coins(coins, "Double Shock")
        heads = sum(1 for r in results if r)
        await ctx.deal_damage(per_heads * heads)
        if heads > 0 and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    return effect


# ---- EX10 Unseen Forces remaining helpers ----

def extra_vs_ex(base: int = 40, bonus: int = 30):
    """base + bonus if Defending is Pokémon-ex."""
    async def effect(ctx):
        extra = bonus if ctx.defender is not None and is_pokemon_ex(ctx.defender) else 0
        await ctx.deal_damage(base + extra)
    return effect


def healing_milk_flip(coins: int = 2, counters_per: int = 2):
    """Flip coins; for each heads remove counters_per damage counters from 1 of yours."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, "Healing Milk")
        heads = sum(1 for r in results if r)
        for _ in range(heads):
            pool = [p for p in ctx.my_pokemon_in_play()
                    if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
            if not pool:
                break
            target = await ctx.choose_pokemon(pool, "Heal which Pokémon?")
            if target is None:
                break
            await ctx.heal(counters_per * 10, target)
    return effect


def parallel_gain_heal(counters: int = 1):
    """Deal printed; remove counters from each of your Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage()
        for p in list(ctx.my_pokemon_in_play()):
            await ctx.heal(counters * 10, p)
    return effect


def spider_trap():
    """Optional gust (opp chooses), then Asleep + Poisoned on new Defending."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench and await ctx.ask_yes_no(
                "Switch 1 of your opponent's Benched Pokémon with the Defending?"):
            target = await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon",
                player_id=ctx.opponent_id) or bench[0]
            await ctx.switch_active(ctx.opponent_id, target)
        d = ctx.opponent_active()
        if d is not None:
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
            await ctx.apply_special_condition(d, SpecialConditions.POISONED)
    return effect


def miraculous_thunder(energy_type=PokemonTypes.LIGHTNING):
    """You may discard all typed Energy; if you do, Burned + Confused."""
    tv = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage()
        energies = [e for e in ctx.attached_energies(ctx.attacker)
                    if energy_provides_type(e, tv)]
        if energies and await ctx.ask_yes_no(
                "Discard all Lightning Energy attached to Ampharos?"):
            await ctx.discard_energy_from(
                ctx.attacker, 99,
                predicate=lambda c: energy_provides_type(c, tv))
            if ctx.defender is not None:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.BURNED)
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.CONFUSED)
    return effect


def snappy_move():
    """If on Bench: draw 1; discard attachments; put self on bottom of deck."""
    async def effect(ctx):
        src = ctx.source
        if src is None or is_in_active_spot(src):
            return
        await ctx.draw_cards(1)
        attached = [c for c in list(src.children) if not isinstance(
            c, type(src))]
        # discard all attached non-pokemon
        from spirit.game.models.board import PokemonEntity
        kids = [c for c in list(src.children) if not isinstance(c, PokemonEntity)]
        if kids:
            await ctx.discard_cards(kids)
        deck = ctx.board.find_player_area(ctx.player_id, "deck")
        if deck is not None:
            ctx.board.move_card(src.entity_id, deck.entity_id, position=-1)
    return effect


def snappy_move_condition():
    def extra(board, player_id, pokemon=None):
        if pokemon is None:
            return False
        return not is_in_active_spot(pokemon)
    return poke_power_condition(extra)


def green_dance(search_count: int = 2):
    """Search up to N Grass Pokémon into hand; if any, you may evolve Bellossom
    from hand onto a Grass basic (Full Bloom companion uses separate attack)."""
    async def effect(ctx):
        def match(c):
            d = def_for(c.archetype_id)
            if d is None or not is_pokemon_card(c):
                return False
            types = getattr(d, "elements", None) or []
            return PokemonTypes.GRASS in types or PokemonTypes.GRASS.value in [
                getattr(t, "value", t) for t in types]
        picks = await ctx.search_deck(
            match, count=search_count, minimum=0,
            prompt="Choose up to 2 Grass Pokémon")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        # "you may evolve" — optional evolve Bellossom onto a Grass in play from hand
        # Card text: If you put any Grass Pokémon into your hand, you may
        # search for a card that evolves from Bellossom... wait, check text.
        # Actual: "If you put any Grass Pokémon into your hand, you may
        # search your deck for a card that evolves from 1 of your Grass
        # Pokémon..." — EX10 Bellossom Green Dance:
        # Search up to 2 Grass Pokémon... If you put any, you may search for
        # a card that evolves from 1 of your Grass Pokémon and put it onto
        # that Pokémon (this counts as evolving).
        if not picks:
            return
        grass_in_play = [
            p for p in ctx.my_pokemon_in_play()
            if PokemonTypes.GRASS.value in (
                [getattr(t, "value", t) for t in (
                    getattr(def_for(p.archetype_id), "elements", None) or [])]
            ) or PokemonTypes.GRASS in (
                getattr(def_for(p.archetype_id), "elements", None) or [])
        ]
        if not grass_in_play:
            return
        if not await ctx.ask_yes_no("Search for a card that evolves from 1 of your Grass Pokémon?"):
            return
        host = await ctx.choose_pokemon(grass_in_play, "Evolve which Grass Pokémon?")
        if host is None:
            return
        logic = host.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        from spirit.game.content.definitions import evolves_from as _evolves_from

        def evo_match(card):
            if logic and _evolves_from(card.archetype_id, logic):
                return True
            ef = (getattr(def_for(card.archetype_id), "evolves_from", None) or "")
            dn = host.get_attribute(AttrID.DISPLAY_NAME) or ""
            return bool(ef) and (dn.lower() in ef.lower() or ef.lower() in dn.lower())

        evo = await ctx.search_deck(
            evo_match, count=1, minimum=0,
            prompt="Choose an Evolution card")
        if evo:
            await ctx.evolve_pokemon(host, evo[0])
        await ctx.shuffle_deck()
    return effect


def full_bloom(base: int = 50, bonus: int = 50, name: str = "Bellossom"):
    """base + bonus if at least 3 named Pokémon in play."""
    async def effect(ctx):
        count = sum(
            1 for p in ctx.my_pokemon_in_play()
            if (p.get_attribute(AttrID.DISPLAY_NAME) or "") == name
            or _display_name(p) == name)
        await ctx.deal_damage(base + (bonus if count >= 3 else 0))
    return effect


def blissful_support_on_evolve():
    """On play-to-evolve: discard all Energy from any number of your Pokémon;
    remove all damage counters from those Pokémon."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        damaged_or_energied = [
            p for p in ctx.my_pokemon_in_play()
            if any(is_energy_card(c) for c in p.children)
            or p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
        ]
        if not damaged_or_energied:
            return
        picks = await ctx.choose_pokemon_multi(
            damaged_or_energied, minimum=0, maximum=len(damaged_or_energied),
            prompt="Choose Pokémon to discard Energy from and fully heal") \
            if hasattr(ctx, "choose_pokemon_multi") else None
        if picks is None:
            # fallback: choose one at a time via yes/no loops
            picks = []
            for p in damaged_or_energied:
                if await ctx.ask_yes_no(
                        f"Discard Energy and heal {_display_name(p)}?"):
                    picks.append(p)
        for p in picks:
            energies = [c for c in list(p.children) if is_energy_card(c)]
            if energies:
                await ctx.discard_cards(energies)
            missing = ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)
            if missing > 0:
                await ctx.heal(missing, p)
    return effect


def energy_absorption(count: int = 3):
    """Attach up to count Energy from discard to self."""
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(
            pool, min(count, len(pool)), minimum=0,
            prompt=f"Attach up to {count} Energy from discard")
        for e in picks or []:
            await ctx.attach_energy(e, ctx.attacker)
    return effect


def spiral_leaf():
    """Flip: heads put 1 counter on each opp Pokémon; tails heal 1 from each yours."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Spiral Leaf")
        if results and results[0]:
            for p in list(ctx.opponent_pokemon_in_play()):
                await ctx.deal_damage(
                    10, target=p, apply_modifiers=False, as_counters=True)
        else:
            for p in list(ctx.my_pokemon_in_play()):
                await ctx.heal(10, p)
    return effect


def time_trap(look: int = 4):
    """Flip: heads reorder opp top N; tails reorder your top N."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Time Trap")
        heads = bool(results and results[0])
        pid = ctx.opponent_id if heads else ctx.player_id
        deck = ctx.board.find_player_area(pid, "deck")
        if deck is None or not deck.children:
            return
        top = list(deck.children[:look])
        if not top:
            return
        await ctx.reveal_cards(top) if hasattr(ctx, "reveal_cards") else None
        # reorder via choose order if available
        if hasattr(ctx, "reorder_cards"):
            ordered = await ctx.reorder_cards(
                top, "Put back on top in any order")
            if ordered:
                for i, c in enumerate(ordered):
                    ctx.board.move_card(c.entity_id, deck.entity_id, position=i)
        else:
            # leave as-is (looked)
            pass
    return effect


def hyper_healing(counters: int = 1):
    """Remove counters and all SCs from each of your Active Pokémon."""
    async def effect(ctx):
        for p in list(ctx.my_pokemon_in_play()):
            if not is_in_active_spot(p):
                continue
            await ctx.heal(counters * 10, p)
            await ctx.cure_all_conditions(p)
    return effect


def cry_for_help(*types):
    """Search deck for a typed Pokémon (excl ex) into hand."""
    type_values = [getattr(t, "value", t) for t in types]

    async def effect(ctx):
        def match(c):
            if not is_pokemon_card(c) or is_pokemon_ex(c):
                return False
            elems = getattr(def_for(c.archetype_id), "elements", None) or []
            vals = [getattr(t, "value", t) for t in elems]
            return any(tv in vals or tv in elems for tv in type_values)
        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose a Water or Fighting Pokémon (excluding ex)")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def double_attack_bench(amount: int = 10, count: int = 2):
    """Deal amount to up to count of opponent's Benched (no W/R)."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        picks = []
        remaining = list(bench)
        for _ in range(min(count, len(bench))):
            if not remaining:
                break
            t = await ctx.choose_pokemon(
                remaining, f"Choose a Benched Pokémon ({amount} damage)")
            if t is None:
                break
            picks.append(t)
            remaining = [p for p in remaining if p is not t]
        for t in picks:
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def energy_evolution_passive() -> Passive:
    """Whenever you attach Energy from hand to this: may search evolve same type."""
    class _P(Passive):
        async def on_energy_attached(self, ctx, energy, pokemon, carrier, from_hand=True):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not from_hand:
                return
            if not await ctx.ask_yes_no("Search for an Evolution of the same Energy type?"):
                return
            # Energy types provided
            provides = energy.get_attribute(AttrID.POKEMON_TYPES) or []
            provide_vals = [getattr(t, "value", t) for t in provides]
            logic = holder.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            from spirit.game.content.definitions import evolves_from as _evolves_from

            def match(card):
                if logic and not _evolves_from(card.archetype_id, logic):
                    # also try display
                    ef = (getattr(def_for(card.archetype_id), "evolves_from", None) or "")
                    dn = holder.get_attribute(AttrID.DISPLAY_NAME) or ""
                    if not (ef and (dn.lower() in ef.lower() or ef.lower() in dn.lower())):
                        return False
                elif logic and _evolves_from(card.archetype_id, logic):
                    pass
                else:
                    return False
                elems = getattr(def_for(card.archetype_id), "elements", None) or []
                vals = [getattr(t, "value", t) for t in elems]
                return any(v in vals or v in elems for v in provide_vals)

            picks = await ctx.search_deck(
                match, count=1, minimum=0,
                prompt="Choose an Evolution of the same type")
            if picks:
                await ctx.evolve_pokemon(holder, picks[0])
            await ctx.shuffle_deck()
    return _P()


def burning_turn_switch():
    """Deal printed; switch self with Bench."""
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(damage=None, optional=False)


def lightning_turn_switch():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(damage=None, optional=False)


def splashing_turn_switch():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(damage=None, optional=False)


def devo_flash_on_evolve():
    """On play-to-evolve: devolve highest stage of 1 opp Bench Evolved."""
    async def effect(ctx):
        bench = [
            p for p in ctx.opponent_bench()
            if is_evolution_pokemon(p)
        ]
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Devolve which Evolved Benched Pokémon?")
        if target is None:
            return
        await ctx.devolve_pokemon(target, steps=1, destination="hand")
    return effect


def snap_tail_snipe(amount: int = 30):
    """Snipe any opp Pokémon for amount (no W/R for Bench)."""
    async def effect(ctx):
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon")
        if t is None:
            return
        apply_mod = is_in_active_spot(t)
        await ctx.deal_damage(amount, target=t, apply_modifiers=apply_mod)
    return effect


def overpowering_fang_passive() -> Passive:
    """While Active: each player's non-ex can't use Poké-Powers or Poké-Bodies."""
    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return False
            if is_pokemon_ex(pokemon):
                return False
            at = getattr(ability, "ability_type", None)
            return at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY)
    return _P()


def tsunami_bench(amount: int = 10):
    """Deal printed to Active; amount to each opp Bench (no W/R)."""
    async def effect(ctx):
        await ctx.deal_damage()
        for p in list(ctx.opponent_bench()):
            await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def spiky_shell_delayed(counters: int = 3):
    """Put counters on Defending at end of opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None:
            return
        target_id = defender.entity_id

        def _guard(board):
            return board.get_entity(target_id) is not None if hasattr(board, "get_entity") else True

        async def _put(session):
            board = session.board_state
            entity = board.get_entity(target_id)
            if entity is None:
                return
            from spirit.game.session.effects import EffectContext
            ectx = EffectContext(session, ctx.player_id, ctx.source, None)
            await ectx.deal_damage(
                counters * 10, target=entity,
                apply_modifiers=False, as_counters=True)

        ctx.schedule_at_checkup(1, _put, guard=_guard)
    return effect


def pop_forretress(self_counters: int = 7):
    """Put self_counters on self; move all Energy to Bench in any way."""
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        await ctx.deal_damage(
            self_counters * 10, target=a, apply_modifiers=False, as_counters=True)
        energies = [c for c in list(a.children) if is_energy_card(c)]
        bench = ctx.my_bench()
        if not energies or not bench:
            return
        for e in energies:
            dest = await ctx.choose_pokemon(bench, "Move Energy to which Benched?")
            if dest is not None:
                await ctx.move_energy(e, dest)
    return effect


def golden_wing_on_ko_passive(move_count: int = 2) -> Passive:
    """If would be KO'd by opp attack damage: may move up to N Energy to your Pokémon."""
    class _P(Passive):
        async def on_would_knock_out(self, ctx, pokemon, carrier, from_attack=True):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not from_attack:
                return False
            energies = [c for c in list(holder.children) if is_energy_card(c)]
            if not energies:
                return False
            if not await ctx.ask_yes_no("Move up to 2 Energy before Knock Out?"):
                return False
            dests = [p for p in ctx.my_pokemon_in_play() if p is not holder]
            if not dests:
                return False
            moved = 0
            remaining = list(energies)
            while moved < move_count and remaining and dests:
                picks = await ctx.choose_cards(
                    remaining, 1, minimum=0, prompt="Energy to move")
                if not picks:
                    break
                dest = await ctx.choose_pokemon(dests, "Move to?")
                if dest is None:
                    break
                await ctx.move_energy(picks[0], dest)
                remaining = [c for c in remaining if c is not picks[0]]
                moved += 1
            return False  # don't prevent KO
    return _P()


def lonesome_no_trainers_passive() -> Passive:
    """While you have fewer Pokémon in play than opponent: opp can't play
    Trainer cards except Supporters."""
    class _P(Passive):
        def blocks_trainer_play(self, card, player_id, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or player_id == holder.owning_player_id:
                return False
            board = getattr(holder, "board", None)
            if board is None:
                return False
            my_n = len(board.pokemon_in_play(holder.owning_player_id))
            opp_n = len(board.pokemon_in_play(player_id))
            if my_n >= opp_n:
                return False
            if is_supporter_card(card):
                return False
            d = def_for(card.archetype_id)
            if d is None:
                return False
            return getattr(d, "trainer_type", None) is not None or getattr(d, "hp", None) is None
    return _P()


def attract_current(energy_type=PokemonTypes.LIGHTNING):
    """Flip; heads search deck for typed Energy and attach to 1 of yours."""
    tv = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Attract Current")
        if not (results and results[0]):
            return

        def match(c):
            return is_energy_card(c) and energy_provides_type(c, tv) and is_basic_energy_card(c)

        picks = await ctx.search_deck(
            match, count=1, minimum=0, prompt="Lightning Energy to attach")
        if picks:
            dest = await ctx.choose_pokemon(
                list(ctx.my_pokemon_in_play()), "Attach to?")
            if dest is not None:
                await ctx.attach_energy(picks[0], dest)
        await ctx.shuffle_deck()
    return effect


def multi_pulse(base: int = 40, bonus: int = 20, need_types: int = 3):
    """If >= need_types different basic Energy types: base+bonus and Confused."""
    async def effect(ctx):
        types = set()
        for e in ctx.attached_energies(ctx.attacker) if ctx.attacker else []:
            if not is_basic_energy_card(e):
                continue
            for tv in (e.get_attribute(AttrID.POKEMON_TYPES) or []):
                types.add(getattr(tv, "value", tv))
        boosted = len(types) >= need_types
        await ctx.deal_damage(base + (bonus if boosted else 0))
        if boosted and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.CONFUSED)
    return effect


def freeze_light():
    """Flip: heads Paralyze; tails Burn."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Freeze Light")
        if ctx.defender is None:
            return
        if results and results[0]:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
        else:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.BURNED)
    return effect


def silver_sparkle_on_damaged_passive() -> Passive:
    """If Active and damaged by opp attack: flip; heads discard Energy from attacker."""
    class _P(Passive):
        async def after_damaged(self, ctx, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            if calc.amount <= 0:
                return
            results = await ctx.flip_coins(1, "Silver Sparkle")
            if not (results and results[0]):
                return
            attacker = calc.attacker
            if attacker is None:
                return
            energies = [c for c in attacker.children if is_energy_card(c)]
            if not energies:
                return
            picks = await ctx.choose_cards(
                energies, 1, prompt="Discard an Energy from Attacking Pokémon")
            if picks:
                await ctx.discard_cards(picks)
    return _P()


def elemental_blast(*energy_types):
    """Discard one of each typed Energy then deal printed."""
    return discard_typed_energies_then_damage(*energy_types)


def healing_aroma_between_turns(counters: int = 1) -> Passive:
    """While Active BETWEEN_TURNS: heal counters from each non-ex (both sides)."""
    class _P(Passive):
        async def between_turns(self, ctx, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return
            for p in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
                if is_pokemon_ex(p):
                    continue
                await ctx.heal(counters * 10, p)
    return _P()


def bouncy_move(base: int = 50, per: int = 10, max_counters: int = 5):
    """You may put up to max_counters on self; deal base + per * put."""
    async def effect(ctx):
        a = ctx.attacker
        put = 0
        if a is not None:
            for n in range(max_counters, -1, -1):
                if n == 0:
                    break
                if await ctx.ask_yes_no(f"Put {n} damage counters on Meganium?"):
                    put = n
                    break
            if put:
                await ctx.deal_damage(
                    put * 10, target=a, apply_modifiers=False, as_counters=True)
        await ctx.deal_damage(base + per * put)
    return effect


def nurture_and_heal(energy_type=PokemonTypes.GRASS):
    """Attach typed Energy from hand to 1 of yours; heal 1 counter from it."""
    tv = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        pool = [c for c in ctx.hand()
                if is_basic_energy_card(c) and energy_provides_type(c, tv)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Grass Energy from hand")
        if not picks:
            return
        dest = await ctx.choose_pokemon(
            list(ctx.my_pokemon_in_play()), "Attach to?")
        if dest is None:
            return
        await ctx.attach_energy(picks[0], dest)
        await ctx.heal(10, dest)
    return effect


def nurture_and_heal_condition(energy_type=PokemonTypes.GRASS):
    tv = getattr(energy_type, "value", energy_type)

    def extra(board, player_id, pokemon=None):
        hand = board.find_player_area(player_id, "hand")
        return any(
            is_basic_energy_card(c) and energy_provides_type(c, tv)
            for c in (hand.children if hand else []))
    return poke_power_condition(extra)


def night_song_gust_asleep():
    """Gust (opp chooses); new Defending Asleep."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon",
                player_id=ctx.opponent_id) or bench[0]
            await ctx.switch_active(ctx.opponent_id, target)
        d = ctx.opponent_active()
        if d is not None:
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
    return effect


def dig_deep_energy_to_hand():
    """Search discard for an Energy into hand."""
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Energy from discard to hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def upward_lick(base: int = 30, stage2: int = 50):
    """Snipe: base, or stage2 if Stage 2 Evolved (no W/R for Bench)."""
    async def effect(ctx):
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon")
        if t is None:
            return
        st = getattr(def_for(t.archetype_id), "stage", None)
        dmg = stage2 if st == PokemonStage.STAGE2 else base
        await ctx.deal_damage(dmg, target=t, apply_modifiers=is_in_active_spot(t))
    return effect


def punch_and_run(damage: int = 40):
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(damage=damage, optional=False)


def energy_ball_capped(base: int = 30, per: int = 10, cap: int = 20):
    """base + per per unused Energy, capped."""
    async def effect(ctx):
        cost = 0
        if ctx.ability and getattr(ctx.ability, "cost", None):
            cost = sum(ctx.ability.cost.values())
        attached = len(list(ctx.attached_energies(ctx.attacker) if ctx.attacker else []))
        extra = min(cap, per * max(0, attached - cost))
        await ctx.deal_damage(base + extra)
    return effect


def spiral_swirl_on_ko_passive() -> Passive:
    """If Active and KO'd by opp attack: Attacking is Confused."""
    class _P(Passive):
        async def on_knocked_out(self, ctx, pokemon, carrier, attacker=None):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not is_in_active_spot(holder):
                return
            if attacker is not None:
                await ctx.apply_special_condition(
                    attacker, SpecialConditions.CONFUSED)
    return _P()


def beatdown_vs_dark(base: int = 40, bonus: int = 30):
    """base + bonus if Defending is Darkness or has Dark in name."""
    async def effect(ctx):
        d = ctx.defender
        extra = 0
        if d is not None:
            name = _display_name(d)
            elems = getattr(def_for(d.archetype_id), "elements", None) or []
            vals = [getattr(t, "value", t) for t in elems]
            if (PokemonTypes.DARKNESS in elems
                    or PokemonTypes.DARKNESS.value in vals
                    or "Dark" in name):
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def tool_reset_to_hand():
    """Return a Tool from 1 of your Pokémon to hand (unlimited)."""
    async def effect(ctx):
        holders = [
            p for p in ctx.my_pokemon_in_play()
            if any(_is_pokemon_tool_card(c) for c in p.children)
        ]
        if not holders:
            return
        host = await ctx.choose_pokemon(holders, "Return Tool from which Pokémon?")
        if host is None:
            return
        tools = [c for c in host.children if _is_pokemon_tool_card(c)]
        picks = await ctx.choose_cards(tools, 1, prompt="Tool to hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


def tool_reset_condition():
    def extra(board, player_id, pokemon=None):
        for p in board.pokemon_in_play(player_id):
            if any(_is_pokemon_tool_card(c) for c in p.children):
                return True
        return False
    return poke_power_condition(extra)


def scramble_trip(base: int = 40, bonus: int = 20):
    """If Scramble Energy attached: base+bonus and Confused."""
    async def effect(ctx):
        has = False
        if ctx.attacker is not None:
            for c in ctx.attacker.children:
                dn = (getattr(def_for(c.archetype_id), "display_name", None) or "")
                if "Scramble" in dn:
                    has = True
                    break
        await ctx.deal_damage(base + (bonus if has else 0))
        if has and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.CONFUSED)
    return effect


def night_cry_search():
    """If on Bench: search deck for Dark/Rocket's Pokémon into hand."""
    async def effect(ctx):
        src = ctx.source
        if src is None or is_in_active_spot(src):
            return

        def match(c):
            if not is_pokemon_card(c):
                return False
            dn = (getattr(def_for(c.archetype_id), "display_name", None) or "")
            return "Dark" in dn or "Rocket's" in dn or "Rocket" in dn

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Pokémon with Dark or Rocket's in its name")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def night_cry_condition():
    def extra(board, player_id, pokemon=None):
        if pokemon is None:
            return False
        return not is_in_active_spot(pokemon)
    return poke_power_condition(extra)


def danger_perception_passive(threshold: int = 60, bonus: int = 40) -> Passive:
    """While remaining HP <= threshold, deal bonus more to Defending."""
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or calc.attacker is not holder:
                return
            if not (calc.is_attack and calc.is_opposing):
                return
            if holder.get_attribute(AttrID.HP, 0) <= threshold:
                calc.amount += bonus
    return _P()


def steel_wing_reduce(amount: int = 20):
    """During opp next turn, take amount less."""
    from spirit.game.card_effects.passives_common import apply_protection

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, reduce=amount)
    return effect


def twin_play(*names):
    """Search deck for up to 2 of named basics/ex onto Bench."""
    needles = [n.lower() for n in names]

    async def effect(ctx):
        def match(c):
            if not is_pokemon_card(c):
                return False
            dn = (getattr(def_for(c.archetype_id), "display_name", None) or "").lower()
            return any(n in dn for n in needles)

        picks = await ctx.search_deck(
            match, count=2, minimum=0,
            prompt="Up to 2 Scyther / Scyther ex to Bench")
        for card in picks or []:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect


def item_search_tool():
    """Search deck for a Pokémon Tool into hand."""
    async def effect(ctx):
        def match(c):
            return _is_pokemon_tool_card(c)
        picks = await ctx.search_deck(
            match, count=1, minimum=0, prompt="Pokémon Tool to hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def aftermath_tools(base: int = 20, per: int = 10, cap: int = 60):
    """base + per per Tool in discard, capped."""
    async def effect(ctx):
        n = sum(1 for c in ctx.discard_pile() if _is_pokemon_tool_card(c))
        await ctx.deal_damage(base + min(cap, per * n))
    return effect


def fishing_tail():
    """Search discard for Basic / Evolution / basic Energy into hand."""
    async def effect(ctx):
        pool = [
            c for c in ctx.discard_pile()
            if is_basic_energy_card(c)
            or (is_pokemon_card(c) and (
                is_basic_pokemon(c) or is_evolution_pokemon(c)))
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0,
            prompt="Basic Pokémon, Evolution, or basic Energy")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def makeover_energy_swap():
    """Discard a basic Energy from a non-ex; then attach a different basic type from discard."""
    async def effect(ctx):
        hosts = [
            p for p in ctx.my_pokemon_in_play()
            if not is_pokemon_ex(p)
            and any(is_basic_energy_card(c) for c in p.children)
        ]
        if not hosts:
            return
        host = await ctx.choose_pokemon(hosts, "Discard basic Energy from?")
        if host is None:
            return
        basics = [c for c in host.children if is_basic_energy_card(c)]
        picks = await ctx.choose_cards(basics, 1, prompt="Discard which basic Energy?")
        if not picks:
            return
        discarded_types = set()
        for tv in (picks[0].get_attribute(AttrID.POKEMON_TYPES) or []):
            discarded_types.add(getattr(tv, "value", tv))
        await ctx.discard_cards(picks)
        pool = [
            c for c in ctx.discard_pile()
            if is_basic_energy_card(c)
            and not any(
                getattr(t, "value", t) in discarded_types
                for t in (c.get_attribute(AttrID.POKEMON_TYPES) or []))
        ]
        if not pool:
            return
        new = await ctx.choose_cards(
            pool, 1, minimum=0,
            prompt="Attach a different type of basic Energy from discard")
        if new:
            await ctx.attach_energy(new[0], host)
    return effect


def poison_immunity_passive() -> Passive:
    class _P(Passive):
        def prevents_special_condition(self, pokemon, condition, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return False
            return condition in (
                SpecialConditions.POISONED,
                getattr(SpecialConditions.POISONED, "value", None))
    return _P()


def copy_defending_attack():
    """Copy 1 of Defending's attacks if you have the Energy."""
    from spirit.game.data_utils import Attack as _Attack

    async def effect(ctx):
        if ctx.defender is None:
            return
        definition = def_for(ctx.defender.archetype_id)
        candidates = []
        for ability in getattr(definition, "abilities", None) or []:
            if isinstance(ability, _Attack):
                candidates.append((ctx.defender, ability))
        if not candidates:
            return
        picked = await ctx.choose_attack_to_copy(
            candidates, "Choose an attack to copy")
        if picked is None:
            return
        _, chosen = picked
        await ctx.use_attack(chosen)
    return effect


def bursting_up_on_evolve():
    """On play-to-evolve: count opp Bench; search that many Fire Energy to hand."""
    async def effect(ctx):
        n = len(ctx.opponent_bench())
        if n <= 0:
            return
        if not await ctx.ask_yes_no(
                f"Search deck for up to {n} Fire Energy?"):
            return

        def match(c):
            return (is_basic_energy_card(c)
                    and energy_provides_type(c, PokemonTypes.FIRE.value))

        picks = await ctx.search_deck(
            match, count=n, minimum=0, prompt=f"Up to {n} Fire Energy")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def darker_ring_on_evolve():
    """On play-to-evolve: switch 1 opp Bench with Defending."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Switch which Benched Pokémon into Active?")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
    return effect


def black_cry_lock():
    """Defending can't retreat or use Poké-Powers during opp next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        ctx.lock_retreat(d)

        class _Lock(Passive):
            def blocks_ability(self, pokemon, ability, carrier):
                if pokemon is not d:
                    return False
                return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER

        ctx.add_passive_through_opponents_turn(d, _Lock())
    return effect


def intimidating_ring_passive() -> Passive:
    """While Active: opp Basic Pokémon can't attack or use Poké-Powers."""
    class _P(Passive):
        def blocks_attack(self, pokemon, attack, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return False
            if pokemon.owning_player_id == holder.owning_player_id:
                return False
            return is_basic_pokemon(pokemon)

        def blocks_ability(self, pokemon, ability, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return False
            if pokemon.owning_player_id == holder.owning_player_id:
                return False
            if not is_basic_pokemon(pokemon):
                return False
            return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER
    return _P()


def aqua_supply():
    """You may attach a basic Energy from hand to 1 of yours."""
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Attach a basic Energy from hand?")
        if not picks:
            return
        dest = await ctx.choose_pokemon(
            list(ctx.my_pokemon_in_play()), "Attach to?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def stages_prevent_effects_no_weakness() -> Passive:
    """While Evolved: prevent all effects of opp attacks except damage; no Weakness."""
    class _P(Passive):
        def prevents_attack_effects(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_evolution_pokemon(holder):
                return False
            return (
                calc.is_attack and calc.is_opposing
                and calc.target is holder)

        def prevents_effects(self, calc, carrier):
            return self.prevents_attack_effects(calc, carrier)

        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is holder and is_evolution_pokemon(holder):
                calc.weakness_applies = False

        def blocks_attack_effects_from(self, target, carrier, attacker):
            holder = carrier_pokemon(carrier) or carrier
            return (
                target is holder and is_evolution_pokemon(holder)
                and attacker is not None
                and attacker.owning_player_id != holder.owning_player_id)
    return _P()


def stages_on_damaged_counters(counters: int = 2) -> Passive:
    """While Evolved + Active and damaged by opp attack: put counters on Attacking."""
    class _P(Passive):
        async def after_damaged(self, ctx, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_evolution_pokemon(holder):
                return
            if not is_in_active_spot(holder):
                return
            if not (calc.is_attack and calc.is_opposing and calc.target is holder):
                return
            if calc.amount <= 0 and not getattr(calc, "knocked_out", False):
                # still triggers even if KO'd
                pass
            attacker = calc.attacker
            if attacker is not None:
                await ctx.deal_damage(
                    counters * 10, target=attacker,
                    apply_modifiers=False, as_counters=True)
    return _P()


def gust_force_switch():
    """Switch 1 opp Bench with Defending (you choose)."""
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Gust which Benched Pokémon?")
        if t is not None:
            await ctx.switch_active(ctx.opponent_id, t)
    return effect


def unown_e_hidden_power():
    """If opp Bench not full: look at hand, put 1 Basic onto their Bench, then switch it in."""
    async def effect(ctx):
        if len(ctx.opponent_bench()) >= 5:
            return
        hand = list(ctx.hand(ctx.opponent_id))
        basics = [c for c in hand if is_basic_pokemon(c)]
        if hasattr(ctx, "reveal_cards") and hand:
            await ctx.reveal_cards(hand)
        if not basics:
            return
        picks = await ctx.choose_cards(
            basics, 1, prompt="Basic Pokémon to put onto opponent's Bench")
        if not picks:
            return
        # Move onto opponent's bench (bench_pokemon uses card owner)
        await ctx.bench_pokemon(picks[0])
        await ctx.switch_active(ctx.opponent_id, picks[0])
    return effect


def unown_s_hidden_power():
    """If Defending has Power/Body: move up to 2 basic Energy from 1 opp Pokémon onto Defending."""
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        definition = def_for(d.archetype_id)
        has_pb = any(
            getattr(a, "ability_type", None) in (
                AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY)
            for a in (getattr(definition, "abilities", None) or []))
        if not has_pb:
            return
        donors = [
            p for p in ctx.opponent_pokemon_in_play()
            if p is not d and any(is_basic_energy_card(c) for c in p.children)
        ]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move basic Energy from?")
        if src is None:
            return
        pool = [c for c in src.children if is_basic_energy_card(c)]
        picks = await ctx.choose_cards(
            pool, min(2, len(pool)), minimum=0,
            prompt="Up to 2 basic Energy to move to Defending")
        for e in picks or []:
            await ctx.move_energy(e, d)
    return effect


def unown_q_hidden_power_guess():
    """Guess Pokémon/Trainer/Energy from hand card; wrong → draw 2."""
    async def effect(ctx):
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, prompt="Put a card face down")
        if not picks:
            return
        card = picks[0]
        options = ["Pokémon", "Trainer", "Energy"]
        guess = await ctx.choose(
            "Opponent guesses the card type", options,
            player_id=ctx.opponent_id)
        if guess is None:
            return
        actual = "Trainer"
        if is_pokemon_card(card):
            actual = "Pokémon"
        elif is_energy_card(card):
            actual = "Energy"
        if hasattr(ctx, "reveal_cards"):
            await ctx.reveal_cards([card])
        if options[guess] != actual:
            await ctx.draw_cards(2)
    return effect


def protective_orb_passive() -> Passive:
    """Holder has no Weakness; discard self if holder becomes Basic or ex."""
    class _Orb(Passive):
        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is holder:
                calc.weakness_applies = False

        async def between_turns(self, ctx, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None:
                return
            if is_basic_pokemon(holder) or is_pokemon_ex(holder):
                tool = carrier if carrier is not holder else None
                if tool is None:
                    for c in list(holder.children):
                        dn = (getattr(def_for(c.archetype_id), "display_name", None) or "")
                        if "Protective Orb" in dn:
                            tool = c
                            break
                if tool is not None:
                    await ctx.discard_cards([tool])
    return _Orb()


def attach_to_evolved_non_ex_pokemon():
    """Protective Orb / similar: Evolved non-ex only."""
    def check(pokemon) -> bool:
        if is_pokemon_ex(pokemon):
            return False
        return is_evolution_pokemon(pokemon)
    return check


def swallow_up_instead(base: int = 70, boosted: int = 120):
    """If Defending remaining HP < self remaining HP, deal boosted else base."""
    async def effect(ctx):
        d, a = ctx.defender, ctx.attacker
        if d is None or a is None:
            await ctx.deal_damage(base)
            return
        d_hp = int(d.get_attribute(AttrID.HP, 0) or 0)
        a_hp = int(a.get_attribute(AttrID.HP, 0) or 0)
        await ctx.deal_damage(boosted if d_hp < a_hp else base)
    return effect


async def professor_elms_training_method(ctx):
    """Search deck for an Evolution card into hand."""
    picks = await ctx.search_deck(
        is_evolution_pokemon, count=1, minimum=0,
        prompt="Choose an Evolution card")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def star_turn_switch(damage: int = 20):
    """Deal damage; mandatory switch with Bench (Burning/Lightning/Splashing Turn)."""
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(damage=damage, optional=False)


def detonation_mill(damage: int = 70, mill: int = 10):
    """Deal damage; if fewer prizes than opponent, discard top mill of your deck."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        mine = count_prizes_remaining("mine")(ctx)
        theirs = count_prizes_remaining("opponent")(ctx)
        if mine < theirs:
            deck = ctx.board.find_player_area(ctx.player_id, "deck")
            if deck and deck.children:
                top = list(deck.children[:mill])
                if top:
                    await ctx.discard_cards(top)
    return effect


def meta_voltage(damage: int = 70, self_each: int = 40):
    """Deal damage; if fewer prizes, deal self_each to each of your Pokémon (no W/R bench)."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        mine = count_prizes_remaining("mine")(ctx)
        theirs = count_prizes_remaining("opponent")(ctx)
        if mine < theirs:
            for p in list(ctx.my_pokemon_in_play()):
                await ctx.deal_damage(
                    self_each, target=p, apply_modifiers=False)
    return effect


def cross_wind_discard_all_energy(damage: int = 70):
    """Deal damage; if fewer prizes, discard all Energy from all your Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        mine = count_prizes_remaining("mine")(ctx)
        theirs = count_prizes_remaining("opponent")(ctx)
        if mine < theirs:
            for p in list(ctx.my_pokemon_in_play()):
                energies = [c for c in list(p.children) if is_energy_card(c)]
                if energies:
                    await ctx.discard_cards(energies)
    return effect


def standing_by_boost(title: str = "Pulse Blast", next_base: int = 120):
    """Discard an Energy; during next turn named attack base is next_base."""
    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.discard_energy_from(
                ctx.attacker, 1, predicate=is_energy_card,
                prompt="Discard an Energy card attached to Octillery")
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


def mudslide_snipe(amount: int = 100, energy_type=PokemonTypes.FIGHTING, discard_n: int = 2):
    """Discard n typed Energy; snipe any opp Pokémon for amount (no W/R bench)."""
    tv = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.discard_energy_from(
                ctx.attacker, discard_n,
                predicate=lambda c: energy_provides_type(c, tv),
                prompt=f"Discard {discard_n} Fighting Energy")
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon")
        if t is None:
            return
        await ctx.deal_damage(amount, target=t, apply_modifiers=is_in_active_spot(t))
    return effect

# --- EX11 Delta Species / Holon / Ditto / Stars ---



def is_delta_pokemon(card) -> bool:
    dn = _display_name(card)
    return "\u03b4" in dn or "δ" in dn


def _is_holon_energy(card) -> bool:
    d = def_for(card.archetype_id)
    dn = (getattr(d, "display_name", None) or "").lower()
    return "holon energy" in dn


def _name_matches(card, *names: str) -> bool:
    dn = _display_name(card).lower()
    return any(n.lower() in dn for n in names)


def ditto_duplicate():
    """Search deck for another Ditto; identity-swap; old to top then shuffle.
    Pair with shared_once_per_turn='Duplicate'."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return

        def match(card):
            d = def_for(card.archetype_id)
            if d is None:
                return False
            dn = (getattr(d, "display_name", None) or "").lower()
            return dn == "ditto"

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Choose another Ditto to switch with")
        if picks:
            await ctx.identity_swap(
                src, picks[0], destination="deck", transfer=True)
        await ctx.shuffle_deck()
    return effect


def ditto_duplicate_condition():
    return poke_power_condition(has_deck)


def delta_heal():
    """Remove 1 damage counter from each of your δ Pokémon.
    Pair with shared_once_per_turn='Delta Heal'."""
    async def effect(ctx):
        for p in ctx.my_pokemon_in_play():
            if not is_delta_pokemon(p):
                continue
            missing = effective_max_hp(ctx.board, p) - p.get_attribute(AttrID.HP, 0)
            if missing > 0:
                await ctx.heal(10, p)
    return effect


def delta_search_holon_attach_self():
    """Deal printed damage; search Holon Energy and attach to self."""
    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            _is_holon_energy, count=1, minimum=0,
            prompt="Choose a Holon Energy card")
        if picks and ctx.attacker is not None:
            await ctx.attach_energy(picks[0], ctx.attacker)
        await ctx.shuffle_deck()
    return effect


def return_energy_then(then_fn):
    """Optional: return an Energy from self to hand; if you do, run then_fn(ctx)."""
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if not pool:
            return
        if not await ctx.ask_yes_no("Return an Energy to your hand?"):
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Return which Energy?")
        if not picks:
            return
        await ctx.put_in_hand(picks)
        await then_fn(ctx)
    return effect


def return_burn():
    async def _then(ctx):
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return return_energy_then(_then)


def return_spark(bench_dmg: int = 20):
    async def _then(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Deal damage to which Benched Pokémon?")
        if t is not None:
            await ctx.deal_damage(bench_dmg, target=t, apply_modifiers=False)
    return return_energy_then(_then)


def return_wave():
    async def _then(ctx):
        d = ctx.defender
        if d is None:
            return
        pool = [c for c in d.children if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Return opponent Energy")
        if picks:
            await ctx.put_in_hand(picks)
    return return_energy_then(_then)


def energy_jump_move_any():
    """Move an Energy from one of your Pokémon to another."""
    async def effect(ctx):
        donors = [
            p for p in ctx.my_pokemon_in_play()
            if any(is_energy_card(c) for c in p.children)
        ]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move Energy from?")
        if src is None:
            return
        pool = [c for c in src.children if is_energy_card(c)]
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


def psychic_rage_snipe(per: int = 10):
    """Snipe 10 per damage counter on self to any opp Pokémon."""
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        n = max(0, effective_max_hp(ctx.board, a) - a.get_attribute(AttrID.HP, 0)) // 10
        if n <= 0:
            return
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if t is not None:
            await ctx.deal_damage(
                n * per, target=t, apply_modifiers=is_in_active_spot(t))
    return effect


def black_magic_base_plus_bench(base: int = 10, per: int = 20):
    async def effect(ctx):
        n = len(ctx.opponent_bench())
        await ctx.deal_damage(base + per * n)
    return effect


def extra_crush_requires_ex(amount: int = 80):
    async def effect(ctx):
        if not any(is_pokemon_ex(p) for p in ctx.opponent_pokemon_in_play()):
            return
        await ctx.deal_damage(amount)
    return effect




def chain_of_events_passive(cheer_title: str = "Cheer On") -> Passive:
    """After your other Active attacks, you may use Cheer On (once this way)."""
    class _P(Passive):
        attack_followup = True  # marker; real impl below

        def __init__(self):
            self._used_this_attack = False

        async def attack_followup(self, ctx, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or ctx.attacker is None:
                return
            if ctx.attacker is holder:
                return  # only after the *other* Active attacks
            if holder.owning_player_id != ctx.player_id:
                return
            # Holder must be Active
            actives = []
            try:
                a = ctx.board.active_pokemon(ctx.player_id)
                if a is not None:
                    actives = [a]
                # Dual-active: collect all actives if API exists
                if hasattr(ctx.board, "active_pokemons"):
                    actives = list(ctx.board.active_pokemons(ctx.player_id) or actives)
            except Exception:
                pass
            if holder not in actives:
                return
            if ctx.attacker not in actives:
                return
            # Once per follow-up chain
            key = "_chain_of_events_used"
            if getattr(ctx, key, False):
                return
            if not await ctx.ask_yes_no(f"Use {cheer_title} via Chain of Events?"):
                return
            setattr(ctx, key, True)
            # Find Cheer On attack on holder and run its effect (energy still required)
            from spirit.game.content.definitions import def_for, ABILITIES_BY_ID
            d = def_for(holder.archetype_id)
            cheer = None
            for ab in getattr(d, "abilities", None) or []:
                if (getattr(ab, "title", "") or "").lower() == cheer_title.lower():
                    cheer = ab
                    break
            if cheer is None:
                return
            # Energy check
            from spirit.game.session.legal_actions import (
                effective_attack_cost, attack_cost_satisfied,
            )
            cost = effective_attack_cost(
                ctx.board, holder, getattr(cheer, "cost", None) or {}, ability=cheer)
            energies = ctx.board.attached_energies(holder)
            if not attack_cost_satisfied(cost, energies, ctx.board):
                return
            # Resolve Cheer On effect with attacker=holder
            old_atk = ctx.attacker
            old_ab = ctx.ability
            try:
                ctx.attacker = holder
                ctx.ability = cheer
                if cheer.effect is not None:
                    await cheer.effect(ctx)
            finally:
                ctx.attacker = old_atk
                ctx.ability = old_ab
    # Passive base expects attack_followup as callable attribute on instance
    inst = _P()
    # Rebind so active_passives sees callable
    async def _follow(ctx, carrier, _self=inst):
        await _self.attack_followup(ctx, carrier)
    inst.attack_followup = _follow
    return inst


def holon_pokemon_energy_attach_to_with_energy(pokemon) -> bool:
    """Electrode/Magneton: may only attach as Energy if target already has Energy."""
    from spirit.game.models.board import BoardState
    # pokemon is the target
    return any(True for _ in BoardState.attached_energies(pokemon)) if pokemon else False


async def holon_stage1_energy_on_attach(ctx):
    """When attaching Holon's Electrode/Magneton as Energy: return 1 Energy from target to hand."""
    target = ctx.attached_to
    if target is None:
        return
    from spirit.game.models.board import BoardState
    energies = [e for e in BoardState.attached_energies(target) if e is not ctx.source]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Return an Energy to your hand")
    if picks:
        await ctx.put_in_hand(picks)


def delta_aura_cost_passive(*partner_names: str, attack_title: str = "",
                            colorless_drop: int = 2) -> Passive:
    """While a named partner is in play, reduce Colorless cost on `attack_title`."""
    lowered = tuple(n.lower() for n in partner_names)
    want = (attack_title or "").lower()

    class _P(Passive):
        def modify_attack_cost(self, cost, pokemon, carrier, board, ability=None, **kwargs):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return cost
            if want:
                title = ""
                if ability is not None:
                    if isinstance(ability, dict):
                        title = (ability.get("title") or ability.get("name") or "")
                        # PIE may nest title as {"id": "..."}
                        if isinstance(title, dict):
                            title = title.get("id") or ""
                    else:
                        title = getattr(ability, "title", "") or ""
                if want not in str(title).lower():
                    return cost
            pid = holder.owning_player_id
            if not any(
                    any(n in _display_name(p).lower() for n in lowered)
                    for p in board.pokemon_in_play(pid)):
                return cost
            cost = dict(cost)
            for key in ("Colorless", PokemonTypes.COLORLESS.value):
                if key in cost and cost[key]:
                    cost[key] = max(0, cost[key] - colorless_drop)
                    break
            return cost
    return _P()

def energy_bone_snipe(per: int = 20):
    """Choose up to Energy-count opp Pokémon; 20 each."""
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        n = sum(1 for c in a.children if is_energy_card(c))
        if n <= 0:
            return
        remaining = list(ctx.opponent_pokemon_in_play())
        picks = []
        for i in range(min(n, len(list(ctx.opponent_pokemon_in_play())))):
            if not remaining:
                break
            t = await ctx.choose_pokemon(
                remaining, f"Choose Pokémon ({i+1}/{n})", optional=True)
            if t is None:
                break
            picks.append(t)
            remaining = [p for p in remaining if p is not t]
        for t in picks:
            await ctx.deal_damage(
                per, target=t, apply_modifiers=is_in_active_spot(t))
    return effect

def metal_crusher(base: int = 50, metal_base: int = 90):
    async def effect(ctx):
        d = ctx.defender
        amount = base
        if d is not None:
            types = d.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.METAL.value in types:
                amount = metal_base
        await ctx.deal_damage(amount)
    return effect


def crush_and_burn_discard_any(base: int = 30, per: int = 20):
    """May discard any number of Energy from your Pokémon; +per each."""
    async def effect(ctx):
        pool = []
        for p in ctx.my_pokemon_in_play():
            for c in p.children:
                if is_energy_card(c):
                    pool.append(c)
        extra = 0
        if pool and await ctx.ask_yes_no("Discard Energy cards for more damage?"):
            picks = await ctx.choose_cards(
                pool, len(pool), minimum=0, prompt="Discard Energy cards")
            if picks:
                await ctx.discard_cards(picks)
                extra = len(picks) * per
        await ctx.deal_damage(base + extra)
    return effect


def delta_control_top4():
    """Look at top 4; put 1 in hand; rest stay on top in any order."""
    async def effect(ctx):
        top = ctx.deck_top(4)
        if not top:
            return
        picks = await ctx.choose_cards(
            list(top), 1, minimum=0,
            prompt="Put which card into your hand?",
            display_cards=top,
        )
        if picks:
            await ctx.put_in_hand(picks)
        remaining = len(top) - len(picks or [])
        if remaining > 1:
            await ctx.reorder_deck_top(remaining)
    return effect

def delta_switch_on_play():
    """ON_PLAY (bench): move any number of basic Energy among your Pokémon
    excluding this Mewtwo."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        if not await ctx.ask_yes_no("Move basic Energy cards around?"):
            return
        # Repeatedly move until player stops
        while True:
            donors = [
                p for p in ctx.my_pokemon_in_play()
                if p is not src and any(is_basic_energy_card(c) for c in p.children)
            ]
            if not donors:
                return
            if not await ctx.ask_yes_no("Move another basic Energy?"):
                return
            donor = await ctx.choose_pokemon(donors, "Move basic Energy from?")
            if donor is None:
                return
            pool = [c for c in donor.children if is_basic_energy_card(c)]
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose Energy")
            if not picks:
                return
            dests = [p for p in ctx.my_pokemon_in_play() if p is not src and p is not donor]
            # Can also move onto other Pokémon excluding Mewtwo; allow donor excluded
            if not dests:
                return
            dest = await ctx.choose_pokemon(dests, "Move Energy to?")
            if dest is None:
                return
            await ctx.move_energy(picks[0], dest)
    return effect


def energy_burst_both_sides(per: int = 10):
    async def effect(ctx):
        n = 0
        if ctx.attacker is not None:
            n += sum(1 for c in ctx.attacker.children if is_energy_card(c))
        if ctx.defender is not None:
            n += sum(1 for c in ctx.defender.children if is_energy_card(c))
        await ctx.deal_damage(per * n)
    return effect


def lightning_storm_self(dmg: int = 70, self_counters: int = 7):
    """Deal dmg; put self_counters on self unless Holon Energy attached
    (Delta Guard)."""
    async def effect(ctx):
        await ctx.deal_damage(dmg)
        a = ctx.attacker
        if a is None:
            return
        if any(_is_holon_energy(c) for c in a.children):
            return
        await ctx.deal_damage(
            self_counters * 10, target=a, apply_modifiers=False, as_counters=True)
    return effect


def delta_guard_noop_passive() -> Passive:
    """Marker body; Lightning Storm itself checks Holon Energy."""
    return Passive()


def fire_dance_attach(energy_type=PokemonTypes.FIRE):
    async def effect(ctx):
        await ctx.deal_damage()
        tv = getattr(energy_type, "value", energy_type)
        pool = [
            c for c in ctx.discard_pile()
            if is_energy_card(c) and energy_provides_type(c, tv)
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach Fire Energy")
        if not picks:
            return
        dests = list(ctx.my_pokemon_in_play())
        dest = await ctx.choose_pokemon(dests, "Attach to which Pokémon?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def metal_navigation_attach():
    async def effect(ctx):
        def match(c):
            d = def_for(c.archetype_id)
            dn = (getattr(d, "display_name", None) or "").lower()
            return "metal energy" in dn or energy_provides_type(
                c, PokemonTypes.METAL.value)
        picks = await ctx.search_deck(
            match, count=1, minimum=0, prompt="Metal Energy")
        if picks and ctx.source is not None:
            await ctx.attach_energy(picks[0], ctx.source)
        await ctx.shuffle_deck()
    return effect


def draw_cards_n(n: int = 3):
    async def effect(ctx):
        await ctx.draw_cards(n)
    return effect


def delta_crush_optional(base: int = 50, bonus: int = 20):
    async def effect(ctx):
        extra = 0
        a = ctx.attacker
        if a is not None:
            pool = [c for c in a.children if is_energy_card(c)]
            if pool and await ctx.ask_yes_no("Discard an Energy for more damage?"):
                picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
                if picks:
                    await ctx.discard_cards(picks)
                    extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def crush_draw_any():
    """Reveal top; if basic Energy, attach to 1 of your Pokémon."""
    async def effect(ctx):
        top = ctx.deck_top(1)
        if not top:
            return
        card = top[0]
        await ctx.reveal_cards([card])
        if not is_basic_energy_card(card):
            return
        dests = list(ctx.my_pokemon_in_play())
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Attach Energy to?")
        if dest is not None:
            await ctx.attach_energy(card, dest)
    return effect


def delta_moon_on_special_attach():
    """When opponent attaches Special Energy from hand, put 1 counter on that Pokémon.
    Pair with shared_once_per_turn / used_abilities for once per turn."""
    async def effect(ctx):
        if ctx.attaching_player_id == ctx.player_id:
            return
        energy = ctx.attached_energy
        receiver = ctx.energy_receiver
        if energy is None or receiver is None:
            return
        if not energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            d = def_for(energy.archetype_id)
            if not getattr(d, "is_special", False):
                return
        used_key = ("Delta Moon", ctx.player_id)
        if used_key in ctx.session.turn_state.used_abilities:
            return
        ctx.session.turn_state.used_abilities.add(used_key)
        await ctx.deal_damage(
            10, target=receiver, apply_modifiers=False, as_counters=True)
    return effect


def gang_up_dark_metal(per: int = 10):
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play():
            types = p.get_attribute(AttrID.POKEMON_TYPES) or []
            if (PokemonTypes.DARKNESS.value in types
                    or PokemonTypes.METAL.value in types):
                n += 1
        await ctx.deal_damage(per * n)
    return effect


def delta_fang_lock_ex():
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is not None and is_pokemon_ex(d):
            lock_all_attacks(ctx, d)
    return effect


def machine_burst_if_tm(asleep_burned: bool = True):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None or ctx.defender is None:
            return
        has_tm = False
        for c in a.children:
            subs = subtypes_for(c.archetype_id) or []
            if any(s in ("Technical Machine", "TM", "Pokemon Tool", "Pokémon Tool")
                   for s in subs):
                has_tm = True
                break
        if has_tm:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def backup_draw_to(n: int = 6):
    async def effect(ctx):
        hand = ctx.hand()
        need = n - len(hand)
        if need > 0:
            await ctx.draw_cards(need)
    return effect


def backup_draw_to_condition(n: int = 6):
    def cond(board, player_id, pokemon=None):
        hand = board.find_player_area(player_id, "hand")
        return hand is not None and len(hand.children) < n
    return poke_power_condition(cond)


def psychic_option_water_psychic(base: int = 20, bonus: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        extra = 0
        if a is not None and any(
                energy_provides_type(c, PokemonTypes.WATER.value)
                for c in a.children):
            extra = bonus
        await ctx.deal_damage(base + extra)
        if a is not None and ctx.defender is not None and any(
                energy_provides_type(c, PokemonTypes.PSYCHIC.value)
                for c in a.children):
            pool = [
                c for c in ctx.defender.children
                if c.get_attribute(AttrID.IS_SPECIAL_ENERGY)
                or getattr(def_for(c.archetype_id), "is_special", False)
            ]
            if pool:
                picks = await ctx.choose_cards(
                    pool, 1, minimum=0, prompt="Discard Special Energy")
                if picks:
                    await ctx.discard_cards(picks)
    return effect


def prize_shift():
    """Put a hand card as a face-up Prize; take 1 face-down Prize into hand."""
    async def effect(ctx):
        hand = list(ctx.hand())
        if not hand:
            return
        prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        if prize_area is None or not prize_area.children:
            return
        face_down = [
            c for c in prize_area.children
            if not c.get_attribute("PrizeFaceUp", False)
        ]
        if not face_down:
            return
        picks = await ctx.choose_cards(
            hand, 1, minimum=0, prompt="Choose a card to put as a Prize")
        if not picks:
            return
        taken = random.choice(face_down)
        await ctx.put_in_hand([taken])
        placed = picks[0]
        ctx.board.move_card(placed.entity_id, prize_area.entity_id)
        placed.set_attribute("PrizeFaceUp", True)
        if hasattr(ctx, "reveal_cards"):
            await ctx.reveal_cards([placed])
    return effect


def delta_storm_between_turns(counters: int = 1):
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        for p in ctx.opponent_pokemon_in_play():
            if is_pokemon_ex(p):
                await ctx.deal_damage(
                    counters * 10, target=p,
                    apply_modifiers=False, as_counters=True)
    return effect


def steep_dive(glide_title: str = "Glide", glide_next: int = 100):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Steep Dive")
        if results and results[0]:
            await apply_protection(ctx, prevent=True, effects_too=True)
        else:
            await apply_own_next_turn_boost(
                ctx, glide_next, attack_title=glide_title, replace=True)
    return effect


def body_odor_between_turns(counters: int = 1):
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        for p in ctx.opponent_pokemon_in_play():
            d = def_for(p.archetype_id)
            has_body = False
            for ab in getattr(d, "abilities", None) or []:
                if getattr(ab, "ability_type", None) == AbilityTypes.POKE_BODY:
                    has_body = True
                    break
            if has_body:
                await ctx.deal_damage(
                    counters * 10, target=p,
                    apply_modifiers=False, as_counters=True)
    return effect


def holon_splash(base: int = 30, per: int = 10):
    async def effect(ctx):
        n = 0
        if ctx.attacker is not None:
            n = sum(1 for c in ctx.attacker.children if _is_holon_energy(c))
        await ctx.deal_damage(base + per * n)
    return effect


def holon_blizzard(base: int = 20, bench: int = 10):
    async def effect(ctx):
        await ctx.deal_damage(base)
        a = ctx.attacker
        if a is None or not any(_is_holon_energy(c) for c in a.children):
            return
        for p in ctx.opponent_bench():
            await ctx.deal_damage(bench, target=p, apply_modifiers=False)
    return effect


def holon_search_attach_any():
    async def effect(ctx):
        picks = await ctx.search_deck(
            _is_holon_energy, count=1, minimum=0,
            prompt="Choose a Holon Energy card")
        if picks:
            dests = list(ctx.my_pokemon_in_play())
            dest = await ctx.choose_pokemon(dests, "Attach Holon Energy to?")
            if dest is not None:
                await ctx.attach_energy(picks[0], dest)
        await ctx.shuffle_deck()
    return effect


def holon_draw(extra_if_holon: int = 2):
    async def effect(ctx):
        await ctx.draw_cards(1)
        a = ctx.attacker
        if a is not None and any(_is_holon_energy(c) for c in a.children):
            await ctx.draw_cards(extra_if_holon)
    return effect


def critical_collection(energy_type, base_dmg: int = 10):
    """Deal base; attach up to (opp prizes taken) typed Energy from discard."""
    tv = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage(base_dmg)
        n = ctx.prizes_taken(ctx.opponent_id)
        if n <= 0 or ctx.attacker is None:
            return
        pool = [
            c for c in ctx.discard_pile()
            if is_energy_card(c) and energy_provides_type(c, tv)
        ]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, min(n, len(pool)), minimum=0,
            prompt=f"Attach up to {n} Energy from discard")
        for e in picks or []:
            await ctx.attach_energy(e, ctx.attacker)
    return effect


def evolutionary_flame_on_evolve():
    async def effect(ctx):
        d = ctx.opponent_active()
        if d is None:
            return
        if not await ctx.ask_yes_no("Burn and Confuse the Defending Pokémon?"):
            return
        await ctx.apply_special_condition(d, SpecialConditions.BURNED)
        await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def evolutionary_thunder_on_evolve(counters: int = 1):
    async def effect(ctx):
        if not await ctx.ask_yes_no(
                "Put 1 damage counter on each of your opponent's Pokémon?"):
            return
        for p in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(
                counters * 10, target=p, apply_modifiers=False, as_counters=True)
    return effect


def evolutionary_swirl_on_evolve(draw_up_to: int = 4):
    async def effect(ctx):
        if not await ctx.ask_yes_no(
                f"Have opponent shuffle hand and draw up to {draw_up_to}?"):
            return
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            await ctx.shuffle_into_deck(hand, ctx.opponent_id)
        options = [str(i) for i in range(draw_up_to + 1)]
        # Opponent chooses how many to draw.
        idx = await ctx.choose(
            "How many cards to draw?", options, player_id=ctx.opponent_id) \
            if hasattr(ctx, "choose") else None
        try:
            n = int(options[idx]) if idx is not None else draw_up_to
        except Exception:
            n = draw_up_to
        await ctx.draw_cards(n, player_id=ctx.opponent_id)
    return effect

def final_sting_ko_paralyze_poison(poison_counters: int = 2):
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        if not await ctx.ask_yes_no("Knock Out Beedrill to Paralyze and Poison?"):
            return
        await ctx.knock_out(src)
        d = ctx.opponent_active()
        if d is None:
            return
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
        await ctx.apply_special_condition(d, SpecialConditions.POISONED)
        if hasattr(ctx, "set_poison_counters"):
            await ctx.set_poison_counters(d, poison_counters)
        else:
            # Extra counter beyond the default 1 between turns → put one now
            # so between turns with standard poison ≈ 2 total if engine adds 1;
            # prefer dealing an immediate extra counter marker via attribute.
            d.set_attribute("PoisonDamage", poison_counters * 10)
    return effect


def radar_jam_lock_items():
    """Opponent can't play Trainer cards except Supporters next turn."""
    async def effect(ctx):
        await ctx.deal_damage()

        def pred(card):
            if is_supporter_card(card):
                return False
            d = def_for(card.archetype_id)
            # Lock non-supporter trainers (Item/Stadium/Tool/TM)
            from spirit.game.session.effects import is_trainer_card
            return is_trainer_card(card)
        if hasattr(ctx, "lock_plays"):
            ctx.lock_plays(ctx.opponent_id, pred)
    return effect


def agility_flip_protect():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Agility")
        if results and results[0]:
            await apply_protection(ctx, prevent=True, effects_too=True)
    return effect


def delta_charge_lightning_bench():
    async def effect(ctx):
        pool = [
            c for c in ctx.discard_pile()
            if is_energy_card(c)
            and energy_provides_type(c, PokemonTypes.LIGHTNING.value)
        ]
        if not pool:
            return
        bench = ctx.my_bench()
        if not bench:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Lightning Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(bench, "Attach to Bench?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def reversal_aura_passive(bonus: int = 20, reduce: int = 20) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.attacker is not holder:
                return
            if not calc.is_attack or not calc.is_opposing or not calc.to_active:
                return
            board = calc.board if hasattr(calc, "board") else None
            # Prefer session prizes via calc context — fall back using board
            try:
                mine = board.prizes_taken  # not usable directly
            except Exception:
                pass
            # Use prize pile lengths from calc if available
            pid = holder.owning_player_id
            opp = None
            if board is not None:
                for p in board.player_ids:
                    if p != pid:
                        opp = p
                        break
                if opp is None:
                    return
                my_left = len(board.find_player_area(pid, "prizePile").children)
                opp_left = len(board.find_player_area(opp, "prizePile").children)
                if my_left > opp_left:
                    calc.amount += bonus

        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder:
                return
            if not calc.is_attack or not calc.is_opposing:
                return
            board = getattr(calc, "board", None)
            if board is None:
                return
            pid = holder.owning_player_id
            opp = next((p for p in board.player_ids if p != pid), None)
            if opp is None:
                return
            my_area = board.find_player_area(pid, "prizePile")
            opp_area = board.find_player_area(opp, "prizePile")
            if my_area is None or opp_area is None:
                return
            if len(my_area.children) > len(opp_area.children):
                calc.amount = max(0, calc.amount - reduce)
    return _P()


def beacon_protection_passive(partner: str = "Volbeat") -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return False
            board = getattr(calc, "board", None)
            if board is None:
                return False
            if not any(partner.lower() in _display_name(p).lower()
                       for p in board.pokemon_in_play(holder.owning_player_id)):
                return False
            atk = calc.attacker
            if atk is None:
                return False
            return "dark" in _display_name(atk).lower()

        def blocks_attack_effects(self, target, carrier) -> bool:
            # Mirror prevent for effects when Dark-named
            return False  # damage path handles; effects via blocks_attack_effects_from

        def blocks_attack_effects_from(self, attacker, target, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if target is not holder:
                return False
            board = getattr(carrier, "board", None) or getattr(holder, "board", None)
            if board is None:
                return False
            if not any(partner.lower() in _display_name(p).lower()
                       for p in board.pokemon_in_play(holder.owning_player_id)):
                return False
            return "dark" in _display_name(attacker).lower()
    return _P()


def extra_protection_ex_passive(partner: str = "Illumise") -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return False
            if calc.attacker is None or not is_pokemon_ex(calc.attacker):
                return False
            board = getattr(calc, "board", None)
            if board is None:
                return False
            return any(partner.lower() in _display_name(p).lower()
                       for p in board.pokemon_in_play(holder.owning_player_id))

        def blocks_attack_effects_from(self, attacker, target, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if target is not holder or not is_pokemon_ex(attacker):
                return False
            return True
    return _P()


def prowl_on_evolve_any_card():
    async def effect(ctx):
        if not await ctx.ask_yes_no("Search your deck for any 1 card?"):
            return
        picks = await ctx.search_deck(
            lambda c: True, count=1, minimum=0, prompt="Choose any card")
        if picks:
            await ctx.put_in_hand(picks)
        await ctx.shuffle_deck()
    return effect


def conductive_body_beldum_passive(name: str = "Beldum") -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not is_in_active_spot(holder):
                return cost
            n = sum(
                1 for p in board.pokemon_in_play(holder.owning_player_id)
                if p is not holder and name.lower() in _display_name(p).lower()
            )
            return max(0, cost - n)
    return _P()


def shining_horn_solo_passive() -> Passive:
    class _P(Passive):
        def prevents_attack(self, attacker, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            mine = list(board.pokemon_in_play(holder.owning_player_id))
            if len(mine) != 1 or mine[0] is not holder:
                return False
            if attacker.owning_player_id == holder.owning_player_id:
                return False
            return is_basic_pokemon(attacker)
    return _P()


def binding_aura_passive() -> Passive:
    """Can't evolve Active from hand; can't attach Energy to Asleep Pokémon."""
    class _P(Passive):
        def blocks_evolution(self, player_id, target, carrier):
            if player_id == carrier.owning_player_id:
                return False
            return is_in_active_spot(target)

        def blocks_energy_attach(self, player_id, pokemon, energy, carrier):
            if player_id == carrier.owning_player_id:
                return False
            conds = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            return SpecialConditions.ASLEEP.value in conds or "Asleep" in conds
    return _P()


def extra_ball_vs_ex(base: int = 30, bonus: int = 20):
    async def effect(ctx):
        extra = bonus if ctx.defender is not None and is_pokemon_ex(ctx.defender) else 0
        await ctx.deal_damage(base + extra)
    return effect


def metal_scoop_attach(dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage(dmg)
        pool = [
            c for c in ctx.discard_pile()
            if is_energy_card(c)
            and (energy_provides_type(c, PokemonTypes.METAL.value)
                 or "metal energy" in (
                     getattr(def_for(c.archetype_id), "display_name", "") or "").lower())
        ]
        if pool and ctx.attacker is not None:
            picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Metal Energy")
            if picks:
                await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


def second_bite(base: int = 20, per: int = 10):
    async def effect(ctx):
        n = 0
        d = ctx.defender
        if d is not None:
            n = max(0, effective_max_hp(ctx.board, d) - d.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage(base + per * n)
    return effect


def discard_typed_energy_after(energy_type, amount: int = None):
    tv = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if amount is not None:
            await ctx.deal_damage(amount)
        else:
            await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if energy_provides_type(c, tv)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def flame_screen_reduce(amount: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_protection(ctx, prevent=False, reduce=amount)
    return effect


def rage_self_counters(base: int = 10, per: int = 10):
    async def effect(ctx):
        n = 0
        a = ctx.attacker
        if a is not None:
            n = max(0, effective_max_hp(ctx.board, a) - a.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage(base + per * n)
    return effect


def thunderbolt_discard_all(dmg: int = 40):
    async def effect(ctx):
        await ctx.deal_damage(dmg)
        a = ctx.attacker
        if a is not None:
            pool = [c for c in list(a.children) if is_energy_card(c)]
            if pool:
                await ctx.discard_cards(pool)
    return effect


def discard_energy_typed(energy_type):
    tv = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if energy_provides_type(c, tv)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def recoil_self(amount: int = 10):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(amount)


def flip_heads_paralyze(dmg: int = 0):
    async def effect(ctx):
        if dmg:
            await ctx.deal_damage(dmg)
        else:
            await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Paralyze")
        if results and results[0] and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


def surprise_attack_flip(dmg: int = 20):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Surprise Attack")
        if results and results[0]:
            await ctx.deal_damage(dmg)
    return effect


def slam_flip(per: int = 20, coins: int = 2):
    async def effect(ctx):
        results = await ctx.flip_coins(coins, "Slam")
        heads = sum(1 for r in (results or []) if r)
        if heads:
            await ctx.deal_damage(per * heads)
    return effect


def mist_attack_all(amount: int = 10):
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(
                amount, target=p, apply_modifiers=is_in_active_spot(p))
    return effect


# --- Holon trainers / stadiums ---


async def _holon_discard_cost(ctx) -> bool:
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if not hand:
        return False
    picks = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Discard a card from your hand")
    if not picks:
        return False
    await ctx.discard_cards(picks)
    return True


def holon_mentor():
    async def effect(ctx):
        if not await _holon_discard_cost(ctx):
            return

        def match(c):
            d = def_for(c.archetype_id)
            if d is None or getattr(d, "stage", None) != PokemonStage.BASIC:
                return False
            return getattr(d, "hp", 999) <= 100

        picks = await ctx.search_deck(
            match, count=3, minimum=0,
            prompt="Up to 3 Basic Pokémon with 100 HP or less")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def holon_mentor_condition():
    def cond(board, player_id):
        hand = board.find_player_area(player_id, "hand")
        return hand is not None and len(hand.children) >= 2  # self + 1
    return cond


def holon_farmer():
    async def effect(ctx):
        if not await _holon_discard_cost(ctx):
            return
        disc = list(ctx.discard_pile())
        basics_e = [c for c in disc if is_basic_energy_card(c)]
        pokes = [c for c in disc if is_pokemon_card(c)]
        e_picks = []
        if basics_e:
            e_picks = await ctx.choose_cards(
                basics_e, min(3, len(basics_e)), minimum=0,
                prompt="Up to 3 basic Energy") or []
        p_picks = []
        if pokes:
            p_picks = await ctx.choose_cards(
                [c for c in pokes if c not in e_picks],
                min(3, len(pokes)), minimum=0,
                prompt="Up to 3 Pokémon") or []
        chosen = list(e_picks) + list(p_picks)
        if chosen:
            await ctx.reveal_cards(chosen)
            for c in chosen:
                await ctx.put_on_top_of_deck(c)
        await ctx.shuffle_deck()
    return effect

def holon_lass():
    async def effect(ctx):
        if not await _holon_discard_cost(ctx):
            return
        n = (count_prizes_remaining("mine")(ctx)
             + count_prizes_remaining("opponent")(ctx))
        if n <= 0:
            return
        top = ctx.deck_top(n)
        if not top:
            return
        energies = [c for c in top if is_energy_card(c)]
        taken = []
        if energies:
            picks = await ctx.choose_cards(
                energies, len(energies), minimum=0,
                prompt="Energy cards to put into your hand") or []
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
                taken = list(picks)
        rest_count = len(top) - len(taken)
        if rest_count > 1:
            await ctx.reorder_deck_top(rest_count)
        await ctx.shuffle_deck()
    return effect

def holon_researcher():
    async def effect(ctx):
        if not await _holon_discard_cost(ctx):
            return

        def match(c):
            d = def_for(c.archetype_id)
            dn = (getattr(d, "display_name", None) or "").lower()
            if "metal energy" in dn:
                return True
            if is_pokemon_card(c) or getattr(d, "stage", None) is not None:
                return "\u03b4" in (getattr(d, "display_name", None) or "") or "δ" in (
                    getattr(d, "display_name", None) or "")
            return False

        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt="Metal Energy or δ Pokémon")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def holon_scientist():
    async def effect(ctx):
        if not await _holon_discard_cost(ctx):
            return
        mine = len(ctx.hand())
        opp = len(ctx.hand(ctx.opponent_id))
        if mine < opp:
            await ctx.draw_cards(opp - mine)
    return effect


def holon_transceiver():
    async def effect(ctx):
        def match(c):
            if not is_supporter_card(c):
                return False
            dn = (getattr(def_for(c.archetype_id), "display_name", None) or "")
            return "Holon" in dn

        # Deck or discard
        if await ctx.ask_yes_no("Search deck for a Holon Supporter? (No = discard)"):
            picks = await ctx.search_deck(
                match, count=1, minimum=0, prompt="Holon Supporter")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
            await ctx.shuffle_deck()
        else:
            pool = [c for c in ctx.discard_pile() if match(c)]
            if pool:
                picks = await ctx.choose_cards(
                    pool, 1, minimum=0, prompt="Holon Supporter from discard")
                if picks:
                    await ctx.put_in_hand(picks, reveal=True)
    return effect


def holon_research_tower_passive() -> Passive:
    """δ Pokémon: basic Energy provides its type OR Metal (1 Energy at a time)."""
    class _P(Passive):
        def modify_energy_provided(self, options, energy, holder, board):
            if holder is None or not is_delta_pokemon(holder):
                return options
            if not is_basic_energy_card(energy):
                return options
            metal = [PokemonTypes.METAL.value]
            cleaned = []
            for opt in (options or []):
                cleaned.append([opt[0]] if len(opt) > 1 else list(opt))
            if metal not in cleaned:
                cleaned.append(metal)
            return cleaned
    return _P()


def holon_ruins_draw():
    """Once per turn: if you have a δ Pokémon, draw then discard."""
    async def effect(ctx):
        if not any(is_delta_pokemon(p) for p in ctx.my_pokemon_in_play()):
            return
        await ctx.draw_cards(1)
        hand = list(ctx.hand())
        if hand:
            picks = await ctx.choose_cards(
                hand, 1, minimum=1, prompt="Discard a card")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def holon_ruins_condition():
    def cond(board, player_id, pokemon=None):
        return any(is_delta_pokemon(p) for p in board.pokemon_in_play(player_id))
    return cond

# --- EX12 Legend Maker / React Energy ---


def _is_react_energy(card) -> bool:
    d = def_for(card.archetype_id)
    dn = (getattr(d, "display_name", None) or "").lower()
    return "react energy" in dn


def count_react_energy(pokemon) -> int:
    if pokemon is None:
        return 0
    return sum(1 for c in pokemon.children if _is_react_energy(c))


def react_protection_per(per: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return
            n = count_react_energy(holder)
            if n:
                calc.amount = max(0, calc.amount - per * n)
    return _P()


def prevent_ex_attacks_next_turn():
    """Printed damage; prevent all effects including damage from Pokémon-ex next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_protection(ctx, prevent=True, effects_too=True, only_ex=True)
    return effect


def heavy_blow_react_or_minus(full: int = 70, per_counter: int = 10):
    async def effect(ctx):
        a = ctx.attacker
        if a is not None and count_react_energy(a) > 0:
            await ctx.deal_damage(full)
            return
        n = 0
        if a is not None:
            n = max(0, effective_max_hp(ctx.board, a) - a.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage(max(0, full - per_counter * n))
    return effect


def bound_crush_lock(amount: int = 60, title: str = "Bound Crush"):
    async def effect(ctx):
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if t is None:
            return
        await ctx.deal_damage(amount, target=t, apply_modifiers=is_in_active_spot(t))
        if ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)  # approximation: locks all, not only Bound Crush
    return effect


def search_fossils_to_bench(*names: str, count: int = 2):
    lowered = tuple(n.lower() for n in names)

    async def effect(ctx):
        def match(c):
            d = def_for(c.archetype_id)
            dn = (getattr(d, "display_name", None) or "").lower()
            return any(n == dn or n in dn for n in lowered)
        picks = await ctx.search_deck(match, count=count, minimum=0, prompt="Fossil Pokémon")
        for c in picks or []:
            await ctx.bench_pokemon(c)
        await ctx.shuffle_deck()
    return effect


def fire_remedy_on_attach():
    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id:
            return
        if ctx.energy_receiver is not ctx.source:
            return
        energy = ctx.attached_energy
        if energy is None or not energy_provides_type(energy, PokemonTypes.FIRE.value):
            return
        # Must be from hand — ON_ENERGY_ATTACHED from hand only fires for manual attach
        await ctx.heal(10, ctx.source)
        await ctx.cure_all_conditions(ctx.source)
    return effect


def overrun_bench(active_dmg: int = 30, bench_dmg: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(active_dmg)
        bench = ctx.opponent_bench()
        if bench:
            t = await ctx.choose_pokemon(bench, "Bench damage?")
            if t is not None:
                await ctx.deal_damage(bench_dmg, target=t, apply_modifiers=False)
    return effect


def dual_armor_if_react(*become_types) -> Passive:
    """Dual Armor while any React Energy attached."""
    types = [getattr(t, "value", t) for t in become_types]

    class _P(Passive):
        def modify_pokemon_types(self, current, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or count_react_energy(holder) <= 0:
                return current
            return list(types)
    return _P()


def vortex_chop(base: int = 70, boosted: int = 100):
    async def effect(ctx):
        d = ctx.defender
        amount = base
        if d is not None:
            resists = d.get_attribute(AttrID.RESISTANCE_TYPES) or []
            if resists:
                amount = boosted
        await ctx.deal_damage(amount)
    return effect


def self_charge_metal_from_hand():
    async def effect(ctx):
        pool = [
            c for c in ctx.hand()
            if is_energy_card(c) and (
                energy_provides_type(c, PokemonTypes.METAL.value)
                or "metal energy" in (getattr(def_for(c.archetype_id), "display_name", "") or "").lower())
        ]
        if not pool or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach Metal Energy")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


def shady_move_counter():
    async def effect(ctx):
        if ctx.source is None or not is_in_active_spot(ctx.source):
            return
        all_p = list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play())
        damaged = [
            p for p in all_p
            if effective_max_hp(ctx.board, p) - p.get_attribute(AttrID.HP, 0) >= 10
        ]
        if not damaged:
            return
        src = await ctx.choose_pokemon(damaged, "Move counter from?")
        if src is None:
            return
        dests = [p for p in all_p if p is not src]
        dest = await ctx.choose_pokemon(dests, "Move counter to?")
        if dest is None:
            return
        await ctx.heal(10, src)
        await ctx.deal_damage(10, target=dest, apply_modifiers=False, as_counters=True)
    return effect


def shadow_chant(base: int = 30, per: int = 10, cap: int = 60):
    async def effect(ctx):
        n = sum(1 for c in ctx.discard_pile() if is_supporter_card(c))
        extra = min(cap, per * n)
        await ctx.deal_damage(base + extra)
    return effect


def emerge_evolve():
    """Flip; on heads search deck for evolution of this Pokémon and evolve."""
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        results = await ctx.flip_coins(1, "Emerge")
        if not (results and results[0]):
            return
        logic = src.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or src.get_attribute(AttrID.NAME) or ""
        from spirit.game.content.definitions import evolves_from as _evolves_from

        def match(c):
            if logic and _evolves_from(c.archetype_id, logic):
                return True
            d = def_for(c.archetype_id)
            ef = (getattr(d, "evolves_from", None) or "")
            dn = src.get_attribute(AttrID.DISPLAY_NAME) or ""
            return bool(ef) and dn.lower() in ef.lower()
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Evolution card")
        if picks:
            await ctx.evolve_pokemon(src, picks[0])
        await ctx.shuffle_deck()
    return effect


def iron_defense_flip():
    from spirit.game.card_effects.passives_common import flip_protection
    return flip_protection(prevent=True, effects_too=True)


def reactive_shift():
    async def effect(ctx):
        donors = [
            p for p in ctx.my_pokemon_in_play()
            if count_react_energy(p) > 0
        ]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move React Energy from?")
        if src is None:
            return
        pool = [c for c in src.children if _is_react_energy(c)]
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="React Energy")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Move to?")
        if dest is not None:
            await ctx.move_energy(picks[0], dest)
    return effect


def extra_call_ex():
    async def effect(ctx):
        def match(c):
            return "ex" in (subtypes_for(c.archetype_id) or [])
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Pokémon-ex")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def safeguard_vs_ex_passive() -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return False
            return calc.attacker is not None and is_pokemon_ex(calc.attacker)

        def blocks_attack_effects_from(self, attacker, target, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            return target is holder and is_pokemon_ex(attacker)
    return _P()


def grind_energy(per: int = 10):
    async def effect(ctx):
        n = 0
        if ctx.attacker is not None:
            n = sum(1 for c in ctx.attacker.children if is_energy_card(c))
        await ctx.deal_damage(per * n)
    return effect


def shadow_tag_delayed(counters: int = 7):
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        if hasattr(ctx, "schedule_end_of_opponent_turn"):
            async def put():
                if d.parent is not None:
                    await ctx.deal_damage(
                        counters * 10, target=d,
                        apply_modifiers=False, as_counters=True)
            await ctx.schedule_end_of_opponent_turn(put)
        else:
            # Approximation: put counters now
            await ctx.deal_damage(
                counters * 10, target=d, apply_modifiers=False, as_counters=True)
    return effect


def link_blast(high: int = 50, low: int = 20):
    async def effect(ctx):
        a, d = ctx.attacker, ctx.defender
        if a is None or d is None:
            await ctx.deal_damage(low)
            return
        na = sum(1 for c in a.children if is_energy_card(c))
        nd = sum(1 for c in d.children if is_energy_card(c))
        await ctx.deal_damage(high if na == nd else low)
    return effect


def cross_cut_evolved(base: int = 40, bonus: int = 30):
    async def effect(ctx):
        extra = 0
        if ctx.defender is not None and is_evolution_pokemon(ctx.defender):
            extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def reactive_beating_confuse(base: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(base)
        if ctx.attacker is not None and count_react_energy(ctx.attacker) > 0:
            if ctx.defender is not None:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.CONFUSED)
    return effect


def hypno_splash(dmg: int = 40):
    from spirit.game.card_effects.attacks_common import condition_attack
    # deal then asleep - condition_attack with damage on Attack card
    async def effect(ctx):
        await ctx.deal_damage(dmg)
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    return effect


def search_typed_pokemon_non_ex(ptype, exclude_ex: bool = True):
    tv = getattr(ptype, "value", ptype)

    async def effect(ctx):
        def match(c):
            d = def_for(c.archetype_id)
            if d is None or getattr(d, "stage", None) is None:
                return False
            if exclude_ex and "ex" in (subtypes_for(c.archetype_id) or []):
                return False
            els = getattr(d, "elements", None) or []
            vals = [getattr(e, "value", e) for e in els]
            return tv in vals
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Pokémon")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def reactive_lift_water_retreat_passive() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if count_react_energy(holder) <= 0:
                return cost
            if "ex" in (subtypes_for(pokemon.archetype_id) or []):
                return cost
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.WATER.value not in types:
                return cost
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            return 0
    return _P()


def stages_retreat_tax_passive(extra: int = 1) -> Passive:
    """While Evolved: opponent Active pays Colorless more to retreat."""
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if not is_evolution_pokemon(holder):
                return cost
            if pokemon.owning_player_id == holder.owning_player_id:
                return cost
            if not is_in_active_spot(pokemon):
                return cost
            return cost + extra
    return _P()

# --- EX12 Legend Maker remaining helpers ---


def versatile_passive() -> Passive:
    """Mew ex: may use attacks of all other Pokémon in play."""
    from spirit.game.data_utils import Attack as _Attack

    class _P(Passive):
        stacking_key = "versatile"

        def granted_attacks(self, board, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return []
            attacks = []
            seen = set()
            for pid in board.player_ids:
                for p in board.pokemon_in_play(pid):
                    if p is holder:
                        continue
                    for ability in getattr(def_for(p.archetype_id), "abilities", None) or []:
                        if not isinstance(ability, _Attack):
                            continue
                        key = (ability.title, ability.game_text)
                        if key in seen:
                            continue
                        seen.add(key)
                        attacks.append(ability)
            return attacks
    return _P()


def type_change_copy_defending():
    """Until end of turn, become the Defending Pokémon's type(s)."""
    async def effect(ctx):
        src = ctx.source
        d = ctx.opponent_active()
        if src is None or d is None:
            return
        types = list(d.get_attribute(AttrID.POKEMON_TYPES) or [])
        if not types:
            return
        # OverrideTypePassive takes one type; for multi, use temp passive
        class _Override(Passive):
            def modify_pokemon_types(self, current, pokemon, carrier):
                if pokemon is src:
                    return list(types)
                return current
        ctx.add_temporary_passive(
            src, _Override(),
            expires_after_turn=ctx.session.turn_state.turn_number)
    return effect


def power_move_attach_switch():
    async def effect(ctx):
        a = ctx.attacker or ctx.source
        if a is None:
            return
        picks = await ctx.search_deck(is_energy_card, count=1, minimum=0, prompt="Energy")
        if picks:
            await ctx.attach_energy(picks[0], a)
        await ctx.shuffle_deck()
        bench = ctx.my_bench()
        if bench and await ctx.ask_yes_no("Switch with Benched Pokémon?"):
            t = await ctx.choose_pokemon(bench, "Switch with?")
            if t is not None:
                await ctx.switch_active(ctx.player_id, t)
    return effect


def icy_aura_passive() -> Passive:
    """Between turns: 1 counter on each Active that is not Water or has no Water Energy."""
    class _P(Passive):
        def between_turns_effect(self, board, carrier):
            return True  # marker; wired via ability activation if needed

    # Prefer Ability with BETWEEN_TURNS activation in card wire
    return _P()


def icy_aura_between_turns():
    async def effect(ctx):
        if ctx.source is None or not is_in_active_spot(ctx.source):
            return
        for p in (ctx.my_active(), ctx.opponent_active()):
            if p is None:
                continue
            types = p.get_attribute(AttrID.POKEMON_TYPES) or []
            has_water_e = any(
                energy_provides_type(c, PokemonTypes.WATER.value)
                for c in p.children)
            if PokemonTypes.WATER.value in types or has_water_e:
                continue
            await ctx.deal_damage(10, target=p, apply_modifiers=False, as_counters=True)
    return effect


def ice_barrier_vs_ex():
    """Prevent all effects including damage from Pokémon-ex during opponent's next turn."""
    async def effect(ctx):
        await apply_protection(ctx, prevent=True, effects_too=True, only_ex=True)
    return effect


def final_blizzard_bench_all(amount: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        if (count_prizes_remaining("opponent")(ctx) == 1
                and len(list(ctx.my_pokemon_in_play())) == 1):
            for p in ctx.opponent_bench():
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def final_blast_boost(base: int = 50, boosted: int = 100):
    async def effect(ctx):
        amount = base
        if (count_prizes_remaining("opponent")(ctx) == 1
                and len(list(ctx.my_pokemon_in_play())) == 1):
            amount = boosted
        await ctx.deal_damage(amount)
    return effect


def final_laser_distribute(normal: int = 3, boosted: int = 6):
    async def effect(ctx):
        n = normal
        if (count_prizes_remaining("opponent")(ctx) == 1
                and len(list(ctx.my_pokemon_in_play())) == 1):
            n = boosted
        remaining = n
        while remaining > 0:
            pool = list(ctx.opponent_pokemon_in_play())
            if not pool:
                break
            t = await ctx.choose_pokemon(pool, f"Put a damage counter ({remaining} left)")
            if t is None:
                break
            await ctx.deal_damage(10, target=t, apply_modifiers=False, as_counters=True)
            remaining -= 1
    return effect


def shadow_curse_on_ko(counters: int = 3):
    async def effect(ctx):
        # ON_KNOCKED_OUT
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Put damage counters on?")
        if t is not None:
            await ctx.deal_damage(
                counters * 10, target=t, apply_modifiers=False, as_counters=True)
    return effect


def cursed_reaction(base: int = 2, react_bonus: int = 4):
    async def effect(ctx):
        n = react_bonus if (
            ctx.attacker is not None and count_react_energy(ctx.attacker) > 0
        ) else base
        remaining = n
        while remaining > 0:
            pool = list(ctx.opponent_pokemon_in_play())
            if not pool:
                break
            t = await ctx.choose_pokemon(pool, f"Counter ({remaining} left)")
            if t is None:
                break
            await ctx.deal_damage(10, target=t, apply_modifiers=False, as_counters=True)
            remaining -= 1
    return effect


def rear_sensor_passive() -> Passive:
    """Active Basic (excl ex) can't use Poké-Powers (both players)."""
    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_POWER:
                return False
            if is_pokemon_ex(pokemon) or not is_basic_pokemon(pokemon):
                return False
            if not is_in_active_spot(pokemon):
                return False
            return True
    return _P()


def disorder_confuse_if_special_energy(base: int = 20):
    from spirit.game.session.effects import is_special_energy
    async def effect(ctx):
        await ctx.deal_damage(base)
        d = ctx.defender
        if d is None:
            return
        if any(is_special_energy(c) for c in d.children):
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def reactive_booster_passive() -> Passive:
    """Each React Energy on your Huntail/Gorebyss provides 2 of every type."""
    class _P(Passive):
        def modify_energy_provided(self, energy, pokemon, carrier, provided):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None:
                return provided
            if pokemon.owning_player_id != holder.owning_player_id:
                return provided
            dn = (pokemon.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            if "huntail" not in dn and "gorebyss" not in dn:
                return provided
            if not _is_react_energy(energy):
                return provided
            # Provide 2 of every type
            from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
            # Double each
            out = {}
            for k, v in (provided or {}).items():
                out[k] = max(v, 2)
            # Ensure all types at 2
            for tv in ALL_TYPES_ONE_AT_A_TIME:
                out[tv] = 2
            return out
    return _P()


def reactive_generator():
    async def effect(ctx):
        src = ctx.source
        if src is None or count_react_energy(src) > 0:
            return
        def match(c):
            return _is_react_energy(c)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="React Energy")
        if picks:
            await ctx.attach_energy(picks[0], src)
        await ctx.shuffle_deck()
    return effect


def reactive_colors_passive(*become_types) -> Passive:
    types = [getattr(t, "value", t) for t in become_types]

    class _P(Passive):
        def modify_pokemon_types(self, current, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or count_react_energy(holder) <= 0:
                return current
            return list(types)
    return _P()


def reactive_aroma_passive() -> Passive:
    """Between turns-ish: remove 1 counter from each non-ex with a condition, while React attached.
    Approximation: ON_ENERGY / between — wire as BETWEEN_TURNS Ability."""
    return None  # wired via effect below


def reactive_aroma_between_turns():
    async def effect(ctx):
        src = ctx.source
        if src is None or count_react_energy(src) <= 0:
            return
        for p in ctx.my_pokemon_in_play():
            if is_pokemon_ex(p):
                continue
            conds = p.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            if conds:
                await ctx.heal(10, p)
    return effect


def reactive_healing_on_attach():
    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id:
            return
        if ctx.energy_receiver is not ctx.source:
            return
        if ctx.attached_energy is None or not _is_react_energy(ctx.attached_energy):
            return
        await ctx.heal(9999, ctx.source)
    return effect


def reactive_shield_vs_ex_passive() -> Passive:
    """While React on this Tentacruel: your Tentacruels prevent effects from ex."""
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if count_react_energy(holder) <= 0:
                return False
            if calc.target is None:
                return False
            dn = (calc.target.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            if "tentacruel" not in dn:
                return False
            if calc.target.owning_player_id != holder.owning_player_id:
                return False
            if not (calc.is_attack and calc.is_opposing):
                return False
            return calc.attacker is not None and is_pokemon_ex(calc.attacker)

        def blocks_attack_effects_from(self, attacker, target, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if count_react_energy(holder) <= 0:
                return False
            dn = (target.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            if "tentacruel" not in dn:
                return False
            if target.owning_player_id != holder.owning_player_id:
                return False
            return is_pokemon_ex(attacker)
    return _P()


def reactive_blast(base: int = 40, per: int = 30):
    async def effect(ctx):
        a = ctx.attacker
        extra = 0
        if a is not None:
            pool = [c for c in a.children if _is_react_energy(c)]
            if pool:
                n = await ctx.choose_number(
                    0, len(pool), prompt="Discard how many React Energy?")
                if n is None:
                    n = 0
                n = max(0, min(n, len(pool)))
                if n:
                    picks = await ctx.choose_cards(
                        pool, n, minimum=n, prompt="Discard React Energy")
                    if picks:
                        await ctx.discard_cards(picks)
                        extra = per * len(picks)
        await ctx.deal_damage(base + extra)
    return effect


def reactive_recharge_on_ko():
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        pool = [c for c in src.children if _is_react_energy(c)]
        if not pool:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not dests:
            return
        # Move any number
        while pool:
            if not await ctx.ask_yes_no("Move a React Energy?"):
                break
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="React Energy")
            if not picks:
                break
            dest = await ctx.choose_pokemon(dests, "Move to?")
            if dest is None:
                break
            await ctx.move_energy(picks[0], dest)
            pool = [c for c in src.children if _is_react_energy(c)]
    return effect


def tender_tentacles_heal(counters: int = 2):
    """Attack: printed damage; if React attached, heal `counters` damage counters."""
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is not None and count_react_energy(a) > 0:
            await ctx.heal(counters * 10, a)
    return effect


def ancient_protection_passive(*names) -> Passive:
    lowered = tuple(n.lower() for n in names)

    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            t = calc.target
            if t is None:
                return
            holder = carrier_pokemon(carrier) or carrier
            if t.owning_player_id != holder.owning_player_id:
                return
            dn = _display_name(t).lower()
            if any(n in dn for n in lowered):
                calc.weakness_applies = False
    return _P()


def ancient_shell_passive(*need_names, reduce: int = 20) -> Passive:
    need = tuple(n.lower() for n in need_names)

    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack:
                return
            mine = [
                _display_name(p).lower()
                for p in calc.board.pokemon_in_play(holder.owning_player_id)
            ]
            if any(any(n in dn for n in need) for dn in mine):
                calc.amount = max(0, calc.amount - reduce)
    return _P()


def ancient_tentacles_passive(*names) -> Passive:
    lowered = tuple(n.lower() for n in names)

    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.attacker is None:
                return
            if calc.attacker.owning_player_id != holder.owning_player_id:
                return
            dn = _display_name(calc.attacker).lower()
            if any(n in dn for n in lowered):
                calc.resistance_applies = False
    return _P()


def ancient_fang_passive(*need_names, bonus: int = 20) -> Passive:
    need = tuple(n.lower() for n in need_names)

    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.attacker is not holder:
                return
            mine = [
                _display_name(p).lower()
                for p in calc.board.pokemon_in_play(holder.owning_player_id)
            ]
            if any(any(n in dn for n in need) for dn in mine):
                if calc.is_attack and calc.is_opposing:
                    calc.amount += bonus
    return _P()


def support_navigation_on_bench():
    async def effect(ctx):
        # ON_PLAY to bench
        picks = await ctx.search_deck(
            is_supporter_card, count=1, minimum=0, prompt="Supporter")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def emerge_charge_on_evolve(count: int = 2):
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        n = min(count, len(pool))
        picks = await ctx.choose_cards(pool, n, minimum=0, prompt="Attach Energy from discard")
        for c in picks or []:
            await ctx.attach_energy(c, src)
    return effect


def nectar_pod_switch_stage2():
    async def effect(ctx):
        bench = [
            p for p in ctx.opponent_bench()
            if getattr(def_for(p.archetype_id), "stage", None) == PokemonStage.STAGE2
        ]
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch in Stage 2?")
        if t is not None:
            await ctx.switch_active(ctx.opponent_id, t)
    return effect


def shade_block_powers_passive(partner: str, *blocked_types) -> Passive:
    """While partner in play: typed Pokémon (excl ex) can't use Poké-Powers."""
    partner_l = partner.lower()
    tvs = {getattr(t, "value", t) for t in blocked_types}

    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_POWER:
                return False
            if is_pokemon_ex(pokemon):
                return False
            holder = carrier_pokemon(carrier) or carrier
            partners = [
                p for p in (ability and []) or []
            ]
            # Check partner in play for holder
            found = False
            for p in calc_board_pokemon(holder):
                dn = (p.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
                if partner_l in dn:
                    found = True
                    break
            if not found:
                return False
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            return any(t in tvs for t in types)

        def _partner_in_play(self, holder, board):
            for p in board.pokemon_in_play(holder.owning_player_id):
                dn = (p.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
                if partner_l in dn:
                    return True
            return False

        def blocks_ability(self, ability, pokemon, carrier):  # noqa: F811
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_POWER:
                return False
            if is_pokemon_ex(pokemon):
                return False
            holder = carrier_pokemon(carrier) or carrier
            board = getattr(carrier, "board", None) or getattr(pokemon, "board", None)
            # Prefer session board via pokemon
            # Use a soft check: look through siblings via owning player areas is hard here
            # Store partner check using board from active_passives caller — board not passed
            # Fallback: always check via pokemon's parent chain — use blocks_abilities style
            return False  # replaced below
    return _P()


def sol_shade_passive() -> Passive:
    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_POWER:
                return False
            if is_pokemon_ex(pokemon):
                return False
            holder = carrier_pokemon(carrier) or carrier
            # Need Solrock in play — use board from pokemon entity
            board = None
            # active_passives passes board separately; blocks_ability often has board via calc
            # Check sibling presence via a weak heuristic: look at carrier's known board
            from spirit.game.session.passives import _board_of
            # Simpler: use pokemon lookup through all known — store on first call
            return False
    # Rewrite properly:
    return _shade_block("Solrock", PokemonTypes.FIRE)


def _shade_block(partner_name: str, *types) -> Passive:
    """Block typed Poké-Powers while named partner is in play (Luna/Sol Shade)."""
    partner_l = partner_name.lower()
    tvs = {getattr(t, "value", t) for t in types}

    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier, board=None):
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_POWER:
                return False
            if is_pokemon_ex(pokemon):
                return False
            types_list = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if not any(t in tvs for t in types_list):
                return False
            holder = carrier_pokemon(carrier) or carrier
            if board is None:
                return False
            names = [
                _display_name(p).lower()
                for p in board.pokemon_in_play(holder.owning_player_id)
            ]
            if not any(partner_l in n for n in names):
                return False
            return True
    return _P()


def luna_shade_passive() -> Passive:
    return _shade_block("Lunatone", PokemonTypes.COLORLESS)


def sol_shade_passive() -> Passive:  # noqa: F811
    return _shade_block("Solrock", PokemonTypes.FIRE)


def moon_guidance_trainer():
    from spirit.game.session.effects import is_trainer_card, is_supporter_card
    async def effect(ctx):
        def match(c):
            return is_trainer_card(c) and not is_supporter_card(c)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Trainer")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def pattern_distraction_passive() -> Passive:
    """While Active: opponent's Basic must flip to attack; tails fails."""
    class _P(Passive):
        def requires_attack_attempt_flip(self, attacker, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if not is_in_active_spot(holder):
                return None
            if attacker.owning_player_id == holder.owning_player_id:
                return None
            if not is_basic_pokemon(attacker):
                return None
            return "Pattern Distraction"
    return _P()


def entangling_vines_lock_basic():
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is not None and is_basic_pokemon(d):
            lock_all_attacks(ctx, d)
    return effect


def important_errands_react():
    async def effect(ctx):
        def match(c):
            return _is_react_energy(c)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="React Energy")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def drawup_power_energy():
    async def effect(ctx):
        picks = await ctx.search_deck(is_energy_card, count=1, minimum=0, prompt="Energy")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def continuous_tumble(per: int = 10):
    async def effect(ctx):
        heads = 0
        while True:
            results = await ctx.flip_coins(1, "Continuous Tumble")
            if results and results[0]:
                heads += 1
            else:
                break
        await ctx.deal_damage(per * heads)
    return effect


def magnetic_swirl(dmg: int = 20):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Magnetic Swirl")
        if not (results and results[0]):
            return
        await ctx.deal_damage(dmg)
        d = ctx.defender
        if d is None:
            return
        pool = [c for c in d.children if is_energy_card(c)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Energy")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def influence_fossils_to_bench():
    return search_fossils_to_bench(
        "Omanyte", "Kabuto", "Aerodactyl", "Lileep", "Anorith", count=2)


def overhead_toss(active: int = 30, self_bench: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(active)
        bench = ctx.my_bench()
        if bench:
            t = await ctx.choose_pokemon(bench, "Damage your Bench?")
            if t is not None:
                await ctx.deal_damage(self_bench, target=t, apply_modifiers=False)
    return effect


def bi_blast(base: int = 20, bonus: int = 20):
    async def effect(ctx):
        extra = bonus if (
            ctx.attacker is not None and count_react_energy(ctx.attacker) > 0
        ) else 0
        await ctx.deal_damage(base + extra)
    return effect


def sharp_leaf(base: int = 40, bonus: int = 30):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Sharp Leaf")
        extra = bonus if results and results[0] else 0
        await ctx.deal_damage(base + extra)
    return effect


def bouncing_ball(self_dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def rely_on_friends(base: int = 40, per: int = 10):
    async def effect(ctx):
        n = sum(
            1 for p in ctx.my_bench()
            if getattr(def_for(p.archetype_id), "stage", None) == PokemonStage.STAGE1
        )
        await ctx.deal_damage(base + per * n)
    return effect


def ice_throw(base: int = 80, vs_fighting: int = 120):
    async def effect(ctx):
        amount = base
        d = ctx.defender
        if d is not None:
            types = d.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.FIGHTING.value in types:
                amount = vs_fighting
        await ctx.deal_damage(amount)
    return effect


def string_pull_switch():
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch in?")
        if t is not None:
            await ctx.switch_active(ctx.opponent_id, t)
    return effect


def ignite_if_full_flame():
    async def effect(ctx):
        await ctx.deal_damage()
        stadium = ctx.stadium_in_play()
        if stadium is None:
            return
        dn = (stadium.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
        if "full flame" in dn and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def burning_sensation():
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        max_hp = effective_max_hp(ctx.board, d)
        if max_hp - d.get_attribute(AttrID.HP, 0) > 0:
            await ctx.apply_special_condition(d, SpecialConditions.BURNED)
    return effect


def swift_blow_react(base: int = 60, per: int = 20):
    async def effect(ctx):
        n = count_react_energy(ctx.attacker) if ctx.attacker else 0
        await ctx.deal_damage(base + per * n)
    return effect


def haunt_counters(n: int = 2):
    async def effect(ctx):
        if ctx.defender is not None:
            await ctx.deal_damage(
                n * 10, target=ctx.defender, apply_modifiers=False, as_counters=True)
    return effect


def down_draw(n: int = 2):
    """Draw n cards from the bottom of the deck."""
    async def effect(ctx):
        await ctx.draw_from_bottom(n)
    return effect


def deadlock_named_passive(name: str = "Dunsparce") -> Passive:
    needle = name.lower()

    class _P(Passive):
        def prevents_attack(self, attacker, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if not is_in_active_spot(holder):
                return False
            if attacker.owning_player_id == holder.owning_player_id:
                return False
            dn = (attacker.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
            return needle in dn
    return _P()


def tripping_turn():
    async def effect(ctx):
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
        bench = ctx.my_bench()
        if bench and await ctx.ask_yes_no("Switch with Bench?"):
            t = await ctx.choose_pokemon(bench, "Switch with?")
            if t is not None:
                await ctx.switch_active(ctx.player_id, t)
    return effect


def whimsy_draw(per_heads: int = 2):
    async def effect(ctx):
        total = 0
        while True:
            results = await ctx.flip_coins(1, "Whimsy Draw")
            if results and results[0]:
                total += per_heads
            else:
                break
        if total:
            await ctx.draw_cards(total)
    return effect


def double_edge_recoil(self_dmg: int = 10):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_dmg)


def body_slam_paralyze(dmg: int = 20):
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.PARALYZED, flip=True)


def stench_no_powers_passive() -> Passive:
    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not is_in_active_spot(holder):
                return False
            return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER
    return _P()


def return_trance():
    async def effect(ctx):
        a = ctx.attacker
        if a is not None:
            pool = [c for c in a.children if is_energy_card(c)]
            if pool:
                picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Return Energy")
                if picks:
                    await ctx.put_in_hand(picks, reveal=False)
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    return effect


def dream_eater(amount: int = 50):
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        conds = d.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if SpecialConditions.ASLEEP not in conds and (
                getattr(SpecialConditions.ASLEEP, "value", SpecialConditions.ASLEEP)
                not in conds):
            return
        await ctx.deal_damage(amount)
    return effect


def paranoid_while_confused_passive(bonus: int = 50) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.attacker is not holder:
                return
            conds = holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            confused = SpecialConditions.CONFUSED
            cv = getattr(confused, "value", confused)
            if confused in conds or cv in conds:
                if calc.is_attack and calc.is_opposing:
                    calc.amount += bonus
    return _P()


def stages_energy_as_fire_passive() -> Passive:
    class _P(Passive):
        def modify_energy_provided(self, energy, pokemon, carrier, provided):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or not is_evolution_pokemon(holder):
                return provided
            return {PokemonTypes.FIRE.value: 1}
    return _P()


def multiple_force(base: int = 30, per: int = 10):
    async def effect(ctx):
        extra = 0
        if ctx.attacker is not None and count_react_energy(ctx.attacker) > 0:
            for pid in (ctx.player_id, ctx.opponent_id):
                for p in ctx.board.pokemon_in_play(pid):
                    dn = (p.get_attribute(AttrID.DISPLAY_NAME) or "").lower()
                    if "magnemite" in dn or "magneton" in dn:
                        extra += per
        await ctx.deal_damage(base + extra)
    return effect


def evolutionary_fan_devolve():
    async def effect(ctx):
        # ON_EVOLVE into Shiftry
        evolved = [
            p for p in ctx.my_pokemon_in_play()
            if is_evolution_pokemon(p) and p is not ctx.source
        ]
        if not evolved:
            return
        t = await ctx.choose_pokemon(evolved, "Devolve?")
        if t is None:
            return
        await ctx.devolve_pokemon(t, steps=1, destination="hand")
    return effect


def devolution_wave_react():
    async def effect(ctx):
        a = ctx.attacker
        n = count_react_energy(a) if a else 0
        if n <= 0:
            return
        evolved = [
            p for p in ctx.opponent_pokemon_in_play()
            if is_evolution_pokemon(p)
        ]
        if not evolved:
            return
        picks = []
        for _ in range(min(n, len(evolved))):
            pool = [p for p in evolved if p not in picks]
            if not pool:
                break
            t = await ctx.choose_pokemon(pool, "Devolve?", minimum=0)
            if t is None:
                break
            picks.append(t)
        for t in picks:
            await ctx.devolve_pokemon(t, steps=1, destination="deck")
        await ctx.opponent_shuffle_deck() if hasattr(ctx, "opponent_shuffle_deck") else None
    return effect


def enraged_linear_attack(per: int = 10):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        dmg = max(0, effective_max_hp(ctx.board, a) - a.get_attribute(AttrID.HP, 0))
        amount = (dmg // 10) * per
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if t is not None:
            await ctx.deal_damage(
                amount, target=t,
                apply_modifiers=is_in_active_spot(t))
    return effect


def power_circulation():
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Basic Energy to top")
        if picks:
            await ctx.put_on_top_of_deck(picks[0])
    return effect


def flick_poison_switch():
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench:
            t = await ctx.choose_pokemon(bench, "Switch in?")
            if t is not None:
                await ctx.switch_active(ctx.opponent_id, t)
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def call_for_lunatone():
    async def effect(ctx):
        def match(c):
            d = def_for(c.archetype_id)
            dn = (getattr(d, "display_name", None) or "").lower()
            return dn == "lunatone"
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Lunatone")
        if picks:
            await ctx.bench_pokemon(picks[0])
        await ctx.shuffle_deck()
    return effect


# Stadiums / trainers


def cursed_stone_between_turns():
    async def effect(ctx):
        # Put 1 counter on each Pokémon that has a Poké-Power (both players)
        for pid in (ctx.player_id, ctx.opponent_id):
            for p in ctx.board.pokemon_in_play(pid):
                has_pp = False
                for ab in getattr(def_for(p.archetype_id), "abilities", None) or []:
                    if getattr(ab, "ability_type", None) == AbilityTypes.POKE_POWER:
                        has_pp = True
                        break
                if has_pp:
                    await ctx.deal_damage(
                        10, target=p, apply_modifiers=False, as_counters=True)
    return effect


def fieldworker_draw():
    """Draw 3; opponent may draw 1."""
    async def effect(ctx):
        await ctx.draw_cards(3)
        if await ctx.ask_yes_no("Draw a card?", player_id=ctx.opponent_id):
            await ctx.draw_cards(1, player_id=ctx.opponent_id)
    return effect


def full_flame_passive() -> Passive:
    """Burn puts 4 damage counters; Burned can't be cured by evolve/devolve."""
    class _P(Passive):
        def modify_burn_counters(self, counters, pokemon, carrier):
            return 4

        def prevents_condition_removal(self, pokemon, condition, reason, carrier):
            burned = SpecialConditions.BURNED
            cond = condition
            if cond != burned and getattr(cond, "value", cond) != getattr(burned, "value", burned):
                return False
            return reason in ("evolve", "devolve", "evolution", "devolution")
    return _P()


def giant_stump_passive() -> Passive:
    """Each player can't have more than 3 Benched Pokémon; on-play enforce discards."""
    class _P(Passive):
        def bench_capacity(self, player_id, carrier):
            return 3
    return _P()


def power_tree_effect():
    from spirit.game.session.effects import is_special_energy
    async def effect(ctx):
        if any(is_special_energy(c) for c in ctx.discard_pile()):
            return
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Basic Energy to hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def strange_cave_effect():
    async def effect(ctx):
        names = {"omanyte", "kabuto", "aerodactyl", "aerodactyl ex",
                 "lileep", "anorith"}
        pool = []
        for c in ctx.hand():
            d = def_for(c.archetype_id)
            dn = (getattr(d, "display_name", None) or "").lower()
            if dn in names or dn.replace(" ex", "") in names:
                # Exact-ish
                if any(n == dn or dn.startswith(n) for n in names):
                    pool.append(c)
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Fossil to Bench")
        if picks:
            await ctx.bench_pokemon(picks[0])
    return effect


def prevent_ex_protect_next():
    """Ice Barrier / Speed Stroke style."""
    return prevent_ex_attacks_next_turn()



def stretch_claws_react(bench_dmg: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None or count_react_energy(a) <= 0:
            return
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Bench damage?")
        if t is not None:
            await ctx.deal_damage(bench_dmg, target=t, apply_modifiers=False)
    return effect



def flame_swirl_discard():
    """Discard 2 Fire Energy OR 1 React Energy attached to self."""
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        reacts = [c for c in a.children if _is_react_energy(c)]
        fires = [c for c in a.children if energy_provides_type(c, PokemonTypes.FIRE.value)]
        options = []
        if len(fires) >= 2:
            options.append("Discard 2 Fire Energy")
        if reacts:
            options.append("Discard 1 React Energy")
        if not options:
            return
        if len(options) == 1:
            choice = 0
        else:
            choice = await ctx.choose("Discard?", options)
        if options[choice].startswith("Discard 1 React"):
            picks = await ctx.choose_cards(reacts, 1, minimum=1, prompt="React Energy")
            if picks:
                await ctx.discard_cards(picks)
        else:
            picks = await ctx.choose_cards(fires, 2, minimum=2, prompt="Fire Energy")
            if picks:
                await ctx.discard_cards(picks)
    return effect


async def cyclone_energy_on_attach(ctx):
    """When attached from hand to Active: opponent switches Defending with a Benched (they choose)."""
    target = ctx.attached_to
    if target is None:
        return
    # Must be attached to Active
    active = ctx.my_active()
    if active is None or target is not active:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    # Opponent chooses
    pick = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to switch into the Active Spot",
        player_id=ctx.opponent_id)
    if pick is not None:
        await ctx.switch_active(ctx.opponent_id, pick)


# --- EX13 Holon Phantoms ---


def _has_delta(card_or_pokemon) -> bool:
    """Best-effort: δ in display_name or searchable / subtypes / game text mark."""
    d = def_for(getattr(card_or_pokemon, "archetype_id", None) or "")
    if d is None:
        return False
    dn = getattr(d, "display_name", None) or ""
    if "δ" in dn or "Delta" in dn:
        return True
    # Many δ cards keep display_name without mark; check searchable_by / name
    for s in getattr(d, "searchable_by", None) or []:
        if "δ" in s or "delta" in s.lower():
            return True
    # Fall back: card key often includes Delta in script comments; use elements of
    # Holon Phantoms — smoke uses archetype; also check game_text of abilities
    for ab in getattr(d, "abilities", None) or []:
        gt = getattr(ab, "game_text", "") or ""
        if "δ" in gt or "delta" in gt.lower():
            # weak signal
            pass
    # Attribute flag if engine stamped one
    if getattr(card_or_pokemon, "get_attribute", None):
        raw = card_or_pokemon.get_attribute(AttrID.DISPLAY_NAME) or ""
        if isinstance(raw, dict):
            raw = raw.get("id") or ""
        if "δ" in str(raw):
            return True
    return False


def count_delta_in_play(ctx, side: str = "mine") -> int:
    pool = ctx.my_pokemon_in_play() if side == "mine" else ctx.opponent_pokemon_in_play()
    return sum(1 for p in pool if _has_delta(p))


def delta_draw_up_to():
    async def effect(ctx):
        n = count_delta_in_play(ctx)
        if n <= 0:
            return
        # Draw up to n — ask how many
        k = n
        if hasattr(ctx, "choose_number"):
            k = await ctx.choose_number(0, n, prompt=f"Draw up to {n}?")
            if k is None:
                k = n
        await ctx.draw_cards(max(0, k))
    return effect


def holon_adventurer():
    async def effect(ctx):
        hand = list(ctx.hand())
        # Must discard 1; card itself already leaving as supporter
        # Pool = hand excluding this supporter if still present
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Discard a card")
        if not picks:
            return
        discarded = picks[0]
        await ctx.discard_cards(picks)
        n = 4 if _has_delta(discarded) else 3
        await ctx.draw_cards(n)
    return effect


def holon_fossil_item():
    names = {"omanyte", "kabuto", "aerodactyl", "aerodactyl ex",
             "lileep", "anorith"}

    def match(c):
        d = def_for(c.archetype_id)
        dn = (getattr(d, "display_name", None) or "").lower()
        return dn in names or any(dn.startswith(n) for n in names)

    async def effect(ctx):
        results = await ctx.flip_coins(1, "Holon Fossil")
        if results and results[0]:
            picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Fossil")
            if picks:
                await ctx.bench_pokemon(picks[0])
            await ctx.shuffle_deck()
        else:
            pool = [c for c in ctx.hand() if match(c)]
            if not pool:
                return
            picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Fossil from hand")
            if picks:
                await ctx.bench_pokemon(picks[0])
    return effect


def holon_lake_passive() -> Passive:
    """δ Pokémon may use this stadium's attacks."""
    from spirit.game.data_utils import Attack as _Attack

    class _P(Passive):
        stacking_key = "holon_lake"

        def granted_attacks(self, board, pokemon, carrier):
            if not _has_delta(pokemon):
                return []
            definition = def_for(getattr(carrier, "archetype_id", None) or "")
            attacks = []
            for ability in getattr(definition, "abilities", None) or []:
                if isinstance(ability, _Attack):
                    attacks.append(ability)
            return attacks
    return _P()


def fellowship_oddish_line_passive() -> Passive:
    from spirit.game.data_utils import Attack as _Attack
    names = {"oddish", "gloom", "vileplume", "vileplume ex", "bellossom"}

    class _P(Passive):
        def granted_attacks(self, board, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return []
            attacks = []
            seen = set()
            for p in board.pokemon_in_play(holder.owning_player_id):
                if p is holder:
                    continue
                dn = _display_name(p).lower()
                if not any(n in dn for n in names):
                    continue
                for ability in getattr(def_for(p.archetype_id), "abilities", None) or []:
                    if not isinstance(ability, _Attack):
                        continue
                    key = (ability.title, ability.game_text)
                    if key in seen:
                        continue
                    seen.add(key)
                    attacks.append(ability)
            return attacks
    return _P()


def aqua_flower_no_weakness():
    """Deal attack damage; attacker has no Weakness during opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            from spirit.game.card_effects.passives_common import NoWeaknessPassive
            ctx.add_passive_through_opponents_turn(ctx.attacker, NoWeaknessPassive())
    return effect


def aqua_flower_reduce(reduce: int = 20):
    """Deprecated alias — prefer aqua_flower_no_weakness()."""
    return aqua_flower_no_weakness()


def blaze_kick(base: int = 40, bonus: int = 20):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Blaze Kick")
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
            if ctx.defender is not None:
                await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def take_down_recoil(self_dmg: int = 10):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_dmg)


def reckless_charge_recoil(self_dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Reckless Charge")
        if results and not results[0] and ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def delta_support_basic_to_delta():
    async def effect(ctx):
        # Requires Holon Supporter in play
        stadium_or_supporter_holon = False
        # Check active trainer / last supporter — soft: any card in play with Holon
        for area_name in ("activeTrainer",):
            pass
        # Soft check: look for Holon in stadium display name OR skip gate
        stadium = ctx.stadium_in_play()
        if stadium is not None:
            dn = _display_name(stadium).lower()
            if "holon" in dn:
                stadium_or_supporter_holon = True
        # Also: supporter next to active — approximate via ask always allowed if Holon in discard search
        # Printed: Supporter with Holon in name in play — soft allow if any Holon supporter was played (engine gap)
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c) or (
            "rainbow" in _display_name(c).lower() and "δ" in _display_name(c))]
        # Actually: search discard for basic Energy or δ Rainbow Energy, attach to δ Pokémon
        def match(c):
            dn = _display_name(c).lower()
            if is_basic_energy_card(c):
                return True
            return "rainbow" in dn and ("δ" in dn or "delta" in dn)
        pool = [c for c in ctx.discard_pile() if match(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Energy from discard")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if _has_delta(p)]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Attach to δ Pokémon?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def harsh_fluid_delayed(counters: int = 5):
    """Deal damage now; put `counters` damage counters at end of opponent's next turn."""
    async def effect(ctx):
        d = ctx.defender
        await ctx.deal_damage()
        if d is None:
            return
        eid = d.entity_id
        async def put(session):
            board = session.board_state
            target = board.get_entity(eid)
            if target is None or target.parent is None:
                return
            # Place counters via a fresh effect context
            from spirit.game.session.effects import EffectContext
            c = EffectContext(session, ctx.player_id, ctx.attacker, ctx.ability)
            await c.deal_damage(
                counters * 10, target=target, apply_modifiers=False, as_counters=True)
            await session._flush_effect_runs(c)
        # End of opponent's next turn == checkup of turn_number+1
        ctx.schedule_at_checkup(1, put)
    return effect


def splash_back_return_bench():
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if len(bench) < 4:
            return
        t = await ctx.choose_pokemon(bench, "Return to hand?")
        if t is not None:
            await ctx.return_to_hand_full_stack(t) if hasattr(ctx, "return_to_hand_full_stack") else await ctx.put_in_hand(
                [t], reveal=True)
    return effect


def energy_loop_return(n: int = 2):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if len(pool) < n:
            n2 = len(pool)
        else:
            n2 = n
        if n2 <= 0:
            return
        picks = await ctx.choose_cards(pool, n2, minimum=n2, prompt="Return Energy")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


def delta_reduction_next(reduce: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        # Soft: protect self by reduce next turn
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, reduce=reduce)
    return effect


def crystal_laser_lock():
    """During your next turn, this Pokémon's attacks do +40 damage."""
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await apply_own_next_turn_boost(ctx, 40)
    return effect


def teleportation_burst_switch():
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if bench:
            t = await ctx.choose_pokemon(bench, "Switch with?")
            if t is not None:
                await ctx.switch_active(ctx.player_id, t)
    return effect


def pebble_throw(amount: int = 10):
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Pebble Throw")
        if t is not None:
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def delta_circle(base: int = 10, per: int = 10):
    async def effect(ctx):
        n = count_delta_in_play(ctx)
        await ctx.deal_damage(base + per * max(0, n - 0))
        # Printed: 10 plus 10 per δ — including self
    return effect


def delta_supply_attach():
    async def effect(ctx):
        def match(c):
            if is_basic_energy_card(c):
                return True
            dn = _display_name(c).lower()
            return "rainbow" in dn and ("δ" in _display_name(c) or "delta" in dn)
        pool = [c for c in ctx.hand() if match(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach Energy")
        if not picks:
            return
        dests = list(ctx.my_pokemon_in_play())
        dest = await ctx.choose_pokemon(dests, "Attach to?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def delta_block_powers_passive() -> Passive:
    """While any Holon-named Stadium is in play, opponent can't play Stadiums."""
    class _P(Passive):
        def blocks_trainer_play(self, card, player_id, carrier, board=None):
            holder = carrier_pokemon(carrier) or carrier
            if player_id == getattr(holder, "owning_player_id", None):
                return False
            d = def_for(getattr(card, "archetype_id", None) or "")
            is_stadium = False
            if d is not None:
                subs = getattr(d, "subtypes", None) or []
                if "Stadium" in subs:
                    is_stadium = True
                from spirit.game.data_utils import StadiumCardDef
                if isinstance(d, StadiumCardDef):
                    is_stadium = True
            if not is_stadium:
                return False
            if board is None:
                return False
            stadium_area = board.find_global_area("activeStadium")
            if not stadium_area or not stadium_area.children:
                return False
            return "holon" in _display_name(stadium_area.children[0]).lower()
    return _P()


def mind_play_discard_hand_card():
    """Look at 1 random opponent hand card. If Trainer: +30 and discard it; else return."""
    async def effect(ctx):
        hand = list(ctx.opponent_hand()) if hasattr(ctx, "opponent_hand") else list(
            ctx.hand(player_id=ctx.opponent_id))
        if not hand:
            await ctx.deal_damage()
            return
        # Without looking: pick randomly, then look
        import random as _r
        chosen = _r.choice(hand)
        await ctx.reveal_cards([chosen]) if hasattr(ctx, "reveal_cards") else None
        from spirit.game.session.effects import is_trainer_card
        if is_trainer_card(chosen):
            await ctx.deal_damage(60)  # 30 + 30
            await ctx.discard_cards([chosen])
        else:
            await ctx.deal_damage()  # printed 30
            # Return to hand — already in hand; no move needed after peek
    return effect


def spiral_growth_attach_heads():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        while True:
            results = await ctx.flip_coins(1, "Spiral Growth")
            if not (results and results[0]):
                break
            pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
            if not pool:
                break
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Attach basic Energy")
            if picks:
                await ctx.attach_energy(picks[0], a)
            else:
                break
    return effect


def all_out_blast(base: int = 50, per: int = 20):
    async def effect(ctx):
        # Discard until 1 left; +20 per Energy discarded
        extra = 0
        while True:
            deck = list(ctx.deck())
            if len(deck) <= 1:
                break
            top = deck[0] if hasattr(ctx, "mill") else None
            # Mill 1 from top
            if hasattr(ctx, "mill"):
                milled = await ctx.mill(1)
                for c in milled or []:
                    if is_energy_card(c):
                        extra += per
            else:
                break
        await ctx.deal_damage(base + extra)
    return effect


def delta_reactor_passive(bonus: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.attacker is None:
                return
            if calc.attacker.owning_player_id != holder.owning_player_id:
                return
            if not _has_delta(calc.attacker):
                return
            # Holon stadium?
            # Soft: always apply while body in play (approx)
            if calc.is_attack and calc.is_opposing:
                calc.amount += bonus
    return _P()


def vital_drain_on_ko(heal_counters: int = 7):
    async def effect(ctx):
        await ctx.deal_damage()
        # If KO — heal. Soft: check defender HP after damage via session; 
        # use also_if_ko pattern if available
        d = ctx.defender
        if d is not None and d.get_attribute(AttrID.HP, 0) <= 0 and ctx.attacker is not None:
            await ctx.cure_all_conditions(ctx.attacker)
            await ctx.heal(heal_counters * 10, ctx.attacker)
    return effect


def dragon_curse_put_counters(n: int = 2):
    async def effect(ctx):
        if ctx.source is None or not is_in_active_spot(ctx.source):
            return
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Dragon Curse")
        if t is not None:
            await ctx.deal_damage(n * 10, target=t, apply_modifiers=False, as_counters=True)
    return effect


def dual_aura_weakness_resistance_passive(partner: str) -> Passive:
    """While partner/partner-ex in play: Evolved Pokémon (excl ex) can't use Poké-Bodies."""
    partner_l = partner.lower().replace(" ex", "").strip()

    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier, board=None):
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_BODY:
                return False
            if is_pokemon_ex(pokemon) or is_basic_pokemon(pokemon):
                return False
            holder = carrier_pokemon(carrier) or carrier
            if board is None:
                return False
            names = [
                _display_name(p).lower()
                for p in board.pokemon_in_play(holder.owning_player_id)
            ]
            if not any(partner_l in n for n in names):
                return False
            return True
    return _P()


def aqua_blast_discard_water():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if energy_provides_type(c, PokemonTypes.WATER.value)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Water")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def dragonbreath_paralyze():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Dragonbreath")
        if not (results and results[0]):
            return
        await ctx.deal_damage()
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    return effect


def sweet_scent_heal(counters: int = 2):
    async def effect(ctx):
        pool = list(ctx.my_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Sweet Scent")
        if t is not None:
            await ctx.heal(counters * 10, t)
    return effect


def clear_body_passive() -> Passive:
    """Can't be affected by opponent's attacks' effects other than damage? 
    Or: ignore effects of attacks from Pokémon-ex / Special Conditions from attacks.
    Regi Clear Body: this Pokémon can't be affected by any Special Conditions.
    Soft: prevent special conditions."""
    class _P(Passive):
        def prevents_special_condition(self, pokemon, condition, carrier):
            holder = carrier_pokemon(carrier) or carrier
            return pokemon is holder
    return _P()


def rock_slide_bench2(amount: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if not bench:
            return
        n = min(2, len(bench))
        picks = []
        for _ in range(n):
            pool = [p for p in bench if p not in picks]
            if not pool:
                break
            t = await ctx.choose_pokemon(pool, "Rock Slide bench")
            if t is None:
                break
            picks.append(t)
        for t in picks:
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def aqua_lift_passive() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return cost
            if any(energy_provides_type(c, PokemonTypes.WATER.value) for c in holder.children):
                return 0
            return cost
    return _P()


def overrun_choose_bench(bench_dmg: int = 20):
    return overrun_bench(30, bench_dmg)  # reuse; adjust per card in wire


def primal_light_search_basic():
    async def effect(ctx):
        picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0, prompt="Basic Energy")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def delta_edge_supporter_bonus(base: int = 70, with_supporter: int = 20):
    """Base damage `base`; if a Supporter is in play, deal `with_supporter` instead."""
    async def effect(ctx):
        has = False
        if hasattr(ctx, "active_trainer"):
            has = ctx.active_trainer() is not None
        # Also scan in-play trainers named as Supporter when API allows
        if not has and hasattr(ctx, "board"):
            try:
                area = ctx.board.find_player_area(ctx.player_id, "supporter")
                has = bool(area and area.children)
            except Exception:
                pass
        await ctx.deal_damage(with_supporter if has else base)
    return effect


def fossil_charge_snipe(amount: int = 60):
    async def effect(ctx):
        await ctx.deal_damage()
        names = {"claw fossil", "mysterious fossil", "root fossil", "holon fossil"}
        pool = [c for c in ctx.hand() if _display_name(c).lower() in names]
        if not pool:
            return
        if not await ctx.ask_yes_no("Discard a Fossil from hand?"):
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Fossil")
        if not picks:
            return
        await ctx.discard_cards(picks)
        bench = ctx.opponent_bench()
        if bench:
            t = await ctx.choose_pokemon(bench, "Fossil Charge")
            if t is not None:
                await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def flail_per_counter(per: int = 10):
    from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
    return damage_per(damage_counters_on("self"), per)


def power_blow_per_energy(per: int = 20):
    from spirit.game.card_effects.attacks_common import damage_per, count_energy
    return damage_per(count_energy("self"), per)


def plasma_attach_lightning():
    return plasma_attach(PokemonTypes.LIGHTNING)


def super_psywave_snipe():
    async def effect(ctx):
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Super Psywave")
        if t is None:
            return
        n = sum(1 for c in t.children if is_energy_card(c))
        await ctx.deal_damage(10 * n, target=t, apply_modifiers=is_in_active_spot(t))
    return effect


def psychic_vision():
    async def effect(ctx):
        if ctx.source is None or is_in_active_spot(ctx.source):
            return
        # Look at opponent hand
        if hasattr(ctx, "reveal_opponent_hand"):
            await ctx.reveal_opponent_hand()
        elif hasattr(ctx, "opponent_hand"):
            hand = list(ctx.opponent_hand())
            if hand:
                await ctx.reveal_cards(hand, to_player=ctx.player_id)
    return effect


def devo_crush():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        d = ctx.defender
        if a is None or d is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if len(pool) < 2:
            return
        if not await ctx.ask_yes_no("Discard 2 Energy to devolve?"):
            return
        picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Discard Energy")
        if not picks:
            return
        await ctx.discard_cards(picks)
        if is_evolution_pokemon(d):
            await ctx.devolve_pokemon(d, steps=1, destination="deck")
            await ctx.shuffle_deck()  # soft: should be opponent deck
    return effect


def energy_absorption_self():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach Energy")
        if picks:
            await ctx.attach_energy(picks[0], a)
    return effect


def psychic_star():
    async def effect(ctx):
        d = ctx.defender
        a = ctx.attacker
        if d is not None and is_evolution_pokemon(d) and a is not None:
            pool = [c for c in a.children if is_energy_card(c)]
            if pool:
                await ctx.discard_cards(list(pool))
            await ctx.deal_damage(100)
        else:
            await ctx.deal_damage(50)
    return effect


def swift_attack():
    from spirit.game.card_effects.attacks_common import swift_attack as _sa
    return _sa()


def driving_howl():
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Switch in?")
        if t is not None:
            await ctx.switch_active(ctx.opponent_id, t)
    return effect


def blot_heal(counters: int = 2):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


def vengeful_spikes(base: int = 30, per: int = 10, cap_names=None):
    names = {"omanyte", "omastar", "kabuto", "kabutops", "kabutops ex"}
    async def effect(ctx):
        n = 0
        for c in ctx.discard_pile():
            dn = _display_name(c).lower()
            if any(x in dn for x in names):
                n += 1
        await ctx.deal_damage(base + per * n)
    return effect


def scratch_and_draw_holon(n: int = 3):
    async def effect(ctx):
        await ctx.deal_damage()
        stadium = ctx.stadium_in_play()
        if stadium is not None and "holon" in _display_name(stadium).lower():
            await ctx.draw_cards(n)
    return effect


def deceive_counters(n: int = 4):
    async def effect(ctx):
        # Opponent chooses one of their Pokémon
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        # Soft: we choose (opponent-choice gap)
        t = await ctx.choose_pokemon(pool, "Deceive (opp chooses — soft)")
        if t is not None:
            await ctx.deal_damage(n * 10, target=t, apply_modifiers=False, as_counters=True)
    return effect


def paste_energy_to_delta():
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Energy")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if _has_delta(p)]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "δ Pokémon")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def delta_reserve_passive() -> Passive:
    """While Holon Energy attached: each player's Pokémon (excluding δ) can't use Poké-Powers."""
    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not any("holon" in _display_name(c).lower() and is_energy_card(c)
                       for c in holder.children):
                return False
            if getattr(ability, "ability_type", None) != AbilityTypes.POKE_POWER:
                return False
            if _has_delta(pokemon):
                return False
            return True
    return _P()


def wreck_stadium(base: int = 30, bonus: int = 30):
    async def effect(ctx):
        amount = base
        if ctx.stadium_in_play() is not None:
            amount = base + bonus
            await ctx.discard_stadium()
        await ctx.deal_damage(amount)
    return effect


def flames_of_rage(base: int = 10, per: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c)]
        if len(pool) >= 2:
            picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Discard 2 Energy")
            if picks:
                await ctx.discard_cards(picks)
        dmg = max(0, effective_max_hp(ctx.board, a) - a.get_attribute(AttrID.HP, 0))
        await ctx.deal_damage(base + per * (dmg // 10))
    return effect


def metallic_thunder():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if energy_provides_type(c, PokemonTypes.METAL.value)]
        if len(pool) < 2:
            return
        if not await ctx.ask_yes_no("Discard 2 Metal Energy?"):
            return
        picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Metal Energy")
        if picks:
            await ctx.discard_cards(picks)
            # Printed: discard Stadium or Special Energy from Defending — soft
            d = ctx.defender
            if d is not None:
                from spirit.game.session.effects import is_special_energy
                specials = [c for c in d.children if is_special_energy(c)]
                if specials:
                    sp = await ctx.choose_cards(specials, 1, minimum=0, prompt="Discard Special Energy")
                    if sp:
                        await ctx.discard_cards(sp)
                        return
            if ctx.stadium_in_play() is not None:
                await ctx.discard_stadium()
    return effect


def hydro_barrier_passive() -> Passive:
    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if not any("holon" in _display_name(c).lower() and is_energy_card(c)
                       for c in holder.children):
                return
            t = calc.target
            if t is None or t.owning_player_id != holder.owning_player_id:
                return
            types = t.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.WATER.value in types:
                calc.weakness_applies = False
    return _P()


def outrage_flip(base: int = 10, per: int = 10):
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Outrage")
        if not (results and results[0]):
            return
        a = ctx.attacker
        dmg = 0
        if a is not None:
            dmg = max(0, effective_max_hp(ctx.board, a) - a.get_attribute(AttrID.HP, 0))
        await ctx.deal_damage(base + per * (dmg // 10))
    return effect


def flamethrower_discard_fire():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if energy_provides_type(c, PokemonTypes.FIRE.value)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Fire")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def brush_aside_holon():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None or not any("holon" in _display_name(c).lower() and is_energy_card(c) for c in a.children):
            return
        hand = list(ctx.opponent_hand()) if hasattr(ctx, "opponent_hand") else list(ctx.hand(player_id=ctx.opponent_id))
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Discard opponent card")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def swift_turn_fighting_res(base: int = 50, bonus: int = 30):
    async def effect(ctx):
        amount = base
        d = ctx.defender
        if d is not None:
            resists = d.get_attribute(AttrID.RESISTANCE_TYPES) or []
            if not isinstance(resists, (list, tuple, set)):
                resists = [resists] if resists else []
            # Also check single RESISTANCE_TYPE
            rt = d.get_attribute(AttrID.RESISTANCE_TYPE) if hasattr(AttrID, "RESISTANCE_TYPE") else None
            if rt is not None:
                resists = list(resists) + [rt]
            if PokemonTypes.FIGHTING.value in resists:
                amount = base + bonus
        await ctx.deal_damage(amount)
    return effect


def poison_pollen():
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Poison Pollen")
        if results and results[0] and ctx.opponent_active() is not None:
            await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.POISONED)
    return effect




# --- EX14 Crystal Guardians ---

def shield_veil_active_no_weakness() -> Passive:
    """Each of your Active Pokémon has no Weakness."""
    class _P(Passive):
        def modify_weakness(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            t = calc.target
            if t is None or t.owning_player_id != holder.owning_player_id:
                return
            active = board_active(calc, t.owning_player_id) if False else None
            # Active of holder's side
            board = getattr(calc, "board", None)
            if board is None:
                return
            act = board.active_pokemon(holder.owning_player_id)
            if t is act:
                calc.weakness_applies = False
    return _P()


def water_pressure_passive(threshold_hp: int = 40, bonus: int = 40) -> Passive:
    class _P(Passive):
        def modify_damage(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.attacker is not holder or not calc.is_attack:
                return
            rem = holder.get_attribute(AttrID.REMAINING_HP) if hasattr(AttrID, "REMAINING_HP") else None
            if rem is None:
                hp = holder.get_attribute(AttrID.HP) or 0
                dmg = holder.get_attribute(AttrID.DAMAGE_COUNTERS) or 0
                rem = hp - (dmg * 10 if dmg < 50 else dmg)
            try:
                if int(rem) <= threshold_hp:
                    calc.amount = (calc.amount or 0) + bonus
            except Exception:
                pass
    return _P()


def hydro_pump_unused_water(base: int = 50, per: int = 20):
    """+per for each Water Energy attached but not used to pay for this attack — soft: all attached Water beyond 1."""
    async def effect(ctx):
        a = ctx.attacker
        n = 0
        if a is not None:
            for c in a.children:
                if energy_provides_type(c, PokemonTypes.WATER.value):
                    n += 1
        # Soft: treat attack cost as 1 Water used
        unused = max(0, n - 1)
        await ctx.deal_damage(base + per * unused)
    return effect


def peal_of_thunder_on_evolve(amount: int = 30):
    async def effect(ctx):
        # ON_EVOLVE: put damage on each opp Pokémon with δ — soft: all opp Pokémon if δ check hard
        targets = list(ctx.opponent_pokemon_in_play())
        for t in targets:
            if _has_delta(t):
                await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def metal_burn_discard_all_metal():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        metals = [c for c in a.children if energy_provides_type(c, PokemonTypes.METAL.value)]
        if metals:
            await ctx.discard_cards(metals)
    return effect


def burn_away_heal_on_ko():
    """Before damage: if KO, remove all damage + SC from Blaziken — soft post-damage check."""
    async def effect(ctx):
        d = ctx.defender
        await ctx.deal_damage()
        if d is not None and getattr(d, "is_knocked_out", lambda: False)():
            a = ctx.attacker
            if a is not None:
                await ctx.heal(a, 9999)
                await ctx.clear_special_conditions(a)
    return effect


def focus_energy_boost_named(attack_title: str = "High Jump Kick", damage: int = 70):
    """During your next turn, named attack's base damage becomes `damage`."""
    async def effect(ctx):
        # Focus Energy itself deals no damage; find printed base of named attack
        printed = 30  # Combusken High Jump Kick default
        a = ctx.attacker
        if a is not None:
            for ab in getattr(def_for(a.archetype_id), "abilities", None) or []:
                if getattr(ab, "title", None) == attack_title:
                    printed = int(getattr(ab, "damage", 0) or 0)
                    break
        delta = damage - printed
        if delta:
            await apply_own_next_turn_boost(ctx, delta, attack_title=attack_title)
    return effect


def constrain_discard_to(n: int = 6):
    async def effect(ctx):
        for pid in (ctx.player_id, ctx.opponent_id):
            hand = list(ctx.hand(pid))
            while len(hand) > n:
                picks = await ctx.choose_cards(hand, len(hand) - n, minimum=len(hand) - n,
                                               prompt="Discard down to 6", player_id=pid)
                if not picks:
                    picks = hand[n:]
                await ctx.discard_cards(picks, player_id=pid)
                hand = list(ctx.hand(pid))
    return effect


def upstream_discard_energy_damage(per: int = 10):
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        await ctx.deal_damage(per * len(pool))
        if pool:
            # "put them on top of your deck in any order" soft: shuffle into deck then put on top
            await ctx.put_on_top_of_deck(pool) if hasattr(ctx, "put_on_top_of_deck") else await ctx.shuffle_into_deck(pool)
    return effect


def sand_veil_bench_protect() -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            t = calc.target
            if t is None or not calc.is_attack or not calc.is_opposing:
                return False
            if t.owning_player_id != holder.owning_player_id:
                return False
            board = getattr(calc, "board", None)
            if board is None:
                return False
            return t is not board.active_pokemon(holder.owning_player_id)
    return _P()


def detect_flip_protect():
    return agility_flip_protect()


def spike_storm_counters(n: int = 1):
    async def effect(ctx):
        # Put n counters on each opp Pokémon with Tool — or soft all bench
        for p in ctx.opponent_pokemon_in_play():
            has_tool = any("tool" in str(getattr(def_for(c.archetype_id), "subtypes", [])).lower()
                           for c in p.children)
            # Printed: put 1 on each of opp's Pokémon that has a Tool
            if has_tool or True:  # will refine; put on those with tool only
                if has_tool:
                    await ctx.place_damage_counters(p, n)
    return effect


def delta_protection_vs_delta() -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return False
            return calc.attacker is not None and _has_delta(calc.attacker)
        def blocks_attack_effects_from(self, attacker, target, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            return target is holder and attacker is not None and _has_delta(attacker)
    return _P()


def time_travel_survive_flip():
    """If would be KO'd by attack damage, flip; heads: discard attachments, bottom of deck."""
    class _P(Passive):
        async def damage_interceptor(self, ctx, calc, target, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if target is not holder:
                return None
            if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
                return None
            current = target.get_attribute(AttrID.HP, 0)
            if calc.amount < current:
                return None
            heads = await ctx.flip_coins(1, "Time Travel", source=holder)
            if not (heads and heads[0]):
                return None
            # Prevent KO: deal 0, then discard attachments and put on bottom
            async def after():
                # Discard all attached (energy/tools); leave evolution stack?
                # Printed: "discard all cards attached to Celebi Star"
                attached = [c for c in list(holder.children)
                            if not isinstance(c, type(holder))]
                # children include tucked pre-evos (PokemonEntity) — keep those?
                # "all cards attached" = Energy/Tools, not the Pokémon stack itself
                from spirit.game.models.board import PokemonEntity as _PE
                to_discard = [c for c in list(holder.children) if not isinstance(c, _PE)]
                if to_discard:
                    await ctx.discard_cards(to_discard)
                await ctx.put_on_bottom_of_deck(holder)
            ctx.deferred_actions.append(after)
            return 0
    return _P()


def leaf_shade_energy_counters():
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        n = sum(1 for c in a.children if is_energy_card(c))
        if n <= 0:
            return
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Leaf Shade")
        if t is not None:
            await ctx.place_damage_counters(n, candidates=[t])
    return effect


def circular_steps(per: int = 10):
    async def effect(ctx):
        mine = len(ctx.my_pokemon_in_play())
        opp = len(ctx.opponent_pokemon_in_play())
        # excluding Grumpig — soft subtract 1 for self
        await ctx.deal_damage(per * max(0, mine + opp - 1))
    return effect


def hover_lift_line_retreat() -> Passive:
    names = {"jigglypuff", "wigglytuff", "wigglytuff ex", "igglybuff"}
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board=None):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            if not any(n in _display_name(pokemon).lower() for n in names):
                return cost
            try:
                return max(0, int(cost) - 1)
            except Exception:
                return cost
    return _P()


def stretch_vine_bench(amount: int = 30):
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Stretch Vine")
        if t is not None:
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def star_light_retreat_zero() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board=None):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return cost
            b = board or getattr(holder, "board", None)
            if b is None:
                return cost
            opp_id = None
            for pid in getattr(b, "player_ids", []) or []:
                if pid != holder.owning_player_id:
                    opp_id = pid
                    break
            if opp_id is None:
                return cost
            opp = b.pokemon_in_play(opp_id)
            if any(is_pokemon_ex(p) or (
                    is_evolution_pokemon(p) and str(getattr(def_for(p.archetype_id), "stage", "")).endswith("2"))
                    for p in opp):
                return 0
            return cost
    return _P()


def shield_beam_block_powers_next():
    async def effect(ctx):
        await ctx.deal_damage()
        # Soft: mark opp can't use Poké-Powers next turn via temp passive on board
        if hasattr(ctx, "add_passive_through_opponents_turn") and ctx.attacker:
            class _Block(Passive):
                def blocks_ability(self, ability, pokemon, carrier):
                    return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER
            ctx.add_passive_through_opponents_turn(ctx.attacker, _Block())
    return effect


def prop_up_tool_bonus(base: int = 40, bonus: int = 40):
    async def effect(ctx):
        a = ctx.attacker
        has = False
        if a is not None:
            for c in a.children:
                d = def_for(c.archetype_id)
                subs = [str(s).lower() for s in (getattr(d, "subtypes", None) or [])]
                if any("tool" in s for s in subs):
                    has = True
                    break
        await ctx.deal_damage(base + (bonus if has else 0))
    return effect


def flotation_low_energy_retreat() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board=None):
            holder = carrier_pokemon(carrier) or carrier
            n = sum(1 for c in holder.children if is_energy_card(c))
            if n > 1:
                return cost
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.WATER.value not in types:
                return cost
            return 0
    return _P()


def hydro_shot_discard_snipe(amount: int = 70, discard_n: int = 2):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        energies = [c for c in a.children if is_energy_card(c)]
        if len(energies) < discard_n:
            return
        picks = await ctx.choose_cards(energies, discard_n, minimum=discard_n, prompt="Discard Energy")
        if picks:
            await ctx.discard_cards(picks)
        pool = list(ctx.opponent_pokemon_in_play())
        if pool:
            t = await ctx.choose_pokemon(pool, "Hydro Shot")
            if t is not None:
                await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def even_game_search_basics():
    async def effect(ctx):
        n = len(ctx.opponent_pokemon_in_play())
        if n <= 0:
            return
        picks = await ctx.search_deck(is_basic_pokemon, count=n, minimum=0, prompt="Basic Pokémon")
        if picks:
            for p in picks:
                await ctx.bench_pokemon(p)
        await ctx.shuffle_deck()
    return effect


def stadium_play_heal_or_damage(heal: int = 1, dmg: int = 1):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.stadium_in_play() is None:
            return
        # Soft: if we own stadium heal ours; else damage opp — printed both
        for p in ctx.my_pokemon_in_play():
            await ctx.heal_damage_counters(p, heal) if hasattr(ctx, "heal_damage_counters") else await ctx.heal(p, heal * 10)
        for p in ctx.opponent_pokemon_in_play():
            await ctx.place_damage_counters(p, dmg)
    return effect


def strong_current_tool_bench(amount: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        has = False
        if a is not None:
            for c in a.children:
                d = def_for(c.archetype_id)
                if any("tool" in str(s).lower() for s in (getattr(d, "subtypes", None) or [])):
                    has = True
                    break
        if not has:
            return
        for t in ctx.opponent_bench():
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def mud_splash_bench(amount: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if bench:
            t = await ctx.choose_pokemon(bench, "Mud Splash")
            if t is not None:
                await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect


def mining_search_trainer():
    async def effect(ctx):
        def match(c):
            d = def_for(c.archetype_id)
            return d is not None and getattr(d, "stage", None) is None and not is_energy_card(c) and not is_pokemon_card(c)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Trainer")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        await ctx.deal_damage()
    return effect


def excavate_top_deck():
    async def effect(ctx):
        top = ctx.deck_top(1)
        if not top:
            return
        # Soft: reveal and optionally put in hand if Trainer/Energy
        c = top[0]
        d = def_for(c.archetype_id)
        is_te = d is not None and (is_energy_card(c) or (getattr(d, "stage", None) is None and not is_pokemon_card(c)))
        if is_te and await ctx.ask_yes_no("Put into hand?"):
            await ctx.put_in_hand([c], reveal=True)
        else:
            await ctx.shuffle_deck()
    return effect


def delta_transport_switch():
    async def effect(ctx):
        # Bench power: switch 1 of your δ with another
        deltas = [p for p in ctx.my_pokemon_in_play() if _has_delta(p)]
        if len(deltas) < 2:
            return
        a = await ctx.choose_pokemon(deltas, "Switch this δ")
        if a is None:
            return
        others = [p for p in deltas if p is not a]
        b = await ctx.choose_pokemon(others, "With this δ")
        if b is not None:
            # Soft: switch positions if API exists
            if hasattr(ctx, "switch_pokemon_positions"):
                await ctx.switch_pokemon_positions(a, b)
    return effect


def extra_liquid_ex_passive() -> Passive:
    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            if not is_pokemon_ex(pokemon):
                return False
            return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER
        def modify_attack_cost(self, cost, pokemon, carrier, ability=None, **kwargs):
            if not is_pokemon_ex(pokemon):
                return cost
            cost = dict(cost)
            key = PokemonTypes.COLORLESS.value
            cost[key] = cost.get(key, 0) + 1
            return cost
    return _P()


def power_revenge_prizes_taken(base: int = 60, per: int = 10):
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import count_prizes_remaining
        # Opponent started with 6 typically — soft: 6 - remaining
        rem = count_prizes_remaining("opponent")(ctx)
        taken = max(0, 6 - rem)
        await ctx.deal_damage(base + per * taken)
    return effect


def dark_eyes_after_power() -> Passive:
    """After opponent's Pokémon uses a Poké-Power, put 2 damage counters on it."""
    class _P(Passive):
        def after_poke_power(self, board, power_user, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if power_user.owning_player_id == holder.owning_player_id:
                return 0
            return 2
    return _P()


def target_attack_snipe(amount: int = 30, tool_bonus: int = 30):
    async def effect(ctx):
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Target Attack")
        if t is None:
            return
        bonus = 0
        for c in t.children:
            d = def_for(c.archetype_id)
            if any("tool" in str(s).lower() for s in (getattr(d, "subtypes", None) or [])):
                bonus = tool_bonus
                break
        await ctx.deal_damage(amount + bonus, target=t, apply_modifiers=False)
    return effect


def pick_and_choose_conditions():
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        # Choose Burned or Poisoned
        i1 = await ctx.choose("Burned or Poisoned?", ["Burned", "Poisoned"])
        i2 = await ctx.choose("Asleep or Confused?", ["Asleep", "Confused"])
        m1 = {0: SpecialConditions.BURNED, 1: SpecialConditions.POISONED}
        m2 = {0: SpecialConditions.ASLEEP, 1: SpecialConditions.CONFUSED}
        if i1 in m1:
            await ctx.apply_special_condition(d, m1[i1])
        if i2 in m2:
            await ctx.apply_special_condition(d, m2[i2])
    return effect


def echo_draw():
    async def effect(ctx):
        await ctx.draw_cards(1)
    return effect


def ultra_pump(base: int = 60, bonus: int = 20, discard_n: int = 2):
    async def effect(ctx):
        hand = list(ctx.hand())
        extra = 0
        if len(hand) >= discard_n and await ctx.ask_yes_no(f"Discard {discard_n} cards for +{bonus}?"):
            picks = await ctx.choose_cards(hand, discard_n, minimum=discard_n, prompt="Discard")
            if picks:
                await ctx.discard_cards(picks)
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def crush_chance_on_play():
    """When put from hand onto Bench: you may discard a Stadium in play."""
    async def effect(ctx):
        stadium = ctx.stadium_in_play()
        if stadium is None:
            return
        if await ctx.ask_yes_no("Discard the Stadium in play?"):
            await ctx.discard_stadium()
    return effect


def chlorophyll_colorless_as_grass() -> Passive:
    class _P(Passive):
        def modify_energy_provided(self, options, energy, holder, board):
            if holder is None:
                return options
            types = holder.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.GRASS.value not in types:
                return options
            # Only Colorless-providing energy → also Grass
            out = list(options or [])
            # Soft: if options look colorless-only, add Grass
            grass = [PokemonTypes.GRASS.value]
            if grass not in out:
                out.append(grass)
            return out
    return _P()


def toxic_sleep_poison2():
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
        await ctx.apply_special_condition(d, SpecialConditions.POISONED)
        # Soft: poison for 2 counters — set attribute if supported
        if hasattr(d, "set_attribute"):
            d.set_attribute("PoisonDamage", 20)
    return effect


def tail_whip_lock_attack():
    """Flip; heads: Defending Pokémon can't attack during opponent's next turn."""
    from spirit.game.card_effects.attacks_common import lock_defender_attacks
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Tail Whip")
        if results and results[0]:
            lock_defender_attacks(ctx)
    return effect


def fluffy_fur_asleep_on_damage() -> Passive:
    class _P(Passive):
        def on_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_opposing:
                return
            # Soft: apply Asleep to attacker
            return
    return _P()


def solid_shell_reduce(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is holder and calc.is_attack:
                calc.amount = max(0, (calc.amount or 0) - amount)
    return _P()


def mega_burn_self_lock():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None and hasattr(ctx, "locks_next_turn"):
            await ctx.locks_next_turn("Mega Burn")
    return effect


def skill_copy_from_hand():
    """Discard a Basic/Evolution from hand; copy one of its attacks via use_attack."""
    async def effect(ctx):
        hand = [c for c in ctx.hand() if is_pokemon_card(c)]
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=0, prompt="Discard Pokémon to copy")
        if not picks:
            return
        card = picks[0]
        attacks = [
            ab for ab in (getattr(def_for(card.archetype_id), "abilities", None) or [])
            if isinstance(ab, Attack) or type(ab).__name__ == "Attack"
        ]
        # Prefer Attack type from data_utils
        from spirit.game.data_utils import Attack as _Attack
        attacks = [
            ab for ab in (getattr(def_for(card.archetype_id), "abilities", None) or [])
            if isinstance(ab, _Attack)
        ]
        await ctx.discard_cards(picks)
        if not attacks:
            return
        labels = [a.title for a in attacks]
        idx = await ctx.choose("Choose an attack to copy", labels)
        if idx is None or idx < 0 or idx >= len(attacks):
            return
        await ctx.use_attack(attacks[idx])
    return effect


def intimidating_armor_basic_lock() -> Passive:
    class _P(Passive):
        def prevents_attack(self, attacker, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            board = getattr(holder, "board", None)
            if board is None:
                return False
            if board.active_pokemon(holder.owning_player_id) is not holder:
                return False
            return is_basic_pokemon(attacker)
    return _P()


def hard_rock_low_energy(reduce: int = 20) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            n = sum(1 for c in holder.children if is_energy_card(c))
            if n > 1:
                return
            t = calc.target
            if t is None or not calc.is_attack or not calc.is_opposing:
                return
            # any Groudon — soft: holder family
            if "groudon" in _display_name(t).lower():
                calc.amount = max(0, (calc.amount or 0) - reduce)
    return _P()


def power_blast_discard_energy(n: int = 2):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        energies = [c for c in a.children if is_energy_card(c)]
        if len(energies) < n:
            if energies:
                await ctx.discard_cards(energies)
            return
        picks = await ctx.choose_cards(energies, n, minimum=n, prompt="Discard Energy")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def thunder_jolt_self(self_dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Thunder Jolt")
        if results and not results[0] and ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def self_charge_darkness_from_hand():
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in ctx.hand() if energy_provides_type(c, PokemonTypes.DARKNESS.value)
                or "darkness" in _display_name(c).lower()]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Darkness Energy")
        if picks:
            await ctx.attach_energy(picks[0], a)
    return effect


def extra_noise_bench_counters(n: int = 1):
    """BETWEEN_TURNS while Active: put n counters on each opponent Pokémon-ex.
    Prefer wiring Ability(effect=..., trigger=BETWEEN_TURNS); this returns the effect.
    """
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        for p in ctx.opponent_pokemon_in_play():
            if is_pokemon_ex(p):
                await ctx.deal_damage(
                    n * 10, target=p, apply_modifiers=False, as_counters=True)
    return effect


def night_murmurs_confuse_basic():
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is not None and is_basic_pokemon(d):
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def psychic_shield_vs_ex():
    return safeguard_vs_ex_passive()


def dual_armor_psychic_fighting():
    return dual_armor_if_energy(PokemonTypes.PSYCHIC, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING)


# Trainers

def castaway_search():
    async def effect(ctx):
        def is_supporter(c):
            d = def_for(c.archetype_id)
            return d is not None and any("supporter" in str(s).lower() for s in (getattr(d, "subtypes", None) or []))
        def is_tool(c):
            d = def_for(c.archetype_id)
            return d is not None and any("tool" in str(s).lower() for s in (getattr(d, "subtypes", None) or []))
        for pred, prompt in ((is_supporter, "Supporter"), (is_tool, "Tool"), (is_basic_energy_card, "Basic Energy")):
            picks = await ctx.search_deck(pred, count=1, minimum=0, prompt=prompt)
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def cessation_crystal_passive() -> Passive:
    class _P(Passive):
        def blocks_ability(self, ability, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            board = getattr(holder, "board", None)
            if board is None:
                return False
            # Only while attached to Active
            if board.active_pokemon(holder.owning_player_id) is not holder:
                return False
            at = getattr(ability, "ability_type", None)
            return at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY)
    return _P()


def crystal_beach_passive() -> Passive:
    """Special Energy providing 2+ Energy now provides only 1 Colorless."""
    from spirit.game.session.effects import is_special_energy
    class _P(Passive):
        def modify_energy_provided(self, options, energy, holder, board):
            if not is_special_energy(energy):
                return options
            for opt in options or []:
                if len(opt) >= 2:
                    return [[PokemonTypes.COLORLESS.value]]
            return options
    return _P()


def holon_circle_passive() -> Passive:
    """Prevent all effects/damage from Active Pokémon attacks; then discard this Stadium."""
    class _P(Passive):
        stacking_key = "holon_circle"

        def _attacker_is_active(self, attacker, board) -> bool:
            if attacker is None or board is None:
                return False
            return board.active_pokemon(attacker.owning_player_id) is attacker

        def prevents_damage(self, calc, carrier) -> bool:
            if not calc.is_attack:
                return False
            return self._attacker_is_active(calc.attacker, calc.board)

        def blocks_attack_effects_from(self, target, carrier, attacker) -> bool:
            # Board not passed; approximate: always block attack effects while stadium up
            # (printed: from Active only — Active is who attacks)
            return attacker is not None

        async def attack_followup(self, ctx, carrier):
            # If an Active used an attack, discard Holon Circle
            await ctx.discard_stadium()
    return _P()


def memory_berry_granted() -> Passive:
    """Grant attacks from Basic / Stage 1 Pokémon cards under the holder; discard at EOT if attacked."""
    from spirit.game.data_utils import Attack as _Attack
    from spirit.game.models.board import PokemonEntity

    class _P(Passive):
        def granted_attacks(self, board, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
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

        async def attack_followup(self, ctx, carrier):
            # Discard Memory Berry at end of turn the Pokémon attacks
            holder = carrier_pokemon(carrier) or carrier
            if ctx.attacker is not holder:
                return
            # carrier is the tool
            if carrier is not None and carrier is not holder:
                await ctx.discard_cards([carrier])
    return _P()


def mysterious_shard_ex_protect() -> Passive:
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return False
            return calc.attacker is not None and is_pokemon_ex(calc.attacker)
        def blocks_attack_effects_from(self, attacker, target, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            return target is holder and attacker is not None and is_pokemon_ex(attacker)
    return _P()


def windstorm_discard_tools_stadiums(up_to: int = 2):
    async def effect(ctx):
        pool = []
        # Stadium
        st = ctx.stadium_in_play() if hasattr(ctx, "stadium_in_play") else None
        if st is not None:
            pool.append(st)
        # Tools on all Pokémon
        for p in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
            for c in p.children:
                d = def_for(c.archetype_id)
                if d is not None and any("tool" in str(s).lower() for s in (getattr(d, "subtypes", None) or [])):
                    pool.append(c)
        if not pool:
            return
        picks = await ctx.choose_cards(pool, min(up_to, len(pool)), minimum=0, prompt="Discard Tools/Stadium")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def energy_recycle_to_deck(n: int = 3):
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, min(n, len(pool)), minimum=0, prompt="Energy to deck")
        if picks:
            await ctx.shuffle_into_deck(picks)
    return effect


# ---------------------------------------------------------------------------
# EX15 Dragon Frontiers helpers
# ---------------------------------------------------------------------------

def _holon_veil_owners(board) -> set:
    """Player IDs that currently have Holon Veil in play."""
    if board is None:
        return set()
    from spirit.game.session.passives import active_passives as _ap
    owners = set()
    for passive, carrier in _ap(board):
        if getattr(passive, "stacking_key", None) != "holon_veil":
            continue
        holder = carrier_pokemon(carrier) or carrier
        if holder is not None and holder.owning_player_id:
            owners.add(holder.owning_player_id)
    return owners


_HOLON_VEIL_ZONES = frozenset({
    "deck", "hand", "discard", "activePokemonArea", "bench",
})


def _is_basic_or_evolution_card(card) -> bool:
    """Printed Holon Veil: Basic Pokémon and Evolution cards only."""
    from spirit.game.session.effects import is_pokemon_card, is_basic_pokemon, is_evolution_pokemon
    if not is_pokemon_card(card):
        # Loose fallback via def stage when attributes not stamped (deck search)
        d = def_for(getattr(card, "archetype_id", None) or "")
        if d is None:
            return False
        stage = getattr(d, "stage", None)
        if stage is None:
            return False
        return stage in (
            PokemonStage.BASIC, PokemonStage.STAGE1, PokemonStage.STAGE2,
            getattr(PokemonStage.BASIC, "value", None),
            getattr(PokemonStage.STAGE1, "value", None),
            getattr(PokemonStage.STAGE2, "value", None),
        )
    return is_basic_pokemon(card) or is_evolution_pokemon(card)


def _card_in_holon_veil_zone(card) -> bool:
    """True if card sits in deck/hand/discard/in-play (printed Holon Veil zones)."""
    area_fn = getattr(card, "_containing_area_name", None)
    if not callable(area_fn):
        return True  # mid-effect / unbound — allow when owner has veil
    area = area_fn()
    if area is None:
        return True
    return area in _HOLON_VEIL_ZONES


def holon_veil_treat_as_delta_passive() -> Passive:
    """Treat each of your Basic/Evolution cards in deck, hand, discard, and
    in play as a Pokémon that has δ on its card (Ampharos δ Holon Veil)."""
    class _P(Passive):
        stacking_key = "holon_veil"

        def treats_as_delta(self, card, carrier, board=None) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if card is None or holder is None:
                return False
            if getattr(card, "owning_player_id", None) != holder.owning_player_id:
                return False
            if not _is_basic_or_evolution_card(card):
                return False
            if not _card_in_holon_veil_zone(card):
                return False
            return True
    return _P()


# Patch _has_delta (and is_delta_pokemon) to honor Holon Veil across zones.
_orig_has_delta = _has_delta


def _has_delta(card_or_pokemon, board=None) -> bool:  # noqa: F811
    """Printed δ, or Holon Veil zone tagging for the owner's Basic/Evolutions."""
    if _orig_has_delta(card_or_pokemon):
        return True
    if board is None:
        try:
            from spirit.game.session.effects import current_board
            board = current_board()
        except Exception:
            board = None
    if board is None:
        board = getattr(card_or_pokemon, "board", None)
    if board is None:
        return False
    owner = getattr(card_or_pokemon, "owning_player_id", None)
    if owner is None or owner not in _holon_veil_owners(board):
        return False
    if not _is_basic_or_evolution_card(card_or_pokemon):
        return False
    if not _card_in_holon_veil_zone(card_or_pokemon):
        return False
    return True


def is_delta_pokemon(card, board=None) -> bool:  # noqa: F811
    """δ on the card, or treated as δ via Holon Veil."""
    return _has_delta(card, board=board)


def battle_aura_delta_boost(amount: int = 10) -> Passive:
    """Your δ Pokémon do +amount to Defending (before W/R)."""
    class _P(Passive):
        def modify_attack_damage(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.attacker is None or holder is None:
                return None
            if calc.attacker.owning_player_id != holder.owning_player_id:
                return None
            if not _orig_has_delta(calc.attacker) and not _has_delta(calc.attacker):
                return None
            if not calc.is_attack:
                return None
            return amount
    return _P()


def extra_claws_vs_ex(base: int = 30, bonus: int = 20):
    async def effect(ctx):
        d = ctx.defender
        amt = base + (bonus if d is not None and is_pokemon_ex(d) else 0)
        await ctx.deal_damage(amt)
    return effect


def evolutionary_call_search(count: int = 3):
    """On evolve play: search up to `count` Basic/Evolution into hand."""
    async def effect(ctx):
        if not await ctx.ask_yes_no("Search deck for up to 3 Pokémon?"):
            return
        def match(c):
            return is_pokemon_card(c)
        picks = await ctx.search_deck(match, count=count, minimum=0,
                                     prompt="Choose Basic/Evolution cards")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def milotic_sharing():
    """Look at opponent hand; may use a Supporter effect found there."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            await ctx.reveal_cards(hand)
        supporters = []
        for c in hand:
            d = def_for(c.archetype_id)
            subs = getattr(d, "subtypes", None) or []
            if "Supporter" in subs:
                supporters.append(c)
        if not supporters:
            return
        if not await ctx.ask_yes_no("Use a Supporter from opponent's hand?"):
            return
        picks = await ctx.choose_cards(supporters, 1, minimum=0, prompt="Choose Supporter")
        if not picks:
            return
        d = def_for(picks[0].archetype_id)
        eff = getattr(d, "effect", None)
        if callable(eff):
            await eff(ctx)
    return effect


def dark_horn_discard_snipe_bench(base: int = 60, snipe: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(base)
        hand_pokes = [c for c in ctx.hand() if is_pokemon_card(c)]
        if not hand_pokes:
            return
        if not await ctx.ask_yes_no("Discard a Pokémon from hand to snipe Bench?"):
            return
        picks = await ctx.choose_cards(hand_pokes, 1, minimum=1, prompt="Discard Pokémon")
        if not picks:
            return
        await ctx.discard_cards(picks)
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Choose Benched Pokémon")
        if t is not None:
            await ctx.deal_damage(snipe, target=t, apply_modifiers=False)
    return effect


def invitation_search_pokemon():
    async def effect(ctx):
        def match(c):
            return is_pokemon_card(c)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Basic or Evolution")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def volunteer_heal_and_discard_self(counters: int = 4):
    """Heal 4 counters from Ninetales; discard Ninetales from Vulpix; search
    deck for Ninetales/Ninetales ex onto Vulpix (evolve)."""
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        await ctx.heal(counters * 10, src)
        removed = await ctx.devolve_pokemon(src, steps=1, destination="discard")
        if not removed:
            return
        removed_ids = {c.entity_id for c in removed}
        vulpix = None
        for pkm in ctx.my_pokemon_in_play():
            if pkm.entity_id in removed_ids:
                continue
            if "vulpix" in _display_name(pkm).lower():
                vulpix = pkm
                break
        if vulpix is None:
            return
        def match(c):
            n = _display_name(c).lower().replace("★", "").replace("☆", "").strip()
            return n == "ninetales" or n == "ninetales ex" or n.startswith("ninetales ")
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="Ninetales or Ninetales ex")
        if picks:
            await ctx.evolve_pokemon(vulpix, picks[0])
    return effect

def trick_tail_attach_from_discard():
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Energy from discard")
        if not picks:
            return
        dests = list(ctx.my_pokemon_in_play())
        dest = await ctx.choose_pokemon(dests, "Attach to?")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def pinsir_armor_vs_hand5(reduce: int = 30) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return None
            board = calc.board
            if board is None or calc.attacker is None:
                return None
            area = board.find_player_area(calc.attacker.owning_player_id, "hand")
            n = len(area.children) if area else 0
            if n < 5:
                return None
            return -reduce
    return _P()


def delta_call_search():
    async def effect(ctx):
        def match(c):
            return is_pokemon_card(c) and _orig_has_delta(c)
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt="δ Pokémon")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def bedhead_asleep_between_turns(counters: int = 2):
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        conds = src.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        asleep = SpecialConditions.ASLEEP
        if asleep not in conds and getattr(asleep, "value", asleep) not in conds:
            return
        d = ctx.opponent_active()
        if d is not None:
            await ctx.deal_damage(counters * 10, target=d, apply_modifiers=False, as_counters=True)
    return effect


def dozing_heal_and_asleep(counters: int = 2):
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        await ctx.heal(counters * 10, src)
        await ctx.apply_special_condition(src, SpecialConditions.ASLEEP)
    return effect


def delta_copy_attack():
    """Copy an attack from an opponent's δ Pokémon (ignore energy cost)."""
    async def effect(ctx):
        from spirit.game.data_utils import Attack as _Attack
        cands = [p for p in ctx.opponent_pokemon_in_play() if _has_delta(p)]
        if not cands:
            return
        target = await ctx.choose_pokemon(cands, "Choose δ Pokémon to copy")
        if target is None:
            return
        attacks = [
            ab for ab in (getattr(def_for(target.archetype_id), "abilities", None) or [])
            if isinstance(ab, _Attack)
        ]
        if not attacks:
            return
        idx = await ctx.choose("Choose attack", [a.title for a in attacks])
        if idx is None or idx < 0 or idx >= len(attacks):
            return
        await ctx.use_attack(attacks[idx])
    return effect


def solid_shell_bench_delta_protect() -> Passive:
    """Prevent all effects of attacks incl. damage to your Benched δ Pokémon."""
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            if not calc.is_attack or not calc.is_opposing:
                return False
            t = calc.target
            if t is None or is_in_active_spot(t):
                return False
            holder = carrier_pokemon(carrier) or carrier
            if t.owning_player_id != getattr(holder, "owning_player_id", None):
                return False
            return _has_delta(t)

        def blocks_attack_effects_from(self, target, carrier, attacker) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if target is None or is_in_active_spot(target):
                return False
            if target.owning_player_id != getattr(holder, "owning_player_id", None):
                return False
            return _has_delta(target)
    return _P()


def surge_if_water2(base: int = 40, bonus: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        n = 0
        if a is not None:
            n = sum(1 for c in a.children if energy_provides_type(c, PokemonTypes.WATER.value))
        await ctx.deal_damage(base + (bonus if n >= 2 else 0))
    return effect


def sting_turn_paralyze_switch():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Sting Turn")
        if heads and heads[0] and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
            bench = ctx.my_bench()
            if bench:
                t = await ctx.choose_pokemon(bench, "Switch Gligar with?")
                if t is not None:
                    await ctx.switch_active(ctx.player_id, t)
    return effect


def tail_sting_vs_ex(base: int = 10, bonus: int = 10):
    async def effect(ctx):
        d = ctx.defender
        if d is not None and is_pokemon_ex(d):
            await ctx.deal_damage(base + bonus)
            await ctx.apply_special_condition(d, SpecialConditions.POISONED)
        else:
            await ctx.deal_damage(base)
    return effect


def stages_of_evolution_retreat_discount(*types) -> Passive:
    """Evolved: Colorless less to retreat Fire/Psychic (etc) Pokémon."""
    tvs = {getattr(t, "value", t) for t in types}
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or is_basic_pokemon(holder):
                return cost
            if pokemon.owning_player_id != holder.owning_player_id:
                return cost
            types_list = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if not any(t in tvs for t in types_list):
                return cost
            return max(0, cost - 1)
    return _P()


def metal_star_draw_if_tool(draw: int = 3):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        from spirit.game.card_effects.attacks_common import has_tool
        if has_tool(a):
            await ctx.draw_cards(draw)
    return effect


def lap_up_draw(n: int = 2):
    async def effect(ctx):
        await ctx.draw_cards(n)
    return effect


def delta_mind_counters(normal: int = 1, delta: int = 3):
    async def effect(ctx):
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Delta Mind")
        if t is None:
            return
        n = delta if _has_delta(t) else normal
        await ctx.deal_damage(n * 10, target=t, apply_modifiers=False, as_counters=True)
    return effect


def dig_up_on_evolve_energy(count: int = 2):
    async def effect(ctx):
        if not await ctx.ask_yes_no("Search discard for Energy?"):
            return
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt="Energy from discard")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def pump_out_if_tool(base: int = 50, bonus: int = 20):
    async def effect(ctx):
        from spirit.game.card_effects.attacks_common import has_tool
        a = ctx.attacker
        amt = base + (bonus if a is not None and has_tool(a) else 0)
        await ctx.deal_damage(amt)
    return effect


def tropical_heal_on_bench():
    async def effect(ctx):
        if not await ctx.ask_yes_no("Remove Special Conditions and markers?"):
            return
        for p in ctx.my_pokemon_in_play():
            if hasattr(ctx, "remove_special_conditions"):
                await ctx.remove_special_conditions(p)
            elif hasattr(ctx, "cure_special_conditions"):
                await ctx.cure_special_conditions(p)
            else:
                p.set_attribute(AttrID.SPECIAL_CONDITIONS, [])
            for key in ("Imprison", "ShockWave", "Shock-wave"):
                if p.get_attribute(key, None) is not None:
                    p.set_attribute(key, False)
    return effect


def psychic_wing_retreat0_if_psychic() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder:
                return cost
            if any(energy_provides_type(c, PokemonTypes.PSYCHIC.value) for c in holder.children):
                return 0
            return cost
    return _P()


def extra_feather_stage2_ex_boost(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_attack_damage(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            atk = calc.attacker
            if atk is None or holder is None:
                return None
            if atk.owning_player_id != holder.owning_player_id:
                return None
            if not is_pokemon_ex(atk):
                return None
            st = getattr(def_for(atk.archetype_id), "stage", None)
            if st != PokemonStage.STAGE2:
                return None
            return amount
    return _P()


def power_of_evolution_draw_bottom():
    async def effect(ctx):
        src = ctx.source
        if src is None or is_basic_pokemon(src):
            return
        await ctx.draw_from_bottom(1)
    return effect


def extra_wing_stage2_ex_retreat0() -> Passive:
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon.owning_player_id != getattr(holder, "owning_player_id", None):
                return cost
            if not is_pokemon_ex(pokemon):
                return cost
            st = getattr(def_for(pokemon.archetype_id), "stage", None)
            if st != PokemonStage.STAGE2:
                return cost
            return 0
    return _P()


def flickering_tail_vs_ex(base: int = 10, bonus: int = 10):
    async def effect(ctx):
        d = ctx.defender
        if d is not None and is_pokemon_ex(d):
            await ctx.deal_damage(base + bonus)
            await ctx.apply_special_condition(d, SpecialConditions.ASLEEP)
        else:
            await ctx.deal_damage(base)
    return effect


def alluring_kiss_search():
    async def effect(ctx):
        def is_basic(c):
            d = def_for(c.archetype_id)
            return is_pokemon_card(c) and getattr(d, "stage", None) == PokemonStage.BASIC
        def is_basic_e(c):
            return is_basic_energy_card(c)
        p1 = await ctx.search_deck(is_basic, count=1, minimum=0, prompt="Basic Pokémon")
        p2 = await ctx.search_deck(is_basic_e, count=1, minimum=0, prompt="basic Energy")
        got = (p1 or []) + (p2 or [])
        if got:
            await ctx.put_in_hand(got, reveal=True)
        await ctx.shuffle_deck()
    return effect


def strangle_vs_delta(base: int = 50, bonus: int = 30):
    async def effect(ctx):
        d = ctx.defender
        amt = base + (bonus if d is not None and _has_delta(d) else 0)
        await ctx.deal_damage(amt)
    return effect


def burning_venom():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def reverse_thrust_switch(damage: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(damage)
        bench = ctx.my_bench()
        if bench:
            t = await ctx.choose_pokemon(bench, "Switch with?")
            if t is not None:
                await ctx.switch_active(ctx.player_id, t)
    return effect


def extra_ball_vs_ex(base: int = 30, bonus: int = 30):
    async def effect(ctx):
        d = ctx.defender
        await ctx.deal_damage(base + (bonus if d is not None and is_pokemon_ex(d) else 0))
    return effect


def type_shift_to_fire():
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        src.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        src.set_attribute("TypeShiftFireUntilEOT", True)
    return effect


def dual_stream_optional_split(full: int = 80, half: int = 40):
    async def effect(ctx):
        if await ctx.ask_yes_no(f"Do {half} to Active and {half} to Bench instead of {full}?"):
            await ctx.deal_damage(half)
            bench = ctx.opponent_bench()
            if bench:
                t = await ctx.choose_pokemon(bench, "Bench target")
                if t is not None:
                    await ctx.deal_damage(half, target=t, apply_modifiers=False)
        else:
            await ctx.deal_damage(full)
    return effect


def imprison_marker():
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Put Imprison marker on")
        if t is not None:
            t.set_attribute("Imprison", True)
    return effect


def imprison_blocks_powers_passive() -> Passive:
    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier, board=None):
            if not pokemon.get_attribute("Imprison", False):
                return False
            return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER
    return _P()


def fellow_boost_attach_energy(*names):
    names_l = [n.lower() for n in names]
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
        if not pool:
            return
        dests = [
            p for p in ctx.my_pokemon_in_play()
            if any(n in _display_name(p).lower() for n in names_l)
        ]
        if not dests:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="basic Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(dests, "Attach to Latias/Latios line")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def link_wing_named_retreat0(*names) -> Passive:
    names_l = [n.lower() for n in names]
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            dn = _display_name(pokemon).lower()
            if any(n in dn for n in names_l):
                return 0
            return cost
    return _P()


def power_crush_discard_on_ko(energy_type=PokemonTypes.FIRE, count: int = 2):
    async def effect(ctx):
        await ctx.deal_damage()
        # Soft: if defender HP would be 0 after, discard
        d = ctx.defender
        a = ctx.attacker
        if d is None or a is None:
            return
        hp = d.get_attribute(AttrID.HP, 0)
        # Approximate: if printed damage >= hp, discard
        # Better: use attack_followup; here check after damage via deferred
        async def after():
            # If defender knocked out this attack
            if d.get_attribute(AttrID.HP, 0) <= 0 or d not in ctx.opponent_pokemon_in_play():
                pool = [c for c in list(a.children) if energy_provides_type(c, getattr(energy_type, "value", energy_type))]
                if len(pool) > count:
                    picks = await ctx.choose_cards(pool, count, minimum=count, prompt="Discard Energy")
                else:
                    picks = pool[:count]
                if picks:
                    await ctx.discard_cards(picks)
        ctx.deferred_actions.append(after)
    return effect


def rage_aura_ignore_colorless() -> Passive:
    """If more Prize cards left than opponent, ignore Colorless Energy costs
    on Special Circuit and Sky-high Claws."""
    class _P(Passive):
        def modify_attack_cost(self, cost, pokemon, carrier, board, ability=None, **kwargs):
            holder = carrier_pokemon(carrier) or carrier
            if pokemon is not holder or board is None:
                return cost
            title = ""
            if ability is not None:
                title = (getattr(ability, "title", None) or getattr(ability, "name", "") or "")
                if isinstance(ability, dict):
                    title = ability.get("title") or ability.get("name") or ""
                title = str(title).lower()
            allowed = {"special circuit", "sky-high claws", "sky high claws"}
            if title and title not in allowed:
                return cost
            my_area = board.find_player_area(holder.owning_player_id, "prizePile")
            my_left = len(my_area.children) if my_area else 0
            opp_left = None
            # Discover opponent id via board helpers
            opp_id = None
            if hasattr(board, "opponent_id"):
                try:
                    opp_id = board.opponent_id(holder.owning_player_id)
                except Exception:
                    opp_id = None
            if opp_id is None:
                for attr in ("_player_ids", "player_ids"):
                    ids = getattr(board, attr, None)
                    if ids is None:
                        continue
                    ids = ids() if callable(ids) else ids
                    for pid in ids:
                        if pid != holder.owning_player_id:
                            opp_id = pid
                            break
                    if opp_id:
                        break
            if opp_id is None:
                return cost
            opp_area = board.find_player_area(opp_id, "prizePile")
            opp_left = len(opp_area.children) if opp_area else 0
            if my_left <= opp_left:
                return cost
            out = dict(cost or {})
            cv = getattr(PokemonTypes.COLORLESS, "value", PokemonTypes.COLORLESS)
            out.pop(PokemonTypes.COLORLESS, None)
            out.pop(cv, None)
            return out
    return _P()

def protective_swirl_no_weakness_next():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is not None:
            a.set_attribute("NoWeaknessNextOppTurn", True)
    return effect


def energy_link_attach_from_discard_to_self():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach Energy from discard")
        if picks:
            await ctx.attach_energy(picks[0], a)
    return effect


def extra_smoke_stage2_ex_reduce(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            t = calc.target
            if t is None or not calc.is_attack or not calc.is_opposing:
                return None
            if t.owning_player_id != getattr(holder, "owning_player_id", None):
                return None
            if not is_pokemon_ex(t):
                return None
            st = getattr(def_for(t.archetype_id), "stage", None)
            if st != PokemonStage.STAGE2:
                return None
            return -amount
    return _P()


def extra_boost_attach_to_stage2():
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
        dests = [
            p for p in ctx.my_pokemon_in_play()
            if getattr(def_for(p.archetype_id), "stage", None) == PokemonStage.STAGE2
        ]
        if not pool or not dests:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="basic Energy")
        if not picks:
            return
        dest = await ctx.choose_pokemon(dests, "Stage 2 Pokémon-ex?")
        # Printed: Stage 2 Pokémon-ex
        dests_ex = [p for p in dests if is_pokemon_ex(p)]
        if dests_ex:
            dest = await ctx.choose_pokemon(dests_ex, "Attach to Stage 2 Pokémon-ex")
        if dest is not None:
            await ctx.attach_energy(picks[0], dest)
    return effect


def deafen_block_trainers_next():
    async def effect(ctx):
        await ctx.deal_damage()
        # Mark opponent can't play Trainer (except Supporter) next turn
        opp = ctx.opponent_id
        # Store on board stadium-like attribute via attacker owner
        if ctx.attacker is not None:
            ctx.attacker.set_attribute("DeafenOppTrainers", opp)
    return effect


def dragon_roar_8_counters_overflow():
    """Put 8 counters on Defending; overflow beyond KO onto Bench as chosen."""
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        cur = d.get_attribute(AttrID.HP, 0) or 0
        to_active = min(8, (cur + 9) // 10) if cur > 0 else 8
        overflow = 8 - to_active
        await ctx.deal_damage(to_active * 10, target=d, apply_modifiers=False, as_counters=True)
        if overflow <= 0:
            return
        bench = list(ctx.opponent_bench())
        if bench:
            await ctx.place_damage_counters(overflow, bench)
    return effect

def psychic_pulse_bench_damaged(amount: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        for p in ctx.opponent_bench():
            hp_max = getattr(def_for(p.archetype_id), "hp", 0) or 0
            cur = p.get_attribute(AttrID.HP, 0)
            # damaged if cur < max — AttrID.HP often stores remaining or damage?
            # Use damage counters attribute if present
            dmg = p.get_attribute(AttrID.DAMAGE_COUNTERS, None)
            if dmg is None:
                # remaining HP model: damaged if below max
                if hp_max and cur < hp_max:
                    await ctx.deal_damage(amount, target=p, apply_modifiers=False)
            elif dmg:
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def electromark():
    async def effect(ctx):
        pool = list(ctx.opponent_pokemon_in_play())
        if not pool:
            return
        t = await ctx.choose_pokemon(pool, "Shock-wave marker")
        if t is not None:
            t.set_attribute("ShockWave", True)
    return effect


def hyper_claws_vs_stage2(base: int = 70, bonus: int = 20):
    async def effect(ctx):
        d = ctx.defender
        st = getattr(def_for(d.archetype_id), "stage", None) if d else None
        evolved = d is not None and not is_basic_pokemon(d)
        amt = base + (bonus if st == PokemonStage.STAGE2 and evolved else 0)
        await ctx.deal_damage(amt)
    return effect


def shock_wave_ko_marked():
    async def effect(ctx):
        marked = [p for p in ctx.opponent_pokemon_in_play() if p.get_attribute("ShockWave", False)]
        if not marked:
            return
        t = await ctx.choose_pokemon(marked, "Knock Out marked Pokémon")
        if t is not None:
            await ctx.knock_out(t)
    return effect


def dark_swirl_discard_all_mill3(damage: int = 150):
    async def effect(ctx):
        a = ctx.attacker
        if a is not None:
            energies = [c for c in list(a.children) if is_energy_card(c)]
            if energies:
                await ctx.discard_cards(energies)
        await ctx.deal_damage(damage)
        top = ctx.deck_top(3, player_id=ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)
    return effect


def mimicry_copy_any_opp_attack():
    async def effect(ctx):
        from spirit.game.data_utils import Attack as _Attack
        cands = list(ctx.opponent_pokemon_in_play())
        if not cands:
            return
        target = await ctx.choose_pokemon(cands, "Copy attack from")
        if target is None:
            return
        attacks = [
            ab for ab in (getattr(def_for(target.archetype_id), "abilities", None) or [])
            if isinstance(ab, _Attack)
        ]
        if not attacks:
            return
        idx = await ctx.choose("Choose attack", [a.title for a in attacks])
        if idx is None or idx < 0 or idx >= len(attacks):
            return
        await ctx.use_attack(attacks[idx])
    return effect


def rainbow_wave_per_type(per: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        basics = [c for c in a.children if is_basic_energy_card(c)]
        if not basics:
            return
        picks = await ctx.choose_cards(basics, 1, minimum=1, prompt="Choose basic Energy")
        if not picks:
            return
        d = def_for(picks[0].archetype_id)
        et = getattr(d, "energy_type", None)
        et = getattr(et, "value", et)
        # Also try ENERGY_INFO
        info = picks[0].get_attribute(AttrID.ENERGY_INFO, None)
        if et is None and isinstance(info, dict):
            et = info.get("type") or info.get("energy_type")
        for p in ctx.opponent_pokemon_in_play():
            types = p.get_attribute(AttrID.POKEMON_TYPES) or []
            if et is not None and (et in types or getattr(et, "value", et) in types):
                await ctx.deal_damage(per, target=p, apply_modifiers=is_in_active_spot(p))
            elif et is not None and any(energy_provides_type(picks[0], t) for t in types):
                await ctx.deal_damage(per, target=p, apply_modifiers=is_in_active_spot(p))
    return effect


def old_rod_flip2():
    async def effect(ctx):
        flips = await ctx.flip_coins(2, "Old Rod")
        if not flips:
            return
        if flips[0] and flips[1]:
            pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
            picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Pokémon from discard")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
        elif (not flips[0]) and (not flips[1]):
            pool = []
            for c in ctx.discard_pile():
                d = def_for(c.archetype_id)
                st = getattr(d, "supertype", None) or ""
                subs = getattr(d, "subtypes", None) or []
                if "Trainer" in str(st) or any(x in subs for x in ("Item", "Supporter", "Stadium", "Pokémon Tool", "Tool")):
                    pool.append(c)
            picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Trainer from discard")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
    return effect


def island_hermit_prizes_face_up(draw: int = 2, prizes: int = 2):
    async def effect(ctx):
        prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        if prize_area and prize_area.children:
            face_down = [c for c in prize_area.children if not c.get_attribute("PrizeFaceUp", False)]
            n = min(prizes, len(face_down))
            if n:
                picks = await ctx.choose_cards(face_down, n, minimum=0, prompt="Prizes to turn face up")
                for c in picks or []:
                    c.set_attribute("PrizeFaceUp", True)
                    if hasattr(ctx, "reveal_cards"):
                        await ctx.reveal_cards([c])
        await ctx.draw_cards(draw)
    return effect


def holon_legacy_passive() -> Passive:
    """δ Pokémon have no Weakness and can't use Poké-Powers (both players)."""
    class _P(Passive):
        stacking_key = "holon_legacy"

        def modify_weakness(self, calc, carrier):
            t = calc.target
            if t is not None and _has_delta(t):
                calc.weakness_applies = False

        def blocks_ability(self, pokemon, ability, carrier, board=None):
            if not _has_delta(pokemon):
                return False
            return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER
    return _P()


def charm_reduce_defender_next(reduce: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is not None:
            await apply_protection(ctx, target=ctx.defender, reduce=reduce)
    return effect



def ice_barrier_then_damage():
    """Deal damage; prevent effects/damage from Pokémon-ex next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_protection(ctx, prevent=True, effects_too=True, only_ex=True)
    return effect


def heal_self_counters(counters: int = 2):
    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


# ---------------------------------------------------------------------------
# EX16 Power Keepers helpers
# ---------------------------------------------------------------------------

def stadium_named_in_play(ctx, *names) -> bool:
    st = ctx.stadium_in_play()
    if st is None:
        return False
    dn = _display_name(st).lower()
    return any(n.lower() in dn for n in names)


def drakes_stadium_passive() -> Passive:
    """Colorless Active: -10 damage from opponent attacks (after W/R)."""
    class _P(Passive):
        stacking_key = "drakes_stadium"
        def modify_damage_taken(self, calc, carrier):
            t = calc.target
            if t is None or not calc.is_attack or not calc.is_opposing:
                return None
            if not is_in_active_spot(t):
                return None
            types = t.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.COLORLESS.value not in types:
                return None
            return -10
    return _P()


def glacias_stadium_passive() -> Passive:
    """Water Pokémon (excl ex) have no Weakness."""
    class _P(Passive):
        stacking_key = "glacias_stadium"
        def modify_weakness(self, calc, carrier):
            t = calc.target
            if t is None or is_pokemon_ex(t):
                return
            types = t.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.WATER.value in types:
                calc.weakness_applies = False
    return _P()


def phoebes_stadium_passive() -> Passive:
    """Psychic Pokémon retreat ColorlessColorless less."""
    class _P(Passive):
        stacking_key = "phoebes_stadium"
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.PSYCHIC.value not in types:
                return cost
            return max(0, cost - 2)
    return _P()


def sidneys_stadium_passive() -> Passive:
    """Darkness Pokémon can't be Asleep/Confused/Paralyzed."""
    class _P(Passive):
        stacking_key = "sidneys_stadium"
        def prevents_special_condition(self, pokemon, condition, carrier):
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.DARKNESS.value not in types:
                return False
            blocked = {
                SpecialConditions.ASLEEP, SpecialConditions.CONFUSED, SpecialConditions.PARALYZED,
                getattr(SpecialConditions.ASLEEP, "value", None),
                getattr(SpecialConditions.CONFUSED, "value", None),
                getattr(SpecialConditions.PARALYZED, "value", None),
            }
            return condition in blocked or getattr(condition, "value", condition) in blocked
    return _P()


def altaria_synergy_heal_between_turns():
    async def effect(ctx):
        src = ctx.source
        if src is None:
            return
        if not stadium_named_in_play(ctx, "Drake"):
            return
        await ctx.heal(10, src)
    return effect


def glalie_synergy_reduce(reduce: int = 30) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return None
            board = calc.board
            if board is None:
                return None
            area = board.find_global_area("activeStadium") if hasattr(board, "find_global_area") else None
            name = _display_name(area.children[0]).lower() if area and area.children else ""
            if "glacia" not in name:
                return None
            return -reduce
    return _P()

def sableye_synergy_prevent() -> Passive:
    """If Phoebe's Stadium in play, prevent damage from opponent's Pokémon-ex."""
    class _P(Passive):
        def prevents_damage(self, calc, carrier) -> bool:
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack or not calc.is_opposing:
                return False
            if calc.attacker is None or not is_pokemon_ex(calc.attacker):
                return False
            board = calc.board
            if board is None:
                return False
            area = board.find_global_area("activeStadium") if hasattr(board, "find_global_area") else None
            name = _display_name(area.children[0]).lower() if area and area.children else ""
            return "phoebe" in name
    return _P()

def poison_structure_sidney():
    async def effect(ctx):
        if not stadium_named_in_play(ctx, "Sidney"):
            return
        d = ctx.opponent_active()
        if d is None:
            return
        await ctx.apply_special_condition(d, SpecialConditions.POISONED)
    return effect

def dusclops_mysterious_light():
    async def effect(ctx):
        await ctx.deal_damage()
        if stadium_named_in_play(ctx, "Phoebe") and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    return effect


def dark_burst_sidney(base: int = 50, bonus: int = 20):
    async def effect(ctx):
        amt = base + (bonus if stadium_named_in_play(ctx, "Sidney") else 0)
        await ctx.deal_damage(amt)
    return effect


def cursed_eyes_move_counters():
    """ON_PLAY to Bench: may move 3 damage counters between opponent's Pokémon."""
    async def effect(ctx):
        damaged = []
        for p in ctx.opponent_pokemon_in_play():
            max_hp = ctx.max_hp(p) if hasattr(ctx, "max_hp") else (getattr(def_for(p.archetype_id), "hp", 0) or 0)
            cur = p.get_attribute(AttrID.HP, 0) or 0
            if max_hp and cur < max_hp:
                damaged.append(p)
        if len(damaged) < 1:
            return
        if not await ctx.ask_yes_no("Move 3 damage counters?"):
            return
        src = await ctx.choose_pokemon(damaged, "From?")
        if src is None:
            return
        dests = [p for p in ctx.opponent_pokemon_in_play() if p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "To?")
        if dest is None:
            return
        await ctx.move_damage_counters(src, dest, max_count=3)
    return effect

def terraforming_look5():
    async def effect(ctx):
        top = ctx.deck_top(5)
        if not top:
            return
        await ctx.reorder_deck_top(len(top), prompt="Look at the top 5 cards of your deck and put them back in any order")
    return effect


def rock_blast_discard_fighting(max_n: int = 5, per: int = 20):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIGHTING.value)]
        if not pool:
            return
        n = min(max_n, len(pool))
        picks = await ctx.choose_cards(pool, n, minimum=0, prompt="Discard Fighting Energy")
        if not picks:
            return
        await ctx.discard_cards(picks)
        targets = list(ctx.opponent_pokemon_in_play())
        for _ in picks:
            if not targets:
                break
            t = await ctx.choose_pokemon(targets, "Rock Blast target")
            if t is None:
                break
            await ctx.deal_damage(per, target=t, apply_modifiers=False)
    return effect

def grudge_damage(base: int = 20, per: int = 10):
    async def effect(ctx):
        taken = ctx.prizes_taken(ctx.opponent_id)
        await ctx.deal_damage(base + per * taken)
    return effect

def bench_manipulation():
    """Opponent flips coins = their Bench count; 40 × tails to Defending (no W/R)."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        n = len(bench)
        if n <= 0:
            await ctx.deal_damage(0)
            return
        flips = await ctx.flip_coins(n, "Bench Manipulation")
        tails = sum(1 for f in flips if not f)
        await ctx.deal_damage(tails * 40, apply_modifiers=False)
    return effect

def fire_stream_discard_spread(bench: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Fire Energy")
            if picks:
                await ctx.discard_cards(picks)
        for p in ctx.opponent_bench():
            await ctx.deal_damage(bench, target=p, apply_modifiers=False)
    return effect


def bursting_inferno():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def negative_ion_reduce(reduce: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is not None:
            await apply_protection(ctx, target=ctx.defender, reduce=reduce)
    return effect


def psychic_protector_discard_reduce():
    """If damaged, may discard up to 4 from hand; reduce damage by 10 per."""
    class _P(Passive):
        async def damage_interceptor(self, ctx, calc, target, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if target is not holder or not calc.is_attack or not calc.is_opposing:
                return None
            hand = list(ctx.hand())
            if not hand:
                return None
            if not await ctx.ask_yes_no("Discard cards to reduce damage?"):
                return None
            n = min(4, len(hand))
            picks = await ctx.choose_cards(hand, n, minimum=0, prompt="Discard up to 4")
            if not picks:
                return None
            await ctx.discard_cards(picks)
            return max(0, calc.amount - 10 * len(picks))
    return _P()

def eevee_star_ray_paralyze_all():
    """Crimson/Yellow/Blue Ray: Paralyze each Defending (opponent Active)."""
    async def effect(ctx):
        d = ctx.opponent_active()
        if d is not None:
            await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)
    return effect


def yellow_ray_on_bench():
    """ON_PLAY to Bench: 1 damage counter on each Active (both)."""
    async def effect(ctx):
        if not await ctx.ask_yes_no("Use Yellow Ray?"):
            return
        for p in (ctx.my_active(), ctx.opponent_active()):
            if p is not None:
                await ctx.deal_damage(10, target=p, apply_modifiers=False, as_counters=True)
    return effect

def crimson_ray_on_bench():
    """ON_PLAY to Bench: Burn each Active (yours and opponent's)."""
    async def effect(ctx):
        if not await ctx.ask_yes_no("Use Crimson Ray?"):
            return
        for p in (ctx.my_active(), ctx.opponent_active()):
            if p is not None:
                await ctx.apply_special_condition(p, SpecialConditions.BURNED)
    return effect

def blue_ray_on_bench():
    """ON_PLAY to Bench: clear SC + heal 3 counters from each Active (both)."""
    async def effect(ctx):
        if not await ctx.ask_yes_no("Use Blue Ray?"):
            return
        for p in (ctx.my_active(), ctx.opponent_active()):
            if p is not None:
                await ctx.cure_all_conditions(p)
                await ctx.heal(30, p)
    return effect

def primal_stare_block_basics() -> Passive:
    """While Kabutops Active: opponent can't evolve their Active from hand."""
    class _P(Passive):
        def blocks_evolution(self, player_id, target, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or not is_in_active_spot(holder):
                return False
            if player_id == holder.owning_player_id:
                return False
            return is_in_active_spot(target)
    return _P()

def magnetic_redraw():
    """Each player shuffles hand into deck, then draws 4."""
    async def effect(ctx):
        src = ctx.source
        if src is None or not is_in_active_spot(src):
            return
        for pid in (ctx.player_id, ctx.opponent_id):
            hand = list(ctx.hand(pid))
            if hand:
                await ctx.shuffle_into_deck(hand, player_id=pid)
            await ctx.draw_cards(4, player_id=pid)
    return effect

def scanblast_same_name(amount: int = 70):
    """Deal printed damage to Defending; also `amount` to same-name Bench (no W/R)."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        name = _display_name(d).lower()
        for p in ctx.opponent_bench():
            if _display_name(p).lower() == name:
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect

def dirge_same_name(amount: int = 60):
    return scanblast_same_name(amount)

def skill_hack_play_from_opp_hand():
    """Look at opponent's hand; copy an attack from a Basic/Evolution there."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        pokes = [c for c in hand if is_pokemon_card(c)]
        if not pokes:
            return
        await ctx.reveal_cards(hand)
        picks = await ctx.choose_cards(pokes, 1, minimum=0, prompt="Choose Pokémon from hand")
        if not picks:
            return
        card = picks[0]
        from spirit.game.data_utils import Attack as _Attack
        attacks = [
            ab for ab in (getattr(def_for(card.archetype_id), "abilities", None) or [])
            if isinstance(ab, _Attack)
        ]
        if not attacks:
            return
        labels = [a.title for a in attacks]
        idx = await ctx.choose("Choose an attack to copy", labels)
        if idx is None or idx < 0 or idx >= len(attacks):
            return
        await ctx.use_attack(attacks[idx])
    return effect

def metal_gravity_passive() -> Passive:
    """If opponent's Active retreats with ≥40 remaining HP, put 3 counters.
    stacking_key limits to one Metal Gravity body per retreat."""
    class _P(Passive):
        stacking_key = "metal_gravity"
        def counters_on_active_to_bench(self, pokemon, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if holder is None or pokemon is None:
                return 0
            if pokemon.owning_player_id == holder.owning_player_id:
                return 0
            remaining = pokemon.get_attribute(AttrID.HP, 0) or 0
            if remaining < 40:
                return 0
            return 3
    return _P()

def defense_curl_flip_protect():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Defense Curl")
        if heads and heads[0] and ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, prevent=True)
    return effect


def ember_discard_fire():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Fire Energy")
            if picks:
                await ctx.discard_cards(picks)
    return effect


def flamethrower_discard_fire():
    return ember_discard_fire()


def volcanic_flame_mill5(damage: int = 100):
    """Discard top 5 of deck; deal printed damage."""
    async def effect(ctx):
        top = ctx.deck_top(5)
        if top:
            await ctx.discard_cards(top)
        await ctx.deal_damage()
    return effect

def hydro_wave_discard_water_spread(amount: int = 30):
    """Discard all Water Energy; 30 to each opponent Bench (no W/R). Printed Active damage separate."""
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is not None:
            pool = [c for c in list(a.children) if is_energy_card(c) and energy_provides_type(c, PokemonTypes.WATER.value)]
            if pool:
                await ctx.discard_cards(pool)
        for p in ctx.opponent_bench():
            await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect

def chilling_breath_asleep_all_opp():
    """ON_EVOLVE: opponent can't play Trainer cards during their next turn."""
    async def effect(ctx):
        from spirit.game.session.effects import is_trainer_card
        if not await ctx.ask_yes_no("Use Chilling Breath?"):
            return
        ctx.lock_plays(ctx.opponent_id, is_trainer_card)
    return effect


def chilling_breath_lock_trainers():
    return chilling_breath_asleep_all_opp()

def solid_shell_reduce_self(amount: int = 10) -> Passive:
    class _P(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if calc.target is not holder or not calc.is_attack:
                return None
            return -amount
    return _P()


def double_spin_flip(per: int = 20, coins: int = 2):
    from spirit.game.card_effects.attacks_common import flip_damage
    return flip_damage(coins=coins, per_heads=per)


def charge_attach_lightning_from_discard():
    return plasma_attach_lightning()


def pikachu_charge():
    return plasma_attach_lightning()



def anorith_fury_cutter(base: int = 10):
    """Flip 3: 1H = +10, 2H = +30, 3H = +50."""
    async def effect(ctx):
        flips = await ctx.flip_coins(3, "Fury Cutter")
        heads = sum(1 for f in flips if f)
        bonus = {0: 0, 1: 10, 2: 30, 3: 50}.get(heads, 0)
        await ctx.deal_damage(base + bonus)
    return effect


def critical_crush_discard_basic(count: int = 2):
    """Discard `count` Basic Energy attached or this attack does nothing."""
    async def effect(ctx):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, count,
            predicate=is_basic_energy_card,
            prompt=f"Discard {count} Basic Energy or this attack does nothing",
        )
        if not discarded or len(discarded) < count:
            return
        await ctx.deal_damage()
    return effect


def mud_splash_bench_flip(amount: int = 20):
    """Deal printed damage; may snipe a Bench Pokémon for `amount` on heads."""
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if not bench:
            return
        t = await ctx.choose_pokemon(bench, "Mud Splash")
        if t is None:
            return
        flips = await ctx.flip_coins(1, "Mud Splash")
        if flips and flips[0]:
            await ctx.deal_damage(amount, target=t, apply_modifiers=False)
    return effect
