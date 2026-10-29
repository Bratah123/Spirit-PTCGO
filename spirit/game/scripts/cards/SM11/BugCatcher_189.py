from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def bug_catcher(ctx):
    """Draw 2 cards. Flip a coin; if heads, draw 2 more cards."""
    await ctx.draw_cards(2)
    heads = (await ctx.flip_coins(1, "Bug Catcher"))[0]
    if heads:
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="824cd96a-2209-5375-8ffb-c0694a5407ba",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BugCatcher.Name",
    display_name="Bug Catcher",
    searchable_by=["Bug Catcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=bug_catcher
)
