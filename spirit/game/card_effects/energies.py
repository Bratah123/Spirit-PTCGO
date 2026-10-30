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


# Miracle / Double Rainbow: every type, two at a time.
ALL_TYPES_TWO_AT_A_TIME = [
    [t, t] for t in (
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
        PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.FAIRY,
        PokemonTypes.DRAGON, PokemonTypes.COLORLESS,
    )
]


def attach_to_shining_or_light(pokemon) -> bool:
    """Miracle Energy: only Shining or Light Pokémon (EVOLUTION_LOGIC_NAME)."""
    name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""
    return name.startswith("Shining") or name.startswith("Light")


def discard_energy_end_of_turn(energy_guid: str):
    """END_OF_TURN granted ability: discard this Energy from the holder."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        energy = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == energy_guid.lower()),
            None)
        if energy is not None:
            await ctx.discard_cards([energy])
    return effect

