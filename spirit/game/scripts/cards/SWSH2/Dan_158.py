from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def dan(ctx):
    """Draw 2 cards. (Rock-Paper-Scissors bonus draw is unscripted -- no RPS engine capability.)"""
    await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="eef4c1b0-77f4-5523-a0c4-c1749b53d1a8",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dan.Name",
    display_name="Dan",
    searchable_by=["Dan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=158,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=dan
)
