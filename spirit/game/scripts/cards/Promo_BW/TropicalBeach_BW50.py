from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities


def _beach_condition(board, player_id, stadium=None):
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and hand is not None and len(hand.children) < 7


async def tropical_beach(ctx):
    """Draw cards until you have 7 cards in your hand. If you do, your turn ends."""
    drawn = await ctx.draw_until(7)
    if drawn:
        ctx.ends_turn = True


TROPICAL_BEACH_ABILITY = Ability(
    title="Tropical Beach",
    game_text="Once during each player's turn, that player may draw cards until he or she has 7 cards in his or her hand. If he or she does, that player's turn ends.",
    activation=Activations.ONCE_PER_TURN,
    condition=_beach_condition,
    effect=tropical_beach,
)


card = StadiumCardDef(
    guid="96cb9e70-2675-5489-b133-2f3f1d795aa9",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalBeach.Name",
    display_name="Tropical Beach",
    searchable_by=["Tropical Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=50,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    ability=TROPICAL_BEACH_ABILITY
)
