from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def puzzle_of_time(ctx):
    """Play 2 at once to put 2 cards from your discard pile into your hand;
    1 alone: look at the top 3 cards and put them back in any order."""
    other = next((c for c in ctx.hand() if c is not ctx.source and c.archetype_id == card.guid), None)
    discard = [c for c in ctx.discard_pile() if c is not ctx.source]
    if other is not None and discard and await ctx.ask_yes_no("Play 2 Puzzle of Time cards at once?"):
        await ctx.discard_cards([other])
        pool = [c for c in ctx.discard_pile() if c is not ctx.source and c is not other]
        n = min(2, len(pool))
        if n:
            picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 cards to put into your hand")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
        return
    top = ctx.deck_top(3)
    if not top:
        return
    order = await ctx.choose_cards(top, len(top), minimum=len(top), ordered=True, display_cards=top,
                                   prompt="Choose the order (first = top)") or top
    for c in reversed(list(order)):
        await ctx.put_on_top_of_deck(c)


card = ItemCardDef(
    guid="28440831-0696-58c2-acd5-1ba1ea9f1721",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PuzzleofTime.Name",
    display_name="Puzzle of Time",
    searchable_by=["Puzzle of Time", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=puzzle_of_time
)
