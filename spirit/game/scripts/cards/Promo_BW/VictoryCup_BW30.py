from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


async def victory_cup(ctx):
    """Flip a coin. If heads, search your deck for a Pokemon, reveal it, and
    put it into your hand. Shuffle your deck afterward."""
    results = await ctx.flip_coins(1, "Victory Cup")
    if results and results[0]:
        picks = await ctx.search_deck(is_pokemon_card, count=1, minimum=0, prompt="Choose a Pok\u00e9mon")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="56e5538f-f57c-5e2e-9d4b-8de6204257ea",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryCup.Name",
    display_name="Victory Cup",
    searchable_by=["Victory Cup", "Item"],
    subtypes=["Item"],
    collector_number=30,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    effect=victory_cup
)
