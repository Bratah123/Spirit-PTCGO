"""Unified Minds (SM11) attack, ability, trainer, tool, energy, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

import random

from spirit.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonTypes, SpecialConditions,
    TrainerType,
)
from spirit.game.content.definitions import CARD_DEFS_BY_GUID, looks_like_gx_attack
from spirit.game.data_utils import (
    Ability, Activations, Attack, Triggers, def_for, evolves_from_chain,
    is_tag_team, is_ultra_beast,
)
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_stage1_pokemon,
    is_stage2_pokemon,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import (
    _printed,
    bonus_if,
    count_bench,
    count_discard,
    count_energy,
    count_in_play,
    count_prizes_remaining,
    damage_per,
    discard_for_bonus,
    discard_random_from_hand,
    flip_damage,
    has_attack_titled,
    has_extra_energy,
    mill_attack,
    self_energy_discard_attack,
    snipe_attack,
    GxAttackLockPassive,
)
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost,
    is_in_active_spot,
    no_weakness_passive,
    protect_next_turn,
    retreat_discount,
    retreat_free_when,
    takes_less_passive,
)
from spirit.game.card_effects.pokemon import devolvable, energy_provides_type
from spirit.game.card_effects.sm3 import (
    TakesMorePassive,
    is_darkness_energy,
    is_fire_energy,
    is_grass_energy,
    is_gx_or_ex,
    is_tool_card,
    is_water_energy,
)
from spirit.game.card_effects.sm4 import pokemon_has_ability
from spirit.game.card_effects.sm5 import _direct_evolves_from
from spirit.game.card_effects.sm8 import is_grass_pokemon
from spirit.game.card_effects.sm9 import is_darkness_pokemon, is_psychic_pokemon
from spirit.game.card_effects.sm10 import is_lightning_energy, is_metal_energy
from spirit.game.card_effects.sl import is_benched
from spirit.game.card_effects.support_common import (
    distribute_energy,
    recover_from_discard,
    search_attach_energy,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    deck_nonempty,
    is_basic_energy_card,
    is_energy_card,
)


_ASLEEP = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
_POISONED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)
_TYPE_GUESS_LABELS = [
    ("Grass", PokemonTypes.GRASS),
    ("Fire", PokemonTypes.FIRE),
    ("Water", PokemonTypes.WATER),
    ("Lightning", PokemonTypes.LIGHTNING),
    ("Psychic", PokemonTypes.PSYCHIC),
    ("Fighting", PokemonTypes.FIGHTING),
    ("Darkness", PokemonTypes.DARKNESS),
    ("Metal", PokemonTypes.METAL),
    ("Fairy", PokemonTypes.FAIRY),
    ("Dragon", PokemonTypes.DRAGON),
    ("Colorless", PokemonTypes.COLORLESS),
]


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    return getattr(def_for(getattr(card, "archetype_id", None)), "display_name", "") or ""


def _prize_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _hand(board, player_id):
    area = board.find_player_area(player_id, "hand")
    return list(area.children) if area else []


def _discard(board, player_id):
    area = board.find_player_area(player_id, "discard")
    return list(area.children) if area else []


def _is_damaged(ctx, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)


def _typed(card, pokemon_type: PokemonTypes) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and pokemon_type.value in types


def is_fire_pokemon(card) -> bool:
    return _typed(card, PokemonTypes.FIRE)


def is_active_pokemon(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_in_active_spot(pokemon)


def _is_named(card, name: str) -> bool:
    return _logic_name(card) == name or _display_name(card) == name


def _holder_has_named_attack(title: str):
    pred = has_attack_titled(title)

    def cond(board, player_id, pokemon=None) -> bool:
        return pokemon is not None and pred(pokemon)
    return cond


def _is_basic_darkness_energy(card) -> bool:
    return is_basic_energy_card(card) and is_darkness_energy(card)


def _evolves_from_unidentified_fossil(card) -> bool:
    return is_pokemon_card(card) and _direct_evolves_from(card, "UnidentifiedFossil")


def _is_mistys_favor(card) -> bool:
    return _display_name(card) == "Misty's Favor"


def _is_karate_belt(card) -> bool:
    return _display_name(card) == "Karate Belt"


def _retreat_cost(card) -> int:
    return int(card.get_attribute(AttrID.RETREAT_COST) or 0)


def _is_gx_pokemon(card) -> bool:
    return is_pokemon_card(card) and "GX" in (getattr(def_for(card.archetype_id), "subtypes", None) or [])


def _bench_named(ctx, name: str) -> bool:
    return any(_is_named(p, name) for p in ctx.my_bench())


def _gx_used_last_turn(ctx) -> bool:
    for _eid, _arch, title in ctx.session.turn_state.attacks_used_last_turn:
        if looks_like_gx_attack(title or "", "more than 1 GX attack"):
            return True
        if (title or "").rstrip().endswith("GX"):
            return True
    return False


async def _discard_pokemon_stack(ctx, pokemon) -> bool:
    if pokemon is None or ctx.effects_blocked(pokemon):
        return False
    owner = pokemon.owning_player_id or ctx.opponent_id
    was_active = pokemon is ctx.board.active_pokemon(owner)
    await ctx.discard_cards(full_stack(pokemon))

    async def _promote():
        if not await ctx.session._promote_new_active(owner):
            screen_name = ctx.session.players[owner].screen_name
            winner = ctx.player_id if owner == ctx.opponent_id else ctx.opponent_id
            await ctx.session.end_game(winner, f"{screen_name} has no Pokémon left")
    if was_active:
        ctx.deferred_actions.append(_promote)
    return True


async def _shuffle_self_into_deck(ctx):
    attacker = ctx.attacker
    owner = attacker.owning_player_id or ctx.player_id
    was_active = attacker is ctx.board.active_pokemon(owner)
    await ctx.shuffle_into_deck(full_stack(attacker), owner)

    async def _promote():
        if not await ctx.session._promote_new_active(owner):
            screen_name = ctx.session.players[owner].screen_name
            winner = ctx.opponent_id if owner == ctx.player_id else ctx.player_id
            await ctx.session.end_game(winner, f"{screen_name} has no Pokémon left")
    if was_active:
        ctx.deferred_actions.append(_promote)


# ----------------------------------------------------------------------
# Passives
# ----------------------------------------------------------------------

class AncientCustomPassive(Passive):
    """Opponent Pokémon Tools have no effect."""

    def suppresses_tool(self, tool, carrier):
        holder = carrier_pokemon(tool)
        if holder is None:
            return False
        return holder.owning_player_id != carrier.owning_player_id


class AvengingAuraPassive(Passive):
    """+80 to the opponent's Active when this Pokémon has more prizes remaining."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or carrier_pokemon(carrier) is not attacker:
            return
        me = attacker.owning_player_id
        opp = _other_player(calc.board, me)
        if opp is None or _prize_count(calc.board, me) <= _prize_count(calc.board, opp):
            return
        calc.amount += 80


class CellularCompanionsPassive(Passive):
    """Benched Zygarde: allied Zygarde / Zygarde-GX attacks do +20 to Active."""

    def modify_damage_dealt(self, calc, carrier):
        if not is_benched(carrier):
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != carrier.owning_player_id:
            return
        if _logic_name(attacker) not in ("Zygarde", "ZygardeGX"):
            return
        calc.amount += 20


class DoubleTypePassive(Passive):
    """This Pokémon is Lightning and Metal type."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        return [PokemonTypes.LIGHTNING.value, PokemonTypes.METAL.value]


class DurableBladePassive(Passive):
    """KO by opponent attack damage: this Pokémon goes to hand, attachments discard."""

    def knockout_destination(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return None
        if getattr(pokemon, "ko_by_opponent_attack_damage", False):
            return "hand"
        return None


class LazyHowlPassive(Passive):
    """If the holder is attached Energy from hand, that player's turn ends."""

    def ends_turn_on_energy_attach(self, pokemon, attaching_player_id, energy, carrier):
        holder = carrier_pokemon(carrier)
        return holder is pokemon and attaching_player_id == pokemon.owning_player_id


class NatureWaveCostPassive(Passive):
    """Nature Wave ({Water:2, Colorless:1}) costs Colorless when the opponent has an Ultra Beast."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if cost.get("Water") != 2 or cost.get("Colorless") != 1 or len(cost) != 2:
            return cost
        opp = _other_player(board, pokemon.owning_player_id)
        if opp is None:
            return cost
        if not any(is_ultra_beast(p.archetype_id) for p in board.pokemon_in_play(opp)):
            return cost
        return {"Colorless": 1}


class PerfectionPassive(Passive):
    """Use attacks of Pokémon-GX / Pokémon-EX on the Bench or in the discard pile."""

    def granted_attacks(self, board, pokemon, carrier):
        if carrier is not pokemon:
            return []
        attacks = []
        seen = set()

        def _add(card):
            if not is_gx_or_ex(card):
                return
            for ability in getattr(def_for(card.archetype_id), "abilities", None) or []:
                if not isinstance(ability, Attack):
                    continue
                key = (ability.title, ability.game_text)
                if key in seen:
                    continue
                seen.add(key)
                attacks.append(ability)

        for ally in board.pokemon_in_play(pokemon.owning_player_id):
            if ally is pokemon or not is_benched(ally):
                continue
            _add(ally)
        discard = board.find_player_area(pokemon.owning_player_id, "discard")
        for card in (discard.children if discard else []):
            _add(card)
        return attacks


def _in_play_count(pokemon) -> int:
    if pokemon is None or pokemon.parent is None or pokemon.parent.parent is None:
        return 0
    player_area = pokemon.parent.parent
    n = 0
    for sub in player_area.children:
        if sub.get_attribute(AttrID.NAME) not in ("activePokemonArea", "bench"):
            continue
        n += len(sub.children)
    return n


class PowerBindPassive(Passive):
    """Can't attack with 4 or fewer Pokémon in play."""

    def blocks_attacks(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        return _in_play_count(pokemon) <= 4


class PrimalWindsPassive(Passive):
    """While Active, opponent's Basic Pokémon's attacks cost Colorless more."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        if me is None or not is_in_active_spot(me):
            return cost
        if pokemon.owning_player_id == me.owning_player_id:
            return cost
        if not is_basic_pokemon(pokemon):
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


class PsychicZonePassive(Passive):
    """Don't apply Psychic Weakness."""

    def modify_weakness(self, calc, carrier):
        if PokemonTypes.PSYCHIC.value in (calc.weak_types or []):
            calc.weakness_applies = False


class SecretTerritoryPassive(Passive):
    """With Mesprit and Azelf in play, Weakness is ×4."""

    def modify_weakness(self, calc, carrier):
        owner = carrier.owning_player_id
        if owner is None:
            return
        names = {_logic_name(p) for p in calc.board.pokemon_in_play(owner)}
        if "Mesprit" in names and "Azelf" in names:
            calc.weakness_multiplier = 4


class TagPurgePassive(Passive):
    """Prevent damage from TAG TEAM attacks."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        attacker = calc.attacker
        return attacker is not None and is_tag_team(attacker.archetype_id)


class GigatonShakePassive(Passive):
    """The carrier's owner's Pokémon can't attack."""

    def blocks_attacks(self, pokemon, carrier):
        return pokemon.owning_player_id == carrier.owning_player_id


class BlizzardTownPassive(Passive):
    """Pokémon with 40 HP or less remaining can't attack."""

    def blocks_attacks(self, pokemon, carrier):
        return pokemon.get_attribute(AttrID.HP, 0) <= 40


class SlumberingForestPassive(Passive):
    """Asleep Pokémon flip 2 coins to wake."""

    def sleep_checkup_coins(self, pokemon, carrier):
        return 2


class KarateBeltPassive(Passive):
    """Attacks cost Fighting less when you have more prizes remaining."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        me = pokemon.owning_player_id
        opp = _other_player(board, me)
        if opp is None or _prize_count(board, me) <= _prize_count(board, opp):
            return cost
        if "Fighting" not in cost:
            return cost
        remaining = cost["Fighting"] - 1
        if remaining > 0:
            cost["Fighting"] = remaining
        else:
            del cost["Fighting"]
        return cost


ancient_custom_passive = AncientCustomPassive()
avenging_aura_passive = AvengingAuraPassive()
blanket_weaver_passive = takes_less_passive(
    40,
    protects=lambda target, carrier: (
        target.owning_player_id == carrier.owning_player_id
        and is_grass_pokemon(target)
    ),
    stack_key="Blanket Weaver",
)
cellular_companions_passive = CellularCompanionsPassive()
double_type_passive = DoubleTypePassive()
durable_blade_passive = DurableBladePassive()
emergency_exit_passive = retreat_free_when(
    lambda pokemon, carrier: (
        carrier_pokemon(carrier) is pokemon
        and sum(1 for c in pokemon.children if is_energy_card(c)) <= 2
    )
)
nature_wave_cost_passive = NatureWaveCostPassive()
perfection_passive = PerfectionPassive()
power_bind_passive = PowerBindPassive()
primal_winds_passive = PrimalWindsPassive()
psychic_zone_passive = PsychicZonePassive()
secret_territory_passive = SecretTerritoryPassive()
tag_coach_passive = takes_less_passive(
    20,
    protects=lambda target, carrier: (
        target.owning_player_id == carrier.owning_player_id
        and is_tag_team(target.archetype_id)
    ),
)
blizzard_town_passive = BlizzardTownPassive()
dark_city_passive = retreat_free_when(
    lambda pokemon, carrier: is_basic_pokemon(pokemon) and is_darkness_pokemon(pokemon)
)
slumbering_forest_passive = SlumberingForestPassive()
karate_belt_passive = KarateBeltPassive()
uturn_board_passive = retreat_discount(1)
weakness_guard_passive = no_weakness_passive()


# ----------------------------------------------------------------------
# Attack effects
# ----------------------------------------------------------------------

async def alert_headbutt(ctx):
    amount = 30 if ctx.defender is not None and is_gx_or_ex(ctx.defender) else _printed(ctx)
    await ctx.deal_damage(amount)


async def avenging_heart(ctx):
    taken = ctx.session.turn_state.prizes_taken_last_turn.get(ctx.opponent_id, 0)
    await ctx.deal_damage(_printed(ctx) + 50 * taken)


async def big_eater_gx(ctx):
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    supporters = [c for c in cards if is_supporter_card(c)]
    if supporters:
        await ctx.discard_cards(supporters)


async def black_lance(ctx):
    await ctx.deal_damage()
    pool = [p for p in ctx.opponent_bench() if is_gx_or_ex(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Benched Pokémon-GX or Pokémon-EX")
    if target is not None:
        await ctx.deal_damage(60, target=target, apply_modifiers=False)


async def boost_fang(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = [c for c in ctx.discard_pile()
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIGHTING.value)]
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Attach a Fighting Energy from your discard pile")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def cavern_counter(ctx):
    bench = ctx.my_bench()
    extra = 150 if bench and all(_is_damaged(ctx, p) for p in bench) else 0
    await ctx.deal_damage(_printed(ctx) + extra)


async def cleaning_up(ctx):
    holders = [p for p in ctx.opponent_pokemon_in_play()
               if any(is_tool_card(c) for c in p.children)]
    if not holders:
        return
    target = await ctx.choose_pokemon(holders, "Choose a Pokémon with a Tool")
    if target is None:
        return
    tools = [c for c in target.children if is_tool_card(c)]
    picks = await ctx.choose_cards(tools, 1, prompt="Discard a Pokémon Tool")
    if picks:
        await ctx.discard_cards(picks)


async def clear_vision_gx(ctx):
    ctx.add_global_passive(GxAttackLockPassive(ctx.opponent_id), 10 ** 9)


async def cross_division_gx(ctx):
    n = 20 if has_extra_energy(3)(ctx) else 10
    await ctx.place_damage_counters(n)


async def cross_poison(ctx):
    results = await ctx.flip_coins(4, "Cross Poison")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(50 * heads)
    if heads >= 2 and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


async def dark_moon_gx(ctx):
    ctx.lock_plays(ctx.opponent_id, is_trainer_card)
    if has_extra_energy(5, PokemonTypes.DARKNESS)(ctx):
        await ctx.knock_out(ctx.opponent_active())


ditch_and_splash = discard_for_bonus(
    source="hand", predicate=is_supporter_card, max_count=99, per=40, base=0)


async def downburst(ctx):
    await ctx.deal_damage()
    if not await ctx.ask_yes_no(
            "Have each player shuffle all cards attached to their Active Pokémon into their deck?"):
        return
    for poke in (ctx.my_active(), ctx.opponent_active()):
        if poke is None:
            continue
        if poke is ctx.opponent_active() and ctx.effects_blocked(poke):
            continue
        attached = [c for c in full_stack(poke) if c is not poke]
        if attached:
            await ctx.shuffle_into_deck(attached, poke.owning_player_id)


dragon_pulse = mill_attack(1, opponent=False)


async def dynamic_swing(ctx):
    extra = 0
    if await ctx.ask_yes_no(
            "Do 100 more damage? During your opponent's next turn, this Pokémon takes 100 more damage."):
        extra = 100
        ctx.add_passive_through_opponents_turn(ctx.attacker, TakesMorePassive(100))
    await ctx.deal_damage(_printed(ctx) + extra)


async def electro_rain(ctx):
    energies = [e for e in ctx.attached_energies(ctx.attacker) if is_lightning_energy(e)]
    picks = await ctx.choose_cards(
        energies, len(energies), minimum=0,
        prompt="Discard Lightning Energy from this Pokémon") if energies else []
    await ctx.discard_cards(picks)
    for _ in picks:
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        target = await ctx.choose_pokemon(pool, "Deal 30 damage to a Pokémon")
        if target is not None:
            await ctx.deal_damage(30, target=target, apply_modifiers=False)


async def energy_arrow(ctx):
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Pokémon for Energy Arrow")
    if target is None:
        return
    n = len(ctx.attached_energies(target))
    if n:
        await ctx.deal_damage(20 * n, target=target, apply_modifiers=False)


evil_admonition = damage_per(
    count_in_play("opponent", pred=pokemon_has_ability), 20, base=10)

find_a_friend = search_to_hand(
    is_fire_pokemon, count=1, reveal=True,
    prompt="Choose a Fire Pokémon.",
)


async def flare_raid(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 1, prompt="Discard an Energy from this Pokémon")
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Deal 50 damage to a Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(50, target=target, apply_modifiers=False)


async def full_clean(ctx):
    await ctx.deal_damage()
    await ctx.discard_cards(list(ctx.hand()))


async def fury_cutter(ctx):
    results = await ctx.flip_coins(3, "Fury Cutter")
    heads = sum(1 for r in results if r)
    extra = {0: 0, 1: 40, 2: 80, 3: 150}.get(heads, 0)
    await ctx.deal_damage(_printed(ctx) + extra)


async def gg_end_gx(ctx):
    n = 2 if has_extra_energy(3, PokemonTypes.FIGHTING)(ctx) else 1
    pool = [p for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, min(n, len(pool)),
        prompt="Discard opponent Pokémon and all cards attached")
    for pokemon in picks:
        await _discard_pokemon_stack(ctx, pokemon)


async def gigafall_gx(ctx):
    await ctx.deal_damage()
    if has_extra_energy(5)(ctx):
        await ctx.discard_cards(ctx.deck_top(15, player_id=ctx.opponent_id))


async def gigaton_shake(ctx):
    await ctx.deal_damage()
    ctx.add_global_passive(
        GigatonShakePassive(),
        ctx.session.turn_state.turn_number + 2,
    )


async def greedy_crush(ctx):
    await ctx.deal_damage()
    ctx.add_extra_prize_watcher(target_predicate=is_gx_or_ex, prizes=1)


async def heavy_draw(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if _retreat_cost(p) == 4)
    if n:
        await ctx.draw_cards(n)


hot_burn_gx = damage_per(count_energy(energy_type=PokemonTypes.FIRE), 50)


async def injection_gx(ctx):
    cards = list(ctx.discard_pile(ctx.opponent_id))
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Add a card to your opponent's Prize cards")
    if picks:
        await ctx.put_in_prizes(picks, player_id=ctx.opponent_id, append=True)


last_scene = bonus_if(
    lambda ctx: (
        count_prizes_remaining()(ctx) == 1
        and count_prizes_remaining("opponent")(ctx) == 1
    ),
    130,
)


async def lazy_howl(ctx):
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.add_passive_through_opponents_turn(defender, LazyHowlPassive())


async def licks_go_crazy(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, 1)
    await ctx.discard_cards(ctx.deck_top(1, player_id=ctx.opponent_id))
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1, prompt="Discard an Energy from the Defending Pokémon")


async def lightning_ride_gx(ctx):
    extra = 100 if has_extra_energy(2, PokemonTypes.LIGHTNING)(ctx) else 0
    await ctx.deal_damage(_printed(ctx) + extra)
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Switch this Pokémon with a Benched Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


live_wire = snipe_attack(50, pool="any", apply_modifiers=True)

luminous_blade = self_energy_discard_attack(count=1, energy_type=PokemonTypes.PSYCHIC)


async def mach_delivery_gx(ctx):
    extra = ctx.hand_size() - 9
    if extra > 0:
        await ctx.discard_from_hand(
            extra, minimum=0, prompt="Discard cards until you have 9 or fewer")
    await ctx.draw_until(10)


master_strike = bonus_if(
    lambda ctx: ctx.attacker is not None and any(
        _is_karate_belt(c) for c in ctx.attacker.children),
    60,
)


async def meal_time(ctx):
    heads = await ctx.flip_until_tails("Meal Time")
    if heads:
        await ctx.draw_cards(heads)


async def miraculous_duo_gx(ctx):
    await ctx.deal_damage()
    if has_extra_energy(1)(ctx):
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(ctx.max_hp(pokemon), pokemon)


multiply = search_to_bench(
    lambda c: _is_named(c, "Sewaddle"), count=2,
    prompt="Choose up to 2 Sewaddle.",
)


async def mysterious_noise(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)
    await _shuffle_self_into_deck(ctx)


async def nature_dive(ctx):
    extra = 0
    discard = False
    if ctx.defender is not None and is_ultra_beast(ctx.defender.archetype_id):
        extra = 100
        discard = True
    await ctx.deal_damage(_printed(ctx) + extra)
    if discard:
        await ctx.discard_energy_from(
            ctx.attacker, 2, prompt="Discard 2 Energy from this Pokémon")


nocturnal_maneuvers_gx = search_to_bench(
    is_basic_pokemon, count=99,
    prompt="Choose Basic Pokémon to put onto your Bench.",
)


async def over_slice(ctx):
    extra = 0
    energies = ctx.attached_energies(ctx.attacker)
    if energies and await ctx.ask_yes_no("Discard an Energy to do 40 more damage?"):
        await ctx.discard_energy_from(
            ctx.attacker, 1, prompt="Discard an Energy from this Pokémon")
        extra = 40
    await ctx.deal_damage(_printed(ctx) + extra)


powerful_axe = damage_per(
    lambda ctx: sum(1 for e in ctx.attached_energies(ctx.attacker)
                    if is_basic_energy_card(e)),
    40, base=10,
)

pre_dawn_strike = bonus_if(
    lambda ctx: ctx.defender is not None and _ASLEEP in (
        ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []),
    90,
)

psychic_club = damage_per(
    count_bench(pred=is_psychic_pokemon), 30, base=10)

async def quick_freeze(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    if any(is_water_energy(e) for e in ctx.attached_energies(defender)):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)


async def raging_thunder(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "This attack does 40 damage to 1 of your Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(40, target=target, apply_modifiers=False)


async def rest_well(ctx):
    for poke in (ctx.my_active(), ctx.opponent_active()):
        if poke is not None:
            await ctx.apply_special_condition(poke, SpecialConditions.ASLEEP)
    await apply_own_next_turn_boost(ctx, 100)


async def rototiller(ctx):
    cards = list(ctx.discard_pile())
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, min(4, len(cards)), prompt="Shuffle 4 cards into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


async def sages_riddle(ctx):
    pokes = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not pokes:
        return
    picks = await ctx.choose_cards(pokes, 1, prompt="Choose a Pokémon to hide")
    if not picks:
        return
    card = picks[0]
    labels = [label for label, _ in _TYPE_GUESS_LABELS]
    idx = await ctx.choose(
        "Guess that Pokémon's type", labels, player_id=ctx.opponent_id)
    if idx is None:
        idx = 0
    guessed = _TYPE_GUESS_LABELS[idx][1]
    actual = card.get_attribute(AttrID.POKEMON_TYPES) or []
    if guessed.value in actual:
        await ctx.draw_cards(4, ctx.opponent_id)
    else:
        await ctx.draw_cards(4)


sol_slice = bonus_if(
    lambda ctx: any(is_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)),
    50,
)

special_laser = bonus_if(
    lambda ctx: any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker)),
    60,
)


async def spirit_burner(ctx):
    cards = ctx.deck_top(5)
    await ctx.discard_cards(cards)
    pokemon = [c for c in cards if is_pokemon_card(c)]
    await ctx.deal_damage(_printed(ctx) + 60 * len(pokemon))
    fires = [c for c in pokemon if is_fire_pokemon(c)]
    space = BENCH_CAPACITY - len(ctx.my_bench())
    if fires and space > 0:
        picks = await ctx.choose_cards(
            fires, min(len(fires), space), minimum=0,
            prompt="Put Fire Pokémon onto your Bench")
        for card in picks:
            await ctx.bench_pokemon(card)


async def spirit_smash(ctx):
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    await ctx.discard_cards(top)
    if top and is_pokemon_card(top[0]):
        hp = top[0].get_attribute(AttrID.HP, 0) or 0
        if hp:
            await ctx.deal_damage(hp)


star_search = search_attach_energy(
    is_energy_card, count=1, target_pred=is_psychic_pokemon,
    prompt="Choose an Energy card to attach to a Psychic Pokémon.",
)


async def super_growth(ctx):
    grasses = [p for p in ctx.my_pokemon_in_play() if is_grass_pokemon(p)]
    names = {_logic_name(p) for p in grasses}

    def _evolves_from_grass(card):
        chain = evolves_from_chain(card.archetype_id)
        return bool(chain) and chain[0] in names and is_pokemon_card(card)

    picks = await ctx.search_deck(
        _evolves_from_grass, count=1, minimum=0,
        prompt="Choose a card that evolves from 1 of your Grass Pokémon.",
    )
    if picks:
        evo = picks[0]
        from_name = evolves_from_chain(evo.archetype_id)[0]
        targets = [p for p in grasses if _logic_name(p) == from_name]
        target = targets[0]
        if len(targets) > 1:
            chosen = await ctx.choose_pokemon(
                targets, "Choose a Grass Pokémon to evolve")
            if chosen is not None:
                target = chosen
        await ctx.evolve_pokemon(target, evo)
        if is_stage1_pokemon(target):
            s2_name = _logic_name(target)
            picks2 = await ctx.search_deck(
                lambda c, n=s2_name: is_stage2_pokemon(c) and _direct_evolves_from(c, n),
                count=1, minimum=0,
                prompt="Choose a Stage 2 Pokémon that evolves from that Pokémon.",
            )
            if picks2:
                await ctx.evolve_pokemon(target, picks2[0])
    await ctx.shuffle_deck()


async def swarming_bites(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if _is_named(p, "Basculin"))
    if n <= 0:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Deal damage to a Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(20 * n, target=target, apply_modifiers=False)


async def tag_cheer(ctx):
    energies = [c for c in ctx.hand() if is_energy_card(c)]
    tags = [p for p in ctx.my_pokemon_in_play() if is_tag_team(p.archetype_id)]
    if not energies or not tags:
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Attach an Energy from your hand")
    if not picks:
        return
    target = await ctx.choose_pokemon(tags, "Choose a TAG TEAM Pokémon")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


tag_impact = damage_per(
    count_in_play(pred=lambda p: is_tag_team(p.archetype_id)), 50)


async def tag_purge(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TagPurgePassive())


async def tandem_shock(ctx):
    extra = 0
    paralyze = ctx.entered_active_this_turn(ctx.attacker)
    if paralyze:
        extra = 80
    await ctx.deal_damage(_printed(ctx) + extra)
    if paralyze and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


three_mirrors = bonus_if(
    lambda ctx: count_prizes_remaining("opponent")(ctx) == 3, 90)


async def thrilling_times_gx(ctx):
    coins = 10 if has_extra_energy(6, PokemonTypes.WATER)(ctx) else 1
    results = await ctx.flip_coins(coins, "Thrilling Times-GX")
    heads = sum(1 for r in results if r)
    await ctx.deal_damage(_printed(ctx) + 100 * heads)


thunderous_gale = bonus_if(lambda ctx: _bench_named(ctx, "Tornadus"), 50)


async def thunderous_tornado(ctx):
    await ctx.deal_damage()
    if _bench_named(ctx, "Thundurus"):
        for pokemon in ctx.opponent_bench():
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


async def time_spiral(ctx):
    candidates = [p for p in ctx.opponent_pokemon_in_play()
                  if devolvable(p) and not ctx.effects_blocked(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Devolve 1 of your opponent's evolved Pokémon")
    if target is None:
        return
    await ctx.devolve_pokemon(target, steps=1, destination="deck")
    await ctx.shuffle_deck(ctx.opponent_id)


trap_bolt = bonus_if(
    lambda ctx: (
        ctx.defender is not None and ctx.attacker is not None
        and ctx.defender.get_attribute(AttrID.HP, 0)
        > ctx.attacker.get_attribute(AttrID.HP, 0)
    ),
    30,
)

trash_slash = damage_per(count_discard(pred=is_item_card), 10, cap=130)


async def tropical_hour_gx(ctx):
    await ctx.deal_damage()
    if not has_extra_energy(3)(ctx):
        return
    moved = []
    for pokemon in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(pokemon):
            continue
        moved.extend(ctx.attached_energies(pokemon))
    if moved:
        await ctx.shuffle_into_deck(moved, ctx.opponent_id)


turf_raid = damage_per(count_prizes_remaining(), 20, base=20)


async def turn_the_tables(ctx):
    if not _gx_used_last_turn(ctx):
        return
    active = ctx.opponent_active()
    if active is None or ctx.effects_blocked(active):
        return
    owner = active.owning_player_id
    was_active = True
    await ctx.shuffle_into_deck(full_stack(active), owner)

    async def _promote():
        if not await ctx.session._promote_new_active(owner):
            screen_name = ctx.session.players[owner].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    if was_active:
        ctx.deferred_actions.append(_promote)


async def venom_shot(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 2, prompt="Discard 2 Energy from this Pokémon")
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Deal 170 damage to a Pokémon")
    if target is not None:
        await ctx.deal_damage(170, target=target, apply_modifiers=False)


venoshock = bonus_if(
    lambda ctx: ctx.defender is not None and _POISONED in (
        ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []),
    70,
)


async def victory_sign(ctx):
    first = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card.",
    )
    cards = list(first)
    if first:
        types = first[0].get_attribute(AttrID.POKEMON_TYPES) or []

        def _other_type(c, blocked=types):
            return is_basic_energy_card(c) and (
                c.get_attribute(AttrID.POKEMON_TYPES) or []) != blocked

        second = await ctx.search_deck(
            _other_type, count=1, minimum=0,
            prompt="Choose a basic Energy card of a different type.",
        )
        cards.extend(second)
    if cards:
        await distribute_energy(ctx, cards, ctx.my_pokemon_in_play())
    await ctx.shuffle_deck()


wild_dive_gx = damage_per(count_energy("defender"), 50)


async def blindside(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if _is_damaged(ctx, p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Deal 60 damage to a Pokémon with damage counters")
    if target is not None:
        await ctx.deal_damage(60, target=target, apply_modifiers=False)


# ----------------------------------------------------------------------
# Ability effects
# ----------------------------------------------------------------------

async def burning_road(ctx):
    if not await ctx.ask_yes_no(
            "Move any number of Fire Energy from your other Pokémon to this Pokémon?"):
        return
    others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    if not others:
        return
    await ctx.move_energy_freely(others, [ctx.source], predicate=is_fire_energy)


async def bursting_spores(ctx):
    incoming = getattr(ctx, "benched_pokemon", None) or getattr(ctx, "evolved_pokemon", None)
    if incoming is None or incoming is ctx.source:
        return
    if getattr(ctx, "benching_player_id", ctx.player_id) not in (
            ctx.player_id, None) and getattr(ctx, "evolved_pokemon", None) is None:
        return
    if getattr(ctx, "benched_pokemon", None) is not None:
        if getattr(ctx, "benching_player_id", None) not in (ctx.player_id, None):
            return
    if not has_attack_titled("Spore")(incoming):
        return
    if not await ctx.ask_yes_no(
            "Leave your opponent's Active Pokémon Asleep and Poisoned?"):
        return
    defender = ctx.opponent_active()
    if defender is None:
        return
    await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)
    await ctx.apply_special_condition(defender, SpecialConditions.POISONED)


async def captivating_wink(ctx):
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    basics = [c for c in cards if is_basic_pokemon(c)]
    space = BENCH_CAPACITY - len(ctx.opponent_bench())
    if not basics or space <= 0:
        return
    if not await ctx.ask_yes_no(
            "Put Basic Pokémon from your opponent's hand onto their Bench?"):
        return
    picks = await ctx.choose_cards(
        basics, min(len(basics), space), minimum=0,
        prompt="Put Basic Pokémon onto your opponent's Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


async def counterattack(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(40, target=attacker, apply_modifiers=False, as_counters=True)


async def dimension_breach(ctx):
    if not await ctx.ask_yes_no(
            "Discard a Special Energy from your opponent's Active Pokémon?"):
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    specials = [e for e in ctx.attached_energies(target) if is_special_energy(e)]
    if not specials:
        return
    picks = await ctx.choose_cards(specials, 1, prompt="Discard a Special Energy")
    if picks:
        await ctx.discard_cards(picks)


async def drowsing(ctx):
    conditions = ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    if _ASLEEP not in conditions:
        return
    target = ctx.opponent_active()
    if target is not None:
        await ctx.deal_damage(60, target=target, as_counters=True)


def electric_swamp_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if bench is None or len(bench.children) >= BENCH_CAPACITY:
        return False
    n = 0
    for poke in board.pokemon_in_play(player_id):
        for child in poke.children:
            if is_lightning_energy(child):
                n += 1
    return n >= 4


async def electric_swamp(ctx):
    source = ctx.source
    if not await ctx.bench_pokemon(source):
        return
    others = [p for p in ctx.my_pokemon_in_play() if p is not source]
    if others:
        await ctx.move_energy_freely(
            others, [source], predicate=is_lightning_energy)


async def grind_up(ctx):
    if ctx.stadium_in_play() is None:
        return
    await ctx.discard_stadium()
    pool = [c for c in ctx.hand() if is_fire_energy(c) or is_metal_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, min(3, len(pool)), minimum=0,
        prompt="Attach Fire and Metal Energy cards to this Pokémon")
    for energy in picks:
        await ctx.attach_energy(energy, ctx.source)


def grind_up_condition(board, player_id, pokemon=None) -> bool:
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


async def hearing(ctx):
    await ctx.draw_cards(1)


def hearing_condition(board, player_id, pokemon=None) -> bool:
    return is_in_active_spot(pokemon) and deck_nonempty(board, player_id)


async def hurricane_charge(ctx):
    waters = [c for c in ctx.hand() if is_water_energy(c)]
    lights = [c for c in ctx.hand() if is_lightning_energy(c)]
    chosen = []
    if waters:
        picks = await ctx.choose_cards(
            waters, 1, minimum=0, prompt="Attach a Water Energy card?")
        chosen.extend(picks)
    remaining_lights = [c for c in lights if c not in chosen]
    if remaining_lights:
        picks = await ctx.choose_cards(
            remaining_lights, 1, minimum=0, prompt="Attach a Lightning Energy card?")
        chosen.extend(picks)
    if chosen:
        await distribute_energy(ctx, chosen, ctx.my_pokemon_in_play())


def hurricane_charge_condition(board, player_id, pokemon=None) -> bool:
    return any(is_water_energy(c) or is_lightning_energy(c)
               for c in _hand(board, player_id))


mermaids_call = recover_from_discard(_is_mistys_favor, count=1, prompt="Choose a Misty's Favor.")


def mermaids_call_condition(board, player_id, pokemon=None) -> bool:
    return any(_is_mistys_favor(c) for c in _discard(board, player_id))


async def ominous_posture(ctx):
    damaged = [p for p in ctx.my_pokemon_in_play() if _is_damaged(ctx, p)]
    others = ctx.my_pokemon_in_play()
    if not damaged or len(others) < 2:
        return
    src = await ctx.choose_pokemon(damaged, "Move a damage counter from which Pokémon?")
    if src is None:
        return
    dests = [p for p in others if p is not src]
    dest = await ctx.choose_pokemon(dests, "Move it to which Pokémon?")
    if dest is None:
        return
    await ctx.heal(10, src)
    await ctx.deal_damage(10, target=dest, as_counters=True)


def ominous_posture_condition(board, player_id, pokemon=None) -> bool:
    in_play = list(board.pokemon_in_play(player_id))
    if len(in_play) < 2:
        return False
    from spirit.game.session.passives import effective_max_hp
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in in_play)


async def peppy_pick(ctx):
    results = await ctx.flip_coins(1, "Peppy Pick")
    if not results or not results[0]:
        return
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    card = random.choice(hand)
    await ctx.shuffle_into_deck([card], ctx.opponent_id)


async def prowl(ctx):
    if not await ctx.ask_yes_no("Search your deck for a card?"):
        return
    await search_to_hand(None, count=1, reveal=False, prompt="Choose a card.")(ctx)


async def queenly_reward(ctx):
    active = ctx.my_active()
    if active is None:
        return
    cards = [c for c in ctx.discard_pile() if is_grass_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Attach a Grass Energy to your Active Pokémon")
    if picks:
        await ctx.attach_energy(picks[0], active)


def queenly_reward_condition(board, player_id, pokemon=None) -> bool:
    active = board.active_pokemon(player_id)
    return active is not None and any(is_grass_energy(c) for c in _discard(board, player_id))


async def shadow_connection(ctx):
    await ctx.move_energy_freely(
        ctx.my_pokemon_in_play(), ctx.my_pokemon_in_play(),
        predicate=_is_basic_darkness_energy, max_count=1,
    )


def shadow_connection_condition(board, player_id, pokemon=None) -> bool:
    in_play = list(board.pokemon_in_play(player_id))
    if len(in_play) < 2:
        return False
    return any(_is_basic_darkness_energy(c) for p in in_play for c in p.children)


async def snack_search(ctx):
    results = await ctx.flip_coins(1, "Snack Search")
    if not results or not results[0]:
        return
    cards = list(ctx.discard_pile())
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Put a card from your discard pile on top of your deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


def snack_search_condition(board, player_id, pokemon=None) -> bool:
    return bool(_discard(board, player_id))


async def tag_transport(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Switch your Active TAG TEAM Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


def tag_transport_condition(board, player_id, pokemon=None) -> bool:
    active = board.active_pokemon(player_id)
    if active is None or not is_tag_team(active.archetype_id):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


async def ultra_conversion(ctx):
    ubs = [c for c in ctx.hand()
           if is_pokemon_card(c) and is_ultra_beast(c.archetype_id)]
    if not ubs:
        return
    picks = await ctx.choose_cards(ubs, 1, prompt="Discard an Ultra Beast card")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.draw_cards(3)


def ultra_conversion_condition(board, player_id, pokemon=None) -> bool:
    return any(is_pokemon_card(c) and is_ultra_beast(c.archetype_id)
               for c in _hand(board, player_id))


# ----------------------------------------------------------------------
# Trainer / stadium / tool effects
# ----------------------------------------------------------------------

async def blaines_quiz_show(ctx):
    pokes = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not pokes:
        return
    picks = await ctx.choose_cards(pokes, 1, prompt="Choose a Pokémon to hide")
    if not picks:
        return
    card = picks[0]
    attacks = [
        a for a in (getattr(def_for(card.archetype_id), "abilities", None) or [])
        if isinstance(a, Attack)
    ]
    if not attacks:
        await ctx.draw_cards(4)
        return
    titles = [a.title for a in attacks]
    idx = await ctx.choose("Tell your opponent the name of an attack", titles)
    if idx is None:
        idx = 0
    attack_name = titles[idx]
    names = sorted({
        getattr(d, "display_name", "") or ""
        for d in CARD_DEFS_BY_GUID.values()
        if has_attack_titled(attack_name)(type("Card", (), {"archetype_id": d.guid})())
    } - {""})
    if not names:
        names = [_display_name(card)]
    guess = await ctx.choose(
        f"Guess the Pokémon that has {attack_name}", names,
        player_id=ctx.opponent_id)
    guessed = names[guess] if guess is not None else names[0]
    if guessed == _display_name(card):
        await ctx.draw_cards(4, ctx.opponent_id)
    else:
        await ctx.draw_cards(4)


def blaines_quiz_show_condition(board, player_id, pokemon=None) -> bool:
    return any(is_pokemon_card(c) for c in _hand(board, player_id))


async def blues_tactics(ctx):
    ctx.session.turn_state.end_of_turn_draw_until[ctx.player_id] = 8


async def channeler(ctx):
    state = ctx.session.turn_state
    state.play_locks.pop(ctx.player_id, None)
    mine = list(ctx.my_pokemon_in_play())
    my_ids = {p.entity_id for p in mine}
    for pokemon in mine:
        eid = pokemon.entity_id
        for key in [k for k in state.attack_locks if k[0] == eid]:
            state.attack_locks.pop(key, None)
        state.retreat_locks.pop(eid, None)
        state.attach_restrictions.pop(eid, None)
        state.attack_flip_checks.pop(eid, None)
        state.ignore_target_effects_entities.discard(eid)
    hand = ctx.board.find_player_area(ctx.player_id, "hand")
    hand_id = hand.entity_id if hand is not None else None
    ctx.board.temporary_passives = [
        tp for tp in ctx.board.temporary_passives
        if tp.carrier_entity_id not in my_ids
        and tp.carrier_entity_id != hand_id
    ]


cherish_ball = search_to_hand(
    _is_gx_pokemon, count=1, reveal=True, prompt="Choose a Pokémon-GX.",
)


async def coach_trainer(ctx):
    n = 2
    active = ctx.my_active()
    if active is not None and is_tag_team(active.archetype_id):
        n = 4
    await ctx.draw_cards(n)


async def giant_hearth(ctx):
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(hand, 1, prompt="Discard a card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await search_to_hand(
        is_fire_energy, count=2, reveal=True,
        prompt="Choose Fire Energy cards.",
    )(ctx)


def giant_hearth_condition(board, player_id, stadium=None) -> bool:
    return bool(_hand(board, player_id)) and deck_nonempty(board, player_id)


async def great_potion(ctx):
    active = ctx.my_active()
    if active is not None and is_gx_or_ex(active):
        await ctx.heal(50, active)


def great_potion_condition(board, player_id) -> bool:
    active = board.active_pokemon(player_id)
    if active is None or not is_gx_or_ex(active):
        return False
    from spirit.game.session.passives import effective_max_hp
    return active.get_attribute(AttrID.HP, 0) < effective_max_hp(board, active)


async def grimsley(ctx):
    damaged = [p for p in ctx.opponent_pokemon_in_play() if _is_damaged(ctx, p)]
    others = ctx.opponent_pokemon_in_play()
    if not damaged or len(others) < 2:
        return
    src = await ctx.choose_pokemon(
        damaged, "Move damage counters from which of your opponent's Pokémon?")
    if src is None:
        return
    dests = [p for p in others if p is not src]
    dest = await ctx.choose_pokemon(dests, "Move them to which Pokémon?")
    if dest is None:
        return
    available = (ctx.max_hp(src) - src.get_attribute(AttrID.HP, 0)) // 10
    n = min(3, available)
    if n <= 0:
        return
    if n > 1:
        labels = [str(i) for i in range(1, n + 1)]
        idx = await ctx.choose("How many damage counters?", labels)
        n = (idx + 1) if idx is not None else n
    await ctx.heal(n * 10, src)
    await ctx.deal_damage(n * 10, target=dest, as_counters=True)


def grimsley_condition(board, player_id) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    in_play = list(board.pokemon_in_play(opp))
    if len(in_play) < 2:
        return False
    from spirit.game.session.passives import effective_max_hp
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in in_play)


async def hapu(ctx):
    top = ctx.deck_top(6)
    if not top:
        return
    take = min(2, len(top))
    picks = await ctx.choose_cards(
        top, take, minimum=take,
        prompt="Put 2 cards into your hand",
        display_cards=top,
    )
    await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.discard_cards(rest)


hapu_condition = deck_nonempty

mistys_favor = search_to_hand(
    is_supporter_card, count=3, reveal=True, prompt="Choose Supporter cards.",
)


def poke_maniac_pred(card) -> bool:
    return is_pokemon_card(card) and _retreat_cost(card) == 4


poke_maniac = search_to_hand(
    poke_maniac_pred, count=3, reveal=True,
    prompt="Choose Pokémon with a Retreat Cost of 4.",
)


async def pokemon_research_lab(ctx):
    space = BENCH_CAPACITY - len(ctx.my_bench())
    if space <= 0:
        return
    await search_to_bench(
        _evolves_from_unidentified_fossil, count=min(2, space),
        prompt="Choose Pokémon that evolve from Unidentified Fossil.",
    )(ctx)


def pokemon_research_lab_condition(board, player_id, stadium=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return deck_nonempty(board, player_id) and bench is not None \
        and len(bench.children) < BENCH_CAPACITY


async def reset_stamp(ctx):
    n = _prize_count(ctx.board, ctx.opponent_id)
    await ctx.shuffle_into_deck(list(ctx.hand(ctx.opponent_id)), ctx.opponent_id)
    if n:
        await ctx.draw_cards(n, ctx.opponent_id)


async def stadium_nav(ctx):
    results = await ctx.flip_coins(2, "Stadium Nav")
    heads = sum(1 for r in results if r)
    if heads:
        await search_to_hand(
            lambda c: c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value,
            count=heads, reveal=True, prompt="Choose Stadium cards.",
        )(ctx)


async def tag_switch(ctx):
    sources = [
        p for p in ctx.my_pokemon_in_play()
        if is_tag_team(p.archetype_id) and ctx.attached_energies(p)
    ]
    dests = ctx.my_pokemon_in_play()
    if not sources or len(dests) < 2:
        return
    source = await ctx.choose_pokemon(
        sources, "Move Energy from which TAG TEAM Pokémon?")
    if source is None:
        return
    await ctx.move_energy_freely(
        [source], [p for p in dests if p is not source], max_count=2)


def tag_switch_condition(board, player_id) -> bool:
    in_play = list(board.pokemon_in_play(player_id))
    if len(in_play) < 2:
        return False
    return any(
        is_tag_team(p.archetype_id) and any(is_energy_card(c) for c in p.children)
        for p in in_play
    )


sages_riddle_condition = blaines_quiz_show_condition


# Stadium abilities

GIANT_HEARTH_ABILITY = Ability(
    title="Giant Hearth",
    game_text="Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for up to 2 Fire Energy cards, reveals them, and puts them into their hand. Then, that player shuffles their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=giant_hearth,
    condition=giant_hearth_condition,
)

POKEMON_RESEARCH_LAB_ABILITY = Ability(
    title="Pokémon Research Lab",
    game_text="Once during each player's turn, that player may search their deck for up to 2 Pokémon that evolve from Unidentified Fossil, put those Pokémon onto their Bench, and shuffle their deck. If a player searches their deck in this way, their turn ends.",
    activation=Activations.ONCE_PER_TURN,
    effect=pokemon_research_lab,
    condition=pokemon_research_lab_condition,
    ends_turn=True,
)


# Tools

async def ear_ringing_bell_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)


EAR_RINGING_BELL_ABILITIES = [
    Ability(
        title="Ear-Ringing Bell",
        game_text="If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), the Attacking Pokémon is now Confused.",
        trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        effect=ear_ringing_bell_trigger,
    ),
]


async def giant_bomb_discard(ctx):
    if ctx.session.turn_state.active_player_id == ctx.player_id:
        return
    tools = [c for c in ctx.source.children if _display_name(c) == "Giant Bomb"]
    if tools:
        await ctx.discard_cards(tools)


async def giant_bomb_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    if ctx.damage_amount < 180:
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(100, target=attacker, apply_modifiers=False, as_counters=True)


GIANT_BOMB_ABILITIES = [
    Ability(
        title="Giant Bomb",
        game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn.",
        trigger=Triggers.BETWEEN_TURNS,
        effect=giant_bomb_discard,
    ),
    Ability(
        title="Giant Bomb",
        game_text="If the Pokémon this card is attached to is your Active Pokémon and takes 180 or more damage from an opponent's attack (even if this Pokémon is Knocked Out), put 10 damage counters on the Attacking Pokémon.",
        trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        effect=giant_bomb_trigger,
    ),
]


SPEEDING_SKYSTRIKE_GX = Attack(
    title="Speeding Skystrike-GX",
    game_text="Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
    cost={PokemonTypes.COLORLESS: 4},
    damage=180,
    condition=_holder_has_named_attack("Air Slash"),
    effect=protect_next_turn(prevent=True, effects_too=True),
)

BARRELING_BLITZ_GX = Attack(
    title="Barreling Blitz-GX",
    game_text="Flip a coin until you get tails. This attack does 40 more damage for each heads. (You can't use more than 1 GX attack in a game.)",
    cost={PokemonTypes.COLORLESS: 4},
    damage=200,
    damage_operator="+",
    condition=_holder_has_named_attack("Tackle"),
    effect=flip_damage(until_tails=True, bonus_per_heads=40),
)
