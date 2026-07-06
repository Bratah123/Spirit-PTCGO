import unittest

from spirit.network.message_names import OutboundMsg
from spirit.packets.handlers.social import SocialHandler, LOBBY_ROOMS


class MockPlayer:
    def __init__(self, account_id, screen_name):
        self.account_id = account_id
        self.screen_name = screen_name


class MockServer:
    def __init__(self):
        self.clients = []


class MockClientHandler:
    def __init__(self, server, account_id, screen_name):
        self.server = server
        self.player = MockPlayer(account_id, screen_name)
        self.addr = ("127.0.0.1", 12345)
        self.sent_packets = []
        server.clients.append(self)

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)

    def msgs(self, name):
        return [p for p in self.sent_packets if p.get("messageName") == name]


class TestLobbyChatRooms(unittest.IsolatedAsyncioTestCase):
    """Lobby room wire protocol (decoded from s.f/s.w/T.B/T.C).

    A joined Lobby room must exist so the client's exit-game-chat command
    (T.W) has a JoinedRooms[0] to switch back to; without one it re-selects
    the game room, deletes its RoomMessages entry, and every later
    ChatGenerator.generate() KeyNotFoundExceptions on the dangling
    CurrentSelectedRoom.
    """

    def setUp(self):
        self.server = MockServer()
        self.alice = MockClientHandler(self.server, "acc-alice", "Alice")
        self.bob = MockClientHandler(self.server, "acc-bob", "Bob")

    async def test_public_rooms_lists_lobby_type_zero(self):
        handler = SocialHandler(self.alice)
        await handler.handle_public_rooms({}, request_id=1, flags=0)
        response = self.alice.msgs(OutboundMsg.AVAILABLE_ROOMS.value)[0]
        self.assertTrue(response["rooms"])
        # s.w only auto-joins rooms with roomType == RoomType.Lobby (0).
        self.assertTrue(all(r["roomType"] == 0 for r in response["rooms"]))

    async def test_join_room_replies_chat_connected_and_notifies(self):
        room_id = LOBBY_ROOMS[0]["roomID"]
        await SocialHandler(self.alice).handle_join_room(
            {"roomID": room_id}, request_id=1, flags=0)
        await SocialHandler(self.bob).handle_join_room(
            {"roomID": room_id}, request_id=2, flags=0)

        connected = self.bob.msgs(OutboundMsg.CHAT_CONNECTED.value)[0]
        self.assertEqual(connected["room"]["roomID"], room_id)
        self.assertEqual(connected["room"]["roomType"], 0)
        member_ids = [m["accountID"] for m in connected["members"]]
        self.assertIn("acc-alice", member_ids)
        self.assertEqual(connected["messageHistory"], [])

        joined = self.alice.msgs(OutboundMsg.NOTIFY_JOIN.value)[0]
        self.assertEqual(joined["roomID"], room_id)
        self.assertEqual(joined["userInfo"]["accountID"], "acc-bob")

    async def test_unknown_room_join_is_ignored(self):
        await SocialHandler(self.alice).handle_join_room(
            {"roomID": "not-a-room"}, request_id=1, flags=0)
        self.assertEqual(self.alice.sent_packets, [])

    async def test_room_chat_broadcasts_to_all_members_including_sender(self):
        room_id = LOBBY_ROOMS[0]["roomID"]
        for client in (self.alice, self.bob):
            await SocialHandler(client).handle_join_room(
                {"roomID": room_id}, request_id=1, flags=0)
        await SocialHandler(self.alice).handle_room_chat(
            {"roomID": room_id, "message": "hello lobby"}, request_id=3, flags=0)

        # The sender has no local echo: their own line renders from NotifyChat.
        for client in (self.alice, self.bob):
            notify = client.msgs(OutboundMsg.NOTIFY_CHAT.value)[0]
            self.assertEqual(notify["roomID"], room_id)
            self.assertEqual(notify["message"], "hello lobby")
            self.assertEqual(notify["userInfo"]["displayName"], "Alice")

    async def test_leave_room_replies_disconnected_and_notifies(self):
        room_id = LOBBY_ROOMS[0]["roomID"]
        for client in (self.alice, self.bob):
            await SocialHandler(client).handle_join_room(
                {"roomID": room_id}, request_id=1, flags=0)
        await SocialHandler(self.bob).handle_leave_room(
            {"roomID": room_id}, request_id=4, flags=0)

        disconnected = self.bob.msgs(OutboundMsg.CHAT_DISCONNECTED.value)[0]
        self.assertEqual(disconnected["roomID"], room_id)
        left = self.alice.msgs(OutboundMsg.NOTIFY_LEAVE.value)[0]
        self.assertEqual(left["accountID"], "acc-bob")

        # A member who left no longer receives room chat.
        await SocialHandler(self.alice).handle_room_chat(
            {"roomID": room_id, "message": "still here?"}, request_id=5, flags=0)
        self.assertEqual(len(self.bob.msgs(OutboundMsg.NOTIFY_CHAT.value)), 0)


if __name__ == "__main__":
    unittest.main()
