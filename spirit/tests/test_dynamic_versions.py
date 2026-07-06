import unittest

from spirit.packets.handlers.data_sync import DataSyncHandler
from spirit.network.message_names import OutboundMsg


class MockClientHandler:
    def __init__(self):
        self.addr = ("127.0.0.1", 54321)
        self.sent_packets = []

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)


class TestDynamicVersions(unittest.IsolatedAsyncioTestCase):
    async def test_version_data_contains_content_type_keys(self):
        """
        The client's VersionLabel.Start() (Type.Server) indexes
        versionData["ArchetypeContentType"] and
        versionData["LocalizationContentType"] with no ContainsKey guard.
        These keys MUST be present or the client throws a KeyNotFoundException
        the moment the in-game Settings panel is opened (in any scene).
        """
        client = MockClientHandler()
        handler = DataSyncHandler(client)

        await handler.handle_get_dynamic_versions(
            message={}, request_id=42, flags=0
        )

        self.assertEqual(len(client.sent_packets), 1)
        res = client.sent_packets[0]

        self.assertEqual(res["messageName"], OutboundMsg.DYNAMIC_VERSIONS.value)
        version_data = res["versionData"]

        # Regression guard: the two keys the client indexes unconditionally.
        self.assertIn("ArchetypeContentType", version_data)
        self.assertIn("LocalizationContentType", version_data)

        # All version values must be strings (client concatenates them as text).
        for key, value in version_data.items():
            self.assertIsInstance(value, str, f"{key} must be a string")


if __name__ == "__main__":
    unittest.main()
