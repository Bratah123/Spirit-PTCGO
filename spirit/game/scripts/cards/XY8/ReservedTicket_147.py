from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def reserved_ticket(ctx):
    """Flip a coin. If heads, search your deck for a card, shuffle, then put it on top."""
    results = await ctx.flip_coins(1, "Reserved Ticket")
    if not (results and results[0]):
        return
    picks = await ctx.search_deck(None, count=1, minimum=0, prompt="Choose a card to put on top")
    await ctx.shuffle_deck()
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = ItemCardDef(
    guid="b3f7ca8f-d81a-5893-b7e7-c9e7bc56799a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReservedTicket.Name",
    display_name="Reserved Ticket",
    searchable_by=["Reserved Ticket", "Item"],
    subtypes=["Item"],
    collector_number=147,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=reserved_ticket
)
