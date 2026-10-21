from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _own_tools(board, player_id):
    return [c for p in board.pokemon_in_play(player_id) for c in p.children
            if c.get_attribute(AttrID.TRAINER_TYPE) in (
                TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)]


def tool_retriever_condition(board, player_id):
    return bool(_own_tools(board, player_id))


async def tool_retriever(ctx):
    """Put up to 2 Pokemon Tool cards attached to your Pokemon into your hand."""
    tools = _own_tools(ctx.board, ctx.player_id)
    if not tools:
        return
    picks = await ctx.choose_cards(tools, 2, minimum=1,
                                   prompt="Choose up to 2 Pokémon Tool cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid="b7c58442-1e30-51b9-b283-f08a6b335f2e",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolRetriever.Name",
    display_name="Tool Retriever",
    searchable_by=["Tool Retriever", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=tool_retriever,
    condition=tool_retriever_condition
)
