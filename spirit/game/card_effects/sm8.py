"""Lost Thunder (SM8) attack, ability, trainer, tool, energy, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import (
    AttrID, CardType, CLIENT_POKEMON_TYPE_NAMES, CLIENT_SPECIAL_CONDITION_NAMES,
    GameSequence, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Ability, Activations, TRAINER_EFFECTS_BY_GUID, def_for, evolves_from,
    is_prism_star, is_ultra_beast, unimplemented,
)
from spirit.game.models.board import BoardState, TrainerEntity
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
    Passive, TurnDamageModifier, carrier_pokemon, tool_slots_free,
)
from spirit.game.card_effects.attacks_common import (
    _printed,
    bonus_if,
    count_bench,
    count_energy,
    count_in_play,
    count_prizes_remaining,
    damage_counters_on,
    damage_per,
    discard_for_bonus,
    has_attack_titled,
    has_tool,
    mill_attack,
    place_counters,
    self_energy_discard_attack,
    snipe_attack,
    smokescreen_attack,
)
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost,
    apply_protection,
    guts_survive_passive,
    is_in_active_spot,
    takes_less_passive,
    trainer_effect_shield_passive,
)
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.sm3 import (
    is_fairy_energy, is_fire_energy, is_grass_energy, is_gx_or_ex, is_tool_card,
)
from spirit.game.card_effects.sm4 import is_lightning_pokemon, is_stadium_card, pokemon_has_ability
from spirit.game.card_effects.sm5 import (
    _is_typed_archetype, go_second_first_turn, is_fairy_pokemon,
)
from spirit.game.card_effects.sm6 import is_dragon_pokemon, is_fighting_pokemon
from spirit.game.card_effects.sl import is_benched, trickster_gx
from spirit.game.card_effects.support_common import (
    attach_from_discard,
    distribute_energy,
    opponent_switches,
    recover_from_discard,
    remove_self_from_play,
    requires_bench_space,
    search_attach_energy,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import (
    MemoryCapsulePassive, deck_nonempty, is_basic_energy_card, is_energy_card,
    opponent_has_bench,
)


# ----------------------------------------------------------------------
# Predicates
# ----------------------------------------------------------------------

def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    return getattr(def_for(card.archetype_id), "display_name", None) or ""


def _is_named(card, name: str) -> bool:
    return _logic_name(card) == name or _display_name(card) == name


def _typed(card, pokemon_type: PokemonTypes) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and pokemon_type.value in types


def is_grass_pokemon(card) -> bool:
    return _typed(card, PokemonTypes.GRASS)


def is_psychic_pokemon(card) -> bool:
    return _typed(card, PokemonTypes.PSYCHIC)


def is_active_pokemon(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_in_active_spot(pokemon)


def is_benched_pokemon(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_benched(pokemon)


def _prize_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _fairy_charm_attached(pokemon) -> bool:
    return any(
        "Fairy Charm" in _display_name(child) for child in pokemon.children
    )


def _has_named_energy(pokemon, name: str) -> bool:
    return any(_display_name(child) == name for child in pokemon.children)


def _supporter_name(card) -> str:
    name = _display_name(card)
    return name.split(" {")[0] if name else ""


# ----------------------------------------------------------------------
# Passives
# ----------------------------------------------------------------------

class HarmonicsPassive(Passive):
    """Attach up to 2 Energy from hand to the same Pokémon instead of 1."""

    def allows_second_energy_attach(self, pokemon, carrier):
        return pokemon.owning_player_id == carrier.owning_player_id


class LostOutPassive(Passive):
    """Opponent Pokémon KO'd by this Pokémon's attack go to the Lost Zone
    with their attachments."""

    def knockout_destination(self, pokemon, carrier):
        if getattr(pokemon, "ko_attacker", None) is not carrier:
            return None
        if pokemon.owning_player_id == carrier.owning_player_id:
            return None
        return "lostZone"

    def knockout_whole_stack(self, pokemon, carrier):
        return self.knockout_destination(pokemon, carrier) == "lostZone"


class DoubleDrivePassive(Passive):
    """This Pokémon may have up to 2 Pokémon Tools attached."""

    def tool_capacity(self, pokemon, carrier):
        return 2 if pokemon is carrier else 1


class ProtectiveShellPassive(Passive):
    """Prevent damage from opposing Pokémon that have 2 or fewer Energy."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        attacker = calc.attacker
        if attacker is None:
            return False
        return len(calc.board.attached_energies(attacker)) <= 2


class ThunderclapZonePassive(Passive):
    """Your Pokémon with Lightning Energy attached have no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return cost
        if any(is_lightning_energy(e) for e in board.attached_energies(pokemon)):
            return 0
        return cost


class ShadyTailPassive(Passive):
    """While benched, Prism Star Pokémon in play can't attack and have no
    Abilities."""

    def _applies(self, carrier):
        return is_benched(carrier)

    def blocks_attacks(self, pokemon, carrier):
        return self._applies(carrier) and is_prism_star(pokemon.archetype_id)

    def blocks_abilities(self, pokemon, carrier):
        return self._applies(carrier) and is_prism_star(pokemon.archetype_id)


class MysteriousBuzzPassive(Passive):
    """While benched, prevent opposing Supporter effects done to your Fairy
    Pokémon."""

    def blocks_trainer_effects(
        self, affected_player_id, trainer_card, trainer_type, carrier,
        affected_entity=None, board=None,
    ):
        if trainer_type != TrainerType.SUPPORTER.value:
            return False
        if not is_benched(carrier):
            return False
        if affected_player_id != carrier.owning_player_id:
            return False
        if affected_entity is None:
            return False
        return is_fairy_pokemon(affected_entity)


class UnitColorPassive(Passive):
    """While the named Unit Energy is attached, this Pokémon has those types."""

    def __init__(self, energy_name, types):
        self.energy_name = energy_name
        self.types = [t.value if hasattr(t, "value") else t for t in types]

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        if not _has_named_energy(pokemon, self.energy_name):
            return types
        return list(self.types)


class FairyCharmPassive(Passive):
    """Prevent damage from opposing GX/EX of `pokemon_type` to a Fairy holder."""

    def __init__(self, pokemon_type: PokemonTypes):
        self.pokemon_type = pokemon_type

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
        types = attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        return self.pokemon_type.value in types


class CounterGainPassive(Passive):
    """If you have more Prizes remaining, attacks cost [C] less."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        me = pokemon.owning_player_id
        opp = _other_player(board, me)
        if opp is None:
            return cost
        if _prize_count(board, me) <= _prize_count(board, opp):
            return cost
        if "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - 1
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


class ThunderMountainPassive(Passive):
    """Lightning Pokémon attacks (both sides) cost [L] less."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.LIGHTNING.value not in types:
            return cost
        key = CLIENT_POKEMON_TYPE_NAMES[PokemonTypes.LIGHTNING]
        if key not in cost:
            return cost
        remaining = cost[key] - 1
        if remaining > 0:
            cost[key] = remaining
        else:
            del cost[key]
        return cost


class LusamineUbShield(Passive):
    """Prevent attack damage to the owner's Ultra Beasts."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        target = calc.target
        if target.owning_player_id != carrier.owning_player_id:
            return False
        return is_ultra_beast(target.archetype_id)


class BlazingEnergyPassive(Passive):
    """The owner's attached Energy provide Fire instead of their usual type."""

    def __init__(self, player_id: str):
        self.player_id = player_id

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or holder.owning_player_id != self.player_id:
            return options
        converted = []
        for option in options:
            converted.append([PokemonTypes.FIRE.value] * max(1, len(option)))
        return converted or [[PokemonTypes.FIRE.value]]


class VesselOfLifePassive(Passive):
    """The holder takes 1 fewer Prize card when Knocked Out."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is pokemon:
            return max(0, count - 1)
        return count


class WonderRayPassive(Passive):
    """Prevent effects of attacks, including damage, from Pokémon with Abilities."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return calc.attacker is not None and pokemon_has_ability(calc.attacker)

    def blocks_attack_effects_from(self, target, attacker, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return attacker is not None and pokemon_has_ability(attacker)


class StadiumLockPassive(Passive):
    """Prevent Item/Supporter effects done to this Stadium (Prism Star reminder)."""

    def blocks_trainer_effects(
        self, affected_player_id, trainer_card, trainer_type, carrier,
        affected_entity=None, board=None,
    ):
        if trainer_type not in (
                TrainerType.ITEM.value, TrainerType.SUPPORTER.value):
            return False
        return affected_entity is carrier


class SecretAlleywayPassive(Passive):
    """No Retreat Cost while you have a Fairy Pokémon in play."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if any(is_fairy_pokemon(p) for p in board.pokemon_in_play(pokemon.owning_player_id)):
            return 0
        return cost


class WildDashPassive(Passive):
    """No Retreat Cost while the opponent has a Pokémon-GX or Pokémon-EX in play."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        opp = _other_player(board, pokemon.owning_player_id)
        if opp and any(is_gx_or_ex(p) for p in board.pokemon_in_play(opp)):
            return 0
        return cost


sturdy_passive = guts_survive_passive(10, require_full_hp=True)
choice_helmet_passive = takes_less_passive(30, attacker_pred=is_gx_or_ex)
secret_alleyway_passive = SecretAlleywayPassive()
wild_dash_passive = WildDashPassive()
unit_color_1_passive = UnitColorPassive(
    "Unit Energy GrassFireWater",
    [PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER],
)
unit_color_3_passive = UnitColorPassive(
    "Unit Energy FightingDarknessFairy",
    [PokemonTypes.FIGHTING, PokemonTypes.DARKNESS, PokemonTypes.FAIRY],
)
harmonics_passive = HarmonicsPassive()
lost_out_passive = LostOutPassive()
double_drive_passive = DoubleDrivePassive()
protective_shell_passive = ProtectiveShellPassive()
thunderclap_zone_passive = ThunderclapZonePassive()
shady_tail_passive = ShadyTailPassive()
mysterious_buzz_passive = MysteriousBuzzPassive()
thunder_mountain_passive = ThunderMountainPassive()
counter_gain_passive = CounterGainPassive()
fairy_charm_grass_passive = FairyCharmPassive(PokemonTypes.GRASS)
fairy_charm_psychic_passive = FairyCharmPassive(PokemonTypes.PSYCHIC)
fairy_charm_fighting_passive = FairyCharmPassive(PokemonTypes.FIGHTING)
fairy_charm_dragon_passive = FairyCharmPassive(PokemonTypes.DRAGON)
stadium_lock_passive = StadiumLockPassive()
memory_energy_passive = MemoryCapsulePassive()


# ----------------------------------------------------------------------
# Shared attack helpers
# ----------------------------------------------------------------------

async def _remove_from_play(ctx, pokemon, destination="lostZone"):
    if pokemon is None:
        return
    owner = pokemon.owning_player_id
    was_active = ctx.board.active_pokemon(owner) is pokemon
    stack = full_stack(pokemon)
    if destination == "lostZone":
        await ctx.move_to_lost_zone(stack)
    elif destination == "hand":
        await ctx.put_in_hand(stack, reveal=False)
    else:
        await ctx.shuffle_into_deck(stack, owner)
    if was_active and owner is not None:
        async def _promote():
            if not await ctx.session._promote_new_active(owner):
                winner = ctx.session._opponent_id(owner)
                screen = ctx.session.players[owner].screen_name
                await ctx.session.end_game(
                    winner, f"{screen} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


async def _look_at_prizes(ctx, selectable=None, then=None):
    session = ctx.session
    prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    if not prize_area or not prize_area.children:
        return None
    prizes = list(prize_area.children)
    prize_ids = [c.entity_id for c in prizes]
    selectable_ids = ([c.entity_id for c in selectable]
                      if selectable is not None else prize_ids)
    picked_id = await session.prompt_prize_reveal_pick(
        ctx.player_id, ctx.source.entity_id, prize_ids, selectable_ids)
    picked = ctx.board.get_entity(picked_id) if picked_id else None
    result = None
    if then is not None and picked is not None:
        result = await then(ctx, picked)
    resets = [session._attributes_reset_msg(c.entity_id)
              for c in prize_area.children]
    if resets:
        await session.send_game_sequence(
            [session.players[ctx.player_id]], GameSequence.GROUPED_MOVE, resets)
    return result


def _cure_one_condition(ctx, pokemon):
    names = list(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    if not names:
        return None
    reverse = {v: k for k, v in CLIENT_SPECIAL_CONDITION_NAMES.items()}
    return reverse.get(names[0])


# ----------------------------------------------------------------------
# Attack effects
# ----------------------------------------------------------------------

snowy_wind = snipe_attack(30, also_base=True)
lava_burn = snipe_attack(30, also_base=True)
spoil_the_fun = bonus_if(
    lambda ctx: ctx.session.turn_state.turn_number == 2, 60)
empty_threat = damage_per(count_energy("defender"), -30, base=90)
energy_crush = damage_per(count_energy("opponent"), 20, base=20)
energy_press = damage_per(count_energy("defender"), 20, base=30)
lets_snuggle = damage_per(damage_counters_on("defender"), 30, base=10)
intercept_gx = damage_per(count_energy("defender"), 60)
lost_march = damage_per(
    lambda ctx: sum(
        1 for c in ctx.lost_zone()
        if is_pokemon_card(c) and not is_prism_star(c.archetype_id)
    ),
    20,
)
turning_point = bonus_if(lambda ctx: count_prizes_remaining()(ctx) == 3, 80)
sensitive_blade = bonus_if(lambda ctx: ctx.supporters_played_this_turn() > 0, 80)
sensitive_ray = bonus_if(lambda ctx: ctx.supporters_played_this_turn() > 0, 90)
powerful_friends = bonus_if(
    lambda ctx: any(is_stage2_pokemon(p) for p in ctx.my_bench()), 90)
all_out = bonus_if(lambda ctx: ctx.hand_size() == 0, 130)
metal_arms = bonus_if(lambda ctx: has_tool(ctx.attacker), 40)
charmed_slap = bonus_if(lambda ctx: _fairy_charm_attached(ctx.attacker), 70)
special_blow = bonus_if(
    lambda ctx: ctx.defender is not None and any(
        is_special_energy(e) for e in ctx.attached_energies(ctx.defender)
    ),
    70,
)
second_strike = bonus_if(lambda ctx: damage_counters_on("defender")(ctx) >= 3, 70)
tongue_smack = bonus_if(
    lambda ctx: ctx.defender is not None and is_evolution_pokemon(ctx.defender),
    50,
)
reply_strongly = bonus_if(
    lambda ctx: ctx.damage_taken_last_turn(ctx.attacker) > 0, 80)
hefty_whip = bonus_if(
    lambda ctx: ctx.attacker.entity_id in ctx.session.turn_state.healed_entities,
    130,
)
freezing_flames = bonus_if(
    lambda ctx: any(is_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)),
    80,
)
lost_voltage = bonus_if(
    lambda ctx: any(is_lightning_energy(c) for c in ctx.lost_zone()), 90)
beartic_resolute = bonus_if(
    lambda ctx: ctx.defender is not None and is_gx_or_ex(ctx.defender), 60)
v_beatdown = damage_per(count_in_play("mine", is_basic_pokemon), 20)
heavy_punch = damage_per(count_bench("opponent"), 20)
make_a_mess = discard_for_bonus(
    source="hand", predicate=is_trainer_card, max_count=2, per=20, base=0)
lava_flow = discard_for_bonus(
    source="self-energy", predicate=is_basic_energy_card, max_count=99, per=50)
smokescreen = smokescreen_attack()
thunder_blast = self_energy_discard_attack(count=1, energy_type=PokemonTypes.LIGHTNING)
haunt = place_counters(3)
cursed_drop = place_counters(4, target="choose_any_opponent")
burning_magma_gx = mill_attack(5)
lost_blast = remove_self_from_play("lost_zone")
async def sublimation_gx(ctx):
    defender = ctx.defender
    if defender is not None and is_ultra_beast(defender.archetype_id):
        await ctx.knock_out(defender)


async def trapping_thread(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(
        defender,
        trainer_effect_shield_passive(supporters_only=False, protects="carrier"),
    )


async def polka_dot_search(ctx):
    top = ctx.deck_top(8)
    if not top:
        return
    energies = [c for c in top if is_energy_card(c)]
    picks = []
    if energies:
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt="Attach Energy cards you find",
            display_cards=top,
        )
        if picks:
            await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
    await ctx.shuffle_deck()


async def butterfly_edge(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None and ctx.defender in ctx.knockouts:
        await apply_protection(ctx, ctx.attacker, prevent=True, effects_too=True)


async def mind_blown(ctx):
    energies = [
        e for pokemon in ctx.my_pokemon_in_play()
        for e in ctx.attached_energies(pokemon)
        if is_fire_energy(e)
    ]
    picks = await ctx.choose_cards(
        energies, len(energies), minimum=0,
        prompt="Put Fire Energy in the Lost Zone",
    ) if energies else []
    if picks:
        await ctx.move_to_lost_zone(picks)
    await ctx.deal_damage(50 * len(picks))


async def burst_gx(ctx):
    async def _discard_prize(c, picked):
        await c.discard_cards([picked])
        if is_energy_card(picked) and c.my_pokemon_in_play():
            target = await c.choose_pokemon(
                c.my_pokemon_in_play(),
                "Choose a Pokémon to attach the Energy to",
            ) or c.my_pokemon_in_play()[0]
            await c.attach_energy(picked, target)
        return picked

    await _look_at_prizes(ctx, then=_discard_prize)


async def follow_the_wound(ctx):
    candidates = [
        p for p in ctx.opponent_bench()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Choose a damaged Benched Pokémon")
    if picks:
        await ctx.deal_damage(60, target=picks[0], apply_modifiers=False)


async def diamond_gate(ctx):
    supporters, stadiums = await ctx.search_deck_groups(
        [
            (is_supporter_card, 1, "Choose a Supporter card."),
            (is_stadium_card, 1, "Choose a Stadium card."),
        ],
        prompt="Choose a Supporter and a Stadium.",
    )
    await ctx.put_in_hand(supporters + stadiums, reveal=True)
    await ctx.shuffle_deck()


async def wonder_ray(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, WonderRayPassive())


async def time_distortion(ctx):
    from spirit.game.card_effects.pokemon import devolvable
    while True:
        candidates = [p for p in ctx.my_bench() if devolvable(p)]
        if not candidates:
            return
        picks = await ctx.choose_cards(
            candidates, 1, minimum=0,
            prompt="Choose a Benched Pokémon to devolve",
        )
        if not picks:
            return
        await ctx.devolve_pokemon(picks[0], steps=1, destination="hand")


async def vortex_of_pain(ctx):
    total = sum(
        max(0, (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10)
        for p in ctx.opponent_pokemon_in_play()
    )
    if total:
        await ctx.deal_damage(20 * total)


async def sympathetic_slap(ctx):
    defender = ctx.defender
    if defender is not None and defender.get_attribute(AttrID.HP, 0) < ctx.max_hp(defender):
        return
    await ctx.deal_damage()


async def spirit_juggling(ctx):
    bench = list(ctx.my_bench())
    picks = await ctx.choose_cards(
        bench, len(bench), minimum=0,
        prompt="Discard any number of your Benched Pokémon",
    ) if bench else []
    for pokemon in picks:
        await ctx.discard_cards(full_stack(pokemon))
    await ctx.deal_damage(_printed(ctx) + 30 * len(picks))


async def bee_march(ctx):
    await search_to_bench(
        lambda c: _is_named(c, "Combee"), count=3,
        prompt="Choose up to 3 Combee.",
    )(ctx)


async def cocoon_collector(ctx):
    await search_to_bench(
        lambda c: _logic_name(c) in ("Silcoon", "Cascoon"), count=4,
        prompt="Choose Silcoon and/or Cascoon.",
    )(ctx)


async def multiply(ctx):
    await search_to_bench(
        lambda c: _is_named(c, "Hoppip"), count=1,
        prompt="Choose a Hoppip.",
    )(ctx)


async def eruption(ctx):
    extra = 0
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(1, player_id=pid)
        if top:
            await ctx.discard_cards(top)
            if is_energy_card(top[0]):
                extra += 60
    await ctx.deal_damage(_printed(ctx) + extra)


async def thorny_eruption(ctx):
    results = await ctx.flip_coins(3, "Thorny Eruption")
    heads = sum(1 for r in results if r)
    if not heads:
        return
    amount = 10 * heads
    await ctx.deal_damage(amount)
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(amount, target=pokemon, apply_modifiers=False)


async def get_lost(ctx):
    cards = list(ctx.discard_pile(ctx.opponent_id))
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, min(2, len(cards)), minimum=0,
        prompt="Put cards in the Lost Zone",
    )
    if picks:
        await ctx.move_to_lost_zone(picks)


async def shadow_impact(ctx):
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    if not mine:
        return
    target = await ctx.choose_pokemon(
        mine, "Choose 1 of your Pokémon to put 4 damage counters on")
    if target is not None:
        await ctx.deal_damage(40, target=target, as_counters=True)


async def rainbow_burn(ctx):
    types = set()
    for energy in ctx.attached_energies(ctx.attacker):
        if not is_basic_energy_card(energy):
            continue
        info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
        for option in info.get("options", []):
            types.update(option)
    await ctx.deal_damage(_printed(ctx) + 30 * len(types))


async def team_hunt(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if _logic_name(p) == "Houndour")
    await ctx.draw_cards(n)


async def milk_cannon(ctx):
    milks = [c for c in ctx.hand() if _display_name(c) == "Moomoo Milk"]
    if not milks:
        return
    picks = await ctx.choose_cards(
        milks, len(milks), minimum=0,
        prompt="Reveal Moomoo Milk cards",
    )
    if picks:
        await ctx.deal_damage(60 * len(picks))


async def dream_fear_gx(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to shuffle into the deck")
    if target is not None:
        await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)


async def miracle_harmony(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if has_attack_titled("Sing")(p))
    if not n:
        return
    results = await ctx.flip_coins(n, "Miracle Harmony")
    heads = sum(1 for r in results if r)
    if not heads:
        return
    amount = 10 * heads
    await ctx.deal_damage(amount)
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(amount, target=pokemon, apply_modifiers=False)


async def assisting_heater(ctx):
    await ctx.deal_damage()
    cards = [c for c in ctx.hand() if is_fire_energy(c)]
    bench = ctx.my_bench()
    if not cards or not bench:
        return
    if not await ctx.ask_yes_no(
            "Attach a Fire Energy from your hand to a Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(cards, 1, prompt="Choose a Fire Energy")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon") or bench[0]
    await ctx.attach_energy(picks[0], target)


nightcap = trickster_gx


def nightcap_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    return opp is not None and _prize_count(board, opp) == 2


async def overshort(ctx):
    defender = ctx.defender
    discarded = False
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [c for c in list(defender.children) if is_tool_card(c)]
        if tools:
            await ctx.discard_cards(tools)
            discarded = True
    await ctx.deal_damage(_printed(ctx) + (40 if discarded else 0))
    if discarded:
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)


async def eye_opener(ctx):
    await _look_at_prizes(ctx, selectable=[])


async def pelagic_blade(ctx):
    await ctx.deal_damage()


async def lost_purge_gx(ctx):
    await _remove_from_play(ctx, ctx.defender, "lostZone")


async def leaf_cyclone(ctx):
    await ctx.deal_damage()
    energies = [
        e for e in ctx.attached_energies(ctx.attacker) if is_grass_energy(e)
    ]
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=0, prompt="Move a Grass Energy")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon") or bench[0]
    await ctx.move_energy(picks[0], target)


async def jungle_heal_gx(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if any(is_grass_energy(e) for e in ctx.attached_energies(pokemon)):
            await ctx.heal(9999, pokemon)


async def fury_cutter(ctx):
    results = await ctx.flip_coins(3, "Fury Cutter")
    heads = sum(1 for r in results if r)
    bonus = {1: 20, 2: 50, 3: 70}.get(heads, 0)
    await ctx.deal_damage(_printed(ctx) + bonus)


async def dreams_touch(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    names = defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    if asleep not in names:
        return
    await ctx.shuffle_into_deck(
        list(ctx.attached_energies(defender)), ctx.opponent_id)


async def salvage(ctx):
    await recover_from_discard(
        is_item_card, count=4, minimum=0, to="deck_shuffle",
        prompt="Choose up to 4 Item cards to shuffle into your deck.",
    )(ctx)


async def beckon(ctx):
    await recover_from_discard(
        is_supporter_card, count=1, minimum=0,
        prompt="Choose a Supporter card.",
    )(ctx)


async def quick_hunt(ctx):
    await search_to_hand(None, count=1, reveal=False, prompt="Choose a card.")(ctx)


async def memory_melt(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=0, prompt="Put a card in the Lost Zone")
    if picks:
        await ctx.move_to_lost_zone(picks)


async def stunning_likeness(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
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


async def spider_scram(ctx):
    defender = ctx.defender
    if defender is not None:
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
        await ctx.apply_special_condition(defender, SpecialConditions.POISONED)
    await _remove_from_play(ctx, ctx.attacker, "lostZone")


async def wild_tackle(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Wild Tackle")
    if results and not results[0]:
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)


async def dream_away(ctx):
    results = await ctx.flip_coins(1, "Dream Away")
    if results and results[0]:
        await _remove_from_play(ctx, ctx.defender, "deck")


async def flashing_bolt(ctx):
    await ctx.deal_damage()


async def nuzzle_shot(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if has_attack_titled("Nuzzle")(p))
    bench = ctx.opponent_bench()
    if not n or not bench:
        return
    picks = await ctx.choose_cards(
        bench, 1, prompt="Choose a Benched Pokémon")
    if picks:
        await ctx.deal_damage(10 * n, target=picks[0], apply_modifiers=False)


async def happy_delivery(ctx):
    targets = [p for p in ctx.my_bench() if not has_tool(p)]
    if not targets:
        return
    picks = await ctx.search_deck(
        is_tool_card, count=len(targets), minimum=0,
        prompt="Choose Pokémon Tool cards to attach.",
    )
    remaining = list(targets)
    for tool in picks:
        if not remaining:
            break
        target = remaining.pop(0)
        await ctx.attach_tool(tool, target)
    await ctx.shuffle_deck()


async def find_a_friend(ctx):
    await search_to_hand(
        is_grass_pokemon, count=1, reveal=True,
        prompt="Choose a Grass Pokémon.",
    )(ctx)


async def venom_fever(ctx):
    defender = ctx.defender
    if defender is None:
        return
    names = defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    if CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED] not in names:
        return
    n = damage_counters_on("defender")(ctx)
    if n:
        await ctx.deal_damage(50 * n)


async def commanding_queen(ctx):
    grass = sum(1 for p in ctx.my_bench() if is_grass_pokemon(p))
    if grass <= 4:
        return
    await ctx.deal_damage()


async def breeze_away_gx(ctx):
    pool = ctx.my_pokemon_in_play()
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Choose Pokémon to put into your hand",
    )
    if not picks:
        return
    need_promote = ctx.my_active() in picks
    cards = []
    for pokemon in picks:
        cards.extend(full_stack(pokemon))
    await ctx.put_in_hand(cards, reveal=False)
    if need_promote:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


async def field_crush(ctx):
    await ctx.deal_damage()
    stadium_area = ctx.board.find_global_area("activeStadium")
    stadium = stadium_area.children[0] if stadium_area and stadium_area.children else None
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        await ctx.discard_cards([stadium])


async def energy_gaze(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    extra = 60 if any(is_energy_card(c) for c in cards) else 0
    await ctx.deal_damage(_printed(ctx) + extra)


async def bright_horns(ctx):
    await ctx.deal_damage()


async def dusty_ruckus(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.opponent_bench():
        if is_basic_pokemon(pokemon):
            await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)


async def lost_flame(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = list(ctx.attached_energies(defender))
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, min(2, len(energies)), minimum=0,
        prompt="Put Energy in the Lost Zone",
    )
    if picks:
        await ctx.move_to_lost_zone(picks)


async def full_voltage_gx(ctx):
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, min(5, len(cards)), minimum=0,
        prompt="Choose up to 5 basic Energy cards",
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


async def zzzap_touch(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Zzzap Touch")
    if not results:
        return
    cond = (SpecialConditions.CONFUSED if results[0]
            else SpecialConditions.PARALYZED)
    await ctx.apply_special_condition(ctx.defender, cond)


async def secondary_chills(ctx):
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


async def rolling_spin_attack(ctx):
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 70, attack_title="Rolling Spin")


async def leaf_wallop_attack(ctx):
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 50, attack_title="Leaf Wallop")


rolling_spin = rolling_spin_attack
leaf_wallop = leaf_wallop_attack


# ----------------------------------------------------------------------
# Ability effects
# ----------------------------------------------------------------------

async def mysterious_guidance(ctx):
    if not await ctx.ask_yes_no(
            "Search your deck for up to 2 Item cards?"):
        return
    await search_to_hand(
        is_item_card, count=2, reveal=True,
        prompt="Choose up to 2 Item cards.",
    )(ctx)


async def unseen_flash(ctx):
    cards = [c for c in ctx.hand() if is_lightning_energy(c)]
    if len(cards) < 2:
        return
    picks = await ctx.choose_cards(
        cards, 2, prompt="Put 2 Lightning Energy in the Lost Zone")
    if len(picks) < 2:
        return
    await ctx.move_to_lost_zone(picks)
    await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)


def unseen_flash_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_lightning_energy(c)) >= 2


async def happiness_supplement(ctx):
    active = ctx.my_active()
    if active is None:
        return
    cond = _cure_one_condition(ctx, active)
    if cond is not None:
        await ctx.cure_condition(active, cond)


def happiness_supplement_condition(board, player_id, pokemon=None) -> bool:
    active = board.active_pokemon(player_id)
    return bool(active and active.get_attribute(AttrID.SPECIAL_CONDITIONS))


async def hazardous_evolution(ctx):
    if not await ctx.ask_yes_no(
            "Leave the opponent's Active Paralyzed and Poisoned?"):
        return
    defender = ctx.opponent_active()
    if defender is None:
        return
    await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    await ctx.apply_special_condition(
        defender, SpecialConditions.POISONED, poison_counters=3)


async def crushing_charge(ctx):
    top = ctx.deck_top(1)
    if not top:
        return
    await ctx.discard_cards(top)
    if is_basic_energy_card(top[0]) and ctx.my_pokemon_in_play():
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(),
            "Choose a Pokémon to attach the Energy to",
        ) or ctx.source
        await ctx.attach_energy(top[0], target)


def crushing_charge_condition(board, player_id, pokemon=None) -> bool:
    return deck_nonempty(board, player_id)


async def fluffy_pillow(ctx):
    await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.ASLEEP)


async def quick_ripening_herb(ctx):
    basics = [p for p in ctx.my_pokemon_in_play() if is_basic_pokemon(p)]
    if not basics:
        return
    target = await ctx.choose_pokemon(basics, "Choose a Basic Pokémon")
    if target is None:
        return
    logic_name = _logic_name(target)
    stage2 = [
        c for c in ctx.hand()
        if is_stage2_pokemon(c) and evolves_from(c.archetype_id, logic_name)
    ]
    if not stage2:
        return
    picks = await ctx.choose_cards(
        stage2, 1, prompt="Choose a Stage 2 Pokémon to evolve into")
    if picks:
        await ctx.evolve_pokemon(target, picks[0])


def quick_ripening_herb_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    if not hand:
        return False
    basics = [p for p in board.pokemon_in_play(player_id) if is_basic_pokemon(p)]
    for basic in basics:
        logic_name = basic.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if any(is_stage2_pokemon(c) and evolves_from(c.archetype_id, logic_name)
               for c in hand.children):
            return True
    return False


charging_up = attach_from_discard(is_basic_energy_card, count=1, target="self")


def charging_up_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_basic_energy_card(c) for c in discard.children)


async def molting(ctx):
    if not await ctx.ask_yes_no("Put a Shedinja from your discard pile onto your Bench?"):
        return
    candidates = [
        c for c in ctx.discard_pile() if _is_named(c, "Shedinja")
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(candidates, 1, prompt="Choose a Shedinja")
    if picks:
        await ctx.bench_pokemon(picks[0])


def molting_condition(board, player_id, pokemon=None) -> bool:
    if not requires_bench_space(1)(board, player_id):
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(
        (c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or "") == "Shedinja"
        for c in discard.children
    )


async def go_for_a_swim(ctx):
    await ctx.reorder_deck_top(2)


async def hard_shell_evolution(ctx):
    if await ctx.ask_yes_no(
            "Prevent all damage done to this Pokémon by opponent's attacks until the end of your opponent's next turn?"):
        await apply_protection(ctx, ctx.source, prevent=True)


async def floral_heal(ctx):
    active = ctx.my_active()
    if active is not None and is_grass_pokemon(active):
        await ctx.heal(20, active)


def floral_heal_condition(board, player_id, pokemon=None) -> bool:
    active = board.active_pokemon(player_id)
    return bool(active) and is_grass_pokemon(active)


async def vessel_of_life(ctx):
    shed = ctx.source
    attachments = list(shed.children)
    if attachments:
        await ctx.discard_cards(attachments)
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if p is not shed and tool_slots_free(ctx.board, p) > 0
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to attach Shedinja to as a Tool")
    if target is None:
        return
    was_active = shed is ctx.my_active()
    BoardState.masquerade_as(
        shed, TrainerEntity,
        {
            AttrID.TRAINER_TYPE.value: TrainerType.POKEMON_TOOL.value,
            AttrID.CARD_TYPE.value: CardType.TRAINER.value,
        },
        VesselOfLifePassive(),
    )
    await ctx.attach_tool(shed, target)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


def vessel_of_life_condition(board, player_id, pokemon=None) -> bool:
    if pokemon is None:
        return False
    return any(
        p is not pokemon and tool_slots_free(board, p) > 0
        for p in board.pokemon_in_play(player_id)
    )


async def effect_spore(ctx):
    if not is_in_active_spot(ctx.source):
        return
    attacker = getattr(ctx, "damaged_by", None)
    if attacker is not None:
        await ctx.apply_special_condition(attacker, SpecialConditions.ASLEEP)


async def mirror_counter(ctx):
    if not is_in_active_spot(ctx.source):
        return
    attacker = getattr(ctx, "damaged_by", None)
    amount = getattr(ctx, "damage_amount", 0) or 0
    if attacker is None or amount <= 0 or not is_gx_or_ex(attacker):
        return
    await ctx.deal_damage(amount, target=attacker, as_counters=True)


async def fresh_squeezed(ctx):
    if not await ctx.ask_yes_no(
            "Search your deck for up to 3 basic Energy cards and discard them?"):
        return
    picks = await ctx.search_deck(
        is_basic_energy_card, count=3, minimum=0,
        prompt="Choose up to 3 basic Energy cards to discard.",
    )
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


async def floral_path(ctx):
    picks = await ctx.search_deck(
        lambda c: _is_named(c, "Jumpluff"), count=1, minimum=0,
        prompt="Choose a Jumpluff.",
    )
    if picks:
        await ctx.identity_swap(ctx.source, picks[0], destination="lostZone")
    await ctx.shuffle_deck()


def floral_path_condition(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def phantom_winds(ctx):
    await ctx.shuffle_into_deck(full_stack(ctx.source), ctx.player_id)


async def frozen_flow(ctx):
    await opponent_switches(ctx)


def frozen_flow_condition(board, player_id, pokemon=None) -> bool:
    return is_active_pokemon(board, player_id, pokemon) and opponent_has_bench(
        board, player_id)


async def charmed_charm(ctx):
    tool = getattr(ctx, "attached_tool", None)
    if tool is None or "Fairy Charm" not in _display_name(tool):
        return
    if getattr(ctx, "attaching_player_id", None) != ctx.player_id:
        return
    if not await ctx.ask_yes_no("Leave your opponent's Active Pokémon Confused?"):
        return
    await ctx.apply_special_condition(
        ctx.opponent_active(), SpecialConditions.CONFUSED)


async def mountain_pass(ctx):
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if top:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, top,
            prompt="Top card of your opponent's deck",
        )
    await ctx.move_to_lost_zone([ctx.source])
    if top and is_supporter_card(top[0]):
        if await ctx.ask_yes_no("Put that Supporter card in the Lost Zone?"):
            await ctx.move_to_lost_zone(top)


def mountain_pass_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    deck = board.find_player_area(opp, "deck")
    return bool(deck and deck.children)


async def blazing_energy(ctx):
    ctx.add_global_passive(
        BlazingEnergyPassive(ctx.player_id),
        ctx.session.turn_state.turn_number,
    )


async def distortion_door(ctx):
    if not await ctx.bench_pokemon(ctx.source):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    n = min(2, len(bench))
    picks = await ctx.choose_cards(
        bench, n, minimum=0,
        prompt="Put 1 damage counter on Benched Pokémon",
    )
    for pokemon in picks[:2]:
        await ctx.deal_damage(10, target=pokemon, as_counters=True)


distortion_door_condition = requires_bench_space(1)


async def almighty_evolution(ctx):
    stage1 = [c for c in ctx.hand() if is_stage1_pokemon(c)]
    if not stage1:
        return
    picks = await ctx.choose_cards(
        stage1, 1, prompt="Choose a Stage 1 card to evolve into")
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])


def almighty_evolution_condition(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    if ts is None or ts.turn_number <= 2 or pokemon is None:
        return False
    if ts.entered_play_turn.get(pokemon.entity_id, 0) >= ts.turn_number:
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_stage1_pokemon(c) for c in hand.children)


async def path_of_life(ctx):
    if not await ctx.ask_yes_no(
            "Move any number of Energy from your other Pokémon to this Pokémon?"):
        return
    others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    if not others:
        return
    await ctx.move_energy_freely(others, [ctx.source])


async def sprint(ctx):
    await ctx.discard_from_hand(
        len(ctx.hand()), minimum=0, prompt="Discard your hand")
    await ctx.draw_cards(4)


async def win_the_game(ctx):
    await ctx.session.end_game(
        ctx.player_id, getattr(ctx.ability, "title", None) or "unown")


def unown_damage_condition(board, player_id, pokemon=None) -> bool:
    if not is_active_pokemon(board, player_id, pokemon):
        return False
    total = 0
    for p in board.pokemon_in_play(player_id):
        if is_benched(p):
            printed = p.attribute_originals.get(
                AttrID.HP.value, p.get_attribute(AttrID.HP, 0))
            total += max(0, (printed - p.get_attribute(AttrID.HP, 0)) // 10)
    return total >= 66


def unown_hand_condition(board, player_id, pokemon=None) -> bool:
    if not is_active_pokemon(board, player_id, pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) >= 35


def unown_missing_condition(board, player_id, pokemon=None) -> bool:
    if not is_active_pokemon(board, player_id, pokemon):
        return False
    opp = _other_player(board, player_id)
    if opp is None:
        return False
    zone = board.find_player_area(opp, "lostZone")
    return bool(zone) and sum(
        1 for c in zone.children if is_supporter_card(c)
    ) >= 12


# ----------------------------------------------------------------------
# Trainer / stadium / tool effects
# ----------------------------------------------------------------------

adventure_bag = search_to_hand(
    is_tool_card, count=2, reveal=True,
    prompt="Choose up to 2 Pokémon Tool cards.",
)

aether_foundation_employee = recover_from_discard(
    lambda c: is_pokemon_card(c) and "Alolan" in _display_name(c),
    count=3, minimum=0,
    prompt="Choose up to 3 Alolan Pokémon.",
)


async def faba(ctx):
    stadium_area = ctx.board.find_global_area("activeStadium")
    stadium = stadium_area.children[0] if stadium_area and stadium_area.children else None
    attached = []
    for pokemon in ctx.opponent_pokemon_in_play():
        for child in pokemon.children:
            if is_tool_card(child) or is_special_energy(child):
                attached.append(child)
    candidates = attached + ([stadium] if stadium is not None else [])
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, prompt="Put a card in the Lost Zone")
    if picks:
        await ctx.move_to_lost_zone(picks)


def faba_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    stadium_area = board.find_global_area("activeStadium")
    if stadium_area and stadium_area.children:
        return True
    if opp is None:
        return False
    for pokemon in board.pokemon_in_play(opp):
        for child in pokemon.children:
            if is_tool_card(child) or is_special_energy(child):
                return True
    return False


async def kahili(ctx):
    await ctx.draw_cards(2)
    results = await ctx.flip_coins(1, "Kahili")
    if results and results[0]:
        await ctx.put_in_hand([ctx.source], reveal=False)


kahili_condition = deck_nonempty


async def lost_blender(ctx):
    picks = await ctx.choose_cards(
        ctx.hand(), 2, prompt="Put 2 cards from your hand in the Lost Zone")
    if len(picks) < 2:
        return
    await ctx.move_to_lost_zone(picks)
    await ctx.draw_cards(1)


def lost_blender_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(hand) and len(hand.children) >= 3 and bool(deck and deck.children)


mina = search_attach_energy(is_fairy_energy, count=1)


async def mixed_herbs(ctx):
    others = [
        c for c in ctx.hand()
        if c is not ctx.source and c.archetype_id == ctx.source.archetype_id
    ]
    if others and await ctx.ask_yes_no(
            "Play another Mixed Herbs to heal 90 and remove all Special Conditions?"):
        extra = await ctx.choose_cards(
            others, 1, prompt="Choose another Mixed Herbs")
        if extra:
            await ctx.discard_cards(extra)
            active = ctx.my_active()
            if active is not None:
                await ctx.heal(90, active)
                await ctx.cure_all_conditions(active)
            return
    active = ctx.my_active()
    if active is None:
        return
    cond = _cure_one_condition(ctx, active)
    if cond is not None:
        await ctx.cure_condition(active, cond)


async def custom_catcher(ctx):
    others = [
        c for c in ctx.hand()
        if c is not ctx.source and c.archetype_id == ctx.source.archetype_id
    ]
    if others and opponent_has_bench(ctx.board, ctx.player_id) and await ctx.ask_yes_no(
            "Play another Custom Catcher to switch 1 of your opponent's Benched Pokémon?"):
        extra = await ctx.choose_cards(
            others, 1, prompt="Choose another Custom Catcher")
        if extra:
            await ctx.discard_cards(extra)
            bench = ctx.opponent_bench()
            if bench:
                target = await ctx.choose_pokemon(
                    bench, "Choose a Benched Pokémon to switch in") or bench[0]
                await ctx.switch_active(ctx.opponent_id, target)
            return
    await ctx.draw_until(3)


async def moomoo_milk(ctx):
    targets = ctx.my_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to heal")
    if target is None:
        return
    results = await ctx.flip_coins(2, "Moomoo Milk")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.heal(30 * heads, target)


async def morty(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    if not cards:
        return
    n = min(2, len(cards))
    picks = await ctx.choose_cards(
        cards, n, prompt="Choose cards to shuffle into the deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


def morty_condition(board, player_id, pokemon=None) -> bool:
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    for ko in ts.kos_by_attack_last_turn.get(player_id, []):
        if _is_typed_archetype(ko.get("archetype_id"), PokemonTypes.PSYCHIC):
            return True
    return False


net_ball = search_to_hand(
    lambda c: (is_basic_pokemon(c) and is_grass_pokemon(c)) or is_grass_energy(c),
    count=1, reveal=True,
    prompt="Choose a Basic Grass Pokémon or a Grass Energy card.",
)

professor_elms_lecture = search_to_hand(
    lambda c: is_pokemon_card(c) and (c.get_attribute(AttrID.HP, 0) or 0) <= 60,
    count=3, reveal=True,
    prompt="Choose up to 3 Pokémon with 60 HP or less.",
)


async def sightseer(ctx):
    hand = list(ctx.hand())
    need = max(0, len(hand) - 4)
    if need:
        picks = await ctx.choose_cards(
            hand, len(hand), minimum=need,
            prompt="Discard cards so you can draw",
        )
        await ctx.discard_cards(picks)
    else:
        await ctx.discard_from_hand(
            len(hand), minimum=0,
            prompt="You may discard any number of cards from your hand",
        )
    await ctx.draw_until(5)


def sightseer_condition(board, player_id, pokemon=None) -> bool:
    return deck_nonempty(board, player_id)


async def wait_and_see_hammer(ctx):
    candidates = [
        p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to discard Energy from")
    if target is None:
        return
    await ctx.discard_energy_from(
        target, 1, prompt="Choose an Energy to discard")


wait_and_see_hammer_condition = go_second_first_turn


async def whitney(ctx):
    await ctx.draw_cards(1)
    others = sum(
        1 for c in ctx.discard_pile() if _supporter_name(c) == "Whitney"
    )
    if others:
        await ctx.draw_cards(2 * others)


async def electropower(ctx):
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        30, ctx.player_id, opposing_active_only=True,
        source_predicate=is_lightning_pokemon,
    ))


async def lusamine_prism_star(ctx):
    ctx.add_global_passive(
        LusamineUbShield(),
        ctx.session.turn_state.turn_number + 1,
    )


def lusamine_prism_star_condition(board, player_id, pokemon=None) -> bool:
    opp = _other_player(board, player_id)
    return opp is not None and _prize_count(board, opp) == 3


async def spell_tag_ko(ctx):
    await ctx.place_damage_counters(4, ctx.opponent_pokemon_in_play())


async def heat_factory(ctx):
    cards = [c for c in ctx.hand() if is_fire_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, prompt="Discard a Fire Energy card")
    if picks:
        await ctx.discard_cards(picks)
        await ctx.draw_cards(3)


def heat_factory_condition(board, player_id, stadium=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_fire_energy(c) for c in hand.children)


async def life_forest(ctx):
    candidates = [
        p for p in board_grass(ctx)
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
        or p.get_attribute(AttrID.SPECIAL_CONDITIONS)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Grass Pokémon to heal")
    if target is None:
        return
    await ctx.heal(60, target)
    await ctx.cure_all_conditions(target)


def board_grass(ctx):
    return [p for p in ctx.my_pokemon_in_play() if is_grass_pokemon(p)]


def life_forest_condition(board, player_id, stadium=None) -> bool:
    return any(is_grass_pokemon(p) for p in board.pokemon_in_play(player_id))


HEAT_FACTORY_ABILITY = Ability(
    title="Heat Factory {*}",
    game_text="Once during each player's turn, that player may discard a Fire Energy card from their hand. If they do, they draw 3 cards.",
    activation=Activations.ONCE_PER_TURN,
    effect=heat_factory,
    condition=heat_factory_condition,
)

LIFE_FOREST_ABILITY = Ability(
    title="Life Forest {*}",
    game_text="Once during each player's turn, that player may heal 60 damage and remove all Special Conditions from 1 of their Grass Pokémon.",
    activation=Activations.ONCE_PER_TURN,
    effect=life_forest,
    condition=life_forest_condition,
)
