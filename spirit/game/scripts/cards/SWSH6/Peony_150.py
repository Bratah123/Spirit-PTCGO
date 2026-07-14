from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_trainer_card


async def peony(ctx):
    """Discard your hand and search up to 2 Trainer cards, reveal, put into hand, then shuffle."""
    hand = ctx.hand()
    if hand:
        await ctx.discard_cards(hand)
    picks = await ctx.search_deck(
        is_trainer_card, count=2, minimum=0,
        prompt="Choose up to 2 Trainer cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="468ae19b-b9d0-5335-ada8-7b27389a2e08",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Peony.Name",
    display_name="Peony",
    searchable_by=["Peony", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=peony
)
