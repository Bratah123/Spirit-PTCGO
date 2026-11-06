"""XY-era Special Energy behaviors: the type-locked family ("This card can only
be attached to X Pokemon ... provides X Energy only while attached to a X
Pokemon ... (If this card is attached to anything other than a X Pokemon,
discard this card.)") plus Rainbow and Team Aqua/Magma double energies.

Type-locked cards use `attach_to=only_type(T)`, `provides=[[T]]` and
`discard_unless_attach_to=True`; the engine discards them whenever the holder
stops matching (checked before each action offer and at end of turn), so the
benefits below only need to re-check the type for the in-between moments.
"""

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.content.definitions import def_for, subtypes_for
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive, carrier_pokemon


def _has_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    return pokemon is not None and \
        pokemon_type.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def only_type(pokemon_type: PokemonTypes):
    """attach_to predicate: "can only be attached to <type> Pokemon"."""
    return lambda pokemon: _has_type(pokemon, pokemon_type)


def only_named(prefix: str):
    """attach_to predicate on the card name ("Team Aqua's", "Team Magma's")."""
    def check(pokemon):
        definition = def_for(getattr(pokemon, "archetype_id", None))
        name = getattr(definition, "display_name", "") or ""
        return name.startswith(prefix)
    return check


def _holder(carrier, pokemon_type):
    pokemon = carrier_pokemon(carrier)
    return pokemon if _has_type(pokemon, pokemon_type) else None


# ----------------------------------------------------------------- on attach

async def rainbow_on_attach(ctx):
    """When you attach this card from your hand to 1 of your Pokemon, put 1
    damage counter on that Pokemon."""
    if ctx.attached_to is not None:
        await ctx.deal_damage(10, target=ctx.attached_to, apply_modifiers=False,
                              is_attack=False, as_counters=True)


async def herbal_on_attach(ctx):
    """When you attach this card from your hand to 1 of your Grass Pokemon,
    heal 30 damage from that Pokemon."""
    if _has_type(ctx.attached_to, PokemonTypes.GRASS):
        await ctx.heal(30, ctx.attached_to)


# ------------------------------------------------------------------ passives

class StrongEnergyPassive(Passive):
    """The attacks of the Fighting Pokemon this card is attached to do 20 more
    damage to your opponent's Active Pokemon (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        holder = _holder(carrier, PokemonTypes.FIGHTING)
        if holder is not None and holder is calc.attacker and calc.is_attack \
                and calc.is_opposing and calc.to_active:
            calc.amount += 20


class MysteryEnergyPassive(Passive):
    """The Retreat Cost of the Pokemon this card is attached to is CC less."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon and _has_type(pokemon, PokemonTypes.PSYCHIC):
            return max(0, cost - 2)
        return cost


class WonderEnergyPassive(Passive):
    """Prevent all effects of your opponent's attacks, except damage, done to
    the Fairy Pokemon this card is attached to."""

    def blocks_attack_effects(self, target, carrier):
        return target is _holder(carrier, PokemonTypes.FAIRY)


class ShieldEnergyPassive(Passive):
    """The attacks of your opponent's Pokemon do 10 less damage to the Metal
    Pokemon this card is attached to (before applying W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        holder = _holder(carrier, PokemonTypes.METAL)
        if holder is None or holder is not calc.target or not calc.is_attack \
                or not calc.is_opposing or calc.ignore_target_effects:
            return
        calc.amount -= 10


class FlashEnergyPassive(Passive):
    """The Lightning Pokemon this card is attached to has no Weakness."""

    def modify_weakness(self, calc, carrier):
        if calc.target is _holder(carrier, PokemonTypes.LIGHTNING):
            calc.weakness_applies = False


class SplashEnergyPassive(Passive):
    """If the Water Pokemon this card is attached to is Knocked Out by damage
    from an opponent's attack, put that Pokemon into your hand (attached cards
    are discarded -- the engine always discards attachments)."""

    def knockout_destination(self, pokemon, carrier):
        if pokemon is _holder(carrier, PokemonTypes.WATER) \
                and getattr(pokemon, "ko_by_opponent_attack_damage", False):
            return "hand"
        return None


async def dangerous_energy_damaged(ctx):
    """Whenever the Darkness Pokemon this card is attached to is your Active
    Pokemon and is damaged by an attack from your opponent's Pokemon-EX (even
    if it is Knocked Out), put 2 damage counters on the Attacking Pokemon-EX."""
    pokemon, attacker = ctx.attached_to, getattr(ctx, "damaged_by", None)
    if attacker is None or not _has_type(pokemon, PokemonTypes.DARKNESS) \
            or not is_in_active_spot(pokemon) or "EX" not in subtypes_for(attacker.archetype_id):
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False,
                          is_attack=False, as_counters=True)
