from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import effective_bench_capacity


def claw_fossil_anorith_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def claw_fossil_anorith(ctx):
    """Look at the bottom 7 cards of your deck. You may reveal an Anorith you find
    there and put it onto your Bench. Shuffle the other cards back into your deck."""
    bottom = ctx.deck()[:7]
    pool = [c for c in bottom if getattr(def_for(c.archetype_id), "display_name", "") == "Anorith"]
    if pool and len(ctx.my_bench()) < effective_bench_capacity(ctx.board, ctx.player_id):
        pick = await ctx.choose_cards(pool, 1, minimum=0, prompt="You may put an Anorith onto your Bench",
                                      display_cards=bottom)
        if pick:
            await ctx.reveal_cards(pick)
            await ctx.bench_pokemon(pick[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="06959e7b-0e76-59f4-b155-9834bb527048",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClawFossilAnorith.Name",
    display_name="Claw Fossil Anorith",
    searchable_by=["Claw Fossil Anorith", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    condition=claw_fossil_anorith_condition,
    effect=claw_fossil_anorith
)
