from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, ability_id_for, ABILITIES_BY_ID
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_damage


async def _boo_hoo_trigger(ctx):
    pokemon = ctx.source
    until = getattr(pokemon, "_boo_hoo_until", None)
    turn = ctx.session.turn_state.turn_number
    if until is not None and turn == until:
        if getattr(ctx, "energy_receiver", None) is pokemon \
                and getattr(ctx, "attaching_player_id", None) == pokemon.owning_player_id:
            await ctx.apply_special_condition(pokemon, SpecialConditions.ASLEEP)
        if getattr(ctx, "attached_energy", None) is not None:
            return
    if until is not None and turn >= until and ctx.damaged_by is None \
            and getattr(ctx, "attached_energy", None) is None:
        pokemon._boo_hoo_until = None
        entries = [e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
                   if not (isinstance(e, dict) and e.get("abilityID") == BOO_HOO_GRANTED.ability_id)]
        await ctx.session._broadcast_entity_attribute(pokemon, AttrID.PIE_ABILITIES, entries)


BOO_HOO_GRANTED = Ability(
    title="Boo-Hoo",
    game_text="If your opponent attaches an Energy card from his or her hand to this Pokémon during his or her next turn, it will be Asleep.",
    trigger=(Triggers.ON_ENERGY_ATTACHED, Triggers.BETWEEN_TURNS),
    effect=_boo_hoo_trigger,
)
BOO_HOO_GRANTED.ability_id = ability_id_for("79bd7159-0356-59a5-9064-3d391457b7c4", 99)
ABILITIES_BY_ID[BOO_HOO_GRANTED.ability_id] = BOO_HOO_GRANTED


async def _grant_boo_hoo(ctx, target):
    target._boo_hoo_until = ctx.session.turn_state.turn_number + 1
    entries = list(target.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != BOO_HOO_GRANTED.ability_id for e in entries if isinstance(e, dict)):
        entries.append(BOO_HOO_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(target, AttrID.PIE_ABILITIES, entries)


async def _boo_hoo(ctx):
    """20; if the opponent attaches an Energy from hand to the Defending Pokemon next turn, it is Asleep."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d):
        await _grant_boo_hoo(ctx, d)


card = PokemonCardDef(
    guid="79bd7159-0356-59a5-9064-3d391457b7c4",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1", "Lilligant"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Boo-Hoo",
            game_text="If your opponent attaches an Energy card from his or her hand to the Defending Pok\u00e9mon during his or her next turn, that Pok\u00e9mon will be Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=_boo_hoo,
        ),
        Attack(
            title="Leaf Slice",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)