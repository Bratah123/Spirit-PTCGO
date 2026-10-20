from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def battle_reporter(ctx):
    """Draw cards until you have as many cards in hand as your opponent."""
    await ctx.draw_until(ctx.hand_size(ctx.opponent_id))


card = SupporterCardDef(
    guid="c0b3a52a-81b9-55bf-bee9-03d6d5214416",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleReporter.Name",
    display_name="Battle Reporter",
    searchable_by=["Battle Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    effect=battle_reporter
)
