import json
import unittest

from spirit.packets.handlers.data_sync import DataSyncHandler
from spirit.game.attributes import AttrID

# The exact set of "empty" sentinel names the PTCGO client accepts.
# Recovered by decoding the obfuscated string blob in pie-src.dll
# (AvatarItemRendererBase.empty). Only when an avatar item's NAME is one of
# these does AvatarItemRenderer.UpdateAvatarItem SKIP the texture download and
# mark the slot ready. Any other name triggers a download; if the texture is
# absent from the avatar bundle the slot never becomes ready, stalling
# FlatAvatarRenderer on the VersusScreen and producing the
# "Releasing render texture that is set as Camera.targetTexture!" crash log.
CLIENT_EMPTY_SENTINELS = {
    "EmptyAvatarItem",
    "MNoJacket",
    "MNoGlasses",
    "FNoGlasses",
    "FBarefoot",
}


class MockClientHandler:
    def __init__(self):
        self.addr = ("127.0.0.1", 54321)
        self.sent_packets = []

    async def send_packet(self, data, request_id=0, flags=0):
        self.sent_packets.append(data)


def _attr_map(archetype):
    """Flatten a protobuf archetype's attributes into {attr_id: python_value}."""
    out = {}
    for attr in archetype.attributes:
        v = attr.value
        # objectType: 0=INT, 1=FLOAT?, ... we just read whichever field is set.
        if v.stringValue:
            out[attr.name] = v.stringValue
        elif v.boolValue:
            out[attr.name] = v.boolValue
        else:
            out[attr.name] = v.intValue
    return out


class TestAvatarDefaults(unittest.IsolatedAsyncioTestCase):
    async def test_default_avatar_items_use_empty_sentinel(self):
        """
        The 16 default (AVATAR_IS_DEFAULT) avatar archetypes are what the client's
        DefaultItemForGroup resolves an uncustomized avatar to. For every group
        that has no real texture in the avatar bundle, the default MUST carry an
        "empty" sentinel NAME, otherwise the client tries to download a
        non-existent texture, the avatar renderer hangs, and the VersusScreen
        teardown logs the render-texture crash on both matched clients.
        """
        client = MockClientHandler()
        handler = DataSyncHandler(client)

        await handler.handle_get_protobuf_all_avatar_archetypes_list(
            msg={}, rid=7, flags=0
        )

        self.assertEqual(len(client.sent_packets), 1)
        proto = client.sent_packets[0]

        name_id = int(AttrID.NAME)
        group_id = int(AttrID.AVATAR_GROUP)
        is_default_id = int(AttrID.AVATAR_IS_DEFAULT)

        defaults_by_group = {}
        for arch in proto.archetypes:
            attrs = _attr_map(arch)
            if attrs.get(is_default_id) is True:
                grp = attrs.get(group_id)
                raw_name = attrs.get(name_id)
                # NAME is JSON-wrapped: {"id": "<base_name>"}
                base_name = json.loads(raw_name)["id"]
                defaults_by_group[grp] = base_name

        # One default per customization group (0..15).
        self.assertEqual(set(defaults_by_group.keys()), set(range(16)))

        for grp, base_name in defaults_by_group.items():
            if grp == 15:
                # Skin is a colour slot: the client parses the trailing 6 hex
                # chars of the name for the default skin tone.
                tail = base_name[-6:]
                int(tail, 16)  # raises if not valid hex -> fails the test
            else:
                self.assertIn(
                    base_name,
                    CLIENT_EMPTY_SENTINELS,
                    f"group {grp} default '{base_name}' is not an empty sentinel; "
                    f"the client will try to download a missing texture and hang",
                )
                # Regression guard against the old hanging value.
                self.assertFalse(
                    base_name.startswith("dummy_avatar_item_"),
                    f"group {grp} still uses the hanging placeholder name",
                )


if __name__ == "__main__":
    unittest.main()
