import os
import tempfile
import unittest
from unittest.mock import patch

from spirit.packets.handlers.data_sync import DataSyncHandler
from spirit.network.message_names import OutboundMsg
from spirit.game.attributes import AttrID


class MockClientHandler:
    def __init__(self, account_id="settings_user", username="settings_user"):
        self.addr = ("127.0.0.1", 4444)
        self.sent_packets = []
        self.player = type("P", (), {"account_id": account_id, "username": username})()

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)


class TestAccountSettings(unittest.IsolatedAsyncioTestCase):
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

    def _make_account(self, name):
        from spirit.database.accounts import create_account
        return create_account(name, "pw")["account_id"]

    def test_fresh_account_has_empty_settings_attr(self):
        from spirit.game.account_attributes import build_account_attributes
        aid = self._make_account("fresh_settings")
        attrs = {a["name"]: a["value"] for a in build_account_attributes(aid)}
        self.assertIn(AttrID.ACCOUNT_SETTINGS.value, attrs)
        self.assertEqual(attrs[AttrID.ACCOUNT_SETTINGS.value], {})

    def test_merge_persists_and_is_partial(self):
        from spirit.database.player_data import merge_account_settings, get_account_settings
        aid = self._make_account("merge_settings")
        merge_account_settings(aid, {109: 15, 116: 1})
        merge_account_settings(aid, {110: -1})  # partial write must not wipe others
        settings = get_account_settings(aid)
        self.assertEqual(settings["109"], 15)
        self.assertEqual(settings["116"], 1)
        self.assertEqual(settings["110"], -1)

    def test_login_anchor_suppresses_replay_but_keeps_ingame_animation(self):
        from spirit.database import versus_data
        from spirit.game.season_manager import VersusSeasonManager
        from spirit.game.account_attributes import (
            build_account_attributes, anchor_versus_animation,
            VERSUS_LAST_SEEN_POINTS_SETTING as S109)
        from spirit.game.attributes import AttrID

        aid = self._make_account("anchor_case")
        season = VersusSeasonManager().get_active_season()
        sid = season.season_id if season else ""
        for _ in range(2):
            versus_data.award_match_points(aid, True, season=season)  # prior-session points
        points = versus_data.get_progress(aid, sid)[0]
        self.assertGreater(points, 0)

        def s109(attrs):
            d = {a["name"]: a["value"] for a in attrs}
            return d[AttrID.ACCOUNT_SETTINGS.value].get(str(S109)), d[AttrID.SEASON_POINTS.value]

        # Login anchors 109 to current points -> nothing to animate on relog
        anchor_versus_animation(aid)
        anchored, pts_attr = s109(build_account_attributes(aid))
        self.assertEqual(anchored, points)
        self.assertEqual(pts_attr, points)

        # In-session win: 109 stays stale (no re-anchor) so the gain still animates
        versus_data.award_match_points(aid, True, season=season)
        new_points = versus_data.get_progress(aid, sid)[0]
        stale, pts_attr2 = s109(build_account_attributes(aid))
        self.assertEqual(stale, points)          # last-seen still old
        self.assertEqual(pts_attr2, new_points)  # but season points advanced -> animates

        # Relog re-anchors -> no replay of the now-seen points
        anchor_versus_animation(aid)
        reanchored, _ = s109(build_account_attributes(aid))
        self.assertEqual(reanchored, new_points)

    async def test_handler_persists_and_echoes_account_updated(self):
        aid = self._make_account("handler_settings")
        client = MockClientHandler(account_id=aid, username="handler_settings")
        handler = DataSyncHandler(client)

        # setting 109 = LastKnownSeasonPointTotal (versus ladder animation anchor)
        await handler.handle_set_account_settings({"settings": {"109": 42}}, 0, 0)

        # Echoes AccountUpdated so the client's SaveAccountSettings coroutine unblocks
        self.assertEqual(len(client.sent_packets), 1)
        packet = client.sent_packets[0]
        self.assertEqual(packet["messageName"], OutboundMsg.ACCOUNT_UPDATED.value)
        attrs = {a["name"]: a["value"] for a in packet["account"]["attributes"]}
        self.assertEqual(attrs[AttrID.ACCOUNT_SETTINGS.value]["109"], 42)

        # Value survives a subsequent login attribute build (persisted)
        from spirit.game.account_attributes import build_account_attributes
        relogin = {a["name"]: a["value"] for a in build_account_attributes(aid)}
        self.assertEqual(relogin[AttrID.ACCOUNT_SETTINGS.value]["109"], 42)


if __name__ == "__main__":
    unittest.main()
