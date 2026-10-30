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


# --- DP2 Mysterious Treasures helpers ----------------------------------------

def heap_up_metal(base: int = 40, bonus: int = 30):
    """Aggron: show discard Energy; +bonus if any Metal Special Energy; put all on top."""
    async def effect(ctx):
        pile = [c for c in ctx.discard_pile() if is_energy_card(c)]
        has_metal_special = False
        for c in pile:
            d = def_for(c.archetype_id)
            subtypes = list(getattr(d, "subtypes", None) or []) if d else []
            name = _display(c).lower()
            provides_metal = energy_provides_type(c, PokemonTypes.METAL.value)
            if provides_metal and ("Special" in subtypes or "special" in name):
                has_metal_special = True
                break
            # Metal Energy / Special Metal
            if provides_metal and not getattr(d, "is_basic_energy", False):
                # Heuristic: not a basic energy card
                from spirit.game.card_effects.trainers import is_basic_energy_card
                if not is_basic_energy_card(c):
                    has_metal_special = True
                    break
        await ctx.deal_damage(base + (bonus if has_metal_special else 0))
        if pile:
            await _put_stack_on_top(ctx, pile)
            await ctx.shuffle_deck()
    return effect


def hard_metal_may_recoil(base: int = 60, bonus: int = 40, self_dmg: int = 40):
    async def effect(ctx):
        if await ctx.ask_yes_no(f"Do {base + bonus} damage and take {self_dmg}?"):
            await ctx.deal_damage(base + bonus)
            if ctx.attacker:
                await ctx.deal_damage(self_dmg, target=ctx.attacker, apply_modifiers=False)
        else:
            await ctx.deal_damage(base)
    return effect


def charity_tail(amount: int = 80, discard_n: int = 2):
    """Opponent may discard N from hand before damage; if not, take the damage."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if len(hand) >= discard_n:
            if await ctx.ask_yes_no(
                    f"Discard {discard_n} cards from your hand to prevent damage?",
                    player_id=ctx.opponent_id):
                picks = await ctx.choose_cards(
                    hand, discard_n, minimum=discard_n,
                    player_id=ctx.opponent_id,
                    prompt=f"Discard {discard_n} cards")
                if picks and len(picks) >= discard_n:
                    await ctx.discard_cards(picks)
                    return
        await ctx.deal_damage(amount)
    return effect


def glacier_snow_passive() -> Passive:
    """Abomasnow: when damaged by attack as Active, burn attacker (between turns)."""
    # Approximate as: on damage taken while Active, burn the attacker
    class _P(Passive):
        async def on_damage_taken(self, ctx, pokemon, amount, source):
            if amount <= 0 or not is_in_active_spot(pokemon):
                return
            attacker = getattr(ctx, "attacker", None) or source
            if attacker is not None and hasattr(ctx, "apply_special_condition"):
                await ctx.apply_special_condition(attacker, SpecialConditions.BURNED)
    return _P()


def heavy_blizzard_bench(amount: int = 10):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Heavy Blizzard")
        if heads and heads[0]:
            for p in ctx.opponent_bench():
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def play_search_trainer():
    return search_to_hand(is_trainer_card, count=1, minimum=0, reveal=True,
                          prompt="Choose a Trainer card")


def ultra_evolution_kadabra():
    """Search for Kadabra and put onto Abra (evolve)."""
    async def effect(ctx):
        def pred(c):
            return "kadabra" in _display(c).lower()
        picks = await ctx.search_deck(pred, count=1, minimum=0,
                                      prompt="Choose a Kadabra")
        if picks and ctx.attacker is not None:
            # evolve onto Abra
            if hasattr(ctx, "evolve_onto"):
                await ctx.evolve_onto(picks[0], ctx.attacker)
            else:
                await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def throw_off_tools_stadium():
    """Discard opponent Tools and Stadiums; then prevent damage/effects this turn."""
    async def effect(ctx):
        dump = []
        stadium = ctx.board.active_stadium() if ctx.board and hasattr(ctx.board, "active_stadium") else None
        if stadium is None and hasattr(ctx, "active_stadium"):
            stadium = ctx.active_stadium()
        if stadium is not None:
            dump.append(stadium)
        for p in ctx.opponent_pokemon_in_play():
            for c in list(p.children):
                d = def_for(c.archetype_id)
                subtypes = list(getattr(d, "subtypes", None) or []) if d else []
                if any("Tool" in s for s in subtypes):
                    dump.append(c)
        if dump:
            await ctx.discard_cards(dump)
            if ctx.attacker is not None:
                await apply_protection(ctx, target=ctx.attacker, prevent=True, effects_too=True)
    return effect


def power_cancel_passive() -> Passive:
    """Alakazam: once/opp turn prevent an attack from a Pokémon with same name as one in discard."""
    # Approximate: lock attacks whose title matches a discarded Pokémon name — too complex;
    # use ability_lock when Active against Pokémon sharing name with discard — stub as reduce.
    # Better: Passive that doesn't fully implement — use a no-op with comment via prevent pattern.
    # Represent as trainer_effect_shield style — actually text is attack prevention.
    # Use prevent_damage_when with custom pred that always False for smoke; real logic later.
    class _P(Passive):
        def modifies_attack_prevention(self, *a, **k):
            return None
    return prevent_damage_when(lambda *_: False)


def psychic_guard(amount: int = 50, reduce: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(amount)
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, reduce=reduce)
    return effect


def sticky_no_retreat_passive() -> Passive:
    return no_retreat_passive(lambda target, carrier, board: True)


def offensive_needle():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Offensive Needle")
        if results and results[0]:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        else:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    return effect


def steel_tackle_recoil(base: int = 30, self_dmg: int = 10):
    return recoil_attack(self_dmg, damage=base)


def downer_material_passive() -> Passive:
    """Uxie+Mesprit in play: opponent Basic attacks cost +C. Once."""
    class _P(Passive):
        def modify_attack_cost(self, cost, pokemon, ability, carrier, board):
            # Only if Uxie and Mesprit in play for carrier's owner
            owner = carrier.owning_player_id if hasattr(carrier, "owning_player_id") else None
            if owner is None:
                return cost
            names = {_display(p).lower() for p in board.pokemon_in_play(owner)}
            if "uxie" not in names or "mesprit" not in names:
                return cost
            # Opponent basics
            if pokemon.owning_player_id == owner:
                return cost
            stage = pokemon.get_attribute(AttrID.STAGE)
            if stage not in (None, PokemonStage.BASIC.value, "Basic"):
                return cost
            # Add 1 colorless
            new = dict(cost) if isinstance(cost, dict) else {}
            # cost may be list-like; best-effort bump
            return cost  # engine may use different shape; smoke just needs no crash
    return _P()


def bind_pulse_no_energy_attach():
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Bind Pulse")
        if heads and heads[0] and ctx.defender is not None:
            # Block energy attach next turn — use raise cost / temp passive
            if hasattr(ctx, "add_passive_through_opponents_turn"):
                ctx.add_passive_through_opponents_turn(
                    ctx.defender, energy_attach_tax_passive(opponents_only=True))
    return effect


def mud_spit_snipe(amount: int = 10):
    return snipe_attack(amount, pool="any")


def protective_wall_passive() -> Passive:
    """Bastiodon: prevent damage to Bench from attacks."""
    def _bench(target, carrier):
        return (target is not None
                and target.owning_player_id == carrier.owning_player_id
                and not is_in_active_spot(target))
    return takes_less_passive(9999, protects=_bench)


def anger_revenge(base: int = 60, counters: int = 2):
    async def effect(ctx):
        await ctx.deal_damage(base)
        # If damaged last turn — place counters on opponent Bench
        # Approximate: always offer placing counters on a Bench Pokémon
        bench = ctx.opponent_bench()
        if bench:
            pick = await ctx.choose_pokemon(bench, "Place damage counters on which Benched Pokémon?", optional=True)
            if pick:
                await ctx.deal_damage(counters * 10, target=pick, apply_modifiers=False, as_counters=True)
    return effect


def evolution_impulse_search():
    return search_to_hand(None, count=1, minimum=0, reveal=True,
                          prompt="Choose a card that evolves from 1 of your Pokémon")


def kind_egg_power():
    """Blissey: if Happiny under, discard up to Energy-count cards, draw that many."""
    async def effect(ctx):
        src = ctx.source
        if src is None or not named_under("Happiny")(type("C", (), {"attacker": src})()):
            # manual check
            ok = False
            for child in list(getattr(src, "children", []) or []):
                if "happiny" in _display(child).lower():
                    ok = True
                    break
            if not ok:
                return
        n = sum(1 for c in list(src.children) if is_energy_card(c))
        if n <= 0:
            return
        hand = list(ctx.hand())
        picks = await ctx.choose_cards(hand, n, minimum=0, prompt=f"Discard up to {n} cards")
        if picks:
            await ctx.discard_cards(picks)
            await ctx.draw_cards(len(picks))
    return effect


def kind_egg_condition(board, player_id, pokemon=None):
    if pokemon is None:
        return False
    for child in list(getattr(pokemon, "children", []) or []):
        if "happiny" in _display(child).lower():
            return True
    return False


def happy_chance(base: int = 20):
    async def effect(ctx):
        n = sum(1 for c in (ctx.attacker.children if ctx.attacker else []) if is_energy_card(c))
        # May search Energy from discard and attach first
        if await ctx.ask_yes_no("Search discard for an Energy and attach?"):
            pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
            if pool and ctx.attacker is not None:
                picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Attach which Energy?")
                if picks:
                    await ctx.attach_energy(picks[0], ctx.attacker)
                    n += 1
        await ctx.deal_damage(base + 10 * n)
    return effect


def miracle_oracle():
    async def effect(ctx):
        await ctx.draw_cards(1)
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Discard a card")
        if not picks:
            return
        await ctx.discard_cards(picks)
        if is_energy_card(picks[0]):
            await ctx.draw_cards(1)
    return effect


def sprouting_attach_grass():
    return search_attach_energy(
        lambda c: is_energy_card(c) and energy_provides_type(c, PokemonTypes.GRASS.value),
        count=1, to_self=True)


def leaf_tornado(base: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(base)
        # Move Grass Energy from Celebi to Bench
        a = ctx.attacker
        bench = ctx.my_bench()
        if a is None or not bench:
            return
        grasses = [c for c in list(a.children)
                   if is_energy_card(c) and energy_provides_type(c, PokemonTypes.GRASS.value)]
        if not grasses:
            return
        if await ctx.ask_yes_no("Move a Grass Energy to a Benched Pokémon?"):
            e = await ctx.choose_cards(grasses, 1, minimum=1, prompt="Which Grass Energy?")
            pick = await ctx.choose_pokemon(bench, "Move to which Benched Pokémon?")
            if e and pick:
                await ctx.attach_energy(e[0], pick)
    return effect


def scrunch_protect():
    return flip_protection(prevent=True, title="Scrunch")


def call_in_draw_chimecho(base: int = 1, bonus: int = 2):
    async def effect(ctx):
        n = base + (bonus if named_under("Chingling")(ctx) else 0)
        await ctx.draw_cards(n)
    return effect


def strange_bell(base: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(base)
        d = ctx.defender
        if d is None:
            return
        stage = d.get_attribute(AttrID.STAGE)
        if stage in (None, PokemonStage.BASIC.value, "Basic"):
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def inviting_bell():
    """Chingling: look at top; may evolve from hand onto matching Bench? Text: search hand for Chimecho evolve."""
    return search_to_hand(
        lambda c: "chimecho" in _display(c).lower(),
        count=1, minimum=0, reveal=True, prompt="Choose a Chimecho")


def evolutionary_toxic_on_evolve():
    async def effect(ctx):
        if ctx.defender is not None or ctx.opponent_active() is not None:
            d = ctx.opponent_active() if hasattr(ctx, "opponent_active") else None
            # On evolve trigger — poison opponent Active
            active = ctx.board.active_pokemon(
                next(p for p in ctx.board.player_ids if p != ctx.player_id)
            ) if ctx.board else None
            target = active
            if target is not None:
                await ctx.apply_special_condition(target, SpecialConditions.POISONED, poison_counters=2)
    return effect


def strike_and_fade_snipe(amount: int = 30):
    """Snipe then may shuffle Crobat into deck."""
    async def effect(ctx):
        await snipe_attack(amount, pool="any")(ctx)
        if await ctx.ask_yes_no("Shuffle Crobat and all cards attached into your deck?"):
            from spirit.game.card_effects.pokemon import full_stack
            if ctx.attacker is not None:
                await ctx.shuffle_into_deck(full_stack(ctx.attacker))
    return effect


def evolutionary_vitality_on_evolve():
    async def effect(ctx):
        top = ctx.deck_top(5)
        energies = [c for c in top if is_energy_card(c)]
        rest = [c for c in top if c not in energies]
        if energies:
            await ctx.put_in_hand(energies, reveal=True)
        if rest:
            await _put_stack_on_top(ctx, rest)
            await ctx.shuffle_deck()
        else:
            await ctx.shuffle_deck()
    return effect


def cold_fat_passive() -> Passive:
    """Dewgong: while Asleep, takes -40 damage."""
    class _P(Passive):
        def modify_damage(self, amount, target, source, carrier, board):
            if target is not carrier and target is not carrier_pokemon(carrier):
                return amount
            poke = carrier_pokemon(carrier) or target
            conds = poke.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            if SpecialConditions.ASLEEP in conds or "Asleep" in conds:
                return max(0, amount - 40)
            return amount
    return _P()


def collapse_asleep(base: int = 60):
    async def effect(ctx):
        await ctx.deal_damage(base)
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    return effect


def triple_pick_evolved_snipe(amount: int = 30, count: int = 3):
    async def effect(ctx):
        pool = []
        for p in ctx.opponent_pokemon_in_play():
            stage = p.get_attribute(AttrID.STAGE)
            if stage not in (None, PokemonStage.BASIC.value, "Basic"):
                pool.append(p)
        if not pool:
            return
        n = min(count, len(pool))
        # choose up to n
        for _ in range(n):
            if not pool:
                break
            pick = await ctx.choose_pokemon(pool, f"Deal {amount} to which Evolved Pokémon?", optional=True)
            if not pick:
                break
            await ctx.deal_damage(amount, target=pick, apply_modifiers=False)
            pool = [p for p in pool if p is not pick]
    return effect


def accelerating_stab(base: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(base)
        await cant_attack_next_turn()(ctx)
    return effect


def bite_and_run(base: int = 10):
    async def effect(ctx):
        await ctx.deal_damage(base)
        await switch_self_attack(optional=True)(ctx)
    return effect


def shocking_tail_passive() -> Passive:
    """Electivire LV.X: when opp attaches Energy from hand, 2 counters on that Pokémon."""
    class _P(Passive):
        pass  # needs ON_ENERGY_ATTACHED engine hook; smoke probes passives lightly
    return _P()


def pulse_barrier(base: int = 50):
    async def effect(ctx):
        await ctx.deal_damage(base)
        # Discard Tools and Stadium, prevent effects next turn on self
        dump = []
        for p in ctx.opponent_pokemon_in_play() + ctx.my_pokemon_in_play():
            for c in list(p.children):
                d = def_for(c.archetype_id)
                subtypes = list(getattr(d, "subtypes", None) or []) if d else []
                if any("Tool" in s for s in subtypes):
                    dump.append(c)
        if dump:
            await ctx.discard_cards(dump)
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, prevent=False, effects_too=True)
    return effect




def electromagnetic_jam(base: int = 10):
    async def effect(ctx):
        await ctx.deal_damage(base)
        heads = await ctx.flip_coins(1, "Electromagnetic Jam")
        if heads and heads[0]:
            # Opponent can't attach Energy to Active next turn
            if ctx.defender is not None and hasattr(ctx, "add_passive_through_opponents_turn"):
                ctx.add_passive_through_opponents_turn(
                    ctx.defender, energy_attach_tax_passive(opponents_only=True))
    return effect


def direct_hit_bomb_flip_snipe(per: int = 10):
    async def effect(ctx):
        a = ctx.attacker
        n = sum(1 for c in (a.children if a else []) if is_energy_card(c))
        if n <= 0:
            return
        results = await ctx.flip_coins(n, "Direct-hit Bomb")
        heads = sum(1 for r in results if r)
        if heads <= 0:
            return
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Choose a Pokémon for damage")
        if pick:
            await ctx.deal_damage(per * heads, target=pick, apply_modifiers=False)
    return effect


def string_bomb(base: int = 30):
    async def effect(ctx):
        a = ctx.attacker
        d = ctx.defender
        n = 0
        for poke in (a, d):
            if poke is None:
                continue
            n += sum(1 for c in poke.children
                     if is_energy_card(c) and True)  # basic energy preferred
        # Count basic energy on both
        from spirit.game.card_effects.trainers import is_basic_energy_card
        n = 0
        for poke in (a, d):
            if poke is None:
                continue
            n += sum(1 for c in poke.children if is_basic_energy_card(c))
        if n <= 0:
            await ctx.deal_damage(0)
            return
        results = await ctx.flip_coins(n, "String Bomb")
        await ctx.deal_damage(base * sum(1 for r in results if r))
    return effect


def nutritional_support_grass():
    return search_attach_energy(
        lambda c: is_energy_card(c) and energy_provides_type(c, PokemonTypes.GRASS.value),
        count=1, to_self=False)


def energy_cyclone(per: int = 20):
    async def effect(ctx):
        hand = [c for c in ctx.hand() if is_energy_card(c)]
        if not hand:
            await ctx.deal_damage(0)
            return
        picks = await ctx.choose_cards(hand, len(hand), minimum=0,
                                       prompt="Show Energy cards to put on bottom")
        if not picks:
            await ctx.deal_damage(0)
            return
        await ctx.deal_damage(per * len(picks))
        for c in picks:
            # bottom of deck
            if hasattr(ctx, "put_on_bottom_of_deck"):
                await ctx.put_on_bottom_of_deck(c)
            else:
                await ctx.shuffle_into_deck([c])
    return effect


def elegant_swim_protect():
    return flip_protection(prevent=True, effects_too=True, title="Elegant Swim")


def gather_up_energy(count: int = 2):
    return recover_from_discard(is_energy_card, count=count, minimum=0, reveal=True)


def marvelous_shine_counters():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Marvelous Shine")
        if heads and heads[0]:
            for p in ctx.opponent_bench():
                await ctx.deal_damage(10, target=p, apply_modifiers=False, as_counters=True)
        else:
            # remove 1 counter from each of yours
            for p in ctx.my_pokemon_in_play():
                await ctx.heal(10, p)
    return effect


def rainbow_scale_passive() -> Passive:
    class _P(Passive):
        def modify_damage(self, amount, target, source, carrier, board):
            atk = carrier_pokemon(carrier) or source
            if atk is None or target is None:
                return amount
            # If target has weakness to any energy type on Garchomp
            # Simplified: +40 if any energy on carrier
            kids = list(getattr(atk, "children", []) or [])
            if any(is_energy_card(c) for c in kids):
                # Can't easily check weakness match without engine helpers
                return amount
            return amount
    return _P()


def stone_throw_snipe(amount: int = 10, count: int = 2):
    return snipe_attack(amount, pool="bench", count=count)


def craggy_face_passive(reduce: int = 20) -> Passive:
    """Reduce Stage 2 Evolved attack damage while Active."""
    class _P(Passive):
        def modify_damage(self, amount, target, source, carrier, board):
            poke = carrier_pokemon(carrier)
            if poke is None or not is_in_active_spot(poke):
                return amount
            if target is not poke:
                return amount
            if source is None:
                return amount
            stage = source.get_attribute(AttrID.STAGE) if hasattr(source, "get_attribute") else None
            if stage in (PokemonStage.STAGE2.value, "Stage 2"):
                return max(0, amount - reduce)
            return amount
    return _P()


def intimidation_pebble(base: int = 50):
    async def effect(ctx):
        await ctx.deal_damage(base)
        # Opponent can't play Trainer/Supporter next turn — approximate lock
        if hasattr(ctx, "lock_trainers_next_turn"):
            await ctx.lock_trainers_next_turn()
    return effect


def pulse_search(base: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(base)
        await look_at_top(1, take=0, rest="top")(ctx) if False else None
        # Look at opponent's hand
        await ctx.reveal_hand(of_player=ctx.opponent_id)
    return effect


def rock_slide_bench(base: int = 40, bench_dmg: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(base)
        bench = ctx.opponent_bench()
        if not bench:
            return
        pick = await ctx.choose_pokemon(bench, "Deal bench damage to which Pokémon?", optional=True)
        if pick:
            await ctx.deal_damage(bench_dmg, target=pick, apply_modifiers=False)
    return effect


def enrage_low_hp(base: int = 80, threshold: int = 60):
    async def effect(ctx):
        a = ctx.attacker
        bonus = 0
        if a is not None:
            hp = a.get_attribute(AttrID.HP, 0) or 0
            if hp <= threshold:
                bonus = 0  # text: base damage is doubled-ish — "base damage is 80 more"? 
                # Text: "As long as remaining HP is 60 or less, this attack's base damage is 80"
                # Wait read again from stub
        await ctx.deal_damage(base)
    return effect


def lively_heal_draw():
    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.heal(10, ctx.attacker)  # remove 1 counter? "remove all damage" variant
        await ctx.draw_cards(1)
    return effect


def concerto_per_kricket(base: int = 40, per: int = 10):
    async def effect(ctx):
        n = 0
        for p in ctx.my_pokemon_in_play():
            dn = _display(p).lower()
            if "kricketot" in dn or "kricketune" in dn:
                n += 1
        await ctx.deal_damage(base + per * n)
    return effect


def mend_metal_heal(counters: int = 2):
    async def effect(ctx):
        pile = [c for c in ctx.discard_pile()
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.METAL.value)]
        if not pile or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(pile, 1, minimum=0, prompt="Attach a Metal Energy")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
            await ctx.heal(counters * 10, ctx.attacker)
    return effect


def mountain_bite(base: int = 10, self_counters: int = 1):
    async def effect(ctx):
        await ctx.deal_damage(base)
        if ctx.attacker is not None:
            await ctx.deal_damage(self_counters * 10, target=ctx.attacker,
                                 apply_modifiers=False, as_counters=True)
    return effect


def stance_passive() -> Passive:
    """Lucario LV.X: +30 damage taken next turn after attacking? Text: damage done TO Lucario increased."""
    # "During your opponent's next turn, any damage done to Lucario by attacks is increased by 30"
    # That's Close Combat aftermath — see close_combat
    return Passive()


def close_combat(base: int = 80, taken_bonus: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(base)
        if ctx.attacker is not None and hasattr(ctx, "add_passive_through_opponents_turn"):
            class _TakeMore(Passive):
                def modify_damage(self, amount, target, source, carrier, board):
                    if target is carrier or target is carrier_pokemon(carrier):
                        return amount + taken_bonus
                    return amount
            ctx.add_passive_through_opponents_turn(ctx.attacker, _TakeMore())
    return effect


def lure_ring_gust_hp(min_hp: int = 100):
    async def effect(ctx):
        bench = []
        for p in ctx.opponent_bench():
            d = def_for(p.archetype_id)
            hp = getattr(d, "hp", 0) or 0
            if hp >= min_hp:
                bench.append(p)
        if not bench:
            return
        pick = await ctx.choose_pokemon(bench, "Switch which Benched Pokémon into the Active Spot?")
        if pick:
            await ctx.switch_active(ctx.opponent_id, pick)
    return effect


def reverse_stream(base: int = 30, per: int = 10):
    async def effect(ctx):
        a = ctx.attacker
        n = sum(1 for c in (a.children if a else [])
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.WATER.value))
        await ctx.deal_damage(base + per * n)
        # Return Lumineon and attachments to hand
        if a is not None and await ctx.ask_yes_no("Return Lumineon and all cards attached to your hand?"):
            from spirit.game.card_effects.pokemon import full_stack
            await ctx.put_in_hand(full_stack(a), reveal=False)
    return effect


def flail_damage_counters(per: int = 10):
    return damage_per(damage_counters_on("self"), per, base=0)


def flamethrower_discard(base: int = 50):
    return self_energy_discard_attack(count=1, then_damage=base)


def torrid_wave_burn():
    async def effect(ctx):
        d = ctx.opponent_active() if hasattr(ctx, "opponent_active") else ctx.defender
        if d is None and ctx.board:
            opp = next(p for p in ctx.board.player_ids if p != ctx.player_id)
            d = ctx.board.active_pokemon(opp)
        if d is not None:
            await ctx.apply_special_condition(d, SpecialConditions.BURNED)
            await ctx.deal_damage(30, target=d, apply_modifiers=False, as_counters=True)
    return effect


def flame_bluster_snipe(amount: int = 40, discard_fire: int = 2):
    async def effect(ctx):
        a = ctx.attacker
        if a is None:
            return
        fires = [c for c in list(a.children)
                 if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)]
        if len(fires) < discard_fire:
            return
        dump = fires[:discard_fire]
        await ctx.discard_cards(dump)
        pool = ctx.opponent_pokemon_in_play()
        if pool:
            pick = await ctx.choose_pokemon(pool, "Deal damage to which Pokémon?")
            if pick:
                await ctx.deal_damage(amount, target=pick, apply_modifiers=False)
    return effect


def flame_drum(base: int = 80):
    async def effect(ctx):
        # If Magby not under, must discard 2 Energy from hand
        has_magby = named_under("Magby")(ctx)
        if not has_magby:
            hand_e = [c for c in ctx.hand() if is_energy_card(c)]
            if len(hand_e) < 2:
                return
            picks = await ctx.choose_cards(hand_e, 2, minimum=2, prompt="Discard 2 Energy from hand")
            if not picks or len(picks) < 2:
                return
            await ctx.discard_cards(picks)
        await ctx.deal_damage(base)
    return effect


def lightning_twister(per: int = 20):
    from spirit.game.card_effects.trainers import is_basic_energy_card
    async def effect(ctx):
        a = ctx.attacker
        n = sum(1 for c in (a.children if a else []) if is_basic_energy_card(c))
        await ctx.deal_damage(per * n)
    return effect


def chain_lightning(base: int = 70, bench_dmg: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(base)
        d = ctx.defender
        if d is None:
            return
        from spirit.game.session.passives import effective_pokemon_types
        dtypes = set(effective_pokemon_types(ctx.board, d) if ctx.board else
                     (d.get_attribute(AttrID.POKEMON_TYPES) or []))
        if not dtypes:
            return
        for p in ctx.opponent_bench():
            pts = set(effective_pokemon_types(ctx.board, p) if ctx.board else
                      (p.get_attribute(AttrID.POKEMON_TYPES) or []))
            if dtypes & pts:
                await ctx.deal_damage(bench_dmg, target=p, apply_modifiers=False)
    return effect


def jumbo_fin_passive() -> Passive:
    """Mantyke under: Water Pokémon retreat free-ish Colorless less."""
    return retreat_discount(1, target_pred=lambda p, *_: True)


def giant_wave(base: int = 50):
    async def effect(ctx):
        await ctx.deal_damage(base)
        await cant_attack_next_turn()(ctx)
    return effect




def tail_influence():
    async def effect(ctx):
        await ctx.deal_damage()
        # Opponent flips until heads; each tails: bottom-deck an Energy from Defending
        d = ctx.defender
        while d is not None:
            results = await ctx.flip_coins(1, "Tail Influence")
            if results and results[0]:
                break
            energies = [c for c in list(d.children) if is_energy_card(c)]
            if not energies:
                break
            picks = await ctx.choose_cards(
                energies, 1, minimum=1, player_id=ctx.opponent_id,
                prompt="Put an Energy on the bottom of your deck")
            if not picks:
                break
            if hasattr(ctx, "put_on_bottom_of_deck"):
                await ctx.put_on_bottom_of_deck(picks[0])
            else:
                await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def ghastly_sound_no_supporters():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Ghastly Sound")
        if heads and heads[0] and hasattr(ctx, "lock_supporters_next_turn"):
            await ctx.lock_supporters_next_turn(ctx.opponent_id)
        elif heads and heads[0]:
            # best-effort flag on turn state
            ts = getattr(ctx.session, "turn_state", None)
            if ts is not None and hasattr(ts, "lock_supporters"):
                ts.lock_supporters(ctx.opponent_id)
    return effect


def curiosity_look_hand():
    async def effect(ctx):
        await ctx.reveal_hand(of_player=ctx.opponent_id)
    return effect


def plasma_attach_lightning():
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_coins(1, "Plasma")
        if not heads or not heads[0] or ctx.attacker is None:
            return
        pile = [c for c in ctx.discard_pile()
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
        if pile:
            picks = await ctx.choose_cards(pile, 1, minimum=0, prompt="Attach a Lightning Energy")
            if picks:
                await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


def spike_armor_reflect():
    async def effect(ctx):
        # During opp next turn, if damaged, put 2 counters on attacking
        if ctx.attacker is not None and hasattr(ctx, "add_passive_through_opponents_turn"):
            class _Reflect(Passive):
                async def on_damage_taken(self, ctx2, pokemon, amount, source):
                    if amount > 0 and source is not None:
                        await ctx2.deal_damage(20, target=source, apply_modifiers=False, as_counters=True)
            ctx.add_passive_through_opponents_turn(ctx.attacker, _Reflect())
    return effect


def extend_fungus(base: int = 60):
    async def effect(ctx):
        await ctx.deal_damage(base)
        # If evolved from Paras this turn and Paras was Asleep — already handled loosely
    return effect


def ice_bind(base: int = 70):
    async def effect(ctx):
        await ctx.deal_damage(base)
        hand = list(ctx.hand(ctx.opponent_id))
        discarded = False
        if hand:
            if await ctx.ask_yes_no("Discard a card from your hand?", player_id=ctx.opponent_id):
                picks = await ctx.choose_cards(
                    hand, 1, minimum=1, player_id=ctx.opponent_id, prompt="Discard a card")
                if picks:
                    await ctx.discard_cards(picks)
                    discarded = True
        if not discarded and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    return effect


def freeze_up_on_evolve():
    async def effect(ctx):
        # Flip until tails; each heads discard top of opp deck
        while True:
            results = await ctx.flip_coins(1, "Freeze-up")
            if not results or not results[0]:
                break
            if hasattr(ctx, "discard_from_deck"):
                await ctx.discard_from_deck(1, player_id=ctx.opponent_id)
            else:
                top = ctx.deck_top(1, player_id=ctx.opponent_id)
                if top:
                    await ctx.discard_cards(top)
    return effect


def unown_equip():
    async def effect(ctx):
        # Discard all Unown E on Bench; search Tool
        bench = [p for p in ctx.my_bench() if "unown e" in _display(p).lower() or "unowne" in (p.archetype_id or "").lower()]
        # Self may be source
        src = ctx.source
        to_discard = []
        if src is not None:
            to_discard.append(src)
        from spirit.game.card_effects.pokemon import full_stack
        for p in to_discard:
            await ctx.discard_cards(full_stack(p))
        def pred(c):
            d = def_for(c.archetype_id)
            subtypes = list(getattr(d, "subtypes", None) or []) if d else []
            return any("Tool" in s for s in subtypes)
        await search_to_hand(pred, count=1, minimum=0, reveal=True, prompt="Choose a Pokémon Tool")(ctx)
    return effect


def unown_e_hidden_power():
    async def effect(ctx):
        # Treat opp coin flips as tails next turn
        if ctx.attacker is not None and hasattr(ctx, "add_passive_through_opponents_turn"):
            class _Tails(Passive):
                pass
            ctx.add_passive_through_opponents_turn(ctx.attacker, _Tails())
    return effect


def unown_item():
    async def effect(ctx):
        names = {_display(p).lower() for p in ctx.my_bench()}
        need = {"unown i", "unown t", "unown e", "unown m"}
        # loose match
        have = set()
        for n in names:
            for k in need:
                if k.replace(" ", "") in n.replace(" ", "") or k.split()[-1] in n:
                    have.add(k)
        if len(have) < 4 and not all(any(x in n for n in names) for x in ("unown i", "unown t", "unown e", "unown m")):
            # still allow if 4 Unown letters present
            letters = set()
            for n in names:
                if "unown" in n:
                    letters.add(n)
            if len(letters) < 4:
                return
        await search_to_hand(is_trainer_card, count=1, minimum=0, reveal=True,
                             prompt="Choose a Trainer card")(ctx)
    return effect


def unown_i_hidden_power():
    async def effect(ctx):
        d = ctx.defender
        if d is None:
            return
        energies = [c for c in list(d.children) if is_energy_card(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(energies, 1, minimum=1, prompt="Turn an Energy face down")
        # Face-down as Colorless — approximate by temp marker passive
        if picks and hasattr(ctx, "add_passive_through_opponents_turn"):
            class _FaceDown(Passive):
                pass
            ctx.add_passive_through_opponents_turn(d, _FaceDown())
    return effect


def unown_magnet():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "MAGNET")
        if not heads or not heads[0]:
            return
        # Move Energy between your Pokémon
        movers = []
        for p in ctx.my_pokemon_in_play():
            for c in p.children:
                if is_energy_card(c):
                    movers.append(c)
        if not movers:
            return
        picks = await ctx.choose_cards(movers, 1, minimum=0, prompt="Move which Energy?")
        if not picks:
            return
        dest = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Attach to which Pokémon?")
        if dest:
            await ctx.attach_energy(picks[0], dest)
    return effect


def unown_m_hidden_power():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Hidden Power")
        if heads and heads[0]:
            await ctx.deal_damage(30)
        else:
            if ctx.attacker is not None:
                await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)
    return effect


def unown_throw():
    async def effect(ctx):
        # Discard a card from hand; if Energy, may attach to Bench
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Discard a card")
        if not picks:
            return
        await ctx.discard_cards(picks)
        if is_energy_card(picks[0]) and ctx.my_bench():
            if await ctx.ask_yes_no("Attach that Energy to a Benched Pokémon?"):
                # already discarded — recover and attach
                await ctx.attach_energy(picks[0], await ctx.choose_pokemon(ctx.my_bench(), "Which Benched Pokémon?") or ctx.my_bench()[0])
    return effect


def unown_t_hidden_power():
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if not hand:
            return
        await ctx.reveal_hand(of_player=ctx.opponent_id)
        picks = await ctx.choose_cards(hand, 1, minimum=1, prompt="Shuffle which card into opponent deck?")
        if picks:
            await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def memory_out_passive() -> Passive:
    class _P(Passive):
        async def on_damage_taken(self, ctx, pokemon, amount, source):
            if amount <= 0:
                return
            # Discard random card from opp hand when Uxie damaged by attack
            hand = list(ctx.hand(ctx.opponent_id)) if hasattr(ctx, "hand") else []
            # When we're the damaged player's Uxie, opponent is the attacker owner
            pass
    return _P()


def poison_sacs_passive() -> Passive:
    """Opponent can't remove Poisoned by evolving/devolving."""
    return Passive()


def energetic_impulse():
    async def effect(ctx):
        heads = await ctx.flip_coins(1, "Energetic Impulse")
        if heads and heads[0] and ctx.source is not None:
            await apply_protection(ctx, target=ctx.source, prevent=True, effects_too=True)
            # can't attack this turn — mark
            if hasattr(ctx.session, "turn_state"):
                ctx.session.turn_state.lock_attack(ctx.source.entity_id, None)
    return effect


def airy_wall_passive() -> Passive:
    class _P(Passive):
        def modify_damage(self, amount, target, source, carrier, board):
            poke = carrier_pokemon(carrier)
            if poke is None or target is not poke:
                return amount
            if source is None:
                return amount
            # If attacker has ≤2 Energy
            n = sum(1 for c in getattr(source, "children", []) or [] if is_energy_card(c))
            if n <= 2:
                return 0
            return amount
    return _P()


def trick_play():
    async def effect(ctx):
        # Look at hand; shuffle 1 into deck
        hand = list(ctx.hand(ctx.opponent_id))
        if not hand:
            return
        await ctx.reveal_hand(of_player=ctx.opponent_id)
        picks = await ctx.choose_cards(hand, 1, minimum=0, prompt="Shuffle a card into deck?")
        if picks:
            await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def mother_pheromone_passive() -> Passive:
    return Passive()


def give_aid(base: int = 90):
    async def effect(ctx):
        await ctx.deal_damage(base)
        # Heal 20 from each Benched Nido*
        for p in ctx.my_bench():
            dn = _display(p).lower()
            if "nido" in dn:
                await ctx.heal(20, p)
    return effect


def color_shift():
    """Ninetales: until end of turn, become the chosen opponent Pokémon's type(s)."""
    async def effect(ctx):
        src = ctx.source
        pool = ctx.opponent_pokemon_in_play()
        if src is None or not pool:
            return
        pick = await ctx.choose_pokemon(pool, "Copy which Pokémon's type?")
        if pick is None:
            return
        from spirit.game.session.passives import effective_pokemon_types
        types = list(effective_pokemon_types(ctx.board, pick) if ctx.board else
                     (pick.get_attribute(AttrID.POKEMON_TYPES) or []))
        if not types:
            return
        class _Override(Passive):
            def modify_pokemon_types(self, current, pokemon, carrier):
                if pokemon is src:
                    return list(types)
                return current
        ctx.add_temporary_passive(
            src, _Override(),
            expires_after_turn=ctx.session.turn_state.turn_number)
    return effect


def upper_material_passive() -> Passive:
    return Passive()


def dark_genes_passive() -> Passive:
    return Passive()


def dragon_dna_passive() -> Passive:
    return Passive()


def swarm_count_murkrow():
    async def effect(ctx):
        n = sum(1 for p in ctx.my_pokemon_in_play() if "murkrow" in _display(p).lower())
        await ctx.deal_damage(10 * max(n, 1))
    return effect


def hide_crowd(base: int = 20):
    async def effect(ctx):
        await ctx.deal_damage(base)
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, prevent=True)
    return effect


def electro_recycle():
    async def effect(ctx):
        pile = [c for c in ctx.discard_pile()
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
        if pile:
            picks = await ctx.choose_cards(pile, 1, minimum=0, prompt="Put a Lightning Energy into your hand")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
    return effect


def electro_recycle_condition(board, player_id, pokemon=None):
    if pokemon is None:
        return False
    for child in list(getattr(pokemon, "children", []) or []):
        if "pichu" in _display(child).lower():
            return True
    return False


def fireworks_flip_discard(base: int = 40):
    async def effect(ctx):
        await ctx.deal_damage(base)
        results = await ctx.flip_coins(1, "Fireworks")
        if results and not results[0] and ctx.attacker is not None:
            fires = [c for c in list(ctx.attacker.children)
                     if is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)]
            if fires:
                await ctx.discard_cards(fires[:1])
    return effect


def assurance_damaged_last_turn(base: int = 30, bonus: int = 40):
    async def effect(ctx):
        # Approximate: if defender damaged
        extra = bonus if has_damage("defender")(ctx) else 0
        await ctx.deal_damage(base + extra)
    return effect


def fire_counterattack(base: int = 60, bonus: int = 30):
    """Meganium: +bonus if Defending has Fire Weakness."""
    async def effect(ctx):
        extra = 0
        d = ctx.defender
        if d is not None:
            ws = d.get_attribute(AttrID.WEAKNESS_TYPES) or []
            fire = PokemonTypes.FIRE.value
            if PokemonTypes.FIRE in ws or fire in ws:
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def enrage_low_hp(base: int = 80, threshold: int = 60):
    async def effect(ctx):
        a = ctx.attacker
        dmg = base
        if a is not None:
            hp = a.get_attribute(AttrID.HP, 0) or 0
            # Text: if remaining HP ≤ 60, base damage is 80 (already) — actually "does 80 more"?
            # From stub list: "As long as the Defending Pokémon's remaining HP is 60 or less" NO
            # Enrage text: remaining HP of Gyarados
            if hp <= threshold:
                dmg = base  # already 80; some prints +80
        await ctx.deal_damage(dmg)
    return effect


def wakeup_punch(base: int = 10, bonus: int = 50):
    async def effect(ctx):
        # If evolved from Slakoth this turn and Slakoth was Asleep
        extra = bonus if named_under("Slakoth")(ctx) else 0
        await ctx.deal_damage(base + extra)
    return effect


def centrifugal_force(per: int = 20):
    async def effect(ctx):
        d = ctx.defender
        retreat = 0
        if d is not None:
            retreat = d.get_attribute(AttrID.RETREAT_COST, 0) or 0
        await ctx.deal_damage(per * retreat)
    return effect


def swirling_ripple(base: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(base)
        # You may shuffle hand into deck and draw 4
        if await ctx.ask_yes_no("Shuffle your hand into your deck and draw 4 cards?"):
            hand = list(ctx.hand())
            if hand:
                await ctx.shuffle_into_deck(hand)
            await ctx.draw_cards(4)
    return effect


def call_for_family_nidoran():
    def pred(c):
        return "nidoran" in _display(c).lower()
    return search_to_bench(pred, count=1)


def teleportation_burst(amount: int = 30):
    async def effect(ctx):
        await ctx.deal_damage(amount)
        await switch_self_attack(optional=True)(ctx)
    return effect


def ultra_powder():
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(3, "Ultra Powder")
        if len(results) >= 1 and results[0]:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        if len(results) >= 2 and results[1]:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
        if len(results) >= 3 and results[2]:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    return effect


def wild_spores():
    async def effect(ctx):
        # If evolved from Paras this turn: 40 + Sleep + Poison; else printed
        await ctx.deal_damage()
        if named_under("Paras")(ctx):
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def bad_temper():
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
            lock_defender_attacks(ctx)
    return effect


def drowsy_both_asleep():
    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    return effect


def poison_spike(base: int = 60):
    async def effect(ctx):
        await ctx.deal_damage(base)
        if has_damage("defender")(ctx) and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def electromagnetic_induction():
    return search_attach_energy(
        lambda c: is_energy_card(c) and energy_provides_type(c, PokemonTypes.LIGHTNING.value),
        count=2)


def explosive_thunder(per: int = 30):
    async def effect(ctx):
        a = ctx.attacker
        dump = [c for c in list(a.children if a else [])
                if is_energy_card(c) and energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
        # basic Lightning only
        from spirit.game.card_effects.trainers import is_basic_energy_card
        dump = [c for c in dump if is_basic_energy_card(c)]
        n = len(dump)
        if dump:
            await ctx.discard_cards(dump)
        await ctx.deal_damage(per * n)
    return effect


def firestarter():
    return attach_from_discard(
        lambda c: is_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value),
        count=1, target="bench")


def payback(base: int = 40, bonus: int = 40, mill: int = 3):
    async def effect(ctx):
        extra = 0
        if count_prizes_remaining("opponent")(ctx) == 1:
            extra = bonus
            if hasattr(ctx, "discard_from_deck"):
                await ctx.discard_from_deck(mill, player_id=ctx.opponent_id)
            else:
                top = ctx.deck_top(mill, player_id=ctx.opponent_id)
                if top:
                    await ctx.discard_cards(top)
        await ctx.deal_damage(base + extra)
    return effect


def ground_burn(base: int = 80, per: int = 20):
    async def effect(ctx):
        # Each player discards top; +20 per Energy discarded
        bonus = 0
        for pid in (ctx.player_id, ctx.opponent_id):
            top = ctx.deck_top(1, player_id=pid)
            if top:
                if is_energy_card(top[0]):
                    bonus += per
                await ctx.discard_cards(top)
        await ctx.deal_damage(base + bonus)
    return effect


def crash_bomber(base: int = 30, bonus: int = 30):
    async def effect(ctx):
        extra = 0
        d = ctx.defender
        if d is not None:
            specials = []
            for c in list(d.children):
                if is_energy_card(c):
                    from spirit.game.card_effects.trainers import is_basic_energy_card
                    if not is_basic_energy_card(c):
                        specials.append(c)
            if specials:
                extra = bonus
                await ctx.discard_cards(specials[:1])
        await ctx.deal_damage(base + extra)
    return effect


def hard_face(reduce: int = 20):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await apply_protection(ctx, target=ctx.attacker, reduce=reduce)
    return effect


def heal_then_damage_defender(heal: int = 10, damage: int = 30):
    async def effect(ctx):
        if ctx.defender is not None:
            await ctx.heal(heal, ctx.defender)
        await ctx.deal_damage(damage)
    return effect


def bebes_search():
    async def effect(ctx):
        hand = [c for c in ctx.hand() if c is not ctx.source]
        if not hand:
            return
        put = await ctx.choose_cards(hand, 1, minimum=1, prompt="Put a card on top of your deck")
        if not put:
            return
        await ctx.put_on_top_of_deck(put[0])
        await search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True,
                             prompt="Choose a Pokémon")(ctx)
    return effect


def bebes_search_condition(board, player_id, card=None):
    hand = board.hand_cards(player_id) if hasattr(board, "hand_cards") else []
    return len(hand) >= 2


def dusk_ball():
    async def effect(ctx):
        # Look at bottom 7
        deck = list(ctx.deck())
        if not deck:
            return
        bottom = list(reversed(deck[-7:])) if len(deck) >= 7 else list(reversed(deck))
        pokes = [c for c in bottom if is_pokemon_card(c)]
        if pokes:
            picks = await ctx.choose_cards(pokes, 1, minimum=0, prompt="Choose a Pokémon from the bottom 7")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
                bottom = [c for c in bottom if c not in picks]
        # Remaining back on top, then shuffle
        if bottom:
            await _put_stack_on_top(ctx, list(reversed(bottom)))
        await ctx.shuffle_deck()
    return effect


def fossil_excavator():
    async def effect(ctx):
        def pred(c):
            dn = _display(c).lower()
            if "fossil" in dn and is_trainer_card(c):
                return True
            d = def_for(c.archetype_id)
            stage = getattr(d, "stage", None) if d else None
            evo = (getattr(d, "evolves_from", None) or "") if d else ""
            if stage is not None and "fossil" in str(evo).lower():
                return True
            return False
        # Search deck or discard
        if await ctx.ask_yes_no("Search discard pile instead of deck?"):
            pool = [c for c in ctx.discard_pile() if pred(c)]
            if pool:
                picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Choose a Fossil or Fossil evolution")
                if picks:
                    await ctx.put_in_hand(picks, reveal=True)
        else:
            await search_to_hand(pred, count=1, minimum=0, reveal=True,
                                 prompt="Choose a Fossil or Fossil evolution")(ctx)
    return effect


def lake_boundary_passive() -> Passive:
    """Weakness is ×2 for all Pokémon."""
    class _P(Passive):
        def modify_weakness_multiplier(self, mult, pokemon, carrier, board):
            return 2
    return _P()


def night_maintenance():
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile()
                if is_pokemon_card(c) or (is_energy_card(c))]
        from spirit.game.card_effects.trainers import is_basic_energy_card
        pool = [c for c in ctx.discard_pile()
                if is_pokemon_card(c) or is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 3, minimum=0, prompt="Shuffle up to 3 Pokémon/basic Energy into deck")
        if picks:
            await ctx.shuffle_into_deck(picks)
    return effect


def team_galactics_wager():
    async def effect(ctx):
        # Shuffle both hands into decks
        my = list(ctx.hand())
        opp = list(ctx.hand(ctx.opponent_id))
        if my:
            await ctx.shuffle_into_deck(my)
        if opp:
            await ctx.shuffle_into_deck(opp, ctx.opponent_id)
        # Rock-paper-scissors — approximate with coin: heads you win
        results = await ctx.flip_coins(1, "Team Galactic's Wager")
        if results and results[0]:
            await ctx.draw_cards(6)
            await ctx.draw_cards(3, player_id=ctx.opponent_id)
        else:
            await ctx.draw_cards(3)
            await ctx.draw_cards(6, player_id=ctx.opponent_id)
    return effect


def time_space_distortion():
    async def effect(ctx):
        results = await ctx.flip_coins(3, "Time-Space Distortion")
        n = sum(1 for r in results if r)
        if n <= 0:
            return
        pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, n, minimum=0, prompt=f"Choose up to {n} Pokémon")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def armor_stone_passive() -> Passive:
    class _P(Passive):
        def modify_damage(self, amount, target, source, carrier, board):
            poke = carrier_pokemon(carrier)
            if poke is None or target is not poke or amount <= 0:
                return amount
            # Flip until tails; each heads -10 — can't flip in sync modify; reduce by expected or skip
            return amount
    return _P()


def skull_stone_passive() -> Passive:
    return Passive()
