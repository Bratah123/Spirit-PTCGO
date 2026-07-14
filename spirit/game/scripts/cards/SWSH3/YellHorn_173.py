from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, SpecialConditions


async def yell_horn(ctx):
    """Both Active Pokemon are now Confused."""
    my_active = ctx.my_active()
    if my_active is not None:
        await ctx.apply_special_condition(my_active, SpecialConditions.CONFUSED)
    opp_active = ctx.opponent_active()
    if opp_active is not None:
        await ctx.apply_special_condition(opp_active, SpecialConditions.CONFUSED)


card = ItemCardDef(
    guid="3a6478e1-c769-5d5d-83e4-ed876b96d75b",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.YellHorn.Name",
    display_name="Yell Horn",
    searchable_by=["Yell Horn", "Item"],
    subtypes=["Item"],
    collector_number=173,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=yell_horn
)
