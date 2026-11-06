from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top


def mistys_condition(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) >= 2


_look = look_at_top(8, take=1, rest="shuffle", prompt="Choose a card to put into your hand")


async def mistys_determination(ctx):
    """Discard a card from your hand; if you do, look at the top 8 cards and put 1 into your hand."""
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if not hand:
        return
    pick = await ctx.choose_cards(hand, 1, minimum=1, prompt="Discard a card from your hand")
    if not pick:
        return
    await ctx.discard_cards(pick)
    await _look(ctx)


card = SupporterCardDef(
    guid="06ef6071-19b1-5271-bd2f-75c68a9a5529",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDetermination.Name",
    display_name="Misty's Determination",
    searchable_by=["Misty's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=mistys_determination,
    condition=mistys_condition
)
