"""LEGEND assembly and physical-card departure choreography."""

from spirit.game.attributes import AttrID, GameSequence
from spirit.game.content.definitions import Triggers, def_for
from spirit.game.content.legends import LegendHalf, matching_legend_halves
from spirit.game.models.board import LegendHalfEntity, LegendPokemonEntity
from spirit.game.models.card import Card
from spirit.game.session.passives import effective_bench_capacity
from spirit.network.message_names import OutboundMsg


def pair_is_playable(session, player_id, first, second):
    """Validate live ownership, matching halves, hand location, and Bench capacity."""
    board = session.board_state
    hand = board.find_player_area(player_id, "hand")
    bench = board.find_player_area(player_id, "bench")

    # Both cards must be physical LEGEND halves.
    if not isinstance(first, LegendHalfEntity) or not isinstance(second, LegendHalfEntity):
        return False

    # Reject stale copies that are no longer registered on this board.
    if board.get_entity(first.entity_id) is not first or board.get_entity(second.entity_id) is not second:
        return False

    # Both halves must currently be in the acting player's hand.
    if hand is None or first.parent is not hand or second.parent is not hand:
        return False

    # Neither half may belong to the opponent.
    if first.owning_player_id != player_id or second.owning_player_id != player_id:
        return False

    # The combined Pokemon needs one available Bench slot.
    if bench is None or len(bench.children) >= effective_bench_capacity(board, player_id):
        return False

    # Require opposite halves of the same resolved LEGEND definition.
    if not matching_legend_halves(first, second):
        return False

    # Play restrictions on either half prevent the paired play.
    if session.turn_state.play_locked(player_id, first) or session.turn_state.play_locked(player_id, second):
        return False

    return True


async def execute_play(session, player_id, card, entry, target_ids):
    """Resolve the offered hand play, choosing a printing when several match."""
    bench = session.board_state.find_player_area(player_id, "bench")
    if bench is None or session._validated_target(entry, target_ids) != bench.entity_id:
        return False
    hand = session.board_state.find_player_area(player_id, "hand")
    partners = [other for other in hand.children
                if pair_is_playable(session, player_id, card, other)] if hand else []
    if not partners:
        return False
    if len(partners) > 1:
        picked = await session.prompt_card_chooser(
            player_id, card.entity_id, partners, 1,
            prompt="Choose the other half of this LEGEND",
        )
        partners = [other for other in partners if other.entity_id in picked]
        if len(partners) != 1:
            return False
    legend = await assemble_legend(session, player_id, card, partners[0])
    if legend is None:
        return False
    return bool(await session._fire_triggered_abilities(player_id, legend, Triggers.ON_PLAY))


async def assemble_legend(session, player_id, first, second):
    """Play two compatible halves from hand as one benched Pokemon."""
    if not pair_is_playable(session, player_id, first, second):
        return None
    definition = def_for(first.archetype_id).legend_definition
    top, bottom = ((first, second) if def_for(first.archetype_id).half == LegendHalf.TOP
                   else (second, first))
    archetype = definition.to_archetype_dict()
    model = Card(definition.guid, definition.key, archetype["attributes"],
                 definition.display_name, definition.searchable_by, definition.subtypes)
    legend = LegendPokemonEntity(model, top, bottom, player_id)
    board = session.board_state
    bench = board.find_player_area(player_id, "bench")
    staging = board.find_global_area("outOfPlay")
    position = board.free_bench_slot(player_id)
    staging.add_child(legend)
    board._register_entity(legend)
    added = session._build_msg(OutboundMsg.ENTITY_ADDED.value, {
        "gameID": session.game_id, "entityID": legend.entity_id,
        "owningPlayerID": player_id, "parentEntityID": staging.entity_id,
    })
    for half in (top, bottom):
        board.attach_card(half.entity_id, legend.entity_id)
    board.move_card(legend.entity_id, bench.entity_id)
    session.turn_state.mark_entered_play(legend.entity_id)
    viewers = list(session.players.values())
    # ConfigureLegendary immediately dereferences both already-introduced halves.
    await session.send_game_sequence(viewers, GameSequence.SERIAL_SEQUENCE,
                                  [session._entity_introduced_msg(top), session._entity_introduced_msg(bottom)])
    await session.send_game_sequence(viewers, GameSequence.SERIAL_SEQUENCE,
                                  [added, session._entity_introduced_msg(legend)])
    # The renderer follows half IDs; ordinary child links duplicate the halves
    # in N.V's zoom list and break ZoomRenderRequester's two-position LEGEND step.
    client_staging = board.client_out_of_play_children()
    await session.send_game_sequence(viewers, GameSequence.CREATE_LEGEND, [
        session._entity_moved_msg(top.entity_id, staging.entity_id, client_staging.index(top),
                                  stamp_slot=False),
        session._entity_moved_msg(bottom.entity_id, staging.entity_id, client_staging.index(bottom),
                                  stamp_slot=False),
        session._entity_moved_msg(legend.entity_id, bench.entity_id, position),
    ])
    await session.fire_pokemon_benched_triggers(player_id, legend)
    return legend


def depart_legend(session, legend, destination, *, move_with=None, position=None):
    """Move physical cards out, then destroy the combined entity on both peers."""
    board = session.board_state
    if board.get_entity(legend.entity_id) is not legend:
        return [], []
    move_with = set(move_with or ())
    discard = board.find_player_area(legend.owning_player_id, "discard")
    staging = board.find_global_area("outOfPlay")
    members = []
    pending = list(legend.children)
    while pending:
        member = pending.pop(0)
        members.append(member)
        pending.extend(member.children)
    messages = session._clear_entity_visualizations_msg(legend)
    messages = [messages] if messages is not None else []
    session.clear_pokemon_effects(legend)
    session.reset_pokemon_damage(legend)
    session.reset_ability_usage(legend)
    # Knockout's constructor needs a move whose source is the combined Pokemon.
    messages.append(session._entity_moved_msg(legend.entity_id, staging.entity_id,
                                             len(board.client_out_of_play_children())))
    owner = legend.owning_player_id
    board.move_card(legend.entity_id, staging.entity_id)
    legend.owning_player_id = owner
    halves = (legend.top_half, legend.bottom_half)
    for member in members:
        area = destination if member in halves or member.entity_id in move_with else discard
        slot = position if area is destination and position is not None else len(area.children)
        if member in halves:
            legend.remove_child(member)
        board.move_card(member.entity_id, area.entity_id, position=slot)
        messages.extend(session._clear_departed_visualizations(member))
        messages.append(session._entity_moved_msg(member.entity_id, area.entity_id, slot))
    staging.remove_child(legend)
    board._unregister_entity(legend)
    session.turn_state.entered_play_turn.pop(legend.entity_id, None)
    messages.append(session._build_msg(OutboundMsg.ENTITY_DESTROYED.value, {
        "gameID": session.game_id, "entityID": legend.entity_id,
    }))
    return messages, members
