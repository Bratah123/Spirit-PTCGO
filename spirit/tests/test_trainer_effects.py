"""Tests for scripted trainer effects (resolve_trainer_effect + Worker)."""

import importlib.util
import os
import unittest
import uuid

from spirit.game.attributes import GameSequence, PokemonTypes
from spirit.game.data_utils import (
    TRAINER_EFFECTS_BY_GUID,
    PokemonCardDef,
    StadiumCardDef,
    SupporterCardDef,
)
from spirit.game.models.board import create_card_entity
from spirit.game.models.card import Card

from spirit.game.session.game_session import GameSession

P1 = "player-1"
P2 = "player-2"

WORKER_SCRIPT = os.path.join(
    os.path.dirname(__file__), "..", "game", "scripts", "cards", "SWSH12", "Worker_167.py"
)


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


def load_worker_def():
    spec = importlib.util.spec_from_file_location("test_worker_script", WORKER_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.card


DECK_FILLER = PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000f1",
    key="BW1", name="com.test.pokemon.Filler.Name",
    collector_number=1, set_code="BW1", rarity=1,
    hp=50, elements=[PokemonTypes.COLORLESS],
)

TEST_STADIUM = StadiumCardDef(
    guid="00000000-0000-0000-0000-0000000000d1",
    key="BW1", name="com.test.trainer.Stadium.Name",
    collector_number=90, set_code="BW1", rarity=1,
)

PLAIN_SUPPORTER = SupporterCardDef(
    guid="00000000-0000-0000-0000-0000000000c1",
    key="BW1", name="com.test.trainer.Plain.Name",
    collector_number=91, set_code="BW1", rarity=1,
)


class MockClientHandler:
    def __init__(self, account_id, username):
        self.player = type("P", (), {
            "account_id": account_id, "username": username,
            "screen_name": username, "avatar_decks": [],
        })()
        self.addr = ("127.0.0.1", 12345)
        self.sent_packets = []

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)


class TestTrainerEffectRegistry(unittest.TestCase):
    def test_effect_registers_by_lowercase_guid(self):
        async def noop(ctx):
            pass

        SupporterCardDef(
            guid="AAAAAAAA-0000-0000-0000-0000000000AA",
            key="BW1", name="com.test.trainer.Reg.Name",
            collector_number=92, set_code="BW1", rarity=1,
            effect=noop,
        )
        self.assertIs(
            TRAINER_EFFECTS_BY_GUID["aaaaaaaa-0000-0000-0000-0000000000aa"], noop
        )

    def test_worker_script_registers_its_effect(self):
        card_def = load_worker_def()
        self.assertIn(card_def.guid.lower(), TRAINER_EFFECTS_BY_GUID)


class TestExecutePlayTrainer(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client1 = MockClientHandler(P1, "Ash")
        self.client2 = MockClientHandler(P2, "Gary")
        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                P1: {"client": self.client1, "deck": {"deckID": "d1", "deckName": "A", "cards": []}, "ready": True},
                P2: {"client": self.client2, "deck": {"deckID": "d2", "deckName": "B", "cards": []}, "ready": True},
            },
        }
        self.session = GameSession(str(uuid.uuid4()), pairing)
        self.board = self.session.board_state

        self.worker_card = make_card(load_worker_def())
        self.worker = self.add_to("hand", self.worker_card)
        filler = make_card(DECK_FILLER)
        self.deck_cards = [self.add_to("deck", filler) for _ in range(5)]
        self.session.turn_state.begin_turn(P1)
        self.session.turn_state.begin_turn(P1)  # turn 2: supporters legal

    def add_to(self, area_name, card, player_id=P1):
        entity = create_card_entity(card, owning_player_id=player_id)
        self.board.add_card_to_area(entity, self.board.find_player_area(player_id, area_name))
        return entity

    def add_stadium_in_play(self, player_id=P2):
        entity = create_card_entity(make_card(TEST_STADIUM), owning_player_id=player_id)
        self.board.add_card_to_area(entity, self.board.find_global_area("activeStadium"))
        entity.owning_player_id = player_id  # global area add clears the owner
        return entity

    def sequence_brackets(self, client, name):
        """Inner messages of each sequence bracket with the given name.

        Nested child brackets are folded in: their Start/Stop markers are
        skipped and their inner messages count as the parent's."""
        brackets = []
        current = None
        depth = 0
        for packet in client.sent_packets:
            msg = packet.get("msg") if isinstance(packet, dict) else None
            if not isinstance(msg, dict):
                continue
            if msg.get("name") == "StartSequence":
                if current is not None:
                    depth += 1
                elif msg["value"].get("name") == name:
                    current = []
                    depth = 0
            elif msg.get("name") == "StopSequence":
                if current is not None:
                    if depth == 0:
                        brackets.append(current)
                        current = None
                    else:
                        depth -= 1
            elif current is not None:
                current.append(msg)
        return brackets

    def bracket_order(self, client):
        """Sequence bracket names in send order."""
        return [
            packet["msg"]["value"].get("name")
            for packet in client.sent_packets
            if isinstance(packet, dict) and isinstance(packet.get("msg"), dict)
            and packet["msg"].get("name") == "StartSequence"
        ]

    async def test_worker_draws_three_and_discards_the_stadium(self):
        stadium = self.add_stadium_in_play(player_id=P2)
        await self.session._execute_play_trainer(P1, self.worker)

        hand = self.board.find_player_area(P1, "hand")
        deck = self.board.find_player_area(P1, "deck")
        self.assertEqual(len(hand.children), 3)
        self.assertEqual(len(deck.children), 2)
        self.assertIn(self.worker, self.board.find_player_area(P1, "discard").children)
        self.assertIn(stadium, self.board.find_player_area(P2, "discard").children)
        self.assertTrue(self.session.turn_state.supporter_played)

        trainer_area = self.board.find_global_area("activeTrainer")
        discard_area = self.board.find_player_area(P1, "discard")

        # Owner: placement and discard ride separate TrainerCard brackets so
        # the card sits in the slot while the effect resolves between them.
        brackets = self.sequence_brackets(self.client1, GameSequence.TRAINER_CARD.value)
        self.assertEqual(len(brackets), 2)
        self.assertEqual([m["name"] for m in brackets[0]], ["EntityMoved"])
        self.assertEqual(brackets[0][0]["value"]["destinationID"], trainer_area.entity_id)
        self.assertEqual([m["name"] for m in brackets[1]], ["EntityMoved"])
        self.assertEqual(brackets[1][0]["value"]["destinationID"], discard_area.entity_id)
        self.assertEqual(brackets[1][0]["value"]["entityID"], self.worker.entity_id)

        # Non-owner placement is a PlayCard bracket (plain move: k.z delegation
        # presents the card large, then flies it into the slot); discard is a
        # plain TrainerCard bracket afterwards.
        opp_play = self.sequence_brackets(self.client2, GameSequence.PLAY_CARD.value)
        self.assertEqual(
            [m["name"] for m in opp_play[0]], ["RevealCardToAllEffect", "EntityMoved"]
        )
        self.assertEqual(opp_play[0][1]["value"]["destinationID"], trainer_area.entity_id)
        opp_trainer = self.sequence_brackets(self.client2, GameSequence.TRAINER_CARD.value)
        self.assertEqual(len(opp_trainer), 1)
        self.assertEqual(opp_trainer[0][0]["value"]["destinationID"], discard_area.entity_id)

        # Effect resolves between placement and discard: draws ride their own
        # Draw bracket (moves in a nested GroupedMove child), the stadium
        # move a plain GroupedMove.
        self.assertEqual(
            self.bracket_order(self.client1)[-5:],
            [GameSequence.TRAINER_CARD.value, GameSequence.DRAW.value,
             GameSequence.GROUPED_MOVE.value, GameSequence.GROUPED_MOVE.value,
             GameSequence.TRAINER_CARD.value],
        )
        self.assertEqual(
            self.bracket_order(self.client2)[-6:],
            [GameSequence.SERIAL_SEQUENCE.value, GameSequence.PLAY_CARD.value,
             GameSequence.DRAW.value, GameSequence.GROUPED_MOVE.value,
             GameSequence.GROUPED_MOVE.value, GameSequence.TRAINER_CARD.value],
        )

        # The Draw bracket matches _broadcast_draw's shape exactly: intros
        # first (drawer only), then the moves.
        draw = self.sequence_brackets(self.client1, GameSequence.DRAW.value)
        self.assertEqual(len(draw), 1)
        names = [m["name"] for m in draw[0]]
        self.assertEqual(names, ["EntityIntroduced"] * 3 + ["EntityMoved"] * 3)

        opp_draw = self.sequence_brackets(self.client2, GameSequence.DRAW.value)
        opp_names = [m["name"] for m in opp_draw[0]]
        self.assertEqual(opp_names, ["EntityMoved"] * 3)

        grouped = self.sequence_brackets(self.client1, GameSequence.GROUPED_MOVE.value)
        self.assertEqual(grouped[-1][-1]["value"]["entityID"], stadium.entity_id)

    async def test_worker_without_a_stadium_just_draws(self):
        await self.session._execute_play_trainer(P1, self.worker)

        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 3)
        self.assertIn(self.worker, self.board.find_player_area(P1, "discard").children)

    async def test_unscripted_trainer_still_plays_to_discard(self):
        plain = self.add_to("hand", make_card(PLAIN_SUPPORTER))
        await self.session._execute_play_trainer(P1, plain)

        self.assertIn(plain, self.board.find_player_area(P1, "discard").children)
        self.assertTrue(self.session.turn_state.supporter_played)
        brackets = self.sequence_brackets(self.client1, GameSequence.TRAINER_CARD.value)
        self.assertEqual(len(brackets), 2)
        self.assertEqual([m["name"] for m in brackets[0]], ["EntityMoved"])
        self.assertEqual([m["name"] for m in brackets[1]], ["EntityMoved"])
        self.assertFalse(self.sequence_brackets(self.client1, GameSequence.DRAW.value))


if __name__ == "__main__":
    unittest.main()
