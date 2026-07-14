from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def caitlin(ctx):
    """Put any number of hand cards on the bottom of the deck in any order,
    then draw that many cards."""
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, len(hand), minimum=0, ordered=True,
        prompt="Choose any number of cards to put on the bottom of your deck, in order.",
    )
    if not picks:
        return
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)
    await ctx.draw_cards(len(picks))


card = SupporterCardDef(
    guid="ba755403-7be0-5457-8923-c58fc662dddf",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caitlin.Name",
    display_name="Caitlin",
    searchable_by=["Caitlin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    effect=caitlin
)
