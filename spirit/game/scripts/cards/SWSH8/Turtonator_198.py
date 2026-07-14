from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, Triggers, ability_id_for, ABILITIES_BY_ID,
)
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

TURTONATOR_198_GUID = "ce380d56-f682-5267-b661-6afc1d22ea1a"


async def _shell_trap_trigger(ctx):
    """Fires on ON_DAMAGED_BY_ATTACK (put counters if still within the window)
    and on BETWEEN_TURNS (cleans up the grant once the window has passed)."""
    pokemon = ctx.source
    until = getattr(pokemon, "_shell_trap_until", None)
    if ctx.damaged_by is not None:
        if until is not None and ctx.session.turn_state.turn_number == until:
            await ctx.deal_damage(
                80, target=ctx.damaged_by, apply_modifiers=False, as_counters=True
            )
        return
    if until is not None and ctx.session.turn_state.turn_number >= until:
        pokemon._shell_trap_until = None
        entries = [
            e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
            if not (isinstance(e, dict) and e.get("abilityID") == SHELL_TRAP_GRANTED.ability_id)
        ]
        await ctx.session._broadcast_entity_attribute(pokemon, AttrID.PIE_ABILITIES, entries)


SHELL_TRAP_GRANTED = Ability(
    title="Shell Trap",
    game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pokémon.",
    trigger=(Triggers.ON_DAMAGED_BY_ATTACK, Triggers.BETWEEN_TURNS),
    effect=_shell_trap_trigger,
)
SHELL_TRAP_GRANTED.ability_id = ability_id_for(TURTONATOR_198_GUID, 99)
ABILITIES_BY_ID[SHELL_TRAP_GRANTED.ability_id] = SHELL_TRAP_GRANTED


async def shell_trap(ctx):
    """30. During the opponent's next turn, being damaged by an attack puts
    8 damage counters on the attacker (even if this Pokemon is KO'd)."""
    await ctx.deal_damage()
    ctx.attacker._shell_trap_until = ctx.session.turn_state.turn_number + 1
    entries = list(ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != SHELL_TRAP_GRANTED.ability_id
           for e in entries if isinstance(e, dict)):
        entries.append(SHELL_TRAP_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(
            ctx.attacker, AttrID.PIE_ABILITIES, entries
        )


card = PokemonCardDef(
    guid="ce380d56-f682-5267-b661-6afc1d22ea1a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=198,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=776,
    abilities=[
        Attack(
            title="Shell Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=shell_trap,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)