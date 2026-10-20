from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def acro_bike(ctx):
    """Look at the top 2 cards of your deck; put 1 into your hand, discard the other."""
    top = ctx.deck_top(2)
    if not top:
        return
    picks = await ctx.choose_cards(top, 1, minimum=1, display_cards=top,
                                   prompt="Choose a card to put into your hand") or []
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.discard_cards(rest)


card = ItemCardDef(
    guid="09c2a182-8a5a-5c10-acac-589fd1281f95",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=acro_bike,
    condition=deck_nonempty
)
