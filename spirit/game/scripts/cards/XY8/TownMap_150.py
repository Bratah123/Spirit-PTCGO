from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def town_map_condition(board, player_id):
    """Playable only with a face-down Prize card left to turn."""
    area = board.find_player_area(player_id, "prizePile")
    return bool(area) and any(not getattr(c, "face_up_prize", False) for c in area.children)


async def town_map(ctx):
    """Turn all of your Prize cards face up (they remain face up for the rest of the game)."""
    await ctx.turn_prizes_face_up()


card = ItemCardDef(
    guid="c8904062-e8ac-5c98-8b22-e1548f1a257e",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownMap.Name",
    display_name="Town Map",
    searchable_by=["Town Map", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=town_map,
    condition=town_map_condition
)
