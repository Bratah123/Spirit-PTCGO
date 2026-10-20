from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions


async def _rain_dish(ctx):
    """At any times between turns, heal 20 damage from this Pokemon."""
    await ctx.heal(20, ctx.source)


async def _groovy_dance(ctx):
    """Printed damage; you may discard an Energy attached to this Pokemon. If
    you do, the Defending Pokemon is now Confused."""
    await ctx.deal_damage()
    d = ctx.defender
    if not ctx.attached_energies(ctx.attacker) or d is None:
        return
    if not await ctx.ask_yes_no("Discard an Energy to Confuse the Defending Pokémon?"):
        return
    if await ctx.discard_energy_from(ctx.attacker, 1, minimum=1) and not ctx.effects_blocked(d):
        await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="dc9260f8-a956-57ba-af3f-c66444f692f1",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Rain Dish",
            game_text="At any times between turns, heal 20 damage from this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=_rain_dish,
        ),
        Attack(
            title="Groovy Dance",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_groovy_dance,
        ),
    ],
)