from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, ability_id_for, ABILITIES_BY_ID
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _scout(ctx):
    """Printed damage; your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(ctx.opponent_id)


async def _reflective_shield_trigger(ctx):
    pokemon = ctx.source
    until = getattr(pokemon, "_reflective_until", None)
    turn = ctx.session.turn_state.turn_number
    if until is not None and turn == until:
        if ctx.damaged_by is not None:
            await ctx.deal_damage(50, target=ctx.damaged_by, apply_modifiers=False, as_counters=True)
            return
    if until is not None and turn >= until and ctx.damaged_by is None \
            and getattr(ctx, "attached_energy", None) is None:
        pokemon._reflective_until = None
        entries = [e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
                   if not (isinstance(e, dict) and e.get("abilityID") == REFLECTIVE_SHIELD_GRANTED.ability_id)]
        await ctx.session._broadcast_entity_attribute(pokemon, AttrID.PIE_ABILITIES, entries)


REFLECTIVE_SHIELD_GRANTED = Ability(
    title="Reflective Shield",
    game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 5 damage counters on the Attacking Pokémon.",
    trigger=(Triggers.ON_DAMAGED_BY_ATTACK, Triggers.BETWEEN_TURNS),
    effect=_reflective_shield_trigger,
)
REFLECTIVE_SHIELD_GRANTED.ability_id = ability_id_for("0f36dd67-7c1d-5aa2-96e1-16db5548fd03", 99)
ABILITIES_BY_ID[REFLECTIVE_SHIELD_GRANTED.ability_id] = REFLECTIVE_SHIELD_GRANTED


async def _grant_reflective_shield(ctx, target):
    target._reflective_until = ctx.session.turn_state.turn_number + 1
    entries = list(target.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != REFLECTIVE_SHIELD_GRANTED.ability_id for e in entries if isinstance(e, dict)):
        entries.append(REFLECTIVE_SHIELD_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(target, AttrID.PIE_ABILITIES, entries)


async def _reflective_shield(ctx):
    """During your opponent's next turn, if this Pokemon is damaged by an attack, 5 counters on the attacker."""
    await _grant_reflective_shield(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="0f36dd67-7c1d-5aa2-96e1-16db5548fd03",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=561,
    abilities=[
        Attack(
            title="Reflective Shield",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put 5 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_reflective_shield,
        ),
        Attack(
            title="Psy Report",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=_scout,
        ),
    ],
)