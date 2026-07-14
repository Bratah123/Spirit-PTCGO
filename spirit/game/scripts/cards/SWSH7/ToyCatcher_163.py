from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID


def _opponent_id(board, player_id):
    for pid in board.player_ids:
        if pid != player_id:
            return pid
    return None


def _toy_catcher_targets(board, player_id):
    opponent = _opponent_id(board, player_id)
    if opponent is None:
        return []
    bench = board.find_player_area(opponent, "bench")
    if not bench:
        return []
    return [p for p in bench.children if p.get_attribute(AttrID.HP, 0) <= 50]


def toy_catcher_condition(board, player_id):
    return bool(_toy_catcher_targets(board, player_id))


async def toy_catcher(ctx):
    """Switch 1 of the opponent's Benched Pokemon that has 50 HP or less
    remaining with their Active Pokemon."""
    targets = [p for p in ctx.opponent_bench() if p.get_attribute(AttrID.HP, 0) <= 50]
    target = await ctx.choose_pokemon(targets, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = ItemCardDef(
    guid="0fcd3510-0d73-5bbf-9426-6bd9a417b7cc",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToyCatcher.Name",
    display_name="Toy Catcher",
    searchable_by=["Toy Catcher", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    effect=toy_catcher,
    condition=toy_catcher_condition,
)
