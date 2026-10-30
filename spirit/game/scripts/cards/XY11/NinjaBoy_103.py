from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon


def ninja_boy_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and any(is_basic_pokemon(p) for p in board.pokemon_in_play(player_id))


async def ninja_boy(ctx):
    """Choose 1 of your Basic Pokemon in play; search your deck for a Basic
    Pokemon and switch it with that Pokemon (everything stays on the new one);
    shuffle the first Pokemon into your deck."""
    mine = [p for p in ctx.my_pokemon_in_play() if is_basic_pokemon(p)]
    if not mine:
        return
    out = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Choose 1 of your Basic Pokémon")
    if out is None:
        return
    picks = await ctx.search_deck(is_basic_pokemon, 1, minimum=0, prompt="Choose a Basic Pokémon")
    if picks:
        await ctx.identity_swap(out, picks[0], destination="deck", transfer=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="c3d648fc-4092-59c9-89a1-ac8b7d792683",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NinjaBoy.Name",
    display_name="Ninja Boy",
    searchable_by=["Ninja Boy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    condition=ninja_boy_condition,
    effect=ninja_boy
)
