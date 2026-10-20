from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def teammates_condition(board, player_id):
    """Only if 1 of your Pokemon was Knocked Out during your opponent's last turn."""
    ts = getattr(board, "turn_state", None)
    deck = board.find_player_area(player_id, "deck")
    return ts is not None and bool(ts.kos_by_attack_last_turn.get(player_id)) \
        and bool(deck and deck.children)


async def teammates(ctx):
    """Search your deck for up to 2 cards and put them into your hand. Shuffle."""
    picks = await ctx.search_deck(lambda c: True, count=2, minimum=0, prompt="Choose up to 2 cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="310ed132-2054-5afe-9fa4-dc2684a83865",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Teammates.Name",
    display_name="Teammates",
    searchable_by=["Teammates", "Supporter"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    effect=teammates,
    condition=teammates_condition
)
