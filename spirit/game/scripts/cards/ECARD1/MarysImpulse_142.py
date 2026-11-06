from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def marys_impulse(ctx):
    """Flip until tails; for each heads draw 2 cards."""
    heads = 0
    while True:
        results = await ctx.flip_coins(1, "Mary's Impulse")
        if not results or not results[0]:
            break
        heads += 1
    if heads:
        await ctx.draw_cards(heads * 2)


card = SupporterCardDef(
    guid="91e720d8-9311-56cb-ae4e-b30e4218c729",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarysImpulse.Name",
    display_name="Mary's Impulse",
    searchable_by=["Mary's Impulse", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=marys_impulse,
)
