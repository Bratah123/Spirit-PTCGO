from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def choy(ctx):
    """Each player reveals their hand. Draw 3 cards."""
    await ctx.reveal_hand(ctx.player_id, ctx.opponent_id)
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="1479c7a3-c3c3-56e4-86fa-d770af40c554",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Choy.Name",
    display_name="Choy",
    searchable_by=["Choy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=choy,
)
