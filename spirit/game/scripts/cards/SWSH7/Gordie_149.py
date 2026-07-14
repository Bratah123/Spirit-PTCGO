from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import is_energy_card


async def gordie(ctx):
    """Look at the top 7 cards of your deck. You may reveal any number of
    Energy cards you find there and put them into your hand. Shuffle the
    other cards back into your deck."""
    top = ctx.deck_top(7)
    candidates = [c for c in top if is_energy_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        candidates, max(len(candidates), 1), minimum=0,
        prompt="Choose Energy cards to put into your hand.",
        display_cards=top,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="114fed3f-796f-5c17-8fc3-3c77eac969e6",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gordie.Name",
    display_name="Gordie",
    searchable_by=["Gordie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    effect=gordie
)
