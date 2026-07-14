from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_item_card


async def miss_fortune_sisters(ctx):
    """Look at the top 5 cards of your opponent's deck and discard any
    number of Item cards you find there. Your opponent shuffles the other
    cards back into their deck."""
    top = ctx.deck_top(5, player_id=ctx.opponent_id)
    if not top:
        return
    items = [c for c in top if is_item_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        items, max(len(items), 1), minimum=0,
        prompt="Choose any number of Item cards to discard",
        display_cards=top if len(items) < len(top) else None,
    )
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck(ctx.opponent_id)


card = SupporterCardDef(
    guid="a294cf50-f40b-57f8-bee5-a7e9f5f520ac",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MissFortuneSisters.Name",
    display_name="Miss Fortune Sisters",
    searchable_by=["Miss Fortune Sisters", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    effect=miss_fortune_sisters,
)
