"""Cosmic Eclipse (SM12) attack, ability, trainer, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

import random

from spirit.game.attributes import (
    AttrID, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Ability, Activations, Attack, TRAINER_EFFECTS_BY_GUID, Triggers,
    def_for, evolves_from_chain, is_prism_star, is_tag_team, is_ultra_beast,
    subtypes_for, unimplemented,
)
from spirit.game.models.board import PokemonEntity
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.passives import Passive, carrier_pokemon, effective_max_hp
from spirit.game.card_effects.attacks_common import (
    _printed,
    bonus_if,
    condition_attack,
    count_discard,
    count_energy,
    count_in_play,
    count_prizes_remaining,
    damage_counters_on,
    damage_per,
    defender_has_condition,
    discard_for_bonus,
    flip_damage,
    has_attack_titled,
    has_extra_energy,
    lock_defender_attacks,
    place_counters,
)
from spirit.game.card_effects.passives_common import (
    apply_protection,
    boost_own_next_turn,
    is_in_active_spot,
    no_retreat_passive,
    takes_less_passive,
    team_damage_boost_passive,
    trainer_effect_shield_passive,
)
from spirit.game.card_effects.sm3 import (
    is_fire_energy,
    is_grass_energy,
    is_gx_or_ex,
    is_tool_card,
    is_water_energy,
)
from spirit.game.card_effects.sm4 import is_lightning_pokemon
from spirit.game.card_effects.sm5 import _direct_evolves_from, is_fairy_pokemon
from spirit.game.card_effects.sm6 import is_dragon_pokemon, is_fighting_energy
from spirit.game.card_effects.sm8 import lost_march
from spirit.game.card_effects.sm10 import is_lightning_energy
from spirit.game.card_effects.dm import ko_last_turn_condition
from spirit.game.card_effects.support_common import (
    distribute_energy,
    draw_attack,
    draw_until_effect,
    heal_targets,
    look_top_attach_energy,
    opponent_switches,
    recover_from_discard,
    requires_hand,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    FossilBodyPassive, is_basic_energy_card, is_energy_card,
)


_BURNED = SpecialConditions.BURNED
_PARALYZED = SpecialConditions.PARALYZED
_POISONED = SpecialConditions.POISONED
_CONFUSED = SpecialConditions.CONFUSED
_ASLEEP = SpecialConditions.ASLEEP


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    return getattr(def_for(getattr(card, "archetype_id", None)), "display_name", "") or ""


def _playmat(entity):
    node = entity
    while node is not None and getattr(node, "parent", None) is not None:
        node = node.parent
    return node


def _hand(board, player_id):
    area = board.find_player_area(player_id, "hand")
    return list(area.children) if area else []


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _is_unidentified_fossil(card) -> bool:
    return _display_name(card) == "Unidentified Fossil"


def _is_eevee(card) -> bool:
    return _logic_name(card) in ("Eevee", "EeveeGX") or _display_name(card) in (
        "Eevee", "Eevee-GX")


def _is_tag_team_card(card) -> bool:
    return is_tag_team(getattr(card, "archetype_id", None))


def _is_lillies_poke_doll(card) -> bool:
    return _display_name(card) == "Lillie's Poké Doll"


def _runnable_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


def _named_in_play_from(pokemon, *names) -> bool:
    playmat = _playmat(pokemon)
    owner = pokemon.owning_player_id
    wanted = set(names)
    for child in getattr(playmat, "children", []) or []:
        if getattr(child, "owning_player_id", None) != owner:
            continue
        for area in child.children:
            if area.get_attribute(AttrID.NAME) not in ("activePokemonArea", "bench"):
                continue
            for ally in area.children:
                if _logic_name(ally) in wanted:
                    return True
    return False


def _opponent_active_from(pokemon):
    playmat = _playmat(pokemon)
    owner = pokemon.owning_player_id
    for child in getattr(playmat, "children", []) or []:
        pid = getattr(child, "owning_player_id", None)
        if pid in (None, owner):
            continue
        for area in child.children:
            if area.get_attribute(AttrID.NAME) == "activePokemonArea":
                return next(iter(area.children), None)
    return None


def _own_stadium_in_play(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return False
    owner = stadium.owning_player_id or getattr(stadium, "home_player_id", None)
    return owner == ctx.player_id


def _stadium_in_play(ctx) -> bool:
    return ctx.stadium_in_play() is not None


def _deck_at_most_3(ctx) -> bool:
    return len(ctx.deck()) <= 3


def _two_basic_energy_types(ctx) -> bool:
    types = set()
    attacker = ctx.attacker
    if attacker is None:
        return False
    for energy in ctx.attached_energies(attacker):
        if not is_basic_energy_card(energy):
            continue
        for energy_type in energy.get_attribute(AttrID.POKEMON_TYPES) or []:
            types.add(energy_type)
    return len(types) >= 2


def _has_water_energy(ctx) -> bool:
    attacker = ctx.attacker
    return attacker is not None and any(
        is_water_energy(energy) for energy in ctx.attached_energies(attacker))


def _played_tag_team_supporter(ctx) -> bool:
    return ctx.played_trainer_this_turn(
        lambda record: record[2] == TrainerType.SUPPORTER.value
        and is_tag_team(record[0])
    ) > 0


def _basic_fire_or_lightning(card) -> bool:
    return is_basic_energy_card(card) and (
        is_fire_energy(card) or is_lightning_energy(card))


# ----------------------------------------------------------------------
# Passives
# ----------------------------------------------------------------------

class DoubleTypePassive(Passive):
    """This Pokémon is Psychic and Fighting type."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        return [PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value]


class BeastBoostPassive(Passive):
    """This Pokémon's attacks do +20 to the opponent's Active per Prize taken."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or carrier_pokemon(carrier) is not attacker:
            return
        calc.amount += 20 * calc.board.prizes_taken(attacker.owning_player_id)


class BoilingBloodPassive(Passive):
    """Attacks cost ColorlessColorlessColorless less if the opponent has a GX/EX."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        opp = _other_player(board, pokemon.owning_player_id)
        if opp is None or not any(is_gx_or_ex(p) for p in board.pokemon_in_play(opp)):
            return cost
        if "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - 3
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


class FightersRoarPassive(Passive):
    """Can evolve the turn it is played if the opponent's Active is GX/EX."""

    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        active = _opponent_active_from(pokemon)
        return active is not None and is_gx_or_ex(active)


def _sunne_protects(target, carrier) -> bool:
    if target.owning_player_id != carrier.owning_player_id:
        return False
    if _logic_name(target) not in ("Solgaleo", "Lunala"):
        return False
    return _named_in_play_from(carrier, "Lunala")


double_type_passive = DoubleTypePassive()
beast_boost_passive = BeastBoostPassive()
boiling_blood_passive = BoilingBloodPassive()
fighters_roar_passive = FightersRoarPassive()
armor_of_the_sunne_passive = takes_less_passive(
    50, protects=_sunne_protects, stack_key="armor_of_the_sunne")


# ----------------------------------------------------------------------
# Factory-backed attacks
# ----------------------------------------------------------------------

allergic_explosion_gx = condition_attack(_BURNED, _PARALYZED, _POISONED)
ancient_blast = damage_per(
    count_discard("mine", _is_unidentified_fossil), 50, base=20)
bye_bye_throw = discard_for_bonus(
    source="hand", max_count=2, per=60, base=0, optional=True,
    prompt="Discard up to 2 cards from your hand")
dazzling_blizzard = bonus_if(_own_stadium_in_play, 100)
dig_deep = recover_from_discard(
    is_energy_card, count=1, minimum=0,
    prompt="Choose an Energy card from your discard pile")
dragon_arcana = bonus_if(_two_basic_energy_types, 70)
dual_calling = search_to_hand(
    _is_tag_team_card, count=2, minimum=0,
    prompt="Choose up to 2 TAG TEAM cards")
eleventh_hour_tackle = bonus_if(_deck_at_most_3, 150)
fire_fling = recover_from_discard(
    is_fire_energy, count=4, minimum=0,
    prompt="Choose Fire Energy cards from your discard pile")
floral_invitation = search_to_hand(
    is_fairy_pokemon, count=2, minimum=0,
    prompt="Choose up to 2 Fairy Pokémon")
follow_my_tail = search_to_bench(
    _is_eevee, count=BENCH_CAPACITY,
    prompt="Choose Eevee or Eevee-GX to put onto your Bench.")
freezing_punch = bonus_if(_has_water_energy, 80)
iron_tail = flip_damage(until_tails=True, per_heads=100)
beloved_pulse = bonus_if(_played_tag_team_supporter, 80)
_look_top_8_energy = look_top_attach_energy(8, is_basic_energy_card)


# ----------------------------------------------------------------------
# Custom attacks / abilities
# ----------------------------------------------------------------------

async def _promote_if_needed(ctx, owner):
    if not await ctx.session._promote_new_active(owner):
        screen_name = ctx.session.players[owner].screen_name
        winner = ctx.opponent_id if owner == ctx.player_id else ctx.player_id
        await ctx.session.end_game(winner, f"{screen_name} has no Pokémon left")


async def backfire(ctx):
    await ctx.deal_damage()
    fires = [e for e in ctx.attached_energies(ctx.attacker) if is_fire_energy(e)]
    if not fires:
        return
    take = min(2, len(fires))
    picks = await ctx.choose_cards(
        fires, take, minimum=take,
        prompt="Put Fire Energy into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


async def bag_slash(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    items = [c for c in cards if is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(
        items, 1, prompt="Discard an Item card from your opponent's hand")
    if picks:
        await ctx.discard_cards(picks)


async def balloon_burst(ctx):
    await ctx.deal_damage()
    attacker = ctx.attacker
    owner = attacker.owning_player_id or ctx.player_id
    was_active = attacker is ctx.board.active_pokemon(owner)
    await ctx.discard_cards(full_stack(attacker))
    if was_active:
        async def _promote():
            await _promote_if_needed(ctx, owner)
        ctx.deferred_actions.append(_promote)


async def brilliant_flare(ctx):
    await ctx.deal_damage()
    if not await ctx.ask_yes_no("Search your deck for up to 3 cards?"):
        return
    picks = await ctx.search_deck(
        None, count=3, minimum=0,
        prompt="Choose up to 3 cards to put into your hand.")
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def blow_away_bomb(ctx):
    """Roxie calls this after discarding a Koffing/Weezing from hand."""
    if not await ctx.ask_yes_no(
            "Put 1 damage counter on each of your opponent's Pokémon?"):
        return
    await place_counters(1, target="each_opponent")(ctx)


async def charming_stamp(ctx):
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Choose 1 of your Pokémon", player_id=ctx.opponent_id)
    if target is not None:
        await ctx.deal_damage(90, target=target, apply_modifiers=False)


def cold_snap_condition(board, player_id, pokemon=None) -> bool:
    state = getattr(board, "turn_state", None)
    if state is None:
        return True
    return not any(title == "Cold Snap" for _, _, title in state.attacks_used_last_turn)


async def cold_snap(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_trainer_card)


async def cross_break_gx(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    first = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to take 170 damage")
    if first is None:
        return
    await ctx.deal_damage(170, target=first, apply_modifiers=False)
    if ctx.played_trainer_this_turn("N's Resolve") <= 0:
        return
    rest = [p for p in ctx.opponent_bench() if p is not first]
    if not rest:
        return
    second = await ctx.choose_pokemon(
        rest, "Choose another Benched Pokémon to take 170 damage")
    if second is not None:
        await ctx.deal_damage(170, target=second, apply_modifiers=False)


async def desert_hurricane(ctx):
    extra = 120 if _stadium_in_play(ctx) else 0
    await ctx.deal_damage(_printed(ctx) + extra)
    if extra:
        await ctx.discard_stadium()


async def direct_dive(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 99, prompt="Discard all Energy from this Pokémon")
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "This attack does 100 damage to 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(100, target=target, apply_modifiers=False)


async def dirty_throw(ctx):
    if ctx.hand_size() == 0:
        return
    discarded = await ctx.discard_from_hand(
        1, minimum=1, prompt="Discard a card from your hand")
    if not discarded:
        return
    await ctx.deal_damage()


async def doll_swap(ctx):
    await ctx.deal_damage()
    pokemon = ctx.attacker
    owner = pokemon.owning_player_id or ctx.player_id
    was_active = pokemon is ctx.board.active_pokemon(owner)
    await ctx.put_in_hand(full_stack(pokemon), reveal=False)

    async def _replace():
        dolls = [c for c in ctx.hand(owner) if _is_lillies_poke_doll(c)]
        active_area = ctx.board.find_player_area(owner, "activePokemonArea")
        if dolls and isinstance(dolls[0], PokemonEntity) and active_area is not None:
            if await ctx.ask_yes_no(
                    "Play Lillie's Poké Doll as your new Active Pokémon?"):
                doll = dolls[0]
                if ctx.board.move_card(doll.entity_id, active_area.entity_id):
                    ctx.session.turn_state.mark_entered_play(doll.entity_id)
                    ctx.session.turn_state.became_active_turn[doll.entity_id] = (
                        ctx.session.turn_state.turn_number)
                    await ctx.session.fire_move_to_active_triggers(doll)
                    return
        if was_active:
            await _promote_if_needed(ctx, owner)

    ctx.deferred_actions.append(_replace)


async def drought(ctx):
    cards = [c for c in ctx.hand() if is_fighting_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0, prompt="Choose up to 2 Fighting Energy cards")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Energy to")
    if target is None:
        return
    for card in picks:
        await ctx.attach_energy(card, target)


async def explosive_fire_dance(ctx):
    if not await ctx.ask_yes_no("Look at the top 8 cards of your deck?"):
        return
    await _look_top_8_energy(ctx)


async def energy_assist(ctx):
    bench = ctx.my_bench()
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not bench or not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0,
        prompt="Choose basic Energy cards to attach to your Benched Pokémon")
    if picks:
        await distribute_energy(ctx, picks, bench)


async def fabled_flarebolts(ctx):
    pool = []
    for pokemon in ctx.my_bench():
        for energy in ctx.attached_energies(pokemon):
            if _basic_fire_or_lightning(energy):
                pool.append(energy)
    picks = await ctx.choose_cards(
        pool, 3, minimum=0,
        prompt="Discard up to 3 basic Fire or Lightning Energy from your Benched Pokémon",
    ) if pool else []
    await ctx.discard_cards(picks)
    if picks:
        await ctx.deal_damage(90 * len(picks))


async def fireworks_bomb(ctx):
    n = 12 if count_prizes_remaining("opponent")(ctx) == 3 else 4
    await ctx.place_damage_counters(n)


async def fist_of_antiquity(ctx):
    if any(is_supporter_card(c) for c in ctx.discard_pile()):
        return
    await ctx.deal_damage()


async def flower_picking(ctx):
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    if not await ctx.ask_yes_no(
            "Choose 2 random cards from your opponent's hand?"):
        return
    picks = random.sample(hand, min(2, len(hand)))
    await ctx.reveal_cards(picks, to_player=ctx.player_id)
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def grim_marking(ctx):
    if not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    await ctx.place_damage_counters(4)


async def heavy_hold(ctx):
    await ctx.deal_damage()
    lock_defender_attacks(ctx)


def impersonation_condition(board, player_id, pokemon=None) -> bool:
    return any(_runnable_supporter(c) for c in _hand(board, player_id))


async def impersonation(ctx):
    candidates = [c for c in ctx.hand() if _runnable_supporter(c)]
    if not candidates:
        return
    picked = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Discard a Supporter card and use its effect")
    if not picked:
        return
    await ctx.discard_cards(picked)
    effect = TRAINER_EFFECTS_BY_GUID[(picked[0].archetype_id or "").lower()]
    await effect(ctx)


async def improvisational_performance(ctx):
    n = ctx.hand_size()
    extra = 100 if n == 1 else 0
    await ctx.deal_damage(_printed(ctx) + extra)
    if n == 3:
        await ctx.apply_special_condition(ctx.defender, _CONFUSED)
    if n == 6:
        for pokemon in ctx.opponent_bench():
            await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)


async def arf_arf_bark(ctx):
    discarded = ctx.source in ctx.discard_pile(ctx.player_id)
    if discarded and (not ctx.ko_from_attack or not ctx.was_active_at_ko):
        return
    active = ctx.opponent_active()
    if active is None or not ctx.attached_energies(active):
        return
    if not await ctx.ask_yes_no(
            "Discard an Energy from your opponent's Active Pokémon?"):
        return
    await ctx.discard_energy_from(
        active, 1, prompt="Choose an Energy to discard from the Defending Pokémon")


def _prizes_remaining(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _is_damaged_pokemon(pokemon) -> bool:
    playmat = _playmat(pokemon)
    board = getattr(playmat, "board_state", None) if playmat is not None else None
    current = pokemon.get_attribute(AttrID.HP, 0) or 0
    if board is not None:
        return current < effective_max_hp(board, pokemon)
    definition = def_for(getattr(pokemon, "archetype_id", None))
    return current < (getattr(definition, "hp", 0) or 0)


def _is_gx_pokemon(card) -> bool:
    return "GX" in subtypes_for(getattr(card, "archetype_id", None))


def _is_eevee_gx_evolution(card) -> bool:
    if not _is_gx_pokemon(card):
        return False
    chain = evolves_from_chain(getattr(card, "archetype_id", None))
    return bool(chain) and chain[0] in ("Eevee", "EeveeGX")


def _is_wishiwashi(card) -> bool:
    return _logic_name(card) in ("Wishiwashi", "WishiwashiGX")


def _is_grass_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.GRASS.value in types


def _is_solgaleo_or_lunala(card) -> bool:
    return _logic_name(card) in ("Solgaleo", "Lunala")


def _retreat_cost_exactly_4(card) -> bool:
    return is_pokemon_card(card) and (card.get_attribute(AttrID.RETREAT_COST) or 0) == 4


def _first_named_ability_carrier(pokemon, title: str):
    playmat = _playmat(pokemon)
    owner = pokemon.owning_player_id
    for child in getattr(playmat, "children", []) or []:
        if getattr(child, "owning_player_id", None) != owner:
            continue
        for area in child.children:
            if area.get_attribute(AttrID.NAME) not in ("activePokemonArea", "bench"):
                continue
            for ally in area.children:
                definition = def_for(getattr(ally, "archetype_id", None))
                for ability in getattr(definition, "abilities", None) or []:
                    if getattr(ability, "title", None) == title:
                        return ally
    return None


def _hand_size(board, player_id) -> int:
    area = board.find_player_area(player_id, "hand")
    return len(area.children) if area else 0


# ----------------------------------------------------------------------
# Remaining passives
# ----------------------------------------------------------------------

class AlteredCreationPassive(Passive):
    """Rest-of-game +30 to Active; optional extra prize on Active KOs."""

    def __init__(self, owner_id, extra_prize: bool):
        self.owner_id = owner_id
        self.extra_prize = extra_prize

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.attacker is None or calc.attacker.owning_player_id != self.owner_id:
            return
        calc.amount += 30

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if not self.extra_prize:
            return count
        if not ctx.is_attack_effect():
            return count
        if ctx.attacker is None or ctx.attacker.owning_player_id != self.owner_id:
            return count
        if ctx.board.active_pokemon(pokemon.owning_player_id) is not pokemon:
            return count
        return count + 1


class SmugFacePassive(Passive):
    """Prevent attack effects including damage from TAG TEAM, Ultra Beasts,
    and Pokémon with Special Energy attached."""

    def _matches(self, attacker) -> bool:
        if attacker is None:
            return False
        if is_tag_team(attacker.archetype_id) or is_ultra_beast(attacker.archetype_id):
            return True
        playmat = _playmat(attacker)
        board = getattr(playmat, "board_state", None) if playmat is not None else None
        if board is None:
            return False
        return any(is_special_energy(e) for e in board.attached_energies(attacker))

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return self._matches(calc.attacker)

    def blocks_attack_effects_from(self, target, attacker, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return self._matches(attacker)


class ShadowBoxPassive(Passive):
    """Damaged Pokémon-GX (both sides) have no Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        if not _is_gx_pokemon(pokemon):
            return False
        return _is_damaged_pokemon(pokemon)


class UltraBurstPassive(Passive):
    """Can't attack unless the opponent has 2 or fewer Prize cards remaining."""

    def blocks_attacks(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        playmat = _playmat(pokemon)
        board = getattr(playmat, "board_state", None) if playmat is not None else None
        if board is None:
            return False
        opp = _other_player(board, pokemon.owning_player_id)
        if opp is None:
            return True
        return _prizes_remaining(board, opp) > 2


class SpeedCheerPassive(Passive):
    """Eevee-GX evolutions' attacks cost Colorless less; max 1 Speed Cheer."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is None:
            return cost
        if _first_named_ability_carrier(holder, "Speed Cheer") is not holder:
            return cost
        if pokemon.owning_player_id != holder.owning_player_id:
            return cost
        if not _is_eevee_gx_evolution(pokemon):
            return cost
        if "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - 1
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


class VitalityCheerPassive(Passive):
    """Eevee-GX evolutions get +60 HP; max 1 Vitality Cheer."""

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None:
            return 0
        if _first_named_ability_carrier(holder, "Vitality Cheer") is not holder:
            return 0
        if pokemon.owning_player_id != holder.owning_player_id:
            return 0
        if not _is_eevee_gx_evolution(pokemon):
            return 0
        return 60


class SolarPowerPassive(Passive):
    """During the owner's next turn, Grass and Fire attacks ignore Energy costs."""

    def __init__(self, owner_id, start_turn: int):
        self.owner_id = owner_id
        self.start_turn = start_turn

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        ts = getattr(board, "turn_state", None)
        if ts is None or ts.turn_number <= self.start_turn:
            return cost
        if pokemon.owning_player_id != self.owner_id:
            return cost
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if (PokemonTypes.GRASS.value not in types
                and PokemonTypes.FIRE.value not in types):
            return cost
        return {}


class PoisonCultivationPassive(Passive):
    """Opposing Poisoned Pokémon take 10 poison counters between turns."""

    def modify_poison_counters(self, counters, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None or pokemon.owning_player_id == me.owning_player_id:
            return counters
        if counters <= 0:
            return counters
        return 10


class BeastitePassive(Passive):
    """Ultra Beast holder: +10 to Active per Prize taken."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if not is_ultra_beast(holder.archetype_id):
            return
        calc.amount += 10 * calc.board.prizes_taken(holder.owning_player_id)


class IslandChallengeAmuletPassive(Passive):
    """GX/EX holder: -100 HP; opponent takes 1 fewer Prize on attack KO."""

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon or not is_gx_or_ex(pokemon):
            return 0
        return -100

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon or not is_gx_or_ex(pokemon):
            return count
        if not ctx.is_attack_effect():
            return count
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return count
        return max(0, count - 1)


class ChaoticSwellPassive(Passive):
    """Replacement Stadiums are discarded with no effect."""

    def nullify_stadium_replacement(self, incoming, current, carrier):
        return carrier is current


class NoPrizePassive(Passive):
    """This card takes 0 Prize cards when Knocked Out."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is pokemon:
            return 0
        return count


class LilliesPokeDollPassive(FossilBodyPassive):
    """Can't retreat; opponent takes no Prize cards for a Knock Out."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is carrier or carrier_pokemon(carrier) is pokemon:
            return 0
        return count


smug_face_passive = SmugFacePassive()
shadow_box_passive = ShadowBoxPassive()
ultra_burst_passive = UltraBurstPassive()
speed_cheer_passive = SpeedCheerPassive()
vitality_cheer_passive = VitalityCheerPassive()
power_cheer_passive = team_damage_boost_passive(
    30, attacker_pred=_is_eevee_gx_evolution, once_key="Power Cheer",
    to_active_only=True)
swaying_strangle_passive = no_retreat_passive(
    lambda p, c: (
        p.owning_player_id != (carrier_pokemon(c) or c).owning_player_id
        and bool(p.get_attribute(AttrID.SPECIAL_CONDITIONS))
    )
)
obnoxious_whirring_passive = trainer_effect_shield_passive(
    supporters_only=True,
    protects=lambda affected, carrier: carrier_pokemon(carrier) is affected,
)
beastite_passive = BeastitePassive()
island_challenge_amulet_passive = IslandChallengeAmuletPassive()
chaotic_swell_passive = ChaoticSwellPassive()
lillies_poke_doll_passive = LilliesPokeDollPassive()


# ----------------------------------------------------------------------
# Factory-backed remaining attacks / abilities
# ----------------------------------------------------------------------

rubbish_blizzard = damage_per(count_discard("mine", is_tool_card), 10)
thumping_fall = discard_for_bonus(
    source="hand", predicate=_retreat_cost_exactly_4, max_count=99, per=50,
    base=0, prompt="Discard Pokémon with a Retreat Cost of exactly 4")
rototiller = recover_from_discard(
    None, count=1, minimum=1, to="deck_shuffle",
    prompt="Choose a card to shuffle into your deck")
parabolic_counter = bonus_if(
    lambda ctx: any(is_lightning_pokemon(p) for p in ctx.opponent_pokemon_in_play()),
    90)
riled_horn = bonus_if(
    lambda ctx: any(is_tag_team(p.archetype_id) for p in ctx.opponent_pokemon_in_play()),
    70)
work_up = boost_own_next_turn(60)
triple_nose = flip_damage(coins=3, bonus_per_heads=40)
powerful_spark = damage_per(count_energy("mine", PokemonTypes.LIGHTNING), 20)
sweet_panic = bonus_if(defender_has_condition(_CONFUSED), 0, else_nothing=True)
school_storm = damage_per(count_in_play("mine", _is_wishiwashi), 20)
disk_reload = draw_until_effect(5)
dance_of_tribute = draw_attack(3)
fragrant_flower_garden = heal_targets(30, "each_own")
victory_heal = heal_targets(20, "bench_choice")
tag_call = dual_calling


async def _confuse_self(ctx):
    if ctx.attacker is not None:
        await ctx.apply_special_condition(ctx.attacker, _CONFUSED)


petal_dance = flip_damage(coins=3, per_heads=60, also=_confuse_self)


def disk_reload_condition(board, player_id, pokemon=None) -> bool:
    return _hand_size(board, player_id) < 5


def dance_of_tribute_condition(board, player_id, pokemon=None) -> bool:
    return ko_last_turn_condition(board, player_id, pokemon)


def victory_heal_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return any(
        (p.get_attribute(AttrID.HP, 0) or 0) < effective_max_hp(board, p)
        for p in (bench.children if bench else [])
        if isinstance(p, PokemonEntity)
    )


def scampering_tail_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    deck = board.find_player_area(opp, "deck")
    return bool(deck and deck.children)


def blinking_lights_condition(board, player_id, pokemon=None) -> bool:
    return scampering_tail_condition(board, player_id, pokemon)


def blessing_of_the_moone_condition(board, player_id, pokemon=None) -> bool:
    return any(_logic_name(p) == "Solgaleo" for p in board.pokemon_in_play(player_id))


def whirlpool_suction_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None or is_in_active_spot(pokemon):
        return False
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    bench = board.find_player_area(opp, "bench")
    return bool(bench and bench.children)


def flaming_shot_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(is_fire_energy(c) for c in (hand.children if hand else []))


def spiritborne_evolution_condition(board, player_id, pokemon=None) -> bool:
    return _hand_size(board, player_id) >= 3


def violent_appetite_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(is_pokemon_card(c) for c in (hand.children if hand else []))


def lillies_poke_doll_condition(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_in_active_spot(pokemon)


# ----------------------------------------------------------------------
# Remaining custom attacks / abilities
# ----------------------------------------------------------------------

async def altered_creation_gx(ctx):
    extra = has_extra_energy(1, PokemonTypes.WATER)(ctx)
    ctx.add_global_passive(
        AlteredCreationPassive(ctx.player_id, extra), expires_after_turn=10 ** 9)


async def splash_maker(ctx):
    await ctx.deal_damage()
    cards = [c for c in ctx.hand() if is_water_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 3, minimum=0, prompt="Attach up to 3 Water Energy cards")
    if not picks:
        return
    attached = await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
    heals = {}
    for _card, target in attached:
        heals[target.entity_id] = heals.get(target.entity_id, 0) + 50
    by_id = {p.entity_id: p for p in ctx.my_pokemon_in_play()}
    for eid, amount in heals.items():
        target = by_id.get(eid)
        if target is not None:
            await ctx.heal(amount, target)


async def bubble_launcher_gx(ctx):
    extra = 150 if has_extra_energy(3, PokemonTypes.WATER)(ctx) else 0
    await ctx.deal_damage(_printed(ctx) + extra)
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, _PARALYZED)


async def jumping_balloon(ctx):
    extra = 60 * count_in_play("opponent", is_gx_or_ex)(ctx)
    await ctx.deal_damage(_printed(ctx) + extra)


async def puffy_smashers_gx(ctx):
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, _ASLEEP)
    if not has_extra_energy(4)(ctx):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "This attack does 200 damage to 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(200, target=target, apply_modifiers=False)


async def violent_appetite(ctx):
    pokes = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not pokes:
        return
    picks = await ctx.choose_cards(
        pokes, 1, prompt="Discard a Pokémon from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.heal(60, ctx.source)


async def chaotic_order_gx(ctx):
    await ctx.turn_prizes_face_up()
    extra_p = has_extra_energy(1, PokemonTypes.PSYCHIC)(ctx)
    extra_d = has_extra_energy(1, PokemonTypes.DARKNESS)(ctx)
    if extra_p and extra_d:
        await ctx.take_prizes(2)


async def stalking_claws_gx(ctx):
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "This attack does 120 damage to 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(
            120, target=target, apply_modifiers=False,
            ignore_weakness=True, ignore_resistance=True,
            ignore_target_effects=True)


async def crimson_flame_pillar_gx(ctx):
    extra = has_extra_energy(1)(ctx)
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks = await ctx.choose_cards(
        cards, 5, minimum=0,
        prompt="Choose up to 5 basic Energy cards to attach") if cards else []
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
    if extra and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, _BURNED)
        await ctx.apply_special_condition(ctx.defender, _CONFUSED)


async def light_of_the_protector_gx(ctx):
    await ctx.deal_damage()
    if ctx.played_trainer_this_turn("Lillie's Full Force") <= 0:
        return
    for pokemon in ctx.my_pokemon_in_play():
        await apply_protection(ctx, target=pokemon, prevent=True, effects_too=True)


async def shining_vine(ctx):
    if ctx.attaching_player_id != ctx.player_id:
        return
    if ctx.energy_receiver is not ctx.source:
        return
    if not is_in_active_spot(ctx.source):
        return
    if ctx.attached_energy is None or not is_grass_energy(ctx.attached_energy):
        return
    if not ctx.opponent_bench():
        return
    if not await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokémon with their Active Pokémon?"):
        return
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose a Benched Pokémon to switch into the Active Spot")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def solar_plant_gx(ctx):
    for pokemon in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(50, target=pokemon, apply_modifiers=False)
    if not has_extra_energy(2)(ctx):
        return
    for pokemon in ctx.my_pokemon_in_play():
        amount = ctx.max_hp(pokemon) - (pokemon.get_attribute(AttrID.HP, 0) or 0)
        if amount > 0:
            await ctx.heal(amount, pokemon)


async def massive_bloom(ctx):
    amount = max(0, _printed(ctx) - 10 * damage_counters_on("self")(ctx))
    if amount:
        await ctx.deal_damage(amount)


async def flaming_shot(ctx):
    fires = [c for c in ctx.hand() if is_fire_energy(c)]
    if not fires:
        return
    picks = await ctx.choose_cards(
        fires, 1, prompt="Discard a Fire Energy card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await place_counters(2, target="choose_any_opponent")(ctx)


async def supreme_puff_gx(ctx):
    ctx.take_extra_turn()
    if not has_extra_energy(14, PokemonTypes.FAIRY)(ctx):
        return
    for pokemon in list(ctx.opponent_bench()):
        await ctx.shuffle_into_deck(full_stack(pokemon), ctx.opponent_id)


async def scatter(ctx):
    if ctx.session.turn_state.active_player_id == ctx.player_id:
        return
    if not _is_damaged_pokemon(ctx.source):
        return
    results = await ctx.flip_coins(1, "Scatter")
    if results and results[0]:
        return
    pokemon = ctx.source
    owner = pokemon.owning_player_id or ctx.player_id
    was_active = pokemon is ctx.board.active_pokemon(owner)
    await ctx.shuffle_into_deck(full_stack(pokemon), owner)
    if was_active:
        async def _promote():
            await _promote_if_needed(ctx, owner)
        ctx.deferred_actions.append(_promote)


async def ominous_news(ctx):
    holders = [
        p for p in ctx.opponent_pokemon_in_play()
        if any(is_special_energy(e) for e in ctx.attached_energies(p))
    ]
    if not holders:
        return
    target = await ctx.choose_pokemon(
        holders, "Choose a Pokémon to discard a Special Energy from")
    if target is None:
        return
    specials = [e for e in ctx.attached_energies(target) if is_special_energy(e)]
    picked = await ctx.choose_cards(
        specials, 1, prompt="Choose a Special Energy to discard")
    if picked:
        await ctx.discard_cards(picked)


async def scampering_tail(ctx):
    top = ctx.deck_top(1, ctx.opponent_id)
    if top:
        await ctx.put_on_bottom_of_deck(top[0])


async def growing_up(ctx):
    results = await ctx.flip_coins(1, "Growing Up")
    if not (results and results[0]):
        return
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Attach a basic Energy card to your Active Pokémon")
    if not picks:
        return
    active = ctx.my_active()
    if active is not None:
        await ctx.attach_energy(picks[0], active)


async def tracking_shot(ctx):
    candidates = [p for p in ctx.opponent_bench() if _is_damaged_pokemon(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates,
        "This attack does 80 damage to 1 of your opponent's Benched Pokémon that has any damage counters on it")
    if target is not None:
        await ctx.deal_damage(80, target=target, apply_modifiers=False)


async def poison_cultivation(ctx):
    active = ctx.opponent_active()
    if active is None:
        return
    if "Poisoned" not in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        return
    ctx.add_temporary_passive(
        ctx.attacker, PoisonCultivationPassive(), expires_after_turn=10 ** 9)


async def spiritborne_evolution(ctx):
    discarded = await ctx.discard_from_hand(
        3, minimum=3, prompt="Discard 3 cards from your hand")
    if len(discarded) < 3:
        return
    name = _logic_name(ctx.source)
    picks = await ctx.search_deck(
        lambda c: _direct_evolves_from(c, name),
        count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon")
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


async def ominous_eyes(ctx):
    await place_counters(2, target="choose_any_opponent")(ctx)


async def solar_power(ctx):
    turn = ctx.session.turn_state.turn_number
    ctx.add_global_passive(
        SolarPowerPassive(ctx.player_id, turn), expires_after_turn=turn + 2)


async def red_banquet(ctx):
    await ctx.deal_damage()
    ctx.extra_prizes += 1


async def sleepy_voice(ctx):
    results = await ctx.flip_coins(1, "Sleepy Voice")
    if results and results[0] and ctx.opponent_active() is not None:
        await ctx.apply_special_condition(ctx.opponent_active(), _ASLEEP)


async def scaly_uppercut(ctx):
    extra = 0
    tools = [
        c for c in ctx.attacker.children
        if c.get_attribute(AttrID.TRAINER_TYPE) in (
            TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)
    ] if ctx.attacker is not None else []
    if tools and await ctx.ask_yes_no("Discard a Pokémon Tool card from this Pokémon?"):
        picked = await ctx.choose_cards(
            tools, 1, prompt="Discard a Pokémon Tool card from this Pokémon")
        if picked:
            await ctx.discard_cards(picked)
            extra = 90
    await ctx.deal_damage(_printed(ctx) + extra)


async def blinking_lights(ctx):
    top = ctx.deck_top(1, ctx.opponent_id)
    if top:
        await ctx.reveal_cards(top, to_player=ctx.player_id)


async def swirling_flow(ctx):
    await ctx.deal_damage()
    if await ctx.ask_yes_no("Have your opponent shuffle their deck?"):
        await ctx.shuffle_deck(ctx.opponent_id)


async def blessing_of_the_moone(ctx):
    def pred(c):
        return is_energy_card(c)
    picks = await ctx.search_deck(
        pred, count=2, minimum=0,
        prompt="Choose up to 2 Energy cards to attach")
    if picks:
        targets = [p for p in ctx.my_pokemon_in_play() if _is_solgaleo_or_lunala(p)]
        if targets:
            await distribute_energy(ctx, picks, targets)
    await ctx.shuffle_deck()


async def call_signal(ctx):
    picks = await ctx.search_deck(
        is_supporter_card, count=3, minimum=0,
        prompt="Choose up to 3 Supporter cards")
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()
    await ctx.knock_out(ctx.source)


async def shadow_imitation(ctx):
    defender = ctx.opponent_active()
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    candidates = []
    for ability in getattr(definition, "abilities", None) or []:
        if not isinstance(ability, Attack):
            continue
        if getattr(ability, "gx", False) or (ability.title or "").rstrip().endswith("GX"):
            continue
        candidates.append((defender, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose a non-GX attack to use")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


async def whirlpool_suction(ctx):
    if is_in_active_spot(ctx.source) or not ctx.opponent_bench():
        return
    if not await ctx.ask_yes_no(
            "Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        return
    await opponent_switches(ctx)
    pokemon = ctx.source
    owner = pokemon.owning_player_id or ctx.player_id
    await ctx.discard_cards([c for c in full_stack(pokemon) if c is not pokemon])
    await ctx.put_on_bottom_of_deck(pokemon)


async def swirling_inferno(ctx):
    await ctx.deal_damage()
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        tools = [
            c for c in pokemon.children
            if c.get_attribute(AttrID.TRAINER_TYPE) in (
                TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)
        ]
        if tools:
            await ctx.discard_cards(tools)
        specials = [e for e in ctx.attached_energies(pokemon) if is_special_energy(e)]
        if specials:
            await ctx.discard_cards(specials)


async def tremulous_fist(ctx):
    extra = 30 * sum(1 for p in ctx.my_bench() if _is_damaged_pokemon(p))
    await ctx.deal_damage(_printed(ctx) + extra)


async def sneaky_pocket(ctx):
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, prompt="Put a card from your hand in the Lost Zone")
    if not picks:
        return
    await ctx.move_to_lost_zone(picks)
    await ctx.draw_cards(3)


async def massive_catch_gx(ctx):
    top = list(ctx.deck_top(12))
    if not top:
        return
    basics = [c for c in top if is_basic_pokemon(c)]
    space = BENCH_CAPACITY - len(ctx.my_bench())
    picks = await ctx.choose_cards(
        basics, space, minimum=0, display_cards=top,
        prompt="Choose Basic Pokémon to put onto your Bench",
    ) if basics and space else []
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Trainers
# ----------------------------------------------------------------------

async def _optional_discard_other(ctx, n: int, prompt: str) -> bool:
    others = list(ctx.hand())
    if len(others) < n:
        return False
    if not await ctx.ask_yes_no(prompt):
        return False
    picks = await ctx.choose_cards(others, n, minimum=n, prompt=prompt)
    if len(picks) < n:
        return False
    await ctx.discard_cards(picks)
    return True


async def _discard_bench_down_to(ctx, player_id, n: int):
    bench_area = ctx.board.find_player_area(player_id, "bench")
    bench = list(bench_area.children) if bench_area else []
    while len(bench) > n:
        pick = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to discard", player_id=player_id)
        if pick is None:
            pick = bench[0]
        await ctx.discard_cards(full_stack(pick))
        bench = [p for p in bench if p is not pick]


async def roxie(ctx):
    candidates = [
        c for c in ctx.hand()
        if is_pokemon_card(c) and not is_gx_or_ex(c)
    ]
    picks = await ctx.choose_cards(
        candidates, 2, minimum=0,
        prompt="Discard up to 2 Pokémon that aren't Pokémon-GX or Pokémon-EX")
    await ctx.discard_cards(picks)
    if picks:
        await ctx.draw_cards(3 * len(picks))
    bombs = sum(
        1 for c in picks
        if _logic_name(c) in ("Koffing", "Weezing")
        or _display_name(c) in ("Koffing", "Weezing")
    )
    if bombs:
        async def _bombs():
            for _ in range(bombs):
                await blow_away_bomb(ctx)
        ctx.deferred_actions.append(_bombs)


async def lillies_poke_doll_return(ctx):
    doll = ctx.source
    if doll is not ctx.my_active():
        return
    owner = doll.owning_player_id or ctx.player_id
    await ctx.discard_cards([c for c in full_stack(doll) if c is not doll])
    await ctx.put_on_bottom_of_deck(doll)

    async def _promote():
        await _promote_if_needed(ctx, owner)
    ctx.deferred_actions.append(_promote)


def lillies_poke_doll_ability():
    return Ability(
        "Return",
        "At any time during your turn (before your attack), if this Pokémon is your Active Pokémon, you may discard all cards from it and put it on the bottom of your deck.",
        activation=Activations.ONCE_PER_TURN,
        effect=lillies_poke_doll_return,
        condition=lillies_poke_doll_condition,
    )


async def bellelba_brycen_man(ctx):
    await ctx.discard_cards(ctx.deck_top(3))
    await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))
    if await _optional_discard_other(
            ctx, 3, "Discard 3 other cards to make each player discard down to 3 Benched Pokémon?"):
        await _discard_bench_down_to(ctx, ctx.opponent_id, 3)
        await _discard_bench_down_to(ctx, ctx.player_id, 3)


async def clay(ctx):
    top = list(ctx.deck_top(7))
    await ctx.discard_cards(top)
    items = [c for c in top if is_item_card(c)]
    if items:
        await ctx.put_in_hand(items, reveal=True)


async def cynthia_caitlin(ctx):
    discarded = []
    others = list(ctx.hand())
    if others and await ctx.ask_yes_no(
            "Discard another card from your hand to draw 3 cards?"):
        picks = await ctx.choose_cards(
            others, 1, minimum=1, prompt="Discard another card from your hand")
        discarded = list(picks)
        await ctx.discard_cards(picks)
        await ctx.draw_cards(3)
    supporters = [
        c for c in ctx.discard_pile()
        if is_supporter_card(c)
        and _display_name(c) != "Cynthia & Caitlin"
        and c not in discarded
    ]
    if supporters:
        picks = await ctx.choose_cards(
            supporters, 1,
            prompt="Put a Supporter card from your discard pile into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)


async def erika(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        if await ctx.ask_yes_no("Draw up to 3 cards?", player_id=pid):
            await ctx.draw_cards(3, pid)


async def great_catcher(ctx):
    others = list(ctx.hand())
    picks = await ctx.choose_cards(
        others, 2, minimum=2, prompt="Discard 2 other cards from your hand")
    if len(picks) < 2:
        return
    await ctx.discard_cards(picks)
    pool = [p for p in ctx.opponent_bench() if is_gx_or_ex(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Switch 1 of your opponent's Benched Pokémon-GX or Pokémon-EX")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


def great_catcher_condition(board, player_id, pokemon=None) -> bool:
    if not requires_hand(n=2)(board, player_id, pokemon):
        return False
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    bench = board.find_player_area(opp, "bench")
    return any(is_gx_or_ex(p) for p in (bench.children if bench else []))


async def guzma_hala(ctx):
    extra = await _optional_discard_other(
        ctx, 2, "Discard 2 other cards to also search for a Tool and a Special Energy?")
    stadium = await ctx.search_deck(
        lambda c: c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value,
        count=1, minimum=0, prompt="Choose a Stadium card")
    extra_picks = []
    if extra:
        tool = await ctx.search_deck(
            is_tool_card, count=1, minimum=0, prompt="Choose a Pokémon Tool card")
        special = await ctx.search_deck(
            is_special_energy, count=1, minimum=0, prompt="Choose a Special Energy card")
        extra_picks = tool + special
    await ctx.put_in_hand(stadium + extra_picks, reveal=True)
    await ctx.shuffle_deck()


async def lanas_fishing_rod(ctx):
    pokes = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    tools = [c for c in ctx.discard_pile() if is_tool_card(c)]
    chosen = []
    if pokes:
        picks = await ctx.choose_cards(
            pokes, 1, minimum=0, prompt="Shuffle a Pokémon from your discard pile into your deck")
        chosen.extend(picks)
    tools = [c for c in ctx.discard_pile() if is_tool_card(c) and c not in chosen]
    if tools:
        picks = await ctx.choose_cards(
            tools, 1, minimum=0,
            prompt="Shuffle a Pokémon Tool card from your discard pile into your deck")
        chosen.extend(picks)
    if chosen:
        await ctx.shuffle_into_deck(chosen)


async def lillies_full_force(ctx):
    await ctx.draw_cards(4)
    ctx.session.turn_state.end_of_turn_shuffle_until[ctx.player_id] = 2


async def mallow_lana(ctx):
    extra = await _optional_discard_other(
        ctx, 2, "Discard 2 other cards to heal 120 damage from the Pokémon you move to your Bench?")
    bench = ctx.my_bench()
    active = ctx.my_active()
    if active is None or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Switch your Active Pokémon with 1 of your Benched Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    if extra:
        await ctx.heal(120, active)


async def misty_lorelei(ctx):
    extra = await _optional_discard_other(
        ctx, 5, "Discard 5 other cards so your Water Pokémon can use GX attacks this turn?")
    picks = await ctx.search_deck(
        is_water_energy, count=3, minimum=0,
        prompt="Choose up to 3 Water Energy cards")
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()
    if extra:
        ctx.session.turn_state.gx_unlocked_types.add(PokemonTypes.WATER.value)


async def ns_resolve(ctx):
    top = list(ctx.deck_top(6))
    await ctx.discard_cards(top)
    basics = [c for c in top if is_basic_energy_card(c)]
    dragons = [p for p in ctx.my_bench() if is_dragon_pokemon(p)]
    if not basics or not dragons:
        return
    target = await ctx.choose_pokemon(
        dragons, "Attach the basic Energy to 1 of your Benched Dragon Pokémon")
    if target is None:
        return
    for energy in basics:
        await ctx.attach_energy(energy, target)


async def professor_oaks_setup(ctx):
    used_types = set()
    space = min(3, BENCH_CAPACITY - len(ctx.my_bench()))
    for _ in range(space):
        def pred(card, used=used_types):
            if not is_basic_pokemon(card):
                return False
            types = set(card.get_attribute(AttrID.POKEMON_TYPES) or [])
            return bool(types) and types.isdisjoint(used)
        picks = await ctx.search_deck(
            pred, count=1, minimum=0,
            prompt="Choose a Basic Pokémon of a different type")
        if not picks:
            break
        used_types.update(picks[0].get_attribute(AttrID.POKEMON_TYPES) or [])
        await ctx.bench_pokemon(picks[0])
    await ctx.shuffle_deck()


def professor_oaks_setup_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bench is not None and len(bench.children) < BENCH_CAPACITY


async def red_blue(ctx):
    extra = await _optional_discard_other(
        ctx, 2, "Discard 2 other cards to attach up to 2 basic Energy to the evolved Pokémon?")
    turn = ctx.session.turn_state.turn_number

    def pred(card):
        if not _is_gx_pokemon(card):
            return False
        chain = evolves_from_chain(card.archetype_id)
        if not chain:
            return False
        from_name = chain[0]
        return any(
            _logic_name(p) == from_name
            and ctx.session.turn_state.entered_play_turn.get(p.entity_id, 0) != turn
            for p in ctx.my_pokemon_in_play()
        )

    picks = await ctx.search_deck(
        pred, count=1, minimum=0,
        prompt="Choose a Pokémon-GX that evolves from 1 of your Pokémon")
    evolved = None
    if picks:
        evo = picks[0]
        from_name = evolves_from_chain(evo.archetype_id)[0]
        candidates = [
            p for p in ctx.my_pokemon_in_play()
            if _logic_name(p) == from_name
            and ctx.session.turn_state.entered_play_turn.get(p.entity_id, 0) != turn
        ]
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to evolve") if candidates else None
        if target is not None:
            await ctx.evolve_pokemon(target, evo)
            evolved = evo
    await ctx.shuffle_deck()
    if extra and evolved is not None:
        energies = await ctx.search_deck(
            is_basic_energy_card, count=2, minimum=0,
            prompt="Choose up to 2 basic Energy cards to attach")
        holder = next((p for p in ctx.my_pokemon_in_play() if p is evolved), None)
        if holder is None:
            holder = next(
                (p for p in ctx.my_pokemon_in_play()
                 if _logic_name(p) == _logic_name(evolved)),
                None,
            )
        if energies and holder is not None:
            for energy in energies:
                await ctx.attach_energy(energy, holder)
        await ctx.shuffle_deck()


def red_blue_condition(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number > 2


async def roller_skater(ctx):
    if not ctx.hand():
        return
    picks = await ctx.choose_cards(
        ctx.hand(), 1, prompt="Discard a card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    n = 4 if is_energy_card(picks[0]) else 2
    await ctx.draw_cards(n)


def roller_skater_condition(board, player_id, pokemon=None) -> bool:
    return requires_hand(n=1)(board, player_id, pokemon)


async def rosa(ctx):
    found = []
    for pred, prompt in (
        (is_pokemon_card, "Choose a Pokémon"),
        (is_trainer_card, "Choose a Trainer card"),
        (is_basic_energy_card, "Choose a basic Energy card"),
    ):
        picks = await ctx.search_deck(pred, count=1, minimum=0, prompt=prompt)
        found.extend(picks)
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


async def will(ctx):
    ctx.session.turn_state.will_choose_first_coin.add(ctx.player_id)


async def draw_energy_on_attach(ctx):
    await ctx.draw_cards(1)


async def destructive_drake_gx(ctx):
    basics = [
        e for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e)
    ] if ctx.attacker is not None else []
    await ctx.discard_cards(basics)
    if basics:
        await ctx.deal_damage(80 * len(basics))


def _has_dragon_claw(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and has_attack_titled("Dragon Claw")(pokemon)


DESTRUCTIVE_DRAKE_GX = Attack(
    title="Destructive Drake-GX",
    game_text="Discard all basic Energy from this Pokémon. This attack does 80 damage for each card you discarded in this way. (You can't use more than 1 GX attack in a game.)",
    cost={PokemonTypes.COLORLESS: 3},
    damage=80,
    damage_operator="×",
    effect=destructive_drake_gx,
    condition=_has_dragon_claw,
)


def rosa_condition(board, player_id, pokemon=None) -> bool:
    return ko_last_turn_condition(board, player_id, pokemon)
