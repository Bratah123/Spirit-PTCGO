"""Prize-take choreography: the r.B fan-in flag and taken-slot gap tracking."""

import unittest
import uuid

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import PokemonCardDef
from spirit.game.models.board import create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.game_session import GameSession

P1 = "player-1"
P2 = "player-2"


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


POKEMON = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000f1",
    key="BW1", name="com.test.pokemon.Purrloin.Name",
    collector_number=5, set_code="BW1", rarity=1,
    hp=60, elements=[PokemonTypes.COLORLESS],
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


class PrizePickTestBase(unittest.IsolatedAsyncioTestCase):
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
        self.prize_area = self.board.find_player_area(P1, "prizePile")
        self.prizes = []
        for slot in range(6):
            entity = create_card_entity(POKEMON, owning_player_id=P1)
            self.board.add_card_to_area(entity, self.prize_area)
            entity.board_slot = slot
            self.prizes.append(entity)
        self.board.prizes_dealt[P1] = 6
        self.captured_offers = []
        self.pick_queue = []

        async def fake_prompt(player, msg_name, offer, expected_counter=None):
            self.captured_offers.append(offer)
            picked = self.pick_queue.pop(0)
            return {"selection": {"targetResponses": [{"entityList": picked}]}}

        self.session.prompt_selection_message = fake_prompt

    def bracket_msgs(self, client, name):
        """Inner messages of the last `name` sequence bracket sent to client."""
        runs, current = [], None
        for p in client.sent_packets:
            msg = p.get("msg") if isinstance(p, dict) else None
            if not isinstance(msg, dict):
                continue
            if msg["name"] == "StartSequence" and msg["value"]["name"] == name:
                current = []
            elif msg["name"] == "StopSequence" and msg["value"]["name"] == name:
                runs.append(current or [])
                current = None
            elif current is not None:
                current.append(msg)
        return runs[-1] if runs else None


class TestPrizePickOffer(PrizePickTestBase):
    async def test_offer_enables_the_fan_in_animation(self):
        self.pick_queue.append([self.prizes[0].entity_id])
        await self.session._take_prizes(P1, 1)

        offer = self.captured_offers[0]
        node = next(iter(offer["targetMap"].values()))[0]
        # r.B plays the pile->slots fly-in ONLY when this JSON flag is true;
        # omitted/false = the fan teleports into frame.
        self.assertTrue(node["presentPrizesAllowed"])
        self.assertEqual(node["name"], "PrizeCardTargetInformation")
        self.assertFalse(node["horizontalLayout"])


class TestPrizeGaps(PrizePickTestBase):
    async def test_taken_slots_are_marked_as_gaps(self):
        self.pick_queue.append([self.prizes[2].entity_id, self.prizes[4].entity_id])
        await self.session._take_prizes(P1, 2)

        self.assertEqual(
            self.prize_area.get_attribute(AttrID.AREA_EMPTY_SLOTS), [2, 4]
        )
        for client in (self.client1, self.client2):
            msgs = self.bracket_msgs(client, "WithOpenPrizeCards")
            self.assertIsNotNone(msgs)
            attr = next(m for m in msgs if m["name"] == "AttributeModified")
            self.assertEqual(attr["value"]["entityID"], self.prize_area.entity_id)
            self.assertEqual(attr["value"]["attribute"]["value"], [2, 4])
        # Prize faces reveal to the taker only.
        taker = self.bracket_msgs(self.client1, "WithOpenPrizeCards")
        opponent = self.bracket_msgs(self.client2, "WithOpenPrizeCards")
        self.assertEqual(
            sum(1 for m in taker if m["name"] == "EntityIntroduced"), 2)
        self.assertEqual(
            sum(1 for m in opponent if m["name"] == "EntityIntroduced"), 0)

    async def test_gaps_accumulate_across_takes(self):
        self.pick_queue.append([self.prizes[5].entity_id])
        await self.session._take_prizes(P1, 1)
        self.pick_queue.append([self.prizes[1].entity_id])
        await self.session._take_prizes(P1, 1)

        self.assertEqual(
            self.prize_area.get_attribute(AttrID.AREA_EMPTY_SLOTS), [1, 5]
        )


if __name__ == "__main__":
    unittest.main()
