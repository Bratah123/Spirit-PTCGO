from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def _rotom_dex_condition(board, player_id):
    prizes = board.find_player_area(player_id, "prizePile")
    return bool(prizes and prizes.children)


async def _rotom_dex(ctx):
    """Shuffle your Prize cards into your deck, then put that many cards from
    the top of your deck face down as your Prize cards."""
    prizes_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(prizes_area.children if prizes_area else [])
    if not prizes:
        return
    await ctx.shuffle_into_deck(prizes, ctx.player_id)
    await ctx.put_in_prizes(ctx.deck_top(len(prizes)), ctx.player_id)


card = ItemCardDef(
    guid="5e94fa4a-54ad-5206-864e-f34de06f53a2",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDex.Name",
    display_name="Rotom Dex",
    searchable_by=["Rotom Dex", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=_rotom_dex,
    condition=_rotom_dex_condition
)
