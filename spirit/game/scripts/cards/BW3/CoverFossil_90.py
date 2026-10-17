from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities


async def cover_fossil(ctx):
    """Look at the bottom 7 cards of your deck. You may reveal a Tirtouga
    you find there and put it onto your Bench. Shuffle the other cards
    back into your deck."""
    bottom = ctx.deck()[:7]
    if not bottom:
        return
    matches = [
        c for c in bottom
        if c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Tirtouga"
    ]
    picks = await ctx.choose_cards(
        matches, 1, minimum=0,
        prompt="Choose a Tirtouga to put onto your Bench.",
        display_cards=bottom,
    )
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.bench_pokemon(picks[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="f2987372-7898-53bf-810b-e00e3fa45d59",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoverFossil.Name",
    display_name="Cover Fossil",
    searchable_by=["Cover Fossil", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=cover_fossil,
)
