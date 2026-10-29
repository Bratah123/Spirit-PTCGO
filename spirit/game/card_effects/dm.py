"""Dragon Majesty (DM) attack, ability, trainer, tool, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.data_utils import subtypes_for
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import (
    bonus_if,
    condition_attack,
    count_energy,
    damage_all_opponents,
    damage_counters_on,
    damage_per,
    defender_has_condition,
    flip_damage,
    has_damage,
    self_energy_discard_attack,
    snipe_attack,
    spread_damage,
)
from spirit.game.card_effects.passives_common import (
    attack_effect_shield_passive,
    is_in_active_spot,
    prevent_damage_when,
    retreat_free_when,
    takes_less_passive,
    team_damage_boost_passive,
)
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.sm3 import is_fire_energy, is_gx_or_ex, is_water_energy
from spirit.game.card_effects.sm6 import is_dragon_pokemon, is_fire_pokemon
from spirit.game.card_effects.sl import is_benched
from spirit.game.card_effects.support_common import (
    attach_from_discard,
    distribute_energy,
    requires_hand,
    search_attach_energy,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import is_basic_energy_card, is_energy_card


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def is_water_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.WATER.value in types


def is_basic_water_energy(card) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.WATER.value)


def is_wishiwashi_gx(card) -> bool:
    return (
        is_pokemon_card(card)
        and _logic_name(card) == "Wishiwashi"
        and "GX" in subtypes_for(getattr(card, "archetype_id", None))
    )


def _gx_ex_next_turn(calc, carrier):
    holder = carrier_pokemon(carrier)
    attacker = calc.attacker
    return (
        holder is calc.target and calc.is_attack and calc.is_opposing
        and attacker is not None and is_gx_or_ex(attacker)
    )


def _has_basic_energy(pokemon) -> bool:
    return any(is_basic_energy_card(c) for c in pokemon.children)


def _water_energy_on_bench(board, player_id) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if bench is None:
        return False
    return any(
        is_water_energy(child)
        for pokemon in bench.children
        for child in pokemon.children
        if is_energy_card(child)
    )


# ======================================================================
# Passives
# ======================================================================

class ResoluteFlamePassive(Passive):
    """This Pokémon's attacks do +30 to the Active per opponent GX/EX."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is not calc.attacker:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        opponent_id = calc.target.owning_player_id if calc.target is not None else None
        if opponent_id is None:
            return
        n = sum(1 for p in calc.board.pokemon_in_play(opponent_id) if is_gx_or_ex(p))
        if n:
            calc.amount += 30 * n


class MeetUpPassive(Passive):
    """Your Wishiwashi-GX get +20 HP and +20 attack damage to the Active."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        return 20 if is_wishiwashi_gx(pokemon) else 0

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != carrier.owning_player_id:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if is_wishiwashi_gx(attacker):
            calc.amount += 20


class MurmursOfTheSeaPassive(Passive):
    """Your Water Pokémon can't be Confused."""

    def blocks_special_conditions(self, target, condition, carrier):
        if condition != SpecialConditions.CONFUSED:
            return False
        if target is None or target.owning_player_id != carrier.owning_player_id:
            return False
        return is_water_pokemon(target)


class WelaVolcanoParkPassive(Passive):
    """Burned Pokémon never recover during checkup, even on heads."""

    def blocks_burn_recovery(self, pokemon, carrier):
        return True


fight_song_passive = team_damage_boost_passive(
    20, attacker_pred=is_dragon_pokemon, once_key=None)
resolute_flame_passive = ResoluteFlamePassive()
meet_up_passive = MeetUpPassive()
murmurs_of_the_sea_passive = MurmursOfTheSeaPassive()
wela_volcano_park_passive = WelaVolcanoParkPassive()
dragon_guard_passive = attack_effect_shield_passive(
    protects=lambda target, carrier: (
        target.owning_player_id == carrier.owning_player_id
        and is_dragon_pokemon(target)
    ),
)
energy_guard_passive = takes_less_passive(
    20,
    protects=lambda target, carrier: (
        carrier_pokemon(carrier) is target and _has_basic_energy(target)
    ),
)
dragon_lift_passive = retreat_free_when(
    lambda pokemon, carrier: (
        pokemon.owning_player_id == carrier.owning_player_id
        and not is_gx_or_ex(pokemon)
    ),
)


# ======================================================================
# Attack / ability effects
# ======================================================================

async def bright_tone(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, prevent_damage_when(_gx_ex_next_turn))


async def euphoria_gx(ctx):
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    for pokemon in list(ctx.my_pokemon_in_play()):
        missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, pokemon)


fire_stream = self_energy_discard_attack(
    count=1, energy_type=PokemonTypes.FIRE, also=spread_damage(20))

firestarter = attach_from_discard(
    is_fire_energy, count=1, target=is_benched, minimum=1,
    prompt="Choose a Fire Energy card to attach to a Benched Pokémon.",
)


def firestarter_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    bench = board.find_player_area(player_id, "bench")
    if not discard or not bench or not bench.children:
        return False
    return any(is_fire_energy(c) for c in discard.children)


async def burning_fighter(ctx):
    if not await ctx.ask_yes_no("Discard the top 5 cards of your deck?"):
        return
    top = list(ctx.deck_top(5))
    if not top:
        return
    await ctx.discard_cards(top)
    for energy in [c for c in top if is_fire_energy(c)]:
        await ctx.attach_energy(energy, ctx.source)


async def bubble_shoot(ctx):
    amount = 20 * count_energy("self", PokemonTypes.WATER)(ctx)
    if amount <= 0:
        return
    await snipe_attack(amount, pool="any")(ctx)


async def heat_assist(ctx):
    fire = [c for c in ctx.hand() if is_fire_energy(c)]
    if not fire:
        return
    picks = await ctx.choose_cards(
        fire, 3, minimum=0,
        prompt="Choose up to 3 Fire Energy cards to attach.")
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


darmani_hands = flip_damage(coins=4, bonus_per_heads=50)


async def dragonporter_gx(ctx):
    space = BENCH_CAPACITY - len(ctx.my_bench())
    take = min(3, space)
    dragons = [c for c in ctx.discard_pile() if is_dragon_pokemon(c)]
    if take <= 0 or not dragons:
        return
    picks = await ctx.choose_cards(
        dragons, take, minimum=0,
        prompt="Choose up to 3 Dragon Pokémon to put onto your Bench.")
    for card in picks:
        await ctx.bench_pokemon(card)


dragon_wisdom = attach_from_discard(
    is_basic_energy_card, count=1, target=is_dragon_pokemon, minimum=0,
    prompt="Choose a basic Energy card to attach to a Dragon Pokémon.",
)


async def downpour(ctx):
    water = [c for c in ctx.hand() if is_water_energy(c)]
    if not water:
        return
    picks = await ctx.choose_cards(
        water, 1, prompt="Choose a Water Energy card to discard.")
    await ctx.discard_cards(picks)


def downpour_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_water_energy(c) for c in hand.children)


async def riptide(ctx):
    waters = [c for c in ctx.discard_pile() if is_basic_water_energy(c)]
    await ctx.deal_damage((ctx.ability.damage or 0) + 20 * len(waters))
    if waters:
        await ctx.shuffle_into_deck(waters)


async def commotion(ctx):
    if not is_in_active_spot(ctx.source):
        return
    for pokemon in list(ctx.my_bench()):
        await ctx.deal_damage(
            20, target=pokemon, apply_modifiers=False, as_counters=True)


charring_breath = bonus_if(
    defender_has_condition(SpecialConditions.BURNED), 0, else_nothing=True)

horsea_hydro_pump = damage_per(
    count_energy("self", PokemonTypes.WATER), 10, base=10)
seadra_hydro_pump = damage_per(
    count_energy("self", PokemonTypes.WATER), 20, base=10)
lapras_hydro_pump = damage_per(
    count_energy("self", PokemonTypes.WATER), 10, base=70)
kingdra_hydro_pump = damage_per(
    count_energy("self", PokemonTypes.WATER), 50, base=10)

maelstrom_gx = damage_all_opponents(40)
raging_uppercut = bonus_if(
    lambda ctx: damage_counters_on("self")(ctx) >= 8, 120)
kyurem_outrage = damage_per(damage_counters_on("self"), 10, base=20)
aqua_split = snipe_attack(40, also_base=True, count=2)
flame_charge = search_attach_energy(
    is_fire_energy, count=2, to_self=True,
    prompt="Choose up to 2 Fire Energy cards to attach to this Pokémon.",
)


async def vermilion_gx(ctx):
    await ctx.deal_damage()
    fire = [c for c in ctx.hand() if is_fire_energy(c)]
    if not fire:
        return
    if not await ctx.ask_yes_no(
            "Attach up to 5 Fire Energy cards from your hand to your Pokémon?"):
        return
    picks = await ctx.choose_cards(
        fire, 5, minimum=0,
        prompt="Choose up to 5 Fire Energy cards to attach.")
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


flame_jet_gx = snipe_attack(120, pool="any")


async def wash_out(ctx):
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    await ctx.move_energy_freely(
        bench, [active], predicate=is_water_energy, max_count=1,
        prompt="Choose a Water Energy to move to your Active Pokémon.")


def wash_out_condition(board, player_id, pokemon=None) -> bool:
    if board.active_pokemon(player_id) is None:
        return False
    return _water_energy_on_bench(board, player_id)


async def explosive_jet(ctx):
    pool = [
        energy for pokemon in ctx.my_pokemon_in_play()
        for energy in ctx.attached_energies(pokemon) if is_fire_energy(energy)
    ]
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Discard any amount of Fire Energy from your Pokémon",
    ) if pool else []
    await ctx.discard_cards(picks)
    if picks:
        await ctx.deal_damage(50 * len(picks))


dragon_nova_gx = condition_attack(
    SpecialConditions.BURNED, SpecialConditions.PARALYZED)
ring_of_fire = condition_attack(SpecialConditions.BURNED, no_retreat=True)

bolt_strike = flip_damage(coins=1, tails_self_damage=50)
zygarde_raging_blade = bonus_if(has_damage("self"), 60)


async def murmurs_of_the_sea_cure(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if is_water_pokemon(pokemon):
            await ctx.cure_condition(pokemon, SpecialConditions.CONFUSED)


# ======================================================================
# Trainers
# ======================================================================

def blaines_last_stand_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    cards = list(hand.children) if hand else []
    others = [c for c in cards if c is not pokemon]
    return len(others) == 0


async def blaines_last_stand(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if is_fire_pokemon(p))
    if n:
        await ctx.draw_cards(2 * n)


async def dragon_talon(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon) or not is_dragon_pokemon(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.parent is None \
            or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(
        30, target=attacker, apply_modifiers=False, as_counters=True)


fiery_flint_condition = requires_hand(n=2)


async def fiery_flint(ctx):
    discarded = await ctx.discard_from_hand(
        2, prompt="Discard 2 other cards from your hand.", exclude=[ctx.source])
    if len(discarded) < 2:
        return
    await search_to_hand(
        is_fire_energy, count=4, minimum=0, reveal=True,
        prompt="Choose up to 4 Fire Energy cards.",
    )(ctx)


def ko_last_turn_condition(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    return bool(ts.kos_by_attack_last_turn.get(player_id))


lance_prism_star = search_to_bench(
    is_dragon_pokemon, count=2,
    prompt="Choose up to 2 Dragon Pokémon to put onto your Bench.",
)


def switch_raft_condition(board, player_id, pokemon=None) -> bool:
    active = board.active_pokemon(player_id)
    bench = board.find_player_area(player_id, "bench")
    return (
        active is not None and is_water_pokemon(active)
        and bench is not None and bool(bench.children)
    )


async def switch_raft(ctx):
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench or not is_water_pokemon(active):
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    await ctx.heal(30, active)


async def zinnia(ctx):
    energy = [c for c in ctx.hand() if is_basic_energy_card(c)]
    dragons = [p for p in ctx.my_pokemon_in_play() if is_dragon_pokemon(p)]
    if not energy or not dragons:
        return
    picks = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach.")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        dragons, "Choose a Dragon Pokémon to attach the Energy to")
    if target is None:
        return
    for card in picks:
        await ctx.attach_energy(card, target)
