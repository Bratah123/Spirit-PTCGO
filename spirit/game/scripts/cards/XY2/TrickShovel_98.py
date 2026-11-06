from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def trick_shovel_condition(board, player_id):
    return any(bool(board.find_player_area(pid, "deck").children) for pid in board.player_ids)


async def trick_shovel(ctx):
    """Look at the top card of either player's deck. You may discard it or
    return it to the top of the deck."""
    idx = await ctx.choose("Look at the top card of which deck?", ["Your deck", "Your opponent's deck"])
    pid = ctx.opponent_id if idx == 1 else ctx.player_id
    top = ctx.deck_top(1, player_id=pid)
    if not top:
        return
    await ctx.session.prompt_view_cards(ctx.player_id, ctx.source.entity_id, top,
                                        prompt="Top card of the deck")
    if await ctx.ask_yes_no("Discard that card?"):
        await ctx.discard_cards(top)


card = ItemCardDef(
    guid="19baa988-4599-57a9-a76f-6c7d9fd87212",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrickShovel.Name",
    display_name="Trick Shovel",
    searchable_by=["Trick Shovel", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    effect=trick_shovel,
    condition=trick_shovel_condition
)
