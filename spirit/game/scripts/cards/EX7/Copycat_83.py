from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def copycat(ctx):
    """Shuffle your hand into your deck. Draw a card for each card in your opponent's hand."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    count = ctx.hand_size(ctx.opponent_id)
    if count > 0:
        await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="0a2629c9-5743-5c4c-9dc0-325c6f542be1",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=copycat
)
