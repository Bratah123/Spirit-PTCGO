from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.pokemon import energy_provides_type


async def _sand_slammer(ctx):
    """Between turns, if this Pokemon is your Active, put 1 damage counter on
    each of your opponent's Pokemon."""
    if ctx.source is not ctx.my_active():
        return
    for pokemon in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False, as_counters=True)


async def _flying_beatdown(ctx):
    """Printed damage; you may discard a Grass and a Fighting Energy attached to
    this Pokemon. If you do, the Defending Pokemon is now Paralyzed."""
    await ctx.deal_damage()
    mine = ctx.attached_energies(ctx.attacker)
    grass = [e for e in mine if energy_provides_type(e, PokemonTypes.GRASS.value)]
    fight = [e for e in mine if energy_provides_type(e, PokemonTypes.FIGHTING.value)]
    pair = None
    for g in grass:
        f = next((x for x in fight if x is not g), None)
        if f is not None:
            pair = [g, f]
            break
    if pair is None or not await ctx.ask_yes_no("Discard a Grass and a Fighting Energy to Paralyze?"):
        return
    await ctx.discard_cards(pair)
    if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="dff407ba-5498-5dff-9e7c-4acfd2b5dbd3",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=99,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sand Slammer",
            game_text="At any time between turns, if this Pok\u00e9mon is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=_sand_slammer,
        ),
        Attack(
            title="Flying Beatdown",
            game_text="You may discard a Grass Energy and a Fighting Energy attached to this Pok\u00e9mon. If you do, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_flying_beatdown,
        ),
    ],
)