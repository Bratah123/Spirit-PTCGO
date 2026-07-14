from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_supporter_card


async def pokegear_30(ctx):
    """Look at the top 7 cards of the deck; may reveal a Supporter found
    there and put it into hand. Shuffle the rest back into the deck."""
    top = ctx.deck_top(7)
    if not top:
        return
    candidates = [c for c in top if is_supporter_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a Supporter card to put into your hand.",
        display_cards=top,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="307f7f44-275a-52a2-8f2e-300fd37739e1",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name",
    display_name="PokÃ©gear 3.0",
    searchable_by=["Pok\u00c3\u00a9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=174,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=pokegear_30
)
