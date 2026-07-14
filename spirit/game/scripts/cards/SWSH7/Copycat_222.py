from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def copycat(ctx):
    """Shuffle your hand into your deck. Draw a card for each card in your opponent's hand."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    count = ctx.hand_size(ctx.opponent_id)
    if count > 0:
        await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="06b5a68c-6612-5201-b505-010966316dc4",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=222,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    effect=copycat
)
