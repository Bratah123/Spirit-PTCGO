import unittest
import os
import tempfile
from unittest.mock import patch

from spirit.database import db_manager


class TestStarterContent(unittest.TestCase):
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

    def test_eligible_booster_sets_excludes_placeholder_sets(self):
        from spirit.game.set_utils import eligible_booster_sets, card_script_counts

        eligible = eligible_booster_sets()
        counts = card_script_counts()

        self.assertNotIn("BW1", eligible)
        self.assertNotIn("CUSTOM", eligible)
        self.assertNotIn("Free_Energy", eligible)
        self.assertIn("SWSH12", eligible)
        for code in eligible:
            self.assertGreater(counts[code], 10)

    def test_starter_decks_resolve_to_60_cards(self):
        from spirit.game.starter_content import STARTER_DECKS, build_deck_data

        for deck_name, decklist in STARTER_DECKS:
            deck_data = build_deck_data(deck_name, decklist)
            self.assertEqual(deck_data["deckName"], deck_name)
            self.assertEqual(len(deck_data["piles"]["deck"]), 60,
                             f"Deck '{deck_name}' did not resolve all 60 cards")
            self.assertTrue(deck_data["deckID"])
            attr_names = {a["name"] for a in deck_data["attributes"]}
            self.assertIn(200670, attr_names)  # coin
            self.assertIn(200680, attr_names)  # sleeve
            self.assertIn(200690, attr_names)  # deck box

    def test_every_eligible_set_has_booster_product(self):
        from spirit.game.set_utils import eligible_booster_sets
        from spirit.game.starter_content import starter_booster_packs

        packs = starter_booster_packs()
        pack_keys = {p.key.upper() for p in packs}
        for code in eligible_booster_sets():
            self.assertIn(code.upper(), pack_keys,
                          f"No booster pack product for eligible set {code}")

    def test_create_account_grants_starter_content(self):
        from spirit.database.accounts import create_account
        from spirit.database.player_data import get_decks_by_account_id, get_collection_by_account_id
        from spirit.game.starter_content import starter_booster_packs, STARTER_BOOSTER_PACK_COUNT

        account = create_account("starter_tester", "pw123")
        self.assertIsNotNone(account)
        account_id = account["account_id"]

        decks = get_decks_by_account_id(account_id)
        deck_names = {d["name"] for d in decks}
        self.assertIn("Lugia VSTAR", deck_names)
        self.assertIn("Mew VMAX", deck_names)
        self.assertIn("Lost Zone Box", deck_names)
        self.assertIn("Regigigas", deck_names)
        for d in decks:
            self.assertEqual(len(d["deck_data"]["piles"]["deck"]), 60)

        collection = {c["archetype_id"]: c for c in get_collection_by_account_id(account_id)}
        for pack in starter_booster_packs():
            self.assertIn(pack.guid, collection, f"Missing starter packs for {pack.key}")
            self.assertEqual(collection[pack.guid]["nontradable_count"], STARTER_BOOSTER_PACK_COUNT)

        # Starter cosmetics (coin, sleeve, deck box) are granted
        from spirit.game.starter_content import STARTER_COSMETICS
        for cosmetic_guid in STARTER_COSMETICS:
            self.assertIn(cosmetic_guid, collection, f"Missing starter cosmetic {cosmetic_guid}")

        # Deck cards were added to the collection too
        lugia = next(d for d in decks if d["name"] == "Lugia VSTAR")
        for guid in set(lugia["deck_data"]["piles"]["deck"]):
            self.assertIn(guid, collection)

    def test_new_account_starting_wallet(self):
        from spirit.database.accounts import create_account
        from spirit.database.player_data import get_wallet_by_account_id

        account = create_account("wallet_tester", "pw123")
        wallet = get_wallet_by_account_id(account["account_id"])
        self.assertEqual(wallet["coins"], 1000)
        self.assertEqual(wallet["gems"], 0)
        self.assertEqual(wallet["tickets"], 100)

    def test_account_does_not_own_every_card(self):
        """The account only owns starter-deck cards + packs, not the whole card pool."""
        from spirit.database.accounts import create_account
        from spirit.database.player_data import (
            get_merged_collection_payload, get_decks_by_account_id)
        from spirit.game.scripts.cards import loader as card_loader

        account = create_account("scoping_tester", "pw123")
        account_id = account["account_id"]

        payload = get_merged_collection_payload(account_id)
        owned = {c["archetypeID"] for c in payload}

        # Every non-free card in the payload must come from a starter deck or a pack
        free_energy = {c.guid.lower() for c in card_loader.load_all()
                       if c.key == "Free_Energy"}
        deck_guids = set()
        for d in get_decks_by_account_id(account_id):
            deck_guids.update(g.lower() for g in d["deck_data"]["piles"]["deck"])

        # The full card pool is far larger than what a new account should own
        all_cards = {c.guid.lower() for c in card_loader.load_all()}
        self.assertLess(len(owned), len(all_cards),
                        "New account should not own the entire card pool")

        for guid in owned:
            if guid in free_energy or guid in deck_guids:
                continue
            # Anything else must be an owned product (booster pack), never a bulk card
            self.assertNotIn(guid, all_cards,
                             f"Owns unexpected card not from a starter deck: {guid}")


if __name__ == '__main__':
    unittest.main()
