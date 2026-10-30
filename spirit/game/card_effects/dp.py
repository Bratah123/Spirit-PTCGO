"""Diamond & Pearl–era shared attack / ability / trainer helpers."""
from __future__ import annotations

from typing import Callable, Optional

from spirit.game.attributes import (
    AbilityTypes, AttrID, PokemonStage, PokemonTypes, SpecialConditions,
)
from spirit.game.data_utils import Activations, Triggers
from spirit.game.card_effects.attacks_common import *  # noqa: F401,F403
from spirit.game.card_effects.passives_common import *  # noqa: F401,F403
from spirit.game.card_effects.support_common import *  # noqa: F401,F403
from spirit.game.card_effects.ex import (  # noqa: F401
    baby_evolution, baby_evolution_condition, baby_evolution_ex7,
    defense_curl_flip_protect, splash_about, water_gun_extra, karate_chop,
    heal_equal_to_damage, metronome_defending, force_opponent_switch,
    bonus_if_damaged, bonus_if_special_condition, bonus_if_asleep,
    extra_energy_damage, may_discard_all_energy_for_damage, pin_missile,
    feint_attack, shuffle_random_from_opponent_hand, warp_point, super_scoop_up,
    strength_charm_passive, discard_basic_energy_attack,
    poke_power_condition, is_active_pokemon,
)
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.pokemon import energy_provides_type, is_energy_card
from spirit.game.session.effects import (
    is_basic_pokemon, is_pokemon_card, is_supporter_card, is_trainer_card,
)
from spirit.game.session.passives import Passive, carrier_pokemon
# apply_protection / is_in_active_spot come from passives_common via star-import above


def _display(card) -> str:
    """Best-effort printable name; never returns a non-str."""
    d = def_for(getattr(card, "archetype_id", None) or "")
    if d is not None and getattr(d, "display_name", None):
        return str(d.display_name)
    raw = None
    if hasattr(card, "get_attribute"):
        raw = (card.get_attribute(AttrID.DISPLAY_NAME)
               or card.get_attribute(AttrID.CARD_NAME)
               or card.get_attribute(AttrID.NAME))
    if isinstance(raw, dict):
        return str(raw.get("id") or raw.get("en") or "")
    return str(raw or "")


def named_under(*names: str):
    """True if any tucked-under Pokemon matches one of the display names."""
    want = {n.lower() for n in names}

    def pred(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        for child in list(getattr(attacker, "children", []) or []):
            if not hasattr(child, "get_attribute"):
                continue
            if child.get_attribute(AttrID.CARD_TYPE) is None:
                continue
            # Pokemon tucked under have EVOLUTION_LOGIC_NAME / display
            dn = _display(child).lower()
            logic = (child.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or "").lower()
            if dn in want or any(n in dn for n in want) or any(n in logic for n in want):
                return True
            # also check nested stacks
            for grand in list(getattr(child, "children", []) or []):
                gd = _display(grand).lower()
                if gd in want or any(n in gd for n in want):
                    return True
        return False

    return pred


def evolved_from_named(*names: str):
    """True if the attacker's evolution line includes a named prior stage
    (evolves_from chain or tucked-under names)."""
    want = {n.lower() for n in names}

    def pred(ctx) -> bool:
        if named_under(*names)(ctx):
            return True
        attacker = ctx.attacker
        if attacker is None:
            return False
        # Check evolves_from of the current definition against names, or
        # any child display name (covers Babies placed under via Baby Evolution).
        for child in list(getattr(attacker, "children", []) or []):
            dn = _display(child).lower()
            if dn in want or any(n == dn or n in dn for n in want):
                return True
        return False

    return pred



async def _put_stack_on_top(ctx, cards, player_id=None):
    """Put cards on top of deck (last in list ends on top)."""
    if not cards:
        return
    # Normalize single entity
    if not isinstance(cards, (list, tuple)):
        cards = [cards]
    for c in cards:
        await ctx.put_on_top_of_deck(c)


def bonus_if_evolved_from(*names: str, bonus: int = 20, base: Optional[int] = None):
    return bonus_if(evolved_from_named(*names), bonus, base=base)


def bubble_pump(base: int = 40, energy_bonus: int = 20, energy_threshold: int = 3,
                under_name: str = "Azurill"):
    """Azumarill Bubble Pump: +20 if ≥3 Energy; if Azurill under, flip Paralyze."""
    async def effect(ctx):
        n = sum(1 for c in (ctx.attacker.children if ctx.attacker else [])
                if is_energy_card(c))
        dmg = base + (energy_bonus if n >= energy_threshold else 0)
        await ctx.deal_damage(dmg)
        if named_under(under_name)(ctx):
            heads = await ctx.flip_coins(1, "Bubble Pump")
            if heads and heads[0] and ctx.defender is not None:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.PARALYZED)
    return effect


def harden_prevent_at_most(max_damage: int = 30):
    """Prevent next-turn attack damage to self if that damage is ≤ max_damage."""
    class _Harden(Passive):
        def modify_damage_taken(self, calc, carrier):
            holder = carrier_pokemon(carrier) or carrier
            if (calc.target is holder and calc.is_attack
                    and not calc.prevented and calc.amount <= max_damage):
                calc.amount = 0
                calc.prevented = True

    async def effect(ctx):
        if ctx.attacker is None:
            return
        ctx.add_passive_through_opponents_turn(ctx.attacker, _Harden())
    return effect


def fake_tears(reduce: int = 30):
    """Flip: opponent can't play Trainers next turn; take reduce less damage."""
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Fake Tears")
        if not heads or not heads[0] or ctx.attacker is None:
            return
        ctx.lock_plays(ctx.opponent_id, is_trainer_card)
        await apply_protection(ctx, target=ctx.attacker, reduce=reduce)
    return effect


def soliciting_nectar():
    """Gust opponent Bench → Active, then Asleep."""
    async def then(ctx, new_active):
        if new_active is not None:
            await ctx.apply_special_condition(new_active, SpecialConditions.ASLEEP)
    return gust_then(then, opponent_chooses=False)


def roam_counters(counters: int = 2):
    """Heads: counters on each opponent Pokemon; tails: counters on 1 of yours."""
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Roam")
        if heads and heads[0]:
            for p in ctx.opponent_pokemon_in_play():
                await ctx.deal_damage(counters * 10, target=p,
                                     apply_modifiers=False, as_counters=True)
        else:
            pool = ctx.my_pokemon_in_play()
            if not pool:
                return
            pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
            if pick:
                await ctx.deal_damage(counters * 10, target=pick,
                                     apply_modifiers=False, as_counters=True)
    return effect


def gravity_wave(amount: int = 10):
    """Damage each opponent Bench Pokémon with retreat cost 0."""
    async def effect(ctx):
        await ctx.deal_damage()
        for p in ctx.opponent_bench():
            retreat = p.get_attribute(AttrID.RETREAT_COST, 0) or 0
            if retreat == 0:
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def hard_feelings(base_counters: int = 5):
    """base_counters + prizes-taken counters on Defending."""
    async def effect(ctx):
        prizes = 0
        if hasattr(ctx, "prizes_taken"):
            prizes = ctx.prizes_taken(ctx.opponent_id)
        else:
            board = ctx.board
            dealt = getattr(board, "prizes_dealt", {}).get(ctx.opponent_id, 6)
            remaining = len(board.prize_cards(ctx.opponent_id)) if hasattr(board, "prize_cards") else dealt
            prizes = max(0, dealt - remaining)
        await ctx.deal_damage((base_counters + prizes) * 10,
                             apply_modifiers=False, as_counters=True)
    return effect


def thunderpunch_recoil(base: int = 30, bonus: int = 10, self_dmg: int = 10):
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Thunderpunch")
        if heads and heads[0]:
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
            if ctx.attacker is not None:
                await ctx.deal_damage(self_dmg, target=ctx.attacker,
                                     apply_modifiers=False)
    return effect


def shock_wave_elekid(bench_snipe: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Shock Wave")
        if heads and heads[0] and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
        if evolved_from_named("Elekid")(ctx):
            bench = ctx.opponent_bench()
            if bench:
                pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
                if pick:
                    await ctx.deal_damage(bench_snipe, target=pick,
                                         apply_modifiers=False)
    return effect


def giga_impact_may_discard(energy_type=PokemonTypes.LIGHTNING,
                            normal: int = 60, boosted: int = 120):
    return may_discard_all_energy_for_damage(energy_type, boosted)


def aqua_jet_flip_snipe(amount: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Aqua Jet")
        if heads and heads[0]:
            bench = ctx.opponent_bench()
            if bench:
                pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
                if pick:
                    await ctx.deal_damage(amount, target=pick,
                                         apply_modifiers=False)
    return effect


def pain_payback():
    """Move 1 damage counter from self to an opponent Pokémon."""
    async def effect(ctx):
        if ctx.attacker is None:
            return
        # need at least 1 counter
        hp = ctx.attacker.get_attribute(AttrID.HP, 0)
        max_hp = getattr(def_for(ctx.attacker.archetype_id), "hp", 0) or 0
        if max_hp and hp >= max_hp:
            return
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if not pick:
            return
        await ctx.heal(10, ctx.attacker)
        await ctx.deal_damage(10, target=pick,
                             apply_modifiers=False, as_counters=True)
    return effect


def shadow_dance(counters: int = 4):
    async def effect(ctx):
        remaining = counters
        while remaining > 0:
            pool = ctx.opponent_pokemon_in_play()
            if not pool:
                break
            pick = await ctx.choose_pokemon(pool, f"Place a damage counter ({remaining} left)")
            if not pick:
                break
            await ctx.deal_damage(10, target=pick,
                                 apply_modifiers=False, as_counters=True)
            remaining -= 1
        await switch_self_attack(optional=False)(ctx)
    return effect


def healing_wish():
    async def effect(ctx):
        heads = 0
        while True:
            results = await ctx.flip_coins(1, "Healing Wish")
            if not results or not results[0]:
                break
            heads += 1
        if heads <= 0:
            return
        pool = [p for p in ctx.my_pokemon_in_play()
                if (getattr(def_for(p.archetype_id), "hp", 0) or 0) >
                (p.get_attribute(AttrID.HP, 0) or 0)]
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if pick:
            await ctx.heal(heads * 10, pick)
    return effect


def flop_snipe_switch(amount: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if bench:
            pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
            if pick:
                await ctx.deal_damage(amount, target=pick,
                                     apply_modifiers=False)
        await switch_self_attack(optional=True)(ctx)
    return effect


def revenge_bonus(base: int = 20, bonus: int = 50):
    async def effect(ctx):
        ko = False
        state = getattr(ctx.board, "turn_state", None) if ctx.board else None
        if state is not None and hasattr(state, "knocked_out_last_turn"):
            ko = state.knocked_out_last_turn(ctx.player_id)
        elif hasattr(ctx, "ally_knocked_out_last_turn"):
            ko = ctx.ally_knocked_out_last_turn()
        await ctx.deal_damage(base + (bonus if ko else 0))
    return effect


def dynamic_punch(base: int = 60, bonus: int = 30):
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Dynamic Punch")
        if heads and heads[0]:
            await ctx.deal_damage(base + bonus)
            if ctx.defender is not None:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.CONFUSED)
        else:
            await ctx.deal_damage(base)
    return effect


def resonance_confused(base: int = 20, bonus: int = 20):
    return bonus_if(
        lambda ctx: bool(
            ctx.defender is not None and
            SpecialConditions.CONFUSED in (
                ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        ),
        bonus, base=base,
    )


def magnetic_ray():
    """Optional gust of Energy-bearing Bench, then damage."""
    async def effect(ctx):
        bench = [p for p in ctx.opponent_bench()
                 if any(is_energy_card(c) for c in p.children)]
        if bench:
            pick = await ctx.choose_pokemon(bench, "Switch an Energy-bearing Benched Pokémon into the Active Spot?", optional=True)
            if pick:
                await ctx.switch_active(ctx.opponent_id, pick)
        await ctx.deal_damage()
    return effect


def metal_blast(base: int = 50, per: int = 10):
    return damage_per(count_energy("self", energy_type=PokemonTypes.METAL),
                      per, base=base)


def psywave(base: int = 30, per: int = 20):
    return damage_per(count_energy("defender"), per, base=base)


def brine(amount: int = 40):
    async def effect(ctx):
        pool = []
        for p in ctx.opponent_pokemon_in_play():
            max_hp = getattr(def_for(p.archetype_id), "hp", 0) or 0
            hp = p.get_attribute(AttrID.HP, 0) or 0
            if max_hp and hp < max_hp:
                pool.append(p)
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if pick:
            await ctx.deal_damage(amount, target=pick,
                                 apply_modifiers=False)
    return effect


def flail_self(per: int = 10):
    return damage_per(damage_counters_on("self"), per, base=0)


def dark_pulse(per: int = 10):
    return damage_per(
        count_energy("mine", energy_type=PokemonTypes.DARKNESS),
        per, base=0,
    )


def attack_order(per: int = 10, element=PokemonTypes.GRASS):
    def count_fn(ctx):
        n = 0
        for side in (ctx.my_pokemon_in_play(), ctx.opponent_pokemon_in_play()):
            for p in side:
                types = p.get_attribute(AttrID.POKEMON_TYPES) or []
                if element.value in types or element in types:
                    n += 1
        return n
    return damage_per(count_fn, per, base=0)


def leaf_storm(counters: int = 2, element=PokemonTypes.GRASS):
    async def effect(ctx):
        await ctx.deal_damage()
        for p in ctx.my_pokemon_in_play():
            types = p.get_attribute(AttrID.POKEMON_TYPES) or []
            if element.value in types or element in types:
                await ctx.heal(counters * 10, p)
    return effect


def toxic_spikes_budew(poison_damage: int = 10):
    async def effect(ctx):
        dmg = poison_damage if evolved_from_named("Budew")(ctx) else 0
        if dmg:
            await ctx.deal_damage(dmg)
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.POISONED)
    return effect


def sweet_spike():
    async def effect(ctx):
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.ASLEEP)
        pool = [p for p in ctx.my_pokemon_in_play()
                if (getattr(def_for(p.archetype_id), "hp", 0) or 0) >
                (p.get_attribute(AttrID.HP, 0) or 0)]
        if pool:
            pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
            if pick:
                await ctx.heal(20, pick)
    return effect


def spike_whip_budew(amount: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        if named_under("Budew")(ctx):
            bench = ctx.opponent_bench()
            if bench:
                pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
                if pick:
                    await ctx.deal_damage(amount, target=pick,
                                         apply_modifiers=False)
    return effect


def ease_up_munchlax(base: int = 40, bonus: int = 30):
    async def effect(ctx):
        dmg = base + (bonus if evolved_from_named("Munchlax")(ctx) else 0)
        await ctx.deal_damage(dmg)
        if ctx.attacker is not None:
            await ctx.apply_special_condition(
                ctx.attacker, SpecialConditions.ASLEEP)
    return effect


def frustration(amount: int = 30):
    async def effect(ctx):
        pool = []
        for p in ctx.opponent_pokemon_in_play():
            max_hp = getattr(def_for(p.archetype_id), "hp", 0) or 0
            hp = p.get_attribute(AttrID.HP, 0) or 0
            if not max_hp or hp >= max_hp:
                pool.append(p)
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if pick:
            await ctx.deal_damage(amount, target=pick,
                                 apply_modifiers=False)
    return effect


def toxic_cloud():
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Toxic Cloud")
        if heads and heads[0] and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.POISONED)
            # Put 2 counters instead of 1 for Poison — set poison strength
            if hasattr(ctx, "set_poison_counters"):
                await ctx.set_poison_counters(ctx.defender, 2)
            else:
                await ctx.deal_damage(10, target=ctx.defender,
                                     apply_modifiers=False, as_counters=True)
    return effect


def accelerative_dive():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Accelerative Dive")
        if not heads or not heads[0]:
            return
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, prevent=True)
    return effect


def brave_heart(self_dmg: int = 100):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Brave Heart")
        if (not heads or not heads[0]) and ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker,
                                 apply_modifiers=False)
    return effect


def countercharge():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Countercharge")
        if not heads or not heads[0] or ctx.attacker is None or ctx.defender is None:
            return
        max_hp = getattr(def_for(ctx.attacker.archetype_id), "hp", 0) or 0
        hp = ctx.attacker.get_attribute(AttrID.HP, 0) or 0
        damage = max(0, max_hp - hp)
        if damage <= 0:
            return
        await ctx.heal(damage, ctx.attacker)
        await ctx.deal_damage(damage, target=ctx.defender,
                             apply_modifiers=False, as_counters=True)
    return effect


def leaf_honey():
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        pool = [c for c in a.children
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.GRASS.value)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard Grass Energy")
        if not picks:
            return
        await ctx.discard_cards(picks)
        bench = [p for p in ctx.my_bench()
                 if (PokemonTypes.GRASS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])
                     or PokemonTypes.GRASS in (p.get_attribute(AttrID.POKEMON_TYPES) or []))]
        damaged = [p for p in bench
                   if (getattr(def_for(p.archetype_id), "hp", 0) or 0) >
                   (p.get_attribute(AttrID.HP, 0) or 0)]
        if damaged:
            pick = await ctx.choose_pokemon(damaged, "Choose a Pokémon")
            if pick:
                await ctx.heal(9999, pick)
    return effect


def rock_wrecker():
    return ignore_resistance_attack(also=cant_attack_next_turn())


def vigorous_dash(bench: int = 30, self_dmg: int = 30):
    async def effect(ctx):
        await ctx.deal_damage()
        b = ctx.opponent_bench()
        if b:
            pick = await ctx.choose_pokemon(b, "Choose a Pokémon")
            if pick:
                await ctx.deal_damage(bench, target=pick, apply_modifiers=False)
        if ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
    return effect


def hydro_impact(amount: int = 80):
    async def effect(ctx):
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if pick:
            await ctx.deal_damage(amount, target=pick, apply_modifiers=False)
        await cant_attack_next_turn()(ctx)
    return effect


def synthesis_attach(energy_type=PokemonTypes.GRASS):
    def pred(c):
        return is_energy_card(c) and energy_provides_type(c, energy_type.value)
    return search_attach_energy(pred, count=1, to_self=False,
                                prompt="Attach Grass Energy to 1 of your Pokémon")


def outlet_search(energy_type=PokemonTypes.LIGHTNING):
    def pred(c):
        return is_energy_card(c) and energy_provides_type(c, energy_type.value)
    return search_to_hand(pred, count=1, minimum=0, reveal=True,
                          prompt="Choose a Lightning Energy card")


def call_for_friends_basic(element=PokemonTypes.WATER):
    def pred(c):
        if not is_basic_pokemon(c):
            return False
        d = def_for(c.archetype_id)
        types = getattr(d, "elements", None) or []
        return element in types or element.value in types
    return search_to_hand(pred, count=1, minimum=0, reveal=True,
                          prompt="Choose a Water Basic Pokémon")


def nasty_plot():
    return search_to_hand(None, count=1, minimum=0, reveal=False,
                          prompt="Choose any card")


def scavenge_trainer():
    return recover_from_discard(is_trainer_card, count=1, minimum=1, reveal=True,
                                prompt="Choose a Trainer card")


def flame_dance_attach():
    def pred(c):
        return is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)
    return attach_from_discard(pred, count=1, target="self",
                               prompt="Attach a Fire Energy from discard")


def flare_blitz():
    return self_energy_discard_attack(
        energy_type=PokemonTypes.FIRE, count=None)  # all Fire — may need custom


def flare_blitz_all_fire():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        dump = [c for c in list(a.children)
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)]
        if dump:
            await ctx.discard_cards(dump)
    return effect


def magnetize_passive() -> Passive:
    """Retreat cost 0 for Active if it has Metal Energy."""

    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            if not is_in_active_spot(pokemon):
                return cost
            kids = list(getattr(pokemon, "children", []) or [])
            if any(is_energy_card(c) and energy_provides_type(c, PokemonTypes.METAL.value)
                   for c in kids):
                return 0
            return cost

    return _P()


# --- Trainers -----------------------------------------------------------------

def pokedex_handy():
    """Look at top 2; take 1; other to bottom."""
    return look_at_top(2, take=1, rest="bottom",
                      prompt="Choose a card to put into your hand")


def professor_rowan():
    async def effect(ctx):
        hand = [c for c in ctx.hand() if c is not ctx.source]
        if not hand and ctx.source in ctx.hand():
            # only this card — can't play (condition should block)
            return
        keep = await ctx.choose_cards(
            list(ctx.hand()), 1, minimum=1,
            prompt="Choose 1 card to keep")
        if not keep:
            return
        rest = [c for c in ctx.hand() if c not in keep]
        if rest:
            await ctx.shuffle_into_deck(rest)
        await ctx.draw_cards(4)
    return effect


def professor_rowan_condition(board, player_id, card=None):
    hand = board.hand_cards(player_id) if hasattr(board, "hand_cards") else []
    # Need at least one other card besides Rowan itself when played from hand
    return len(hand) >= 2


def rival_supporter():
    async def effect(ctx):
        top = ctx.deck_top(5)
        if not top:
            return
        # Opponent chooses 3 for you to take
        if len(top) <= 3:
            await ctx.put_in_hand(top, reveal=True)
            await ctx.shuffle_deck()
            return
        picks = await ctx.choose_cards(
            top, 3, minimum=3, player_id=ctx.opponent_id,
            prompt="Choose 3 cards for your opponent's hand")
        if not picks:
            picks = top[:3]
        rest = [c for c in top if c not in picks]
        await ctx.put_in_hand(picks, reveal=True)
        if rest:
            await _put_stack_on_top(ctx, rest)
        await ctx.shuffle_deck()
    return effect


def night_pokemon_center():
    async def effect(ctx):
        pool = ctx.my_pokemon_in_play()
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if not pick:
            return
        target = pick
        results = await ctx.flip_coins(2, "Night Pokémon Center")
        if all(results):
            await ctx.heal(9999, target)
        elif not any(results):
            energies = [c for c in list(target.children) if is_energy_card(c)]
            if energies:
                await ctx.discard_cards(energies)
    return effect


def speed_stadium_ability():
    """Flip until tails; draw per heads. Offered once per turn to each player."""
    async def effect(ctx):
        heads = 0
        while True:
            results = await ctx.flip_coins(1, "Speed Stadium")
            if not results or not results[0]:
                break
            heads += 1
        if heads:
            await ctx.draw_cards(heads)
    return effect


def plus_power_passive(amount: int = 10) -> Passive:
    """Attacks from holder do +amount to Active (before W/R). Discard EOT via grant."""
    return strength_charm_passive(amount)


def mime_draw_equal_opponent():
    async def effect(ctx):
        await ctx.shuffle_into_deck(list(ctx.hand()))
        opp_n = len(ctx.hand(ctx.opponent_id))
        if opp_n:
            await ctx.draw_cards(opp_n)
    return effect



def force_palm():
    async def effect(ctx):
        n = damage_counters_on("self")(ctx)
        if n <= 0:
            return
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if pick:
            await ctx.deal_damage(n * 10, target=pick,
                                 apply_modifiers=False, as_counters=True)
    return effect


def detect_flip():
    return flip_protection(prevent=True, effects_too=True, title="Detect")


def splashing_turn():
    return switch_self_attack(optional=False)


def wind_wave_recover(max_count: int = 5):
    def pred(c):
        return is_pokemon_card(c) or is_supporter_card(c)
    async def effect(ctx):
        await recover_from_discard(
            pred, count=max_count, minimum=0, reveal=True, to="deck",
            prompt="Choose Pokémon and Supporter cards to shuffle into your deck",
        )(ctx)
    return effect


def blowing_wind_bench_to_deck():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Blowing Wind")
        if not heads or not heads[0]:
            return
        bench = ctx.my_bench()
        if not bench:
            return
        pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
        if not pick:
            return
        from spirit.game.card_effects.pokemon import full_stack
        await _put_stack_on_top(ctx, full_stack(pick))
    return effect


def burning_head():
    """Look at top 3; take 1; discard the other 2."""
    async def effect(ctx):
        top = ctx.deck_top(3)
        if not top:
            return
        picks = await ctx.choose_cards(
            top, 1, minimum=0, prompt="Choose a card to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
        rest = [c for c in top if c not in picks]
        if rest:
            await ctx.discard_cards(rest)
    return effect


def flare_up(count: int = 8, energy_type=PokemonTypes.FIRE):
    def pred(c):
        return is_energy_card(c) and energy_provides_type(c, energy_type.value)
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if pred(c)]
        if len(pool) < count:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=count,
            prompt=f"Choose {count} Fire Energy cards to shuffle into your deck")
        if not picks or len(picks) < count:
            return
        await ctx.shuffle_into_deck(picks)
    return effect


def flash_cannon_devolve():
    """May return all Energy to hand; if you do, devolve Defending highest stage."""
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        if a is None:
            return
        energies = [c for c in list(a.children) if is_energy_card(c)]
        if not energies:
            return
        if not await ctx.ask_yes_no("Return all Energy to your hand to devolve the Defending Pokémon?"):
            return
        await ctx.put_in_hand(energies, reveal=False)
        d = ctx.defender
        if d is None:
            return
        # Highest stage under the top: the top card itself if evolved
        stage = d.get_attribute(AttrID.STAGE)
        if stage in (None, PokemonStage.BASIC.value):
            return
        if hasattr(ctx, "devolve"):
            await ctx.devolve(d, to_hand=False, shuffle_into_deck=True)
        elif hasattr(ctx, "remove_highest_evolution"):
            await ctx.remove_highest_evolution(d, destination="deck")
        else:
            # Manual: move the evolution card to opponent deck, promote under-card
            await ctx.shuffle_into_deck([d], ctx.opponent_id)
    return effect


def dark_palm():
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if len(bench) < 4:
            return
        pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
        if not pick:
            return
        from spirit.game.card_effects.pokemon import full_stack
        await ctx.shuffle_into_deck(full_stack(pick), ctx.opponent_id)
    return effect


def dark_palm_condition(board, player_id, pokemon=None):
    opp = next(p for p in board.player_ids if p != player_id)
    active = board.active_pokemon(opp)
    bench = [p for p in board.pokemon_in_play(opp) if p is not active]
    return len(bench) >= 4


def disable_attack_flip():
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Disable")
        if not heads or not heads[0] or ctx.defender is None:
            return
        abilities = ctx.defender.get_attribute(AttrID.PIE_ABILITIES) or []
        attacks = [a for a in abilities if isinstance(a, dict) and a.get("abilityType") == "Attack"]
        if not attacks:
            return
        labels = [a.get("title") or a.get("abilityID") for a in attacks]
        idx = await ctx.choose("Choose an attack to Disable", labels)
        if idx is None:
            return
        aid = attacks[idx].get("abilityID")
        if aid:
            ctx.session.turn_state.lock_attack(ctx.defender.entity_id, aid)
    return effect


def intense_voltage():
    """Move a Lightning Energy from any of yours onto Electivire; needs Elekid under."""
    async def effect(ctx):
        src = ctx.source
        if src is None or not named_under("Elekid")(type("C", (), {"attacker": src})()):
            # named_under expects ctx.attacker — set manually
            pass
        # Check Elekid under source
        has_elekid = False
        for child in list(getattr(src, "children", []) or []):
            if "elekid" in _display(child).lower():
                has_elekid = True
                break
        if not has_elekid:
            return
        # Collect Lightning Energy on other Pokemon
        movers = []
        for p in ctx.my_pokemon_in_play():
            for c in p.children:
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.LIGHTNING.value):
                    movers.append(c)
        if not movers:
            return
        picks = await ctx.choose_cards(
            movers, 1, minimum=0, prompt="Move a Lightning Energy to Electivire")
        if picks:
            await ctx.attach_energy(picks[0], src)
    return effect


def intense_voltage_condition(board, player_id, pokemon=None):
    if pokemon is None:
        return False
    for child in list(getattr(pokemon, "children", []) or []):
        if "elekid" in _display(child).lower():
            return True
    return False


def supreme_command():
    """Exile up to 2 cards from opponent hand beside Defending until end of their next turn."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if not hand:
            return
        n = min(2, len(hand))
        picks = await ctx.choose_cards(
            hand, n, minimum=0,
            prompt="Choose up to 2 cards from opponent's hand")
        if not picks:
            return
        # Park beside defending — use set-aside / attach-as-marker if available
        if hasattr(ctx, "set_aside"):
            await ctx.set_aside(picks, return_after_turns=2, to_owner_hand=True)
        else:
            # Fallback: attach face-down under defending as markers, restore later via temp
            d = ctx.my_active()  # Defending from our view is opponent active
            d = ctx.opponent_active() if hasattr(ctx, "opponent_active") else ctx.defender
            for c in picks:
                if d is not None and hasattr(ctx, "attach_card"):
                    await ctx.attach_card(c, d)
            # Schedule return — best-effort via temp passive END
            if hasattr(ctx, "add_passive_through_opponents_turn") and d is not None:
                class _Return(Passive):
                    def __init__(self, cards):
                        self.cards = cards
                    async def on_end_of_turn(self, ctx2, carrier):
                        await ctx2.put_in_hand(self.cards, reveal=False)
                ctx.add_passive_through_opponents_turn(d, _Return(picks))
    return effect


def lightning_star():
    async def effect(ctx):
        await ctx.deal_damage()
        a = ctx.attacker
        bench = ctx.my_bench()
        if a is None or not bench:
            return
        energies = [c for c in list(a.children)
                    if is_energy_card(c) and energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
        if not energies:
            return
        pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
        if pick:
            for e in energies:
                await ctx.attach_energy(e, pick)
    return effect


def gleam_eyes_on_evolve():
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            await ctx.reveal_hand(of_player=ctx.opponent_id)
        bench = ctx.opponent_bench()
        if len(bench) >= 5:
            return
        basics = [c for c in hand if is_basic_pokemon(c)]
        if not basics:
            return
        picks = await ctx.choose_cards(
            basics, 1, minimum=0,
            prompt="Put a Basic Pokémon onto your opponent's Bench")
        if not picks:
            return
        card = picks[0]
        ok = await ctx.bench_pokemon(card)
        if not ok:
            return
        await ctx.switch_active(ctx.opponent_id, card)
    return effect


def heave(per_heads: int = 30, coins: int = 2, discard_n: int = 2):
    async def effect(ctx):
        hand = list(ctx.hand())
        if len(hand) < discard_n:
            return
        dumped = await ctx.discard_from_hand(discard_n, minimum=discard_n,
                                             prompt=f"Discard {discard_n} cards")
        if not dumped or len(dumped) < discard_n:
            return
        results = await ctx.flip_coins(coins, "Heave")
        await ctx.deal_damage(per_heads * sum(1 for r in results if r))
    return effect


def see_beyond():
    async def effect(ctx):
        prizes = list(ctx.my_prizes()) if hasattr(ctx, "my_prizes") else []
        face_down = [p for p in prizes if not getattr(p, "face_up", False)]
        if not face_down:
            return
        hand = list(ctx.hand())
        if not hand:
            return
        put = await ctx.choose_cards(hand, 1, minimum=1, prompt="Put which card as a face-up Prize?")
        if not put:
            return
        # Swap mechanics
        if hasattr(ctx, "replace_prize"):
            taken = await ctx.replace_prize(put[0], face_up=True)
            if taken:
                await ctx.put_in_hand([taken], reveal=False)
        else:
            # Best-effort stub path
            pass
    return effect


def dirty_trick():
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Dirty Trick")
        if not heads or not heads[0]:
            return
        pool = [p for p in ctx.opponent_pokemon_in_play()
                if any(is_energy_card(c) for c in p.children)]
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon")
        if not pick:
            return
        energies = [c for c in pick.children if is_energy_card(c)]
        chosen = await ctx.choose_cards(energies, 1, minimum=1, prompt="Discard which Energy?")
        if chosen:
            await ctx.discard_cards(chosen)
    return effect


def spacial_rend():
    from spirit.game.attributes import TrainerType
    def is_stadium(c):
        d = def_for(c.archetype_id)
        return getattr(d, "trainer_type", None) == TrainerType.STADIUM
    async def effect(ctx):
        await search_to_hand(is_stadium, count=1, minimum=0, reveal=True,
                             prompt="Choose a Stadium card")(ctx)
        stadium = ctx.stadium_in_play() if hasattr(ctx, "stadium_in_play") else None
        if stadium is not None:
            await ctx.discard_cards([stadium])
    return effect


def transback():
    async def effect(ctx):
        await ctx.deal_damage()
        if not await ctx.ask_yes_no("Flip to discard Energy and put Defending on top of deck?"):
            return
        heads = await ctx.flip_coins(1, "Transback")
        if not heads or not heads[0]:
            return
        a = ctx.attacker
        if a is not None:
            energies = [c for c in list(a.children) if is_energy_card(c)]
            if energies:
                await ctx.discard_cards(energies)
        d = ctx.defender
        if d is None:
            return
        from spirit.game.card_effects.pokemon import full_stack
        await _put_stack_on_top(ctx, full_stack(d))
    return effect


def blaze_up(bench_dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Blaze Up")
        if heads and heads[0]:
            return
        a = ctx.attacker
        if a is not None:
            fires = [c for c in list(a.children)
                     if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)]
            if fires:
                picks = await ctx.choose_cards(fires, 1, minimum=1, prompt="Discard a Fire Energy")
                if picks:
                    await ctx.discard_cards(picks)
        for p in ctx.opponent_bench():
            await ctx.deal_damage(bench_dmg, target=p, apply_modifiers=False)
    return effect


def storm_up(base: int = 30, bonus: int = 20):
    async def effect(ctx):
        stadium = ctx.stadium_in_play() if hasattr(ctx, "stadium_in_play") else None
        extra = bonus if stadium is not None else 0
        await ctx.deal_damage(base + extra)
        if stadium is not None:
            await ctx.discard_cards([stadium])
    return effect


def crash_impact(self_dmg: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
        # Opponent switches
        if hasattr(ctx, "force_opponent_switch"):
            await force_opponent_switch()(ctx)
        else:
            bench = ctx.opponent_bench()
            if bench:
                pick = await ctx.choose_pokemon(bench, "Choose a Pokémon", player_id=ctx.opponent_id)
                if pick:
                    await ctx.switch_active(ctx.opponent_id, pick)
    return effect


def earth_fissure_on_evolve(mill: int = 3):
    async def effect(ctx):
        top = ctx.opponent_deck_top(mill) if hasattr(ctx, "opponent_deck_top") else []
        if not top and hasattr(ctx, "deck_top"):
            # deck_top of opponent
            top = ctx.deck_top(mill, player_id=ctx.opponent_id) if False else []
        if hasattr(ctx, "mill_opponent"):
            await ctx.mill_opponent(mill)
        else:
            # Use mill_attack style
            cards = []
            if hasattr(ctx, "opponent_deck_cards"):
                cards = list(ctx.opponent_deck_cards())[:mill]
            if cards:
                await ctx.discard_cards(cards)
            elif hasattr(ctx, "discard_from_deck"):
                await ctx.discard_from_deck(mill, player_id=ctx.opponent_id)
    return effect


def bide_survive():
    """Flip: if heads, survive KO at 10 HP during opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Bide")
        if heads and heads[0] and ctx.attacker is not None:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker, guts_survive_passive(hp_floor=10, title="Bide", flip=False))
    return effect


def darkness_fan():
    async def effect(ctx):
        if not is_in_active_spot(ctx.source):
            return
        heads = await ctx.flip_coins(1, "Darkness Fan")
        if not heads or not heads[0]:
            return
        bench = [p for p in ctx.opponent_bench()
                 if p.get_attribute(AttrID.STAGE) not in (None, PokemonStage.BASIC.value)]
        if not bench:
            return
        pick = await ctx.choose_pokemon(bench, "Choose a Pokémon")
        if not pick:
            return
        if hasattr(ctx, "devolve_to_hand"):
            await ctx.devolve_to_hand(pick)
        elif hasattr(ctx, "remove_highest_evolution"):
            await ctx.remove_highest_evolution(pick, destination="hand")
    return effect


def forest_murmurs():
    async def effect(ctx):
        my_p = count_prizes_remaining("mine")(ctx)
        opp_p = count_prizes_remaining("opponent")(ctx)
        if my_p <= opp_p:
            return
        await force_opponent_switch()(ctx)
    return effect


def forest_murmurs_condition(board, player_id, pokemon=None):
    # Rough: more prizes remaining than opponent
    try:
        from spirit.game.content.definitions import prize_value  # noqa
    except Exception:
        pass
    return True  # gate lightly; effect rechecks


def unown_analyze():
    async def effect(ctx):
        top = ctx.deck_top(2)
        if not top:
            return
        # Reorder
        if len(top) == 1:
            return
        order = await ctx.choose_cards(top, len(top), minimum=len(top),
                                       prompt="Put back on top in order (first = top)")
        if order:
            for c in reversed(order):
                await ctx.put_on_top_of_deck(c)
    return effect


def unown_bounce():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "BOUNCE")
        if not heads or not heads[0]:
            return
        src = ctx.source
        if src is None:
            return
        from spirit.game.card_effects.pokemon import full_stack
        await ctx.shuffle_into_deck(full_stack(src), ctx.player_id)
    return effect


def unown_call():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "CALL")
        if not heads or not heads[0]:
            return
        def pred(c):
            d = def_for(c.archetype_id)
            name = (getattr(d, "display_name", None) or "")
            return name.startswith("Unown")
        await search_to_hand(pred, count=1, minimum=0, reveal=True,
                             prompt="Choose an Unown")(ctx)
    return effect


def unown_draw():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "DRAW")
        if heads and heads[0]:
            await ctx.draw_cards(1)
    return effect


def unown_bench_condition(board, player_id, pokemon=None):
    if pokemon is None:
        return False
    active = board.active_pokemon(player_id)
    return pokemon is not active


# Fix extrasensory default bonus to match Noctowl (+50)
def extrasensory_same_hand(base: int = 30, bonus: int = 50):
    async def effect(ctx):
        extra = bonus if len(ctx.hand()) == len(ctx.hand(ctx.opponent_id)) else 0
        await ctx.deal_damage(base + extra)
    return effect
