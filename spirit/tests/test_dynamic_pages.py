import unittest
import os
import tempfile
from unittest.mock import MagicMock, AsyncMock, patch

from spirit.database import db_manager


class TestDynamicPages(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        cls.db_patcher = patch('spirit.database.connection.DB_PATH', cls.db_path)
        cls.db_patcher.start()

        from spirit.database.setup_db import setup_database
        setup_database()

    @classmethod
    def tearDownClass(cls):
        cls.db_patcher.stop()
        try:
            os.close(cls.db_fd)
            os.unlink(cls.db_path)
        except OSError:
            pass

    def setUp(self):
        from spirit.database import db_session, DynamicPage
        with db_session() as session:
            session.query(DynamicPage).delete()

    def _make_handler(self):
        from spirit.packets.handlers.data_sync import DataSyncHandler
        mock_client = MagicMock()
        mock_client.send_packet = AsyncMock()
        mock_client.addr = ("127.0.0.1", 4444)
        mock_client.player = None
        return DataSyncHandler(mock_client), mock_client

    async def test_dynamic_pages_served_from_db_sorted(self):
        from spirit.database.economy_data import upsert_dynamic_page
        from spirit.network.message_names import OutboundMsg

        upsert_dynamic_page({"template": "LandingPageLeft"}, sort_order=2)
        upsert_dynamic_page({"template": "LandingPageRight"}, sort_order=1)
        upsert_dynamic_page({"template": "Hidden"}, sort_order=0, enabled=False)
        upsert_dynamic_page({"note": "down for maintenance"},
                            page_type="maintenance", sort_order=0)

        handler, client = self._make_handler()
        await handler.handle_get_dynamic_pages({}, 100, 0)

        client.send_packet.assert_called_once()
        res = client.send_packet.call_args.args[0]
        self.assertEqual(res["messageName"], OutboundMsg.DYNAMIC_LANDING_PAGES.value)

        templates = [p["template"] for p in res["pageData"]]
        self.assertEqual(templates, ["LandingPageRight", "LandingPageLeft"])
        self.assertNotIn("Hidden", templates)

        self.assertEqual(len(res["maintenanceData"]), 1)
        self.assertEqual(res["maintenanceData"][0]["note"], "down for maintenance")

    async def test_dynamic_pages_empty_db(self):
        handler, client = self._make_handler()
        await handler.handle_get_dynamic_pages({}, 101, 0)

        res = client.send_packet.call_args.args[0]
        self.assertEqual(res["pageData"], [])
        self.assertEqual(res["maintenanceData"], [])

    async def test_admin_edit_flows_to_client(self):
        """A page saved through the Admin API is served to the game client."""
        import json as jsonlib
        from spirit.server.admin_api import route_admin

        login = route_admin('POST', '/admin/api/login',
                            jsonlib.dumps({"username": "brandon", "password": "password"}),
                            headers={})
        cookie = login[3][0][1].split(';')[0]

        content = {"template": "LandingPageRight",
                   "labels": {"GameText": {"bundle": {"en_US": "Season 1 rewards!"}}}}
        result = route_admin('POST', '/admin/api/pages', jsonlib.dumps({
            "content_json": content, "sort_order": 1
        }), headers={"Cookie": cookie})
        self.assertEqual(result[0], 200)

        handler, client = self._make_handler()
        await handler.handle_get_dynamic_pages({}, 102, 0)
        res = client.send_packet.call_args.args[0]
        self.assertEqual(len(res["pageData"]), 1)
        self.assertEqual(
            res["pageData"][0]["labels"]["GameText"]["bundle"]["en_US"],
            "Season 1 rewards!")


if __name__ == '__main__':
    unittest.main()
