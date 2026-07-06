"""Behaviors for the Trainer cards of the Lugia VSTAR and Mew VMAX decks."""

from spirit.game.attributes import (
    AttrID, CardType, CLIENT_POKEMON_TYPE_NAMES, PokemonStage, PokemonTypes, TrainerType,
)
from spirit.game.models.board import PokemonEntity
from spirit.game.data_utils import (
    Ability, Activations, has_rule_box, is_pokemon_v, subtypes_for,
)
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_evolution_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_supporter_card,
    is_water_pokemon,
)
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    carrier_pokemon,
    effective_max_hp,
)


# --- Shared playability predicates -----------------------------------------

def hand_size_at_least(count: int):
    """Condition: the hand holds `count` cards INCLUDING the trainer itself."""
    def check(board, player_id):
        hand = board.find_player_area(player_id, "hand")
        return hand is not None and len(hand.children) >= count
    return check


def _bench_pokemon(board, player_id):
    bench = board.find_player_area(player_id, "bench")
    return [c for c in (bench.children if bench else [])
            if isinstance(c, PokemonEntity)]


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def opponent_has_bench(board, player_id):
    opponent = _other_player(board, player_id)
    return bool(opponent) and bool(_bench_pokemon(board, opponent))


def player_has_bench(board, player_id):
    return bool(_bench_pokemon(board, player_id))


def someone_has_bench(board, player_id):
    return bool(_bench_pokemon(board, player_id)) or opponent_has_bench(board, player_id)


def has_supporter_in_discard(board, player_id):
    return any(is_supporter_card(c) for c in _discard(board, player_id))


def has_discard_card(board, player_id):
    return bool(_discard(board, player_id))


def opponent_prizes_low(board, player_id):
    """Roxanne's gate: the opponent has 3 or fewer Prize cards remaining."""
    opponent = _other_player(board, player_id)
    if not opponent:
        return False
    area = board.find_player_area(opponent, "prizePile")
    return bool(area) and len(area.children) <= 3


def battle_vip_pass_playable(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None or turn_state.turn_number > 2:
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and len(bench.children) < BENCH_CAPACITY


def has_other_item_in_hand(board, player_id):
    """Cram-o-matic's gate: another Item card besides itself sits in hand."""
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_item_card(c)) >= 2


def deck_nonempty(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck) and bool(deck.children)


def _opponent_special_energies(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        out.extend(c for c in pokemon.children if is_special_energy(c))
    return out


def opponent_has_special_energy(board, player_id):
    return bool(_opponent_special_energies(board, player_id))


def _discard(board, player_id):
    area = board.find_player_area(player_id, "discard")
    return list(area.children) if area else []


def is_energy_card(card) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value


def is_basic_energy_card(card) -> bool:
    return is_energy_card(card) and not is_special_energy(card)


def is_metal_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.METAL.value in types


def is_grass_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.GRASS.value in types


def is_darkness_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.DARKNESS.value in types


def is_pokemon_vmax(archetype_id) -> bool:
    return "VMAX" in subtypes_for(archetype_id)


def has_basic_energy_in_hand(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_basic_energy_card(c) for c in hand.children)


def bede_playable(board, player_id) -> bool:
    return player_has_bench(board, player_id) and has_basic_energy_in_hand(board, player_id)


def _opponent_energies(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        out.extend(c for c in pokemon.children if is_energy_card(c))
    return out


def opponent_has_energy_attached(board, player_id) -> bool:
    return bool(_opponent_energies(board, player_id))


def _my_vmax_pokemon(board, player_id):
    return [p for p in board.pokemon_in_play(player_id) if is_pokemon_vmax(p.archetype_id)]


def has_vmax_in_play(board, player_id) -> bool:
    return bool(_my_vmax_pokemon(board, player_id))


def has_two_metal_energy_in_hand(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_metal_energy_card(c)) >= 2


def _tools_and_stadium(board):
    """Every attached Pokemon Tool plus the Stadium in play."""
    targets = []
    for pid in board.player_ids:
        for pokemon in board.pokemon_in_play(pid):
            for child in pokemon.children:
                if child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value:
                    targets.append(child)
    stadium_area = board.find_global_area("activeStadium")
    targets.extend(stadium_area.children if stadium_area else [])
    return targets


def lost_vacuum_playable(board, player_id):
    return hand_size_at_least(2)(board, player_id) and bool(_tools_and_stadium(board))


def serena_playable(board, player_id):
    if hand_size_at_least(2)(board, player_id):
        return True
    opponent = _other_player(board, player_id)
    return bool(opponent) and any(
        is_pokemon_v(p.archetype_id) for p in _bench_pokemon(board, opponent)
    )


# --- Supporters -------------------------------------------------------------

async def professors_research(ctx):
    """Discard your hand and draw 7 cards."""
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(7)


async def marnie(ctx):
    """Both players shuffle their hands under their decks; you draw 5, the
    opponent draws 4. Per player in sequence: shuffle-to-bottom, then draw."""
    await ctx.hand_to_bottom_of_deck(ctx.player_id)
    await ctx.draw_cards(5)
    await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    await ctx.draw_cards(4, ctx.opponent_id)


async def bosss_orders(ctx):
    """Switch 1 of the opponent's Benched Pokemon with their Active."""
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def serena(ctx):
    """Choose 1: discard up to 3 then draw to 5, OR gust a Benched Pokemon V."""
    v_bench = [p for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id)]
    can_discard = bool(ctx.hand())
    if can_discard and v_bench:
        gust = await ctx.choose(
            "Choose 1:", ["Discard up to 3 cards from your hand. If you do, draw cards until you have 5 cards in your hand.", 
                          "Switch 1 of your opponent's Benched Pokemon V with their Active Pokemon."]
        ) == 1
    else:
        gust = bool(v_bench)
    if gust:
        target = await ctx.choose_pokemon(
            v_bench, "Choose the opponent's new Active Pokémon"
        )
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
        return
    discarded = await ctx.discard_from_hand(
        3, minimum=1, prompt="Choose up to 3 cards to discard"
    )
    if discarded:
        await ctx.draw_until(5)


async def irida(ctx):
    """Search the deck for up to 1 Water Pokemon and up to 1 Item card."""
    water, items = await ctx.search_deck_groups(
        [
            # loc keys render the {W} energy icon in the slot labels
            (is_water_pokemon, 1, "playmat.prompt.selectapokemonwater"),
            (is_item_card, 1, "playmat.prompt.select1item"),
        ],
        prompt="Choose up to 1 Water Pokémon and up to 1 Item card",
    )
    await ctx.put_in_hand(water + items, reveal=True)
    await ctx.shuffle_deck()


async def pal_pad(ctx):
    """Shuffle up to 2 Supporter cards from your discard pile into your deck."""
    picks = await ctx.choose_cards(
        [c for c in ctx.discard_pile() if is_supporter_card(c)], 2, minimum=1,
        prompt="Choose up to 2 Supporter cards to shuffle into your deck",
    )
    await ctx.shuffle_into_deck(picks)


async def judge(ctx):
    """Each player shuffles their hand into their deck and draws 4 cards."""
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(4, pid)


async def roxanne(ctx):
    """Opponent has 3 or fewer Prize cards remaining: each player shuffles
    their hand into their deck, then you draw 6 and the opponent draws 2."""
    for pid, count in ((ctx.player_id, 6), (ctx.opponent_id, 2)):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(count, pid)


async def cyllene(ctx):
    """Flip 2 coins; put up to that many cards from your discard pile on
    top of your deck, in an order you choose."""
    heads = await ctx.flip_coins(2, "Cyllene")
    count = heads.count(True)
    if count <= 0:
        return
    picks = await ctx.choose_cards(
        ctx.discard_pile(), count, minimum=1, ordered=True,
        prompt="Choose cards to put on top of your deck, in order",
    )
    # Ordered picks stack in selection order -- the last one picked ends up
    # on top of the deck.
    for card in picks:
        await ctx.put_on_top_of_deck(card)


async def piers(ctx):
    """Search your deck for an Energy card and a Darkness Pokemon, reveal
    them, and put them into your hand. Then, shuffle your deck."""
    energy, darkness = await ctx.search_deck_groups(
        [
            (is_energy_card, 1, "Energy card"),
            (is_darkness_pokemon, 1, "Darkness Pokémon"),
        ],
        prompt="Choose an Energy card and a Darkness Pokémon",
    )
    await ctx.put_in_hand(energy + darkness, reveal=True)
    await ctx.shuffle_deck()


async def bede(ctx):
    """Attach a basic Energy card from your hand to 1 of your Benched Pokemon."""
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a basic Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose the Benched Pokémon to attach it to"
    )
    if target is not None:
        await ctx.attach_energy(picked[0], target)


async def team_yell_grunt(ctx):
    """Put an Energy attached to 1 of the opponent's Pokemon into their hand."""
    targets = _opponent_energies(ctx.board, ctx.player_id)
    picked = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose an Energy card to return to its owner's hand",
    )
    # Already visible in play (attached), so no reveal-on-move is needed.
    await ctx.put_in_hand(picked, reveal=False)


async def milo(ctx):
    """Discard up to 2 cards from your hand, and draw 2 cards for each card
    you discarded in this way."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, prompt="Choose up to 2 cards to discard"
    )
    if discarded:
        await ctx.draw_cards(2 * len(discarded))


async def sonia(ctx):
    """Search your deck for up to 2 Basic Pokemon or up to 2 basic Energy
    cards, reveal them, and put them into your hand. Then, shuffle your deck."""
    want_energy = await ctx.choose(
        "Choose 1:", ["Up to 2 Basic Pokémon", "Up to 2 basic Energy cards"]
    ) == 1
    predicate = is_basic_energy_card if want_energy else is_basic_pokemon
    picks = await ctx.search_deck(
        predicate, count=2, minimum=0,
        prompt="Choose up to 2 Basic Pokémon or up to 2 basic Energy cards.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def kabu(ctx):
    """Shuffle your hand into your deck. Then, draw 4 cards; draw 8 instead
    if your Active Pokemon is your only Pokemon in play."""
    await ctx.shuffle_into_deck(ctx.hand())
    only_active = len(ctx.my_pokemon_in_play()) <= 1
    await ctx.draw_cards(8 if only_active else 4)


async def rose(ctx):
    """Attach up to 2 basic Energy cards from your discard pile to 1 of your
    Pokemon VMAX. If you attached any this way, discard your hand."""
    target = await ctx.choose_pokemon(
        _my_vmax_pokemon(ctx.board, ctx.player_id), "Choose your Pokémon VMAX"
    )
    if target is None:
        return
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 basic Energy cards to attach",
    )
    for energy in picks:
        await ctx.attach_energy(energy, target)
    if picks:
        await ctx.discard_cards(ctx.hand())


async def hop(ctx):
    """Draw 3 cards."""
    await ctx.draw_cards(3)


async def adaman(ctx):
    """Discard 2 Metal Energy cards from your hand, then search your deck
    for up to 2 cards and put them into your hand. Then, shuffle your deck."""
    discarded = await ctx.discard_from_hand(
        2, predicate=is_metal_energy_card,
        prompt="Discard 2 Metal Energy cards for Adaman",
    )
    if len(discarded) < 2:
        return
    picks = await ctx.search_deck(
        None, count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.",
    )
    # No "reveal it" clause on this card's text.
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def gardenias_vigor(ctx):
    """Draw 2 cards. If you drew any this way, attach up to 2 Grass Energy
    cards from your hand to 1 of your Benched Pokemon."""
    drawn = await ctx.draw_cards(2)
    if not drawn:
        return
    energies = [c for c in ctx.hand() if is_grass_energy_card(c)]
    if not energies:
        return
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose the Benched Pokémon to attach Grass Energy to",
        optional=True,
    )
    if target is None:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 Grass Energy cards to attach",
    )
    for energy in picks:
        await ctx.attach_energy(energy, target)


async def kamado(ctx):
    """Choose a card in your hand, and discard the other cards. If you do,
    draw 4 cards."""
    hand = ctx.hand()
    if not hand:
        return
    keep = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Choose a card to keep in your hand"
    )
    if not keep:
        return
    await ctx.discard_cards([c for c in hand if c is not keep[0]])
    await ctx.draw_cards(4)


async def zisu(ctx):
    """Draw cards until you have 1 more card in your hand than your opponent."""
    await ctx.draw_until(ctx.hand_size(ctx.opponent_id) + 1)


def _center_lady_targets(board, player_id):
    return [
        p for p in board.pokemon_in_play(player_id)
        if p.get_attribute(AttrID.SPECIAL_CONDITIONS)
        or p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
    ]


def center_lady_playable(board, player_id) -> bool:
    return bool(_center_lady_targets(board, player_id))


async def pokemon_center_lady(ctx):
    """Heal 60 damage from 1 of your Pokemon, and it recovers from all
    Special Conditions."""
    target = await ctx.choose_pokemon(
        _center_lady_targets(ctx.board, ctx.player_id), "Choose a Pokémon to heal"
    )
    if target is None:
        return
    await ctx.heal(60, target)
    await ctx.cure_all_conditions(target)


# --- Items -------------------------------------------------------------------

async def switch(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon."""
    target = await ctx.choose_pokemon(ctx.my_bench(), "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def quick_ball(ctx):
    """Discard 1 other card, then search the deck for a Basic Pokemon."""
    if not await ctx.discard_from_hand(1, prompt="Discard a card for Quick Ball"):
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def ultra_ball(ctx):
    """Discard 2 other cards, then search the deck for any Pokemon."""
    if len(await ctx.discard_from_hand(2, prompt="Discard 2 cards for Ultra Ball")) < 2:
        return
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def evolution_incense(ctx):
    """Search the deck for an Evolution Pokemon."""
    picks = await ctx.search_deck(
        is_evolution_pokemon, count=1, minimum=0,
        prompt="Choose an Evolution Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def escape_rope(ctx):
    """Each player switches their Active with a Benched Pokemon; the
    opponent switches first (no Bench, no switch)."""
    for pid in (ctx.opponent_id, ctx.player_id):
        bench = ctx.opponent_bench() if pid == ctx.opponent_id else ctx.my_bench()
        if not bench:
            continue
        target = await ctx.choose_pokemon(
            bench, "Choose your new Active Pokémon", player_id=pid
        )
        await ctx.switch_active(pid, target or bench[0])


async def lost_vacuum(ctx):
    """Lost-Zone a card from hand, then Lost-Zone a Tool in play or the Stadium."""
    cost = await ctx.choose_cards(
        ctx.hand(), 1, prompt="Choose a card to put in the Lost Zone"
    )
    if not cost:
        return
    await ctx.move_to_lost_zone(cost)
    targets = _tools_and_stadium(ctx.board)
    picks = await ctx.choose_cards(
        targets, 1, prompt="Choose a Pokémon Tool or Stadium to put in the Lost Zone",
    )
    await ctx.move_to_lost_zone(picks)


async def battle_vip_pass(ctx):
    """First turn only: search the deck for up to 2 Basic Pokemon and put
    them onto your Bench."""
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    space = BENCH_CAPACITY - len(bench.children) if bench else 0
    count = min(2, space)
    if count <= 0:
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=count, minimum=0,
        prompt="Choose up to 2 Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def power_tablet(ctx):
    """This turn, your Fusion Strike Pokemon's attacks do 30 more damage to
    the opponent's Active Pokemon (before Weakness and Resistance)."""
    ctx.add_turn_damage_modifier(
        TurnDamageModifier(30, ctx.player_id, requires_subtype="Fusion Strike")
    )
    # Green up-arrow PiP on each buffed Fusion Strike Pokemon in play.
    for pokemon in ctx.my_pokemon_in_play():
        if "Fusion Strike" in subtypes_for(pokemon.archetype_id):
            await ctx.add_stat_visualization(
                pokemon, "Positive", "DamageDealtIncreased", card_text="+30 damage"
            )


async def cramomatic(ctx):
    """Discard another Item card, then flip a coin; heads searches the deck
    for any card and puts it into your hand."""
    if not await ctx.discard_from_hand(
        1, predicate=is_item_card, prompt="Discard an Item card for Cram-o-matic"
    ):
        return
    heads, = await ctx.flip_coins(1, "Cram-o-matic")
    if not heads:
        return
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    # No "reveal it" clause on this card's text (unlike Ultra/Quick Ball).
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def rotom_phone(ctx):
    """Look at the top 5 cards of your deck, choose 1, shuffle the rest back
    into your deck, then put the chosen card on top."""
    top = ctx.deck_top(5)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, minimum=1, prompt="Choose a card to put on top of your deck",
    )
    if not picks:
        return
    await ctx.shuffle_deck()
    await ctx.put_on_top_of_deck(picks[0])


async def fan_of_waves(ctx):
    """Put a Special Energy attached to 1 of the opponent's Pokemon on the
    bottom of their deck."""
    targets = _opponent_special_energies(ctx.board, ctx.player_id)
    picks = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose a Special Energy to put on the bottom of their deck",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


async def star_alchemy(ctx):
    """Search your deck for a card and put it into your hand (VSTAR Power)."""
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    # No "reveal it" clause on this card's text (unlike Ultra/Quick Ball).
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


# --- Stadiums & Pokemon Tools -------------------------------------------------

class BigParasolPassive(Passive):
    """While the holder is in the Active Spot, shields the owner's whole
    side from the opponent's attack EFFECTS (not damage)."""

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or target.owning_player_id != holder.owning_player_id:
            return False
        parent = holder.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


class PathToThePeakPassive(Passive):
    """Rule Box Pokemon (both sides) have no Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        return has_rule_box(pokemon.archetype_id)


class LostCityPassive(Passive):
    """Knocked Out Pokemon go to the Lost Zone instead of the discard pile."""

    def knockout_destination(self, pokemon, carrier):
        return "lostZone"


# ======================================================================
# Lost Zone Box + Regigigas decks
# ======================================================================

def is_v_or_gx(archetype_id) -> bool:
    return is_pokemon_v(archetype_id) or "GX" in subtypes_for(archetype_id)


def has_basic_energy_in_discard(board, player_id) -> bool:
    return any(is_basic_energy_card(c) for c in _discard(board, player_id))


def has_pokemon_or_basic_energy_in_discard(board, player_id) -> bool:
    return any(is_pokemon_card(c) or is_basic_energy_card(c)
               for c in _discard(board, player_id))


# --- Colress's Experiment (LOR, Supporter) -------------------------------

async def colresss_experiment(ctx):
    """Look at the top 5 cards of your deck, put 3 into your hand, and put the
    other cards in the Lost Zone."""
    top = ctx.deck_top(5)
    if not top:
        return
    take = min(3, len(top))
    picks = await ctx.choose_cards(
        top, take, minimum=take, prompt="Choose 3 cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.move_to_lost_zone([c for c in top if c not in picks])


# --- Klara (CRE, Supporter) ----------------------------------------------

async def klara(ctx):
    """Choose 1 or both: up to 2 Pokemon and/or up to 2 basic Energy from your
    discard pile into your hand."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks_p = await ctx.choose_cards(
        pokemon, 2, minimum=0,
        prompt="Choose up to 2 Pokémon from your discard pile.",
    ) if pokemon else []
    picks_e = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy from your discard pile.",
    ) if energy else []
    await ctx.put_in_hand(picks_p + picks_e, reveal=False)


# --- Mirage Gate (LOR, Item) ---------------------------------------------

def mirage_gate_condition(board, player_id):
    """Usable only with 7 or more cards in the Lost Zone."""
    lost = board.find_player_area(player_id, "lostZone")
    return bool(lost) and len(lost.children) >= 7


async def mirage_gate(ctx):
    """Search your deck for up to 2 basic Energy of different types and attach
    them to your Pokemon in any way you like. Then, shuffle your deck."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    labels = {}
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
        labels[card.entity_id] = f"{CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(types[0])]} Energy"

    if not reps:
        await ctx.search_deck(
            is_basic_energy_card, count=2, minimum=0,
            prompt="Choose up to 2 basic Energy cards of different types.",
        )
        await ctx.shuffle_deck()
        return

    picks = await ctx.choose_cards(
        reps, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards of different types.",
        display_cards=reps,
    )
    for energy in picks:
        label = labels[energy.entity_id]
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), f"Choose a Pokémon to attach {label} to"
        )
        if target is not None:
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


# --- Scoop Up Net (RCL, Item) --------------------------------------------

async def scoop_up_net(ctx):
    """Put 1 of your Pokemon that isn't a Pokemon V or GX into your hand.
    Discard all attached cards."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if not is_v_or_gx(p.archetype_id)]
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokémon to put into your hand"
    )
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.discard_cards([c for c in full_stack(target) if c is not target])
    await ctx.put_in_hand([target], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


# --- Switch Cart (ASR, Item) ---------------------------------------------

def switch_cart_condition(board, player_id):
    active = board.active_pokemon(player_id)
    return (
        active is not None
        and active.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        and bool(_bench_pokemon(board, player_id))
    )


async def switch_cart(ctx):
    """Switch your Active Basic Pokemon with a Benched Pokemon; heal 30 from
    the Pokemon you moved to the Bench."""
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    await ctx.heal(30, active)


# --- Ordinary Rod (SSH, Item) --------------------------------------------

async def ordinary_rod(ctx):
    """Choose 1 or both: shuffle up to 2 Pokemon and/or up to 2 basic Energy
    from your discard pile into your deck."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks_p = await ctx.choose_cards(
        pokemon, 2, minimum=0,
        prompt="Choose up to 2 Pokémon to shuffle into your deck.",
    ) if pokemon else []
    picks_e = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy to shuffle into your deck.",
    ) if energy else []
    picks = picks_p + picks_e
    if picks:
        await ctx.shuffle_into_deck(picks)


# --- Energy Recycler (BST, Item) -----------------------------------------

async def energy_recycler(ctx):
    """Shuffle up to 5 basic Energy cards from your discard pile into your deck."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 5, minimum=1,
        prompt="Choose up to 5 basic Energy to shuffle into your deck.",
    )
    if picks:
        await ctx.shuffle_into_deck(picks)


# --- Trekking Shoes (ASR, Item) ------------------------------------------

async def trekking_shoes(ctx):
    """Look at the top card of your deck; you may put it into your hand,
    otherwise discard it and draw a card."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Put this card into your hand?",
        ["Put into hand", "Discard and draw a card"],
    )
    if idx == 0:
        await ctx.put_in_hand([card], reveal=False)
    else:
        await ctx.discard_cards([card])
        await ctx.draw_cards(1)


# --- Hisuian Heavy Ball (ASR, Item) --------------------------------------

async def hisuian_heavy_ball(ctx):
    """Look at your Prize cards; you may reveal a Basic Pokemon there, put it
    into your hand, and put this card in its place as a face-down Prize. Then
    shuffle your face-down Prize cards. (No Basic revealed -> discard normally.)

    The prize-fan node keeps the client's peek-your-prizes click handler
    suppressed; the reveal browser did not, which crashed on prize clicks."""
    await ctx.look_at_prizes_take_basic()


# --- Air Balloon (SSH, Pokemon Tool) -------------------------------------

class AirBalloonPassive(Passive):
    """The Retreat Cost of the holder is [C][C] less."""

    def modify_retreat_cost(self, cost, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon:
            return cost - 2
        return cost


# --- Training Court (RCL, Stadium) ---------------------------------------

def training_court_condition(board, player_id, stadium):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_basic_energy_card(c) for c in discard.children)


async def training_court(ctx):
    """Put a basic Energy card from your discard pile into your hand."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a basic Energy card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


TRAINING_COURT_ABILITY = Ability(
    title="Training Court",
    game_text="Once during each player's turn, that player may put a basic Energy card from their discard pile into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=training_court,
    condition=training_court_condition,
)
