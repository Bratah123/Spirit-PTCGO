from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _opponent_tools(board, player_id):
    opp = next((p for p in board.player_ids if p != player_id), None)
    return [c for p in (board.pokemon_in_play(opp) if opp else []) for c in p.children if _is_tool(c)]


def startling_megaphone_condition(board, player_id):
    return bool(_opponent_tools(board, player_id))


async def startling_megaphone(ctx):
    """Discard all Pokemon Tool cards attached to each of your opponent's Pokemon."""
    tools = _opponent_tools(ctx.board, ctx.player_id)
    if tools:
        await ctx.discard_cards(tools)


card = ItemCardDef(
    guid="6c240695-897c-5aab-8df8-f67f879df73b",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StartlingMegaphone.Name",
    display_name="Startling Megaphone",
    searchable_by=["Startling Megaphone", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    effect=startling_megaphone,
    condition=startling_megaphone_condition
)
