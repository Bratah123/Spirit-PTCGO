"""Reusable search / draw / heal / switch / energy effect factories.

Every factory returns an `async def effect(ctx)` usable on attacks, abilities
AND trainers (TrainerCardDef(effect=...)); attack usages resolve the printed
damage first (text order). The matching playability `condition=` factories at
the bottom accept both the trainer (board, player_id) and the ability
(board, player_id, pokemon) call shapes.
"""

from typing import Callable, List, Optional

from spirit.game.attributes import AttrID
from spirit.game.data_utils import def_for
from spirit.game.models.board import CardEntity, PokemonEntity
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_pokemon_card,
    is_trainer_card,
)
from spirit.game.session.passives import effective_bench_capacity, effective_max_hp
from spirit.game.card_effects.trainers import is_energy_card

# Spec-friendly aliases used as factory defaults.
is_basic = is_basic_pokemon
is_energy = is_energy_card


# --- Internal helpers --------------------------------------------------------

async def _deal_printed(ctx):
    """Printed attack damage first (text order); no-op for abilities/trainers."""
    if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
        await ctx.deal_damage()


def _card_label(card: CardEntity) -> str:
    definition = def_for(card.archetype_id)
    return getattr(definition, "display_name", None) or "the card"


def _is_damaged(board, pokemon: PokemonEntity) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _has_conditions(pokemon: PokemonEntity) -> bool:
    return bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))


def _opponent_of(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


async def _attach_all(ctx, cards, target: PokemonEntity):
    if target.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(target.entity_id)
    for card in cards:
        await ctx.attach_energy(card, target)


# --- Deck searches -----------------------------------------------------------

def search_to_hand(predicate=None, count=1, minimum=0, reveal=True, prompt=""):
    """Search the deck for up to `count` matches into hand, then shuffle.

    reveal follows the card text ("reveal it" -> True; Adaman-style -> False).
    """
    async def effect(ctx):
        await _deal_printed(ctx)
        picks = await ctx.search_deck(
            predicate, count=count, minimum=minimum,
            prompt=prompt or "Choose a card to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=reveal)
        await ctx.shuffle_deck()
    return effect


def search_to_bench(predicate=is_basic, count=1, then=None, prompt=""):
    """Search the deck for Pokémon onto the Bench (capped by free bench
    space, regi_gate shape), shuffle after; `then(ctx, benched)` runs last."""
    async def effect(ctx):
        await _deal_printed(ctx)
        space = BENCH_CAPACITY - len(ctx.my_bench())
        benched: List[CardEntity] = []
        take = min(count, space)
        if take > 0:
            picks = await ctx.search_deck(
                predicate, count=take, minimum=0,
                prompt=prompt or "Choose a Pokémon to put onto your Bench.",
            )
            for card in picks:
                if await ctx.bench_pokemon(card):
                    benched.append(card)
        await ctx.shuffle_deck()
        if then is not None and benched:
            await then(ctx, benched)
    return effect


# --- Energy search & attachment ----------------------------------------------

async def distribute_energy(ctx, cards, candidates):
    """Attach each card to a chosen Pokémon ("in any way you like"); each card
    may pick a different target. Returns the (card, target) pairs."""
    attached = []
    for card in cards:
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to attach {_card_label(card)} to"
        )
        if target is None:
            target = candidates[0]
        await _attach_all(ctx, [card], target)
        attached.append((card, target))
    return attached


def search_attach_energy(predicate=is_energy, count=1, to_self=False,
                         target_pred=None, distribute=True, shuffle=True,
                         prompt=""):
    """Search the deck for up to `count` Energy and attach: to this Pokémon
    (to_self), per-card free distribution, or all onto one chosen target."""
    async def effect(ctx):
        await _deal_printed(ctx)
        picks = await ctx.search_deck(
            predicate, count=count, minimum=0,
            prompt=prompt or f"Choose up to {count} Energy card(s) to attach.",
        )
        if picks:
            if to_self:
                await _attach_all(ctx, picks, ctx.source)
            else:
                candidates = [p for p in ctx.my_pokemon_in_play()
                              if target_pred is None or target_pred(p)]
                if candidates and distribute:
                    await distribute_energy(ctx, picks, candidates)
                elif candidates:
                    target = await ctx.choose_pokemon(
                        candidates, "Choose a Pokémon to attach the Energy to"
                    )
                    if target is not None:
                        await _attach_all(ctx, picks, target)
        if shuffle:
            await ctx.shuffle_deck()
    return effect


def look_top_attach_energy(n, predicate=is_energy, rest="shuffle",
                           target_pred=None, distribute=True, minimum=0):
    """Look at the top `n` deck cards and attach the Energy you find there;
    rest: 'shuffle' the deck after, 'back' leaves the others on top in order."""
    async def effect(ctx):
        await _deal_printed(ctx)
        top = ctx.deck_top(n)
        matches = [c for c in top if predicate(c)]
        if top:
            # No matches still shows the looked-at cards (nothing selectable).
            picks = await ctx.choose_cards(
                matches, max(len(matches), 1), minimum=minimum,
                prompt="Choose Energy cards to attach to your Pokémon.",
                display_cards=top,
            )
            candidates = [p for p in ctx.my_pokemon_in_play()
                          if target_pred is None or target_pred(p)]
            if picks and candidates:
                if distribute:
                    await distribute_energy(ctx, picks, candidates)
                else:
                    target = await ctx.choose_pokemon(
                        candidates, "Choose a Pokémon to attach the Energy to"
                    )
                    if target is not None:
                        await _attach_all(ctx, picks, target)
        if rest == "shuffle":
            await ctx.shuffle_deck()
    return effect


# --- Discard-pile recursion ----------------------------------------------------

def attach_from_discard(predicate=is_energy, count=1, target="self",
                        minimum=1, then=None, prompt=""):
    """Attach up to `count` matching discard-pile cards to one Pokémon:
    'self' = the acting Pokémon (abilities only), 'choice' = pick any of
    yours, or a predicate narrowing the pickable targets. minimum=1 keeps the
    activated public-zone pick mandatory; gate activation with a condition=."""
    async def effect(ctx):
        await _deal_printed(ctx)
        cards = [c for c in ctx.discard_pile() if predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=minimum,
            prompt=prompt or "Choose card(s) from your discard pile to attach",
        )
        if not picks:
            return
        if target == "self":
            holder: Optional[PokemonEntity] = ctx.source
        else:
            pred = None if target == "choice" else target
            candidates = [p for p in ctx.my_pokemon_in_play()
                          if pred is None or pred(p)]
            if not candidates:
                return
            holder = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to"
            ) or candidates[0]
        await _attach_all(ctx, picks, holder)
        if then is not None:
            await then(ctx, picks)
    return effect


def recover_from_discard(predicate=None, count=1, minimum=1, reveal=False,
                         to="hand", prompt=""):
    """Move up to `count` matching discard-pile cards to 'hand',
    'deck_shuffle', or 'deck_top' (ordered pick; the last pick ends on top).
    minimum=1 discipline for activated public-zone picks."""
    async def effect(ctx):
        await _deal_printed(ctx)
        cards = [c for c in ctx.discard_pile()
                 if predicate is None or predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=minimum, ordered=(to == "deck_top"),
            prompt=prompt or "Choose card(s) from your discard pile",
        )
        if not picks:
            return
        if to == "hand":
            await ctx.put_in_hand(picks, reveal=reveal)
        elif to == "deck_shuffle":
            await ctx.shuffle_into_deck(picks)
        elif to == "deck_top":
            for card in picks:
                await ctx.put_on_top_of_deck(card)
    return effect


# --- Draw family ---------------------------------------------------------------

def draw_attack(n):
    """Printed damage (if an attack), then draw `n`; also fine as an ability."""
    async def effect(ctx):
        await _deal_printed(ctx)
        await ctx.draw_cards(n)
    return effect


def conditional_draw(base, bonus, predicate):
    """Draw `base`, or `base + bonus` when `predicate(ctx)` holds (Kabu shape)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        count = base + (bonus if predicate(ctx) else 0)
        if count > 0:
            await ctx.draw_cards(count)
    return effect


def discard_then_draw(discard_count, draw_count, whole_hand=False,
                      optional=True, predicate=None, prompt=""):
    """Discard from hand, then draw. optional=True gates the draw on any
    discard ("If you do..."); whole_hand discards everything and always draws.
    draw_count may be `int` or `(ctx, discarded) -> int` (Milo's 2-per)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        if whole_hand:
            discarded = [c for c in ctx.hand()
                         if predicate is None or predicate(c)]
            await ctx.discard_cards(discarded)
        else:
            discarded = await ctx.discard_from_hand(
                discard_count, minimum=0 if optional else None,
                predicate=predicate,
                prompt=prompt or ("Choose up to %d card(s) to discard" % discard_count
                                  if optional else
                                  "Choose %d card(s) to discard" % discard_count),
            )
            if not discarded:
                return
        n = draw_count(ctx, discarded) if callable(draw_count) else draw_count
        if n > 0:
            await ctx.draw_cards(n)
    return effect


def draw_until_effect(n):
    """Draw until the hand holds `n` cards (Dragon's Hoard shape)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        await ctx.draw_until(n)
    return effect


def shuffle_hand_into_deck_draw(n, opponent_n=None):
    """Shuffle your hand into your deck and draw `n` (Cynthia); with
    opponent_n the opponent then does the same drawing that many (Judge)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        await ctx.draw_cards(n)
        if opponent_n is not None:
            await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
            await ctx.draw_cards(opponent_n, ctx.opponent_id)
    return effect


def look_at_top(n, take=1, predicate=None, rest="shuffle", minimum=None,
                prompt=""):
    """Look at the top `n` deck cards, put up to `take` matches into hand;
    rest: 'shuffle' the deck, 'bottom' the others under it, 'back' leaves
    them on top in order. minimum=None picks exactly `take` (or all if fewer)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        top = ctx.deck_top(n)
        if not top:
            return
        candidates = [c for c in top if predicate is None or predicate(c)]
        picks: List[CardEntity] = []
        if take > 0:
            # No matches still shows the looked-at cards (nothing selectable).
            picks = await ctx.choose_cards(
                candidates, take, minimum=minimum,
                prompt=prompt or "Choose a card to put into your hand.",
                display_cards=top if len(candidates) < len(top) else None,
            )
            if picks:
                await ctx.put_in_hand(picks, reveal=False)
        if rest == "shuffle":
            await ctx.shuffle_deck()
        elif rest == "bottom":
            for card in top:
                if card not in picks:
                    await ctx.put_on_bottom_of_deck(card)
    return effect


# --- Heal family -----------------------------------------------------------------

async def _heal_scope_targets(ctx, scope, condition_cure=False):
    """Targets for a heal scope; 'choice'/'bench_choice' pick one eligible."""
    if scope == "active":
        active = ctx.my_active()
        return [active] if active is not None else []
    if scope in ("each_own", "all_own"):
        return ctx.my_pokemon_in_play()
    pool = ctx.my_bench() if scope == "bench_choice" else ctx.my_pokemon_in_play()
    eligible = [p for p in pool
                if _is_damaged(ctx.board, p)
                or (condition_cure and _has_conditions(p))]
    if not eligible:
        return []
    target = await ctx.choose_pokemon(eligible, "Choose a Pokémon to heal")
    return [target] if target is not None else []


def heal_attack(amount=None, all_damage=False, discard_energy=0, target="self"):
    """Printed damage, optional self energy-discard cost, then heal this
    Pokémon (`target='self'`) or your Active; all_damage heals everything."""
    async def effect(ctx):
        await _deal_printed(ctx)
        pokemon = ctx.attacker if target == "self" else ctx.my_active()
        if pokemon is None:
            return
        if discard_energy > 0:
            await ctx.discard_energy_from(
                pokemon, discard_energy,
                prompt=f"Discard {discard_energy} Energy",
            )
        heal_amount = (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) \
            if all_damage else (amount or 0)
        if heal_amount > 0:
            await ctx.heal(heal_amount, pokemon)
    return effect


def heal_targets(amount, scope="each_own"):
    """Heal `amount` from the scope: 'each_own'/'all_own' (every one of
    yours), 'active', 'bench_choice', or 'choice' (pick one damaged)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        for pokemon in await _heal_scope_targets(ctx, scope):
            await ctx.heal(amount, pokemon)
    return effect


def heal_item(amount, scope="choice", condition_cure=False):
    """Trainer heal over a scope (see heal_targets); condition_cure also
    removes Special Conditions (Pokémon Center Lady). Gate playability with
    requires_damaged_pokemon()."""
    async def effect(ctx):
        for pokemon in await _heal_scope_targets(ctx, scope, condition_cure):
            if amount > 0:
                await ctx.heal(amount, pokemon)
            if condition_cure:
                await ctx.cure_all_conditions(pokemon)
    return effect


def cure_conditions_effect(scope="active"):
    """Remove all Special Conditions from the scope ('active', 'choice',
    'each_own'); conditions only, never attack locks."""
    async def effect(ctx):
        await _deal_printed(ctx)
        if scope == "choice":
            afflicted = [p for p in ctx.my_pokemon_in_play() if _has_conditions(p)]
            if not afflicted:
                return
            target = await ctx.choose_pokemon(afflicted, "Choose a Pokémon to recover")
            targets = [target] if target is not None else []
        elif scope in ("each_own", "all_own"):
            targets = [p for p in ctx.my_pokemon_in_play() if _has_conditions(p)]
        else:
            active = ctx.my_active()
            targets = [active] if active is not None else []
        for pokemon in targets:
            await ctx.cure_all_conditions(pokemon)
    return effect


# --- Switching / gusting -----------------------------------------------------------

async def opponent_switches(ctx):
    """The opponent switches their Active with a Benched Pokémon of THEIR
    choice (escape_rope precedent); returns the new Active, or None."""
    bench = ctx.opponent_bench()
    if not bench:
        return None
    target = await ctx.choose_pokemon(
        bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
    ) or bench[0]
    if not await ctx.switch_active(ctx.opponent_id, target):
        return None  # switch blocked/failed: nothing became the new Active
    return target


def switch_self_attack(damage=None, optional=False, bench_predicate=None):
    """Damage first (text order), then switch this Pokémon with a Benched one
    of your choice; optional adds the "you may" dialog."""
    async def effect(ctx):
        if damage is not None:
            if damage > 0:
                await ctx.deal_damage(damage)
        else:
            await _deal_printed(ctx)
        bench = [p for p in ctx.my_bench()
                 if bench_predicate is None or bench_predicate(p)]
        if not bench:
            return
        if optional and not await ctx.ask_yes_no(
                "Switch this Pokémon with 1 of your Benched Pokémon?"):
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


async def _gust(ctx, opponent_chooses=False):
    """Switch one of the opponent's Benched Pokémon with their Active;
    returns the new Active or None (no bench / effect-shielded Active /
    switch blocked), so "damage to the new Active" is skipped when no switch happens."""
    old_active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old_active is None or not bench:
        return None
    if ctx.effects_blocked(old_active):
        return None
    if opponent_chooses:
        return await opponent_switches(ctx)
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon"
    ) or bench[0]
    if not await ctx.switch_active(ctx.opponent_id, target):
        return None  # switch blocked/failed: nothing became the new Active
    return target


def gust_attack(damage_to_new_active=0, damage_before=None, opponent_chooses=False):
    """Gust: switch an opposing Benched Pokémon with their Active (YOU choose
    unless the text says the opponent switches); optional damage before the
    switch (printed by default) and onto the new Active after."""
    async def effect(ctx):
        if damage_before is not None:
            if damage_before > 0:
                await ctx.deal_damage(damage_before)
        else:
            await _deal_printed(ctx)
        new_active = await _gust(ctx, opponent_chooses)
        if new_active is not None and damage_to_new_active > 0:
            await ctx.deal_damage(damage_to_new_active, target=new_active)
    return effect


def gust_then(then, opponent_chooses=False):
    """Gust composite: switch, then `then(ctx, new_active)` (conditions etc.)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        new_active = await _gust(ctx, opponent_chooses)
        if new_active is not None:
            await then(ctx, new_active)
    return effect


# --- Self-removal from play -----------------------------------------------------

_REMOVAL_PROMPTS = {
    "hand": "Put this Pokémon and all attached cards into your hand?",
    "deck": "Shuffle this Pokémon and all attached cards into your deck?",
    "lost_zone": "Put this Pokémon in the Lost Zone?",
}


def remove_self_from_play(destination="hand", with_attachments="same",
                          optional=False, prompt=""):
    """Remove the acting Pokémon from play to 'hand', 'deck' (shuffled) or
    'lost_zone'; with_attachments 'same' takes the whole stack along ("this
    Pokémon and all attached cards"), 'discard' discards the attachments
    (Scoop Up Net). Vacating the Active defers promotion (psychic_leap)."""
    async def effect(ctx):
        pokemon = ctx.source
        await _deal_printed(ctx)
        if optional and not await ctx.ask_yes_no(
                prompt or _REMOVAL_PROMPTS.get(destination, "Remove this Pokémon from play?")):
            return
        was_active = pokemon is ctx.my_active()
        if with_attachments == "discard":
            await ctx.discard_cards([c for c in full_stack(pokemon) if c is not pokemon])
            stack = [pokemon]
        else:
            stack = full_stack(pokemon)
        if destination == "hand":
            await ctx.put_in_hand(stack, reveal=False)
        elif destination == "deck":
            await ctx.shuffle_into_deck(stack, ctx.player_id)
        elif destination == "lost_zone":
            await ctx.move_to_lost_zone(stack)
        if was_active:
            # Promotion must wait for the attack bracket to flush, or the client
            # sees the new Active land while the old one still stands there.
            async def _promote():
                if not await ctx.session._promote_new_active(ctx.player_id):
                    screen_name = ctx.session.players[ctx.player_id].screen_name
                    await ctx.session.end_game(
                        ctx.opponent_id, f"{screen_name} has no Pokémon left"
                    )

            ctx.deferred_actions.append(_promote)
    return effect


# --- BW Fossil Items (Restored Pokemon) -----------------------------------------

def restore_fossil(pokemon_name: str, look: int = 7):
    """BW Fossil Item (Plume/Cover/Root Fossil, Old Amber): look at the bottom
    `look` cards of your deck, you may reveal a `pokemon_name` there and put
    it onto your Bench, then shuffle. Matches EVOLUTION_LOGIC_NAME, so pass
    the importer's logic name (e.g. "Archen")."""
    async def effect(ctx):
        bottom = ctx.deck()[:look]
        if not bottom:
            return
        matches = [c for c in bottom
                   if c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == pokemon_name]
        if len(ctx.my_bench()) >= effective_bench_capacity(ctx.board, ctx.player_id):
            matches = []
        # Shows the bottom cards even when nothing there is selectable.
        picks = await ctx.choose_cards(
            matches, 1, minimum=0,
            prompt=f"Choose a {pokemon_name} to put onto your Bench.",
            display_cards=bottom,
        )
        if picks:
            await ctx.reveal_cards(picks)
            await ctx.bench_pokemon(picks[0])
        await ctx.shuffle_deck()
    return effect


# --- Playability condition factories ---------------------------------------------
# Each returns a check accepting BOTH call shapes: trainers/energies call
# (board, player_id), abilities call (board, player_id, pokemon).

def requires_discard(predicate=None, n=1):
    """At least `n` matching cards sit in the player's discard pile."""
    def check(board, player_id, pokemon=None):
        area = board.find_player_area(player_id, "discard")
        cards = list(area.children) if area else []
        return sum(1 for c in cards if predicate is None or predicate(c)) >= n
    return check


def requires_bench_space(n=1):
    """At least `n` free bench slots."""
    def check(board, player_id, pokemon=None):
        bench = board.find_player_area(player_id, "bench")
        return bench is not None and BENCH_CAPACITY - len(bench.children) >= n
    return check


def _side_player_ids(board, player_id, side) -> List[str]:
    pids = [player_id] if side in ("mine", "any") else []
    if side in ("opponent", "any"):
        opponent = _opponent_of(board, player_id)
        if opponent:
            pids.append(opponent)
    return pids


def requires_in_play(predicate, side="mine"):
    """A Pokémon matching `predicate` is in play on 'mine'/'opponent'/'any' side."""
    def check(board, player_id, pokemon=None):
        return any(predicate(p) for pid in _side_player_ids(board, player_id, side)
                   for p in board.pokemon_in_play(pid))
    return check


def requires_hand(predicate=None, n=1, exclude_self=True):
    """At least `n` matching cards in hand. exclude_self discounts the card
    being played when it may be among the matches (predicate None always
    matches it; otherwise only Trainer-card matches are suspect) -- pass
    exclude_self=False when the card itself can never match `predicate`."""
    def check(board, player_id, pokemon=None):
        hand = board.find_player_area(player_id, "hand")
        matches = [c for c in (hand.children if hand else [])
                   if predicate is None or predicate(c)]
        discount = 0
        if exclude_self:
            if pokemon is not None:
                # Trainer play conditions get the played copy itself as the
                # third argument (trainer_condition_met): drop exactly it.
                # Ability conditions pass the in-play Pokemon, never in hand.
                matches = [c for c in matches if c is not pokemon]
            elif predicate is None or any(is_trainer_card(c) for c in matches):
                discount = 1
        return len(matches) - discount >= n
    return check


def requires_damaged_pokemon(side="mine"):
    """A damaged Pokémon is in play on 'mine'/'opponent'/'any' side."""
    def check(board, player_id, pokemon=None):
        return any(_is_damaged(board, p)
                   for pid in _side_player_ids(board, player_id, side)
                   for p in board.pokemon_in_play(pid))
    return check


# --- Cedric Juniper (BW11): height-guess quiz, draw 3 -------------------------------

_POKEDEX_HEIGHT_DM = (
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
13, 18, 21, 17, 16, 20, 18, 40, 22, 20,
4, 9, 12, 18, 5, 9, 17, 6, 11, 23,
8, 18, 7, 16, 10, 14, 5, 11, 18, 5,
12, 3, 3, 3, 3, 6, 2, 15, 6, 8,
14, 4, 4, 8, 12, 11, 4, 6, 8, 8,
3, 8, 12, 4, 14, 9, 10, 5, 20, 7,
5, 13, 15, 6, 12, 15, 11, 92, 6, 14,
5, 18, 6, 15, 9, 6, 18, 7, 8, 4,
11, 6, 6, 9, 9, 21, 17, 6, 14, 18,
5, 11, 6, 14, 12, 7, 14, 4, 6, 7,
12, 15, 19, 21, 20, 6, 12, 20, 52, 38,
6, 5, 9, 17, 4, 9, 19, 4, 7, 15,
5, 10, 4, 5, 3, 6, 10, 7, 12, 5,
12, 15, 5, 10, 13, 3, 7, 6, 12, 4,
8, 16, 5, 8, 4, 12, 8, 14, 20, 5,
8, 8, 6, 10, 15, 10, 23, 2, 10, 6,
11, 5, 6, 4, 9, 21, 6, 13, 6, 15,
4, 4, 7, 6, 3, 4, 17, 8, 18, 20,
145, 7, 19, 5, 7, 9, 11, 7, 11, 20,
4, 13, 4, 11, 13, 27, 10, 12, 4, 9,
6, 11, 5, 15, 10, 15, 7, 15, 6, 62,
3, 10, 6, 11, 8, 16, 20, 6, 12, 6,
7, 15, 8, 11, 14, 4, 17, 18, 10, 6,
6, 11, 15, 6, 12, 16, 17, 18, 19, 14,
20, 45, 35, 70, 3, 17, 4, 11, 22, 5,
9, 12, 4, 8, 17, 3, 6, 12, 5, 10,
3, 10, 5, 9, 14, 2, 9, 9, 16, 5,
13, 2, 5, 9, 3, 12, 4, 7, 11, 4,
5, 3, 9, 12, 4, 12, 4, 12, 9, 9,
5, 10, 2, 4, 10, 5, 13, 5, 6, 6,
5, 10, 7, 14, 19, 6, 7, 12, 8, 20,
8, 13, 7, 13, 14, 4, 12, 10, 10, 22,
11, 12, 17, 24, 20, 18, 16, 15, 19, 10,
8, 20, 25, 9, 16, 14, 22, 13, 3, 3,
3, 3, 54, 42, 17, 37, 45, 15, 4, 3,
15, 2, 32, 4, 6, 8, 33, 5, 10, 16,
5, 8, 15, 5, 11, 4, 9, 12, 4, 11,
6, 11, 6, 10, 6, 10, 6, 11, 3, 6,
12, 8, 16, 4, 9, 17, 4, 9, 3, 7,
11, 6, 12, 14, 5, 8, 15, 13, 14, 3,
5, 12, 4, 12, 25, 3, 7, 5, 11, 10,
7, 10, 15, 6, 13, 10, 3, 14, 6, 11,
14, 5, 17, 7, 12, 5, 14, 6, 19, 7,
16, 4, 5, 4, 7, 15, 3, 6, 10, 5,
13, 4, 11, 13, 6, 19, 4, 5, 10, 2,
6, 12, 22, 12, 1, 8, 6, 10, 3, 6,
6, 2, 12, 21, 5, 10, 3, 6, 10, 6,
10, 18, 5, 26, 11, 4, 8, 7, 9, 14,
16, 10, 28, 5, 16, 16, 5, 15, 5, 12,
14, 3, 8, 14, 18, 11, 16, 21, 19, 20,
15, 15, 32, 29, 15, 30, 14, 6, 15, 4,
7, 16, 4, 10, 15, 3, 6, 15, 4, 10,
3, 7, 12, 3, 3, 12, 6, 15, 1, 2,
11, 9, 17, 6, 21, 12, 3, 6, 8, 8,
17, 2, 8, 4, 8, 4, 15, 5, 13, 5,
18, 5, 13, 5, 10, 8, 25, 13, 27, 10,
8, 2, 3, 3, 8, 20, 2, 4, 15, 4,
9, 10, 20, 5, 15, 30, 58, 50, 7, 5,
17,
)


def _height_ft_in(family_id):
    """Printed Pokédex height as (feet, inches), or None if unknown."""
    if not family_id:
        return None
    try:
        idx = int(family_id) - 1
    except (TypeError, ValueError):
        return None
    if idx < 0 or idx >= len(_POKEDEX_HEIGHT_DM):
        return None
    inches = int(round(_POKEDEX_HEIGHT_DM[idx] * 3.937))
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


cedric_juniper_condition = requires_hand(is_pokemon_card)


async def cedric_juniper(ctx):
    """Put a Pokémon from hand face down; opponent guesses its height.
    Wrong → you draw 3. Right → opponent draws 3. (Exact Cedric Juniper text.)"""
    matches = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1, minimum=1,
        prompt="Choose a Pokémon to put face down",
    )
    if not picks:
        return
    chosen = picks[0]
    definition = def_for(chosen.archetype_id)
    name = getattr(definition, "display_name", None) or "Pokémon"
    feet = await ctx.choose(
        f"The Pokémon is named {name}. Guess its height (feet).",
        [str(i) for i in range(41)],
        player_id=ctx.opponent_id, use_panel=False,
    )
    inches = await ctx.choose(
        f"Guess {name}'s height: {feet} feet and how many inches?",
        [str(i) for i in range(12)],
        player_id=ctx.opponent_id, use_panel=False,
    )
    await ctx.reveal_cards([chosen], to_player=ctx.opponent_id)
    actual = _height_ft_in(_family_id_of(chosen))
    if actual is None:
        guess = f"{feet}'{inches:02}\""
        correct = await ctx.ask_yes_no(
            f"Your opponent guessed {guess}. "
            f"Does that match {name}'s printed height?",
        )
    else:
        correct = actual == (feet, inches)
    if correct:
        await ctx.draw_cards(3, ctx.opponent_id)
    else:
        await ctx.draw_cards(3)
