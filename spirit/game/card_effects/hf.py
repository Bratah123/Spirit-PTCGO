"""Hidden Fates (HF) attack, ability, trainer, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import (
    AttrID, CLIENT_POKEMON_TYPE_NAMES, PokemonTypes,
)
from spirit.game.data_utils import def_for
from spirit.game.session.legal_actions import attack_cost_satisfied
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import (
    bonus_if,
    count_energy,
    damage_per,
    discard_opponent_energy_attack,
    discard_random_from_hand,
    snipe_attack,
)
from spirit.game.card_effects.passives_common import (
    is_in_active_spot,
    takes_less_passive,
)
from spirit.game.card_effects.sm3 import is_gx_or_ex, is_water_energy
from spirit.game.card_effects.sm6 import is_fighting_energy
from spirit.game.card_effects.sm10 import is_lightning_energy
from spirit.game.card_effects.sm11 import _shuffle_self_into_deck
from spirit.game.card_effects.support_common import (
    attach_from_discard,
    look_at_top,
    search_attach_energy,
    search_to_hand,
)
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.session.effects import is_supporter_card


BROCK_TRAINING_NAMES = {
    "Geodude", "Graveler", "Golem", "OnixGX", "Cubone",
    "Rhyhorn", "Rhydon", "Sudowoodo",
}
MISTY_COMMAND_NAMES = {
    "Psyduck", "Horsea", "Staryu", "StarmieGX", "Magikarp",
    "Gyarados", "Lapras",
}


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _named(pokemon, *names) -> bool:
    return _logic_name(pokemon) in names


def _display_name(card) -> str:
    return getattr(def_for(card.archetype_id), "display_name", "") or ""


def _hand_cards(board, player_id):
    area = board.find_player_area(player_id, "hand")
    return list(area.children) if area else []


# ======================================================================
# Passives / stadiums
# ======================================================================

def _onix_gx(target, _carrier) -> bool:
    return _named(target, "OnixGX")


brocks_pewter_city_gym_passive = takes_less_passive(
    40, protects=_onix_gx, stack_key="brocks_pewter")


class MistysCeruleanPassive(Passive):
    """Starmie-GX (both sides) do +40 to the opponent's Active."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or not _named(attacker, "StarmieGX"):
            return
        if "mistys_cerulean" in calc.applied_once:
            return
        calc.applied_once.add("mistys_cerulean")
        calc.amount += 40


mistys_cerulean_city_gym_passive = MistysCeruleanPassive()


# ======================================================================
# Attacks
# ======================================================================

golem_rock_slide = snipe_attack(20, pool="bench", count=3, also_base=True)

star_stream = attach_from_discard(
    is_water_energy, count=2, target="choice", minimum=0,
    prompt="Choose up to 2 Water Energy cards to attach.",
)

hydro_pump_gx = damage_per(
    count_energy("self", PokemonTypes.WATER), 40, base=40)

psycrush_gx = discard_opponent_energy_attack(count=99)


def _jessie_james_in_discard(ctx) -> bool:
    return any(_display_name(c) == "Jessie & James" for c in ctx.discard_pile())


rocket_tail = bonus_if(_jessie_james_in_discard, 80)


async def wrap(ctx):
    """10 damage; flip to discard an Energy from the opponent's Active."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Wrap")
    if not heads[0]:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose an Energy to discard from your opponent's Active Pokémon.",
    )


async def mudslide(ctx):
    """Discard 2 Fighting Energy; 80 to 1 of the opponent's Pokémon."""
    await ctx.discard_energy_from(
        ctx.attacker, 2, predicate=is_fighting_energy,
        prompt="Choose 2 Fighting Energy to discard")
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Choose a Pokémon to take 80 damage")
    if target is not None:
        await ctx.deal_damage(80, target=target)


async def lead(ctx):
    """Flip; heads searches a Supporter into hand."""
    heads = await ctx.flip_coins(1, "Lead")
    if not heads[0]:
        return
    await search_to_hand(
        is_supporter_card, count=1, reveal=True,
        prompt="Choose a Supporter card to put into your hand.",
    )(ctx)


async def happy_mime(ctx):
    """Each player draws a card."""
    await ctx.draw_cards(1, player_id=ctx.opponent_id)
    await ctx.draw_cards(1)


async def hurricane_call(ctx):
    """Flip 4; for each heads attach a Lightning Energy from the deck to a GX/EX."""
    n = sum(1 for heads in await ctx.flip_coins(4, "Hurricane Call") if heads)
    if n <= 0:
        return
    if not any(is_gx_or_ex(p) for p in ctx.my_pokemon_in_play()):
        return
    await search_attach_energy(
        is_lightning_energy, count=n, target_pred=is_gx_or_ex, distribute=True,
        prompt="Choose Lightning Energy cards to attach to your Pokémon-GX or Pokémon-EX.",
    )(ctx)


def _sky_legends_extra(ctx) -> bool:
    attacker = ctx.attacker
    if attacker is None or ctx.ability is None:
        return False
    printed = getattr(ctx.ability, "cost", None) or {}
    cost = {CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(int(k))]: v
            for k, v in printed.items()}
    for name in ("Fire", "Water", "Lightning"):
        cost[name] = cost.get(name, 0) + 1
    return attack_cost_satisfied(
        cost, ctx.board.attached_energies(attacker), ctx.board)


async def sky_legends_gx(ctx):
    """Optional 110 to 3 of the opponent's Pokémon, then shuffle this Pokémon into the deck."""
    if _sky_legends_extra(ctx):
        await snipe_attack(110, pool="any", count=3)(ctx)
    await _shuffle_self_into_deck(ctx)


# ======================================================================
# Abilities
# ======================================================================

async def last_pattern(ctx):
    """KO'd by opponent attack damage: discard 2 random cards from their hand."""
    if not ctx.ko_from_attack:
        return
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=2)


async def electromagnetic_wall(ctx):
    """While Active, opponent hand-attaches put 2 damage counters on the receiver."""
    if ctx.attaching_player_id == ctx.player_id:
        return
    me = ctx.source
    if me is None or not is_in_active_spot(me):
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    await ctx.deal_damage(
        20, target=receiver, apply_modifiers=False, as_counters=True)


async def surrender_now(ctx):
    """Opponent discards a card from their hand (Jessie & James follow-up)."""
    if not ctx.hand(ctx.opponent_id):
        return
    await ctx.discard_from_hand(
        1, player_id=ctx.opponent_id,
        prompt="Choose a card to discard from your hand.",
    )


def _has_surrender_now(card) -> bool:
    definition = def_for(card.archetype_id)
    for ability in getattr(definition, "abilities", None) or []:
        if getattr(ability, "title", "") == "Surrender Now":
            return True
    return False


# ======================================================================
# Trainers
# ======================================================================

async def jessie_james(ctx):
    """Each player discards 2 from hand (opponent first); Surrender Now may follow."""
    await ctx.discard_from_hand(
        2, player_id=ctx.opponent_id,
        prompt="Choose 2 cards to discard from your hand.",
    )
    discarded = await ctx.discard_from_hand(
        2, prompt="Choose 2 cards to discard from your hand.",
    )
    if not any(_has_surrender_now(c) for c in discarded):
        return
    if not ctx.hand(ctx.opponent_id):
        return
    if await ctx.ask_yes_no("Use Surrender Now to make your opponent discard a card?"):
        await surrender_now(ctx)


def _brock_targets(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if _logic_name(p) in BROCK_TRAINING_NAMES]


def brocks_training_condition(board, player_id) -> bool:
    return (
        any(is_energy_card(c) for c in _hand_cards(board, player_id))
        and bool(_brock_targets(board, player_id))
    )


async def brocks_training(ctx):
    """Attach an Energy from hand to a Brock's Pokémon."""
    energies = [c for c in ctx.hand() if is_energy_card(c)]
    targets = _brock_targets(ctx.board, ctx.player_id)
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


def _misty_targets(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if _logic_name(p) in MISTY_COMMAND_NAMES]


def mistys_water_command_condition(board, player_id) -> bool:
    return bool(_misty_targets(board, player_id))


async def mistys_water_command(ctx):
    """Move any number of Water Energy onto Misty's Pokémon."""
    dests = _misty_targets(ctx.board, ctx.player_id)
    if not dests:
        return
    await ctx.move_energy_freely(
        ctx.my_pokemon_in_play(), dests, predicate=is_water_energy,
        prompt="Choose a Water Energy to move",
    )


async def mistys_determination(ctx):
    """Discard a card, then look at the top 8 and take 1."""
    if not await ctx.discard_from_hand(1, prompt="Discard a card from your hand"):
        return
    await look_at_top(8, take=1, rest="shuffle")(ctx)
