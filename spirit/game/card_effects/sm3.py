"""Burning Shadows (SM3) attack, ability, trainer, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

import random

from spirit.game.attributes import (
    AttrID, PokemonStage, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Attack, def_for, evolves_from_chain, subtypes_for,
)
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_supporter_card,
)
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import (
    count_energy,
    lock_all_attacks,
)
from spirit.game.card_effects.passives_common import (
    apply_protection,
    is_in_active_spot,
)
from spirit.game.card_effects.pokemon import energy_provides_type, is_pokemon_gx
from spirit.game.card_effects.support_common import (
    discard_then_draw,
    recover_from_discard,
    search_attach_energy,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    hand_size_at_least,
    is_basic_energy_card,
    is_energy_card,
    opponent_has_energy_attached,
)


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def is_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


def is_gx_or_ex(pokemon_or_id) -> bool:
    aid = getattr(pokemon_or_id, "archetype_id", pokemon_or_id) or ""
    subs = subtypes_for(aid)
    return "GX" in subs or "EX" in subs


def _energy_of_type(card, pokemon_type: PokemonTypes) -> bool:
    return is_energy_card(card) and energy_provides_type(card, pokemon_type.value)


def is_fire_energy(card) -> bool:
    return _energy_of_type(card, PokemonTypes.FIRE)


def is_water_energy(card) -> bool:
    return _energy_of_type(card, PokemonTypes.WATER)


def is_fairy_energy(card) -> bool:
    return _energy_of_type(card, PokemonTypes.FAIRY)


def is_darkness_energy(card) -> bool:
    return _energy_of_type(card, PokemonTypes.DARKNESS)


def is_psychic_energy(card) -> bool:
    return _energy_of_type(card, PokemonTypes.PSYCHIC)


def is_grass_energy(card) -> bool:
    return _energy_of_type(card, PokemonTypes.GRASS)


def _has_ability(pokemon) -> bool:
    abilities = pokemon.get_attribute(AttrID.PIE_ABILITIES) or []
    return any(isinstance(e, dict) and e.get("abilityType") in
               ("PokeAbility", "PokePower", "PokeBody") for e in abilities)


def _special_condition_count(pokemon) -> int:
    return len(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if pokemon else 0


def _has_conditions(pokemon) -> bool:
    return bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def _return_to_hand(ctx, pokemon, with_attachments=True):
    """Put `pokemon` (and attached cards) into its owner's hand; defer promotion."""
    if pokemon is None:
        return
    owner = pokemon.owning_player_id or ctx.player_id
    was_active = pokemon is ctx.board.active_pokemon(owner)
    if with_attachments:
        stack = full_stack(pokemon)
    else:
        await ctx.discard_cards([c for c in full_stack(pokemon) if c is not pokemon])
        stack = [pokemon]
    await ctx.put_in_hand(stack, reveal=False)

    async def _promote():
        if not await ctx.session._promote_new_active(owner):
            screen_name = ctx.session.players[owner].screen_name
            winner = ctx.opponent_id if owner == ctx.player_id else ctx.player_id
            await ctx.session.end_game(winner, f"{screen_name} has no Pokémon left")
    if was_active:
        ctx.deferred_actions.append(_promote)


async def _shuffle_opponent_active(ctx) -> bool:
    """Shuffle the opponent's Active and attachments into their deck; defer promotion."""
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return False
    await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)
    return True


# ======================================================================
# Trainers
# ======================================================================

def _is_damaged(board, pokemon) -> bool:
    from spirit.game.session.passives import effective_max_hp
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def acerola_condition(board, player_id):
    return any(_is_damaged(board, p) for p in board.pokemon_in_play(player_id))


async def acerola(ctx):
    """Put 1 of your damaged Pokémon and all attached cards into your hand."""
    damaged = [p for p in ctx.my_pokemon_in_play()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon with damage counters on it")
    if target is not None:
        await _return_to_hand(ctx, target)


def guzma_condition(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return False
    bench = board.find_player_area(opponent, "bench")
    return bool(bench and bench.children)


async def guzma(ctx):
    """Switch an opponent's Benched Pokémon into the Active spot; if you do,
    switch your Active with a Benched Pokémon of yours."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon") or bench[0]
    if not await ctx.switch_active(ctx.opponent_id, target):
        return
    await ctx.flush_choreography()
    mine = ctx.my_bench()
    if mine:
        mine_target = await ctx.choose_pokemon(
            mine, "Choose your new Active Pokémon") or mine[0]
        await ctx.switch_active(ctx.player_id, mine_target)


async def kiawe(ctx):
    """Search for up to 4 Fire Energy and attach them to 1 of your Pokémon; turn ends."""
    await search_attach_energy(
        is_fire_energy, count=4, distribute=False,
        prompt="Choose up to 4 Fire Energy cards to attach.",
    )(ctx)
    ctx.ends_turn = True


async def lana(ctx):
    """Heal 50 from each of your Pokémon that has any Water Energy attached."""
    for pokemon in ctx.my_pokemon_in_play():
        if any(is_water_energy(e) for e in ctx.attached_energies(pokemon)):
            await ctx.heal(50, pokemon)


olivia = search_to_hand(
    lambda c: is_pokemon_gx(c.archetype_id), count=2, minimum=0,
    prompt="Choose up to 2 Pokémon-GX to put into your hand.",
)


def plumeria_playable(board, player_id):
    from spirit.game.card_effects.trainers import hand_size_at_least
    return hand_size_at_least(3)(board, player_id) and opponent_has_energy_attached(board, player_id)


async def plumeria(ctx):
    """Discard 2 cards from your hand. If you do, discard an Energy from 1 of
    your opponent's Pokémon."""
    discarded = await ctx.discard_from_hand(
        2, minimum=2, prompt="Discard 2 cards from your hand")
    if len(discarded) < 2:
        return
    pool = [e for p in ctx.opponent_pokemon_in_play() if not ctx._trainer_blocked(p)
            for e in ctx.attached_energies(p)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, prompt="Choose an Energy to discard from your opponent's Pokémon")
    if picks:
        await ctx.discard_cards(picks)


sophocles = discard_then_draw(
    2, 4, optional=False, prompt="Discard 2 cards from your hand",
)
sophocles_condition = hand_size_at_least(3)


async def wicke(ctx):
    """Each player counts their hand, shuffles it into their deck, then draws that many."""
    for pid in (ctx.player_id, ctx.opponent_id):
        n = ctx.hand_size(pid)
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        if n > 0:
            await ctx.draw_cards(n, pid)


async def super_scoop_up(ctx):
    """Flip a coin. If heads, put 1 of your Pokémon and all attached cards into your hand."""
    results = await ctx.flip_coins(1, "Super Scoop Up")
    if not results or not results[0]:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to put into your hand")
    if target is not None:
        await _return_to_hand(ctx, target)


def tormenting_spray_playable(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    hand = board.find_player_area(opponent, "hand") if opponent else None
    return bool(hand and hand.children)


async def tormenting_spray(ctx):
    """Choose a random card from the opponent's hand; reveal it; discard if Supporter."""
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    if is_supporter_card(card):
        await ctx.discard_cards([card])


async def rotom_dex_poke_finder(ctx):
    """Look at the top 4; put them back in any order, or shuffle the deck."""
    top = ctx.deck_top(4)
    if not top:
        return
    choice = await ctx.choose(
        "Put the cards back in any order, or shuffle them into your deck?",
        ["Reorder", "Shuffle"],
    )
    if choice == 1:
        await ctx.shuffle_deck()
        return
    await ctx.reorder_deck_top(len(top), prompt="Put the cards on top of your deck in any order.")


async def wishful_baton_ko(ctx):
    """If the holder is Knocked Out by an opponent's attack while Active, move
    up to 3 basic Energy from it to 1 of your Benched Pokémon."""
    if not getattr(ctx, "was_active_at_ko", False):
        return
    energies = [e for e in (getattr(ctx, "ko_energies", None) or [])
                if is_basic_energy_card(e)]
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    picks = await ctx.choose_cards(
        energies, min(3, len(energies)), minimum=0,
        prompt="Choose up to 3 basic Energy to move",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to") or bench[0]
    for energy in picks:
        await ctx.attach_energy(energy, target)


class MountLanakilaPassive(Passive):
    """Each Basic Pokémon in play has +1 retreat cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if is_basic_pokemon(pokemon):
            return cost + 1
        return cost


class PoTownPassive(Passive):
    """Whenever a player evolves from hand, put 3 damage counters on it."""

    def damage_counters_on_evolve(self, evolved, pre_evolution, player_id, carrier):
        return 3


def is_stage1(pokemon) -> bool:
    return pokemon.get_attribute(AttrID.STAGE) == PokemonStage.STAGE1.value


# ======================================================================
# Pokémon attacks / abilities
# ======================================================================

async def chemical_breath(ctx):
    """10 + 70 for each Special Condition on the opponent's Active."""
    n = _special_condition_count(ctx.defender)
    await ctx.deal_damage(10 + 70 * n)


async def tri_hazard_gx(ctx):
    """Gust a Benched Pokémon into the Active spot; Burn, Paralyze, Poison it."""
    bench = ctx.opponent_bench()
    active = ctx.opponent_active()
    if not bench or active is None or ctx.effects_blocked(active):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon") or bench[0]
    if not await ctx.switch_active(ctx.opponent_id, target):
        return
    new_active = ctx.opponent_active()
    if new_active is None:
        return
    for condition in (SpecialConditions.BURNED, SpecialConditions.PARALYZED,
                      SpecialConditions.POISONED):
        await ctx.apply_special_condition(new_active, condition)


class LuminousBarrierPassive(Passive):
    """Prevent all effects of attacks, including damage, from Pokémon-GX or EX."""

    def _from_gx_ex(self, attacker) -> bool:
        return attacker is not None and is_gx_or_ex(attacker)

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return self._from_gx_ex(calc.attacker)

    def blocks_attack_effects_from(self, target, attacker, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return self._from_gx_ex(attacker)


class ThickFatPassive(Passive):
    """This Pokémon takes 30 less from Fire or Water attacks (after W/R)."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.target or calc.attacker is None:
            return
        types = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.FIRE.value in types or PokemonTypes.WATER.value in types:
            calc.amount = max(0, calc.amount - 30)


class DisgustingPollenPassive(Passive):
    """As long as this is your Active, opponent's Basic Pokémon can't attack."""

    def blocks_attacks(self, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None or not is_in_active_spot(me):
            return False
        if pokemon.owning_player_id == me.owning_player_id:
            return False
        return is_basic_pokemon(pokemon)


class LightsEndPassive(Passive):
    """Prevent all damage done to this Pokémon by attacks from Colorless Pokémon."""

    def prevents_damage(self, calc, carrier):
        if not calc.is_attack:
            return False
        if carrier_pokemon(carrier) is not calc.target or calc.attacker is None:
            return False
        types = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        return PokemonTypes.COLORLESS.value in types


class MorePoisonPassive(Passive):
    """Put 1 more damage counter on the opponent's Poisoned Pokémon between turns."""

    def modify_poison_counters(self, counters, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None or pokemon.owning_player_id == me.owning_player_id:
            return counters
        return counters + 1


class UnarmedPassive(Passive):
    """If the owner has no cards in hand, ignore Energy in this Pokémon's attack costs.

    Unarmed is the only costed attack that the printed text covers; Drift Ashore
    (1 Psychic) also becomes free with an empty hand.
    """

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        hand = board.find_player_area(pokemon.owning_player_id, "hand")
        if hand is not None and len(hand.children) == 0:
            return {}
        return cost


class WimpOutPassive(Passive):
    """During your first turn, this Pokémon has no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        ts = getattr(board, "turn_state", None)
        if ts is None or ts.active_player_id != pokemon.owning_player_id:
            return cost
        if ts.turn_number <= 2:
            return 0
        return cost


class ShadowHuntPassive(Passive):
    """May use the attacks of any Basic Pokémon in the owner's discard pile."""

    def granted_attacks(self, board, pokemon, carrier):
        if carrier is not pokemon:
            return []
        discard = board.find_player_area(pokemon.owning_player_id, "discard")
        attacks = []
        for card in (discard.children if discard else []):
            if not is_basic_pokemon(card):
                continue
            for ability in getattr(def_for(card.archetype_id), "abilities", None) or []:
                if isinstance(ability, Attack):
                    attacks.append(ability)
        return attacks


class WeaknessOverridePassive(Passive):
    """The carrier's Weakness is now `weak_type` (amount unchanged)."""

    def __init__(self, weak_type):
        self.weak_type = weak_type

    def modify_weakness(self, calc, carrier):
        if carrier_pokemon(carrier) is calc.target:
            calc.weak_types = [self.weak_type]


class TakesMorePassive(Passive):
    """The carrier takes N more damage from attacks after W/R (Screech)."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and carrier_pokemon(carrier) is calc.target:
            calc.amount += self.amount


class QuickGuardPassive(Passive):
    """Prevent all damage from attacks by Basic Pokémon."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target or calc.attacker is None:
            return False
        return is_basic_pokemon(calc.attacker)


class LunatoneHealBlockPassive(Passive):
    """If Solrock is in play on this side, Pokémon (both sides) can't be healed."""

    def prevents_healing(self, target, carrier):
        me = carrier_pokemon(carrier)
        if me is None or me.parent is None or me.parent.parent is None:
            return False
        player_area = me.parent.parent
        for sub in player_area.children:
            name = sub.get_attribute(AttrID.NAME) if hasattr(sub, "get_attribute") else None
            if name not in ("activePokemonArea", "bench"):
                continue
            for poke in sub.children:
                if poke.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Solrock":
                    return True
        return False


def fairy_energy_in_hand(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_fairy_energy(c) for c in hand.children)


async def secret_spring(ctx):
    """Attach a Fairy Energy from your hand to 1 of your Pokémon."""
    cards = [c for c in ctx.hand() if is_fairy_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose a Fairy Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Fairy Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def infinite_force(ctx):
    """30 times Energy attached to both Active Pokémon."""
    n = count_energy()(ctx) + count_energy("defender")(ctx)
    if n > 0:
        await ctx.deal_damage(30 * n)


twilight_gx = recover_from_discard(
    None, count=10, minimum=0, to="deck_shuffle",
    prompt="Choose up to 10 cards to shuffle into your deck",
)


def restoration_condition(board, player_id, pokemon=None):
    from spirit.game.card_effects.support_common import requires_bench_space
    return requires_bench_space(1)(board, player_id)


async def restoration(ctx):
    """From discard: Bench this Pokémon, then attach a Darkness Energy from discard."""
    if not await ctx.ask_yes_no("Put this Pokémon onto your Bench?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    energies = [c for c in ctx.discard_pile() if is_darkness_energy(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=0,
        prompt="Choose a Darkness Energy card to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.source)


async def dead_end_gx(ctx):
    """If the opponent's Active is affected by a Special Condition, Knock it Out."""
    defender = ctx.defender
    if defender is None or not _has_conditions(defender):
        return
    await ctx.knock_out(defender)


def count_basic_energy(ctx) -> int:
    return sum(1 for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e))


async def raging_out_gx(ctx):
    """Discard the top 10 cards of the opponent's deck."""
    await ctx.discard_cards(ctx.deck_top(10, player_id=ctx.opponent_id))


async def eternal_flame_gx(ctx):
    """Put 3 in any combination of Fire Pokémon-GX or Fire Pokémon-EX from
    discard onto your Bench."""
    space = BENCH_CAPACITY - len(ctx.my_bench())
    if space <= 0:
        return

    def pred(card):
        if not is_pokemon_card(card) or not is_gx_or_ex(card):
            return False
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        return PokemonTypes.FIRE.value in types

    cards = [c for c in ctx.discard_pile() if pred(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, min(3, space, len(cards)), minimum=0,
        prompt="Choose Fire Pokémon-GX or Pokémon-EX to put onto your Bench",
    )
    for card in picks:
        await ctx.bench_pokemon(card)


async def natures_judgment(ctx):
    """You may discard all Energy; if you do, +60."""
    extra = 0
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies and await ctx.ask_yes_no("Discard all Energy from this Pokémon?"):
        await ctx.discard_cards(energies)
        extra = 60
    await ctx.deal_damage(120 + extra)


async def tapu_wilderness_gx(ctx):
    """150 damage, then heal all damage from this Pokémon."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    if attacker is not None:
        await ctx.heal(ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0),
                       attacker)


async def hydro_shot(ctx):
    """Discard 2 Water Energy; 120 to 1 of the opponent's Pokémon."""
    await ctx.discard_energy_from(
        ctx.attacker, 2, predicate=is_water_energy,
        prompt="Choose 2 Water Energy to discard")
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Choose a Pokémon to take 120 damage")
    if target is not None:
        await ctx.deal_damage(120, target=target)


async def tapu_storm_gx(ctx):
    """If the opponent has a Benched Pokémon, shuffle their Active into their deck."""
    if not ctx.opponent_bench():
        return
    await _shuffle_opponent_active(ctx)


async def queens_haze_gx(ctx):
    """Discard all Energy from the opponent's Active Pokémon."""
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_cards(list(ctx.attached_energies(target)))


async def first_impression(ctx):
    """30, +90 if this Pokémon became Active from the Bench this turn."""
    bonus = 90 if ctx.entered_active_this_turn(ctx.attacker) else 0
    await ctx.deal_damage(30 + bonus)


async def crossing_cut_gx(ctx):
    """150, then switch this Pokémon with a Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def prismatic_burst(ctx):
    """Discard all Psychic Energy; 10 + 60 per discarded card."""
    energies = [e for e in ctx.attached_energies(ctx.attacker) if is_psychic_energy(e)]
    await ctx.discard_cards(energies)
    await ctx.deal_damage(10 + 60 * len(energies))


async def black_ray_gx(ctx):
    """100 to each of the opponent's Pokémon-GX and Pokémon-EX; ignore W/R."""
    for pokemon in ctx.opponent_pokemon_in_play():
        if is_gx_or_ex(pokemon):
            await ctx.deal_damage(100, target=pokemon, ignore_weakness=True,
                                  ignore_resistance=True)


async def distort(ctx):
    """50; opponent can't play Item cards next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


async def sonic_volume(ctx):
    """120; opponent can't play Special Energy next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_special_energy)


async def bedrock_breaker(ctx):
    """130, then discard any Stadium in play."""
    await ctx.deal_damage()
    await ctx.discard_stadium()


async def muscle_punch_gx(ctx):
    """180 that isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def mix_up(ctx):
    """Flip a coin. If heads, discard the top 3 of the opponent's deck."""
    results = await ctx.flip_coins(1, "Mix-Up")
    if results and results[0]:
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))


async def knock_over(ctx):
    """Printed damage; you may discard any Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


async def bye_bye_heal(ctx):
    """Heal all damage from all of your Pokémon, then shuffle this Pokémon
    and all attached cards into your deck."""
    for pokemon in list(ctx.my_pokemon_in_play()):
        await ctx.heal(ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0),
                       pokemon)
    attacker = ctx.attacker
    was_active = attacker is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(attacker), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


async def gutsy_hammer(ctx):
    """Printed damage, then this Pokémon does 10 to itself per damage counter."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    counters = max(0, (ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0)) // 10)
    if counters:
        await ctx.deal_damage(10 * counters, target=attacker, apply_modifiers=False)


async def sparkling_wish(ctx):
    """Search for a card that evolves from 1 of your Pokémon and evolve it."""
    in_play = ctx.my_pokemon_in_play()
    names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in in_play}

    def pred(card):
        chain = evolves_from_chain(card.archetype_id)
        return bool(chain) and chain[0] in names

    picks = await ctx.search_deck(
        pred, count=1, minimum=0,
        prompt="Choose a card that evolves from 1 of your Pokémon.",
    )
    if picks:
        direct = evolves_from_chain(picks[0].archetype_id)[0]
        candidates = [p for p in in_play
                      if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == direct]
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to evolve") if candidates else None
        if target is not None:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


async def diamond_storm(ctx):
    """30 damage, then heal 30 from each of your Fairy Pokémon."""
    await ctx.deal_damage()
    for pokemon in ctx.my_pokemon_in_play():
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.FAIRY.value in types:
            await ctx.heal(30, pokemon)


async def night_roam(ctx):
    """Put 1 damage counter on each Pokémon (both sides)."""
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(10, target=pokemon, as_counters=True)


def dark_invitation_condition(board, player_id, pokemon=None) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return False
    hand = board.find_player_area(opponent, "hand")
    bench = board.find_player_area(opponent, "bench")
    if not hand or not bench or len(bench.children) >= BENCH_CAPACITY:
        return False
    return any(is_basic_pokemon(c) for c in hand.children)


async def dark_invitation(ctx):
    """Reveal the opponent's hand; put a Basic from there onto their Bench
    with 3 damage counters."""
    await ctx.reveal_hand(ctx.opponent_id)
    basics = [c for c in ctx.hand(ctx.opponent_id) if is_basic_pokemon(c)]
    if not basics:
        return
    if len(ctx.opponent_bench()) >= BENCH_CAPACITY:
        return
    picks = await ctx.choose_cards(
        basics, 1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your opponent's Bench")
    if not picks:
        return
    if await ctx.bench_pokemon(picks[0]):
        await ctx.deal_damage(30, target=picks[0], as_counters=True)


async def small_appetite(ctx):
    """If the opponent's Active has 100 or more max HP, this attack does nothing."""
    defender = ctx.defender
    if defender is None:
        return
    if ctx.max_hp(defender) >= 100:
        return
    await ctx.deal_damage()


async def vacuum_bolt(ctx):
    """You may do +80; if you do, 80 to 1 of your Pokémon."""
    extra = False
    if await ctx.ask_yes_no("Do 80 more damage? This Pokémon or another of yours takes 80 damage."):
        extra = True
    await ctx.deal_damage((ctx.ability.damage or 0) + (80 if extra else 0))
    if extra:
        pool = ctx.my_pokemon_in_play()
        if pool:
            target = await ctx.choose_pokemon(
                pool, "Choose 1 of your Pokémon to take 80 damage") or pool[0]
            await ctx.deal_damage(80, target=target, apply_modifiers=False)


async def thunder_punch(ctx):
    """Flip: heads +60, tails 20 to self."""
    results = await ctx.flip_coins(1, "Thunder Punch")
    heads = bool(results and results[0])
    await ctx.deal_damage((ctx.ability.damage or 0) + (60 if heads else 0))
    if not heads:
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)


async def perplexing_eyes(ctx):
    """The Defending Pokémon's Weakness is now Psychic until the end of your next turn."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_own_next_turn(
        defender, WeaknessOverridePassive(PokemonTypes.PSYCHIC.value))


async def mind_jack(ctx):
    """Printed + 30 per opponent's Benched Pokémon."""
    from spirit.game.card_effects.attacks_common import count_bench
    n = count_bench("opponent")(ctx)
    await ctx.deal_damage((ctx.ability.damage or 0) + 30 * n)


async def division(ctx):
    """Search your deck for Alolan Grimer and put it onto your Bench."""
    from spirit.game.card_effects.support_common import search_to_bench
    await search_to_bench(
        lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "AlolanGrimer",
        count=1,
        prompt="Choose an Alolan Grimer to put onto your Bench.",
    )(ctx)


async def synchronoise(ctx):
    """Printed damage, then 20 to each of the opponent's Benched Pokémon that
    shares a type with their Active."""
    await ctx.deal_damage()
    active = ctx.opponent_active()
    if active is None:
        return
    types = set(active.get_attribute(AttrID.POKEMON_TYPES) or [])
    for pokemon in ctx.opponent_bench():
        theirs = set(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
        if types & theirs:
            await ctx.deal_damage(20, target=pokemon)


async def bubble_net(ctx):
    """Printed damage; Energy can't be attached to the Defending Pokémon
    from the opponent's hand during their next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.restrict_attachments(defender)


async def dust_storm(ctx):
    """100, then discard all attached cards from both Actives."""
    await ctx.deal_damage()
    for pokemon in (ctx.attacker, ctx.defender):
        if pokemon is None:
            continue
        attached = [c for c in full_stack(pokemon) if c is not pokemon]
        if attached:
            await ctx.discard_cards(attached)


async def intentional_grounding(ctx):
    """Discard a Pokémon Tool from hand; if you don't, this attack does nothing."""
    tools = [c for c in ctx.hand() if is_tool_card(c)]
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, 1, prompt="Discard a Pokémon Tool card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.deal_damage()


async def screech(ctx):
    """During your next turn, the Defending Pokémon takes 60 more from attacks."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_own_next_turn(defender, TakesMorePassive(60))


async def calculate(ctx):
    """Look at the top 6 of your deck and put them back in any order."""
    await ctx.reorder_deck_top(6, prompt="Put the cards on top of your deck in any order.")


async def initialize(ctx):
    """On evolve: you may devolve each of the opponent's evolved Pokémon."""
    evolved = [p for p in ctx.opponent_pokemon_in_play()
               if p.get_attribute(AttrID.STAGE) in (
                   PokemonStage.STAGE1.value, PokemonStage.STAGE2.value)]
    if not evolved:
        return
    if not await ctx.ask_yes_no(
            "Devolve each of your opponent's evolved Pokémon?"):
        return
    for pokemon in list(evolved):
        if ctx.effects_blocked(pokemon):
            continue
        await ctx.devolve_pokemon(pokemon, steps=1, destination="hand")


async def code_check(ctx):
    """Look at 1 of your opponent's face-down Prize cards."""
    area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
    prizes = [c for c in (area.children if area else []) if not getattr(c, "face_up_prize", False)]
    if not prizes:
        prizes = list(area.children) if area else []
    if not prizes:
        return
    idx = await ctx.choose(
        "Look at which Prize card?",
        [str(i + 1) for i in range(len(prizes))],
    ) if len(prizes) > 1 else 0
    card = prizes[idx or 0]
    await ctx.session.prompt_view_cards(
        ctx.player_id, ctx.source.entity_id, [card],
        prompt="Your opponent's Prize card")


async def evoshock(ctx):
    """On evolve: you may leave the opponent's Active Paralyzed."""
    defender = ctx.opponent_active()
    if defender is None:
        return
    if await ctx.ask_yes_no("Leave your opponent's Active Pokémon Paralyzed?"):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)


async def rock_wrecker(ctx):
    """Damage isn't affected by Weakness or Resistance; this Pokémon can't
    attack during your next turn."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)
    lock_all_attacks(ctx, ctx.attacker)


honey_gather = search_to_hand(
    is_basic_energy_card, count=2, minimum=0,
    prompt="Choose up to 2 basic Energy cards to put into your hand.",
)


async def strength_sap(ctx):
    """Printed damage, then heal 30 times Energy on the opponent's Active."""
    await ctx.deal_damage()
    n = count_energy("defender")(ctx)
    if n > 0 and ctx.attacker is not None:
        await ctx.heal(30 * n, ctx.attacker)


async def aqua_reflect(ctx):
    """Printed damage, then move a Water Energy from this Pokémon to a Bench Pokémon."""
    await ctx.deal_damage()
    waters = [e for e in ctx.attached_energies(ctx.attacker) if is_water_energy(e)]
    bench = ctx.my_bench()
    if not waters or not bench:
        return
    picks = await ctx.choose_cards(
        waters, 1, minimum=0, prompt="Choose a Water Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to") or bench[0]
    await ctx.move_energy(picks[0], target)


async def leaf_supply(ctx):
    """Printed damage; you may attach a Grass Energy from hand to 1 of yours."""
    await ctx.deal_damage()
    cards = [c for c in ctx.hand() if is_grass_energy(c)]
    if not cards:
        return
    if not await ctx.ask_yes_no("Attach a Grass Energy card from your hand?"):
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose a Grass Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Grass Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def flare_recharge(ctx):
    """Printed damage, then attach a Fire Energy from discard to a Bench Pokémon."""
    await ctx.deal_damage()
    from spirit.game.card_effects.support_common import attach_from_discard
    from spirit.game.card_effects.passives_common import is_in_active_spot

    def _benched(pokemon):
        return not is_in_active_spot(pokemon)

    await attach_from_discard(
        is_fire_energy, count=1, target=_benched, minimum=0,
        prompt="Choose a Fire Energy card to attach to a Benched Pokémon",
    )(ctx)


async def poison_boost(ctx):
    """If this Pokémon is Poisoned, +80, then remove Poisoned from it."""
    attacker = ctx.attacker
    poisoned = attacker is not None and "Poisoned" in (
        attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage((ctx.ability.damage or 0) + (80 if poisoned else 0))
    if poisoned:
        await ctx.cure_condition(attacker, SpecialConditions.POISONED)


async def stance(ctx):
    """On evolve: you may prevent all effects of attacks, including damage,
    until the end of the opponent's next turn."""
    if await ctx.ask_yes_no(
            "Prevent all effects of your opponent's attacks, including damage, "
            "done to this Pokémon until the end of your opponent's next turn?"):
        await apply_protection(ctx, target=ctx.source, prevent=True, effects_too=True)


async def energy_slosh(ctx):
    """Printed damage; you may move all Energy from this Pokémon to a Bench Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = list(ctx.attached_energies(ctx.attacker))
    if not bench or not energies:
        return
    if not await ctx.ask_yes_no("Move all Energy attached to this Pokémon to 1 of your Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to") or bench[0]
    for energy in energies:
        await ctx.move_energy(energy, target)


async def night_raid(ctx):
    """Opponent reveals their hand. Discard a Pokémon from it."""
    await ctx.reveal_hand(ctx.opponent_id)
    pokes = [c for c in ctx.hand(ctx.opponent_id) if is_pokemon_card(c)]
    if not pokes:
        return
    picks = await ctx.choose_cards(
        pokes, 1, prompt="Choose a Pokémon to discard from your opponent's hand")
    if picks:
        await ctx.discard_cards(picks)


async def vigorous_dash(ctx):
    """Printed damage, 30 to self, 30 to 1 of opponent's Benched Pokémon."""
    await ctx.deal_damage()
    await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to take 30 damage")
        if target is not None:
            await ctx.deal_damage(30, target=target)


async def rule_of_evil(ctx):
    """60 to each Pokémon that has an Ability (both sides); no W/R on Bench."""
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if _has_ability(pokemon):
            await ctx.deal_damage(60, target=pokemon)


async def core_enforcer(ctx):
    """150; discard a Darkness Energy and a Fairy Energy from this Pokémon."""
    await ctx.deal_damage()
    dark = [e for e in ctx.attached_energies(ctx.attacker) if is_darkness_energy(e)]
    fairy = [e for e in ctx.attached_energies(ctx.attacker) if is_fairy_energy(e)]
    picks = []
    if dark:
        d = await ctx.choose_cards(dark, 1, prompt="Choose a Darkness Energy to discard")
        picks.extend(d)
    if fairy:
        f = await ctx.choose_cards(fairy, 1, prompt="Choose a Fairy Energy to discard")
        picks.extend(f)
    if picks:
        await ctx.discard_cards(picks)


async def odor_sleuth(ctx):
    """Flip 2 coins. For each heads, put a card from discard into your hand."""
    results = await ctx.flip_coins(2, "Odor Sleuth")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    pile = ctx.discard_pile()
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, min(heads, len(pile)),
        prompt=f"Choose {heads} card(s) from your discard pile to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


async def venting_anger(ctx):
    """50 damage for each Magikarp in your discard pile."""
    n = sum(1 for c in ctx.discard_pile()
            if c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Magikarp")
    if n > 0:
        await ctx.deal_damage(50 * n)


async def splash_burn(ctx):
    """Printed damage, then 30 to each of your Benched Pokémon."""
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)


async def brine(ctx):
    """90 to 1 of the opponent's Pokémon that has damage counters."""
    damaged = [p for p in ctx.opponent_pokemon_in_play()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon with damage counters on it")
    if target is not None:
        await ctx.deal_damage(90, target=target)


async def tornado_shot(ctx):
    """Discard a Water Energy; printed damage; 30 to 1 Benched opponent."""
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_water_energy,
        prompt="Choose a Water Energy to discard")
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to take 30 damage")
        if target is not None:
            await ctx.deal_damage(30, target=target)


async def enhanced_fang(ctx):
    """If this Pokémon has a Tool attached, +50."""
    from spirit.game.card_effects.attacks_common import has_tool
    bonus = 50 if ctx.attacker is not None and has_tool(ctx.attacker) else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def quick_guard_attack(ctx):
    """Prevent all damage from Basic Pokémon during the opponent's next turn."""
    ctx.add_passive_through_opponents_turn(ctx.attacker, QuickGuardPassive())


async def brick_break(ctx):
    """Damage isn't affected by Resistance or effects on the opponent's Active."""
    await ctx.deal_damage(ignore_resistance=True, ignore_target_effects=True)


async def solar_heat(ctx):
    """If a Stadium is in play, +20."""
    bonus = 20 if ctx.stadium_in_play() else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def aqua_shock(ctx):
    """If the opponent's Active has any Water Energy, +30."""
    defender = ctx.defender
    bonus = 0
    if defender is not None and any(is_water_energy(e) for e in ctx.attached_energies(defender)):
        bonus = 30
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def dark_raid(ctx):
    """If the opponent has already used their GX attack, +80."""
    from spirit.game.card_effects.attacks_common import gx_used
    bonus = 80 if gx_used(ctx, ctx.opponent_id) else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def dangerous_claws(ctx):
    """If the opponent's Active is a Basic Pokémon, +30."""
    bonus = 30 if ctx.defender is not None and is_basic_pokemon(ctx.defender) else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)
