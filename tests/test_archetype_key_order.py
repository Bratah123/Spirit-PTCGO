"""Archetype key order for the deck-builder OwnedStacks path."""
import unittest

from spirit.packets.handlers.data_sync import (
    ARCHETYPE_KEYS,
    DataSyncHandler,
    order_archetype_keys,
)


class ArchetypeKeyOrderTests(unittest.TestCase):
    def test_seed_order_puts_free_energy_first(self):
        self.assertEqual(ARCHETYPE_KEYS[0], "Free_Energy")

    def test_order_helper_keeps_seed_prefix_and_appends_new_keys(self):
        keys = order_archetype_keys(
            ["Free_Energy", "Energy", "AvatarItems"],
            ["AvatarItems", "DP1", "", None, "Free_Energy", "EX1"],
        )
        self.assertEqual(keys[0], "Free_Energy")
        self.assertEqual(keys, ["Free_Energy", "Energy", "AvatarItems", "DP1", "EX1"])

    def test_alphabetical_sort_would_put_avatar_items_first(self):
        sample = ["Free_Energy", "Energy", "AvatarItems", "BW1"]
        self.assertEqual(sorted(sample)[0], "AvatarItems")
        self.assertEqual(order_archetype_keys(sample)[0], "Free_Energy")

    def test_built_key_list_starts_with_free_energy(self):
        keys = DataSyncHandler._build_archetype_keys()
        self.assertGreater(len(keys), 0)
        self.assertEqual(keys[0], "Free_Energy")
        seed = [key for key in ARCHETYPE_KEYS if key in keys]
        self.assertEqual(keys[:len(seed)], seed)
        self.assertEqual(len(keys), len(set(keys)))


if __name__ == "__main__":
    unittest.main()
