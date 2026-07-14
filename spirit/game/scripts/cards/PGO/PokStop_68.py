from spirit.game.data_utils import Ability, Activations, StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty, is_item_card


async def pokestop_effect(ctx):
    """That player may discard the top 3 of their deck; any Item cards
    discarded this way go into their hand instead."""
    top = ctx.deck_top(3)
    if not top:
        return
    await ctx.discard_cards(top)
    items = [c for c in top if is_item_card(c)]
    if items:
        await ctx.put_in_hand(items, reveal=False)


POKESTOP_ABILITY = Ability(
    title="PokéStop",
    game_text="Once during each player's turn, that player may discard 3 cards from the top of their deck. If a player discarded any Item cards in this way, they put those Item cards into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=pokestop_effect,
    condition=lambda board, player_id, stadium: deck_nonempty(board, player_id),
)

card = StadiumCardDef(
    guid="57d9c8fc-1ed5-522a-b7de-93f1d280b715",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokStop.Name",
    display_name="PokÃ©Stop",
    searchable_by=["Pok\u00c3\u00a9Stop", "Stadium"],
    subtypes=["Stadium"],
    collector_number=68,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    ability=POKESTOP_ABILITY,
)
