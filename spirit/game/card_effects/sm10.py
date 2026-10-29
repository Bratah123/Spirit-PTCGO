"""Unbroken Bonds (SM10) attack, ability, trainer, tool, energy, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import (
    AbilityTypes, AttrID, CLIENT_SPECIAL_CONDITION_NAMES, CardType,
    PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Ability, Activations, Attack, Triggers, def_for, evolves_from,
    is_tag_team, is_ultra_beast, subtypes_for,
)
from spirit.game.models.board import BoardState, EnergyEntity, PokemonEntity
from spirit.game.session.constants import BENCH_CAPACITY
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
    Passive, active_passives, carrier_pokemon, effective_max_hp,
)
from spirit.game.card_effects.attacks_common import (
    _printed,
    active_is,
    bonus_if,
    condition_attack,
    count_discard,
    count_energy,
    count_hand,
    count_in_play,
    count_prizes_remaining,
    damage_counters_on,
    damage_per,
    defender_is_tag_team,
    defender_is_ultra_beast,
    discard_for_bonus,
    discard_random_from_hand,
    flip_damage,
    has_attack_titled,
    has_extra_energy,
    has_tool,
    self_energy_discard_attack,
    snipe_attack,
)
from spirit.game.card_effects.passives_common import (
    ability_lock_passive,
    apply_own_next_turn_boost,
    apply_protection,
    guts_survive_passive,
    is_in_active_spot,
    prevent_damage_when,
    retreat_free_when,
    takes_less_passive,
    team_damage_boost_passive,
)
from spirit.game.card_effects.pokemon import devolve_depth, devolvable, energy_provides_type
from spirit.game.card_effects.sm3 import (
    _return_to_hand,
    is_darkness_energy,
    is_fairy_energy,
    is_fire_energy,
    is_grass_energy,
    is_gx_or_ex,
    is_tool_card,
    is_water_energy,
)
from spirit.game.card_effects.sm4 import is_lightning_pokemon, is_stadium_card, pokemon_has_ability
from spirit.game.card_effects.sm5 import (
    _direct_evolves_from,
    _logic_name,
    evolve_self_from_deck,
    go_second_first_turn,
)
from spirit.game.card_effects.sm6 import used_attack_last_own_turn
from spirit.game.card_effects.sm8 import FairyCharmPassive, is_fairy_pokemon
from spirit.game.card_effects.sm9 import is_darkness_pokemon, is_metal_pokemon, is_psychic_pokemon
from spirit.game.card_effects.sl import is_benched, trickster_gx
from spirit.game.card_effects.support_common import (
    attach_from_discard,
    distribute_energy,
    look_at_top,
    look_top_attach_energy,
    recover_from_discard,
    search_attach_energy,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    deck_nonempty, is_basic_energy_card, is_energy_card, is_metal_energy_card,
    opponent_has_bench,
)


_POISONED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)
_DUSK_STONE_NAMES = {"Mismagius", "Honchkrow", "Chandelure", "Aegislash"}
_RPS = ["Rock", "Paper", "Scissors"]
_RPS_BEATS = {0: 2, 1: 0, 2: 1}


def _display_name(card) -> str:
    return getattr(def_for(getattr(card, "archetype_id", None)), "display_name", "") or ""


def _prize_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _stadium(board):
    area = board.find_global_area("activeStadium")
    return next(iter(area.children), None) if area and area.children else None


def _hand(board, player_id):
    area = board.find_player_area(player_id, "hand")
    return list(area.children) if area else []


def _discard(board, player_id):
    area = board.find_player_area(player_id, "discard")
    return list(area.children) if area else []


def _has_condition(pokemon) -> bool:
    return bool(pokemon and (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))


def is_lightning_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


def is_metal_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.METAL.value)


def is_basic_fighting_energy(card) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIGHTING.value)


def is_ultra_beast_pokemon(card) -> bool:
    return is_ultra_beast(getattr(card, "archetype_id", None))


def is_haunter(card) -> bool:
    return _logic_name(card) == "Haunter" or _display_name(card).startswith("Haunter")


def is_vikavolt(card) -> bool:
    name = _logic_name(card) or _display_name(card)
    return name in ("Vikavolt", "VikavoltGX") or name.startswith("Vikavolt")


def is_dusk_stone_evo(card) -> bool:
    if not is_pokemon_card(card):
        return False
    name = _logic_name(card) or ""
    display = _display_name(card)
    stem = name.replace("GX", "")
    return stem in _DUSK_STONE_NAMES or any(
        display.startswith(n) for n in _DUSK_STONE_NAMES)


def is_darkness_gx_or_ex(card) -> bool:
    return is_gx_or_ex(card) and is_darkness_pokemon(card)


def is_lightning_gx_or_ex(card) -> bool:
    return is_gx_or_ex(card) and is_lightning_pokemon(card)


def _condition_count(ctx) -> int:
    defender = ctx.defender
    if defender is None:
        return 0
    return len(defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def _own_damaged_count(ctx) -> int:
    return sum(
        1 for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    )


def _fairy_energy_pokemon_count(ctx) -> int:
    return sum(
        1 for p in ctx.my_pokemon_in_play()
        if any(is_fairy_energy(e) for e in ctx.attached_energies(p))
    )


def _fight_alone_fewer(ctx) -> int:
    mine = len(ctx.my_pokemon_in_play())
    theirs = len(ctx.opponent_pokemon_in_play())
    return max(0, theirs - mine)


def _more_prizes_than_opp(ctx) -> bool:
    return count_prizes_remaining()(ctx) > count_prizes_remaining("opponent")(ctx)


def _exactly_n_prizes(n):
    def cond(ctx) -> bool:
        return count_prizes_remaining()(ctx) == n
    return cond


def _played_named(name):
    def cond(ctx) -> bool:
        return ctx.played_trainer_this_turn(name) > 0
    return cond


def _own_stadium_in_play(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return False
    owner = stadium.owning_player_id or getattr(stadium, "home_player_id", None)
    return owner == ctx.player_id


def _tool_attached_this_turn(ctx) -> bool:
    attacker = ctx.attacker
    if attacker is None:
        return False
    played = {
        record[0] for record in ctx.session.turn_state.trainers_played
        if record[2] in _TOOL_TYPES
    }
    return any(c.archetype_id in played and is_tool_card(c) for c in attacker.children)


def _evolved_from_this_turn(ctx, logic_name: str) -> bool:
    attacker = ctx.attacker
    if attacker is None:
        return False
    entered = ctx.session.turn_state.entered_play_turn.get(attacker.entity_id)
    if entered != ctx.session.turn_state.turn_number:
        return False
    return any(_logic_name(c) == logic_name for c in attacker.children)


def _named_on_bench(*names):
    def cond(ctx) -> bool:
        present = {_logic_name(p) for p in ctx.my_bench()}
        return set(names) <= present
    return cond


def _fire_energy_in_play(ctx) -> int:
    return count_energy("mine", PokemonTypes.FIRE)(ctx)


def _pokemon_in_discard(ctx) -> int:
    return count_discard(pred=is_pokemon_card)(ctx)


async def _promote_if_needed(ctx, owner, was_active):
    if not was_active:
        return

    async def _promote():
        if not await ctx.session._promote_new_active(owner):
            screen = ctx.session.players[owner].screen_name
            winner = ctx.opponent_id if owner == ctx.player_id else ctx.player_id
            await ctx.session.end_game(winner, f"{screen} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


# ----------------------------------------------------------------------
# Passives
# ----------------------------------------------------------------------

class StealthyBodyPassive(Passive):
    """If any Stadium is in play, this Pokémon has no Weakness."""

    def modify_weakness(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or me is not calc.target:
            return
        if _stadium(calc.board) is None:
            return
        calc.weakness_applies = False


def _playmat(entity):
    node = entity
    while node is not None and getattr(node, "parent", None) is not None:
        node = node.parent
    return node


def _opp_prize_count_from(pokemon) -> int:
    playmat = _playmat(pokemon)
    if playmat is None:
        return 0
    owner = pokemon.owning_player_id
    for child in getattr(playmat, "children", []) or []:
        if getattr(child, "owning_player_id", None) not in (None, owner):
            for area in child.children:
                if area.get_attribute(AttrID.NAME) == "prizePile":
                    return len(area.children)
    return 0


class WallOfStonePassive(Passive):
    """If the opponent has 3 or fewer Prize cards remaining, max HP is 200."""

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        if _opp_prize_count_from(pokemon) > 3:
            return 0
        printed = pokemon.attribute_originals.get(AttrID.HP.value, 120)
        return max(0, 200 - printed)


class RulerOfTheNightPassive(Passive):
    """While Active, the opponent can't play Tools, Special Energy, or Stadiums."""

    def _applies(self, player_id, carrier):
        me = carrier_pokemon(carrier)
        return me is not None and is_in_active_spot(me) and player_id != me.owning_player_id

    def blocks_trainer_play(self, card, player_id, carrier, board=None):
        if not self._applies(player_id, carrier):
            return False
        ttype = card.get_attribute(AttrID.TRAINER_TYPE)
        return ttype in (TrainerType.POKEMON_TOOL.value, TrainerType.STADIUM.value,
                         TrainerType.POKEMON_TOOL_F.value)

    def blocks_energy_attach(self, energy, player_id, target, carrier):
        if not self._applies(player_id, carrier):
            return False
        return is_special_energy(energy)


class GatheringOfCatsPassive(Passive):
    """Ignore Energy in the attack costs of your Pokémon that have Caturday."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return cost
        if not has_attack_titled("Caturday")(pokemon):
            return cost
        return {}


class ForceCancelerPassive(Passive):
    """While Active, prevent damage and effects of the opponent's GX attacks
    done to your Pokémon."""

    def _gx_title(self, title) -> bool:
        return (title or "").rstrip().endswith("GX")

    def prevents_damage(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or not is_in_active_spot(me):
            return False
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target.owning_player_id != me.owning_player_id:
            return False
        return self._gx_title(calc.attack_title)

    def blocks_attack_effects_from(self, target, attacker, carrier):
        me = carrier_pokemon(carrier)
        if me is None or not is_in_active_spot(me):
            return False
        if target.owning_player_id != me.owning_player_id:
            return False
        if attacker is None or attacker.owning_player_id == me.owning_player_id:
            return False
        playmat = _playmat(me)
        for child in getattr(playmat, "children", []) or []:
            ts = getattr(child, "turn_state", None)
            if ts is None:
                continue
            for entity_id, _arch, title in ts.attacks_used:
                if entity_id == attacker.entity_id and self._gx_title(title):
                    return True
        return False


class DustIslandPassive(Passive):
    """Trainer switches of a Poisoned Active keep Poison on the new Active."""

    def keeps_condition_on_trainer_switch(self, pokemon, condition, carrier):
        return condition == _POISONED


class MartialArtsDojoPassive(Passive):
    """Non-Ultra Beast with basic Fighting Energy: +10 to Active, or +40 if more prizes."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or is_ultra_beast(attacker.archetype_id):
            return
        if not any(is_basic_fighting_energy(e) for e in calc.board.attached_energies(attacker)):
            return
        me = attacker.owning_player_id
        opp = _other_player(calc.board, me)
        extra = 40 if opp is not None and _prize_count(calc.board, me) > _prize_count(calc.board, opp) else 10
        calc.amount += extra


class MetalCoreBarrierPassive(Passive):
    """Metal holder takes 70 less from opposing attacks."""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.target:
            return
        if not (calc.is_attack and calc.is_opposing):
            return
        if not is_metal_pokemon(holder):
            return
        calc.amount = max(0, calc.amount - 70)


class BeastBringerPassive(Passive):
    """If you have exactly 6 prizes and the Ultra Beast holder KOs a GX/EX
    Active by attack damage, take 1 more Prize."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or getattr(ctx, "attacker", None) is not holder:
            return count
        if not ctx.is_attack_effect():
            return count
        if not is_ultra_beast(holder.archetype_id):
            return count
        if _prize_count(ctx.board, holder.owning_player_id) != 6:
            return count
        if not is_gx_or_ex(pokemon):
            return count
        if ctx.board.active_pokemon(pokemon.owning_player_id) is not pokemon:
            return count
        return count + 1


class UndergroundWorkPassive(Passive):
    """Marker: Giovanni's Exile mills 1 from the opponent's deck."""

    mills_on_giovannis_exile = True


class FairyCharmAbilityPassive(Passive):
    """Prevent damage from opposing GX/EX that have Abilities, to a Fairy holder."""

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
        return pokemon_has_ability(attacker)


class StealthyHoodPassive(Passive):
    """Prevent effects of the opponent's Abilities done to the holder."""

    def blocks_ability_effects(self, target, carrier):
        return target is carrier_pokemon(carrier)


class FullMetalWallPassive(Passive):
    """Your Metal Pokémon take 30 less from opposing attacks for the rest of the game."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        owner = getattr(carrier, "owning_player_id", None)
        if calc.target.owning_player_id != owner:
            return
        if not is_metal_pokemon(calc.target):
            return
        calc.amount = max(0, calc.amount - 30)


class LtSurgePassive(Passive):
    """Play 3 Supporters this turn (including Lt. Surge's Strategy)."""

    def supporter_limit(self, player_id, carrier):
        owner = getattr(carrier, "owning_player_id", None)
        return 3 if player_id == owner else 1


hair_wall_passive = takes_less_passive(
    10,
    protects=lambda target, carrier: (
        target.owning_player_id == carrier.owning_player_id
        and is_metal_pokemon(target)
    ),
)

strong_cheer_passive = team_damage_boost_passive(
    30, once_key="Strong Cheer", to_active_only=True)

bench_barrier_passive = prevent_damage_when(
    lambda calc, carrier: (
        calc.is_attack and calc.is_opposing
        and calc.target.owning_player_id == carrier.owning_player_id
        and is_benched(calc.target)
    )
)

intimidating_fang_passive = takes_less_passive(
    20,
    protects=lambda target, carrier: (
        is_in_active_spot(carrier)
        and target.owning_player_id != carrier.owning_player_id
        and is_in_active_spot(target)
    ),
)

# Free Flight: no Energy attached => no Retreat Cost.
free_flight_passive = retreat_free_when(
    lambda pokemon, carrier: (
        carrier_pokemon(carrier) is pokemon
        and not any(is_energy_card(c) for c in pokemon.children)
    )
)

stealthy_body_passive = StealthyBodyPassive()
wall_of_stone_passive = WallOfStonePassive()
ruler_of_the_night_passive = RulerOfTheNightPassive()
gathering_of_cats_passive = GatheringOfCatsPassive()
force_canceler_passive = ForceCancelerPassive()
dust_island_passive = DustIslandPassive()
martial_arts_dojo_passive = MartialArtsDojoPassive()
metal_core_barrier_passive = MetalCoreBarrierPassive()
beast_bringer_passive = BeastBringerPassive()
fairy_charm_ability_passive = FairyCharmAbilityPassive()
fairy_charm_lightning_passive = FairyCharmPassive(PokemonTypes.LIGHTNING)
stealthy_hood_passive = StealthyHoodPassive()
power_plant_passive = ability_lock_passive(lambda p, c: is_gx_or_ex(p))
underground_work_passive = UndergroundWorkPassive()


# ----------------------------------------------------------------------
# Ability effects
# ----------------------------------------------------------------------

async def flip_evolve_from_deck(ctx):
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "Evolve")
    if results and results[0]:
        await evolve_self_from_deck(ctx)


def flip_evolve_condition(board, player_id, pokemon=None) -> bool:
    return deck_nonempty(board, player_id)


async def irresistible_aroma(ctx):
    if len(ctx.opponent_bench()) >= BENCH_CAPACITY:
        return
    results = await ctx.flip_coins(1, "Irresistible Aroma")
    if not results or not results[0]:
        return
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    basics = [c for c in cards if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(
        basics, 1, prompt="Put a Basic Pokémon onto your opponent's Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])


def irresistible_aroma_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    bench = board.find_player_area(opp, "bench")
    if bench is None or len(bench.children) >= BENCH_CAPACITY:
        return False
    hand = board.find_player_area(opp, "hand")
    return bool(hand and hand.children)


async def varied_pollen(ctx):
    results = await ctx.flip_coins(1, "Varied Pollen")
    if not results or not results[0]:
        return
    options = ["Asleep", "Burned", "Confused", "Poisoned"]
    mapping = {
        0: SpecialConditions.ASLEEP,
        1: SpecialConditions.BURNED,
        2: SpecialConditions.CONFUSED,
        3: SpecialConditions.POISONED,
    }
    idx = await ctx.choose("Choose a Special Condition", options)
    if idx is None:
        return
    defender = ctx.opponent_active()
    if defender is not None:
        await ctx.apply_special_condition(defender, mapping[idx])


async def roast_reveal(ctx):
    fires = [c for c in ctx.hand() if is_fire_energy(c)]
    if not fires:
        return
    picks = await ctx.choose_cards(fires, 1, prompt="Discard a Fire Energy card")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.draw_cards(3)


def roast_reveal_condition(board, player_id, pokemon=None) -> bool:
    return any(is_fire_energy(c) for c in _hand(board, player_id))


async def round_n_round(ctx):
    defender = ctx.opponent_active()
    if defender is not None:
        await ctx.apply_special_condition(defender, SpecialConditions.CONFUSED)


async def dedechange(ctx):
    if not await ctx.ask_yes_no("Discard your hand and draw 6 cards?"):
        return
    await ctx.discard_cards(list(ctx.hand()))
    await ctx.draw_cards(6)


async def battery(ctx):
    holders = [p for p in ctx.my_pokemon_in_play() if is_vikavolt(p)]
    if not holders:
        return
    target = await ctx.choose_pokemon(
        holders, "Choose a Vikavolt or Vikavolt-GX to attach this as Energy")
    if target is None:
        return
    source = ctx.source
    BoardState.masquerade_as(
        source, EnergyEntity,
        {
            AttrID.CARD_TYPE.value: CardType.ENERGY.value,
            AttrID.ENERGY_INFO.value: {
                "options": [[PokemonTypes.LIGHTNING.value, PokemonTypes.LIGHTNING.value]],
            },
            AttrID.IS_SPECIAL_ENERGY.value: True,
        },
    )
    await ctx.attach_energy(source, target)


def battery_condition(board, player_id, pokemon=None) -> bool:
    return any(is_vikavolt(p) for p in board.pokemon_in_play(player_id))


async def swelling_spite(ctx):
    space = BENCH_CAPACITY - len(ctx.my_bench())
    if space <= 0:
        return
    picks = await ctx.search_deck(
        is_haunter, count=min(2, space), minimum=0,
        prompt="Choose up to 2 Haunter to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def shadow_pain(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if is_gx_or_ex(p)]
    if not pool:
        return
    if not await ctx.ask_yes_no(
            "Put 6 damage counters on your opponent's Pokémon-GX and Pokémon-EX?"):
        return
    await ctx.place_damage_counters(6, pool)


async def hypnotic_pendulum(ctx):
    if not getattr(ctx, "was_active_at_ko", False):
        return
    results = await ctx.flip_coins(1, "Hypnotic Pendulum")
    if results and results[0]:
        owner = ctx.ko_pokemon.owning_player_id if getattr(ctx, "ko_pokemon", None) else ctx.opponent_id
        ctx.session.turn_state.promotion_chooser[owner] = ctx.player_id


async def detention_gas(ctx):
    if not is_in_active_spot(ctx.source):
        return
    for pokemon in ctx.opponent_pokemon_in_play():
        if is_basic_pokemon(pokemon):
            await ctx.deal_damage(10, target=pokemon, as_counters=True)


async def mind_report(ctx):
    if not await ctx.ask_yes_no(
            "Put a Supporter card from your discard pile on top of your deck?"):
        return
    cards = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, prompt="Choose a Supporter card")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


async def mysterious_message(ctx):
    before = ctx.hand_size()
    await ctx.draw_until(7)
    if ctx.hand_size() > before:
        await ctx.knock_out(ctx.source)


def mysterious_message_condition(board, player_id, pokemon=None) -> bool:
    return len(_hand(board, player_id)) < 7 and deck_nonempty(board, player_id)


async def resetting_hole(ctx):
    if not is_benched(ctx.source):
        return
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return
    await ctx.discard_stadium()
    await ctx.discard_cards(full_stack(ctx.source))


def resetting_hole_condition(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_benched(pokemon) and _stadium(board) is not None


async def bratty_kick(ctx):
    results = await ctx.flip_coins(1, "Bratty Kick")
    if results and results[0]:
        pool = ctx.opponent_pokemon_in_play()
        if pool:
            target = await ctx.choose_pokemon(pool, "Choose a Pokémon")
            if target is not None:
                await ctx.deal_damage(30, target=target, as_counters=True)


async def building_spite(ctx):
    await ctx.deal_damage(10, target=ctx.source, as_counters=True)


async def metal_eater(ctx):
    metals = [c for c in ctx.hand() if is_metal_pokemon(c)]
    if not metals:
        return
    picks = await ctx.choose_cards(metals, 1, prompt="Discard a Metal Pokémon")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.heal(100, ctx.source)


def metal_eater_condition(board, player_id, pokemon=None) -> bool:
    return any(is_metal_pokemon(c) for c in _hand(board, player_id))


async def excitable_draw(ctx):
    results = await ctx.flip_coins(1, "Excitable Draw")
    if results and results[0]:
        await ctx.shuffle_into_deck(list(ctx.hand()), ctx.player_id)
        await ctx.draw_cards(6)


async def fairy_feast(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if is_fairy_pokemon(pokemon):
            await ctx.heal(30, pokemon)


async def cat_walk(ctx):
    picks = await ctx.search_deck(
        None, count=2, minimum=0, prompt="Choose up to 2 cards.")
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


def cat_walk_condition(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    for ko in ts.kos_by_attack_last_turn.get(player_id, []):
        subs = ko.get("subtypes") or []
        if "GX" in subs or "EX" in subs:
            return True
    return False


async def crazy_code(ctx):
    cards = [c for c in ctx.hand() if is_special_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Choose a Special Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Special Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


def crazy_code_condition(board, player_id, pokemon=None) -> bool:
    return any(is_special_energy(c) for c in _hand(board, player_id))


async def lazy_eating(ctx):
    await ctx.heal(10, ctx.source)


async def playhouse_heal(ctx):
    results = await ctx.flip_coins(1, "Playhouse Heal")
    if not results or not results[0]:
        return
    damaged = [
        p for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal")
    if target is not None:
        await ctx.heal(60, target)


async def greedy_evolution(ctx):
    if not await ctx.ask_yes_no(
            "Look at the top 6 cards of your deck and attach Darkness Energy?"):
        return
    await look_top_attach_energy(
        6, predicate=is_darkness_energy, rest="shuffle",
        target_pred=lambda p: p is ctx.source, distribute=False,
    )(ctx)


# ----------------------------------------------------------------------
# Attack effects
# ----------------------------------------------------------------------

async def elegant_sole(ctx):
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, -130, attack_title="Elegant Sole")


async def beast_game_gx(ctx):
    ctx.extra_prizes += 3 if has_extra_energy(7)(ctx) else 1
    await ctx.deal_damage()


async def assassin_flight(ctx):
    await snipe_attack(90)(ctx)


def assassin_flight_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    active = board.active_pokemon(opp)
    return _has_condition(active) and opponent_has_bench(board, player_id)


async def shinobi_mastery(ctx):
    extra = 90 if ctx.played_trainer_this_turn("Koga's Trap") else 0
    await ctx.deal_damage(_printed(ctx) + extra)
    if ctx.played_trainer_this_turn("Janine"):
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            prevent_damage_when(
                lambda calc, carrier: (
                    calc.is_attack and calc.is_opposing
                    and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None
                    and is_basic_pokemon(calc.attacker)
                )
            ),
        )


async def gastro_acid(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.add_passive_through_own_next_turn(
            defender, ability_lock_passive(lambda p, c: p is c))


async def chlorowhip(ctx):
    await ctx.deal_damage()
    if count_energy("self", PokemonTypes.GRASS)(ctx) >= 2:
        await ctx.heal(60, ctx.attacker)


async def false_swipe(ctx):
    results = await ctx.flip_coins(1, "False Swipe")
    if not results or not results[0]:
        return
    target = ctx.defender
    if target is None:
        return
    amount = target.get_attribute(AttrID.HP, 0) - 10
    if amount > 0:
        await ctx.deal_damage(amount, target=target, as_counters=True)


async def double_blaze_gx(ctx):
    extra = has_extra_energy(3, PokemonTypes.FIRE)(ctx)
    if extra:
        await ctx.deal_damage(_printed(ctx) + 100, ignore_target_effects=True)
    else:
        await ctx.deal_damage()


async def grand_flame(ctx):
    await ctx.deal_damage()
    await attach_from_discard(
        is_fire_energy, count=2, target=is_benched, minimum=0,
        prompt="Choose up to 2 Fire Energy cards to attach.",
    )(ctx)


async def flare_starter(ctx):
    n = 3 if go_second_first_turn(ctx.board, ctx.player_id) else 1
    await search_attach_energy(
        is_fire_energy, count=n, distribute=True,
        prompt="Choose Fire Energy cards to attach.",
    )(ctx)


def caturday(n):
    async def effect(ctx):
        before = ctx.hand_size()
        await ctx.draw_cards(n)
        if ctx.hand_size() > before:
            await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    return effect


caturday_1 = caturday(1)
caturday_2 = caturday(2)


async def blazer(ctx):
    extra = 0
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    from spirit.game.models.board import CardEntity
    prizes = [
        c for c in (area.children if area else [])
        if isinstance(c, CardEntity) and not c.face_up_prize
    ]
    if prizes:
        idx = await ctx.choose(
            "Turn which Prize card face up?",
            [str(i + 1) for i in range(len(prizes))],
        ) if len(prizes) > 1 else 0
        card = prizes[idx or 0]
        card.face_up_prize = True
        await ctx.flush_choreography()
        from spirit.game.attributes import GameSequence
        await ctx.session.send_game_sequence(
            list(ctx.session.players.values()), GameSequence.GROUPED_MOVE,
            [ctx.session._entity_introduced_msg(card)],
        )
        if is_fire_energy(card):
            extra = 50
    await ctx.deal_damage(_printed(ctx) + extra)


async def giant_geyser_gx(ctx):
    waters = [c for c in ctx.hand() if is_water_energy(c)]
    if waters and ctx.my_pokemon_in_play():
        picks = await ctx.choose_cards(
            waters, len(waters), minimum=0,
            prompt="Attach any number of Water Energy cards")
        if picks:
            await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


async def rocket_splash(ctx):
    pool = [
        e for p in ctx.my_pokemon_in_play()
        for e in ctx.attached_energies(p) if is_water_energy(e)
    ]
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Shuffle Water Energy into your deck") if pool else []
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)
    amount = 60 * len(picks)
    if amount:
        await ctx.deal_damage(amount)


async def wicked_tentacles(ctx):
    dests = ctx.opponent_pokemon_in_play()
    sources = [p for p in dests if ctx.attached_energies(p)]
    if len(dests) < 2 or not sources:
        return
    moved = await ctx.move_energy_freely(sources, dests, max_count=1)
    if moved:
        _, dest = moved[0]
        await ctx.deal_damage(30, target=dest, as_counters=True)


async def three_strikes(ctx):
    results = await ctx.flip_coins(3, "Three Strikes")
    heads = sum(1 for r in results if r)
    if heads == 0:
        screen = ctx.session.players[ctx.player_id].screen_name
        await ctx.session.end_game(
            ctx.opponent_id, f"{screen} lost to Three Strikes")
        return
    await ctx.deal_damage(100 * heads)


async def dual_blizzard(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 2, prompt="Choose 2 Energy to discard")
    await snipe_attack(60, pool="any", count=2)(ctx)


async def enhanced_horn(ctx):
    coins = 6 if ctx.attacker is not None and has_tool(ctx.attacker) else 2
    await flip_damage(coins=coins, per_heads=30)(ctx)


async def hail_prison(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 2, predicate=is_water_energy,
        prompt="Choose 2 Water Energy to discard")
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


async def surprise_fist(ctx):
    extra = 0
    mine = await ctx.choose("Rock-Paper-Scissors", _RPS)
    theirs = await ctx.choose(
        "Rock-Paper-Scissors", _RPS, player_id=ctx.opponent_id)
    if mine is not None and theirs is not None and _RPS_BEATS.get(mine) == theirs:
        extra = 60
    await ctx.deal_damage(_printed(ctx) + extra)


async def never_give_up(ctx):
    cards = [c for c in ctx.discard_pile() if is_lightning_energy(c)]
    if not cards or not ctx.my_pokemon_in_play():
        return
    picks = await ctx.choose_cards(
        cards, len(cards), minimum=0,
        prompt="Attach Lightning Energy cards from your discard pile.")
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


def never_give_up_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    return _prize_count(board, player_id) >= _prize_count(board, opp) + 3


async def raging_thunder(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(10, target=target, apply_modifiers=False)


async def tingly_return_gx(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    await _return_to_hand(ctx, ctx.attacker, with_attachments=True)


async def electricannon(ctx):
    lightning = [
        e for e in ctx.attached_energies(ctx.attacker) if is_lightning_energy(e)]
    extra = 0
    if lightning and await ctx.ask_yes_no(
            "Discard all Lightning Energy from this Pokémon? If you do, this attack does 100 more damage."):
        await ctx.discard_cards(lightning)
        extra = 100
    await ctx.deal_damage(_printed(ctx) + extra)


async def discharge(ctx):
    lightning = [
        e for e in ctx.attached_energies(ctx.attacker) if is_lightning_energy(e)]
    await ctx.discard_cards(lightning)
    amount = 50 * len(lightning)
    if amount:
        await ctx.deal_damage(amount)


async def nasty_goo_mix_gx(ctx):
    defender = ctx.defender
    extra = has_extra_energy(4)(ctx)
    counters = 15 if extra else 1
    if defender is not None:
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
        await ctx.apply_special_condition(
            defender, SpecialConditions.POISONED, poison_counters=counters)


async def poison_absorption(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and _POISONED in (
            defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        await ctx.heal(100, ctx.attacker)


async def sinister_fog(ctx):
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(10, target=pokemon, as_counters=True)


async def acme_of_heroism_gx(ctx):
    await ctx.deal_damage()
    if has_extra_energy(1)(ctx):
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            guts_survive_passive(
                hp_floor=10, title="Acme of Heroism-GX", flip=False),
        )


async def focus_energy(ctx):
    await apply_own_next_turn_boost(ctx, 70, attack_title="Beat")


async def dirty_work(ctx):
    n = 5 if ctx.played_trainer_this_turn("Giovanni's Exile") else 1
    await ctx.discard_cards(ctx.deck_top(n, player_id=ctx.opponent_id))


async def finishing_combo(ctx):
    for pokemon in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(60, target=pokemon)


def finishing_combo_condition(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    titles = ts.attack_titles_prev_turn_by_player.get(player_id) or []
    return "Special Combo" in titles


async def dark_union_gx(ctx):
    extra = has_extra_energy(1)(ctx)
    space = BENCH_CAPACITY - len(ctx.my_bench())
    cards = [c for c in ctx.discard_pile() if is_darkness_gx_or_ex(c)]
    take = min(2, space)
    if take <= 0 or not cards:
        return
    picks = await ctx.choose_cards(
        cards, take, minimum=0,
        prompt="Choose Darkness Pokémon-GX or Pokémon-EX to bench")
    benched = []
    for card in picks:
        if await ctx.bench_pokemon(card):
            benched.append(card)
    if extra and benched:
        energies = [c for c in ctx.discard_pile() if is_energy_card(c)]
        for pokemon in benched:
            if not energies:
                break
            chosen = await ctx.choose_cards(
                energies, min(2, len(energies)), minimum=0,
                prompt=f"Attach up to 2 Energy cards to {_display_name(pokemon)}")
            for energy in chosen:
                await ctx.attach_energy(energy, pokemon)
                if energy in energies:
                    energies.remove(energy)


async def unfair_gx(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    if not cards:
        return
    n = min(2, len(cards))
    picks = await ctx.choose_cards(cards, n, prompt="Discard 2 cards from that hand")
    if picks:
        await ctx.discard_cards(picks)


async def grandiose_fangs(ctx):
    defender = ctx.defender
    await ctx.deal_damage()
    if defender is not None and defender in ctx.knockouts:
        await apply_own_next_turn_boost(ctx, 120)


async def bring_down(ctx):
    others = [
        p for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        if p is not ctx.attacker
    ]
    if not others:
        return
    lowest = min(p.get_attribute(AttrID.HP, 0) for p in others)
    tied = [p for p in others if p.get_attribute(AttrID.HP, 0) == lowest]
    target = tied[0]
    if len(tied) > 1:
        target = await ctx.choose_pokemon(tied, "Choose a Pokémon to Knock Out") or tied[0]
    await ctx.knock_out(target)


async def hypnotic_reign(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    pokes = [c for c in cards if is_pokemon_card(c)]
    if not pokes:
        return
    picks = await ctx.choose_cards(
        pokes, 1, minimum=0, prompt="Discard a Pokémon you find there")
    if not picks:
        return
    await ctx.discard_cards(picks)
    definition = def_for(picks[0].archetype_id)
    candidates = []
    for ability in getattr(definition, "abilities", None) or []:
        if not isinstance(ability, Attack):
            continue
        if (ability.title or "").rstrip().endswith("GX"):
            continue
        candidates.append((picks[0], ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


async def full_metal_wall_gx(ctx):
    ctx.add_global_passive(FullMetalWallPassive(), expires_after_turn=10 ** 9)
    extra = has_extra_energy(1)(ctx)
    if extra and ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await ctx.discard_energy_from(
            ctx.defender, 99, prompt="Discard all Energy from the Defending Pokémon")


async def kaleidostorm(ctx):
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    if len(mine) >= 2:
        await ctx.move_energy_freely(mine, mine)


async def magical_miracle_gx(ctx):
    await ctx.deal_damage()
    if has_extra_energy(3, PokemonTypes.FAIRY)(ctx):
        await ctx.shuffle_into_deck(list(ctx.hand(ctx.opponent_id)), ctx.opponent_id)


async def energy_present(ctx):
    energies = [c for c in ctx.hand() if is_energy_card(c)]
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy card")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def pungent_aroma(ctx):
    results = await ctx.flip_coins(2, "Pungent Aroma")
    heads = sum(1 for r in results if r)
    if not heads:
        return
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    if not cards:
        return
    n = min(heads, len(cards))
    picks = await ctx.choose_cards(
        cards, n, prompt="Choose cards to shuffle into the deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def escaping_incisors(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or not is_evolution_pokemon(defender):
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def drill_run_double(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Drill Run Double")
    if results and results[0] and ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await ctx.discard_energy_from(
            ctx.defender, 2, prompt="Choose 2 Energy to discard")


async def eat_up(ctx):
    defender = ctx.defender
    discarded = False
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [c for c in list(defender.children) if is_tool_card(c)]
        if tools:
            await ctx.discard_cards(tools)
            discarded = True
    await ctx.deal_damage()
    if discarded and ctx.attacker is not None:
        await ctx.heal(ctx.max_hp(ctx.attacker), ctx.attacker)


async def digicharge(ctx):
    results = await ctx.flip_coins(3, "Digicharge")
    heads = sum(1 for r in results if r)
    if heads:
        await search_to_hand(
            is_energy_card, count=heads, reveal=True,
            prompt="Choose Energy cards.",
        )(ctx)


async def stray_cat_dash(ctx):
    await ctx.deal_damage()
    n = 2 if _evolved_from_this_turn(ctx, "Glameow") else 1
    await discard_random_from_hand(ctx, ctx.opponent_id, n)


async def discovery_gx(ctx):
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(area.children) if area else []
    n = len(prizes)
    if n == 0:
        return
    top = list(ctx.deck_top(n))
    if len(top) < n:
        return
    await ctx.put_in_hand(prizes, reveal=False)
    await ctx.put_in_prizes(top)


async def top_down(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails("Top Down")
    if heads > 0:
        await ctx.discard_cards(ctx.deck_top(heads, player_id=ctx.opponent_id))


# Factories / aliases
radar_eyes = look_at_top(7, take=1, rest="shuffle", minimum=0)
electrical_signal = search_to_hand(
    is_lightning_pokemon, count=2, reveal=True,
    prompt="Choose up to 2 Lightning Pokémon.",
)
find_wildfire = search_to_hand(
    is_fire_energy, count=3, reveal=True,
    prompt="Choose up to 3 Fire Energy cards.",
)
fireball_circus = discard_for_bonus(
    source="hand", predicate=is_fire_energy, max_count=99, per=50, base=0,
    prompt="Discard any number of Fire Energy cards from your hand.",
)
reactive_poison = damage_per(_condition_count, 60, base=10)
big_cut = bonus_if(_exactly_n_prizes(4), 120)
high_heat_blast = bonus_if(lambda ctx: _fire_energy_in_play(ctx) >= 4, 60)
swirly_rush = bonus_if(_named_on_bench("Poliwag", "Poliwhirl"), 90)
bubble_jutsu = bonus_if(_played_named("Janine"), 50)
electric_trap = damage_per(_own_damaged_count, 30)
heavy_choke = bonus_if(used_attack_last_own_turn("Wrap"), 120)
red_knuckles = bonus_if(defender_is_ultra_beast, 60)
home_ground = bonus_if(_own_stadium_in_play, 60)
assault_boom = bonus_if(lambda ctx: ctx.defender is not None and has_tool(ctx.defender), 70)
bone_rush = flip_damage(until_tails=True, per_heads=50)
shinobi_strike = bonus_if(_played_named("Janine"), 90)
knuckle_blast = bonus_if(_more_prizes_than_opp, 60)
feather_storm = snipe_attack(30, pool=is_gx_or_ex, count=2)
steel_fist = search_attach_energy(is_metal_energy, count=1, to_self=True)
rush_up = bonus_if(_tool_attached_this_turn, 70)
splitting_beam = snipe_attack(30, count=2, also_base=True)
steel_melt = bonus_if(active_is(is_metal_pokemon), 40)
fairy_song = search_attach_energy(
    is_fairy_energy, count=2, target_pred=is_benched, distribute=True,
    prompt="Choose up to 2 Fairy Energy cards to attach to Benched Pokémon.",
)
orb_polish = recover_from_discard(
    is_energy_card, count=3, minimum=0,
    prompt="Choose up to 3 Energy cards.",
)
energy_blow = damage_per(count_energy("self"), 30, base=10)
big_counter = bonus_if(defender_is_tag_team, 120)
boing_boing_tail = snipe_attack(60, pool=is_gx_or_ex, count=1)
severe_poison_eight = condition_attack(SpecialConditions.POISONED, counters=8)


def _with_printed(count_fn, per, cap=None):
    async def effect(ctx):
        amount = _printed(ctx) + per * max(0, count_fn(ctx))
        if cap is not None:
            amount = min(amount, cap)
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


stir_the_brain = _with_printed(count_hand("opponent"), 10)
fight_alone = _with_printed(_fight_alone_fewer, 50)
dark_pulse = _with_printed(count_energy("mine", PokemonTypes.DARKNESS), 30)
bad_fangs = _with_printed(count_energy("self", PokemonTypes.DARKNESS), 20)
anguish_cry = _with_printed(damage_counters_on(), 30)
moon_watching_dance = _with_printed(_fairy_energy_pokemon_count, 30)


async def vengeance(ctx):
    extra = min(180, 20 * _pokemon_in_discard(ctx))
    await ctx.deal_damage(_printed(ctx) + extra)


async def splattering_sludge(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.opponent_bench():
        if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon):
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


# ----------------------------------------------------------------------
# Trainers
# ----------------------------------------------------------------------

async def chip_chip_ice_axe(ctx):
    top = list(ctx.deck_top(3, player_id=ctx.opponent_id))
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, prompt="Choose a card to put on top of your opponent's deck")
    if picks:
        await ctx.shuffle_deck_below(picks[0])


async def devolution_spray_z(ctx):
    evolved = [p for p in ctx.my_pokemon_in_play() if devolvable(p)]
    if not evolved:
        return
    target = await ctx.choose_pokemon(evolved, "Choose an evolved Pokémon")
    if target is None:
        return
    depth = devolve_depth(target)
    if depth <= 0:
        return
    if depth == 1:
        steps = 1
    else:
        options = [str(i) for i in range(1, depth + 1)]
        idx = await ctx.choose("How many Evolution cards to shuffle in?", options)
        steps = (idx or 0) + 1
    await ctx.devolve_pokemon(target, steps=steps, destination="deck")
    remaining = ctx.board.get_entity(target.entity_id) or target
    ctx.session.turn_state.mark_entered_play(
        remaining.entity_id if remaining is not None else target.entity_id)
    await ctx.shuffle_deck()


def devolution_spray_z_condition(board, player_id) -> bool:
    return any(devolvable(p) for p in board.pokemon_in_play(player_id))


async def dusk_stone(ctx):
    in_play = ctx.my_pokemon_in_play()
    if not in_play:
        return
    names = {_logic_name(p) for p in in_play}
    picks = await ctx.search_deck(
        lambda c: is_dusk_stone_evo(c) and any(
            evolves_from(c.archetype_id, n) for n in names),
        count=1, minimum=0,
        prompt="Choose a Mismagius, Honchkrow, Chandelure, or Aegislash.",
    )
    if not picks:
        await ctx.shuffle_deck()
        return
    evo = picks[0]
    holders = [
        p for p in in_play
        if evolves_from(evo.archetype_id, _logic_name(p))
    ]
    target = holders[0]
    if len(holders) > 1:
        target = await ctx.choose_pokemon(
            holders, "Choose a Pokémon to evolve") or holders[0]
    await ctx.evolve_pokemon(target, evo)
    await ctx.shuffle_deck()


def dusk_stone_condition(board, player_id) -> bool:
    return deck_nonempty(board, player_id) and bool(board.pokemon_in_play(player_id))


async def electromagnetic_radar(ctx):
    discarded = await ctx.discard_from_hand(
        2, minimum=2, prompt="Discard 2 other cards from your hand")
    if len(discarded) < 2:
        return
    await search_to_hand(
        is_lightning_gx_or_ex, count=2, reveal=True,
        prompt="Choose Lightning Pokémon-GX and Pokémon-EX.",
    )(ctx)


def electromagnetic_radar_condition(board, player_id) -> bool:
    return len(_hand(board, player_id)) >= 3 and deck_nonempty(board, player_id)


fire_crystal = recover_from_discard(
    is_fire_energy, count=3, minimum=0,
    prompt="Choose up to 3 Fire Energy cards.",
)


def giovannis_exile_condition(board, player_id) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if bench is None:
        return False
    return any(
        isinstance(p, PokemonEntity)
        and p.get_attribute(AttrID.HP, 0) >= effective_max_hp(board, p)
        for p in bench.children
    )


async def giovannis_exile(ctx):
    undamaged = [
        p for p in ctx.my_bench()
        if p.get_attribute(AttrID.HP, 0) >= ctx.max_hp(p)
    ]
    if not undamaged:
        return
    picks = await ctx.choose_cards(
        undamaged, min(2, len(undamaged)), minimum=0,
        prompt="Discard up to 2 of your undamaged Benched Pokémon")
    mill = 0
    for pokemon in picks:
        if any(getattr(p, "mills_on_giovannis_exile", False)
               for p, c in active_passives(ctx.board)
               if carrier_pokemon(c) is pokemon):
            mill += 1
        await ctx.discard_cards(full_stack(pokemon))
    if mill:
        await ctx.discard_cards(ctx.deck_top(mill, player_id=ctx.opponent_id))


def greens_exploration_condition(board, player_id) -> bool:
    return (
        not any(pokemon_has_ability(p) for p in board.pokemon_in_play(player_id))
        and deck_nonempty(board, player_id)
    )


greens_exploration = search_to_hand(
    is_trainer_card, count=2, reveal=True,
    prompt="Choose up to 2 Trainer cards.",
)

janine = look_at_top(4, take=2, rest="shuffle")

kogas_trap = condition_attack(
    SpecialConditions.CONFUSED, SpecialConditions.POISONED, damage=0)


async def lt_surges_strategy(ctx):
    ctx.add_global_passive(
        LtSurgePassive(), expires_after_turn=ctx.session.turn_state.turn_number)


def lt_surges_strategy_condition(board, player_id) -> bool:
    opp = _other_player(board, player_id)
    return opp is not None and _prize_count(board, player_id) > _prize_count(board, opp)


async def metal_core_barrier_discard(ctx):
    if ctx.session.turn_state.active_player_id == ctx.player_id:
        return
    holder = ctx.source
    tools = [
        c for c in holder.children
        if _display_name(c) == "Metal Core Barrier"
    ]
    if tools:
        await ctx.discard_cards(tools)


METAL_CORE_BARRIER_ABILITY = Ability(
    title="Metal Core Barrier",
    game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn.",
    trigger=Triggers.BETWEEN_TURNS,
    effect=metal_core_barrier_discard,
)


async def molayne(ctx):
    metals = [c for c in ctx.hand() if is_metal_energy_card(c) or is_metal_energy(c)]
    if len(metals) < 2:
        return
    cost = await ctx.choose_cards(
        metals, 2, prompt="Discard 2 Metal Energy cards from your hand")
    if len(cost) < 2:
        return
    await ctx.discard_cards(cost)
    trainers = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, prompt="Shuffle a Trainer card into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


def molayne_condition(board, player_id) -> bool:
    metals = [c for c in _hand(board, player_id)
              if is_metal_energy_card(c) or is_metal_energy(c)]
    trainers = [c for c in _discard(board, player_id) if is_trainer_card(c)]
    return len(metals) >= 2 and bool(trainers)


pokegear_30 = look_at_top(
    7, take=1, predicate=is_supporter_card, rest="shuffle", minimum=0,
    prompt="You may reveal a Supporter card.",
)


async def reds_challenge(ctx):
    discarded = await ctx.discard_from_hand(
        2, minimum=2, prompt="Discard 2 other cards from your hand")
    if len(discarded) < 2:
        return
    await search_to_hand(None, count=1, reveal=False, prompt="Choose a card.")(ctx)


def reds_challenge_condition(board, player_id) -> bool:
    return len(_hand(board, player_id)) >= 3 and deck_nonempty(board, player_id)


async def samson_oak(ctx):
    await ctx.draw_cards(2)
    mine = ctx.my_active()
    theirs = ctx.opponent_active()
    if mine is None or theirs is None:
        return
    my_types = set(mine.get_attribute(AttrID.POKEMON_TYPES) or [])
    their_types = set(theirs.get_attribute(AttrID.POKEMON_TYPES) or [])
    if my_types & their_types:
        await ctx.draw_cards(2)


async def surprise_box(ctx):
    cards = list(ctx.discard_pile(ctx.opponent_id))
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Put a card into your opponent's hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


def surprise_box_condition(board, player_id) -> bool:
    opp = _other_player(board, player_id)
    return bool(opp and _discard(board, opp))


async def ultra_forest_kartenvoy(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if is_ultra_beast(pokemon.archetype_id):
            ctx.ignore_own_target_effects(pokemon)


def ultra_forest_kartenvoy_condition(board, player_id) -> bool:
    return any(is_ultra_beast(p.archetype_id) for p in board.pokemon_in_play(player_id))


async def welder(ctx):
    fires = [c for c in ctx.hand() if is_fire_energy(c)]
    if not fires or not ctx.my_pokemon_in_play():
        return
    picks = await ctx.choose_cards(
        fires, min(2, len(fires)), minimum=0,
        prompt="Attach up to 2 Fire Energy cards")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Fire Energy to")
    if target is None:
        return
    for energy in picks:
        await ctx.attach_energy(energy, target)
    await ctx.draw_cards(3)


def welder_condition(board, player_id) -> bool:
    return any(is_fire_energy(c) for c in _hand(board, player_id))


async def energy_spinner(ctx):
    n = 3 if go_second_first_turn(ctx.board, ctx.player_id) else 1
    await search_to_hand(
        is_basic_energy_card, count=n, reveal=True,
        prompt="Choose basic Energy cards.",
    )(ctx)
