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
    guid="e6192c06-9992-544d-b2a1-de32994d1037",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ghetsis.Name",
    display_name="Ghetsis",
    searchable_by=["Ghetsis", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=115,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    effect=ghetsis
)
