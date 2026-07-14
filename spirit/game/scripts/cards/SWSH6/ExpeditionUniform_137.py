from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def expedition_uniform(ctx):
    """Look at the bottom 3 cards of your deck and put them on top of your
    deck in any order."""
    bottom = ctx.deck()[:3]
    if not bottom:
        return
    picks = await ctx.choose_cards(
        bottom, len(bottom), minimum=len(bottom), ordered=True,
        prompt="Put these cards on top of your deck, in order",
    )
    for card in picks:
        await ctx.put_on_top_of_deck(card)


card = ItemCardDef(
    guid="bbe8c187-08f1-533a-9ec5-e1306bc2067b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpeditionUniform.Name",
    display_name="Expedition Uniform",
    searchable_by=["Expedition Uniform", "Item"],
    subtypes=["Item"],
    collector_number=137,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=expedition_uniform,
)
