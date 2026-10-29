"""SM Black Star Promos (Promo_SM) attack, ability, trainer, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import (
    AttrID, PokemonTypes, SpecialConditions,
)
from spirit.game.data_utils import (
    Ability, Activations, Attack, def_for, evolves_from_chain,
    subtypes_for,
)
from spirit.game.models.board import PokemonEntity
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_pokemon_card,
    is_special_energy,
)
from spirit.game.session.passives import Passive, effective_max_hp
from spirit.game.card_effects.attacks_common import (
    _printed,
    bonus_if,
    condition_attack,
    condition_bonus_attack,
    count_discard,
    count_energy,
    count_prizes_remaining,
    damage_counters_on,
    damage_per,
    discard_random_from_hand,
    flip_damage,
    has_extra_energy,
    self_energy_discard_attack,
    snipe_attack,
    spread_damage,
)
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost,
    is_in_active_spot,
    no_weakness_passive,
    protect_next_turn,
    retreat_free_when,
    takes_less_passive,
    team_damage_boost_passive,
)
from spirit.game.card_effects.sm3 import is_fire_energy, is_gx_or_ex, is_psychic_energy
from spirit.game.card_effects.sm5 import _direct_evolves_from
from spirit.game.card_effects.sm8 import LostOutPassive
from spirit.game.card_effects.sm10 import is_metal_energy
from spirit.game.card_effects.pokemon import delayed_knockout
from spirit.game.card_effects.support_common import (
    attach_from_discard,
    distribute_energy,
    draw_attack,
    look_at_top,
    requires_bench_space,
    search_attach_energy,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    deck_nonempty, is_basic_energy_card, is_energy_card,
)


_BURNED = SpecialConditions.BURNED
_CONFUSED = SpecialConditions.CONFUSED
_ASLEEP = SpecialConditions.ASLEEP


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _typed(card, pokemon_type: PokemonTypes) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return pokemon_type.value in types


def is_water_pokemon(card) -> bool:
    return is_pokemon_card(card) and _typed(card, PokemonTypes.WATER)


def is_grass_or_fire(pokemon) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return (PokemonTypes.GRASS.value in types
            or PokemonTypes.FIRE.value in types)


def is_latios(pokemon) -> bool:
    return _logic_name(pokemon) in ("Latios", "LatiosGX")


def is_deoxys(pokemon) -> bool:
    return _logic_name(pokemon) == "Deoxys"


def is_passimian(pokemon) -> bool:
    return _logic_name(pokemon) == "Passimian"


def is_meltan(card) -> bool:
    return is_pokemon_card(card) and _logic_name(card) == "Meltan"


def is_gx_pokemon(card) -> bool:
    return is_pokemon_card(card) and "GX" in subtypes_for(
        getattr(card, "archetype_id", None))


def evolves_from_eevee(card) -> bool:
    chain = evolves_from_chain(getattr(card, "archetype_id", None))
    return bool(chain) and chain[0] in ("Eevee", "EeveeGX")


def evolves_from_unidentified_fossil(card) -> bool:
    return is_pokemon_card(card) and _direct_evolves_from(card, "UnidentifiedFossil")


def _own_stadium_in_play(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return False
    owner = stadium.owning_player_id or getattr(stadium, "home_player_id", None)
    return owner == ctx.player_id


def _exactly_n_prizes(n, side="mine"):
    def cond(ctx) -> bool:
        return count_prizes_remaining(side)(ctx) == n
    return cond


def _water_healed_this_turn(ctx) -> bool:
    healed = getattr(ctx.session.turn_state, "healed_entities", None) or set()
    return any(
        p.entity_id in healed and is_water_pokemon(p)
        for p in ctx.my_pokemon_in_play()
    )


def _total_prizes_at_most_6(ctx) -> bool:
    return (count_prizes_remaining("mine")(ctx)
            + count_prizes_remaining("opponent")(ctx)) <= 6


# ----------------------------------------------------------------------
# Passives
# ----------------------------------------------------------------------

class HighDensityArmorPassive(Passive):
    """If this Pokémon has full HP, it takes 90 less from opposing attacks."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.target is not carrier:
            return
        if carrier.get_attribute(AttrID.HP, 0) < effective_max_hp(calc.board, carrier):
            return
        calc.amount = max(0, calc.amount - 90)


class TimeRecallPassive(Passive):
    """Each of your evolved Pokémon can use attacks from tucked previous Evolutions."""

    def granted_attacks(self, board, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return []
        attacks = []
        seen = set()
        for child in pokemon.children:
            if not isinstance(child, PokemonEntity):
                continue
            for ability in getattr(def_for(child.archetype_id), "abilities", None) or []:
                if not isinstance(ability, Attack):
                    continue
                key = (ability.title, ability.game_text)
                if key in seen:
                    continue
                seen.add(key)
                attacks.append(ability)
        return attacks


high_density_armor_passive = HighDensityArmorPassive()
time_recall_passive = TimeRecallPassive()
pressure_passive = takes_less_passive(
    20,
    protects=lambda target, carrier: (
        is_in_active_spot(carrier)
        and target.owning_player_id != carrier.owning_player_id
        and is_in_active_spot(target)
    ),
)
sunny_day_passive = team_damage_boost_passive(20, attacker_pred=is_grass_or_fire)
shining_mane_passive = no_weakness_passive(protects="team")
flight_support_passive = retreat_free_when(
    lambda pokemon, carrier: (
        pokemon.owning_player_id == carrier.owning_player_id
        and is_latios(pokemon)
    )
)


# ----------------------------------------------------------------------
# Ability effects
# ----------------------------------------------------------------------

def _ascension_dna_candidates(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return [c for c in (hand.children if hand else []) if evolves_from_eevee(c)]


def ascension_dna_condition(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    if ts is None or ts.turn_number <= 2 or pokemon is None:
        return False
    if ts.entered_play_turn.get(pokemon.entity_id, 0) >= ts.turn_number:
        return False
    return bool(_ascension_dna_candidates(board, player_id))


async def ascension_dna(ctx):
    """Heal this Pokémon, then evolve it into an Eevee evolution from hand."""
    candidates = [c for c in ctx.hand() if evolves_from_eevee(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Choose a Pokémon that evolves from Eevee")
    if not picks:
        return
    damage = max(0, ctx.max_hp(ctx.source) - ctx.source.get_attribute(AttrID.HP, 0))
    if damage:
        await ctx.heal(damage, ctx.source)
    await ctx.evolve_pokemon(ctx.source, picks[0])


async def cursed_body(ctx):
    """If Active and damaged by an opponent's attack, Confuse the attacker."""
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.apply_special_condition(attacker, _CONFUSED)


def elusive_master_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    if not hand or len(hand.children) != 1:
        return False
    return requires_bench_space(1)(board, player_id)


async def elusive_master(ctx):
    """Last card in hand: play onto the Bench and draw 3."""
    if not await ctx.ask_yes_no("Play this Pokémon onto your Bench and draw 3 cards?"):
        return
    if await ctx.bench_pokemon(ctx.source):
        await ctx.draw_cards(3)


async def golden_wing(ctx):
    """Active KO by opponent attack: move up to 2 basic Energy to the Bench."""
    if not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    energies = [e for e in (ctx.ko_energies or []) if is_basic_energy_card(e)]
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    picks = await ctx.choose_cards(
        energies, min(2, len(energies)), minimum=0,
        prompt="Choose up to 2 basic Energy to move",
    )
    if picks:
        await distribute_energy(ctx, picks, bench)


def hydrating_drops_condition(board, player_id, pokemon=None) -> bool:
    active = board.active_pokemon(player_id)
    if active is None or not is_water_pokemon(active):
        return False
    return active.get_attribute(AttrID.HP, 0) < effective_max_hp(board, active)


async def hydrating_drops(ctx):
    """Heal 30 damage from your Active Water Pokémon."""
    active = ctx.my_active()
    if active is None or not is_water_pokemon(active):
        return
    await ctx.heal(30, active)


def power_suction_condition(board, player_id, pokemon=None) -> bool:
    pokes = board.pokemon_in_play(player_id)
    dests = [p for p in pokes if is_deoxys(p)]
    if not dests:
        return False
    dest_ids = {p.entity_id for p in dests}
    return any(
        board.attached_energies(p) and p.entity_id not in dest_ids
        for p in pokes
    ) or (len(dests) >= 2 and any(board.attached_energies(p) for p in dests))


async def power_suction(ctx):
    """Move an Energy from 1 of your Pokémon to 1 of your Deoxys."""
    dests = [p for p in ctx.my_pokemon_in_play() if is_deoxys(p)]
    if not dests:
        return
    await ctx.move_energy_freely(
        ctx.my_pokemon_in_play(), dests, max_count=1,
        prompt="Choose an Energy to move to a Deoxys",
    )


def troubleshooting_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None:
        return False
    return any(is_special_energy(e) for e in board.attached_energies(pokemon))


async def troubleshooting(ctx):
    """Discard a Special Energy from this Pokémon; if you do, heal 80."""
    special = [e for e in ctx.attached_energies(ctx.source) if is_special_energy(e)]
    if not special:
        return
    picks = await ctx.choose_cards(
        special, 1, prompt="Discard a Special Energy from this Pokémon")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.heal(80, ctx.source)


# ----------------------------------------------------------------------
# Attack effects
# ----------------------------------------------------------------------

abnormal_overheating = condition_attack(self_conditions=(_BURNED,))
aero_force = self_energy_discard_attack(count=1)
doom_crush = self_energy_discard_attack(count=1, energy_type=PokemonTypes.DARKNESS)
enraged_strike = condition_bonus_attack(80, _CONFUSED)
jumping_side_kick = condition_bonus_attack(90, _CONFUSED)
hypnotic_blizzard = condition_attack(_ASLEEP, also=spread_damage(20))
spark = snipe_attack(10, also_base=True)
thundering_hurricane_gx = flip_damage(coins=4, per_heads=100)
swift_bolt_strike = flip_damage(coins=2, bonus_per_heads=60)
thunder = flip_damage(tails_self_damage=20)
pulverizing_pancake_gx = condition_attack(self_conditions=(_ASLEEP,))
psychic_nova_gx = protect_next_turn(prevent=True)
familial_combo_gx = draw_attack(5)
brilliant_deduction = look_at_top(4, take=1, rest="shuffle")
exploder = search_attach_energy(is_fire_energy, count=3)
multiply = search_to_bench(is_meltan, count=1, prompt="Choose a Meltan to put onto your Bench.")
iron_force_gx = attach_from_discard(
    is_metal_energy, count=99, target="self", minimum=0,
    prompt="Attach Metal Energy from your discard pile",
)
power_burner_gx = damage_per(count_discard("mine", is_fire_energy), 20)
rusty_claws = bonus_if(_exactly_n_prizes(1, "opponent"), 100)
territorial_strike = bonus_if(_own_stadium_in_play, 0, else_nothing=True)
shining_current = bonus_if(_water_healed_this_turn, 60)
dusk_shot = snipe_attack(60, pool=is_gx_or_ex, apply_modifiers=False)


async def metal_blast(ctx):
    """Printed damage +20 per Metal Energy attached."""
    await damage_per(count_energy("self", PokemonTypes.METAL), 20, base=_printed(ctx))(ctx)


async def team_play(ctx):
    """Printed damage +30 per Benched Passimian."""
    n = sum(1 for p in ctx.my_bench() if is_passimian(p))
    await ctx.deal_damage(_printed(ctx) + 30 * n)


async def joy_maker_gx(ctx):
    """Put 3 cards from your discard pile into your hand."""
    cards = list(ctx.discard_pile())
    if not cards:
        return
    n = min(3, len(cards))
    picks = await ctx.choose_cards(
        cards, n, minimum=n,
        prompt="Choose 3 cards to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)


async def big_throw_gx(ctx):
    """Discard the opponent's Active and all attached cards (not a Knock Out)."""
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_cards(full_stack(target))

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


async def dark_mist_gx(ctx):
    """Put 1 of the opponent's Benched Pokémon (and attachments) into their hand."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    picks = await ctx.choose_cards(
        bench, 1, prompt="Choose a Benched Pokémon to put into your opponent's hand")
    for target in picks:
        await ctx.put_in_hand(full_stack(target), reveal=False)


async def lost_boomerang_gx(ctx):
    """50 to 2 of the opponent's Pokémon, ignore W/R; KOs go to the Lost Zone."""
    ctx.add_temporary_passive(
        ctx.attacker, LostOutPassive(),
        expires_after_turn=ctx.session.turn_state.turn_number,
    )
    await snipe_attack(50, pool="any", count=2, apply_modifiers=False)(ctx)


async def pale_moon_gx(ctx):
    """Delayed KO at the end of the opponent's next turn; extra Psychic discards Energy."""
    await delayed_knockout(ctx)
    if has_extra_energy(1, PokemonTypes.PSYCHIC)(ctx):
        target = ctx.opponent_active()
        if target is not None and not ctx.effects_blocked(target):
            await ctx.discard_energy_from(
                target, 99, prompt="Discard all Energy from the Defending Pokémon")


async def call_for_greatness(ctx):
    """Search up to 3 Pokémon-GX with different names."""
    used = set()
    found = []
    for _ in range(3):
        def pred(card, used_names=used):
            if not is_gx_pokemon(card):
                return False
            name = _logic_name(card)
            return bool(name) and name not in used_names
        picks = await ctx.search_deck(
            pred, count=1, minimum=0,
            prompt="Choose a Pokémon-GX with a different name")
        if not picks:
            break
        used.add(_logic_name(picks[0]))
        found.extend(picks)
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


async def find_a_friend(ctx):
    """Flip a coin. If heads, search for a Pokémon."""
    results = await ctx.flip_coins(1, "Find a Friend")
    if results and results[0]:
        await search_to_hand(
            is_pokemon_card, count=1, reveal=True,
            prompt="Choose a Pokémon to put into your hand.",
        )(ctx)


async def nasty_plot(ctx):
    """Flip a coin. If heads, search for a card."""
    results = await ctx.flip_coins(1, "Nasty Plot")
    if results and results[0]:
        await search_to_hand(
            None, count=1, reveal=False,
            prompt="Choose a card to put into your hand.",
        )(ctx)


async def gulf_stream(ctx):
    """+20 per damage counter if you have exactly 6 Prize cards remaining."""
    extra = 0
    if count_prizes_remaining()(ctx) == 6:
        extra = 20 * damage_counters_on()(ctx)
    await ctx.deal_damage(_printed(ctx) + extra)


async def heat_stage(ctx):
    """Printed damage, then attach up to 3 Fire Energy from hand."""
    await ctx.deal_damage()
    pool = [c for c in ctx.hand() if is_fire_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, min(3, len(pool)), minimum=0,
        prompt="Attach up to 3 Fire Energy from your hand")
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


async def liberation_gx(ctx):
    """Reveal the opponent's hand; 120 damage per Energy card there."""
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    n = sum(1 for c in ctx.hand(ctx.opponent_id) if is_energy_card(c))
    if n:
        await ctx.deal_damage(120 * n)


async def luster_purge(ctx):
    """Printed damage; on tails, discard all Energy from this Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Luster Purge")
    if results and not results[0]:
        await ctx.discard_energy_from(
            ctx.attacker, 99, prompt="Discard all Energy from this Pokémon")


async def mist_ball(ctx):
    """Printed damage; on tails, discard a Fire Energy and a Psychic Energy."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Mist Ball")
    if not results or results[0]:
        return
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_fire_energy,
        prompt="Discard a Fire Energy from this Pokémon")
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_psychic_energy,
        prompt="Discard a Psychic Energy from this Pokémon")


async def nonahex(ctx):
    """If the Defending Pokémon has exactly 9 damage counters, Knock it Out."""
    if damage_counters_on("defender")(ctx) == 9:
        await ctx.knock_out(ctx.defender)


async def psycho_boost(ctx):
    """Printed damage; next turn, Psycho Boost's base damage is 50."""
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, -50, attack_title="Psycho Boost")


async def queens_command_gx(ctx):
    """The opponent discards 4 cards from their hand."""
    n = min(4, ctx.hand_size(ctx.opponent_id))
    if n:
        await ctx.discard_from_hand(
            n, minimum=n, player_id=ctx.opponent_id,
            prompt="Discard 4 cards from your hand")


async def raging_destruction(ctx):
    """Discard the top 8; attach any Fire Energy among them to this Pokémon."""
    top = list(ctx.deck_top(8))
    await ctx.discard_cards(top)
    fires = [c for c in top if is_fire_energy(c)]
    for energy in fires:
        await ctx.attach_energy(energy, ctx.attacker)


async def shadowy_echoes(ctx):
    """Put a Basic Pokémon from each discard pile onto its owner's Bench."""
    for pid in (ctx.player_id, ctx.opponent_id):
        bench = ctx.board.find_player_area(pid, "bench")
        if bench is None or len(bench.children) >= BENCH_CAPACITY:
            continue
        basics = [c for c in ctx.discard_pile(pid) if is_basic_pokemon(c)]
        if not basics:
            continue
        picks = await ctx.choose_cards(
            basics, 1, minimum=1,
            prompt="Choose a Basic Pokémon to put onto the Bench")
        if picks:
            await ctx.bench_pokemon(picks[0])


async def shining_burst(ctx):
    """If remaining Prizes total 6 or less, discard all Energy and do +100."""
    extra = 0
    if _total_prizes_at_most_6(ctx):
        extra = 100
        await ctx.discard_energy_from(
            ctx.attacker, 99, prompt="Discard all Energy from this Pokémon")
    await ctx.deal_damage(_printed(ctx) + extra)


async def spiky_storm_gx(ctx):
    """100 damage to each of the opponent's Pokémon that has damage counters."""
    for pokemon in ctx.opponent_pokemon_in_play():
        if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon):
            await ctx.deal_damage(100, target=pokemon)


async def stone_age_gx(ctx):
    """Bench any number of Pokémon that evolve from Unidentified Fossil from discard."""
    space = BENCH_CAPACITY - len(ctx.my_bench())
    pool = [c for c in ctx.discard_pile() if evolves_from_unidentified_fossil(c)]
    if space <= 0 or not pool:
        return
    picks = await ctx.choose_cards(
        pool, min(space, len(pool)), minimum=0,
        prompt="Put Pokémon that evolve from Unidentified Fossil onto your Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


async def thunderous_rain_gx(ctx):
    """100 to each of the opponent's Pokémon that has any Energy attached."""
    for pokemon in ctx.opponent_pokemon_in_play():
        if ctx.attached_energies(pokemon):
            await ctx.deal_damage(100, target=pokemon)


async def yank_out(ctx):
    """Discard random cards from the opponent's hand until they have 5."""
    while ctx.hand_size(ctx.opponent_id) > 5:
        discarded = await discard_random_from_hand(ctx, ctx.opponent_id, 1)
        if not discarded:
            break


async def bullet_uppercut(ctx):
    """+60 vs GX/EX; this attack's damage isn't affected by Weakness."""
    bonus = 60 if ctx.defender is not None and is_gx_or_ex(ctx.defender) else 0
    await ctx.deal_damage(_printed(ctx) + bonus, ignore_weakness=True)


async def critical_error_gx(ctx):
    """Search the deck for up to 10 cards and discard them."""
    picks = await ctx.search_deck(
        None, count=10, minimum=0,
        prompt="Choose up to 10 cards to discard")
    await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


async def cure_shower_gx(ctx):
    """Heal all damage from all of your Water Pokémon."""
    for pokemon in ctx.my_pokemon_in_play():
        if is_water_pokemon(pokemon):
            await ctx.heal(ctx.max_hp(pokemon), pokemon)


# ----------------------------------------------------------------------
# Trainers / stadiums
# ----------------------------------------------------------------------

def champions_festival_condition(board, player_id, stadium=None) -> bool:
    return len(board.pokemon_in_play(player_id)) == 6


async def champions_festival(ctx):
    """Heal 10 damage from each of your Pokémon."""
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10, pokemon)


CHAMPIONS_FESTIVAL_ABILITY = Ability(
    title="Champions Festival",
    game_text="Once during each player's turn, if that player has 6 Pokémon in play, they may heal 10 damage from each of their Pokémon.",
    activation=Activations.ONCE_PER_TURN,
    effect=champions_festival,
    condition=champions_festival_condition,
)


def sabrina_brycen_condition(board, player_id) -> bool:
    return deck_nonempty(board, player_id)


async def sabrina_brycen(ctx):
    """Search up to 2 basic Energy; optional discard 5 other to also search 3 Pokémon of different types."""
    extra = False
    others = list(ctx.hand())
    if len(others) >= 5 and await ctx.ask_yes_no(
            "Discard 5 other cards to also search for up to 3 Pokémon of different types?"):
        picks = await ctx.choose_cards(
            others, 5, minimum=5, prompt="Discard 5 other cards from your hand")
        if len(picks) >= 5:
            await ctx.discard_cards(picks)
            extra = True
    energies = await ctx.search_deck(
        is_basic_energy_card, count=2, minimum=0,
        prompt="Choose up to 2 basic Energy cards")
    pokemon_picks = []
    if extra:
        used_types = set()
        for _ in range(3):
            def pred(card, used=used_types):
                if not is_pokemon_card(card):
                    return False
                types = set(card.get_attribute(AttrID.POKEMON_TYPES) or [])
                return bool(types) and types.isdisjoint(used)
            found = await ctx.search_deck(
                pred, count=1, minimum=0,
                prompt="Choose a Pokémon of a different type")
            if not found:
                break
            used_types.update(found[0].get_attribute(AttrID.POKEMON_TYPES) or [])
            pokemon_picks.extend(found)
    await ctx.put_in_hand(energies + pokemon_picks, reveal=True)
    await ctx.shuffle_deck()
