import random
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def hooligans(ctx):
    """Flip a coin. If heads, 3 random cards from the opponent's hand are
    revealed and shuffled into their deck."""
    results = await ctx.flip_coins(1, "Hooligans Jim & Cas")
    if not results or not results[0]:
        return
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    picks = random.sample(hand, min(3, len(hand)))
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = SupporterCardDef(
    guid="95b4b0c5-f29c-58a8-947b-27f88890b72a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HooligansJimCas.Name",
    display_name="Hooligans Jim & Cas",
    searchable_by=["Hooligans Jim & Cas", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=hooligans
)
