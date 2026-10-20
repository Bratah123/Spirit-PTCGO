from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def hugh(ctx):
    """Each player draws or discards until they have 5 cards in hand
    (your opponent goes first)."""
    for pid in (ctx.opponent_id, ctx.player_id):
        size = len(ctx.hand(pid))
        if size < 5:
            await ctx.draw_until(5, pid)
        elif size > 5:
            await ctx.discard_from_hand(size - 5, minimum=size - 5, player_id=pid,
                                        prompt=f"Discard {size - 5} card(s) down to 5")


card = SupporterCardDef(
    guid="e65008f5-1b43-5b61-b244-d159baf7db68",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hugh.Name",
    display_name="Hugh",
    searchable_by=["Hugh", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=hugh
)
