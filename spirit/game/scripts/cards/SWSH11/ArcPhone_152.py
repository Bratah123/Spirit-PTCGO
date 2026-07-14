from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import GameSequence, Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def _arc_phone(ctx):
    """Look at the top card of your deck; you may switch it with 1 of your
    face-down Prize cards (the cards stay face down)."""
    session = ctx.session
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(prize_area.children) if prize_area else []
    if not prizes:
        await ctx.present_card_choice(card, "Top card of your deck", ["OK"])
        return
    idx = await ctx.present_card_choice(
        card, "Switch this card with 1 of your face-down Prize cards?",
        ["Switch with a Prize card", "Put it back on top"],
    )
    if idx != 0:
        return
    picked_ids = await session._prompt_prize_pick(
        ctx.player_id, [c.entity_id for c in prizes], 1,
        prompt="Choose a face-down Prize card to switch.",
    )
    picked = ctx.board.get_entity(picked_ids[0]) if picked_ids else None
    if picked is None or picked.parent is not prize_area:
        return
    slot = getattr(picked, "board_slot", None)
    if slot is None:
        slot = prizes.index(picked)
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    both = list(session.players.values())
    # Prize -> top of deck rides WithOpenPrizeCards: after a pick, r.B defers
    # the fan teardown to this bracket; no intro = the card stays face down.
    pos = len(deck.children)
    if not ctx.board.move_card(picked.entity_id, deck.entity_id):
        return
    move = session._entity_moved_msg(picked.entity_id, deck.entity_id, pos)
    for viewer in both:
        await session.send_game_sequence(
            [viewer], GameSequence.WITH_OPEN_PRIZE_CARDS, [move])
    # The peeked deck card takes the vacated face-down Prize slot.
    if ctx.board.move_card(card.entity_id, prize_area.entity_id, slot):
        await session.send_game_sequence(
            both, GameSequence.GROUPED_MOVE,
            [session._entity_moved_msg(card.entity_id, prize_area.entity_id, slot)])
        # "The cards stay face down": re-hide the peeked face for the owner.
        await session.send_game_sequence(
            [session.players[ctx.player_id]], GameSequence.GROUPED_MOVE,
            [session._attributes_reset_msg(card.entity_id)])


card = ItemCardDef(
    guid="233044df-118b-5892-8421-f89a8780e5d8",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArcPhone.Name",
    display_name="Arc Phone",
    searchable_by=["Arc Phone", "Item"],
    subtypes=["Item"],
    collector_number=152,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=_arc_phone,
)
