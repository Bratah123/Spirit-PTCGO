from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import effective_bench_capacity


def helix_fossil_omanyte_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def helix_fossil_omanyte(ctx):
    """Look at the bottom 7 cards of your deck. You may reveal a Omanyte you find
    there and put it onto your Bench. Shuffle the other cards back into your deck."""
    bottom = ctx.deck()[:7]
    pool = [c for c in bottom if getattr(def_for(c.archetype_id), "display_name", "") == "Omanyte"]
    if pool and len(ctx.my_bench()) < effective_bench_capacity(ctx.board, ctx.player_id):
        pick = await ctx.choose_cards(pool, 1, minimum=0, prompt="You may put a Omanyte onto your Bench",
                                      display_cards=bottom)
        if pick:
            await ctx.reveal_cards(pick)
            await ctx.bench_pokemon(pick[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="40fa2b61-b005-5839-8432-f96e46f5ceeb",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HelixFossilOmanyte.Name",
    display_name="Helix Fossil Omanyte",
    searchable_by=["Helix Fossil Omanyte", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    condition=helix_fossil_omanyte_condition,
    effect=helix_fossil_omanyte
)
