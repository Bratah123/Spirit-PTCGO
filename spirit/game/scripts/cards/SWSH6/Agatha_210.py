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
    guid="970774b9-32fa-5f60-bff7-ffc32bdac0af",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Agatha.Name",
    display_name="Agatha",
    searchable_by=["Agatha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=210,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    effect=agatha
)
