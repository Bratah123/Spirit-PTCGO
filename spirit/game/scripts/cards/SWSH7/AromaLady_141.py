from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def aroma_lady(ctx):
    drawn = await ctx.draw_cards(2)
    if not drawn:
        return
    active = ctx.my_active()
    if active is not None:
        await ctx.cure_all_conditions(active)


card = SupporterCardDef(
    guid="2f2c650c-aaeb-5f5d-9fa5-5b4c90e67c9c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AromaLady.Name",
    display_name="Aroma Lady",
    searchable_by=["Aroma Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    effect=aroma_lady,
)
