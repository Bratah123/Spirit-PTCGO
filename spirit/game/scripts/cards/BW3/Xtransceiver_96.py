from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_supporter_card


async def xtransceiver(ctx):
    """Flip a coin. If heads, search your deck for a Supporter card, reveal
    it, and put it into your hand. Then, shuffle your deck."""
    if (await ctx.flip_coins(1, "Xtransceiver"))[0]:
        await search_to_hand(
            is_supporter_card, count=1, minimum=0, reveal=True,
            prompt="Choose a Supporter card.",
        )(ctx)


card = ItemCardDef(
    guid="366251ef-5691-5e67-bf80-4bf88b52fae6",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Xtransceiver.Name",
    display_name="Xtransceiver",
    searchable_by=["Xtransceiver", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=xtransceiver,
)
