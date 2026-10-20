from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def roller_skates(ctx):
    """Flip a coin. If heads, draw 3 cards."""
    results = await ctx.flip_coins(1, "Roller Skates")
    if results and results[0]:
        await ctx.draw_cards(3)


card = ItemCardDef(
    guid="762c8466-bfbb-5e0b-ab40-00861f03ed81",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkates.Name",
    display_name="Roller Skates",
    searchable_by=["Roller Skates", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=roller_skates,
    condition=deck_nonempty
)
