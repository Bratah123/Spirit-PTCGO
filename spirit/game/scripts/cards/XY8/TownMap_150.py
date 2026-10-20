from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def town_map(ctx):
    """Turn all of your Prize cards face up (approximation: you look at them;
    the engine has no persistent face-up Prize state)."""
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(area.children) if area else []
    if prizes:
        await ctx.choose_cards(prizes, 0, minimum=0, display_cards=prizes, prompt="Your Prize cards")


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
    effect=town_map
)
