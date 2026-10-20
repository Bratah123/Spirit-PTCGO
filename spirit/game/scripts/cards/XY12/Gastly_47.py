from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, ability_id_for, ABILITIES_BY_ID
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack


async def _little_grudge_trigger(ctx):
    pokemon = ctx.source
    until = getattr(pokemon, "_little_grudge_until", None)
    turn = ctx.session.turn_state.turn_number
    if until is not None and turn == until:
        att = getattr(ctx, "ko_attacker", None)
        if getattr(ctx, "ko_from_attack", False) and att is not None and ctx.attached_energies(att):
            await ctx.discard_energy_from(att, 1, minimum=1, prompt="Discard an Energy from the Attacking Pokémon")
    if until is not None and turn >= until and ctx.damaged_by is None \
            and getattr(ctx, "attached_energy", None) is None:
        pokemon._little_grudge_until = None
        entries = [e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
                   if not (isinstance(e, dict) and e.get("abilityID") == LITTLE_GRUDGE_GRANTED.ability_id)]
        await ctx.session._broadcast_entity_attribute(pokemon, AttrID.PIE_ABILITIES, entries)


LITTLE_GRUDGE_GRANTED = Ability(
    title="Little Grudge",
    game_text="During your opponent's next turn, if this Pok\\u00e9mon is Knocked Out by damage from an attack, discard an Energy attached to the Attacking Pok\\u00e9mon.",
    trigger=(Triggers.ON_KNOCKED_OUT, Triggers.BETWEEN_TURNS),
    effect=_little_grudge_trigger,
)
LITTLE_GRUDGE_GRANTED.ability_id = ability_id_for("3b3f2e1c-0000-4000-8000-000000000047", 99)
ABILITIES_BY_ID[LITTLE_GRUDGE_GRANTED.ability_id] = LITTLE_GRUDGE_GRANTED


async def _grant_little_grudge(ctx, target):
    target._little_grudge_until = ctx.session.turn_state.turn_number + 1
    entries = list(target.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != LITTLE_GRUDGE_GRANTED.ability_id for e in entries if isinstance(e, dict)):
        entries.append(LITTLE_GRUDGE_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(target, AttrID.PIE_ABILITIES, entries)


async def _little_grudge(ctx):
    await ctx.deal_damage()
    await _grant_little_grudge(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="6de7493d-d3c3-5569-8c59-25064fb1be00",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="XY12",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=92,
    abilities=[
        Attack(
            title="Little Grudge",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is Knocked Out by damage from an attack, discard an Energy attached to the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_little_grudge,
        ),
        Attack(
            title="Nightmare",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)