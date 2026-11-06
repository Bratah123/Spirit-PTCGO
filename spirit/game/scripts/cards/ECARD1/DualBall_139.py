from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import is_basic_non_baby


async def dual_ball(ctx):
    """Flip 2 coins; for each heads search for a Basic non-Baby Pokémon."""
    results = await ctx.flip_coins(2, "Dual Ball")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    picks = await ctx.search_deck(
        is_basic_non_baby, count=heads, minimum=0,
        prompt="Choose Basic Pokémon (other than Baby Pokémon) to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="e6f4e260-36e7-5ad7-95a4-a64421839dd8",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball"],
    subtypes=[],
    collector_number=139,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=dual_ball,
)
