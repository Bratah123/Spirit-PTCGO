from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def copycat(ctx):
    """Shuffle your hand into your deck. Draw a card for each card in your opponent's hand."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    count = ctx.hand_size(ctx.opponent_id)
    if count > 0:
        await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="d256b5ed-7e16-582d-9828-0e8f68580918",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=copycat
)
