from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _any_tool_in_play(board, player_id, card=None):
    return any(child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
               for pid in board.player_ids
               for pokemon in board.pokemon_in_play(pid)
               for child in pokemon.children)


async def tool_scrapper(ctx):
    """Choose up to 2 Pok\u00e9mon Tools attached to Pok\u00e9mon in play
    (either side) and discard them."""
    tools = [tool for tool, _holder in ctx.tools_in_play()]
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, min(2, len(tools)), minimum=1,
        prompt="Choose up to 2 Pok\u00e9mon Tool cards to discard")
    if picks:
        await ctx.discard_cards(picks)


card = ItemCardDef(
    guid="8b68c57e-60c9-58fd-b87c-aa6e2dd4a841",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolScrapper.Name",
    display_name="Tool Scrapper",
    searchable_by=["Tool Scrapper", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    effect=tool_scrapper,
    condition=_any_tool_in_play
)
