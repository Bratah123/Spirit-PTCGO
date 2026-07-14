from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def digging_duo(ctx):
    """Flip a coin: heads look at bottom 8, tails bottom 3; put 1 into hand."""
    heads, = await ctx.flip_coins(1, "Digging Duo")
    bottom = ctx.deck()[:8 if heads else 3]
    if bottom:
        picks = await ctx.choose_cards(
            bottom, 1, prompt="Choose a card to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="bba06028-290f-5617-8d42-9f4927565f2f",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiggingDuo.Name",
    display_name="Digging Duo",
    searchable_by=["Digging Duo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=digging_duo,
)
