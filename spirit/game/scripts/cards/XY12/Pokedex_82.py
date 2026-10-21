from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def pokedex_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def pokedex(ctx):
    """Look at the top 5 cards of your deck and put them back in any order."""
    await ctx.reorder_deck_top(5)


card = ItemCardDef(
    guid="6dea3f2c-dac3-5b88-ab90-b6d0ad542c16",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokedex.Name",
    display_name="Pok\u00e9dex",
    searchable_by=["Pokédex", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    condition=pokedex_condition,
    effect=pokedex
)
