from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def paint_roller_condition(board, player_id):
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


async def paint_roller(ctx):
    """Discard any Stadium card in play. Then, draw a card."""
    await ctx.discard_stadium()
    await ctx.draw_cards(1)


card = ItemCardDef(
    guid="b15e2067-8360-58c1-b37c-ffea09f3bcd5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PaintRoller.Name",
    display_name="Paint Roller",
    searchable_by=["Paint Roller", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=paint_roller,
    condition=paint_roller_condition
)
