from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.trainers import _other_player


def _megas(board, player_id):
    bench = board.find_player_area(_other_player(board, player_id), "bench")
    return [p for p in (bench.children if bench else [])
            if "MEGA" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])]


def mega_catcher_condition(board, player_id):
    return bool(_megas(board, player_id))


async def mega_catcher(ctx):
    """Switch 1 of your opponent's Benched Mega Evolution Pokemon with his or her Active Pokemon."""
    target = await ctx.choose_pokemon(_megas(ctx.board, ctx.player_id), "Choose the opponent's new Active Pok\u00e9mon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = ItemCardDef(
    guid="c102cb21-1255-5094-95c7-7525ec80e694",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaCatcher.Name",
    display_name="Mega Catcher",
    searchable_by=["Mega Catcher", "Item"],
    subtypes=["Item"],
    collector_number=104,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    condition=mega_catcher_condition,
    effect=mega_catcher
)
