from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def team_rockets_handiwork(ctx):
    """Flip 2 coins. For each heads, discard 2 cards from the top of your opponent's deck."""
    results = await ctx.flip_coins(2, "Team Rocket's Handiwork")
    n = 2 * sum(1 for r in results or [] if r)
    cards = ctx.deck_top(n, ctx.opponent_id)
    if cards:
        await ctx.discard_cards(cards)


card = SupporterCardDef(
    guid="7117ef04-9e42-5aa4-a20e-39951495e458",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHandiwork.Name",
    display_name="Team Rocket's Handiwork",
    searchable_by=["Team Rocket's Handiwork", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=team_rockets_handiwork
)
