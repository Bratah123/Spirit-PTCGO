from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def choy(ctx):
    """Each player reveals their hand. Draw 3 cards."""
    await ctx.reveal_hand(ctx.player_id, ctx.opponent_id)
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="8d696952-8618-5bb7-9c79-ed5fb18ec5b2",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Choy.Name",
    display_name="Choy",
    searchable_by=["Choy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=182,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=choy,
)
