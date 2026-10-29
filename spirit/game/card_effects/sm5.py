"""Ultra Prism (SM5) attack, ability, trainer, energy, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

import json

from spirit.game.attributes import (
    AttrID, PokemonStage, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Ability, Activations, def_for, evolves_from_chain,
)
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_supporter_card,
    is_evolution_pokemon,
)
from spirit.game.session.passives import (
    Passive, carrier_pokemon, effective_max_hp, effective_pokemon_types,
    effective_retreat_cost,
)
from spirit.game.card_effects.attacks_common import (
    bonus_if,
    count_energy,
    damage_counters_on,
    damage_per,
    discard_for_bonus,
    discard_random_from_hand,
    has_attack_titled,
    self_energy_discard_attack,
)
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.passives_common import (
    apply_protection,
    is_in_active_spot,
    no_weakness_passive,
    prevent_damage_when,
    retreat_free_when,
    takes_less_passive,
)
from spirit.game.card_effects.pokemon import energy_provides_type, is_lightning_energy
from spirit.game.card_effects.sm3 import (
    is_darkness_energy,
    is_gx_or_ex,
    is_grass_energy,
    is_psychic_energy,
    is_tool_card,
    is_water_energy,
)
from spirit.game.card_effects.sm4 import (
    MemoryTypePassive,
    more_prizes_remaining,
    pokemon_has_ability,
)
from spirit.game.card_effects.sl import defender_has_any_condition
from spirit.game.card_effects.support_common import (
    distribute_energy,
    recover_from_discard,
    search_to_hand,
    shuffle_hand_into_deck_draw,
)
from spirit.game.card_effects.trainers import (
    FossilBodyPassive,
    fossil_discard_ability,
    is_energy_card,
    is_metal_energy_card,
)


ALL_TYPES_FOUR_AT_A_TIME = [list(opt) * 4 for opt in ALL_TYPES_ONE_AT_A_TIME]
UNIT_ENERGY_GRW = [
    [PokemonTypes.GRASS], [PokemonTypes.FIRE], [PokemonTypes.WATER],
]
UNIT_ENERGY_LPM = [
    [PokemonTypes.LIGHTNING], [PokemonTypes.PSYCHIC], [PokemonTypes.METAL],
]
_REGI_NAMES = {"Regirock", "Regice", "Registeel", "Regigigas"}
_WATER_OR_METAL = {PokemonTypes.WATER.value, PokemonTypes.METAL.value}


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _is_damaged(ctx, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)


def _has_energy(ctx, pokemon) -> bool:
    return bool(ctx.attached_energies(pokemon))


def _pokemon_types(board, pokemon):
    if board is not None:
        try:
            return effective_pokemon_types(board, pokemon) or []
        except Exception:
            pass
    return pokemon.get_attribute(AttrID.POKEMON_TYPES) or []


def _is_typed(board, pokemon, pokemon_type: PokemonTypes) -> bool:
    return pokemon_type.value in _pokemon_types(board, pokemon)


def _is_typed_archetype(archetype_id, pokemon_type: PokemonTypes) -> bool:
    definition = def_for(archetype_id)
    attr = definition.extra_attributes.get(str(AttrID.POKEMON_TYPES.value)) if definition else None
    if not attr:
        return False
    try:
        types = json.loads(attr["value"])
    except (TypeError, ValueError):
        return False
    return pokemon_type.value in types


def _tool_count_in_discard(board, player_id) -> int:
    discard = board.find_player_area(player_id, "discard")
    return sum(1 for c in (discard.children if discard else []) if is_tool_card(c))


def _direct_evolves_from(card, logic_name: str) -> bool:
    chain = evolves_from_chain(card.archetype_id)
    return bool(chain) and chain[0] == logic_name


def is_fairy_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.FAIRY.value in types


def is_looker_card(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Looker"


def ancient_crystal_attach_to(pokemon) -> bool:
    return _logic_name(pokemon) in _REGI_NAMES


def go_second_first_turn(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number == 2


# ======================================================================
# Passives
# ======================================================================

def _special_energy_attacker(calc, carrier) -> bool:
    attacker = calc.attacker
    if attacker is None or not (calc.is_attack and calc.is_opposing):
        return False
    return any(is_special_energy(c) for c in attacker.children)


def _earthen_shield_pred(calc, carrier):
    if not _special_energy_attacker(calc, carrier):
        return False
    target = calc.target
    if target is None or target.owning_player_id != carrier.owning_player_id:
        return False
    types = target.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.METAL.value in types


def _flashing_head_pred(calc, carrier):
    me = carrier_pokemon(carrier)
    return me is not None and calc.target is me and _special_energy_attacker(calc, carrier)


earthen_shield_passive = prevent_damage_when(_earthen_shield_pred)
flashing_head_passive = prevent_damage_when(_flashing_head_pred)

weather_guard_passive = no_weakness_passive(
    lambda target, carrier: (
        target.owning_player_id == carrier.owning_player_id
        and PokemonTypes.GRASS.value in (target.get_attribute(AttrID.POKEMON_TYPES) or [])
    )
)

rock_hiding_passive = retreat_free_when(
    lambda pokemon, carrier: (
        carrier_pokemon(carrier) is pokemon
        and any(energy_provides_type(e, PokemonTypes.FIGHTING.value)
                for e in pokemon.children if is_energy_card(e))
    )
)

def _ancient_crystal_protects(target, carrier):
    return (
        carrier_pokemon(carrier) is target
        and _logic_name(target) in _REGI_NAMES
    )


ancient_crystal_passive = takes_less_passive(30, protects=_ancient_crystal_protects)


class EscapeBoardPassive(Passive):
    """Retreat cost Colorless less; can retreat while Asleep or Paralyzed."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon:
            return max(0, cost - 1)
        return cost

    def retreats_despite_conditions(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


class RotoMotorPassive(Passive):
    """If 9+ Tools are in the discard, this Pokémon's attacks cost nothing."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if _tool_count_in_discard(board, pokemon.owning_player_id) >= 9:
            return {}
        return cost


class FlamingFighterPassive(Passive):
    """Opponent's Burned Pokémon take 6 damage counters between turns."""

    def modify_burn_counters(self, counters, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None or pokemon.owning_player_id == me.owning_player_id:
            return counters
        return 6


class EvolutionaryAdvantagePassive(Passive):
    """If you go second, this Pokémon can evolve during your first turn."""

    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        cur = pokemon
        while getattr(cur, "parent", None) is not None:
            cur = cur.parent
        ts = getattr(cur, "turn_state", None)
        return ts is not None and ts.turn_number == 2


class PowerHuddlePassive(Passive):
    """While this Passimian is benched, your Passimian attacks do +30 to
    the opponent's Active Evolution Pokémon."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or is_in_active_spot(me):
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or _logic_name(attacker) != "Passimian":
            return
        if attacker.owning_player_id != me.owning_player_id:
            return
        if calc.target is None or not is_evolution_pokemon(calc.target):
            return
        if "power_huddle" in calc.applied_once:
            return
        calc.applied_once.add("power_huddle")
        calc.amount += 30


class FreezingGazePassive(Passive):
    """While Active, opponent's GX/EX in play have no Abilities.
    Hand/discard ability lock is out of engine scope."""

    def blocks_abilities(self, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None or not is_in_active_spot(me):
            return False
        if pokemon.owning_player_id == me.owning_player_id:
            return False
        # Text excepts Freezing Gaze; Glaceon-GX's only Ability is that one.
        if _logic_name(pokemon) == "GlaceonGX":
            return False
        return is_gx_or_ex(pokemon)


class SuperBoostEnergyPassive(Passive):
    """Colorless; on a Stage 2, every type 1-at-a-time, or 4-at-a-time with
    3+ Stage 2 Pokémon in play."""

    def modify_energy_provided(self, options, energy, holder, board):
        definition = def_for(getattr(energy, "archetype_id", None))
        if not isinstance(getattr(definition, "passive", None), SuperBoostEnergyPassive):
            return options
        if holder is None:
            return options
        if holder.get_attribute(AttrID.STAGE) != PokemonStage.STAGE2.value:
            return options
        owner = holder.owning_player_id
        stage2 = sum(
            1 for p in board.pokemon_in_play(owner)
            if p.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
        )
        if stage2 >= 3:
            return ALL_TYPES_FOUR_AT_A_TIME
        return ALL_TYPES_ONE_AT_A_TIME


class SpikeArmorPassive(Passive):
    """If this Pokémon is damaged by an attack, put 6 counters on the attacker."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(
                60, target=attacker, apply_modifiers=False, as_counters=True)
        return None


# ======================================================================
# Attack / ability effects
# ======================================================================

gold_rush = discard_for_bonus(
    source="hand", predicate=is_metal_energy_card, max_count=99, per=30, base=0,
    prompt="Discard any number of Metal Energy cards from your hand",
)

psychic_60_plus = damage_per(count_energy("defender"), 20, base=60)
hydro_pressure = damage_per(
    count_energy("self", PokemonTypes.WATER), 20, base=60)
psystorm = damage_per(count_energy("both"), 20)
total_command = damage_per(
    lambda ctx: len(ctx.my_bench()) + len(ctx.opponent_bench()), 20)
frost_crush = damage_per(count_energy("opponent"), 20, base=10)
polar_spear_gx = damage_per(damage_counters_on("defender"), 50)
beauty_gx = damage_per(
    lambda ctx: ctx.prizes_taken(ctx.opponent_id), 50)
evil_admonition = damage_per(
    lambda ctx: sum(1 for p in ctx.opponent_pokemon_in_play()
                    if pokemon_has_ability(p)), 50)
psywave = damage_per(count_energy("defender"), 20)


async def _deal_printed(ctx):
    if getattr(ctx.ability, "damage", 0):
        await ctx.deal_damage()


async def evolve_self_from_deck(ctx):
    """Search for a card that evolves from this Pokémon and evolve it."""
    name = _logic_name(ctx.source)
    picks = await ctx.search_deck(
        lambda c: _direct_evolves_from(c, name),
        count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


async def loom_over(ctx):
    """90 minus 10 per damage counter on this Pokémon."""
    amount = max(0, 90 - 10 * damage_counters_on()(ctx))
    if amount:
        await ctx.deal_damage(amount)


async def rocket_fall(ctx):
    """30 plus 30 per Colorless in the opponent's Active retreat cost."""
    target = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, target) if target is not None else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + 30 * cost)


async def dust_cannon(ctx):
    """100 plus 10 per Colorless in the opponent's Active retreat cost."""
    target = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, target) if target is not None else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + 10 * cost)


async def eleventh_hour_tackle(ctx):
    """50, +130 if 3 or fewer cards remain in the deck."""
    bonus = 130 if len(ctx.deck()) <= 3 else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def lunar_payback(ctx):
    """Discard an Energy; if you do, swap damage counters with the Defending Pokémon."""
    energies = ctx.attached_energies(ctx.attacker)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy to discard")
    if not picks:
        return
    await ctx.discard_cards(picks)
    me, them = ctx.attacker, ctx.defender
    if me is None or them is None:
        return
    mine = max(0, (ctx.max_hp(me) - me.get_attribute(AttrID.HP, 0)) // 10)
    theirs = max(0, (ctx.max_hp(them) - them.get_attribute(AttrID.HP, 0)) // 10)
    await ctx.set_damage_counters(me, theirs)
    await ctx.set_damage_counters(them, mine)


async def damage_transport(ctx):
    """Move 4 damage counters from each of your Pokémon to the opponent's Active."""
    dest = ctx.opponent_active()
    if dest is None:
        return
    for pokemon in list(ctx.my_pokemon_in_play()):
        await ctx.move_damage_counters(pokemon, dest, max_count=4)


async def dangerous_stinger(ctx):
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


async def steel_short(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and _is_typed(ctx.board, defender, PokemonTypes.METAL):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)


async def ice_shard(ctx):
    bonus = 40 if (ctx.defender is not None
                   and _is_typed(ctx.board, ctx.defender, PokemonTypes.FIGHTING)) else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def hunters_nails(ctx):
    await bonus_if(defender_has_any_condition, 60)(ctx)


async def psychic_resonance(ctx):
    has_psychic = any(
        _is_typed(ctx.board, p, PokemonTypes.PSYCHIC)
        for p in ctx.opponent_pokemon_in_play())
    await ctx.deal_damage((ctx.ability.damage or 0) + (60 if has_psychic else 0))


async def palette_of_friends(ctx):
    types = set()
    for pokemon in ctx.my_bench():
        types.update(_pokemon_types(ctx.board, pokemon))
    amount = 10 * len(types)
    if amount:
        await ctx.deal_damage(amount)


async def identify(ctx):
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    bonus = 80 if any(is_pokemon_card(c) for c in cards) else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def royal_blades(ctx):
    bonus = 100 if ctx.played_trainer_this_turn("Cynthia") else 0
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def exact_revenge(ctx):
    bonus = 0
    for ko in ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, []):
        if _is_typed_archetype(ko.get("archetype_id"), PokemonTypes.FIGHTING):
            bonus = 70
            break
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def dangerous_lick(ctx):
    heads = await ctx.flip_until_tails("Dangerous Lick")
    await ctx.deal_damage((ctx.ability.damage or 0) + 50 * heads)
    if heads == 0:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


async def petal_dance(ctx):
    results = await ctx.flip_coins(3, "Petal Dance")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(30 * heads)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


async def fire_blaster(ctx):
    energies = ctx.attached_energies(ctx.attacker)
    bonus = 0
    if len(energies) >= 2 and await ctx.ask_yes_no(
            "Discard 2 Energy from this Pokémon for 80 more damage?"):
        picks = await ctx.choose_cards(
            energies, 2, prompt="Choose 2 Energy to discard")
        if len(picks) == 2:
            await ctx.discard_cards(picks)
            bonus = 80
    await ctx.deal_damage((ctx.ability.damage or 0) + bonus)


async def volt_bolt(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 99,
        predicate=lambda c: energy_provides_type(c, PokemonTypes.LIGHTNING.value),
        prompt="Discard all Lightning Energy from this Pokémon",
    )
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Choose a Pokémon to take 150 damage")
    if picks:
        await ctx.deal_damage(150, target=picks[0])


async def aqua_blast(ctx):
    await self_energy_discard_attack(count=1, energy_type=PokemonTypes.WATER)(ctx)


async def draco_meteor_barrage_effect(ctx):
    n = count_energy("self", PokemonTypes.GRASS)(ctx)
    results = await ctx.flip_coins(n, "Draco Meteor Barrage") if n else []
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(80 * heads)


async def spike_armor(ctx):
    await ctx.deal_damage()
    if ctx.attacker is not None and not ctx.effects_blocked(ctx.attacker):
        ctx.add_passive_through_opponents_turn(ctx.attacker, SpikeArmorPassive())


async def sticky_smokescreen(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.require_attack_flip(defender, coins=2)


async def hone_claws(ctx):
    from spirit.game.card_effects.passives_common import apply_own_next_turn_boost
    # Pierce prints 30; next turn its base is 90.
    await apply_own_next_turn_boost(ctx, 60, attack_title="Pierce")


async def sneaky_smash(ctx):
    pool = [e for p in ctx.opponent_pokemon_in_play()
            for e in ctx.attached_energies(p)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, prompt="Choose an Energy to discard from an opponent's Pokémon")
    if picks:
        await ctx.discard_cards(picks)


async def rip_and_run(ctx):
    await discard_random_from_hand(ctx, ctx.opponent_id, 1)
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


async def gentle_bite(ctx):
    from spirit.game.card_effects.passives_common import apply_defender_debuff
    await ctx.deal_damage()
    await apply_defender_debuff(ctx, 40)


async def own_the_place(ctx):
    await ctx.deal_damage()
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        await ctx.discard_stadium()
        await apply_protection(ctx, prevent=True, effects_too=True)


async def toss_aside(ctx):
    await ctx.deal_damage()
    extra = max(0, ctx.hand_size(ctx.opponent_id) - 3)
    if extra:
        await discard_random_from_hand(ctx, ctx.opponent_id, extra)


async def earthquake(ctx):
    await ctx.deal_damage()
    for pokemon in list(ctx.my_bench()):
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


async def flower_tornado(ctx):
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    if len(mine) >= 2:
        await ctx.move_energy_freely(mine, mine, predicate=is_grass_energy)


async def spatial_control(ctx):
    active = ctx.attacker
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    await ctx.move_energy_freely(bench, [active])


async def zero_vanish_gx(ctx):
    await ctx.deal_damage()
    energies = [e for p in ctx.opponent_pokemon_in_play()
                for e in ctx.attached_energies(p)]
    if energies:
        await ctx.shuffle_into_deck(energies, ctx.opponent_id)


async def timeless_gx(ctx):
    await ctx.deal_damage()
    ctx.take_extra_turn()


async def blaster_gx(ctx):
    await ctx.deal_damage()
    await ctx.turn_prizes_face_up()


async def moons_eclipse_gx(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)


async def suns_eclipse_gx(ctx):
    await ctx.deal_damage()


async def lighting_gx(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=0,
        prompt="Choose a card to add to your opponent's Prize cards",
    )
    if picks:
        await ctx.put_in_prizes(picks, player_id=ctx.opponent_id, append=True)


async def magical_swap(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)]
    if len(pool) < 2:
        return
    total = 0
    for pokemon in pool:
        dmg = max(0, ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0))
        counters = dmg // 10
        if counters:
            total += counters
            await ctx.heal(counters * 10, pokemon)
    if total:
        await ctx.place_damage_counters(total, pool)


async def invasion(ctx):
    await ctx.switch_active(ctx.player_id, ctx.source)


def invasion_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None or is_in_active_spot(pokemon):
        return False
    return board.active_pokemon(player_id) is not None


async def breath_of_the_leaves(ctx):
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if _has_energy(ctx, p) and _is_damaged(ctx, p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to heal 50 damage")
    if target is not None:
        await ctx.heal(50, target)


def breath_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None or not is_in_active_spot(pokemon):
        return False
    for p in board.pokemon_in_play(player_id):
        if any(is_energy_card(c) for c in p.children):
            if p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p):
                return True
    return False


async def grand_bloom_gx(ctx):
    basics = [p for p in ctx.my_bench() if is_basic_pokemon(p)]
    for pokemon in basics:
        name = _logic_name(pokemon)
        picks = await ctx.search_deck(
            lambda c, n=name: _direct_evolves_from(c, n),
            count=1, minimum=0,
            prompt=f"Choose a card that evolves from {name}.",
        )
        if picks:
            await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()


async def exeggutors_paradise(ctx):
    eggs = [p for p in ctx.my_bench() if _logic_name(p) == "Exeggcute"]
    for pokemon in eggs:
        picks = await ctx.search_deck(
            lambda c: _logic_name(c) in ("AlolanExeggutor", "AlolanExeggutorGX"),
            count=1, minimum=0,
            prompt="Choose an Alolan Exeggutor or Alolan Exeggutor-GX.",
        )
        if picks:
            await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()


async def chaotic_star(ctx):
    cards = [c for c in ctx.hand() if is_psychic_energy(c)]
    if not cards:
        return
    if not await ctx.ask_yes_no(
            "Attach up to 2 Psychic Energy cards from your hand to this Pokémon?"):
        return
    picks = await ctx.choose_cards(
        cards, min(2, len(cards)), minimum=0,
        prompt="Choose up to 2 Psychic Energy cards to attach")
    for energy in picks:
        await ctx.attach_energy(energy, ctx.source)


async def nightmare_star(ctx):
    cards = [c for c in ctx.hand() if is_darkness_energy(c)]
    if not cards:
        return
    if not await ctx.ask_yes_no(
            "Attach up to 2 Darkness Energy cards from your hand to this Pokémon?"):
        return
    picks = await ctx.choose_cards(
        cards, min(2, len(cards)), minimum=0,
        prompt="Choose up to 2 Darkness Energy cards to attach")
    for energy in picks:
        await ctx.attach_energy(energy, ctx.source)


async def _star_attach_from_discard(ctx, predicate, prompt):
    n = len(ctx.opponent_pokemon_in_play())
    if n <= 0:
        return
    cards = [c for c in ctx.discard_pile() if predicate(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, min(n, len(cards)), minimum=0, prompt=prompt)
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


async def full_moon_star(ctx):
    await _star_attach_from_discard(
        ctx, is_psychic_energy,
        "Choose Psychic Energy cards from your discard pile to attach")


async def radiant_star(ctx):
    await _star_attach_from_discard(
        ctx, is_metal_energy_card,
        "Choose Metal Energy cards from your discard pile to attach")


async def magnetic_circuit(ctx):
    cards = [c for c in ctx.hand() if is_metal_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose a Metal Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Metal Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


def magnetic_circuit_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_metal_energy_card(c) for c in hand.children)


async def change_clothes(ctx):
    tools = [tool for tool, poke in ctx.tools_in_play()
             if poke.owning_player_id == ctx.player_id]
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, 1, prompt="Choose a Pokémon Tool to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


def change_clothes_condition(board, player_id, pokemon=None) -> bool:
    for poke in board.pokemon_in_play(player_id):
        if any(c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
               for c in poke.children):
            return True
    return False


async def incandescent_body(ctx):
    if not is_in_active_spot(ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.BURNED)


async def precognitive_aura(ctx):
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card.")
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


def precognitive_aura_condition(board, player_id, pokemon=None) -> bool:
    return any(_logic_name(p) == "Garchomp" for p in board.pokemon_in_play(player_id))


async def resource_management(ctx):
    cards = list(ctx.discard_pile())
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 3, minimum=0, ordered=True,
        prompt="Choose up to 3 cards to put on the bottom of your deck, in order.",
    )
    for card in reversed(picks):
        await ctx.put_on_bottom_of_deck(card)


async def snuggly_generator(ctx):
    targets = [p for p in ctx.my_bench() if has_attack_titled("Nuzzle")(p)]
    for pokemon in targets:
        picks = await ctx.search_deck(
            is_lightning_energy, count=1, minimum=0,
            prompt="Choose a Lightning Energy card to attach.",
        )
        if picks:
            await ctx.attach_energy(picks[0], pokemon)
    await ctx.shuffle_deck()


async def coax(ctx):
    space = BENCH_CAPACITY - len(ctx.my_bench())
    take = min(3, space)
    used_types = set()
    for _ in range(take):
        blocked = set(used_types)

        def pred(card, blocked=blocked):
            if not is_basic_pokemon(card):
                return False
            types = set(card.get_attribute(AttrID.POKEMON_TYPES) or [])
            return not (types & blocked)

        picks = await ctx.search_deck(
            pred, count=1, minimum=0,
            prompt="Choose a Basic Pokémon of a different type.",
        )
        if not picks:
            break
        if await ctx.bench_pokemon(picks[0]):
            used_types.update(picks[0].get_attribute(AttrID.POKEMON_TYPES) or [])
    await ctx.shuffle_deck()


async def searching_magnet(ctx):
    await search_to_hand(
        is_metal_energy_card, count=3, minimum=0,
        prompt="Choose up to 3 Metal Energy cards.",
    )(ctx)


async def deep_currents(ctx):
    await recover_from_discard(
        is_water_energy, count=5, minimum=0, to="deck_shuffle",
        prompt="Choose up to 5 Water Energy cards to shuffle into your deck",
    )(ctx)


lightless_world = recover_from_discard(
    is_supporter_card, count=2, minimum=0,
    prompt="Choose up to 2 Supporter cards",
)

illuminate = search_to_hand(
    is_fairy_pokemon, count=1, minimum=0,
    prompt="Choose a Fairy Pokémon.",
)


# ======================================================================
# Trainers
# ======================================================================

cynthia = shuffle_hand_into_deck_draw(6)
pokemon_fan_club = search_to_hand(
    is_basic_pokemon, count=2, minimum=0,
    prompt="Choose up to 2 Basic Pokémon.",
)
looker_whistle = search_to_hand(
    is_looker_card, count=2, minimum=0,
    prompt="Choose up to 2 cards named Looker.",
)


def cyrus_condition(board, player_id, pokemon=None) -> bool:
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    types = set(_pokemon_types(board, active))
    return bool(types & _WATER_OR_METAL)


async def cyrus(ctx):
    """Opponent keeps 2 Benched Pokémon; shuffle the rest into their deck."""
    bench = list(ctx.opponent_bench())
    if len(bench) <= 2:
        return
    keep = await ctx.choose_cards(
        bench, 2, prompt="Choose 2 Benched Pokémon to keep",
        player_id=ctx.opponent_id,
    )
    if len(keep) < 2:
        keep = bench[:2]
    keep_ids = {p.entity_id for p in keep}
    for pokemon in bench:
        if pokemon.entity_id not in keep_ids:
            await ctx.shuffle_into_deck(full_stack(pokemon), ctx.opponent_id)


def gardenia_condition(board, player_id, pokemon=None) -> bool:
    for poke in board.pokemon_in_play(player_id):
        if any(is_grass_energy(c) for c in poke.children):
            if poke.get_attribute(AttrID.HP, 0) < effective_max_hp(board, poke):
                return True
    return False


async def gardenia(ctx):
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if any(is_grass_energy(c) for c in ctx.attached_energies(p))
        and _is_damaged(ctx, p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to heal 80 damage")
    if target is not None:
        await ctx.heal(80, target)


async def looker(ctx):
    """Draw 3 cards from the bottom of the deck."""
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    if not deck or not deck.children:
        return
    cards = list(deck.children[:3])
    await ctx.put_in_hand(cards, reveal=False)


def looker_condition(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def mars(ctx):
    drawn = await ctx.draw_cards(2)
    if drawn:
        await discard_random_from_hand(ctx, ctx.opponent_id, 1)


async def volkner(ctx):
    items, energy = await ctx.search_deck_groups(
        [
            (is_item_card, 1, "Choose an Item card"),
            (is_lightning_energy, 1, "Choose a Lightning Energy card"),
        ],
        prompt="Choose an Item card and a Lightning Energy card",
    )
    await ctx.put_in_hand(list(items) + list(energy), reveal=True)
    await ctx.shuffle_deck()


async def order_pad(ctx):
    results = await ctx.flip_coins(1, "Order Pad")
    if results and results[0]:
        await search_to_hand(
            is_item_card, count=1, minimum=0, prompt="Choose an Item card.",
        )(ctx)


def mt_coronet_condition(board, player_id, stadium=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_metal_energy_card(c) for c in discard.children)


async def mt_coronet(ctx):
    energy = [c for c in ctx.discard_pile() if is_metal_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 Metal Energy cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


MT_CORONET_ABILITY = Ability(
    title="Mt. Coronet",
    game_text="Once during each player's turn, that player may put 2 Metal Energy cards from their discard pile into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=mt_coronet,
    condition=mt_coronet_condition,
)


