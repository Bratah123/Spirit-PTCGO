from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def _lillie_target(board):
    state = getattr(board, "turn_state", None)
    return 8 if state is not None and state.turn_number <= 2 else 6


def _lillie_condition(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    # The hand still holds Lillie herself while legality is checked.
    return bool(deck and deck.children) and \
        len(hand.children if hand else []) - 1 < _lillie_target(board)


async def _lillie(ctx):
    """Draw until 6 cards in hand (8 during your first turn)."""
    await ctx.draw_until(_lillie_target(ctx.board))


card = SupporterCardDef(
    guid="cad17f44-6aa0-500b-a25f-9b9879e04e9a",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=_lillie,
    condition=_lillie_condition
)
