from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def dancer(ctx):
    """Draw 2; if you go second and it's your first turn, draw 3 more."""
    await ctx.draw_cards(2)
    if ctx.session.turn_state.turn_number == 2:
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="b2b95674-22c8-51c7-9419-c9cfc3cde7bc",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dancer.Name",
    display_name="Dancer",
    searchable_by=["Dancer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=274,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    effect=dancer
)
