from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def caitlin(ctx):
    """Put as many cards from your hand as you like on the bottom of your deck
    in any order (pick order = bottom order), then draw a card for each."""
    hand = list(ctx.hand())
    if not hand:
        return
    picks = await ctx.choose_cards(hand, len(hand), minimum=0,
                                   prompt="Choose cards to put on the bottom of your deck (in order)")
    moved = 0
    for card in picks or []:
        if await ctx.put_on_bottom_of_deck(card):
            moved += 1
    if moved:
        await ctx.draw_cards(moved)


card = SupporterCardDef(
    guid="0c2cf89d-b106-56ad-b7d6-aa9d046b34ae",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caitlin.Name",
    display_name="Caitlin",
    searchable_by=["Caitlin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=caitlin
)
