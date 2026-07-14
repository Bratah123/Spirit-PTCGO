from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def bug_catcher(ctx):
    """Draw 2 cards. Flip a coin; if heads, draw 2 more cards."""
    await ctx.draw_cards(2)
    heads = (await ctx.flip_coins(1, "Bug Catcher"))[0]
    if heads:
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="0c008faf-9553-50c3-b40b-b9249c38d9bb",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BugCatcher.Name",
    display_name="Bug Catcher",
    searchable_by=["Bug Catcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=226,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=bug_catcher
)
