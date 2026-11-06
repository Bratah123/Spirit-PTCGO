from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for


_FOSSILS = ("Helix Fossil Omanyte", "Dome Fossil Kabuto", "Old Amber Aerodactyl")


def _pool(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return [c for c in (discard.children if discard else [])
            if getattr(def_for(c.archetype_id), "display_name", "") in _FOSSILS]


def fossil_excavation_kit_condition(board, player_id):
    return bool(_pool(board, player_id))


async def fossil_excavation_kit(ctx):
    """Put 2 in any combination of Helix Fossil Omanyte, Dome Fossil Kabuto, or
    Old Amber Aerodactyl cards from your discard pile into your hand."""
    pool = _pool(ctx.board, ctx.player_id)
    n = min(2, len(pool))
    picked = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose cards to put into your hand")
    if picked:
        await ctx.put_in_hand(picked)


card = ItemCardDef(
    guid="0348e1db-4ecb-513f-a4a5-d205e26ab877",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationKit.Name",
    display_name="Fossil Excavation Kit",
    searchable_by=["Fossil Excavation Kit", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    condition=fossil_excavation_kit_condition,
    effect=fossil_excavation_kit
)
