from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def _rotom_bike_effect(ctx):
    """Draw cards until you have 6 cards in your hand. Your turn ends."""
    await ctx.draw_until(6)
    ctx.ends_turn = True


card = ItemCardDef(
    guid="a78976d1-210b-51fc-b16c-686b107a2df6",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomBike.Name",
    display_name="Rotom Bike",
    searchable_by=["Rotom Bike", "Item"],
    subtypes=["Item"],
    collector_number=63,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=_rotom_bike_effect,
)
