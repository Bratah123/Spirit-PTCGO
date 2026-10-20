from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def max_revive_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_pokemon_card(c) for c in discard.children)


async def max_revive(ctx):
    """Put a Pokemon from your discard pile on top of your deck."""
    cards = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Pokémon to put on top of your deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = ItemCardDef(
    guid="bdfab0b2-e405-5f82-9a79-2dcf3987e2ed",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=max_revive,
    condition=max_revive_condition
)
