from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def camping_gear(ctx):
    """Search your deck for a card and put it into your hand, then shuffle.
    End the turn."""
    picks = await ctx.search_deck(
        count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()
    ctx.ends_turn = True


card = ItemCardDef(
    guid="d4ec25d9-0922-5db8-87f1-0fe99c66e430",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CampingGear.Name",
    display_name="Camping Gear",
    searchable_by=["Camping Gear", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    effect=camping_gear
)
