from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _is_pokemon_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
    )


def _tools_in_play(board):
    return [
        child
        for pid in board.player_ids
        for pokemon in board.pokemon_in_play(pid)
        for child in pokemon.children
        if _is_pokemon_tool_card(child)
    ]


def tool_scrapper_condition(board, player_id):
    return bool(_tools_in_play(board))


async def tool_scrapper(ctx):
    """Choose up to 2 Pokémon Tools attached to Pokémon (yours or your
    opponent's) and discard them."""
    tools = _tools_in_play(ctx.board)
    picks = await ctx.choose_cards(
        tools, 2, minimum=1,
        prompt="Choose up to 2 Pokémon Tools to discard.",
    )
    if picks:
        await ctx.discard_cards(picks)


card = ItemCardDef(
    guid="bb9c83d8-b506-5765-89bd-7ba4b177fb22",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolScrapper.Name",
    display_name="Tool Scrapper",
    searchable_by=["Tool Scrapper", "Item"],
    subtypes=["Item"],
    collector_number=168,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=tool_scrapper,
    condition=tool_scrapper_condition,
)
