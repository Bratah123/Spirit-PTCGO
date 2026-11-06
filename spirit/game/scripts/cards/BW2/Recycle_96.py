from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard


async def recycle(ctx):
    """Flip a coin. If heads, put a card from your discard pile on top of your deck."""
    results = await ctx.flip_coins(1, "Recycle")
    if not results or not results[0]:
        return
    discard = list(ctx.discard_pile())
    if not discard:
        return
    picks = await ctx.choose_cards(
        discard, 1, minimum=1,
        prompt="Choose a card to put on top of your deck.",
    )
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = ItemCardDef(
    guid="08517d71-90c7-5629-b4b2-7d3db1763e53",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recycle.Name",
    display_name="Recycle",
    searchable_by=["Recycle", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=recycle,
    condition=requires_discard(),
)
