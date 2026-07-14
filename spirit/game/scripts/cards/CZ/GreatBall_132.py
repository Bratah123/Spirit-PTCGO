from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


async def great_ball(ctx):
    """Look at the top 7 cards of your deck. You may reveal a Pokemon you
    find there and put it into your hand. Shuffle the other cards back."""
    top = ctx.deck_top(7)
    candidates = [c for c in top if is_pokemon_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="You may put a Pokémon into your hand.",
        display_cards=top,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="86f22ea3-8a9a-5100-b3e1-a5be7f53f923",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=great_ball
)
