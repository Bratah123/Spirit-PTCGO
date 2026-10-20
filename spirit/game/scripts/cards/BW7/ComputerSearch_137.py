from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least


async def computer_search(ctx):
    """ACE SPEC: discard 2 cards from your hand, then search your deck for any
    card and put it into your hand; shuffle."""
    if len(await ctx.discard_from_hand(2, prompt="Discard 2 cards for Computer Search")) < 2:
        return
    picks = await ctx.search_deck(None, count=1, minimum=0,
                                  prompt="Choose a card to put into your hand.")
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="f827aa15-b0c6-58a2-8fcb-21f1ccff73ac",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=137,
    set_code="BW7",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=computer_search,
    condition=hand_size_at_least(3)
)
