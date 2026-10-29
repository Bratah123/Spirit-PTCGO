"""Forbidden Light (SM6) attack, ability, trainer, energy, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import (
    AttrID, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Ability, Activations, TRAINER_EFFECTS_BY_GUID, def_for, is_ultra_beast,
    unimplemented,
)
from spirit.game.session.effects import (
    full_stack,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_supporter_card,
)
from spirit.game.session.passives import (
    Passive, carrier_pokemon, effective_max_hp, effective_retreat_cost,
)
from spirit.game.card_effects.attacks_common import (
    bonus_if,
    count_bench,
    count_energy,
    count_in_play,
    count_prizes_remaining,
    damage_per,
    defender_has_condition,
    gx_used,
    has_tool,
    snipe_attack,
)
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost,
    is_in_active_spot,
    prevent_damage_when,
    trainer_effect_shield_passive,
)
from spirit.game.card_effects.pokemon import energy_provides_type, is_lightning_energy
from spirit.game.card_effects.sm3 import (
    is_gx_or_ex,
    is_grass_energy,
    is_psychic_energy,
    is_tool_card,
    is_water_energy,
)
from spirit.game.card_effects.sm4 import is_lightning_pokemon, is_stadium_card
from spirit.game.card_effects.sm5 import (
    _is_typed_archetype,
    go_second_first_turn,
    is_fairy_pokemon,
)
from spirit.game.card_effects.sl import is_benched
from spirit.game.card_effects.support_common import (
    attach_from_discard,
    opponent_switches,
    recover_from_discard,
    search_attach_energy,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    is_basic_energy_card,
    is_energy_card,
    opponent_has_bench,
)


UNIT_ENERGY_FDY = [
    [PokemonTypes.FIGHTING], [PokemonTypes.DARKNESS], [PokemonTypes.FAIRY],
]
_BENCH_TYPES = {PokemonTypes.GRASS.value, PokemonTypes.WATER.value,
                PokemonTypes.LIGHTNING.value}


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
    return pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)


def _is_typed(board, pokemon, pokemon_type: PokemonTypes) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return pokemon_type.value in types


def _stadium_in_play(board):
    area = board.find_global_area("activeStadium")
    return next(iter(area.children), None) if area and area.children else None


def is_fighting_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIGHTING.value)


def is_basic_psychic_energy(card) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.PSYCHIC.value)


def is_fighting_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.FIGHTING.value in types


def is_fire_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.FIRE.value in types


def is_dragon_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.DRAGON.value in types


def is_psychic_or_dragon_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and bool(
        {PokemonTypes.PSYCHIC.value, PokemonTypes.DRAGON.value} & set(types)
    )


def is_ultra_beast_card(card) -> bool:
    return is_ultra_beast(getattr(card, "archetype_id", None))


def is_unidentified_fossil(card) -> bool:
    return _display_name(card) == "Unidentified Fossil"


def _runnable_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


def _named_on_bench(ctx, logic_name: str) -> bool:
    return any(_logic_name(p) == logic_name for p in ctx.my_bench())


def _ub_in_play(ctx, side: str = "opponent") -> bool:
    pool = ctx.opponent_pokemon_in_play() if side == "opponent" else ctx.my_pokemon_in_play()
    return any(is_ultra_beast(p.archetype_id) for p in pool)


def _alolan_in_play(ctx) -> int:
    return sum(
        1 for p in ctx.my_pokemon_in_play()
        if "Alolan" in _logic_name(p) or "Alolan" in _display_name(p)
    )


def _basic_energy_types_in_discard(ctx) -> int:
    types = set()
    for card in ctx.discard_pile():
        if is_basic_energy_card(card):
            types.update(card.get_attribute(AttrID.POKEMON_TYPES) or [])
    return len(types)


def used_attack_last_own_turn(title: str):
    def cond(ctx) -> bool:
        titles = ctx.session.turn_state.attack_titles_prev_turn_by_player.get(
            ctx.player_id, [])
        return title in titles
    return cond


def _lysandre_labs_in_play(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    return stadium is not None and _display_name(stadium) == "Lysandre Labs"


def _evolved_from_this_turn(ctx, logic_name: str) -> bool:
    attacker = ctx.attacker
    if attacker is None:
        return False
    entered = ctx.session.turn_state.entered_play_turn.get(attacker.entity_id)
    if entered != ctx.session.turn_state.turn_number:
        return False
    return any(_logic_name(c) == logic_name for c in attacker.children)


# ======================================================================
# Passives
# ======================================================================

class PrincessCheersPassive(Passive):
    """While benched, your Fighting Pokémon's attacks do +20 to the Active."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or is_in_active_spot(me):
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != me.owning_player_id:
            return
        if not is_fighting_pokemon(attacker):
            return
        if "princess_cheers" in calc.applied_once:
            return
        calc.applied_once.add("princess_cheers")
        calc.amount += 20


class StickyMembranePassive(Passive):
    """While Active, opponent's attacks cost [C] more."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        if me is None or not is_in_active_spot(me):
            return cost
        if pokemon.owning_player_id == me.owning_player_id:
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


class FrubblesPassive(Passive):
    """If this Pokémon has Water Energy attached, it has no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        if me is not pokemon:
            return cost
        if any(is_water_energy(e) for e in pokemon.children):
            return 0
        return cost


class EarthenAuraPassive(Passive):
    """This Pokémon's attacks aren't affected by Weakness or Resistance."""

    def modify_weakness(self, calc, carrier):
        if carrier_pokemon(carrier) is calc.attacker:
            calc.weakness_applies = False

    def modify_resistance(self, calc, carrier):
        if carrier_pokemon(carrier) is calc.attacker:
            calc.resistance_applies = False


class SilentWavesPassive(Passive):
    """If Azelf is in play, opponent's Pokémon have no Resistance."""

    def modify_resistance(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None:
            return
        if not any(_logic_name(p) == "Azelf" for p in calc.board.pokemon_in_play(
                me.owning_player_id)):
            return
        if calc.target is not None \
                and calc.target.owning_player_id != me.owning_player_id:
            calc.resistance_applies = False


class TyrannicalHeartPassive(Passive):
    """If you don't have more Pokémon in play than the opponent: +60 damage
    and take 30 less."""

    def _not_more(self, me, board) -> bool:
        opp = _other_player(board, me.owning_player_id)
        if opp is None:
            return True
        return len(board.pokemon_in_play(me.owning_player_id)) <= len(
            board.pokemon_in_play(opp))

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or calc.attacker is not me:
            return
        if not (calc.is_attack and calc.is_opposing):
            return
        if not self._not_more(me, calc.board):
            return
        calc.amount += 60

    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or calc.target is not me or not calc.is_attack:
            return
        if not self._not_more(me, calc.board):
            return
        calc.amount = max(0, calc.amount - 30)


class MetalFryingPanPassive(Passive):
    """Metal holder takes 30 less from attacks and has no Weakness."""

    def _metal_holder(self, target, carrier) -> bool:
        holder = carrier_pokemon(carrier)
        if holder is not target:
            return False
        types = target.get_attribute(AttrID.POKEMON_TYPES) or []
        return PokemonTypes.METAL.value in types

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if self._metal_holder(calc.target, carrier):
            calc.amount = max(0, calc.amount - 30)

    def modify_weakness(self, calc, carrier):
        if self._metal_holder(calc.target, carrier):
            calc.weakness_applies = False


class LysandreLabsPassive(Passive):
    """Pokémon Tool cards in play have no effect."""

    def suppresses_tool(self, tool, carrier) -> bool:
        return True


class BeastEnergyPassive(Passive):
    """On an Ultra Beast: every type 1-at-a-time, and that UB's attacks do
    +30 to the opponent's Active."""

    def modify_energy_provided(self, options, energy, holder, board):
        definition = def_for(getattr(energy, "archetype_id", None))
        if not isinstance(getattr(definition, "passive", None), BeastEnergyPassive):
            return options
        if holder is not None and is_ultra_beast(holder.archetype_id):
            return ALL_TYPES_ONE_AT_A_TIME
        return options

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker:
            return
        if not is_ultra_beast(holder.archetype_id):
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        calc.amount += 30


class TickingKnockOutPassive(Passive):
    """During my next turn, damage to the opponent's Active KOs it."""

    def __init__(self, owner_player_id):
        self.owner_player_id = owner_player_id

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.amount > 0 and calc.to_active):
            return None
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != self.owner_player_id:
            return None
        if target.owning_player_id == self.owner_player_id:
            return None
        current = target.get_attribute(AttrID.HP, 0)
        return max(calc.amount, current)


class NoPrizeOnKoPassive(Passive):
    """If this Pokémon is Knocked Out, take 0 Prize cards for it."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is pokemon:
            return 0
        return count


unnerve_passive = trainer_effect_shield_passive(
    supporters_only=False,
    protects=lambda affected, carrier: carrier_pokemon(carrier) is affected,
)
princess_cheers_passive = PrincessCheersPassive()
sticky_membrane_passive = StickyMembranePassive()
frubbles_passive = FrubblesPassive()
earthen_aura_passive = EarthenAuraPassive()
silent_waves_passive = SilentWavesPassive()
tyrannical_heart_passive = TyrannicalHeartPassive()
metal_frying_pan_passive = MetalFryingPanPassive()
lysandre_labs_passive = LysandreLabsPassive()


# ======================================================================
# Attack / ability effects
# ======================================================================

tropical_shake = damage_per(
    _basic_energy_types_in_discard, 20, base=20, cap=120)
alolan_club = damage_per(_alolan_in_play, 20)
beast_raid = damage_per(
    count_in_play("mine", is_ultra_beast_card), 20)
dangerous_rogue = damage_per(count_bench("opponent"), 20, base=20)
meowstic_psychic = damage_per(count_energy("defender"), 30, base=30)
shadowy_hunter_gx = snipe_attack(130)
aura_strike = bonus_if(lambda ctx: _evolved_from_this_turn(ctx, "Riolu"), 90)
sledgehammer = bonus_if(
    lambda ctx: count_prizes_remaining("opponent")(ctx) == 4, 90)
white_ray = bonus_if(lambda ctx: count_prizes_remaining()(ctx) == 1, 90)
electrichain = bonus_if(
    lambda ctx: any(is_lightning_pokemon(p) for p in ctx.my_bench()), 30)
bubble_trap = bonus_if(used_attack_last_own_turn("Bubble"), 80)
peace_maker = bonus_if(lambda ctx: _ub_in_play(ctx, "opponent"), 30)
calm_strike = bonus_if(gx_used, 60)
mind_splash = bonus_if(lambda ctx: _named_on_bench(ctx, "Uxie"), 50)
resonance = bonus_if(defender_has_condition(SpecialConditions.CONFUSED), 70)
dominating_fangs = bonus_if(_lysandre_labs_in_play, 60)
searching_magnet = search_to_hand(
    is_lightning_energy, count=3, reveal=True,
    prompt="Choose up to 3 Lightning Energy cards.",
)
multiply = search_to_bench(
    lambda c: _logic_name(c) == "Exeggcute",
    prompt="Choose an Exeggcute to put onto your Bench.",
)
secret_blessings = recover_from_discard(
    lambda c: is_pokemon_card(c) or is_basic_energy_card(c),
    count=3, minimum=0, to="deck_shuffle",
    prompt="Choose up to 3 Pokémon and/or basic Energy cards.",
)
trinity_star = search_attach_energy(
    is_basic_energy_card, count=3,
    prompt="Choose up to 3 basic Energy cards to attach.",
)
cell_connector = attach_from_discard(
    is_fighting_energy, count=2, target="self", minimum=0,
    prompt="Choose up to 2 Fighting Energy cards to attach.",
)
psychic_recharge = attach_from_discard(
    is_psychic_energy, count=1, target=is_benched, minimum=1,
    prompt="Choose a Psychic Energy card to attach.",
)
exact_revenge = bonus_if(
    lambda ctx: any(
        _is_typed_archetype(ko.get("archetype_id"), PokemonTypes.PSYCHIC)
        for ko in ctx.session.turn_state.kos_by_attack_last_turn.get(
            ctx.player_id, [])
    ),
    70,
)


def evolve_place_counters(n: int):
    """On evolve: you may put n damage counters on 1 of the opponent's Pokémon."""
    async def effect(ctx):
        if not await ctx.ask_yes_no(
                f"Put {n} damage counters on 1 of your opponent's Pokémon?"):
            return
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your opponent's Pokémon")
        if target is not None:
            await ctx.deal_damage(n * 10, target=target, as_counters=True)
    return effect


shuriken_flurry = evolve_place_counters(3)
gale_shuriken = evolve_place_counters(2)


async def blessings_of_the_frost(ctx):
    if not await ctx.ask_yes_no(
            "Attach a Grass Energy from your discard pile to 1 of your Pokémon?"):
        return
    energy = [c for c in ctx.discard_pile() if is_grass_energy(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, prompt="Choose a Grass Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Grass Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def ticking_knock_out(ctx):
    ctx.add_passive_through_own_next_turn(
        ctx.attacker, TickingKnockOutPassive(ctx.player_id))


async def diamond_rain(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


async def frozen_ground(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_stadium_card)


async def psychic_abduction(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to shuffle into the deck")
    if target is not None:
        await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)


def psychic_abduction_condition(board, player_id, pokemon=None) -> bool:
    return go_second_first_turn(board, player_id) and opponent_has_bench(
        board, player_id)


async def seven_shock(ctx):
    await ctx.deal_damage()
    if len(ctx.hand()) == 7:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


async def break_open(ctx):
    await ctx.deal_damage()
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        await ctx.discard_stadium()
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


async def standing_by(ctx):
    await apply_own_next_turn_boost(
        ctx, 80, attack_title="Sharpshooting", opposing_active_only=False)


async def mystical_torch(ctx):
    active = ctx.opponent_active()
    if active is not None:
        await ctx.apply_special_condition(active, SpecialConditions.BURNED)


async def mountaintop_mining(ctx):
    extra = await ctx.ask_yes_no(
        "Discard the top 2 cards of your deck to do 40 more damage?")
    await ctx.deal_damage((ctx.ability.damage or 0) + (40 if extra else 0))
    if extra:
        await ctx.discard_cards(ctx.deck_top(2))


async def curse_of_the_blade(ctx):
    for pokemon in ctx.opponent_pokemon_in_play():
        if has_tool(pokemon):
            await ctx.deal_damage(
                30, target=pokemon, apply_modifiers=False, as_counters=True)


async def twister(ctx):
    results = await ctx.flip_coins(2, "Twister")
    heads = sum(1 for r in results if r)
    if heads == 0:
        return
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(
        defender, heads,
        prompt="Choose Energy to discard from the Defending Pokémon")


async def energy_teaser(ctx):
    await ctx.move_energy_freely(
        ctx.opponent_bench(), ctx.opponent_pokemon_in_play(), max_count=1)


def swirling_petals_condition(board, player_id, pokemon=None) -> bool:
    return opponent_has_bench(board, player_id)


async def swirling_petals(ctx):
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to switch into the Active Spot")
    if target is None:
        return
    await ctx.switch_active(ctx.opponent_id, target)
    mine = ctx.my_bench()
    if not mine:
        return
    pick = await ctx.choose_pokemon(mine, "Choose your new Active Pokémon")
    if pick is not None:
        await ctx.switch_active(ctx.player_id, pick)


async def wondrous_gift(ctx):
    results = await ctx.flip_coins(1, "Wondrous Gift")
    if not results or not results[0]:
        return
    items = [c for c in ctx.discard_pile() if is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(
        items, 1, prompt="Choose an Item card to put on top of your deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


def _dragon_next_turn(calc, carrier):
    holder = carrier_pokemon(carrier)
    attacker = calc.attacker
    return (
        holder is calc.target and calc.is_attack and calc.is_opposing
        and attacker is not None and is_dragon_pokemon(attacker)
    )


async def mist_guard(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, prevent_damage_when(_dragon_next_turn))


async def milk_drink(ctx):
    results = await ctx.flip_coins(2, "Milk Drink")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.heal(40 * heads, ctx.attacker)


async def hydration(ctx):
    if ctx.attaching_player_id != ctx.player_id:
        return
    if ctx.energy_receiver is not ctx.source:
        return
    energy = ctx.attached_energy
    if energy is None or not is_water_energy(energy):
        return
    await ctx.heal(20, ctx.source)


async def lords_valley(ctx):
    await ctx.deal_damage()
    if count_prizes_remaining()(ctx) in (2, 4, 6):
        await ctx.discard_cards(ctx.deck_top(10))


async def sky_drop(ctx):
    target = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, target) if target is not None else 0
    amount = max(0, (ctx.ability.damage or 0) - 20 * cost)
    if amount:
        await ctx.deal_damage(amount)


async def final_hour(ctx):
    if not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(30, target=target, apply_modifiers=False,
                              as_counters=True)


async def magnetic_circuit(ctx):
    cards = [c for c in ctx.hand() if is_lightning_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose a Lightning Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(),
        "Choose a Pokémon to attach Lightning Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


def magnetic_circuit_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_lightning_energy(c) for c in hand.children)


def psychic_recharge_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    bench = board.find_player_area(player_id, "bench")
    if not discard or not bench or not bench.children:
        return False
    return any(is_psychic_energy(c) for c in discard.children)


async def stinger_gx(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        area = ctx.board.find_player_area(pid, "prizePile")
        prizes = list(area.children) if area else []
        if prizes:
            await ctx.shuffle_into_deck(prizes, pid)
        top = list(ctx.deck_top(3, player_id=pid))
        if top:
            await ctx.put_in_prizes(top, player_id=pid)


async def destructive_sound(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    items = [c for c in cards if is_item_card(c)]
    if items:
        await ctx.discard_cards(items)


async def untamed_punch(ctx):
    damaged = _is_damaged(ctx, ctx.attacker)
    await ctx.deal_damage((ctx.ability.damage or 0) + (50 if damaged else 0))
    if not damaged:
        return
    for pokemon in (ctx.attacker, ctx.defender):
        if pokemon is not None:
            await ctx.apply_special_condition(pokemon, SpecialConditions.CONFUSED)


async def knockout_reviver(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, NoPrizeOnKoPassive())


async def abnormal_outbreak(ctx):
    spewpa, vivillon = await ctx.search_deck_groups(
        [
            (lambda c: _logic_name(c) == "Spewpa", 1, "Choose a Spewpa"),
            (lambda c: _logic_name(c) == "Vivillon", 1, "Choose a Vivillon"),
        ],
        prompt="Choose a Spewpa and a Vivillon",
    )
    await ctx.put_in_hand(list(spewpa) + list(vivillon), reveal=True)
    await ctx.shuffle_deck()


async def ultra_evolution(ctx):
    heads = (await ctx.flip_coins(1, "Ultra Evolution"))[0]
    if not heads:
        return
    picks = await ctx.search_deck(
        lambda c: is_pokemon_card(c) and _logic_name(c) == "Vivillon",
        count=1, minimum=0,
        prompt="Choose a Vivillon to evolve this Scatterbug.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.attacker, picks[0])
    await ctx.shuffle_deck()


async def growth(ctx):
    await ctx.deal_damage()
    cards = [c for c in ctx.hand() if is_grass_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=0, prompt="Choose a Grass Energy card to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


async def wink_wink(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    candidates = [c for c in cards if _runnable_supporter(c)]
    if not candidates:
        return
    if not await ctx.ask_yes_no(
            "Discard a Supporter card and use its effect?"):
        return
    picked = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a Supporter card to discard and use")
    if not picked:
        return
    await ctx.discard_cards(picked)
    effect = TRAINER_EFFECTS_BY_GUID[(picked[0].archetype_id or "").lower()]
    await effect(ctx)


async def photon_geyser(ctx):
    energies = [
        e for e in ctx.attached_energies(ctx.attacker)
        if is_basic_psychic_energy(e)
    ]
    await ctx.discard_cards(energies)
    await ctx.deal_damage((ctx.ability.damage or 0) + 80 * len(energies))


async def sky_scorching_light_gx(ctx):
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage(
            60, target=pokemon, apply_modifiers=False, as_counters=True)


def sky_scorching_condition(board, player_id, pokemon=None) -> bool:
    return sum(_prize_count(board, pid) for pid in board.player_ids) <= 6


def trinity_star_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    types = set()
    for poke in (bench.children if bench else []):
        types.update(poke.get_attribute(AttrID.POKEMON_TYPES) or [])
    return _BENCH_TYPES <= types


async def jet_geyser(ctx):
    water = [c for c in ctx.hand() if is_water_energy(c)]
    if not water:
        return
    picks = await ctx.choose_cards(
        water, 1, prompt="Discard a Water Energy card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await opponent_switches(ctx)


def jet_geyser_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_water_energy(c) for c in hand.children)


async def sanctuary_gx(ctx):
    dest = ctx.opponent_active()
    if dest is None:
        return
    for pokemon in list(ctx.my_pokemon_in_play()):
        await ctx.move_damage_counters(pokemon, dest)


async def cablegram(ctx):
    await ctx.deal_damage()
    if count_prizes_remaining()(ctx) == 3:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


async def doom_count_gx(ctx):
    defender = ctx.defender
    if defender is None:
        return
    counters = max(
        0, (ctx.max_hp(defender) - defender.get_attribute(AttrID.HP, 0)) // 10)
    if counters == 4:
        await ctx.session._resolve_raw_knockout(defender)


def _gx_ex_next_turn(calc, carrier):
    holder = carrier_pokemon(carrier)
    attacker = calc.attacker
    return (
        holder is calc.target and calc.is_attack and calc.is_opposing
        and attacker is not None and is_gx_or_ex(attacker)
    )


async def verdict_gx(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, prevent_damage_when(_gx_ex_next_turn))


# ======================================================================
# Trainers
# ======================================================================

def beast_ring_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None or _prize_count(board, opp) not in (3, 4):
        return False
    return any(is_ultra_beast(p.archetype_id)
               for p in board.pokemon_in_play(player_id))


beast_ring = search_attach_energy(
    is_basic_energy_card, count=2, distribute=False,
    target_pred=is_ultra_beast_card,
    prompt="Choose up to 2 basic Energy cards to attach to an Ultra Beast.",
)


def bonnie_condition(board, player_id, pokemon=None) -> bool:
    return _stadium_in_play(board) is not None


async def bonnie(ctx):
    await ctx.discard_stadium()
    ctx.session.turn_state.gx_unlocked.add("ZygardeGX")


def crasher_wake_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_water_energy(c)) >= 2


async def crasher_wake(ctx):
    water = [c for c in ctx.hand() if is_water_energy(c)]
    picks = await ctx.choose_cards(
        water, 2, prompt="Discard 2 Water Energy cards")
    if len(picks) < 2:
        return
    await ctx.discard_cards(picks)
    await search_to_hand(None, count=2, reveal=False, prompt="Choose up to 2 cards.")(ctx)


def diantha_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    if not discard or len(discard.children) < 2:
        return False
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    for ko in ts.kos_by_attack_last_turn.get(player_id, []):
        if _is_typed_archetype(ko.get("archetype_id"), PokemonTypes.FAIRY):
            return True
    return False


diantha = recover_from_discard(
    None, count=2, minimum=2,
    prompt="Choose 2 cards to put into your hand.",
)


def eneporter_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    pokemon_list = board.pokemon_in_play(opp)
    if len(pokemon_list) < 2:
        return False
    return any(is_special_energy(c) for p in pokemon_list for c in p.children)


async def eneporter(ctx):
    await ctx.move_energy_freely(
        ctx.opponent_pokemon_in_play(), ctx.opponent_pokemon_in_play(),
        predicate=is_special_energy, max_count=1,
        prompt="Choose a Special Energy to move",
    )


def fossil_excavation_map_condition(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    discard = board.find_player_area(player_id, "discard")
    if deck and deck.children:
        return True
    return bool(discard) and any(is_unidentified_fossil(c) for c in discard.children)


async def fossil_excavation_map(ctx):
    fossils = [c for c in ctx.discard_pile() if is_unidentified_fossil(c)]
    options = ["Search your deck for an Unidentified Fossil"]
    if fossils:
        options.append(
            "Put an Unidentified Fossil from your discard pile into your hand")
    choice = 0 if len(options) == 1 else await ctx.choose(
        "Choose 1:", options, use_panel=False)
    if choice == 0:
        await search_to_hand(
            is_unidentified_fossil, count=1, minimum=0, reveal=True,
            prompt="Choose an Unidentified Fossil.",
        )(ctx)
        return
    picks = await ctx.choose_cards(
        fossils, 1, prompt="Choose an Unidentified Fossil")
    await ctx.put_in_hand(picks, reveal=False)


def lysandre_prism_star_condition(board, player_id, pokemon=None) -> bool:
    if not any(is_fire_pokemon(p) for p in board.pokemon_in_play(player_id)):
        return False
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    discard = board.find_player_area(opp, "discard")
    return bool(discard and discard.children)


async def lysandre_prism_star(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if is_fire_pokemon(p))
    cards = list(ctx.discard_pile(ctx.opponent_id))
    if not cards or n <= 0:
        return
    picks = await ctx.choose_cards(
        cards, min(n, len(cards)),
        prompt="Choose cards from your opponent's discard pile for the Lost Zone")
    if picks:
        await ctx.move_to_lost_zone(picks)


def mysterious_treasure_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(hand and len(hand.children) >= 2 and deck and deck.children)


async def mysterious_treasure(ctx):
    discarded = await ctx.discard_from_hand(
        1, prompt="Discard a card from your hand", exclude=[ctx.source])
    if not discarded:
        return
    await search_to_hand(
        is_psychic_or_dragon_pokemon, count=1, minimum=0, reveal=True,
        prompt="Choose a Psychic or Dragon Pokémon.",
    )(ctx)


def ultra_recon_squad_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_ultra_beast_card(c) for c in hand.children)


async def ultra_recon_squad(ctx):
    beasts = [c for c in ctx.hand() if is_ultra_beast_card(c)]
    picks = await ctx.choose_cards(
        beasts, 2, minimum=0,
        prompt="Discard up to 2 Ultra Beast cards from your hand")
    await ctx.discard_cards(picks)
    if picks:
        await ctx.draw_cards(3 * len(picks))


def ultra_space_condition(board, player_id, stadium=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def ultra_space(ctx):
    await search_to_hand(
        is_ultra_beast_card, count=1, minimum=0, reveal=True,
        prompt="Choose an Ultra Beast card.",
    )(ctx)


ULTRA_SPACE_ABILITY = Ability(
    title="Ultra Space",
    game_text="Once during each player's turn, that player may search their deck for an Ultra Beast card, reveal it, put it into their hand, and shuffle their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=ultra_space,
    condition=ultra_space_condition,
)
