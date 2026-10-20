from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


def _is_sail(card):
    return is_pokemon_card(card) and getattr(
        def_for(card.archetype_id), "display_name", None) == "Amaura"


def sail_fossil_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    bench = board.find_player_area(player_id, "bench")
    return bool(deck and deck.children) and bench is not None and \
        len(bench.children) < effective_bench_capacity(board, player_id)


async def sail_fossil(ctx):
    """Look at the bottom 7 cards of your deck; you may put a Amaura you find
    there onto your Bench. Shuffle the other cards back into your deck."""
    bottom = list(ctx.deck())[:7]
    if not bottom:
        return
    picks = await ctx.choose_cards([c for c in bottom if _is_sail(c)], 1, minimum=0,
                                   display_cards=bottom,
                                   prompt="You may choose a Amaura to put onto your Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="878bdf8b-e25d-5433-8d07-3715f4cdedf5",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SailFossil.Name",
    display_name="Sail Fossil",
    searchable_by=["Sail Fossil", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=sail_fossil,
    condition=sail_fossil_condition
)
