from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
async def gym_badge(ctx):
    """Flip a coin until you get tails. For each heads, draw a card."""
    heads = await ctx.flip_until_tails("Gym Badge")
    if heads:
        await ctx.draw_cards(heads)


card = ItemCardDef(
    guid="1d33efd0-6852-5ef1-992a-dabbdc0fc41d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=205,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=gym_badge
)
