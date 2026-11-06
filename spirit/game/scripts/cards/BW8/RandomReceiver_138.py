from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_supporter_card


async def random_receiver(ctx):
    """Reveal cards from the top of your deck until you reveal a Supporter;
    put it into your hand and shuffle the other revealed cards back."""
    deck = ctx.deck()
    if not deck:
        return
    revealed = []
    supporter = None
    for card in reversed(deck):  # topmost first
        revealed.append(card)
        if is_supporter_card(card):
            supporter = card
            break
    await ctx.reveal_cards(revealed)
    if supporter is not None:
        await ctx.put_in_hand([supporter], reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ee8f1352-2792-5a04-902a-cefd6892fc1a",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="BW8",
    rarity=Rarities.RareSecret,
    effect=random_receiver
)
