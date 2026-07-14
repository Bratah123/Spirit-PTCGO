from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def allister(ctx):
    """Draw 3 cards. If you drew any, discard up to 3 (at least 1) from hand."""
    drawn = await ctx.draw_cards(3)
    if drawn <= 0:
        return
    count = min(3, ctx.hand_size())
    if count <= 0:
        return
    await ctx.discard_from_hand(count, minimum=1, prompt="Discard up to 3 cards from your hand")


card = SupporterCardDef(
    guid="3b15b907-d1ba-5330-b6dc-32a506b89346",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Allister.Name",
    display_name="Allister",
    searchable_by=["Allister", "Supporter"],
    subtypes=["Supporter"],
    collector_number=192,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    effect=allister
)
