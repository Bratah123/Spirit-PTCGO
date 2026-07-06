import unittest
import os
from unittest.mock import MagicMock
from spirit.packets.handlers.system import SystemHandler
from spirit.network.message_names import InboundMsg

class MockClientHandler:
    def __init__(self):
        self.addr = ("127.0.0.1", 54321)
        self.sent_packets = []

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)

class TestSystemHandler(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.log_file = "client_errors.log"
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            try:
                os.remove(self.log_file)
            except OSError:
                pass

    async def test_log_client_error_writes_to_file(self):
        client = MockClientHandler()
        handler = SystemHandler(client)

        payload = {
            "name": "NullReferenceException",
            "reason": "Object reference not set to an instance of an object at Playmat.Start()",
            "logID": "test-log-123",
            "debugInfo": {
                "UnityVersion": "2019.4.28f1",
                "Scene": "Playmat"
            }
        }

        # Handle message
        await handler.handle_log_client_error(payload, request_id=45, flags=0)

        # Assert log file exists
        self.assertTrue(os.path.exists(self.log_file))

        # Check content
        with open(self.log_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("NullReferenceException", content)
        self.assertIn("Object reference not set to an instance of an object at Playmat.Start()", content)
        self.assertIn("test-log-123", content)
        self.assertIn("UnityVersion: 2019.4.28f1", content)
        self.assertIn("Scene: Playmat", content)

    async def test_benign_serialized_state_error_downranked_not_errorlevel(self):
        """The known-benign 'game is in progress' client error is logged at INFO (not ERROR)
        but is still persisted to client_errors.log."""
        client = MockClientHandler()
        handler = SystemHandler(client)

        payload = {
            "name": "ClientError",
            "reason": "InvalidOperationException: Serialized game state can't be loaded while a game is in progress!",
            "logID": "benign-log-1",
            "debugInfo": {"Scene": "Playmat"},
        }

        with self.assertLogs(level="INFO") as captured:
            await handler.handle_log_client_error(payload, request_id=1, flags=0)

        # Down-ranked: an INFO 'Benign client error' line, and NO ERROR-level record.
        joined = "\n".join(captured.output)
        self.assertIn("Benign client error", joined)
        self.assertFalse(
            any(rec.levelname == "ERROR" for rec in captured.records),
            "Benign client error should not be logged at ERROR level",
        )

        # Still recorded to file for the audit trail.
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("benign-log-1", content)
        self.assertIn("game is in progress", content)

    async def test_benign_render_texture_error_downranked_not_errorlevel(self):
        """The known-benign 'Releasing render texture' client warning (stock client bug in
        AvatarCamRenderTextureController teardown) is logged at INFO (not ERROR) but is
        still persisted to client_errors.log."""
        client = MockClientHandler()
        handler = SystemHandler(client)

        payload = {
            "name": "ClientError",
            "reason": "Releasing render texture that is set as Camera.targetTexture!\n",
            "logID": "benign-log-2",
            "debugInfo": {"AdditionalInfo": "Active Scene: VersusScreen"},
        }

        with self.assertLogs(level="INFO") as captured:
            await handler.handle_log_client_error(payload, request_id=2, flags=0)

        joined = "\n".join(captured.output)
        self.assertIn("Benign client error", joined)
        self.assertFalse(
            any(rec.levelname == "ERROR" for rec in captured.records),
            "Benign client error should not be logged at ERROR level",
        )

        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("benign-log-2", content)
        self.assertIn("Releasing render texture", content)
