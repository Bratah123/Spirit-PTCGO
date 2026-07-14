from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, SpecialConditions


async def _spicy_seasoned_curry(ctx):
    active = ctx.my_active()
    if active is None:
        return
    await ctx.apply_special_condition(active, SpecialConditions.BURNED)
    await ctx.heal(40, target=active)


card = ItemCardDef(
    guid="1fc1ca9a-1280-5569-8ce4-9b06412630d7",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpicySeasonedCurry.Name",
    display_name="Spicy Seasoned Curry",
    searchable_by=["Spicy Seasoned Curry", "Item"],
    subtypes=["Item"],
    collector_number=151,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=_spicy_seasoned_curry,
)
