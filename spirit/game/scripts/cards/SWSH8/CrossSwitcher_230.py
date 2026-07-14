from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_bench


def _named(card, name):
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == name


def _second_copy(ctx):
    return next((c for c in ctx.hand()
                 if c.entity_id != ctx.source.entity_id
                 and _named(c, "Cross Switcher")), None)


def _playable(board, player_id, card):
    """Needs a 2nd Cross Switcher in hand and an opposing Benched Pokemon."""
    hand = board.find_player_area(player_id, "hand")
    has_pair = any(c.entity_id != card.entity_id and _named(c, "Cross Switcher")
                   for c in (hand.children if hand else []))
    return has_pair and opponent_has_bench(board, player_id)


async def cross_switcher(ctx):
    """Play 2 at once: discard the 2nd copy, gust an opposing Benched Pokemon
    into the Active Spot; if you do, switch your own Active with a Benched one."""
    pair = _second_copy(ctx)
    if pair is None:
        return
    await ctx.discard_cards([pair])
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose the opponent's new Active Pokémon"
    )
    if target is None or not await ctx.switch_active(ctx.opponent_id, target):
        return
    my_bench = ctx.my_bench()
    if not my_bench:
        return
    # Flush the gust so both clients see it land before the own-side pick.
    await ctx.flush_choreography()
    mine = await ctx.choose_pokemon(my_bench, "Choose your new Active Pokémon")
    if mine is not None:
        await ctx.switch_active(ctx.player_id, mine)


card = ItemCardDef(
    guid="4643a72f-8166-5787-a6f5-2605f06339ad",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrossSwitcher.Name",
    display_name="Cross Switcher",
    searchable_by=["Cross Switcher", "Item", "Fusion Strike"],
    subtypes=["Item", "Fusion Strike"],
    collector_number=230,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    condition=_playable,
    effect=cross_switcher,
)
