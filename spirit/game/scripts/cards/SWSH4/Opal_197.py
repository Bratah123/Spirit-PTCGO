from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def opal_effect(ctx):
    """Flip 2 coins. Search your deck for a number of cards up to the
    number of heads, put them into your hand, and shuffle your deck."""
    heads = await ctx.flip_coins(2, "Opal")
    count = heads.count(True)
    if count > 0:
        picks = await ctx.search_deck(
            count=count, minimum=0, prompt=f"Choose up to {count} cards",
        )
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="492d90a6-8ce4-58cc-9391-1ae466724108",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Opal.Name",
    display_name="Opal",
    searchable_by=["Opal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=197,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    effect=opal_effect,
)
