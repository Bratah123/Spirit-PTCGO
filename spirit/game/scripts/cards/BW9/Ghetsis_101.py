from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_item_card


async def ghetsis(ctx):
    """Your opponent reveals their hand and shuffles all Item cards found there
    into their deck. Then, draw a card for each Item card shuffled in."""
    hand = await ctx.reveal_hand(ctx.opponent_id) or []
    items = [c for c in hand if is_item_card(c)]
    if items:
        await ctx.shuffle_into_deck(items, ctx.opponent_id)
        await ctx.draw_cards(len(items))


card = SupporterCardDef(
    guid="ba47b87e-6a16-59ac-8381-7dcd97bf7c94",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ghetsis.Name",
    display_name="Ghetsis",
    searchable_by=["Ghetsis", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=101,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    effect=ghetsis
)
