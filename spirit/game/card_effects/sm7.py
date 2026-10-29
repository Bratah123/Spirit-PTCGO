"""Celestial Storm (SM7) attack, ability, trainer, tool, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

import random

from spirit.game.attributes import (
    AttrID, GameSequence, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    ABILITIES_BY_ID, def_for, is_prism_star, is_ultra_beast,
)
from spirit.network.message_names import OutboundMsg
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_evolution_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_stage2_pokemon,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.passives import (
    Passive, ability_locked, carrier_pokemon, effective_max_hp,
)
from spirit.game.card_effects.attacks_common import (
    bonus_if,
    count_discard,
    count_energy,
    count_hand,
    count_in_play,
    count_prizes_remaining,
    count_prizes_taken,
    damage_counters_on,
    damage_per,
    discard_for_bonus,
    flip_damage,
    has_damage,
    has_tool,
    place_counters,
    snipe_attack,
)
from spirit.game.card_effects.passives_common import (
    guts_survive_passive,
    is_in_active_spot as _is_active,
    prevent_damage_when,
    retreat_free_when,
)
from spirit.game.card_effects.pokemon import delayed_knockout, energy_provides_type, is_lightning_energy
from spirit.game.card_effects.sm3 import (
    TakesMorePassive, is_fire_energy, is_grass_energy, is_gx_or_ex,
    is_psychic_energy, is_tool_card, is_water_energy,
)
from spirit.game.card_effects.sm4 import pokemon_has_ability
from spirit.game.card_effects.sm6 import is_dragon_pokemon, used_attack_last_own_turn
from spirit.game.card_effects.sl import is_benched
from spirit.game.card_effects.support_common import (
    discard_then_draw,
    distribute_energy,
    recover_from_discard,
    requires_bench_space,
    requires_discard,
    requires_hand,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    deck_nonempty, is_basic_energy_card, is_energy_card, is_metal_energy_card,
    opponent_has_bench,
)


def deck_has_cards(board, player_id, pokemon=None) -> bool:
    """Ability/attack-shaped wrapper around deck_nonempty."""
    return deck_nonempty(board, player_id)


def opponent_benched(board, player_id, pokemon=None) -> bool:
    """Ability/attack-shaped wrapper around opponent_has_bench."""
    return opponent_has_bench(board, player_id)


_MAGIC_EVENS = {20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260}
_GFW = {PokemonTypes.GRASS.value, PokemonTypes.FIRE.value, PokemonTypes.WATER.value}
_LPM = [
    PokemonTypes.LIGHTNING.value, PokemonTypes.PSYCHIC.value, PokemonTypes.METAL.value,
]


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    return getattr(def_for(getattr(card, "archetype_id", None)), "display_name", "") or ""


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _prize_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _is_damaged(ctx, pokemon) -> bool:
    return pokemon is not None and pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)


def _remaining_hp(pokemon) -> int:
    return pokemon.get_attribute(AttrID.HP, 0) if pokemon is not None else 0


def _condition_count(pokemon) -> int:
    return len(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if pokemon else 0


def is_ultra_beast_card(card) -> bool:
    return is_ultra_beast(getattr(card, "archetype_id", None))


def is_ball_item(card) -> bool:
    return is_item_card(card) and "Ball" in _display_name(card)


def is_stevens_resolve(card) -> bool:
    return _display_name(card) == "Steven's Resolve"


def is_prism_star_card(card) -> bool:
    return is_prism_star(getattr(card, "archetype_id", None))


def _has_unit_energy_lpm(pokemon) -> bool:
    for child in pokemon.children:
        name = _display_name(child)
        if "Unit Energy" in name and ("{L}{P}{M}" in name or "LightningPsychicMetal" in name):
            return True
    return False


def _basic_gl_energy_count(ctx) -> int:
    n = 0
    for pokemon in ctx.my_pokemon_in_play():
        for energy in ctx.attached_energies(pokemon):
            if not is_basic_energy_card(energy):
                continue
            if energy_provides_type(energy, PokemonTypes.GRASS.value) \
                    or energy_provides_type(energy, PokemonTypes.LIGHTNING.value):
                n += 1
    return n


def _other_pokemon_in_play(ctx) -> int:
    return max(0, count_in_play("both")(ctx) - 1)


def _stevens_resolve_in_discard(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if is_stevens_resolve(c))


def _named(card, *names) -> bool:
    return _logic_name(card) in names


def _in_play_for_owner(pokemon):
    area = getattr(pokemon, "parent", None)
    player = getattr(area, "parent", None) if area else None
    if player is None:
        return []
    found = []
    for child in player.children:
        name = child.get_attribute(AttrID.NAME) if hasattr(child, "get_attribute") else None
        if name in ("bench", "activePokemonArea"):
            found.extend(child.children)
    return found


def _extend_active(ctx) -> bool:
    active = ctx.my_active()
    if active is None or ability_locked(ctx.board, active):
        return False
    for entry in active.get_attribute(AttrID.PIE_ABILITIES) or []:
        if not isinstance(entry, dict):
            continue
        ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
        if ability is not None and ability.title == "Extend":
            return True
    return False


def _stage2_gfw(pokemon) -> bool:
    if not is_stage2_pokemon(pokemon):
        return False
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return bool(_GFW & set(types))


def _basic_benched_dragon(pokemon) -> bool:
    return is_basic_pokemon(pokemon) and is_dragon_pokemon(pokemon)


def _evolution_dragon(pokemon) -> bool:
    return is_evolution_pokemon(pokemon) and is_dragon_pokemon(pokemon)


def _non_fighting(pokemon) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIGHTING.value not in types


def _same_hand_size(ctx) -> bool:
    return ctx.hand_size() == ctx.hand_size(ctx.opponent_id)


def _same_name_in_play(ctx) -> bool:
    mine = {_logic_name(p) for p in ctx.my_pokemon_in_play()}
    theirs = {_logic_name(p) for p in ctx.opponent_pokemon_in_play()}
    return bool(mine & theirs)


def _defender_has_ability(ctx) -> bool:
    defender = ctx.defender
    if defender is None or ability_locked(ctx.board, defender):
        return False
    return pokemon_has_ability(defender)


def _attacker_has_tool(ctx) -> bool:
    return ctx.attacker is not None and has_tool(ctx.attacker)


def _hp_at_most(n: int, target="self"):
    def cond(ctx) -> bool:
        pokemon = ctx.attacker if target == "self" else ctx.defender
        return pokemon is not None and _remaining_hp(pokemon) <= n
    return cond


def _stadium_in_play_ctx(ctx) -> bool:
    return ctx.stadium_in_play() is not None


# ======================================================================
# Passives
# ======================================================================

class MoonRakerPassive(Passive):
    """Moon Raker can be paid with a single [M] when prize totals are 6."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        total = sum(_prize_count(board, pid) for pid in board.player_ids)
        if total == 6:
            return {"Metal": 1}
        return cost


class MagicEvensPassive(Passive):
    """Prevent opposing attack damage of exactly 20, 40, ... 260."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return calc.amount in _MAGIC_EVENS


class DangerPerceptionPassive(Passive):
    """If remaining HP is 100 or less, attacks do +80 to the opponent's Active."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or me is not calc.attacker:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if _remaining_hp(me) > 100:
            return
        calc.amount += 80


class UltraWallPassive(Passive):
    """Your Ultra Beasts take 10 less from opposing attacks."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        target = calc.target
        if target is None or target.owning_player_id != carrier.owning_player_id:
            return
        if not is_ultra_beast(target.archetype_id):
            return
        calc.amount = max(0, calc.amount - 10)


class PowerOfNaturePassive(Passive):
    """Prevent damage from opposing Ultra Beasts to your Grass-Energy Pokémon."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        target = calc.target
        if target is None or target.owning_player_id != carrier.owning_player_id:
            return False
        if calc.attacker is None or not is_ultra_beast(calc.attacker.archetype_id):
            return False
        return any(is_grass_energy(e) for e in target.children)


class ShadowShieldPassive(Passive):
    """If this Pokémon has Psychic Energy, it takes 20 less from attacks."""

    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is not calc.target or not (calc.is_attack and calc.is_opposing):
            return
        if any(is_psychic_energy(e) for e in me.children):
            calc.amount = max(0, calc.amount - 20)


class ConductiveBodyPassive(Passive):
    """While Active, retreat cost [C] less for each Beldum on your Bench."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        if me is not pokemon or not _is_active(me):
            return cost
        bench = board.find_player_area(pokemon.owning_player_id, "bench")
        n = sum(1 for p in (bench.children if bench else []) if _logic_name(p) == "Beldum")
        return max(0, cost - n)


class IcyBarrierPassive(Passive):
    """While Active, the opponent can't play Stadium cards."""

    def blocks_trainer_play(self, card, player_id, carrier):
        me = carrier_pokemon(carrier)
        if me is None or not _is_active(me):
            return False
        if player_id == me.owning_player_id:
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


class LazyPassive(Passive):
    """While Active, opponent's Pokémon have no Abilities except Lazy."""

    def blocks_abilities(self, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None or not _is_active(me):
            return False
        if pokemon.owning_player_id == me.owning_player_id:
            return False
        return _logic_name(pokemon) != "Slaking"


class SolShadePassive(Passive):
    """If you have Solrock, Fire Pokémon have no Abilities except GX/EX."""

    def blocks_abilities(self, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None:
            return False
        if not any(_logic_name(p) == "Solrock" for p in _in_play_for_owner(me)):
            return False
        if is_gx_or_ex(pokemon):
            return False
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        return PokemonTypes.FIRE.value in types


class UnitColor2Passive(Passive):
    """With Unit Energy LPM attached, this Pokémon is Lightning/Psychic/Metal."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        if not _has_unit_energy_lpm(pokemon):
            return types
        return list(_LPM)


class SunbeamPassive(Passive):
    """Your Lunatone's maximum HP is 130."""

    def max_hp_bonus(self, pokemon, carrier):
        if _logic_name(pokemon) != "Lunatone":
            return 0
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        return 50


class SkyPillarPassive(Passive):
    """Prevent opposing attack effects, including damage, done to Benched Pokémon."""

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and is_benched(calc.target))

    def blocks_attack_effects_from(self, target, attacker, carrier):
        if not is_benched(target) or attacker is None:
            return False
        return attacker.owning_player_id != target.owning_player_id

    def prevents_damage_counters(self, target, carrier, source_player_id=None):
        if not is_benched(target):
            return False
        if source_player_id is None:
            return True
        return source_player_id != target.owning_player_id


class HustleBeltPassive(Passive):
    """If remaining HP is 30 or less and damaged, attacks do +60 to Active."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        current = _remaining_hp(holder)
        if current > 30:
            return
        if current >= effective_max_hp(calc.board, holder):
            return
        calc.amount += 60


class FullMetalBodyPassive(Passive):
    """No Weakness while any Metal Energy is attached."""

    def modify_weakness(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is not calc.target:
            return
        if any(is_metal_energy_card(e) for e in me.children):
            calc.weakness_applies = False


def _harden_pred(calc, carrier):
    return (
        calc.is_attack and calc.is_opposing
        and carrier_pokemon(carrier) is calc.target
        and 0 < calc.amount <= 40
    )


moon_raker_passive = MoonRakerPassive()
magic_evens_passive = MagicEvensPassive()
danger_perception_passive = DangerPerceptionPassive()
ultra_wall_passive = UltraWallPassive()
power_of_nature_passive = PowerOfNaturePassive()
shadow_shield_passive = ShadowShieldPassive()
conductive_body_passive = ConductiveBodyPassive()
icy_barrier_passive = IcyBarrierPassive()
lazy_passive = LazyPassive()
sol_shade_passive = SolShadePassive()
unit_color_2_passive = UnitColor2Passive()
sunbeam_passive = SunbeamPassive()
sky_pillar_passive = SkyPillarPassive()
hustle_belt_passive = HustleBeltPassive()
full_metal_body_passive = FullMetalBodyPassive()
floating_electrons_passive = retreat_free_when(
    lambda pokemon, carrier: carrier_pokemon(carrier) is pokemon
    and any(True for _ in pokemon.children if is_energy_card(_))
)


# ======================================================================
# Attack / ability effects
# ======================================================================

chuck_away = discard_for_bonus(source="hand", max_count=2, per=40, base=0)
item_maniac_gx = search_to_hand(
    is_item_card, count=6, minimum=0, reveal=True,
    prompt="Choose up to 6 Item cards to put into your hand.",
)
call_for_the_boss = search_to_hand(
    lambda c: _named(c, "AlolanRaticate", "AlolanRaticateGX"),
    count=1, minimum=0, reveal=True,
    prompt="Choose an Alolan Raticate or Alolan Raticate-GX.",
)
reactive_poison = damage_per(
    lambda ctx: _condition_count(ctx.defender), 50, base=20)
feint_attack = snipe_attack(50, pool="any", apply_modifiers=False)
miraculous_spin = damage_per(_stevens_resolve_in_discard, 40)
twin_play = search_to_bench(lambda c: _named(c, "Scyther"), count=2)
circular_steps = damage_per(_other_pokemon_in_play, 10, base=70)
powerful_storm = damage_per(count_energy("mine", cards=True), 20)
dragon_break = damage_per(_basic_gl_energy_count, 30)
tempest_gx = discard_then_draw(0, 10, whole_hand=True)
assembly_gx = damage_per(count_prizes_taken(), 50, base=50)
shadow_chant = damage_per(
    count_discard("mine", is_supporter_card), 10, base=30, cap=130)
extrasensory = bonus_if(_same_hand_size, 90)
cross_cut_gx = bonus_if(lambda ctx: ctx.defender is not None and is_evolution_pokemon(ctx.defender), 100)
divine_paper = bonus_if(lambda ctx: count_prizes_remaining("opponent")(ctx) == 6, 90)
enhanced_stomp = bonus_if(_attacker_has_tool, 20)
silver_fist = bonus_if(_defender_has_ability, 60)
bite_off = bonus_if(lambda ctx: ctx.defender is not None and is_gx_or_ex(ctx.defender), 30)
strike_of_enlightenment = bonus_if(_hp_at_most(30), 160)
raging_blade = bonus_if(has_damage("self"), 50)
pheromone_catch = bonus_if(used_attack_last_own_turn("Pheromone Signals"), 100)
onix_rage = damage_per(damage_counters_on("self"), 10, base=10)
dragon_fleet = damage_per(
    count_in_play("mine", _evolution_dragon), 50)
enemy_show = place_counters(
    lambda ctx: count_in_play("opponent")(ctx), "choose_any_opponent")
breakdown = place_counters(count_hand("opponent"), "opponent_active")
dual_splash = snipe_attack(30, pool="any", count=2)
beat_up = flip_damage(per_heads=30, coins_from=count_in_play("mine"))


async def _also_discard_stadium(ctx):
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


wreck = bonus_if(_stadium_in_play_ctx, 50, also=_also_discard_stadium)


async def spider_trap(ctx):
    bench = ctx.opponent_bench()
    if bench and await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokémon with their Active Pokémon?"):
        target = await ctx.choose_pokemon(
            bench, "Choose the opponent's new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
    active = ctx.opponent_active()
    if active is None:
        return
    await ctx.apply_special_condition(active, SpecialConditions.ASLEEP)
    await ctx.apply_special_condition(active, SpecialConditions.POISONED)


async def legendary_ascent(ctx):
    if not await ctx.ask_yes_no("Switch this Pokémon with your Active Pokémon?"):
        return
    if not await ctx.switch_active(ctx.player_id, ctx.source):
        return
    others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    await ctx.move_energy_freely(
        others, [ctx.source], predicate=is_water_energy,
        prompt="Choose Water Energy to move to this Pokémon",
    )


async def cold_crush_gx(ctx):
    for pokemon in (ctx.attacker, ctx.defender):
        if pokemon is not None:
            await ctx.discard_cards(list(ctx.attached_energies(pokemon)))


async def shady_move(ctx):
    pool = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    damaged = [p for p in pool if _is_damaged(ctx, p)]
    if not damaged:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to move a damage counter from")
    if source is None:
        return
    dests = [p for p in pool if p is not source]
    dest = await ctx.choose_pokemon(
        dests, "Choose a Pokémon to move the damage counter to")
    if dest is not None:
        await ctx.move_damage_counters(source, dest, max_count=1)


def shady_move_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None or board.active_pokemon(player_id) is not pokemon:
        return False
    opp = _other_player(board, player_id)
    pool = list(board.pokemon_in_play(player_id))
    if opp:
        pool.extend(board.pokemon_in_play(opp))
    damaged = [p for p in pool if p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)]
    return bool(damaged) and len(pool) >= 2


async def red_eyes(ctx):
    if not await ctx.ask_yes_no(
            "Put a Basic Pokémon from your opponent's discard pile onto their Bench?"):
        return
    bench = ctx.board.find_player_area(ctx.opponent_id, "bench")
    if bench is None or len(bench.children) >= BENCH_CAPACITY:
        return
    basics = [c for c in ctx.discard_pile(ctx.opponent_id) if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(
        basics, 1, prompt="Choose a Basic Pokémon to put onto the opponent's Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])


def red_eyes_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    bench = board.find_player_area(opp, "bench")
    if bench is None or len(bench.children) >= BENCH_CAPACITY:
        return False
    discard = board.find_player_area(opp, "discard")
    return bool(discard) and any(is_basic_pokemon(c) for c in discard.children)


async def search_for_friends(ctx):
    if not await ctx.ask_yes_no(
            "Put 2 Supporter cards from your discard pile into your hand?"):
        return
    cards = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if not cards:
        return
    n = min(2, len(cards))
    picks = await ctx.choose_cards(
        cards, n, minimum=0,
        prompt="Choose up to 2 Supporter cards to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)


def search_for_friends_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_supporter_card(c) for c in discard.children)


async def _strike_and_run_then(ctx, benched):
    if not benched:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


strike_and_run = search_to_bench(
    is_basic_pokemon, count=3, then=_strike_and_run_then,
    prompt="Choose up to 3 Basic Pokémon to put onto your Bench.",
)


async def extra_energy_bomb(ctx):
    energy = [c for c in ctx.discard_pile() if is_energy_card(c)]
    targets = [p for p in ctx.my_pokemon_in_play() if not is_gx_or_ex(p)]
    if len(energy) < 5 or not targets:
        return
    picks = await ctx.choose_cards(
        energy, 5, minimum=5, prompt="Choose 5 Energy cards to attach.")
    if len(picks) < 5:
        return
    await distribute_energy(ctx, picks, targets)
    await ctx.knock_out(ctx.source)


def extra_energy_bomb_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    if not discard or sum(1 for c in discard.children if is_energy_card(c)) < 5:
        return False
    return any(not is_gx_or_ex(p) for p in board.pokemon_in_play(player_id))


async def crush_and_burn_gx(ctx):
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)]
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Discard any amount of Energy from your Pokémon") if pool else []
    await ctx.discard_cards(picks)
    await ctx.deal_damage((ctx.ability.damage or 0) + 50 * len(picks))


async def dangerous_concert(ctx):
    for pokemon in ctx.opponent_bench():
        if _is_damaged(ctx, pokemon):
            await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)


async def mirror_step(ctx):
    extra = 70 if _same_name_in_play(ctx) else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + extra)


async def steelworks(ctx):
    top = ctx.deck_top(4)
    metal = [c for c in top if is_metal_energy_card(c)]
    picks = []
    if top:
        picks = await ctx.choose_cards(
            metal, max(len(metal), 1), minimum=0,
            prompt="Attach any number of Metal Energy cards you find there.",
            display_cards=top,
        ) if metal else []
    if picks:
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Metal Energy to")
        if target is not None:
            for energy in picks:
                await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


async def wish_upon_a_star(ctx):
    if len(ctx.my_bench()) >= BENCH_CAPACITY:
        return
    if not await ctx.ask_yes_no(
            "Put this Pokémon onto your Bench and take 1 more Prize card?"):
        return
    if await ctx.bench_pokemon(ctx.source):
        await ctx.take_prizes(1)


async def perish_dream(ctx):
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await delayed_knockout(ctx)


async def lightning_strike(ctx):
    lightning = [e for e in ctx.attached_energies(ctx.attacker) if is_lightning_energy(e)]
    extra = 0
    if lightning and await ctx.ask_yes_no(
            "Discard all Lightning Energy from this Pokémon? If you do, this attack does 70 more damage."):
        await ctx.discard_cards(lightning)
        extra = 70
    await ctx.deal_damage((ctx.ability.damage or 0) + extra)


async def energy_grounding(ctx):
    if not ctx.ko_from_attack or ctx.ko_pokemon is None:
        return
    pool = [e for e in ctx.attached_energies(ctx.ko_pokemon) if is_basic_energy_card(e)]
    if not pool:
        return
    if not await ctx.ask_yes_no(
            "Move a basic Energy from the Knocked Out Pokémon to this Pokémon?"):
        return
    picks = await ctx.choose_cards(pool, 1, prompt="Choose a basic Energy to move")
    if picks:
        await ctx.move_energy(picks[0], ctx.source)


async def dreamy_mist(ctx):
    await ctx.deal_damage()
    targets = [p for p in ctx.my_bench() if _basic_benched_dragon(p)]
    for target in targets:
        energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not energy:
            break
        picks = await ctx.choose_cards(
            energy, 1, minimum=0,
            prompt="Choose a basic Energy card to attach to a Benched Dragon.")
        if picks:
            await ctx.attach_energy(picks[0], target)


async def even_game(ctx):
    n = len(ctx.opponent_bench())
    if n <= 0:
        return
    await search_to_bench(
        is_basic_pokemon, count=n,
        prompt="Choose Basic Pokémon to put onto your Bench.",
    )(ctx)


async def smooth_over(ctx):
    picks = await ctx.search_deck(
        None, count=1, minimum=0,
        prompt="Choose a card to put on top of your deck.",
    )
    if picks:
        await ctx.shuffle_deck_below(picks[0])
    else:
        await ctx.shuffle_deck()


async def double_charge(ctx):
    await ctx.deal_damage()
    energy = [c for c in ctx.hand() if is_basic_energy_card(c)]
    bench = ctx.my_bench()
    if not energy or not bench:
        return
    if not await ctx.ask_yes_no(
            "Attach up to 2 basic Energy cards from your hand to 1 of your Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach.")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    if target is not None:
        for card in picks:
            await ctx.attach_energy(card, target)


async def surprising_pattern(ctx):
    await ctx.deal_damage()
    specials = [
        e for p in ctx.opponent_pokemon_in_play()
        for e in ctx.attached_energies(p) if is_special_energy(e)
    ]
    await ctx.discard_cards(specials)


async def mining(ctx):
    await ctx.deal_damage()
    picks = await ctx.search_deck(
        is_item_card, count=1, minimum=0, prompt="Choose an Item card.")
    await ctx.shuffle_deck()
    if not picks:
        return
    card = picks[0]
    if is_tool_card(card):
        holders = [p for p in ctx.my_pokemon_in_play() if not has_tool(p)]
        if holders and await ctx.ask_yes_no(
                "Attach this Pokémon Tool instead of putting it into your hand?"):
            target = await ctx.choose_pokemon(
                holders, "Choose a Pokémon to attach the Tool to")
            if target is not None and await ctx.attach_tool(card, target):
                return
    await ctx.put_in_hand(picks, reveal=True)


async def endure(ctx):
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Endure")
    if results and results[0]:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            guts_survive_passive(
                hp_floor=10,
                title=ctx.ability.title if ctx.ability else "Endure",
                flip=False,
            ),
        )


async def falling_star(ctx):
    if not await ctx.ask_yes_no(
            "Move your Active Pokémon to your Bench and play this Pokémon as your new Active?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    await ctx.switch_active(ctx.player_id, ctx.source)


def falling_star_condition(board, player_id, pokemon=None) -> bool:
    return requires_bench_space(1)(board, player_id)


async def ditch_and_draw(ctx):
    await ctx.discard_from_hand(
        len(ctx.hand()), minimum=0,
        prompt="Discard any number of cards from your hand.")
    await ctx.draw_until(5)


async def clear_the_room(ctx):
    await ctx.deal_damage()
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    supporters = [c for c in cards if is_supporter_card(c)]
    if not supporters:
        return
    picks = await ctx.choose_cards(
        supporters, 1, prompt="Choose a Supporter card to shuffle into the deck.")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def onix_screech(ctx):
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_own_next_turn(defender, TakesMorePassive(20))


async def captivating_salsa(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon") or bench[0]
    if not await ctx.switch_active(ctx.opponent_id, target):
        return
    active = ctx.opponent_active()
    if active is None:
        return
    await ctx.apply_special_condition(active, SpecialConditions.BURNED)
    await ctx.apply_special_condition(active, SpecialConditions.CONFUSED)


async def zappy_pom_poms(ctx):
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if is_gx_or_ex(pokemon):
            await ctx.deal_damage(30, target=pokemon, apply_modifiers=None)


async def sandy_fear_gx(ctx):
    top = ctx.deck_top(13, ctx.opponent_id)
    if not top:
        return
    pokemon = [c for c in top if is_pokemon_card(c)]
    picks = await ctx.choose_cards(
        pokemon, max(len(pokemon), 1), minimum=0,
        prompt="Discard any number of Pokémon you find there.",
        display_cards=top,
    ) if pokemon else []
    await ctx.discard_cards(picks)
    await ctx.shuffle_deck(ctx.opponent_id)
    if picks:
        await ctx.deal_damage(60 * len(picks))


async def firefighting(ctx):
    await ctx.deal_damage()
    fire = [e for e in ctx.attached_energies(ctx.defender) if is_fire_energy(e)]
    if fire:
        picks = await ctx.choose_cards(fire, 1, prompt="Discard a Fire Energy")
        await ctx.discard_cards(picks)


async def draw_for_everybody(ctx):
    await ctx.shuffle_into_deck(list(ctx.hand()), ctx.player_id)
    n = len(ctx.my_bench()) + len(ctx.opponent_bench())
    if n:
        await ctx.draw_cards(n)


async def dust_devil(ctx):
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if _non_fighting(pokemon):
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=None)


async def stormy_winds(ctx):
    if not await ctx.ask_yes_no("Discard the top 3 cards of your deck?"):
        return
    top = list(ctx.deck_top(3))
    if not top:
        return
    await ctx.discard_cards(top)
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=0,
        prompt="Choose a basic Energy card to attach to this Pokémon.")
    if picks:
        await ctx.attach_energy(picks[0], ctx.source)


async def excavate(ctx):
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Discard the top card of your deck?",
        ["Discard", "Keep it on top"],
    )
    if idx == 0:
        await ctx.discard_cards([card])


async def dragon_wind(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


def dragon_wind_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None or board.active_pokemon(player_id) is not pokemon:
        return False
    return opponent_has_bench(board, player_id)


async def den_of_iniquity_gx(ctx):
    target = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(), "Choose 1 of your opponent's Pokémon")
    if target is None or ctx.effects_blocked(target):
        return
    was_active = target is ctx.opponent_active()
    await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.opponent_id):
                screen_name = ctx.session.players[ctx.opponent_id].screen_name
                await ctx.session.end_game(
                    ctx.player_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


async def harden(ctx):
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, prevent_damage_when(_harden_pred))


async def slack_off(ctx):
    attacker = ctx.attacker
    if attacker is None:
        return
    await ctx.heal(ctx.max_hp(attacker), attacker)


async def swallow_up(ctx):
    extra = 0
    attacker, defender = ctx.attacker, ctx.defender
    if attacker is not None and defender is not None:
        if _remaining_hp(defender) < _remaining_hp(attacker):
            extra = 80
    await ctx.deal_damage((ctx.ability.damage or 0) + extra)


async def power_draw(ctx):
    discarded = await ctx.discard_from_hand(
        1, prompt="Discard a card from your hand")
    if discarded:
        await ctx.draw_cards(3)


def power_draw_condition(board, player_id, pokemon=None) -> bool:
    return requires_hand(n=1)(board, player_id, pokemon)


async def flaming_honk(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(4))
    await ctx.discard_cards(top)
    fire = [c for c in top if is_fire_energy(c)]
    if fire:
        await distribute_energy(ctx, fire, ctx.my_pokemon_in_play())


async def trample(ctx):
    await ctx.deal_damage()
    for pokemon in list(ctx.my_bench()) + list(ctx.opponent_bench()):
        results = await ctx.flip_coins(1, "Trample")
        if results and results[0]:
            await ctx.deal_damage(60, target=pokemon, apply_modifiers=False)


async def fragrance_trap(ctx):
    results = await ctx.flip_coins(1, "Fragrance Trap")
    if not (results and results[0]):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


def fragrance_trap_condition(board, player_id, pokemon=None) -> bool:
    return opponent_has_bench(board, player_id)


async def wave_swallower(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails("Wave Swallower")
    if heads:
        await ctx.heal(50 * heads, ctx.attacker)


async def dwindling_wave(ctx):
    counters = damage_counters_on("self")(ctx)
    amount = max(0, (ctx.ability.damage or 0) - 40 * counters)
    if amount:
        await ctx.deal_damage(amount)


async def weepinbell_growth(ctx):
    cards = [c for c in ctx.hand() if is_grass_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0,
        prompt="Attach up to 2 Grass Energy cards to this Pokémon.")
    for energy in picks:
        await ctx.attach_energy(energy, ctx.attacker)


async def bawl(ctx):
    ctx.lock_plays(ctx.opponent_id, is_trainer_card)


async def scorching_light(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Scorching Light")
    if not results:
        return
    if results[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    else:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


# ======================================================================
# Trainers
# ======================================================================

async def acro_bike(ctx):
    top = ctx.deck_top(2)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, prompt="Choose a card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.discard_cards(rest)


apricorn_maker = search_to_hand(
    is_ball_item, count=2, minimum=0, reveal=True,
    prompt='Choose up to 2 Item cards that have "Ball" in their name.',
)


async def beast_ball(ctx):
    """Look at face-down Prizes; you may reveal an Ultra Beast, put it into
    your hand, and put Beast Ball in its place. Always shuffles Prizes."""
    session = ctx.session
    prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    if not prize_area or not prize_area.children:
        return
    prizes = list(prize_area.children)
    ultra = [c for c in prizes if is_ultra_beast_card(c)]
    picked_id = await session.prompt_prize_reveal_pick(
        ctx.player_id, ctx.source.entity_id,
        [c.entity_id for c in prizes], [c.entity_id for c in ultra],
    )
    picked = ctx.board.get_entity(picked_id) if picked_id else None
    opponent = ctx.opponent_id
    both = list(session.players.values())
    took = False
    if picked is not None and picked in prize_area.children:
        slot = getattr(picked, "board_slot", None)
        if slot is None:
            slot = prizes.index(picked)
        hand = ctx.board.find_player_area(ctx.player_id, "hand")
        pos = len(hand.children)
        ctx.board.move_card(picked.entity_id, hand.entity_id)
        take = [
            session._entity_introduced_msg(picked),
            session._entity_moved_msg(picked.entity_id, hand.entity_id, pos),
        ]
        for viewer in both:
            await session.send_game_sequence(
                [viewer], GameSequence.WITH_OPEN_PRIZE_CARDS, list(take))
        if ctx.board.move_card(ctx.source.entity_id, prize_area.entity_id, slot):
            await session.send_game_sequence(
                both, GameSequence.GROUPED_MOVE,
                [session._entity_moved_msg(
                    ctx.source.entity_id, prize_area.entity_id, slot)])
            took = True
    resets = [session._attributes_reset_msg(c.entity_id) for c in prize_area.children]
    if resets:
        await session.send_game_sequence(
            [session.players[ctx.player_id]], GameSequence.GROUPED_MOVE, resets)
    if took:
        await session.send_game_sequence(
            [session.players[opponent]], GameSequence.GROUPED_MOVE,
            [session._attributes_reset_msg(ctx.source.entity_id)])
    random.shuffle(prize_area.children)
    await session.send_game_sequence(
        both, GameSequence.GROUPED_MOVE,
        [session._build_msg(OutboundMsg.SHUFFLED.value,
                            {"gameID": ctx.game_id, "entityID": prize_area.entity_id})])


def beast_ball_condition(board, player_id, pokemon=None) -> bool:
    prizes = board.find_player_area(player_id, "prizePile")
    return bool(prizes and prizes.children)


async def bills_maintenance(ctx):
    picks = await ctx.choose_cards(
        list(ctx.hand()), 1,
        prompt="Shuffle a card from your hand into your deck.")
    if not picks:
        return
    await ctx.shuffle_into_deck(picks)
    await ctx.draw_cards(3)


bills_maintenance_condition = requires_hand(n=1)


async def energy_recycle_system(ctx):
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    options = ["Put a basic Energy card into your hand"]
    if len(energy) >= 3:
        options.append("Shuffle 3 basic Energy cards into your deck")
    choice = 0 if len(options) == 1 else await ctx.choose(
        "Choose 1:", options, use_panel=False)
    if choice == 0:
        picks = await ctx.choose_cards(
            energy, 1, prompt="Choose a basic Energy card to put into your hand.")
        await ctx.put_in_hand(picks, reveal=True)
    else:
        picks = await ctx.choose_cards(
            energy, 3, minimum=3,
            prompt="Choose 3 basic Energy cards to shuffle into your deck.")
        if picks:
            await ctx.shuffle_into_deck(picks)


def energy_recycle_system_condition(board, player_id, pokemon=None) -> bool:
    return requires_discard(is_basic_energy_card, n=1)(board, player_id)


fisherman = recover_from_discard(
    is_basic_energy_card, count=4, minimum=4, reveal=True,
    prompt="Choose 4 basic Energy cards to put into your hand.",
)
fisherman_condition = requires_discard(is_basic_energy_card, n=4)


async def friend_ball(ctx):
    opp_types = set()
    for pokemon in ctx.opponent_pokemon_in_play():
        opp_types.update(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

    def pred(card, types=opp_types):
        if not is_pokemon_card(card):
            return False
        return bool(types & set(card.get_attribute(AttrID.POKEMON_TYPES) or []))

    await search_to_hand(
        pred, count=1, minimum=0, reveal=True,
        prompt="Choose a Pokémon that shares a type with an opponent's Pokémon.",
    )(ctx)


async def hiker(ctx):
    options = []
    if ctx.deck():
        options.append("Your deck")
    if ctx.deck(ctx.opponent_id):
        options.append("Your opponent's deck")
    if not options:
        return
    choice = 0 if len(options) == 1 else await ctx.choose(
        "Look at the top 5 cards of which deck?", options, use_panel=False)
    pid = ctx.player_id if options[choice] == "Your deck" else ctx.opponent_id
    top = ctx.deck_top(5, pid)
    if not top:
        return
    picks = await ctx.choose_cards(top, 1, prompt="Choose a card to put on top of that deck.")
    if picks:
        await ctx.shuffle_deck_below(picks[0])


def hiker_condition(board, player_id, pokemon=None) -> bool:
    if deck_nonempty(board, player_id):
        return True
    opp = _other_player(board, player_id)
    return bool(opp) and deck_nonempty(board, opp)


def last_chance_potion_condition(board, player_id, pokemon=None) -> bool:
    return any(p.get_attribute(AttrID.HP, 0) <= 30 for p in board.pokemon_in_play(player_id))


async def last_chance_potion(ctx):
    targets = [p for p in ctx.my_pokemon_in_play() if _remaining_hp(p) <= 30]
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to heal 120 damage")
    if target is not None:
        await ctx.heal(120, target)


def life_herb_condition(board, player_id, pokemon=None) -> bool:
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        or (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        for p in board.pokemon_in_play(player_id)
    )


async def life_herb(ctx):
    results = await ctx.flip_coins(1, "Life Herb")
    if not (results and results[0]):
        return
    targets = [
        p for p in ctx.my_pokemon_in_play()
        if _is_damaged(ctx, p) or (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    ]
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Pokémon to heal 60 damage and recover")
    if target is None:
        return
    await ctx.heal(60, target)
    await ctx.cure_all_conditions(target)


lisia = search_to_hand(
    is_prism_star_card, count=2, minimum=0, reveal=True,
    prompt="Choose up to 2 Prism Star cards.",
)


async def lure_ball(ctx):
    results = await ctx.flip_coins(3, "Lure Ball")
    heads = sum(1 for r in results if r)
    evo = [c for c in ctx.discard_pile() if is_evolution_pokemon(c)]
    if not heads or not evo:
        return
    n = min(heads, len(evo))
    picks = await ctx.choose_cards(
        evo, n, minimum=n,
        prompt="Choose Evolution Pokémon to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)


def lure_ball_condition(board, player_id, pokemon=None) -> bool:
    return requires_discard(is_evolution_pokemon, n=1)(board, player_id)


def the_masked_royal_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(is_basic_energy_card(c) for c in hand.children):
        return False
    return any(_stage2_gfw(p) for p in board.pokemon_in_play(player_id))


async def the_masked_royal(ctx):
    energy = [c for c in ctx.hand() if is_basic_energy_card(c)]
    targets = [p for p in ctx.my_pokemon_in_play() if _stage2_gfw(p)]
    if not energy or not targets:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a basic Energy card to attach")
    target = await ctx.choose_pokemon(
        targets, "Choose a Stage 2 Grass, Fire, or Water Pokémon")
    if picks and target is not None:
        await ctx.attach_energy(picks[0], target)


async def poke_nav(ctx):
    top = ctx.deck_top(3)
    if not top:
        return
    matches = [c for c in top if is_pokemon_card(c) or is_energy_card(c)]
    picks = await ctx.choose_cards(
        matches, 1, minimum=0,
        prompt="You may put a Pokémon or Energy card into your hand.",
        display_cards=top,
    ) if matches else []
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    rest = len(top) - len(picks)
    if rest > 1:
        await ctx.reorder_deck_top(
            rest, prompt="Put the other cards back on top in any order.")


def rainbow_brush_condition(board, player_id, pokemon=None) -> bool:
    if not deck_nonempty(board, player_id):
        return False
    return any(
        is_energy_card(c)
        for p in board.pokemon_in_play(player_id)
        for c in p.children
    )


async def rainbow_brush(ctx):
    energies = [
        e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
    ]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy card attached to 1 of your Pokémon")
    if not picks:
        return
    attached = picks[0]
    holder = carrier_pokemon(attached)
    basics = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card to switch in.",
    )
    if basics and holder is not None:
        await ctx.attach_energy(basics[0], holder)
        await ctx.shuffle_into_deck([attached])
    else:
        await ctx.shuffle_deck()


async def stevens_resolve(ctx):
    picks = await ctx.search_deck(
        None, count=3, minimum=0,
        prompt="Choose up to 3 cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()
    ctx.ends_turn = not _extend_active(ctx)


async def tate_liza(ctx):
    can_draw = bool(ctx.deck())
    can_switch = bool(ctx.my_bench())
    options = []
    if can_draw:
        options.append("Shuffle your hand into your deck, then draw 5 cards")
    if can_switch:
        options.append("Switch your Active Pokémon with 1 of your Benched Pokémon")
    if not options:
        return
    choice = 0 if len(options) == 1 else await ctx.choose(
        "Choose 1:", options, use_panel=False)
    if "Shuffle" in options[choice]:
        await ctx.shuffle_into_deck(list(ctx.hand()), ctx.player_id)
        await ctx.draw_cards(5)
        return
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


def tate_liza_condition(board, player_id, pokemon=None) -> bool:
    if deck_nonempty(board, player_id):
        return True
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


async def tv_reporter(ctx):
    await ctx.draw_cards(3)
    await ctx.discard_from_hand(1, prompt="Discard a card from your hand")


async def underground_expedition(ctx):
    bottom = ctx.deck()[:4]
    if not bottom:
        return
    n = min(2, len(bottom))
    picks = await ctx.choose_cards(
        bottom, n, minimum=n,
        prompt="Choose cards to put into your hand.",
        display_cards=bottom,
    )
    await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in bottom if c not in picks]
    if len(rest) > 1:
        order = await ctx.choose_cards(
            rest, len(rest), minimum=len(rest), ordered=True,
            prompt="Put the other cards on the bottom of your deck in any order.",
        )
    else:
        order = rest
    for card in reversed(order):
        await ctx.put_on_bottom_of_deck(card)


def underground_expedition_condition(board, player_id, pokemon=None) -> bool:
    return deck_nonempty(board, player_id)


async def shrine_of_punishment(ctx):
    for pid in ctx.board.player_ids:
        for pokemon in list(ctx.board.pokemon_in_play(pid)):
            if is_gx_or_ex(pokemon):
                await ctx.deal_damage(
                    10, target=pokemon, apply_modifiers=False, as_counters=True)
