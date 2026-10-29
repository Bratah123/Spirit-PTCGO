from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def mallow(ctx):
    """Search your deck for 2 cards, shuffle, put those cards on top in any order."""
    picks = await ctx.search_deck(
        None, count=2, minimum=0,
        prompt="Choose up to 2 cards to put on top of your deck.",
    )
    await ctx.shuffle_deck()
    if len(picks) > 1:
        order = await ctx.choose_cards(
            picks, len(picks), minimum=len(picks), ordered=True,
            prompt="Put the cards on top of your deck in any order.",
        )
        picks = order or picks
    for card in picks:
        await ctx.put_on_top_of_deck(card)


card = SupporterCardDef(
    guid="999af1e2-d460-56b7-b812-18dcfed40236",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mallow.Name",
    display_name="Mallow",
    searchable_by=["Mallow", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=mallow,
)
