from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import effective_bench_capacity


def armor_fossil_shieldon_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def armor_fossil_shieldon(ctx):
    """Look at the bottom 7 cards of your deck. You may reveal a Shieldon you find
    there and put it onto your Bench. Shuffle the other cards back into your deck."""
    bottom = ctx.deck()[:7]
    pool = [c for c in bottom if getattr(def_for(c.archetype_id), "display_name", "") == "Shieldon"]
    if pool and len(ctx.my_bench()) < effective_bench_capacity(ctx.board, ctx.player_id):
        pick = await ctx.choose_cards(pool, 1, minimum=0, prompt="You may put a Shieldon onto your Bench",
                                      display_cards=bottom)
        if pick:
            await ctx.reveal_cards(pick)
            await ctx.bench_pokemon(pick[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="59cde074-a448-5463-ab52-40a51cb0c9c3",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArmorFossilShieldon.Name",
    display_name="Armor Fossil Shieldon",
    searchable_by=["Armor Fossil Shieldon", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    condition=armor_fossil_shieldon_condition,
    effect=armor_fossil_shieldon
)
