"""Behaviors for the Special Energy cards of the Lugia VSTAR archetype deck."""

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for, is_pokemon_v
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


# --- EX-era Multi / Rainbow / Double Rainbow / Team Energies ---------------

# Same as ALL_TYPES_ONE_AT_A_TIME but each option provides two of that type.
ALL_TYPES_TWO_AT_A_TIME = [
    [t, t] for t in (
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
        PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.FAIRY,
        PokemonTypes.DRAGON, PokemonTypes.COLORLESS,
    )
]


class MultiEnergyPassive(Passive):
    """Multi Energy: every type one-at-a-time, unless the holder already has
    another Special Energy attached — then Colorless only."""

    def modify_energy_provided(self, options, energy, holder, board):
        d = def_for(energy.archetype_id)
        if not isinstance(getattr(d, "passive", None), MultiEnergyPassive):
            return options
        if holder is None:
            return options
        others = [
            c for c in holder.children
            if c is not energy and c.get_attribute(AttrID.IS_SPECIAL_ENERGY)
        ]
        if others:
            return [[PokemonTypes.COLORLESS.value]]
        return options


async def rainbow_energy_on_attach(ctx):
    """Put 1 damage counter on the Pokémon this was attached to."""
    target = ctx.attached_to
    if target is not None:
        await ctx.deal_damage(amount=10, target=target, as_counters=True)


class DoubleRainbowPassive(Passive):
    """Damage the holder does to opposing Pokémon is reduced by 10 after W/R."""

    def modify_damage_taken(self, calc, carrier):
        # Runs after the W/R stage; reduce when the attacker is our holder.
        if not (calc.is_attack and calc.is_opposing):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is None or pokemon is not calc.attacker:
            return
        calc.amount = max(0, calc.amount - 10)


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


def discard_energy_if_not_evolved(energy_guid: str):
    """BETWEEN_TURNS: if holder is no longer Evolved, discard this Energy."""
    from spirit.game.session.effects import is_evolution_pokemon

    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        if is_evolution_pokemon(pokemon):
            return
        energy = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == energy_guid.lower()),
            None)
        if energy is not None:
            await ctx.discard_cards([energy])
    return effect


def attach_to_evolved_non_ex():
    """Double Rainbow: Evolved Pokémon excluding Pokémon-ex."""
    from spirit.game.session.effects import is_evolution_pokemon
    from spirit.game.data_utils import subtypes_for

    def check(pokemon) -> bool:
        if not is_evolution_pokemon(pokemon):
            return False
        return "ex" not in subtypes_for(
            getattr(pokemon, "archetype_id", None) or "")
    return check


def attach_to_team_name(*teams: str):
    """Magma/Aqua Energy: Pokémon with Team X in its name."""
    lowered = tuple(t.lower() for t in teams)

    def check(pokemon) -> bool:
        d = def_for(pokemon.archetype_id)
        dn = (getattr(d, "display_name", None) or "").lower()
        return any(t in dn for t in lowered)
    return check
