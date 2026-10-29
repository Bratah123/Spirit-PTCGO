"""Shining Legends (SL) attack, ability, trainer, and energy behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.data_utils import Attack, def_for
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import Passive, active_passives, effective_max_hp
from spirit.game.card_effects.passives_common import (
    is_in_active_spot,
    no_retreat_passive,
    opposing_active,
    prevent_damage_when,
)
from spirit.game.card_effects.pokemon import devolvable, devolve_depth, energy_provides_type
from spirit.game.card_effects.sm3 import is_grass_energy, is_water_energy
from spirit.game.card_effects.support_common import gust_then, opponent_switches
from spirit.game.card_effects.trainers import is_basic_energy_card, opponent_has_bench


def _is_basic_typed_energy(card, pokemon_type: PokemonTypes) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(card, pokemon_type.value)


def is_basic_lightning_energy(card) -> bool:
    return _is_basic_typed_energy(card, PokemonTypes.LIGHTNING)


def is_basic_darkness_energy(card) -> bool:
    return _is_basic_typed_energy(card, PokemonTypes.DARKNESS)


def _is_damaged(board, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def is_benched(pokemon) -> bool:
    parent = getattr(pokemon, "parent", None)
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"


# ======================================================================
# Passives
# ======================================================================

class IntimidatingPatternPassive(Passive):
    """While Active, the opponent's Active's attacks do 30 less (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        if not is_in_active_spot(carrier):
            return
        attacker = calc.attacker
        if attacker is None or not opposing_active(attacker, carrier):
            return
        calc.amount = max(0, calc.amount - 30)


class JungleTotemPassive(Passive):
    """Each basic Grass Energy on your Pokémon provides GrassGrass Energy."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            return options
        if not energy_provides_type(energy, PokemonTypes.GRASS.value):
            return options
        if any(len(option) >= 2 for option in options):
            return options
        active_here = any(
            isinstance(p, JungleTotemPassive)
            and c.owning_player_id == holder.owning_player_id
            for p, c in active_passives(board)
        )
        if not active_here:
            return options
        return [list(option) * 2 for option in options]


fabled_defense_passive = prevent_damage_when(
    lambda calc, carrier: (
        is_in_active_spot(carrier)
        and calc.target.owning_player_id == carrier.owning_player_id
        and not is_in_active_spot(calc.target)
    )
)

cursed_whirlpool_passive = no_retreat_passive(
    lambda pokemon, carrier: opposing_active(pokemon, carrier) and is_in_active_spot(carrier)
)


# ======================================================================
# Attack / ability effects
# ======================================================================

async def _poison_new_active(ctx, new_active):
    await ctx.apply_special_condition(new_active, SpecialConditions.POISONED)


flick_poison = gust_then(_poison_new_active)


def plunge_condition(board, player_id, pokemon):
    if is_in_active_spot(pokemon):
        return False
    active = board.active_pokemon(player_id)
    return active is not None and bool(board.attached_energies(active))


async def plunge(ctx):
    """Move all Energy from the Active to this Benched Pokémon, then switch."""
    active = ctx.my_active()
    dest = ctx.source
    if active is None or dest is None or dest is active:
        return
    energies = list(ctx.attached_energies(active))
    if not energies:
        return
    for energy in energies:
        await ctx.move_energy(energy, dest)
    await ctx.switch_active(ctx.player_id, dest)


def energy_reload_condition(board, player_id, pokemon):
    for other in board.pokemon_in_play(player_id):
        if other is pokemon:
            continue
        if any(is_grass_energy(e) for e in board.attached_energies(other)):
            return True
    return False


async def energy_reload(ctx):
    """Move a Grass Energy from 1 of your other Pokémon to this Pokémon."""
    others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    await ctx.move_energy_freely(
        others, [ctx.source],
        predicate=is_grass_energy, max_count=1,
        prompt="Move a Grass Energy to this Pokémon",
    )


def blessings_condition(board, player_id, pokemon=None):
    for target in board.pokemon_in_play(player_id):
        if not _is_damaged(board, target):
            continue
        if any(is_water_energy(e) for e in board.attached_energies(target)):
            return True
    return False


async def blessings_of_the_deep(ctx):
    """Heal 20 from 1 of your Pokémon that has any Water Energy attached."""
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
        and any(is_water_energy(e) for e in ctx.attached_energies(p))
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to heal 20 damage")
    if target is not None:
        await ctx.heal(20, target)


async def heat_cyclone(ctx):
    """You may have the opponent switch their Active with a Benched Pokémon."""
    if await ctx.ask_yes_no(
        "Have your opponent switch their Active Pokémon with 1 of their "
        "Benched Pokémon?"
    ):
        await opponent_switches(ctx)


def heat_cyclone_condition(board, player_id, pokemon=None):
    return opponent_has_bench(board, player_id)


async def let_loose(ctx):
    """You may have each player shuffle their hand into their deck and draw 4."""
    if not await ctx.ask_yes_no(
        "Have each player shuffle their hand into their deck and draw 4 cards?"
    ):
        return
    for pid, n in ((ctx.player_id, 4), (ctx.opponent_id, 4)):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(n, pid)


async def stellar_reign(ctx):
    """Printed damage; if the Active is evolved, put all Evolution cards into hand."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or not devolvable(defender) or ctx.effects_blocked(defender):
        return
    await ctx.devolve_pokemon(
        defender, steps=devolve_depth(defender), destination="hand")


async def trickster_gx(ctx):
    """Choose 1 of your opponent's Pokémon's attacks and use it as this attack."""
    candidates = []
    seen = set()
    for pokemon in ctx.opponent_pokemon_in_play():
        definition = def_for(pokemon.archetype_id)
        for ability in getattr(definition, "abilities", None) or []:
            if not isinstance(ability, Attack):
                continue
            key = (ability.title, ability.game_text)
            if key in seen:
                continue
            seen.add(key)
            candidates.append((pokemon, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(
                    ctx.attacker.entity_id, entry["abilityID"])


async def wrapped_in_wind(ctx):
    """Printed damage; you may attach a basic Energy from your hand to this Pokémon."""
    await ctx.deal_damage()
    cards = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not cards:
        return
    if not await ctx.ask_yes_no("Attach a basic Energy card from your hand to this Pokémon?"):
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose a basic Energy to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


def minun_on_bench(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Minun"
               for p in ctx.my_bench())


def bench_has_damage(ctx) -> bool:
    return any(p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p) for p in ctx.my_bench())


def defender_has_any_condition(ctx) -> bool:
    defender = ctx.defender
    return bool(defender and (defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))


def opponent_active_is_basic(ctx) -> bool:
    active = ctx.opponent_active()
    return active is not None and is_basic_pokemon(active)


# ======================================================================
# Trainers / Energy
# ======================================================================

def damage_mover_condition(board, player_id):
    pokemon = board.pokemon_in_play(player_id)
    if len(pokemon) < 2:
        return False
    return any(
        (effective_max_hp(board, p) - p.get_attribute(AttrID.HP, 0)) >= 30
        for p in pokemon
    )


async def damage_mover(ctx):
    """Move 3 damage counters from 1 of your Pokémon to another of your Pokémon."""
    mine = ctx.my_pokemon_in_play()
    sources = [
        p for p in mine
        if (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) >= 30
    ]
    if not sources:
        return
    source = await ctx.choose_pokemon(
        sources, "Choose a Pokémon to move 3 damage counters from")
    if source is None:
        return
    dests = [p for p in mine if p is not source]
    if not dests:
        return
    dest = await ctx.choose_pokemon(
        dests, "Choose a Pokémon to move the damage counters to")
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=3)


async def pokemon_breeder(ctx):
    """Draw 2 cards and heal 20 damage from your Active Pokémon."""
    await ctx.draw_cards(2)
    active = ctx.my_active()
    if active is not None:
        await ctx.heal(20, active)


async def warp_energy_on_attach(ctx):
    """When attached from hand to the Active, switch it with a Benched Pokémon."""
    target = ctx.attached_to
    if target is None or target is not ctx.my_active():
        return
    bench = ctx.my_bench()
    if not bench:
        return
    pick = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to switch into the Active Spot"
    ) or bench[0]
    await ctx.switch_active(ctx.player_id, pick)
