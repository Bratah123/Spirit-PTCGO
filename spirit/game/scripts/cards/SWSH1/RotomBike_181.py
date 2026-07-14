from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def _rotom_bike_effect(ctx):
    """Draw cards until you have 6 cards in your hand. Your turn ends."""
    await ctx.draw_until(6)
    ctx.ends_turn = True


card = ItemCardDef(
    guid="a0bfd7b6-5c3e-5d34-a153-6904c38724d2",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomBike.Name",
    display_name="Rotom Bike",
    searchable_by=["Rotom Bike", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=_rotom_bike_effect,
)
