from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _balloon_bomb(ctx):
    """Flip 2 coins; for each heads, discard the top 2 cards of your opponent's deck."""
    results = await ctx.flip_coins(2, ctx.ability.title)
    heads = sum(1 for r in results or [] if r)
    if heads:
        await ctx.discard_cards(ctx.deck_top(2 * heads, player_id=ctx.opponent_id))


async def _thick_liquid(ctx):
    """80; both Active Pokemon are now Confused and Poisoned."""
    await ctx.deal_damage()
    for p in (ctx.opponent_active(), ctx.my_active()):
        if p is not None:
            await ctx.apply_special_condition(p, SpecialConditions.CONFUSED)
            await ctx.apply_special_condition(p, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="496d3579-320d-5ae2-8ef4-48bca82ea2d3",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Balloon Bomb",
            game_text="Flip 2 coins. For each heads, discard 2 cards from the top of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_balloon_bomb,
        ),
        Attack(
            title="Thick Liquid",
            game_text="Both Active Pok\u00e9mon are now Confused and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_thick_liquid,
        ),
    ],
)