"""Behaviors for the Pokemon of the Lugia VSTAR and Mew VMAX archetype decks."""

from spirit.game.attributes import (
    AttrID,
    CardType,
    CLIENT_SPECIAL_CONDITION_NAMES,
    PokemonStage,
    PokemonTypes,
    SpecialConditions,
)
from spirit.game.data_utils import (
    ABILITIES_BY_ID, Ability, Attack, ability_id_for, def_for, is_pokemon_v,
    subtypes_for,
)
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_colorless_no_rule_box,
    is_special_energy,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.models.board import PokemonEntity


# --- Dunsparce (FST): Mysterious Nest -----------------------------------

class MysteriousNestPassive(Passive):
    """Colorless Pokemon in play (both sides) have no Weakness."""

    def modify_weakness(self, calc, carrier):
        types = calc.target.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.COLORLESS.value in types:
            calc.weakness_applies = False


# --- Lugia V (SIT) -------------------------------------------------------

async def read_the_wind(ctx):
    """Discard a card from your hand. If you do, draw 3 cards."""
    if await ctx.discard_from_hand(1, minimum=0, prompt="Discard a card from your hand"):
        await ctx.draw_cards(3)


async def aero_dive(ctx):
    """130. You may discard a Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


# --- Lugia VSTAR (SIT) ---------------------------------------------------

def summoning_star_condition(board, player_id, pokemon):
    """Offerable only with a valid discard target and a free bench slot."""
    bench = board.find_player_area(player_id, "bench")
    if not bench or len(bench.children) >= BENCH_CAPACITY:
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(
        is_colorless_no_rule_box(c) for c in discard.children
    )


async def summoning_star(ctx):
    """VSTAR Power: up to 2 Colorless Pokemon without a Rule Box from the
    discard pile onto the Bench."""
    candidates = [c for c in ctx.discard_pile() if is_colorless_no_rule_box(c)]
    count = min(2, BENCH_CAPACITY - len(ctx.my_bench()))
    if not candidates or count <= 0:
        return
    # The discard pile is public: once used, the pick may not choose zero.
    picks = await ctx.choose_cards(
        candidates, count, minimum=1,
        prompt="Choose up to 2 Pokémon to put onto your Bench",
    )
    for card in picks:
        await ctx.bench_pokemon(card)


async def tempest_dive(ctx):
    """220. You may discard a Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


# --- Oranguru (SSH): Primate Wisdom --------------------------------------

async def primate_wisdom(ctx):
    """Once during your turn: switch a card from your hand with the top card
    of your deck."""
    hand = ctx.hand()
    deck = ctx.deck()
    if not hand or not deck:
        return
    picks = await ctx.choose_cards(
        hand, 1, prompt="Choose a card to put on top of your deck"
    )
    if not picks:
        return
    top_card = deck[-1]  # the deck's top is its last child
    await ctx.put_on_top_of_deck(picks[0])
    await ctx.put_in_hand([top_card], reveal=False)


# --- Snorlax (LOR) --------------------------------------------------------

class UnfazedFatPassive(Passive):
    """Prevent all effects of opposing attacks (damage is not an effect)."""

    def blocks_attack_effects(self, target, carrier):
        return target is carrier


async def thumping_snore(ctx):
    """180. This Pokemon is now Asleep; its Checkup flips 2 coins."""
    await ctx.deal_damage()
    await ctx.apply_special_condition(
        ctx.attacker, SpecialConditions.ASLEEP, checkup_coins=2
    )


# --- Stoutland V (BST) ----------------------------------------------------

async def double_dip_fangs(ctx):
    """40. If the opposing Basic is Knocked Out by this damage, +1 Prize."""
    defender = ctx.defender
    await ctx.deal_damage()
    if (
        defender is not None
        and defender in ctx.knockouts
        and defender.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
    ):
        ctx.extra_prizes += 1


async def wild_tackle(ctx):
    """200. This Pokemon also does 30 damage to itself."""
    await ctx.deal_damage()
    await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)


# --- Archeops (SIT): Primal Turbo ----------------------------------------

async def primal_turbo(ctx):
    """Once during your turn: search the deck for up to 2 Special Energy and
    attach them to 1 of your Pokemon. Then shuffle."""
    picks = await ctx.search_deck(
        is_special_energy, count=2, minimum=0,
        prompt="Choose up to 2 Special Energy cards to attach to 1 of your Pokémon.",
    )
    if picks:
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to"
        )
        if target is not None:
            ctx.visual_targets = [target.entity_id]
            for energy in picks:
                await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


# --- Yveltal (SHF): Amazing Destruction ----------------------------------

async def amazing_destruction(ctx):
    """Your opponent's Active Pokemon is Knocked Out."""
    await ctx.knock_out(ctx.defender)


# --- Radiant Charizard (PGO) ----------------------------------------------

class ExcitedHeartPassive(Passive):
    """Attacks cost [C] less for each Prize the opponent has taken."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        owner = carrier.owning_player_id
        opponent = next((p for p in board.player_ids if p != owner), None)
        if opponent is None:
            return cost
        discount = board.prizes_taken(opponent)
        if discount <= 0 or "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - discount
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


# --- Raikou (VIV): Amazing Shot -------------------------------------------

async def amazing_shot(ctx):
    """120, plus 120 to one opposing Benched Pokemon (no W/R on the bench)."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon"
        )
        if target is not None:
            await ctx.deal_damage(120, target=target, apply_modifiers=False)


# --- Pumpkaboo (EVS): Pumpkin Pit -----------------------------------------

async def pumpkin_pit(ctx):
    """On play from hand: you may discard a Stadium in play."""
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


# --- Lumineon V (BRS) ------------------------------------------------------

async def luminous_sign(ctx):
    """On play from hand: you may search the deck for a Supporter card."""
    if not await ctx.ask_yes_no("Search your deck for a Supporter card?"):
        return
    picks = await ctx.search_deck(
        is_supporter_card, count=1, minimum=0,
        prompt="Choose a Supporter card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def aqua_return(ctx):
    """120. Shuffle this Pokemon and all attached cards into your deck."""
    attacker = ctx.attacker
    await ctx.deal_damage()
    await ctx.shuffle_into_deck(full_stack(attacker), ctx.player_id)


# --- Manaphy (BRS): Wave Veil ----------------------------------------------

class WaveVeilPassive(Passive):
    """Prevent all damage done to your Benched Pokemon by opposing attacks."""

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and calc.target.owning_player_id == carrier.owning_player_id
            and not calc.to_active
        )


# --- Shared tool passives ---------------------------------------------------

class ChoiceBeltPassive(Passive):
    """+30 damage to the opponent's Active Pokemon V."""

    def modify_damage_dealt(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and calc.to_active
            and carrier_pokemon(carrier) is calc.attacker
            and is_pokemon_v(calc.target.archetype_id)
        ):
            calc.amount += 30


# --- Oricorio (FST): Lesson in Zeal ---------------------------------------

class LessonInZealPassive(Passive):
    """Your Fusion Strike Pokemon take 20 less damage from attacks (after
    Weakness/Resistance); doesn't stack with a second Lesson in Zeal."""

    def modify_damage_taken(self, calc, carrier):
        target = calc.target
        if not (
            calc.is_attack
            and calc.is_opposing
            and target.owning_player_id == carrier.owning_player_id
            and "Fusion Strike" in subtypes_for(target.archetype_id)
        ):
            return
        if "LessonInZeal" in calc.applied_once:
            return
        calc.applied_once.add("LessonInZeal")
        calc.amount -= 20


async def glistening_droplets(ctx):
    """Put 5 damage counters on your opponent's Pokemon in any way you like."""
    await ctx.place_damage_counters(5, ctx.opponent_pokemon_in_play())


# --- Genesect V (FST): Fusion Strike System --------------------------------

def _fusion_strike_in_play_count(board, player_id) -> int:
    return sum(
        1 for p in board.pokemon_in_play(player_id)
        if "Fusion Strike" in subtypes_for(p.archetype_id)
    )


def fusion_strike_system_condition(board, player_id, pokemon) -> bool:
    """A draw that would find nothing (already caught up) may not be offered."""
    hand = board.find_player_area(player_id, "hand")
    hand_size = len(hand.children) if hand else 0
    return hand_size < _fusion_strike_in_play_count(board, player_id)


async def fusion_strike_system(ctx):
    """Once during your turn: draw until you have as many cards in your hand
    as you have Fusion Strike Pokemon in play."""
    await ctx.draw_until(_fusion_strike_in_play_count(ctx.board, ctx.player_id))


# --- Mew V (FST) -----------------------------------------------------------

def _is_energy_card(card) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value


async def energy_mix(ctx):
    """Search your deck for an Energy card and attach it to 1 of your Fusion
    Strike Pokemon. Then, shuffle your deck."""
    picks = await ctx.search_deck(
        _is_energy_card, count=1, minimum=0,
        prompt="Choose an Energy card to attach to 1 of your Fusion Strike Pokémon.",
    )
    if picks:
        targets = [p for p in ctx.my_pokemon_in_play()
                   if "Fusion Strike" in subtypes_for(p.archetype_id)]
        if targets:
            target = await ctx.choose_pokemon(
                targets, "Choose a Fusion Strike Pokémon to attach the Energy to"
            )
            if target is not None:
                await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


async def psychic_leap(ctx):
    """70. You may shuffle this Pokemon and all attached cards into your deck."""
    await ctx.deal_damage()
    if await ctx.ask_yes_no("Shuffle Mew V and all attached cards into your deck?"):
        await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)

        # Promotion must wait for the attack bracket to flush, or the client
        # sees the new Active land while the old one still stands there.
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )

        ctx.deferred_actions.append(_promote)


# --- Mew VMAX (FST) ---------------------------------------------------------

def fusion_strike_bench_attacks(board, player_id):
    """(pokemon, attack) pairs for each benched Fusion Strike Pokemon's
    attacks, deduped by attack identity (two Genesect offer one Techno Blast).
    Copy attacks stay selectable per the ruling -- picking one that re-enters
    the copy chain fizzles inside ctx.use_attack."""
    bench_area = board.find_player_area(player_id, "bench")
    pairs = []
    seen = set()
    for pokemon in (bench_area.children if bench_area else []):
        if not isinstance(pokemon, PokemonEntity):
            continue
        if "Fusion Strike" not in subtypes_for(pokemon.archetype_id):
            continue
        definition = def_for(pokemon.archetype_id)
        for ability in getattr(definition, "abilities", []):
            if isinstance(ability, Attack):
                key = (ability.title, ability.game_text)
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((pokemon, ability))
    return pairs


def _fusion_strike_bench_attacks(ctx):
    return fusion_strike_bench_attacks(ctx.board, ctx.player_id)


async def cross_fusion_strike(ctx):
    """Choose 1 of your Benched Fusion Strike Pokemon's attacks and use it as
    this attack."""
    candidates = _fusion_strike_bench_attacks(ctx)
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        # Copying a locked attack means the user can't attack at all next
        # turn, not just can't reuse the copied attack.
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, entry["abilityID"])


async def max_miracle(ctx):
    """130. This attack's damage isn't affected by any effects on your
    opponent's Active Pokemon."""
    await ctx.deal_damage(130, ignore_target_effects=True)


# --- Special-condition attack factory ---------------------------------------

def condition_attack(*conditions, flip=False, self_conditions=(), counters=1):
    """Effect factory: printed damage, then apply the conditions (all of them
    on heads when flip=True; nothing on tails)."""
    async def effect(ctx):
        await ctx.deal_damage()
        if flip:
            results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
            if not results or not results[0]:
                return
        for condition in conditions:
            await ctx.apply_special_condition(ctx.defender, condition, poison_counters=counters)
        for condition in self_conditions:
            await ctx.apply_special_condition(ctx.attacker, condition, poison_counters=counters)
    return effect


# --- Drizzile / Inteleon (SWSH1): Shady Dealings ----------------------------

def shady_dealings(count):
    """On evolve: search the deck for up to `count` Trainer card(s), reveal
    them, and put them into hand. Then shuffle."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            is_trainer_card, count=count, minimum=0,
            prompt=f"Choose up to {count} Trainer card(s) to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


# --- Dunsparce (SWSH3): Final Dig --------------------------------------------

async def final_dig(ctx):
    """If Knocked Out by damage from an attack from your opponent's Pokemon:
    discard the top 2 cards of your opponent's deck."""
    if not ctx.ko_from_attack:
        return
    await ctx.discard_cards(ctx.deck_top(2, player_id=ctx.opponent_id))


# --- Gengar (SWSH6): Last Gift -----------------------------------------------

async def last_gift(ctx):
    """If Knocked Out by damage from an attack from your opponent's Pokemon:
    search the deck for up to 2 cards and put them into hand. Then shuffle."""
    if not ctx.ko_from_attack:
        return
    picks = await ctx.search_deck(
        count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.",
    )
    # No "reveal" clause on this card's text.
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


# --- Toxicroak (SWSH1): More Poison ------------------------------------------

async def more_poison(ctx):
    """Between Pokemon Checkups: put 2 more damage counters on your
    opponent's Poisoned Active."""
    target = ctx.opponent_active()
    if target is None:
        return
    conditions = target.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    if CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED] not in conditions:
        return
    await ctx.deal_damage(20, target=target, apply_modifiers=False, is_attack=False)


# ======================================================================
# Lost Zone Box + Regigigas decks
# ======================================================================

def is_energy_card(card) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value


def is_lightning_energy(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.LIGHTNING.value in types


def is_pokemon_gx(archetype_id) -> bool:
    return "GX" in subtypes_for(archetype_id)


def is_pokemon_vmax(archetype_id) -> bool:
    return "VMAX" in subtypes_for(archetype_id)

def in_active_spot(board, player_id, pokemon) -> bool:
    """Ability condition: this Pokemon is in the Active Spot."""
    return pokemon is board.active_pokemon(player_id)

def dragons_hoard_condition(board, player_id, pokemon) -> bool:
    """Active-spot only, and only when it would draw at least 1 card (a hand of
    4+ can't draw up to 4, so the ability may not be used)."""
    hand = board.find_player_area(player_id, "hand")
    hand_size = len(hand.children) if hand else 0
    return in_active_spot(board, player_id, pokemon) and hand_size < 4

async def _damage_up_to_two(ctx, targets_pool, amount, prompt):
    """Deal `amount` to up to 2 distinct Pokemon the player chooses (bench
    damage takes no Weakness/Resistance; the Active does)."""
    chosen = await ctx.choose_cards(targets_pool, 2, prompt=prompt)
    active = ctx.opponent_active()
    for target in chosen:
        await ctx.deal_damage(amount, target=target, apply_modifiers=target is active)


# --- Crobat V (SHF): Dark Asset / Venomous Fang --------------------------

async def dark_asset(ctx):
    """On play from hand: you may draw until you have 6 cards in your hand."""
    if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


# --- Drapion V (LOR): Wild Style / Dynamic Tail --------------------------

class WildStylePassive(Passive):
    """This Pokemon's attacks cost [C] less for each of the opponent's Single
    Strike, Rapid Strike, and Fusion Strike Pokemon in play."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        owner = carrier.owning_player_id
        opponent = next((p for p in board.player_ids if p != owner), None)
        if opponent is None or "Colorless" not in cost:
            return cost
        discount = sum(
            1 for p in board.pokemon_in_play(opponent)
            if any(s in ("Single Strike", "Rapid Strike", "Fusion Strike")
                   for s in subtypes_for(p.archetype_id))
        )
        if discount <= 0:
            return cost
        remaining = cost["Colorless"] - discount
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


async def dynamic_tail(ctx):
    """190. This attack also does 60 damage to 1 of your Pokemon."""
    await ctx.deal_damage()
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to take 60 damage"
    )
    if target is not None:
        await ctx.deal_damage(60, target=target, apply_modifiers=False)


# --- Dragonite V (EVS): Shred / Dragon Gale ------------------------------

async def shred(ctx):
    """50. Damage isn't affected by any effects on the opponent's Active."""
    await ctx.deal_damage(50, ignore_target_effects=True)


async def dragon_gale(ctx):
    """250. Also does 20 damage to each of your Benched Pokemon."""
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


# --- Aerodactyl V (LOR): Rock Crush --------------------------------------

async def rock_crush(ctx):
    """120. Discard an Energy from your opponent's Active Pokemon."""
    await ctx.deal_damage()
    active = ctx.opponent_active()
    if active is None:
        return
    energies = ctx.attached_energies(active)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Discard an Energy from the Defending Pokémon",
    )
    await ctx.discard_cards(picks)


# --- Aerodactyl VSTAR (LOR): Lost Dive / Ancient Star --------------------

AERODACTYL_VSTAR_GUID = "6f389b61-a045-5659-bd41-cf3d7c08dc41"


class AncientStarPassive(Passive):
    """While active (after Ancient Star), the opponent's Pokemon V in play
    (except Aerodactyl VSTAR) have no Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        if not getattr(carrier, "_ancient_star", False):
            return False
        if pokemon.owning_player_id == carrier.owning_player_id:
            return False
        return (
            is_pokemon_v(pokemon.archetype_id)
            and (pokemon.archetype_id or "").lower() != AERODACTYL_VSTAR_GUID
        )


# The granted Ability contributes AncientStarPassive once it rides the
# attacker's PIE_ABILITIES; its abilityID must be a registered GUID.
ANCIENT_STAR_GRANTED = Ability(
    title="Ancient Star",
    game_text="Your opponent's Pokémon V in play, except any Aerodactyl VSTAR, have no Abilities.",
    passive=AncientStarPassive(),
)
ANCIENT_STAR_GRANTED.ability_id = ability_id_for(AERODACTYL_VSTAR_GUID, 90)
ABILITIES_BY_ID[ANCIENT_STAR_GRANTED.ability_id] = ANCIENT_STAR_GRANTED


async def lost_dive(ctx):
    """240. Put the top 3 cards of your deck in the Lost Zone."""
    await ctx.deal_damage()
    await ctx.move_to_lost_zone(ctx.deck_top(3))


async def ancient_star(ctx):
    """VSTAR Power: gain the ability that shuts off the opponent's Pokemon V's
    Abilities (except Aerodactyl VSTAR) until this Pokemon leaves play."""
    ctx.attacker._ancient_star = True
    entries = list(ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != ANCIENT_STAR_GRANTED.ability_id
           for e in entries if isinstance(e, dict)):
        entries.append(ANCIENT_STAR_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(
            ctx.attacker, AttrID.PIE_ABILITIES, entries
        )


# --- Zeraora (VIV): Fighting Lightning -----------------------------------

async def fighting_lightning(ctx):
    """30, plus 80 more if the opponent's Active is a Pokemon V or GX."""
    active = ctx.opponent_active()
    bonus = 80 if active is not None and (
        is_pokemon_v(active.archetype_id) or is_pokemon_gx(active.archetype_id)
    ) else 0
    await ctx.deal_damage(30 + bonus)


# --- Comfey (LOR): Flower Selecting --------------------------------------

async def flower_selecting(ctx):
    """Look at the top 2 cards of your deck; put 1 into your hand, the other
    in the Lost Zone."""
    top = ctx.deck_top(2)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, minimum=1,
        prompt="Put 1 card into your hand; the other goes to the Lost Zone.",
    )
    if not picks:
        return
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.move_to_lost_zone([c for c in top if c not in picks])


# --- Sableye (LOR): Lost Mine --------------------------------------------

def lost_mine_condition(board, player_id, pokemon):
    """Usable only with 10 or more cards in the Lost Zone."""
    lost = board.find_player_area(player_id, "lostZone")
    return bool(lost) and len(lost.children) >= 10


async def lost_mine(ctx):
    """Put 12 damage counters on your opponent's Pokemon in any way you like."""
    await ctx.place_damage_counters(12, ctx.opponent_pokemon_in_play())


# --- Cramorant (LOR): Lost Provisions / Spit Innocently ------------------

class LostProvisionsPassive(Passive):
    """If you have 4+ cards in the Lost Zone, ignore all Energy in this
    Pokemon's attack costs."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        lost = board.find_player_area(carrier.owning_player_id, "lostZone")
        if lost and len(lost.children) >= 4:
            return {}
        return cost


async def spit_innocently(ctx):
    """110. This attack's damage isn't affected by Weakness."""
    await ctx.deal_damage(ignore_weakness=True)


# --- Radiant Greninja (ASR): Concealed Cards / Moonlight Shuriken --------

def has_energy_in_hand(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_energy_card(c) for c in hand.children)


async def concealed_cards(ctx):
    """Discard an Energy card from your hand, then draw 2 cards."""
    discarded = await ctx.discard_from_hand(
        1, predicate=is_energy_card,
        prompt="Discard an Energy card to use Concealed Cards",
    )
    if discarded:
        await ctx.draw_cards(2)


async def moonlight_shuriken(ctx):
    """Discard 2 Energy from this Pokemon; 90 damage to 2 of the opponent's
    Pokemon (no Weakness/Resistance for Benched Pokemon)."""
    await ctx.discard_energy_from(
        ctx.attacker, 2, prompt="Discard 2 Energy from Radiant Greninja"
    )
    await _damage_up_to_two(
        ctx, ctx.opponent_pokemon_in_play(), 90,
        "Choose a Pokémon to take 90 damage",
    )


# --- Regigigas (ASR): Ancient Wisdom / Gigaton Break ---------------------

_REGI_NAMES = {"Regirock", "Regice", "Registeel", "Regieleki", "Regidrago"}


def _regi_names_in_play(board, player_id):
    return {
        p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        for p in board.pokemon_in_play(player_id)
    }


def ancient_wisdom_condition(board, player_id, pokemon):
    """All five Regis in play and an Energy in the discard pile."""
    if not _REGI_NAMES.issubset(_regi_names_in_play(board, player_id)):
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_energy_card(c) for c in discard.children)


async def ancient_wisdom(ctx):
    """Attach up to 3 Energy cards from your discard pile to 1 of your Pokemon."""
    energies = [c for c in ctx.discard_pile() if is_energy_card(c)]
    picks = await ctx.choose_cards(
        energies, 3, minimum=1,
        prompt="Choose up to 3 Energy from your discard pile to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to"
    )
    if target is None:
        return
    ctx.visual_targets = [target.entity_id]
    for energy in picks:
        await ctx.attach_energy(energy, target)


async def gigaton_break(ctx):
    """150, plus 150 more if the opponent's Active is a Pokemon VMAX."""
    active = ctx.opponent_active()
    bonus = 150 if active is not None and is_pokemon_vmax(active.archetype_id) else 0
    await ctx.deal_damage(150 + bonus)


# --- Regidrago (ASR): Dragon's Hoard -------------------------------------

async def dragons_hoard(ctx):
    """Draw cards until you have 4 cards in your hand."""
    await ctx.draw_until(4)


# --- Regidrago (EVS): Dragon Energy --------------------------------------

async def dragon_energy(ctx):
    """240, minus 20 for each damage counter on this Pokemon."""
    counters = (ctx.max_hp(ctx.attacker) - ctx.attacker.get_attribute(AttrID.HP, 0)) // 10
    await ctx.deal_damage(max(0, 240 - 20 * counters))


# --- Regirock/Registeel/Regice (ASR): Regi Gate --------------------------

async def regi_gate(ctx):
    """Search your deck for a Basic Pokemon, put it onto your Bench, shuffle."""
    if BENCH_CAPACITY - len(ctx.my_bench()) > 0:
        picks = await ctx.search_deck(
            is_basic_pokemon, count=1, minimum=0,
            prompt="Choose a Basic Pokémon to put onto your Bench.",
        )
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


# --- Registeel (ASR): Heavy Slam -----------------------------------------

async def heavy_slam(ctx):
    """220, minus 50 for each Colorless in the opponent's Active's Retreat Cost."""
    active = ctx.opponent_active()
    retreat = int(active.get_attribute(AttrID.RETREAT_COST) or 0) if active else 0
    await ctx.deal_damage(max(0, 220 - 50 * retreat))


# --- Regice (ASR): Blizzard Bind -----------------------------------------

async def blizzard_bind(ctx):
    """100. If the Defending Pokemon is a Pokemon V, it can't attack during
    your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or not is_pokemon_v(defender.archetype_id):
        return
    state = ctx.session.turn_state
    for entry in defender.get_attribute(AttrID.PIE_ABILITIES) or []:
        if isinstance(entry, dict) and entry.get("abilityType") == "Attack" \
                and entry.get("abilityID"):
            # Lock through the opponent's next turn (turn_number + 1).
            state.attack_locks[(defender.entity_id, entry["abilityID"])] = \
                state.turn_number + 1


# --- Regieleki (ASR): Electromagnetic Sonar / Targeted Bolt --------------

async def electromagnetic_sonar(ctx):
    """Put a Trainer card from your discard pile into your hand."""
    trainers = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1,
        prompt="Choose a Trainer card to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=False)


async def targeted_bolt(ctx):
    """Discard 2 Lightning Energy from this Pokemon; 120 damage to 1 of the
    opponent's Benched Pokemon."""
    await ctx.discard_energy_from(
        ctx.attacker, 2, predicate=is_lightning_energy,
        prompt="Discard 2 Lightning Energy from Regieleki",
    )
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is not None:
        await ctx.deal_damage(120, target=target, apply_modifiers=False)


# --- Regieleki (EVS): Teraspark ------------------------------------------

async def teraspark(ctx):
    """120. Discard all Lightning Energy from this Pokemon; also 40 damage to
    2 of the opponent's Benched Pokemon."""
    await ctx.deal_damage()
    await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=is_lightning_energy,
        prompt="Discard all Lightning Energy from Regieleki",
    )
    await _damage_up_to_two(
        ctx, ctx.opponent_bench(), 40,
        "Choose a Benched Pokémon to take 40 damage",
    )
