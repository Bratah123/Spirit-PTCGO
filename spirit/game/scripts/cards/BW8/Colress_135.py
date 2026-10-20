from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def colress(ctx):
    """Shuffle your hand into your deck, then draw a card for each Benched
    Pokemon (both yours and your opponent's)."""
    n = len(ctx.my_bench()) + len(ctx.opponent_bench())
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    if n:
        await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="5a2ed0ca-d5bf-55bb-aa66-5924901e2bc3",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Colress.Name",
    display_name="Colress",
    searchable_by=["Colress", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=135,
    set_code="BW8",
    rarity=Rarities.RareUltra,
    effect=colress
)
