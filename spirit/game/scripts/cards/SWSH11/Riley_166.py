from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def _riley_effect(ctx):
    """Reveal the top 5 cards of your deck; your opponent chooses 2 to
    discard, the rest go to your hand."""
    top = ctx.deck_top(5)
    if not top:
        return
    count = min(2, len(top))
    discard_picks = await ctx.choose_cards(
        top, count, player_id=ctx.opponent_id,
        prompt="Choose 2 cards to discard.",
        display_cards=top,
    )
    keep = [c for c in top if c not in discard_picks]
    if discard_picks:
        await ctx.discard_cards(discard_picks)
    if keep:
        await ctx.put_in_hand(keep, reveal=False)


card = SupporterCardDef(
    guid="882fea74-0f0d-57a7-a1a5-b537ffcca399",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Riley.Name",
    display_name="Riley",
    searchable_by=["Riley", "Supporter"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    effect=_riley_effect,
)
