from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def ad_hoc_shock(ctx):
    """On evolve: you may flip a coin. If heads, the opponent's Active is now Paralyzed."""
    if not await ctx.ask_yes_no("Flip a coin?"):
        return
    results = await ctx.flip_coins(1, "Ad Hoc Shock")
    if not results or not results[0]:
        return
    defender = ctx.defender
    if defender is not None:
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="6806e5e1-1032-5db4-8978-3841d7bd6a7d",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    display_name="Eelektrik",
    searchable_by=["Eelektrik", "Stage 1", "Eelektrik"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    family_id=603,
    abilities=[
        Ability(
            title="Ad Hoc Shock",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            trigger=Triggers.ON_EVOLVE,
            effect=ad_hoc_shock,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
    ],
)