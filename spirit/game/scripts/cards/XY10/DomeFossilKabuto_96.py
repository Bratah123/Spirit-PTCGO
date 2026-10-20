from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import effective_bench_capacity


def dome_fossil_kabuto_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def dome_fossil_kabuto(ctx):
    """Look at the bottom 7 cards of your deck. You may reveal a Kabuto you find
    there and put it onto your Bench. Shuffle the other cards back into your deck."""
    bottom = ctx.deck()[:7]
    pool = [c for c in bottom if getattr(def_for(c.archetype_id), "display_name", "") == "Kabuto"]
    if pool and len(ctx.my_bench()) < effective_bench_capacity(ctx.board, ctx.player_id):
        pick = await ctx.choose_cards(pool, 1, minimum=0, prompt="You may put a Kabuto onto your Bench",
                                      display_cards=bottom)
        if pick:
            await ctx.reveal_cards(pick)
            await ctx.bench_pokemon(pick[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="8d39e07c-2ead-54f4-9f11-c6a2f6e6c6a9",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DomeFossilKabuto.Name",
    display_name="Dome Fossil Kabuto",
    searchable_by=["Dome Fossil Kabuto", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    condition=dome_fossil_kabuto_condition,
    effect=dome_fossil_kabuto
)
