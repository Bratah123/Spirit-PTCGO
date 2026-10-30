"""Behaviors for the Special Energy cards of the Lugia VSTAR archetype deck."""

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import is_pokemon_v
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import Passive, carrier_pokemon

# Aurora Energy provides every type of Energy, one at a time.
ALL_TYPES_ONE_AT_A_TIME = [
    [t] for t in (
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
        PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.FAIRY,
        PokemonTypes.DRAGON, PokemonTypes.COLORLESS,
    )
]


def _pokemon_has_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    return pokemon_type.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def another_card_in_hand(board, player_id) -> bool:
    """Aurora's gate: the hand must hold a second card to discard."""
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) >= 2


async def aurora_attach_cost(ctx) -> bool:
    """Attaching Aurora Energy costs discarding another card from hand."""
    picks = await ctx.discard_from_hand(
        1, prompt="Discard a card to attach Aurora Energy", exclude=[ctx.source]
    )
    return bool(picks)


async def capture_on_attach(ctx):
    """On attach from hand: search the deck for a Basic onto the Bench."""
    if len(ctx.my_bench()) == BENCH_CAPACITY:
        return
    
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def speed_lightning_on_attach(ctx):
    """On attach from hand: draw 2 cards only if the target is a Lightning Pokemon."""
    if _pokemon_has_type(ctx.attached_to, PokemonTypes.LIGHTNING):
        await ctx.draw_cards(2)


class PowerfulColorlessPassive(Passive):
    """+20 damage to the opponent's Active from the Colorless carrier."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker:
            return
        if _pokemon_has_type(pokemon, PokemonTypes.COLORLESS):
            calc.amount += 20


class DoubleTurboPassive(Passive):
    """The carrier's attacks do 20 less damage."""

    def modify_damage_dealt(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.attacker
        ):
            calc.amount -= 20


class HeatFirePassive(Passive):
    """The Fire Pokemon this card is attached to gets +20 max HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon \
                and _pokemon_has_type(pokemon, PokemonTypes.FIRE):
            return 20
        return 0


async def gift_energy_on_ko(ctx):
    """When the carrier is Knocked Out by an opponent's attack: draw cards
    until you have 7 cards in your hand."""
    await ctx.draw_until(7)


class VGuardPassive(Passive):
    """The carrier takes 30 less damage from opposing Pokemon V (after W/R)."""

    def modify_damage_taken(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.target
            and calc.attacker is not None
            and is_pokemon_v(calc.attacker.archetype_id)
            # "This effect can't be applied more than once at a time."
            and not getattr(calc, "_v_guard_applied", False)
        ):
            calc._v_guard_applied = True
            calc.amount = max(0, calc.amount - 30)


# === DP-era Special Energy ===

def _holder_has_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    if pokemon is None:
        return False
    return pokemon_type.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


class SpecialDarknessEnergyPassive(Passive):
    """Attached Darkness Pokémon's attacks do +10 to Active (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker:
            return
        if _holder_has_type(pokemon, PokemonTypes.DARKNESS):
            calc.amount += 10


class SpecialMetalEnergyPassive(Passive):
    """Metal holder takes 10 less damage from attacks (after W/R)."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack:
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.target:
            return
        if _holder_has_type(pokemon, PokemonTypes.METAL):
            calc.amount = max(0, calc.amount - 10)


# Multi Energy: every type one at a time; Colorless if holder already has Special Energy.
MULTI_ENERGY_PROVIDES = [
    [t] for t in (
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
        PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.COLORLESS,
    )
]


class MultiEnergyPassive(Passive):
    """If holder already has another Special Energy, Multi provides only Colorless."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or board is None:
            return options
        for child in list(getattr(holder, "children", []) or []):
            if child is energy:
                continue
            if child.get_attribute(AttrID.IS_SPECIAL_ENERGY):
                return [[PokemonTypes.COLORLESS.value]]
        return options


async def health_energy_on_attach(ctx):
    """Remove 1 damage counter from the Pokémon this was attached to."""
    target = getattr(ctx, "attached_to", None)
    if target is not None:
        await ctx.heal(10, target)


async def recover_energy_on_attach(ctx):
    """Remove all Special Conditions from the Pokémon this was attached to."""
    target = getattr(ctx, "attached_to", None)
    if target is not None and hasattr(ctx, "cure_all_conditions"):
        await ctx.cure_all_conditions(target)


async def cyclone_energy_on_attach(ctx):
    """If attached to Active: opponent switches Defending with a Bench Pokémon."""
    target = getattr(ctx, "attached_to", None)
    if target is None:
        return
    # Must be Active
    active = ctx.my_active()
    if active is not target:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    pick = await ctx.choose_pokemon(
        bench, "Switch Defending with which Benched Pokémon?",
        player_id=ctx.opponent_id)
    if pick:
        await ctx.switch_active(ctx.opponent_id, pick)


async def warp_energy_on_attach(ctx):
    """If attached to Active: switch that Pokémon with 1 of your Bench."""
    target = getattr(ctx, "attached_to", None)
    if target is None:
        return
    active = ctx.my_active()
    if active is not target:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    pick = await ctx.choose_pokemon(bench, "Switch with which Benched Pokémon?")
    if pick:
        await ctx.switch_active(ctx.player_id, pick)


async def call_energy_ability(ctx):
    """Search up to 2 Basic onto Bench; shuffle; turn ends.
    Only usable when Call Energy's holder is Active."""
    src = getattr(ctx, "source", None)
    holder = carrier_pokemon(src) if src is not None else None
    if holder is None:
        holder = ctx.my_active()
    if holder is None or holder is not ctx.my_active():
        return
    open_slots = BENCH_CAPACITY - len(ctx.my_bench())
    if open_slots <= 0:
        await ctx.shuffle_deck()
        return
    n = min(2, open_slots)
    picks = await ctx.search_deck(
        is_basic_pokemon, count=n, minimum=0,
        prompt="Up to 2 Basic Pokémon onto your Bench")
    for card in picks or []:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()
    ctx.ends_turn = True


def call_energy_ability_condition(board, player_id, pokemon=None):
    """Holder (`pokemon`) must be the player's Active Pokémon."""
    if pokemon is None:
        return False
    active = board.active_pokemon(player_id) if hasattr(board, "active_pokemon") else None
    return active is pokemon
