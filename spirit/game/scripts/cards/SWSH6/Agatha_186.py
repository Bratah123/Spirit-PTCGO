from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def agatha(ctx):
    """Move up to 3 damage counters from your Active to your opponent's Active."""
    active = ctx.my_active()
    opponent_active = ctx.opponent_active()
    if active is None or opponent_active is None:
        return
    await ctx.move_damage_counters(active, opponent_active, max_count=3)


card = SupporterCardDef(
    guid="fb2eb864-2803-5933-967d-299f057f565f",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Agatha.Name",
    display_name="Agatha",
    searchable_by=["Agatha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    effect=agatha
)
