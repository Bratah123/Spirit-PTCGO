from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _is_pokemon_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
    )


async def tool_box(ctx):
    """Look at the top 7 cards of your deck. You may reveal any number of
    Pokémon Tool cards found there and put them into your hand. Shuffle the
    other cards back into your deck."""
    top = ctx.deck_top(7)
    if not top:
        return
    tools = [c for c in top if _is_pokemon_tool_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        tools, max(len(tools), 1), minimum=0,
        prompt="Choose any number of Pokémon Tool cards to put into your hand.",
        display_cards=top,
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="92ce36bc-12f1-5ba5-8541-46203ea28615",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolBox.Name",
    display_name="Tool Box",
    searchable_by=["Tool Box", "Item"],
    subtypes=["Item"],
    collector_number=168,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    effect=tool_box,
)
