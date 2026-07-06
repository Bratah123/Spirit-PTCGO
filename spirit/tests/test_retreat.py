"""Tests for the retreat executor (GameSession._execute_retreat)."""

import unittest
import uuid

from spirit.game.attributes import AttrID, GameSequence, PokemonTypes
from spirit.game.data_utils import EnergyCardDef, PokemonCardDef
from spirit.game.models.board import create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.game_session import GameSession
from spirit.game.session.legal_actions import ACTION_RETREAT, compute_legal_actions

P1 = "player-1"
P2 = "player-2"


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


ACTIVE_POKEMON = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000a1",
    key="BW1", name="com.test.pokemon.Snivy.Name",
    collector_number=1, set_code="BW1", rarity=1,
    hp=60, elements=[PokemonTypes.GRASS], retreat_cost=1,
))

BENCH_POKEMON = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000b1",
    key="BW1", name="com.test.pokemon.Patrat.Name",
    collector_number=2, set_code="BW1", rarity=1,
    hp=50, elements=[PokemonTypes.COLORLESS],
))

GRASS_ENERGY = make_card(EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000e1",
    key="BW1", name="com.test.energy.Grass.Name",
    collector_number=100, set_code="BW1", rarity=0,
    energy_type=PokemonTypes.GRASS,
))


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


class TestExecuteRetreat(unittest.IsolatedAsyncioTestCase):
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

        self.active = self.add_to("activePokemonArea", ACTIVE_POKEMON)
        self.benched = self.add_to("bench", BENCH_POKEMON)
        self.energy = self.add_to("discard", GRASS_ENERGY)
        self.board.attach_card(self.energy.entity_id, self.active.entity_id)
        self.session.turn_state.begin_turn(P1)

    def add_to(self, area_name, card, player_id=P1):
        entity = create_card_entity(card, owning_player_id=player_id)
        self.board.add_card_to_area(entity, self.board.find_player_area(player_id, area_name))
        return entity

    def retreat_entry(self):
        entries = compute_legal_actions(
            self.board, self.session.turn_state, P1, self.session.game_id
        )
        return next(
            e for e in entries
            if e["selectableAction"]["description"] == ACTION_RETREAT
        )

    def sequence_brackets(self, client, name):
        """Inner messages of each sequence bracket with the given name."""
        brackets = []
        current = None
        for packet in client.sent_packets:
            msg = packet.get("msg") if isinstance(packet, dict) else None
            if not isinstance(msg, dict):
                continue
            if msg.get("name") == "StartSequence" and msg["value"].get("name") == name:
                current = []
            elif msg.get("name") == "StopSequence" and current is not None:
                brackets.append(current)
                current = None
            elif current is not None:
                current.append(msg)
        return brackets

    async def test_retreat_swaps_active_discards_energy_and_broadcasts(self):
        entry = self.retreat_entry()
        await self.session._execute_retreat(
            P1, self.active, entry, [self.energy.entity_id, self.benched.entity_id]
        )

        active_area = self.board.find_player_area(P1, "activePokemonArea")
        bench_area = self.board.find_player_area(P1, "bench")
        discard_area = self.board.find_player_area(P1, "discard")
        self.assertEqual(active_area.children, [self.benched])
        self.assertEqual(bench_area.children, [self.active])
        self.assertIn(self.energy, discard_area.children)
        self.assertTrue(self.session.turn_state.retreated)

        for client in (self.client1, self.client2):
            brackets = self.sequence_brackets(client, GameSequence.RETREAT.value)
            self.assertEqual(len(brackets), 1)
            names = [m["name"] for m in brackets[0]]
            # N.P's ctor requires the Retreating/NewActive data effects.
            self.assertEqual(names[:2], ["EntityIDDataEffect", "EntityIDDataEffect"])
            self.assertEqual(brackets[0][0]["value"]["key"], "Retreating")
            self.assertEqual(brackets[0][0]["value"]["value"], self.active.entity_id)
            self.assertEqual(brackets[0][1]["value"]["key"], "NewActive")
            self.assertEqual(brackets[0][1]["value"]["value"], self.benched.entity_id)
            self.assertEqual(names[2:], ["EntityMoved", "EntityMoved", "EntityMoved"])

        # The retreat is spent for the rest of the turn.
        entries = compute_legal_actions(
            self.board, self.session.turn_state, P1, self.session.game_id
        )
        self.assertFalse(
            [e for e in entries if e["selectableAction"]["description"] == ACTION_RETREAT]
        )

    async def test_underpaid_retreat_is_rejected(self):
        entry = self.retreat_entry()
        # Reply omits the energy payment entirely.
        await self.session._execute_retreat(P1, self.active, entry, [self.benched.entity_id])

        active_area = self.board.find_player_area(P1, "activePokemonArea")
        self.assertEqual(active_area.children, [self.active])
        self.assertFalse(self.session.turn_state.retreated)
        self.assertFalse(self.sequence_brackets(self.client1, GameSequence.RETREAT.value))

    async def test_invalid_new_active_is_rejected(self):
        entry = self.retreat_entry()
        await self.session._execute_retreat(
            P1, self.active, entry, [self.energy.entity_id, self.active.entity_id]
        )

        active_area = self.board.find_player_area(P1, "activePokemonArea")
        self.assertEqual(active_area.children, [self.active])
        self.assertFalse(self.session.turn_state.retreated)

    async def test_old_active_takes_the_vacated_bench_slot(self):
        other_benched = self.add_to("bench", BENCH_POKEMON)
        entry = self.retreat_entry()
        await self.session._execute_retreat(
            P1, self.active, entry, [self.energy.entity_id, other_benched.entity_id]
        )

        bench_area = self.board.find_player_area(P1, "bench")
        active_area = self.board.find_player_area(P1, "activePokemonArea")
        self.assertEqual(active_area.children, [other_benched])
        self.assertEqual(bench_area.children, [self.benched, self.active])


if __name__ == "__main__":
    unittest.main()
