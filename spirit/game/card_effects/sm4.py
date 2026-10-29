"""Crimson Invasion (SM4) attack, ability, trainer, energy, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

import random

from spirit.game.attributes import (
    AbilityTypes, AttrID, GameSequence, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import def_for, evolves_from
from spirit.network.message_names import OutboundMsg
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_pokemon_card,
    is_special_energy,
    is_stage2_pokemon,
    is_supporter_card,
)
from spirit.game.session.passives import Passive, carrier_pokemon, effective_max_hp
from spirit.game.card_effects.attacks_common import (
    bonus_if,
    condition_attack,
    count_energy,
    count_prizes_remaining,
    damage_per,
    discard_for_bonus,
    flip_damage,
    recoil_attack,
    snipe_attack,
    smokescreen_attack,
    spread_damage,
)
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.passives_common import (
    TypedDamageBoostPassive,
    condition_immunity_passive,
    is_in_active_spot,
    prevent_damage_when,
    retreat_free_when,
    takes_less_passive,
    team_damage_boost_passive,
    boost_own_next_turn,
)
from spirit.game.card_effects.sm3 import (
    TakesMorePassive,
    is_darkness_energy,
    is_fire_energy,
    is_gx_or_ex,
    is_tool_card,
)
from spirit.game.card_effects.support_common import (
    distribute_energy,
    recover_from_discard,
    search_to_bench,
    switch_self_attack,
)
from spirit.game.card_effects.trainers import (
    bosss_orders,
    is_basic_energy_card,
    is_energy_card,
    is_dragon_pokemon,
    opponent_has_bench,
    opponent_play_targets,
)


_TOOL_STADIUM_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.STADIUM.value)
ALL_TYPES_TWO_AT_A_TIME = [opt + opt for opt in ALL_TYPES_ONE_AT_A_TIME]


def is_stadium_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


def is_lightning_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.LIGHTNING.value in types


def pokemon_has_ability(card) -> bool:
    """Hand/in-play Pokemon whose definition lists a Poke-Ability/Power/Body."""
    if not is_pokemon_card(card):
        return False
    for ability in getattr(def_for(card.archetype_id), "abilities", None) or []:
        ability_type = getattr(ability, "ability_type", None)
        if ability_type in (
            AbilityTypes.POKE_ABILITY, AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY,
        ):
            return True
    return False


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _logic_names_in_play(pokemon, bench_only=False) -> set:
    names = set()
    if pokemon is None or pokemon.parent is None or pokemon.parent.parent is None:
        return names
    player_area = pokemon.parent.parent
    wanted = ("bench",) if bench_only else ("activePokemonArea", "bench")
    for sub in player_area.children:
        if sub.get_attribute(AttrID.NAME) not in wanted:
            continue
        for child in sub.children:
            names.add(child.get_attribute(AttrID.EVOLUTION_LOGIC_NAME))
    return names


def _is_damaged(ctx, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _prize_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def more_prizes_remaining(board, player_id, pokemon=None) -> bool:
    opponent = _other_player(board, player_id)
    if opponent is None:
        return False
    return _prize_count(board, player_id) > _prize_count(board, opponent)


def has_prizes_remaining(board, player_id, pokemon=None) -> bool:
    return _prize_count(board, player_id) > 0


def counter_catcher_condition(board, player_id, pokemon=None) -> bool:
    return more_prizes_remaining(board, player_id) and opponent_has_bench(board, player_id)


def weed_out_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bench is not None and len(bench.children) > 3


def has_shelmet_in_hand(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(_logic_name(c) == "Shelmet" for c in (hand.children if hand else []))


def tlc_condition(board, player_id, pokemon=None) -> bool:
    opponent = _other_player(board, player_id)
    if opponent is None:
        return False
    bench = board.find_player_area(opponent, "bench")
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in (bench.children if bench else [])
    )


def lusamine_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return any(
        is_supporter_card(c) or is_stadium_card(c)
        for c in (discard.children if discard else [])
    )


def _all_cards_lock(_card) -> bool:
    return True


def _tool_special_energy_or_stadium(card) -> bool:
    if is_special_energy(card):
        return True
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_STADIUM_TYPES


def _has_darkness_energy_on(pokemon, ctx) -> bool:
    return any(is_darkness_energy(e) for e in ctx.attached_energies(pokemon))


def _self_has_darkness(ctx) -> bool:
    return ctx.attacker is not None and _has_darkness_energy_on(ctx.attacker, ctx)


def _opponent_has_darkness_energy(ctx) -> bool:
    return any(_has_darkness_energy_on(p, ctx) for p in ctx.opponent_pokemon_in_play())


def _fewer_in_play(ctx) -> bool:
    return len(ctx.my_pokemon_in_play()) < len(ctx.opponent_pokemon_in_play())


def _bench_damage_counters(ctx) -> int:
    return sum(
        max(0, (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10)
        for p in ctx.my_bench()
    )


def _evolved_from_this_turn(ctx, logic_name: str) -> bool:
    attacker = ctx.attacker
    if attacker is None:
        return False
    entered = ctx.session.turn_state.entered_play_turn.get(attacker.entity_id)
    if entered != ctx.session.turn_state.turn_number:
        return False
    return any(_logic_name(c) == logic_name for c in attacker.children)


async def _promote_self_if_needed(ctx, was_active: bool):
    if not was_active:
        return

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.opponent_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


# ======================================================================
# Passives
# ======================================================================

def _submerge_pred(calc, carrier):
    return calc.is_attack and calc.target is carrier and not calc.to_active


submerge_passive = prevent_damage_when(_submerge_pred, attacks_only=False)

fluffy_passive = takes_less_passive(
    30,
    attacker_pred=lambda attacker: PokemonTypes.FIRE.value not in (
        attacker.get_attribute(AttrID.POKEMON_TYPES) or []
    ),
)

own_tempo_passive = condition_immunity_passive(SpecialConditions.CONFUSED)

sap_sipper_passive = TypedDamageBoostPassive(PokemonTypes.GRASS, 80)

gyro_unit_passive = retreat_free_when(
    lambda pokemon, carrier: (
        pokemon.owning_player_id == carrier.owning_player_id
        and is_basic_pokemon(pokemon)
    )
)

rock_peak_growl_passive = team_damage_boost_passive(
    10, attacker_pred=lambda p: _logic_name(p) == "Registeel",
)


class SurgeSurferPassive(Passive):
    """If any Stadium is in play, this Pokémon has no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        area = board.find_global_area("activeStadium")
        if area and area.children:
            return 0
        return cost


class IcebergShieldPassive(Passive):
    """If Regirock is in play, prevent attack damage and effects from Stage 2."""

    def _armed(self, carrier) -> bool:
        me = carrier_pokemon(carrier)
        return me is not None and "Regirock" in _logic_names_in_play(me)

    def _from_opp_stage2(self, calc, carrier) -> bool:
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target or calc.attacker is None:
            return False
        if not is_stage2_pokemon(calc.attacker):
            return False
        return self._armed(carrier)

    def prevents_damage(self, calc, carrier):
        return self._from_opp_stage2(calc, carrier)

    def blocks_attack_effects_from(self, target, attacker, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        if attacker is None or not is_stage2_pokemon(attacker):
            return False
        return self._armed(carrier)


class SealOfAntiquityPassive(Passive):
    """Can't attack unless Regirock, Regice, and Registeel are on the Bench."""

    NEEDED = {"Regirock", "Regice", "Registeel"}

    def blocks_attacks(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        return not self.NEEDED <= _logic_names_in_play(pokemon, bench_only=True)


class DevouredFieldPassive(Passive):
    """Darkness and Dragon attacks do +10 to the opponent's Active (both sides)."""

    TYPES = {PokemonTypes.DARKNESS.value, PokemonTypes.DRAGON.value}

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None:
            return
        types = attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        if self.TYPES & set(types):
            calc.amount += 10


class SeaOfNothingnessPassive(Passive):
    """Special Conditions are not removed when Pokémon evolve or devolve."""

    def keeps_conditions_on_evolve(self, pokemon, carrier):
        return True


class DashingPouchPassive(Passive):
    """Retreat-cost Energy from the holder goes to hand instead of discard."""

    def retreat_cost_destination(self, pokemon, energy, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return None
        return "hand"


class MemoryTypePassive(Passive):
    """The attached Silvally-GX is `pokemon_type` instead of Colorless."""

    def __init__(self, pokemon_type):
        self.pokemon_type = pokemon_type

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        if _logic_name(pokemon) != "SilvallyGX":
            return types
        return [self.pokemon_type.value]


class CounterEnergyPassive(Passive):
    """Colorless, or every type 2-at-a-time when more prizes remain on a non-GX/EX."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None:
            return options
        owner = holder.owning_player_id
        opponent = _other_player(board, owner)
        if opponent is None:
            return options
        if _prize_count(board, owner) <= _prize_count(board, opponent):
            return options
        if is_gx_or_ex(holder):
            return options
        return ALL_TYPES_TWO_AT_A_TIME


class AttacksDoMorePassive(Passive):
    """The carrier's attacks do +N (Lucha Fight rider on the Defending Pokémon)."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        if calc.is_attack and carrier_pokemon(carrier) is calc.attacker:
            calc.amount += self.amount


# ======================================================================
# Attacks
# ======================================================================

revenge_cannon = damage_per(_bench_damage_counters, 10, base=10)


async def tower_go_round_gx(ctx):
    """Printed 180, then move any number of your Energy in any way you like."""
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    if len(mine) >= 2:
        await ctx.move_energy_freely(mine, mine)


super_electromagnetic_tackle = recoil_attack(50)
self_destruct = recoil_attack(100)


async def heavy_rock_gx(ctx):
    """Printed 100; opponent can't play any cards during their next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _all_cards_lock)


async def dance_of_flames(ctx):
    """For each Energy on the opponent's Pokémon, attach a Fire Energy from discard."""
    needed = sum(len(ctx.attached_energies(p)) for p in ctx.opponent_pokemon_in_play())
    fires = [c for c in ctx.discard_pile() if is_fire_energy(c)]
    take = min(needed, len(fires))
    if take <= 0:
        return
    picks = await ctx.choose_cards(
        fires, take, minimum=take,
        prompt="Choose Fire Energy to attach",
    )
    mine = ctx.my_pokemon_in_play()
    if picks and mine:
        await distribute_energy(ctx, picks, mine)


async def burning_bonemerang(ctx):
    """Flip 2 coins: 70×heads, and Burn if any heads."""
    results = await ctx.flip_coins(2, "Burning Bonemerang")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(70 * heads)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


psychic_70_plus = damage_per(count_energy("defender"), 20, base=70)


async def draco_melody(ctx):
    """Flip a coin. If heads, search for a Dragon Pokémon onto the Bench."""
    results = await ctx.flip_coins(1, "Draco Melody")
    if results and results[0]:
        await search_to_bench(is_dragon_pokemon, count=1)(ctx)


async def sudden_sting(ctx):
    """Printed 10; if evolved from Kakuna this turn, Paralyze and Poison."""
    await ctx.deal_damage()
    if _evolved_from_this_turn(ctx, "Kakuna"):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


absorption_gx = damage_per(count_prizes_remaining(), 40)
sucker_punch = bonus_if(_self_has_darkness, 30)
continuous_headbutt = flip_damage(until_tails=True, per_heads=80)


async def bell_of_silence(ctx):
    """Printed 10; opponent can't play Pokémon that have Abilities next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, pokemon_has_ability)


async def amazing_plea(ctx):
    """Choose 2 from discard; opponent may allow them into hand, else 80 damage."""
    pile = list(ctx.discard_pile())
    if len(pile) < 2:
        return
    picks = await ctx.choose_cards(pile, 2, prompt="Choose 2 cards from your discard pile")
    if len(picks) < 2:
        return
    if await ctx.ask_yes_no(
        "Allow those cards into the hand?", player_id=ctx.opponent_id,
    ):
        await ctx.put_in_hand(picks)
    else:
        await ctx.deal_damage(80)


energy_catch = recover_from_discard(is_basic_energy_card, count=3, minimum=0)
volt_switch = switch_self_attack(bench_predicate=is_lightning_pokemon)
earthquake = spread_damage(10, side="mine", also_base=True)


async def pumpkin_bomb(ctx):
    """You may discard any number of your Tools; 10 + 40 per discarded Tool."""
    tools = [
        child for pokemon in ctx.my_pokemon_in_play()
        for child in pokemon.children if is_tool_card(child)
    ]
    picked = await ctx.choose_cards(
        tools, len(tools), minimum=0,
        prompt="Choose Pokémon Tool cards to discard",
    ) if tools else []
    await ctx.discard_cards(picked)
    await ctx.deal_damage(10 + 40 * len(picked))


psych_up = boost_own_next_turn(60, attack_title="Psych Up")


async def eat_sloppily(ctx):
    """Discard the top 5 of your deck; attach any discarded Energy to this Pokémon."""
    top = list(ctx.deck_top(5))
    await ctx.discard_cards(top)
    energies = [c for c in top if is_energy_card(c)]
    for energy in energies:
        await ctx.attach_energy(energy, ctx.attacker)


async def glutton_gx(ctx):
    """Printed 100; take 2 extra Prize cards if this attack KOs."""
    await ctx.deal_damage()
    ctx.extra_prizes += 2


async def draconic_disaster(ctx):
    """100, +100 and discard the Stadium if one is in play."""
    stadium = ctx.stadium_in_play()
    await ctx.deal_damage(200 if stadium is not None else 100)
    if stadium is not None:
        await ctx.discard_stadium()


async def dread_storm_gx(ctx):
    """Discard an Energy from each of the opponent's Pokémon."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        await ctx.discard_energy_from(
            pokemon, 1, prompt="Choose an Energy to discard",
        )


async def pain_amplifier(ctx):
    """Put 2 damage counters on each damaged opponent Pokémon."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        if _is_damaged(ctx, pokemon):
            await ctx.deal_damage(
                20, target=pokemon, apply_modifiers=False, as_counters=True,
            )


kakuna_multiply = search_to_bench(
    lambda c: _logic_name(c) == "Kakuna", count=3,
    prompt="Choose Kakuna to put onto your Bench.",
)


async def slice_off(ctx):
    """On play: you may discard a Special Energy from 1 of the opponent's Pokémon."""
    holders = [
        p for p in ctx.opponent_pokemon_in_play()
        if any(is_special_energy(e) for e in ctx.attached_energies(p))
    ]
    if not holders:
        return
    if not await ctx.ask_yes_no(
        "Discard a Special Energy from 1 of your opponent's Pokémon?"
    ):
        return
    target = await ctx.choose_pokemon(
        holders, "Choose a Pokémon to discard a Special Energy from",
    )
    if target is None:
        return
    specials = [e for e in ctx.attached_energies(target) if is_special_energy(e)]
    picked = await ctx.choose_cards(
        specials, 1, prompt="Choose a Special Energy to discard",
    )
    await ctx.discard_cards(picked)


async def blade_gx(ctx):
    """Take a Prize card."""
    await ctx.take_prizes(1)


war_cry = bonus_if(_fewer_in_play, 90)


async def clanging_scales(ctx):
    """Printed 130; this Pokémon takes 30 more from attacks during the opponent's next turn."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TakesMorePassive(30))


async def forceful_tackle(ctx):
    """You may put up to 9 damage counters on this Pokémon; 90 + 10 per counter placed."""
    n = await ctx.choose(
        "Put how many damage counters on this Pokémon?",
        [str(i) for i in range(10)],
        use_panel=False,
    )
    if n:
        await ctx.deal_damage(
            n * 10, target=ctx.attacker, apply_modifiers=False, as_counters=True,
        )
    await ctx.deal_damage(90 + n * 10)


async def tlc(ctx):
    """Shuffle 1 damaged opponent Benched Pokémon and attachments into their deck."""
    damaged = [p for p in ctx.opponent_bench() if _is_damaged(ctx, p)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(
        damaged, "Choose a damaged Benched Pokémon to shuffle into the deck",
    )
    if target is not None:
        await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)


async def chaos_wheel(ctx):
    """Printed 30; opponent can't play Tool, Special Energy, or Stadium next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _tool_special_energy_or_stadium)


async def empty_light(ctx):
    """On play: you may Confuse and Poison both Active Pokémon."""
    if not await ctx.ask_yes_no("Leave both Active Pokémon Confused and Poisoned?"):
        return
    for pokemon in (ctx.my_active(), ctx.opponent_active()):
        if pokemon is None:
            continue
        await ctx.apply_special_condition(pokemon, SpecialConditions.CONFUSED)
        await ctx.apply_special_condition(pokemon, SpecialConditions.POISONED)


async def symbiont_gx(ctx):
    """Add the top 2 of the opponent's deck to their Prize cards."""
    top = list(ctx.deck_top(2, player_id=ctx.opponent_id))
    if top:
        await ctx.put_in_prizes(top, player_id=ctx.opponent_id, append=True)


ink_spit = smokescreen_attack()
special_artillery = discard_for_bonus(
    source="self-energy", predicate=is_special_energy, max_count=1, per=80,
)
fixer_of_the_forest = recover_from_discard(is_tool_card, count=3, minimum=0)


async def rest(ctx):
    """This Pokémon is now Asleep. Heal 90 damage from it."""
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await ctx.heal(90, ctx.attacker)


async def lucha_fight(ctx):
    """Printed 90; the Defending Pokémon's attacks do +30 during the opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.add_passive_through_opponents_turn(defender, AttacksDoMorePassive(30))


async def iron_hand(ctx):
    """Printed 90; if Regice is on your Bench, heal 30 from this Pokémon."""
    await ctx.deal_damage()
    if any(_logic_name(p) == "Regice" for p in ctx.my_bench()):
        await ctx.heal(30, ctx.attacker)


severe_poison = condition_attack(SpecialConditions.POISONED, counters=4)


async def sky_hunting(ctx):
    """Printed 120; if this attack KOs, switch this Pokémon with a Benched one."""
    await ctx.deal_damage()
    if not any(p.owning_player_id == ctx.opponent_id for p in ctx.knockouts):
        return
    bench = ctx.my_bench()
    if not bench:
        return
    pick = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to switch into the Active Spot",
    )
    if pick is not None:
        await ctx.switch_active(ctx.player_id, pick)


punishing_slap = bonus_if(_opponent_has_darkness_energy, 60)


def evolve_from_search(logic_name: str):
    """Search the deck for a card that evolves from `logic_name` and evolve it."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            lambda c: evolves_from(c.archetype_id, logic_name),
            count=1, minimum=0,
            prompt=f"Choose a card that evolves from {logic_name}.",
        )
        if picks:
            await ctx.evolve_pokemon(ctx.source, picks[0])
        await ctx.shuffle_deck()
    return effect


waterfall_evolution = evolve_from_search("Magikarp")


# ======================================================================
# Abilities
# ======================================================================

async def weed_out(ctx):
    """Choose 3 of your Benched Pokémon; discard the rest of the Bench."""
    bench = list(ctx.my_bench())
    if len(bench) <= 3:
        return
    keep = await ctx.choose_cards(bench, 3, prompt="Choose 3 Benched Pokémon to keep")
    if len(keep) < 3:
        return
    keep_ids = {p.entity_id for p in keep}
    for pokemon in bench:
        if pokemon.entity_id not in keep_ids:
            await ctx.discard_cards(full_stack(pokemon))


async def shell_on(ctx):
    """Discard a Shelmet from hand, then evolve this Pokémon from the deck."""
    shelmets = [c for c in ctx.hand() if _logic_name(c) == "Shelmet"]
    if not shelmets:
        return
    picked = await ctx.choose_cards(shelmets, 1, prompt="Discard a Shelmet")
    if not picked:
        return
    await ctx.discard_cards(picked)
    await evolve_from_search("Karrablast")(ctx)


async def moomoo_malt(ctx):
    """While Active, heal 90 from a Pokémon you attach Energy to from hand."""
    if not is_in_active_spot(ctx.source):
        return
    if ctx.attaching_player_id != ctx.player_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    await ctx.heal(90, receiver)


async def escape(ctx):
    """Shuffle this Pokémon and all attached cards into your deck."""
    source = ctx.source
    was_active = source is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(source), ctx.player_id)
    await _promote_self_if_needed(ctx, was_active)


# ======================================================================
# Trainers
# ======================================================================

counter_catcher = bosss_orders


async def gladion(ctx):
    """Look at face-down Prizes, put 1 into hand, shuffle Gladion into the rest."""
    session = ctx.session
    prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    if not prize_area or not prize_area.children:
        return
    prizes = list(prize_area.children)
    prize_ids = [c.entity_id for c in prizes]
    picked_id = await session.prompt_prize_reveal_pick(
        ctx.player_id, ctx.source.entity_id, prize_ids, prize_ids,
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


lusamine = recover_from_discard(
    lambda c: is_supporter_card(c) or is_stadium_card(c),
    count=2, minimum=0,
)


async def peeking_red_card(ctx):
    """Opponent reveals their hand; you may shuffle it into their deck and they redraw."""
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    n = len(cards)
    if not n:
        return
    if await ctx.ask_yes_no(
        f"Shuffle the opponent's {n} cards into their deck? They draw {n}."
    ):
        await ctx.shuffle_into_deck(list(ctx.hand(ctx.opponent_id)), ctx.opponent_id)
        await ctx.draw_cards(n, player_id=ctx.opponent_id)
