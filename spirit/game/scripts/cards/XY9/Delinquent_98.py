from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def delinquent_condition(board, player_id):
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


async def delinquent(ctx):
    """Discard any Stadium in play; if you do, your opponent discards 3 cards from their hand."""
    if await ctx.discard_stadium() is None:
        return
    hand = list(ctx.hand(ctx.opponent_id))
    n = min(3, len(hand))
    if n:
        picks = await ctx.choose_cards(hand, n, minimum=n, prompt="Discard 3 cards from your hand",
                                       player_id=ctx.opponent_id)
        if picks:
            await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="69bcc164-329e-5742-b18a-d8992a01cef1",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name",
    display_name="Delinquent",
    searchable_by=["Delinquent", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=delinquent,
    condition=delinquent_condition
)
