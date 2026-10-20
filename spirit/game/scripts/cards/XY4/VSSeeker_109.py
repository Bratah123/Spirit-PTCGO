from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_supporter_card


def vs_seeker_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard and any(is_supporter_card(c) for c in discard.children))


async def vs_seeker(ctx):
    """Put a Supporter card from your discard pile into your hand."""
    cards = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Supporter card")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="f8bef826-caea-5575-926e-0ffca16f2c5e",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=vs_seeker,
    condition=vs_seeker_condition
)
