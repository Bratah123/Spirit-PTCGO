import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from spirit.packets.handlers.auth import AuthHandler
from spirit.network.message_names import OutboundMsg


class MockServer:
    def __init__(self):
        self.clients = []


class MockClientHandler:
    def __init__(self, addr=("127.0.0.1", 54321), server=None):
        self.addr = addr
        self.server = server or MockServer()
        self.sent_packets = []
        self.session_id = "test-session-id"
        self.player = None

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)


class TestAuthConcurrentLogin(unittest.IsolatedAsyncioTestCase):
    @patch("spirit.packets.handlers.auth.process_daily_login")
    @patch("spirit.packets.handlers.auth.Player")
    @patch("spirit.packets.handlers.auth.SocialHandler")
    async def test_auth_success_when_no_concurrent_sessions(self, mock_social_handler_class, mock_player_class, mock_process_daily_login):
        mock_process_daily_login.return_value = {
            "firstDailyLogin": True,
            "activations": 1,
            "rewardDay": 1,
            "nextRewardTimestampMs": 4102444800000,
            "granted": []
        }
        # Mocking SocialHandler instance and its broadcast_presence method
        mock_social_instance = MagicMock()
        mock_social_instance.broadcast_presence = AsyncMock()
        mock_social_handler_class.return_value = mock_social_instance

        # Mock player
        mock_player_instance = MagicMock()
        mock_player_class.return_value = mock_player_instance

        server = MockServer()
        client = MockClientHandler(addr=("127.0.0.1", 1111), server=server)
        server.clients.append(client)

        handler = AuthHandler(client)
        
        account_data = {
            "account_id": "user123",
            "username": "testuser",
            "screen_name": "TestUser"
        }

        await handler._send_auth_success(request_id=123, account_data=account_data)

        # Assert player is set
        self.assertIsNotNone(client.player)
        mock_player_class.assert_called_once_with(account_data)

        # Assert success packet was sent (at least the AUTH_SUCCESS packet)
        sent_messages = [p["messageName"] for p in client.sent_packets]
        self.assertIn(OutboundMsg.AUTH_SUCCESS.value, sent_messages)

    @patch("spirit.packets.handlers.auth.Player")
    @patch("spirit.packets.handlers.auth.SocialHandler")
    async def test_auth_failed_when_concurrent_session_exists(self, mock_social_handler_class, mock_player_class):
        # Setup Server and two clients
        server = MockServer()
        
        # Existing client (already logged in)
        existing_client = MockClientHandler(addr=("127.0.0.1", 2222), server=server)
        existing_player = MagicMock()
        existing_player.account_id = "user123"
        existing_client.player = existing_player
        server.clients.append(existing_client)

        # New client trying to log in
        new_client = MockClientHandler(addr=("127.0.0.1", 3333), server=server)
        server.clients.append(new_client)

        handler = AuthHandler(new_client)
        
        account_data = {
            "account_id": "user123",
            "username": "testuser",
            "screen_name": "TestUser"
        }

        await handler._send_auth_success(request_id=456, account_data=account_data)

        # Assert new player is NOT set (login blocked)
        self.assertIsNone(new_client.player)

        # Assert AUTH_FAILED packet is sent with the expected message
        self.assertEqual(len(new_client.sent_packets), 1)
        response = new_client.sent_packets[0]
        self.assertEqual(response["messageName"], OutboundMsg.AUTH_FAILED.value)
        self.assertEqual(response["reason"]["token"], "The account you are trying to login is already online.")
        
        # Ensure player and social methods were NOT called for the new client
        mock_player_class.assert_not_called()
        mock_social_handler_class.assert_not_called()


if __name__ == "__main__":
    unittest.main()
