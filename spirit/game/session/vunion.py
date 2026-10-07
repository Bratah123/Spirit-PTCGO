"""V-UNION summoning (CreateVUnion) and break-apart (VUnionBreakSequence) choreography."""

import logging
from typing import List, Optional

from spirit.game.attributes import AttrID, GameSequence
from spirit.game.content.vunion import VUnionPiece, VUnionPokemonDef, piece_definition
from spirit.game.models.board import VUnionPieceEntity, VUnionPokemonEntity
from spirit.game.models.card import Card
from spirit.game.session import legends
from spirit.game.session.passives import effective_bench_capacity
from spirit.game.session.sequence_packets import NestedSequence
from spirit.network.message_names import OutboundMsg

# VUnionBreakSequence (r.P) indexes its data effects by these keys (decoded client strings).
SUBCARD_KEYS = ("Subcard0", "Subcard1", "Subcard2", "Subcard3")
VUNION_KEY = "VUnion"


def _combined_of(piece) -> VUnionPokemonDef:
    definition = piece_definition(piece)
    assert definition is not None and definition.vunion_definition is not None
    return definition.vunion_definition


def _summon_key(player_id, definition):
    return player_id, definition.guid.lower()


def summon_pieces(board, turn_state, player_id, piece) -> Optional[List[VUnionPieceEntity]]:
    """The four discard pieces `piece` would combine with (itself included, slot-ordered), or None."""
    piece_def = piece_definition(piece)
    if piece_def is None or not isinstance(piece, VUnionPieceEntity) \
            or piece.owning_player_id != player_id:
        return None
    discard = board.find_player_area(player_id, "discard")
    bench = board.find_player_area(player_id, "bench")
    if discard is None or bench is None or piece.parent is not discard:
        return None
    combined = piece_def.vunion_definition
    if _summon_key(player_id, combined) in turn_state.vunions_assembled:
        return None
    if len(bench.children) >= effective_bench_capacity(board, player_id):
        return None
    chosen = {piece_def.piece: piece}
    for card in discard.children:
        card_def = piece_definition(card)
        if isinstance(card, VUnionPieceEntity) and card_def is not None \
                and card_def.vunion_definition is combined:
            chosen.setdefault(card_def.piece, card)
    if len(chosen) != len(VUnionPiece):
        return None
    return [chosen[slot] for slot in VUnionPiece]


def assemble_state(session, player_id, pieces):
    """Builds the combined Pokemon on the server board; returns (entity, CreateVUnion messages)."""
    board = session.board_state
    definition = _combined_of(pieces[0])
    archetype = definition.to_archetype_dict()
    model = Card(definition.guid, definition.key, archetype["attributes"],
                 definition.display_name, definition.searchable_by, definition.subtypes)
    vunion = VUnionPokemonEntity(model, pieces, player_id)
    # Client texture name = attr 10020 (S.y.CardImage) when set, else the padded collector number.
    vunion.set_attribute(AttrID.IMAGE_FALLBACK_1, definition.image_name)
    staging = board.find_global_area("outOfPlay")
    bench = board.find_player_area(player_id, "bench")
    staging.add_child(vunion)
    board._register_entity(vunion)
    # r.Q binds its combined entity from this EntityAdded before any piece flies.
    added = session._build_msg(OutboundMsg.ENTITY_ADDED.value, {
        "gameID": session.game_id, "entityID": vunion.entity_id,
        "owningPlayerID": player_id, "parentEntityID": staging.entity_id,
    })
    introduced = session._entity_introduced_msg(vunion)
    for piece in pieces:
        board.attach_card(piece.entity_id, vunion.entity_id)
    # Pieces stay server children but sit in outOfPlay client-side: N.V zooms every child.
    client_staging = board.client_out_of_play_children()
    joins = [session._entity_moved_msg(piece.entity_id, staging.entity_id,
                                       client_staging.index(piece), stamp_slot=False)
             for piece in pieces]
    position = board.free_bench_slot(player_id)
    board.move_card(vunion.entity_id, bench.entity_id)
    landing = session._entity_moved_msg(vunion.entity_id, bench.entity_id, position)
    # AttachToVUnion needs exactly 4 moves (r.Q's CardSlot1-4); nested PlayCard lands data-only.
    return vunion, [
        added,
        introduced,
        NestedSequence(GameSequence.ATTACH_TO_VUNION, joins),
        NestedSequence(GameSequence.PLAY_CARD, [landing]),
    ]


async def assemble_vunion(session, player_id, pieces) -> VUnionPokemonEntity:
    """Combines four validated discard pieces onto the Bench (no on-play triggers: not from hand)."""
    definition = _combined_of(pieces[0])
    vunion, messages = assemble_state(session, player_id, pieces)
    session.turn_state.vunions_assembled.add(_summon_key(player_id, definition))
    session.turn_state.mark_entered_play(vunion.entity_id)
    await session.send_game_sequence(
        list(session.players.values()), GameSequence.CREATE_VUNION, messages)
    return vunion


async def execute_play(session, player_id, piece) -> bool:
    """Resolves the discard-panel V-UNION action; never ends the turn."""
    pieces = summon_pieces(session.board_state, session.turn_state, player_id, piece)
    if pieces is None:
        viewer = session.players.get(player_id)
        if viewer is not None:
            await session.send_game_sequence([viewer], GameSequence.DISMISS_ABILITY_SELECT, [])
        return False
    vunion = await assemble_vunion(session, player_id, pieces)
    logging.info(
        f"[Session {session.game_id}] {session.players[player_id].screen_name} "
        f"combined V-UNION {vunion.entity_id}."
    )
    return False


def depart_vunion(session, vunion, destination, *, move_with=None, position=None,
                  knockout=False):
    """Returns (lead messages, [(VUnionBreakSequence, messages)], departed members).

    Lead messages ride the caller's bracket: attachments, plus for a knockout the
    combined card's own move so the Knockout executor has a Pokemon to fly.
    """
    board = session.board_state
    if board.get_entity(vunion.entity_id) is not vunion:
        return [], [], []
    move_with = set(move_with or ())
    owner = vunion.owning_player_id
    discard = board.find_player_area(owner, "discard")
    staging = board.find_global_area("outOfPlay")
    members = []
    pending = list(vunion.children)
    while pending:
        member = pending.pop(0)
        members.append(member)
        pending.extend(member.children)

    lead = []
    viz = session._clear_entity_visualizations_msg(vunion)
    if viz is not None:
        lead.append(viz)
    session.clear_pokemon_effects(vunion)
    session.reset_pokemon_damage(vunion)
    session.reset_ability_usage(vunion)
    if knockout:
        lead.append(session._entity_moved_msg(
            vunion.entity_id, destination.entity_id, len(destination.children),
            stamp_slot=False))
    for member in members:
        if member in vunion.pieces:
            continue
        area = destination if member.entity_id in move_with else discard
        slot = position if area is destination and position is not None else len(area.children)
        board.move_card(member.entity_id, area.entity_id, position=slot)
        lead.extend(session._clear_departed_visualizations(member))
        lead.append(session._entity_moved_msg(member.entity_id, area.entity_id, slot))

    # r.P resolves these keys at parse time; its piece moves apply data-only before the split.
    breakup = [session._entity_id_data_effect_msg(key, piece.entity_id)
               for key, piece in zip(SUBCARD_KEYS, vunion.pieces)]
    breakup.append(session._entity_id_data_effect_msg(VUNION_KEY, vunion.entity_id))
    for piece in vunion.pieces:
        slot = position if position is not None else len(destination.children)
        vunion.remove_child(piece)
        board.move_card(piece.entity_id, destination.entity_id, position=slot)
        breakup.append(session._entity_moved_msg(piece.entity_id, destination.entity_id, slot))

    board.move_card(vunion.entity_id, staging.entity_id)
    vunion.owning_player_id = owner
    staging.remove_child(vunion)
    board._unregister_entity(vunion)
    session.turn_state.entered_play_turn.pop(vunion.entity_id, None)
    breakup.append(session._build_msg(OutboundMsg.ENTITY_DESTROYED.value, {
        "gameID": session.game_id, "entityID": vunion.entity_id,
    }))
    return lead, [(GameSequence.VUNION_BREAK_SEQUENCE.value, breakup)], members


def depart_composite(session, pokemon, destination, *, move_with=None, position=None,
                     knockout=False):
    """LEGEND/V-UNION departure: (lead messages, trailing [(bracket, messages)] runs, members)."""
    if isinstance(pokemon, VUnionPokemonEntity):
        return depart_vunion(session, pokemon, destination, move_with=move_with,
                             position=position, knockout=knockout)
    messages, members = legends.depart_legend(session, pokemon, destination,
                                              move_with=move_with, position=position)
    return messages, [], members
