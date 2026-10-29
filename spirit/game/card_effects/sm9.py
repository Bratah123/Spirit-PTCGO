"""Team Up (SM9) attack, ability, trainer, tool, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import (
    AttrID, CLIENT_POKEMON_TYPE_NAMES, CLIENT_SPECIAL_CONDITION_NAMES,
    PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Ability, Activations, TRAINER_EFFECTS_BY_GUID, def_for, evolves_from,
    is_ultra_beast, unimplemented,
)
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_evolution_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_stage1_pokemon,
    is_stage2_pokemon,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.passives import (
    Passive, carrier_pokemon, effective_max_hp, effective_pokemon_types,
)
from spirit.game.card_effects.attacks_common import (
    _printed,
    bonus_if,
    condition_attack,
    count_bench,
    count_discard,
    count_energy,
    count_prizes_remaining,
    damage_counters_on,
    damage_per,
    discard_for_bonus,
    discard_opponent_energy_attack,
    discard_random_from_hand,
    flip_or_nothing,
    gx_used,
    has_attack_titled,
    has_damage,
    has_extra_energy,
    lock_defender_attacks,
    recoil_attack,
    self_energy_discard_attack,
    snipe_attack,
)
from spirit.game.card_effects.passives_common import (
    apply_protection,
    hp_bonus_tool,
    is_in_active_spot,
    prevent_damage_when,
    takes_less_passive,
    trainer_effect_shield_passive,
)
from spirit.game.card_effects.pokemon import energy_provides_type, is_lightning_energy
from spirit.game.card_effects.sm3 import (
    is_darkness_energy, is_fire_energy, is_gx_or_ex, is_psychic_energy,
    is_tool_card, is_water_energy, _return_to_hand,
)
from spirit.game.card_effects.sm4 import MemoryTypePassive
from spirit.game.card_effects.sm5 import go_second_first_turn, is_fairy_pokemon
from spirit.game.card_effects.sl import is_benched
from spirit.game.card_effects.sm8 import StadiumLockPassive
from spirit.game.card_effects.support_common import (
    distribute_energy,
    gust_attack,
    look_at_top,
    look_top_attach_energy,
    search_attach_energy,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    deck_nonempty, is_basic_energy_card, is_energy_card, opponent_has_bench,
)


_MAGIC_ODDS = {10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250}
_POISONED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
_CONFUSED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED]


# ----------------------------------------------------------------------
# Predicates
# ----------------------------------------------------------------------

def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    return getattr(def_for(getattr(card, "archetype_id", None)), "display_name", "") or ""


def _typed(card, pokemon_type: PokemonTypes) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and pokemon_type.value in types


def is_water_pokemon(card) -> bool:
    return _typed(card, PokemonTypes.WATER)


def is_metal_pokemon(card) -> bool:
    return _typed(card, PokemonTypes.METAL)


def is_psychic_pokemon(card) -> bool:
    return _typed(card, PokemonTypes.PSYCHIC)


def is_darkness_pokemon(card) -> bool:
    return _typed(card, PokemonTypes.DARKNESS)


def is_active_pokemon(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_in_active_spot(pokemon)


def is_benched_pokemon(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_benched(pokemon)


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _prize_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _stadium(board):
    area = board.find_global_area("activeStadium")
    return next(iter(area.children), None) if area and area.children else None


def _has_named_energy(pokemon, name: str) -> bool:
    return any(_display_name(child) == name for child in pokemon.children)


def _provides_metal(card) -> bool:
    return energy_provides_type(card, PokemonTypes.METAL.value)


def _has_metal_energy(pokemon) -> bool:
    return any(_provides_metal(child) for child in pokemon.children)


def is_exeggcute(card) -> bool:
    return _logic_name(card) == "Exeggcute" or _display_name(card) == "Exeggcute"


def is_electropower(card) -> bool:
    return _display_name(card) == "Electropower"


def is_judge_card(card) -> bool:
    return _display_name(card) == "Judge"


def is_silvally_gx(pokemon) -> bool:
    return _logic_name(pokemon) == "SilvallyGX"


has_nuzzle = has_attack_titled("Nuzzle")


def _is_tauros(pokemon) -> bool:
    name = _logic_name(pokemon)
    return name in ("Tauros", "TaurosGX") or (_display_name(pokemon) or "").startswith("Tauros")


def _not_gx_or_ex(card) -> bool:
    return is_pokemon_card(card) and not is_gx_or_ex(card)


def _water_or_psychic_energy(card) -> bool:
    return is_water_energy(card) or is_psychic_energy(card)


def _any_card(_card) -> bool:
    return True


def _is_damaged(board, pokemon) -> bool:
    return pokemon is not None and pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _hand_except(board, player_id, exclude=None) -> list:
    hand = board.find_player_area(player_id, "hand")
    cards = list(hand.children) if hand else []
    return [c for c in cards if c is not exclude]


def _opp_active(board, player_id):
    opp = _other_player(board, player_id)
    return board.active_pokemon(opp) if opp else None


def _tool_count(ctx) -> int:
    total = 0
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        total += sum(1 for child in pokemon.children if is_tool_card(child))
    return total


def _basic_energy_on_mine(ctx) -> int:
    total = 0
    for pokemon in ctx.my_pokemon_in_play():
        total += sum(1 for energy in ctx.attached_energies(pokemon)
                     if is_basic_energy_card(energy))
    return total


def _tauros_counters(ctx) -> int:
    total = 0
    for pokemon in ctx.my_pokemon_in_play():
        if _is_tauros(pokemon):
            missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
            total += max(0, missing // 10)
    return total


def _nidoqueen_benched(ctx) -> bool:
    return any(_logic_name(p) == "Nidoqueen" for p in ctx.my_bench())


def _no_gx_ex_on_bench(ctx) -> bool:
    return not any(is_gx_or_ex(p) for p in ctx.my_bench())


def _stadium_in_play_ctx(ctx) -> bool:
    return ctx.stadium_in_play() is not None


def _defender_is_evolution(ctx) -> bool:
    d = ctx.defender
    return d is not None and is_evolution_pokemon(d)


def _defender_is_gx_or_ex(ctx) -> bool:
    d = ctx.defender
    return d is not None and is_gx_or_ex(d)


def _undamaged_self(ctx) -> bool:
    return not has_damage("self")(ctx)


def _exactly_one_prize(ctx) -> bool:
    return count_prizes_remaining("theirs")(ctx) == 1


def _became_active_this_turn(ctx) -> bool:
    attacker = ctx.attacker
    return attacker is not None and ctx.entered_active_this_turn(attacker)


def _evolved_from_blitzle(ctx) -> bool:
    attacker = ctx.attacker
    if attacker is None:
        return False
    state = ctx.session.turn_state
    if state.entered_play_turn.get(attacker.entity_id) != state.turn_number:
        return False
    return any(_logic_name(c) == "Blitzle" for c in attacker.children)


def _retreat_cost_exactly_4(pokemon) -> bool:
    return (pokemon.get_attribute(AttrID.RETREAT_COST) or 0) == 4


def _opp_has_water_energy(ctx) -> bool:
    return any(
        any(is_water_energy(e) for e in ctx.attached_energies(p))
        for p in ctx.opponent_pokemon_in_play()
    )


# ----------------------------------------------------------------------
# Passives
# ----------------------------------------------------------------------

class DarkAmbitionPassive(Passive):
    """Opponent's Active Basic has +1 Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        if me is None or pokemon.owning_player_id == me.owning_player_id:
            return cost
        if not is_in_active_spot(pokemon) or not is_basic_pokemon(pokemon):
            return cost
        return cost + 1


class MagicOddsPassive(Passive):
    """Prevent opposing attack damage of exactly 10, 30, ... 250."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return calc.amount in _MAGIC_ODDS


class ScoopUpBlockPassive(Passive):
    """Opponent's damaged Pokémon (and attachments) can't go to hand."""

    def blocks_return_to_hand(self, card, carrier, board=None):
        me = carrier_pokemon(carrier)
        if me is None:
            return False
        pokemon = carrier_pokemon(card)
        if pokemon is None or pokemon.owning_player_id == me.owning_player_id:
            return False
        if board is None:
            return False
        return _is_damaged(board, pokemon)


class PoisonSacsPassive(Passive):
    """Opponent's Poisoned condition is not removed on evolve/devolve."""

    def keeps_condition_on_evolve(self, pokemon, condition, carrier):
        me = carrier_pokemon(carrier)
        if me is None or pokemon.owning_player_id == me.owning_player_id:
            return False
        return condition == _POISONED


class MetalSymbolPassive(Passive):
    """Owner's Metal-Energy Pokémon can't gain Special Conditions."""

    def blocks_special_conditions(self, target, condition, carrier):
        me = carrier_pokemon(carrier)
        if me is None or target is None:
            return False
        if target.owning_player_id != me.owning_player_id:
            return False
        return _has_metal_energy(target)


class KeyOfSecretsPassive(Passive):
    """Your Metal Pokémon's Resistance is -40."""

    def modify_resistance(self, calc, carrier):
        target = calc.target
        me = carrier_pokemon(carrier)
        if target is None or me is None or not calc.resistance_applies:
            return
        if target.owning_player_id != me.owning_player_id:
            return
        if PokemonTypes.METAL.value not in (target.get_attribute(AttrID.POKEMON_TYPES) or []):
            return
        calc.resistance_amount = 40


class FossilBindPassive(Passive):
    """If you have fewer Pokémon in play, the opponent can't play Items."""

    def blocks_trainer_play(self, card, player_id, carrier, board=None):
        me = carrier_pokemon(carrier)
        if me is None or board is None:
            return False
        if player_id == me.owning_player_id:
            return False
        if card.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.ITEM.value:
            return False
        opp = _other_player(board, me.owning_player_id)
        if opp is None:
            return False
        return len(board.pokemon_in_play(me.owning_player_id)) < len(board.pokemon_in_play(opp))


class FossilizedMemoriesPassive(Passive):
    """While Active, the opponent can't play Supporters."""

    def blocks_trainer_play(self, card, player_id, carrier, board=None):
        me = carrier_pokemon(carrier)
        if me is None or not is_in_active_spot(me):
            return False
        if player_id == me.owning_player_id:
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value


class FloatingShellPassive(Passive):
    """No Retreat Cost while you have a Stadium in play."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        stadium = _stadium(board)
        if stadium is not None and stadium.owning_player_id == pokemon.owning_player_id:
            return 0
        return cost


class GrassCushionPassive(Passive):
    """Takes 30 less from attacks if any Grass Energy is attached."""

    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or me is not calc.target:
            return
        if not (calc.is_attack and calc.is_opposing):
            return
        if not any(energy_provides_type(c, PokemonTypes.GRASS.value) for c in me.children):
            return
        calc.amount = max(0, calc.amount - 30)


class IronRulePassive(Passive):
    """`locked_player`'s Pokémon can't attack."""

    def __init__(self, locked_player: str):
        self.locked_player = locked_player

    def blocks_attacks(self, pokemon, carrier):
        return pokemon.owning_player_id == self.locked_player


class FairyCharmUbPassive(Passive):
    """Prevent damage from opposing Ultra Beast GX/EX to a Fairy holder."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.target:
            return False
        if not (calc.is_attack and calc.is_opposing):
            return False
        if not is_fairy_pokemon(holder):
            return False
        attacker = calc.attacker
        if attacker is None or not is_gx_or_ex(attacker):
            return False
        return is_ultra_beast(attacker.archetype_id)


class MetalGogglesPassive(Passive):
    """Holder takes 30 less from attacks; Metal holders also block opposing counters."""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.target:
            return
        if not (calc.is_attack and calc.is_opposing):
            return
        calc.amount = max(0, calc.amount - 30)

    def prevents_damage_counters(self, target, carrier, source_player_id=None):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not target or not is_metal_pokemon(holder):
            return False
        if source_player_id is None:
            return True
        return source_player_id != holder.owning_player_id


class WondrousLabyrinthPassive(StadiumLockPassive):
    """Non-Fairy Pokémon attacks cost [C] more; Prism Star stadium lock."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        types = effective_pokemon_types(board, pokemon)
        if PokemonTypes.FAIRY.value in types:
            return cost
        key = CLIENT_POKEMON_TYPE_NAMES[PokemonTypes.COLORLESS]
        cost = dict(cost)
        cost[key] = cost.get(key, 0) + 1
        return cost


class BlackMarketPassive(StadiumLockPassive):
    """Darkness Pokémon with Darkness Energy take 1 fewer Prize when KO'd
    by opposing attack damage; Prism Star stadium lock."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if not is_darkness_pokemon(pokemon):
            return count
        if not any(is_darkness_energy(child) for child in pokemon.children):
            return count
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return count
        if not ctx.is_attack_effect():
            return count
        if getattr(pokemon, "entity_id", None) not in getattr(ctx, "attack_damage", {}):
            return count
        return max(0, count - 1)


dark_ambition_passive = DarkAmbitionPassive()
royal_guard_passive = takes_less_passive(40)
magic_odds_passive = MagicOddsPassive()
scoop_up_block_passive = ScoopUpBlockPassive()
poison_sacs_passive = PoisonSacsPassive()
metal_symbol_passive = MetalSymbolPassive()
key_of_secrets_passive = KeyOfSecretsPassive()
fossil_bind_passive = FossilBindPassive()
fossilized_memories_passive = FossilizedMemoriesPassive()
floating_shell_passive = FloatingShellPassive()
grass_cushion_passive = GrassCushionPassive()
blizzard_veil_passive = trainer_effect_shield_passive(
    supporters_only=True,
    while_active=True,
    protects=lambda entity, carrier: (
        entity is not None
        and entity.owning_player_id == carrier.owning_player_id
        and is_water_pokemon(entity)
        and is_benched(entity)
    ),
)
fairy_charm_ub_passive = FairyCharmUbPassive()
metal_goggles_passive = MetalGogglesPassive()
buff_padding_passive = hp_bonus_tool(50, holder_pred=_retreat_cost_exactly_4)
grass_memory_passive = MemoryTypePassive(PokemonTypes.GRASS)
water_memory_passive = MemoryTypePassive(PokemonTypes.WATER)
wondrous_labyrinth_passive = WondrousLabyrinthPassive()
black_market_passive = BlackMarketPassive()
stadium_lock_passive = StadiumLockPassive()


# ----------------------------------------------------------------------
# Attack helpers
# ----------------------------------------------------------------------

self_destruct = recoil_attack(60)
shock_bolt = self_energy_discard_attack(
    all_energy=True, energy_type=PokemonTypes.LIGHTNING)
impact_bolt = shock_bolt
electrical_gx = search_to_hand(
    is_pokemon_card, count=7, reveal=True,
    prompt="Choose up to 7 Pokémon.",
)
delivery_dash = search_to_hand(
    is_electropower, count=2, reveal=True,
    prompt="Choose up to 2 Electropower cards.",
)
single_lunge = bonus_if(_undamaged_self, 90)
fossil_fangs = bonus_if(_no_gx_ex_on_bench, 90)
dueling_saber = bonus_if(_stadium_in_play_ctx, 60)
dump_truck_press = bonus_if(_defender_is_evolution, 120)
egg_splat = discard_for_bonus(
    source="hand", predicate=is_exeggcute, max_count=99, per=60, base=0,
    prompt="Discard any number of Exeggcute",
)


async def continuous_blaze_ball(ctx):
    fires = [e for e in ctx.attached_energies(ctx.attacker) if is_fire_energy(e)]
    await ctx.discard_cards(fires)
    await ctx.deal_damage(_printed(ctx) + 50 * len(fires))


tool_drop = damage_per(_tool_count, 30)
hydro_pump = damage_per(count_energy("self", PokemonTypes.WATER), 30, base=10)
splintered_shards_gx = damage_per(count_discard("theirs", is_energy_card), 30)
darkest_tornado_gx = damage_per(damage_counters_on("self"), 50, base=10)
flower_storm = damage_per(_basic_energy_on_mine, 30)
raging_herd = damage_per(_tauros_counters, 10, base=10)
night_punishment = damage_per(count_discard("mine", is_pokemon_card), 20, cap=200)
power_lariat = damage_per(count_bench("mine", is_evolution_pokemon), 50, base=10)
kings_drum = bonus_if(_nidoqueen_benched, 100)
payback = bonus_if(_exactly_one_prize, 90)
calm_strike = bonus_if(gx_used, 70)
bite_off = bonus_if(_defender_is_gx_or_ex, 100)
raid = bonus_if(_evolved_from_blitzle, 90)
howl_in_the_dark = search_to_hand(
    is_darkness_pokemon, count=2, reveal=True,
    prompt="Choose up to 2 Darkness Pokémon.",
)
fast_evolution = search_to_hand(
    is_evolution_pokemon, count=2, reveal=True,
    prompt="Choose up to 2 Evolution Pokémon.",
)
special_combo = snipe_attack(90)
rock_slide = snipe_attack(20, count=2, also_base=True)
drag_off = gust_attack(damage_to_new_active=50)
arm_thrust = flip_or_nothing(then=discard_opponent_energy_attack(count=1, after_damage=True))
toxic_secretion = condition_attack(SpecialConditions.POISONED, counters=2)


async def _also_discard_stadium(ctx):
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


wreck = bonus_if(_stadium_in_play_ctx, 80, also=_also_discard_stadium)


async def paradise_draw(ctx):
    hand = list(ctx.hand())
    if hand and await ctx.ask_yes_no("Discard any number of cards from your hand?"):
        picks = await ctx.choose_cards(
            hand, len(hand), minimum=0, prompt="Choose cards to discard")
        await ctx.discard_cards(picks)
    await ctx.draw_until(6)


async def electromagnetic_bomb(ctx):
    moved = await ctx.move_energy_freely(
        ctx.my_bench(), [ctx.attacker] if ctx.attacker is not None else [],
        predicate=is_lightning_energy,
        prompt="Choose Lightning Energy to move to this Pokémon",
    )
    amount = 20 * len(moved)
    if amount:
        await ctx.deal_damage(amount)


async def power_recharge(ctx):
    await ctx.deal_damage()
    cards = [c for c in ctx.discard_pile() if is_electropower(c)]
    if cards:
        await ctx.put_in_hand(cards, reveal=False)


async def cold_cyclone(ctx):
    await ctx.deal_damage()
    attacker = ctx.attacker
    bench = ctx.my_bench()
    if attacker is None or not bench:
        return
    waters = [e for e in ctx.attached_energies(attacker) if is_water_energy(e)]
    take = waters[:2]
    if not take:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move Water Energy to")
    if target is None:
        return
    for energy in take:
        await ctx.move_energy(energy, target)


async def destiny_stinger(ctx):
    await ctx.knock_out(ctx.attacker)
    await ctx.knock_out(ctx.defender)


def destiny_stinger_condition(board, player_id, pokemon=None) -> bool:
    return _is_damaged(board, pokemon)


async def evergreen_gx(ctx):
    extra = has_extra_energy(1, PokemonTypes.GRASS)(ctx)
    attacker = ctx.attacker
    if attacker is not None:
        await ctx.heal(ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0),
                       attacker)
        await ctx.deal_damage()
    if extra:
        pile = list(ctx.discard_pile())
        if pile:
            await ctx.shuffle_into_deck(pile, ctx.player_id)


async def iron_rule_gx(ctx):
    ctx.add_global_passive(
        IronRulePassive(ctx.opponent_id),
        ctx.session.turn_state.turn_number + 1,
    )


async def cheer_up(ctx):
    cards = [c for c in ctx.hand() if is_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose an Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def megaton_friends_gx(ctx):
    extra = has_extra_energy(1)(ctx)
    await ctx.deal_damage()
    if extra:
        await ctx.draw_until(10)


async def tool_buster(ctx):
    defender = ctx.defender
    discarded = []
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [c for c in list(defender.children) if is_tool_card(c)]
        if tools:
            await ctx.discard_cards(tools)
            discarded = tools
    await ctx.deal_damage(_printed(ctx) + (70 if discarded else 0))


async def thorn_pod_throw(ctx):
    await ctx.deal_damage()
    n = count_energy("self", PokemonTypes.METAL)(ctx)
    amount = min(100, 20 * n)
    bench = ctx.opponent_bench()
    if amount and bench:
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to take damage")
        if target is not None:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)


async def horror_house_gx(ctx):
    extra = has_extra_energy(1, PokemonTypes.PSYCHIC)(ctx)
    ctx.lock_plays(ctx.opponent_id, _any_card)
    if extra:
        await ctx.draw_until(7)
        await ctx.draw_until(7, ctx.opponent_id)


async def swim(ctx):
    bench = ctx.opponent_bench()
    if _opp_has_water_energy(ctx) and bench and await ctx.ask_yes_no(
            "Do 90 damage to a Benched Pokémon instead?"):
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(90, target=target, apply_modifiers=False)
            return
    await ctx.deal_damage()


async def distilled_blast(ctx):
    top = ctx.deck_top(7)
    if top:
        await ctx.reveal_cards(top)
    waters = [c for c in top if is_water_energy(c)]
    await ctx.deal_damage(_printed(ctx) + 30 * len(waters))
    others = [c for c in top if c not in waters]
    if others:
        await ctx.discard_cards(others)
    await ctx.shuffle_deck()


def special_combo_condition(board, player_id, pokemon=None) -> bool:
    state = getattr(board, "turn_state", None)
    if state is None:
        return False
    titles = state.attack_titles_prev_turn_by_player.get(player_id) or []
    return "Hit and Run" in titles and opponent_has_bench(board, player_id)


async def devilish_hands_gx(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if is_gx_or_ex(p)]
    if not pool:
        return
    for _ in range(6):
        target = await ctx.choose_pokemon(
            pool, "Choose a Pokémon-GX or Pokémon-EX")
        if target is None:
            break
        await ctx.deal_damage(30, target=target, apply_modifiers=False)


async def mysterious_dance(ctx):
    n = len(ctx.opponent_bench())
    if n:
        await ctx.place_damage_counters(n, ctx.opponent_pokemon_in_play())


async def aero_unit_gx(ctx):
    extra = has_extra_energy(1)(ctx)
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks = await ctx.choose_cards(
        cards, 5, minimum=0,
        prompt="Choose up to 5 basic Energy cards to attach") if cards else []
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
    if extra:
        await apply_protection(ctx, prevent=True, effects_too=True)


async def towering_splash_gx(ctx):
    extra = has_extra_energy(7, PokemonTypes.WATER)(ctx)
    await ctx.deal_damage()
    if extra:
        for pokemon in ctx.opponent_bench():
            await ctx.deal_damage(100, target=pokemon, apply_modifiers=False)


async def enter_the_dragon(ctx):
    results = await ctx.flip_coins(1, "Enter the Dragon")
    if not (results and results[0]) or ctx.attacker is None:
        return
    name = _logic_name(ctx.attacker)
    candidates = [
        c for c in ctx.discard_pile()
        if is_pokemon_card(c) and evolves_from(c.archetype_id, name)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Choose a card that evolves from this Pokémon")
    if picks:
        await ctx.evolve_pokemon(ctx.attacker, picks[0])


async def trash_crash(ctx):
    items = [c for c in ctx.hand() if is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(items, 1, prompt="Discard an Item card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Pokémon to take 60 damage")
    if target is not None:
        await ctx.deal_damage(60, target=target, apply_modifiers=False)


async def top_burner(ctx):
    fires = [e for e in ctx.attached_energies(ctx.attacker) if is_fire_energy(e)]
    await ctx.discard_cards(fires)
    if fires:
        await ctx.discard_cards(ctx.deck_top(len(fires), player_id=ctx.opponent_id))


async def family_rescue(ctx):
    candidates = [c for c in ctx.discard_pile() if is_psychic_pokemon(c)]
    picks = await ctx.choose_cards(
        candidates, 5, minimum=0,
        prompt="Choose up to 5 Psychic Pokémon to shuffle into your deck") if candidates else []
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


async def tighten_up(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, 2)


async def make_em_pay(ctx):
    await ctx.deal_damage()
    if ctx.hand_size(ctx.opponent_id) < 4:
        return
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    extra = len(cards) - 4
    if extra <= 0:
        return
    picks = await ctx.choose_cards(
        cards, extra, minimum=extra,
        prompt="Discard cards until your opponent has 4 cards in hand")
    if picks:
        await ctx.discard_cards(picks)


async def spin_storm(ctx):
    target = ctx.opponent_active()
    if target is not None:
        await _return_to_hand(ctx, target)


full_blitz = search_attach_energy(
    is_lightning_energy, count=3, distribute=False,
    prompt="Choose up to 3 Lightning Energy cards",
)


async def tag_bolt_gx(ctx):
    extra = has_extra_energy(3, PokemonTypes.LIGHTNING)(ctx)
    await ctx.deal_damage()
    if extra:
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon to take 170 damage")
            if target is not None:
                await ctx.deal_damage(170, target=target, apply_modifiers=False)


async def headache(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Headache")
    if results and results[0]:
        ctx.lock_plays(ctx.opponent_id, is_trainer_card)


async def spirit_compressor(ctx):
    picks = await ctx.search_deck(
        is_pokemon_card, count=4, minimum=0,
        prompt="Choose up to 4 Pokémon to discard",
    )
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


strange_wave = search_attach_energy(
    _water_or_psychic_energy, count=3, distribute=False,
    target_pred=is_benched,
    prompt="Choose up to 3 Water or Psychic Energy cards",
)


async def paranormal(ctx):
    await ctx.deal_damage()
    shield = prevent_damage_when(
        lambda calc, carrier: (
            calc.attacker is not None
            and is_ultra_beast(calc.attacker.archetype_id)
            and carrier_pokemon(carrier) is calc.target
        )
    )
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(ctx.attacker, shield)


async def tail_whip(ctx):
    results = await ctx.flip_coins(1, "Tail Whip")
    if results and results[0]:
        lock_defender_attacks(ctx)


async def head_hunt(ctx):
    top = ctx.deck_top(6)
    if not top:
        return
    pokemon = [c for c in top if is_pokemon_card(c)]
    picks = await ctx.choose_cards(
        pokemon, len(pokemon), minimum=0,
        prompt="Choose Pokémon to put into your hand",
        display_cards=top if len(pokemon) < len(top) else None,
    ) if pokemon else []
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.discard_cards(rest)


async def thunderous_assault(ctx):
    amount = _printed(ctx) + (70 if _became_active_this_turn(ctx) else 0)
    await ctx.deal_damage(amount, ignore_weakness=True)


# ----------------------------------------------------------------------
# Ability effects
# ----------------------------------------------------------------------

async def adventurous_appetite(ctx):
    if not await ctx.ask_yes_no(
            "Look at the top 6 cards of your opponent's deck?"):
        return
    top = ctx.deck_top(6, player_id=ctx.opponent_id)
    if not top:
        return
    items = [c for c in top if is_item_card(c)]
    picks = await ctx.choose_cards(
        items, len(items), minimum=0,
        prompt="Discard any number of Item cards",
        display_cards=top if len(items) < len(top) else None,
    ) if items else []
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck(ctx.opponent_id)


async def powerful_squall(ctx):
    await look_top_attach_energy(6, predicate=is_water_energy)(ctx)


async def roaring_resolve(ctx):
    source = ctx.source
    if source is None:
        return
    await ctx.deal_damage(20, target=source, as_counters=True)
    await search_attach_energy(
        is_fire_energy, count=2, to_self=True,
        prompt="Choose up to 2 Fire Energy cards",
    )(ctx)


async def metal_symbol_cure(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if _has_metal_energy(pokemon) and pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
            await ctx.cure_all_conditions(pokemon)


async def fast_call(ctx):
    await search_to_hand(
        is_supporter_card, count=1, reveal=True,
        prompt="Choose a Supporter card.",
    )(ctx)


async def electro_shaker(ctx):
    if not await ctx.ask_yes_no("Move Lightning Energy among your Pokémon?"):
        return
    mine = ctx.my_pokemon_in_play()
    if len(mine) >= 2:
        await ctx.move_energy_freely(mine, mine, predicate=is_lightning_energy)


async def nuzzly_gathering(ctx):
    await search_to_hand(
        has_nuzzle, count=1, reveal=True,
        prompt="Choose a Pokémon that has the Nuzzle attack.",
    )(ctx)


async def scar_charge(ctx):
    source = ctx.source
    if source is None:
        return
    await ctx.deal_damage(30, target=source, as_counters=True)
    await search_attach_energy(
        is_darkness_energy, count=3, to_self=True,
        prompt="Choose up to 3 Darkness Energy cards",
    )(ctx)


async def stellar_wish(ctx):
    await look_at_top(
        5, take=1, predicate=is_trainer_card, rest="shuffle", minimum=0,
        prompt="Choose a Trainer card to put into your hand.",
    )(ctx)
    if ctx.source is not None:
        await ctx.apply_special_condition(ctx.source, SpecialConditions.ASLEEP)


async def twilight_eyes(ctx):
    if not await ctx.ask_yes_no(
            "Discard an Energy from your opponent's Active Pokémon?"):
        return
    target = ctx.opponent_active()
    if target is None:
        return
    await ctx.discard_energy_from(
        target, 1, prompt="Choose an Energy to discard")


async def queens_call(ctx):
    await search_to_hand(
        _not_gx_or_ex, count=1, reveal=True,
        prompt="Choose a Pokémon that isn't a Pokémon-GX or Pokémon-EX.",
    )(ctx)


async def nine_temptations(ctx):
    fires = [c for c in ctx.hand() if is_fire_energy(c)]
    if len(fires) < 2:
        return
    picks = await ctx.choose_cards(
        fires, 2, prompt="Discard 2 Fire Energy cards from your hand")
    if len(picks) < 2:
        return
    await ctx.discard_cards(picks)
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


def nine_temptations_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    fires = [c for c in (hand.children if hand else []) if is_fire_energy(c)]
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    bench = board.find_player_area(opp, "bench")
    return len(fires) >= 2 and bool(bench and bench.children)


async def panic_spores(ctx):
    targets = [
        p for p in ctx.opponent_pokemon_in_play()
        if _CONFUSED in (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    ]
    for target in targets:
        await ctx.deal_damage(20, target=target, as_counters=True)


async def air_mail(ctx):
    await look_at_top(2, take=1, rest="bottom", minimum=1)(ctx)


def dance_of_the_ancients_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None or not is_benched(pokemon):
        return False
    bench = board.find_player_area(player_id, "bench")
    if bench is None or len(bench.children) < 2:
        return False
    discard = board.find_player_area(player_id, "discard")
    n = sum(1 for c in (discard.children if discard else []) if is_lightning_energy(c))
    return n >= 2


async def dance_of_the_ancients(ctx):
    source = ctx.source
    bench = [p for p in ctx.my_bench()]
    if source is None or len(bench) < 2:
        return
    picks = await ctx.choose_cards(
        bench, 2, minimum=2, prompt="Choose 2 of your Benched Pokémon")
    if len(picks) < 2:
        return
    energies = [c for c in ctx.discard_pile() if is_lightning_energy(c)]
    if len(energies) < 2:
        return
    chosen_energy = await ctx.choose_cards(
        energies, 2, minimum=2,
        prompt="Choose 2 Lightning Energy cards to attach")
    if len(chosen_energy) < 2:
        return
    for energy, target in zip(chosen_energy, picks):
        await ctx.attach_energy(energy, target)
    stack = full_stack(source)
    await ctx.discard_cards([c for c in stack if c is not source])
    await ctx.move_to_lost_zone([source])


# ----------------------------------------------------------------------
# Trainers
# ----------------------------------------------------------------------

bills_analysis = look_at_top(
    7, take=2, predicate=is_trainer_card, rest="shuffle", minimum=0,
    prompt="Choose up to 2 Trainer cards.",
)


async def brocks_grit(ctx):
    candidates = [
        c for c in ctx.discard_pile()
        if is_pokemon_card(c) or is_basic_energy_card(c)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 6, minimum=0,
        prompt="Choose up to 6 Pokémon and basic Energy cards")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


def brocks_grit_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return any(
        is_pokemon_card(c) or is_basic_energy_card(c)
        for c in (discard.children if discard else [])
    )


def dana_condition(board, player_id, pokemon=None) -> bool:
    active = _opp_active(board, player_id)
    return active is not None and is_stage2_pokemon(active) and deck_nonempty(board, player_id)


async def dana(ctx):
    await search_to_hand(count=2, reveal=False, prompt="Choose up to 2 cards.")(ctx)


def evelyn_condition(board, player_id, pokemon=None) -> bool:
    active = _opp_active(board, player_id)
    return active is not None and is_stage1_pokemon(active)


async def evelyn(ctx):
    await ctx.draw_cards(4)


def nita_condition(board, player_id, pokemon=None) -> bool:
    active = _opp_active(board, player_id)
    if active is None or not is_basic_pokemon(active):
        return False
    return any(is_energy_card(c) for c in active.children)


async def nita(ctx):
    target = ctx.opponent_active()
    if target is None:
        return
    energies = list(ctx.attached_energies(target))
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Put an Energy on top of your opponent's deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


def erikas_hospitality_condition(board, player_id, pokemon=None) -> bool:
    return len(_hand_except(board, player_id, pokemon)) <= 4


async def erikas_hospitality(ctx):
    n = len(ctx.opponent_pokemon_in_play())
    if n:
        await ctx.draw_cards(n)


def dangerous_drill_condition(board, player_id, pokemon=None) -> bool:
    others = _hand_except(board, player_id, pokemon)
    if not any(is_darkness_pokemon(c) for c in others):
        return False
    opp = _other_player(board, player_id)
    if _stadium(board) is not None:
        return True
    if opp is None:
        return False
    for poke in board.pokemon_in_play(opp):
        for child in poke.children:
            if is_tool_card(child) or is_special_energy(child):
                return True
    return False


async def dangerous_drill(ctx):
    darkness = [c for c in ctx.hand() if is_darkness_pokemon(c)]
    cost = await ctx.choose_cards(
        darkness, 1, prompt="Discard a Darkness Pokémon from your hand")
    if not cost:
        return
    await ctx.discard_cards(cost)
    stadium = ctx.stadium_in_play()
    attached = []
    for pokemon in ctx.opponent_pokemon_in_play():
        for child in pokemon.children:
            if is_tool_card(child) or is_special_energy(child):
                attached.append(child)
    candidates = attached + ([stadium] if stadium is not None else [])
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Discard a Pokémon Tool, Special Energy, or Stadium")
    if picks:
        await ctx.discard_cards(picks)


def electrocharger_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return any(is_electropower(c) for c in (discard.children if discard else []))


async def electrocharger(ctx):
    results = await ctx.flip_coins(2, "Electrocharger")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    cards = [c for c in ctx.discard_pile() if is_electropower(c)]
    take = min(heads, len(cards))
    if take:
        picks = await ctx.choose_cards(
            cards, take, minimum=take,
            prompt="Shuffle Electropower into your deck")
        if picks:
            await ctx.shuffle_into_deck(picks, ctx.player_id)


async def ingo_emmet(ctx):
    top = ctx.deck_top(1)
    if top:
        await ctx.reveal_cards(top, to_player=ctx.player_id)
    choice = await ctx.choose(
        "Choose 1:",
        ["Discard your hand and draw 5 cards",
         "Discard your hand and draw 5 cards from the bottom of your deck"],
    )
    await ctx.discard_cards(list(ctx.hand()))
    if choice == 1:
        deck = ctx.board.find_player_area(ctx.player_id, "deck")
        cards = list(deck.children[:5]) if deck else []
        if cards:
            await ctx.put_in_hand(cards, reveal=False)
    else:
        await ctx.draw_cards(5)


def jasmine_count(board, player_id) -> int:
    return 5 if go_second_first_turn(board, player_id) else 1


async def jasmine(ctx):
    n = jasmine_count(ctx.board, ctx.player_id)
    await search_to_hand(
        is_metal_pokemon, count=n, reveal=True,
        prompt="Choose Metal Pokémon.",
    )(ctx)


def judge_whistle_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    has_judge = any(is_judge_card(c) for c in (discard.children if discard else []))
    return True if deck_nonempty(board, player_id) or has_judge else False


async def judge_whistle(ctx):
    options = ["Draw a card"]
    judges = [c for c in ctx.discard_pile() if is_judge_card(c)]
    if judges:
        options.append("Put a Judge card from your discard pile into your hand")
    choice = 0 if len(options) == 1 else await ctx.choose("Choose 1:", options)
    if choice == 0:
        await ctx.draw_cards(1)
    elif judges:
        picks = await ctx.choose_cards(
            judges, 1, prompt="Choose a Judge card")
        if picks:
            await ctx.put_in_hand(picks)


def morgan_condition(board, player_id, pokemon=None) -> bool:
    names = {_display_name(c) for c in _hand_except(board, player_id, pokemon)}
    return {"Dana", "Evelyn", "Nita"}.issubset(names)


async def morgan(ctx):
    for name in ("Dana", "Evelyn", "Nita"):
        matches = [c for c in ctx.hand() if _display_name(c) == name]
        if not matches:
            return
        await ctx.discard_cards([matches[0]])
    await look_top_attach_energy(12, predicate=is_energy_card)(ctx)


def nanu_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    has_basic_dark = any(
        is_basic_pokemon(c) and is_darkness_pokemon(c)
        for c in (discard.children if discard else [])
    )
    return has_basic_dark and bool(board.pokemon_in_play(player_id))


async def nanu(ctx):
    candidates = [
        c for c in ctx.discard_pile()
        if is_basic_pokemon(c) and is_darkness_pokemon(c)
    ]
    in_play = ctx.my_pokemon_in_play()
    if not candidates or not in_play:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Choose a Basic Darkness Pokémon from your discard pile")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        in_play, "Choose 1 of your Pokémon in play to switch it with")
    if target is not None:
        await ctx.identity_swap(target, picks[0], destination="discard")


def pokemon_communication_condition(board, player_id, pokemon=None) -> bool:
    others = _hand_except(board, player_id, pokemon)
    return any(is_pokemon_card(c) for c in others) and deck_nonempty(board, player_id)


async def pokemon_communication(ctx):
    candidates = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Reveal a Pokémon from your hand")
    if not picks:
        return
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks, ctx.player_id)
    await search_to_hand(
        is_pokemon_card, count=1, reveal=True,
        prompt="Choose a Pokémon.",
    )(ctx)


def return_label_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    discard = board.find_player_area(opp, "discard")
    return bool(discard and discard.children)


async def return_label(ctx):
    pile = list(ctx.discard_pile(ctx.opponent_id))
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, prompt="Put a card on the bottom of your opponent's deck")
    if picks:
        await ctx.put_on_bottom_of_deck(picks[0])


async def sabrinas_suggestion(ctx):
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    candidates = [c for c in cards if is_supporter_card(c)]
    if not candidates:
        return
    if not await ctx.ask_yes_no("Use the effect of a Supporter card you find there?"):
        return
    picked = await ctx.choose_cards(
        candidates, 1, minimum=0, prompt="Choose a Supporter card")
    if not picked:
        return
    effect = TRAINER_EFFECTS_BY_GUID.get((picked[0].archetype_id or "").lower())
    if effect is not None and effect is not unimplemented:
        await effect(ctx)


def viridian_forest_condition(board, player_id, stadium=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and hand.children) and deck_nonempty(board, player_id)


async def viridian_forest(ctx):
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(hand, 1, prompt="Discard a card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await search_to_hand(
        is_basic_energy_card, count=1, reveal=True,
        prompt="Choose a basic Energy card.",
    )(ctx)


async def lavender_town(ctx):
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)


VIRIDIAN_FOREST_ABILITY = Ability(
    title="Viridian Forest",
    game_text="Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for a basic Energy card, reveals it, and puts it into their hand. Then, that player shuffles their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=viridian_forest,
    condition=viridian_forest_condition,
)

LAVENDER_TOWN_ABILITY = Ability(
    title="Lavender Town",
    game_text="Once during each player's turn, that player may have their opponent reveal their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=lavender_town,
)
