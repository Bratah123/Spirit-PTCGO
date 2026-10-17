from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def watcheck(ctx):
    """Look at top 5 of opponent's deck; put back in any order."""
    await ctx.reorder_deck_top(
        5,
        player_id=ctx.opponent_id,
        prompt="Rearrange the top cards of your opponent's deck",
    )


async def quick_tail_smash(ctx):
    """Optional flip before damage: heads +60; tails nothing; no flip = printed."""
    if await ctx.ask_yes_no("Flip a coin for Quick Tail Smash?"):
        if not (await ctx.flip_coins(1, ctx.ability.title))[0]:
            return
        await ctx.deal_damage(80)
    else:
        await ctx.deal_damage(20)


card = PokemonCardDef(
    guid="0876a883-621b-5d93-9a46-78b966ce3264",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1", "Watchog"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Watcheck",
            game_text="Look at the top 5 cards of your opponent's deck and put them back on top of his or her deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=watcheck,
        ),
        Attack(
            title="Quick Tail Smash",
            game_text="Before doing damage, you may flip a coin. If heads, this attack does 60 more damage. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=quick_tail_smash,
        ),
    ],
)
