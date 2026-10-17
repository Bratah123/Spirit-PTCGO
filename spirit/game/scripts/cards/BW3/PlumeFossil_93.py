from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities


async def plume_fossil(ctx):
    """Look at the bottom 7 cards of your deck. You may reveal an Archen
    you find there and put it onto your Bench. Shuffle the other cards
    back into your deck."""
    bottom = ctx.deck()[:7]
    if not bottom:
        return
    matches = [
        c for c in bottom
        if c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Archen"
    ]
    picks = await ctx.choose_cards(
        matches, 1, minimum=0,
        prompt="Choose an Archen to put onto your Bench.",
        display_cards=bottom,
    )
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.bench_pokemon(picks[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="a059c8ec-e1c3-549a-9aec-dd171b482c80",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlumeFossil.Name",
    display_name="Plume Fossil",
    searchable_by=["Plume Fossil", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=plume_fossil,
)
