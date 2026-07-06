"""Bench slot bookkeeping: the client stamps every card with the
positionInParent of its last EntityMoved and never renumbers the bench,
so vacated slots (KO promotion, retreat) must be refilled explicitly."""

import unittest
import uuid

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import EnergyCardDef, PokemonCardDef
from spirit.game.models.board import create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.effects import EffectContext

from spirit.game.session.game_session import GameSession

P1 = "player-1"
P2 = "player-2"


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


POKEMON = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000c1",
    key="BW1", name="com.test.pokemon.Lillipup.Name",
    collector_number=3, set_code="BW1", rarity=1,
    hp=60, elements=[PokemonTypes.COLORLESS], retreat_cost=1,
))

ENERGY = make_card(EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000e2",
    key="BW1", name="com.test.energy.Colorless.Name",
    collector_number=101, set_code="BW1", rarity=0,
    energy_type=PokemonTypes.COLORLESS,
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


class BenchSlotTestBase(unittest.IsolatedAsyncioTestCase):
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
        self.session.turn_state.begin_turn(P1)

    def add_to(self, area_name, card=POKEMON, player_id=P1, slot=None):
        entity = create_card_entity(card, owning_player_id=player_id)
        self.board.add_card_to_area(entity, self.board.find_player_area(player_id, area_name))
        if slot is not None:
            entity.board_slot = slot
        return entity

    def moved_msgs(self, client):
        return [
            p["msg"] for p in client.sent_packets
            if isinstance(p, dict) and isinstance(p.get("msg"), dict)
            and p["msg"].get("name") == "EntityMoved"
        ]


class TestFreeBenchSlot(BenchSlotTestBase):
    def test_fills_the_lowest_vacated_slot(self):
        # Lugia (slot 0) was promoted away; Lumineon keeps its slot-1 stamp.
        self.add_to("bench", slot=1)
        self.assertEqual(self.board.free_bench_slot(P1), 0)

    def test_appends_after_the_highest_occupied_slot(self):
        self.add_to("bench", slot=0)
        self.add_to("bench", slot=1)
        self.assertEqual(self.board.free_bench_slot(P1), 2)

    def test_unstamped_children_fall_back_to_list_length(self):
        self.add_to("bench")
        self.assertEqual(self.board.free_bench_slot(P1), 1)


class TestBenchEntryFillsGaps(BenchSlotTestBase):
    async def test_play_basic_takes_the_vacated_slot(self):
        self.add_to("bench", slot=1)
        card = self.add_to("hand")
        await self.session._execute_play_basic(P1, card)

        move = self.moved_msgs(self.client1)[-1]
        self.assertEqual(move["value"]["positionInParent"], 0)
        self.assertEqual(card.board_slot, 0)

    async def test_effect_bench_fills_gap_then_appends(self):
        # The Summoning Star scenario: bench = Lumineon stamped slot 1.
        lumineon = self.add_to("bench", slot=1)
        archeops1 = self.add_to("discard")
        archeops2 = self.add_to("discard")
        ctx = EffectContext(self.session, P1, lumineon, None)

        self.assertTrue(await ctx.bench_pokemon(archeops1))
        self.assertTrue(await ctx.bench_pokemon(archeops2))

        self.assertEqual(archeops1.board_slot, 0)
        self.assertEqual(archeops2.board_slot, 2)
        positions = [
            msg["value"]["positionInParent"]
            for _, msg, _ in ctx._messages if msg.get("name") == "EntityMoved"
        ]
        self.assertEqual(positions, [0, 2])


class TestSwapsUseStampedSlot(BenchSlotTestBase):
    async def test_retreat_old_active_takes_the_stamped_slot(self):
        active = self.add_to("activePokemonArea")
        energy = self.add_to("discard", ENERGY)
        self.board.attach_card(energy.entity_id, active.entity_id)
        # Lone benched Pokemon rendered at slot 2 (earlier neighbors left).
        benched = self.add_to("bench", slot=2)

        from spirit.game.session.legal_actions import ACTION_RETREAT, compute_legal_actions
        entries = compute_legal_actions(
            self.board, self.session.turn_state, P1, self.session.game_id
        )
        entry = next(
            e for e in entries
            if e["selectableAction"]["description"] == ACTION_RETREAT
        )
        await self.session._execute_retreat(
            P1, active, entry, [energy.entity_id, benched.entity_id]
        )

        self.assertEqual(active.board_slot, 2)
        moves = self.moved_msgs(self.client1)
        to_bench = next(
            m for m in moves if m["value"]["entityID"] == active.entity_id
        )
        self.assertEqual(to_bench["value"]["positionInParent"], 2)

    async def test_switch_active_old_active_takes_the_stamped_slot(self):
        active = self.add_to("activePokemonArea")
        benched = self.add_to("bench", slot=3)
        ctx = EffectContext(self.session, P1, active, None)

        self.assertTrue(await ctx.switch_active(P1, benched))

        self.assertEqual(active.board_slot, 3)
        self.assertEqual(benched.board_slot, 0)


class TestSerializedGapAttributes(BenchSlotTestBase):
    def test_sgs_lists_empty_slots_and_sorts_children(self):
        later = self.add_to("bench", slot=3)
        earlier = self.add_to("bench", slot=1)

        self.board.serialize(P1)

        bench = self.board.find_player_area(P1, "bench")
        self.assertEqual(bench.children, [earlier, later])
        self.assertEqual(
            bench.get_attribute(AttrID.AREA_EMPTY_SLOTS), [0, 2, 4]
        )


if __name__ == "__main__":
    unittest.main()
