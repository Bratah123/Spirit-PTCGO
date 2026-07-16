import unittest
from types import SimpleNamespace
from unittest.mock import patch

from spirit.game.attributes import AttrID, GameSequence
from spirit.game.models.board import (
    BoardEntity,
    BoardState,
    CardEntity,
    PokemonEntity,
)
from spirit.game.session.game_session import GameSession, NestedSequence
from spirit.network.message_names import OutboundMsg


class RecordingContext:
    def __init__(self):
        self.messages = []
        self.deferred_actions = []

    def _queue(self, msg, viewer_id=None, bracket=None):
        self.messages.append((viewer_id, msg, bracket))


def make_pokemon(entity_id, owner_id, hp=100):
    pokemon = object.__new__(PokemonEntity)
    BoardEntity.__init__(
        pokemon,
        entity_id=entity_id,
        owning_player_id=owner_id,
        archetype_id=f"archetype-{entity_id}",
    )
    pokemon.card_obj = SimpleNamespace()
    pokemon.set_attribute(AttrID.HP, hp)
    pokemon.attribute_originals[AttrID.HP.value] = hp
    return pokemon


def make_stack_card(entity_id, owner_id):
    card = object.__new__(CardEntity)
    BoardEntity.__init__(
        card,
        entity_id=entity_id,
        owning_player_id=owner_id,
        archetype_id=f"archetype-{entity_id}",
    )
    card.card_obj = SimpleNamespace()
    return card


class IdentitySwapChoreographyTests(unittest.IsolatedAsyncioTestCase):
    def make_session(self):
        session = object.__new__(GameSession)
        session.game_id = "game-1"
        session.board_state = BoardState(session.game_id, ["player-1", "player-2"])
        session.players = {
            "player-1": SimpleNamespace(screen_name="Player One"),
            "player-2": SimpleNamespace(screen_name="Player Two"),
        }
        session._opponent_id = lambda player_id: (
            "player-2" if player_id == "player-1" else "player-1"
        )
        session.turn_state = SimpleNamespace(
            mark_entered_play=lambda entity_id: None,
        )
        session.clear_pokemon_effects = lambda pokemon: False
        session.reset_pokemon_damage = lambda pokemon: None
        session.reset_ability_usage = lambda pokemon: None
        session.transfer_pokemon_state = lambda outgoing, incoming: []

        async def refresh_granted_abilities(pokemon):
            return None

        session.refresh_granted_abilities = refresh_granted_abilities
        return session

    def place_cards(self, session):
        board = session.board_state
        active = board.find_player_area("player-1", "activePokemonArea")
        discard = board.find_player_area("player-1", "discard")
        outgoing = make_pokemon("outgoing", "player-1", hp=70)
        incoming = make_pokemon("incoming", "player-1", hp=120)
        attachment = make_stack_card("attachment", "player-1")
        board.add_card_to_area(outgoing, active)
        board.add_card_to_area(incoming, discard)
        outgoing.add_child(attachment)
        board._register_entity(attachment)
        return outgoing, incoming, attachment, active, discard

    async def test_swap_parks_every_card_then_finishes_from_out_of_play(self):
        for transfer in (True, False):
            with self.subTest(transfer=transfer):
                session = self.make_session()
                outgoing, incoming, attachment, active, discard = self.place_cards(session)
                ctx = RecordingContext()

                with patch(
                    "spirit.game.session.game_session.effective_max_hp",
                    side_effect=lambda board, pokemon: pokemon.attribute_originals[
                        AttrID.HP.value
                    ],
                ):
                    result = await session.perform_identity_swap(
                        outgoing,
                        incoming,
                        destination_name="discard",
                        transfer=transfer,
                        ctx=ctx,
                    )

                self.assertIs(result, incoming)
                transform_messages = [
                    msg for _, msg, bracket in ctx.messages
                    if bracket == GameSequence.TRANSFORM_SWAP.value
                ]
                parking = next(
                    msg for msg in transform_messages
                    if isinstance(msg, NestedSequence)
                )
                self.assertEqual(parking.name, GameSequence.ROBO_SUBSTITUTE.value)
                self.assertEqual(
                    [msg["value"]["entityID"] for msg in parking.messages],
                    [incoming.entity_id, attachment.entity_id, outgoing.entity_id],
                )
                out_of_play = session.board_state.find_global_area("outOfPlay")
                self.assertTrue(all(
                    msg["name"] == OutboundMsg.ENTITY_MOVED.value
                    and msg["value"]["destinationID"] == out_of_play.entity_id
                    for msg in parking.messages
                ))

                final_moves = [
                    msg for _, msg, bracket in ctx.messages
                    if bracket == GameSequence.ROBO_SUBSTITUTE.value
                ]
                self.assertEqual(
                    [msg["value"]["entityID"] for msg in final_moves],
                    [attachment.entity_id, outgoing.entity_id, incoming.entity_id],
                )
                expected_attachment_destination = (
                    incoming.entity_id if transfer else discard.entity_id
                )
                self.assertEqual(
                    [msg["value"]["destinationID"] for msg in final_moves],
                    [
                        expected_attachment_destination,
                        discard.entity_id,
                        active.entity_id,
                    ],
                )

                # The visual-only parking moves must not replace the final
                # board stamp with an outOfPlay position.
                self.assertEqual(incoming.board_slot, 0)
                self.assertIs(incoming.parent, active)
                self.assertIs(outgoing.parent, discard)
                self.assertIs(
                    attachment.parent,
                    incoming if transfer else discard,
                )


if __name__ == "__main__":
    unittest.main()
