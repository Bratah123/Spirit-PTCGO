from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def colress(ctx):
    """Shuffle your hand into your deck, then draw a card for each Benched
    Pokemon (both yours and your opponent's)."""
    n = len(ctx.my_bench()) + len(ctx.opponent_bench())
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    if n:
        await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="3d45398c-b56e-511a-8ff5-9e81fd107622",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Colress.Name",
    display_name="Colress",
    searchable_by=["Colress", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=118,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=colress
)
