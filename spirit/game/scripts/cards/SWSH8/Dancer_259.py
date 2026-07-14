from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def dancer(ctx):
    """Draw 2; if you go second and it's your first turn, draw 3 more."""
    await ctx.draw_cards(2)
    if ctx.session.turn_state.turn_number == 2:
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="d233b9b5-d616-55e0-806e-e3a1f4d4f9d0",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dancer.Name",
    display_name="Dancer",
    searchable_by=["Dancer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=259,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    effect=dancer
)
