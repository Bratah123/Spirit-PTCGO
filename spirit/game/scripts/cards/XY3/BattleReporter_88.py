from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def battle_reporter(ctx):
    """Draw cards until you have as many cards in hand as your opponent."""
    await ctx.draw_until(ctx.hand_size(ctx.opponent_id))


card = SupporterCardDef(
    guid="439780a0-3336-5ebe-99b8-8abfba93d6ea",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleReporter.Name",
    display_name="Battle Reporter",
    searchable_by=["Battle Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=battle_reporter
)
