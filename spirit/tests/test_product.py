import unittest
import json
import spirit.server.state as state
from spirit.game.models.product import Product, BoosterPack
from spirit.game.attributes import AttrID, CardType, Rarities
from spirit.game.data_utils import BoosterPackDef
from spirit.game.scripts.cards import loader as card_loader

class TestCardLoaderCache(unittest.TestCase):
    def test_load_all_is_cached(self):
        first = card_loader.load_all()
        self.assertTrue(first)
        # Repeated calls must NOT re-exec scripts (blocks the event loop ~1s
        # per call and rebuilds effect registries mid-game)
        self.assertIs(card_loader.load_all(), first)
        card_one = card_loader.cards[0]
        self.assertIs(card_loader.load_all()[0], card_one)


class TestProductDynamicHostExpansion(unittest.TestCase):
    def setUp(self):
        # Reset server host to default before each test
        state.SERVER_HOST = "127.0.0.1:8000"

    def test_relative_image_url_preservation(self):
        # 1. Setup a product with a relative image URL
        attributes = {
            str(AttrID.IMAGE_URL.value): {"type": "string", "value": "bw1_booster.png"},
            str(AttrID.PRODUCT_TYPE.value): {"type": "int", "value": 1}
        }
        product = Product(guid="test-guid", key="test-key", attributes=attributes)

        # 2. Verify Shop JSON serialization preserves the relative URL to prevent cache overwrites
        serialized_json = product.to_archetype_json()
        img_attr_json = next(attr for attr in serialized_json["attributes"] if attr["name"] == AttrID.IMAGE_URL.value)
        self.assertEqual(img_attr_json["value"], "bw1_booster.png")

        # 3. Verify Protobuf serialization dictionary preserves relative URL
        serialized_dict = product.to_archetype_dict()
        img_attr_dict = serialized_dict["attributes"][str(AttrID.IMAGE_URL.value)]
        self.assertEqual(img_attr_dict["value"], "bw1_booster.png")

    def test_localhost_image_url_preservation(self):
        # 1. Setup a product with a hardcoded localhost URL
        attributes = {
            str(AttrID.IMAGE_URL.value): {"type": "string", "value": "http://127.0.0.1:8000/products/custom_sleeve.png"},
            str(AttrID.PRODUCT_TYPE.value): {"type": "int", "value": 1}
        }
        product = Product(guid="test-guid", key="test-key", attributes=attributes)

        # 2. Verify Shop JSON serialization preserves original URL without dynamic expansion
        serialized_json = product.to_archetype_json()
        img_attr_json = next(attr for attr in serialized_json["attributes"] if attr["name"] == AttrID.IMAGE_URL.value)
        self.assertEqual(img_attr_json["value"], "http://127.0.0.1:8000/products/custom_sleeve.png")

        # 3. Verify Protobuf serialization dictionary preserves exact values
        serialized_dict = product.to_archetype_dict()
        img_attr_dict = serialized_dict["attributes"][str(AttrID.IMAGE_URL.value)]
        self.assertEqual(img_attr_dict["value"], "http://127.0.0.1:8000/products/custom_sleeve.png")

    def test_product_definition_image_name_extraction(self):
        # Verify that ProductDef.to_archetype_dict extracts image name correctly to prevent shop/collection image bugs
        prod_def = BoosterPackDef(
            guid="test-pack-guid",
            key="BW1",
            name="test-pack",
            image_url="http://127.0.0.1:8000/products/bw1_booster.png"
        )
        archetype = prod_def.to_archetype_dict()
        
        # Verify AttrID.IMAGE_NAME (10520) is populated and has the correct relative asset name
        img_name_attr = archetype["attributes"][str(AttrID.IMAGE_NAME.value)]
        self.assertEqual(img_name_attr["value"], "bw1_booster")
        
        # Verify relative image_url extraction works too
        prod_def_rel = BoosterPackDef(
            guid="test-pack-guid-rel",
            key="BW1",
            name="test-pack-rel",
            image_url="my_cool_sleeve.png"
        )
        archetype_rel = prod_def_rel.to_archetype_dict()
        img_name_attr_rel = archetype_rel["attributes"][str(AttrID.IMAGE_NAME.value)]
        self.assertEqual(img_name_attr_rel["value"], "my_cool_sleeve")

    def test_booster_pack_dynamic_pool(self):
        # Load all cards to populate card_loader.cards
        card_loader.load_all()
        
        # Create a SWSH8 booster pack
        booster = BoosterPack(guid="test-swsh8-pack", key="SWSH8")
        
        # Open it
        opened_guids = booster.open("-1")
        
        # Verify it returns 10 cards
        self.assertEqual(len(opened_guids), 10)
        
        # Verify 4 Commons (indices 0 to 3)
        for i in range(4):
            c = card_loader.cards_by_guid.get(opened_guids[i])
            self.assertIsNotNone(c)
            self.assertEqual(c.get_attribute_value(AttrID.RARITY), Rarities.Common.value)
            self.assertNotEqual(c.get_attribute_value(AttrID.CARD_TYPE), CardType.ENERGY.value)

        # Verify 3 Uncommons (indices 4 to 6)
        for i in range(4, 7):
            c = card_loader.cards_by_guid.get(opened_guids[i])
            self.assertIsNotNone(c)
            self.assertEqual(c.get_attribute_value(AttrID.RARITY), Rarities.Uncommon.value)
            self.assertNotEqual(c.get_attribute_value(AttrID.CARD_TYPE), CardType.ENERGY.value)

        # Verify 1 Energy (index 7)
        c_energy = card_loader.cards_by_guid.get(opened_guids[7])
        self.assertIsNotNone(c_energy)
        self.assertEqual(c_energy.get_attribute_value(AttrID.CARD_TYPE), CardType.ENERGY.value)
        self.assertFalse(c_energy.get_attribute_value(AttrID.IS_SPECIAL_ENERGY))

        # Verify 1 Reverse Holo (index 8)
        c_rev = card_loader.cards_by_guid.get(opened_guids[8])
        self.assertIsNotNone(c_rev)
        self.assertNotEqual(c_rev.get_attribute_value(AttrID.CARD_TYPE), CardType.ENERGY.value)

        # Verify 1 Rare / Hit (index 9)
        c_rare = card_loader.cards_by_guid.get(opened_guids[9])
        self.assertIsNotNone(c_rare)
        self.assertGreaterEqual(c_rare.get_attribute_value(AttrID.RARITY), Rarities.Rare.value)
        self.assertNotEqual(c_rare.get_attribute_value(AttrID.CARD_TYPE), CardType.ENERGY.value)
            
        # Create a Booster with a key that has no cards
        empty_booster = BoosterPack(guid="test-empty-pack", key="NO_CARDS_KEY")
        empty_guids = empty_booster.open("-1")
        
        # It should fallback to the default BW1 pool
        self.assertEqual(len(empty_guids), 10)
        for guid in empty_guids:
            self.assertIn(guid, empty_booster.card_pool)


class TestAutoBoosterImages(unittest.TestCase):
    def test_every_eligible_pack_image_maps_to_bundle_asset(self):
        """Each eligible booster's IMAGE_NAME must equal a real PNG basename, or the client
        requests a missing asset from the 'packs' bundle and shows the loading hourglass."""
        import os
        from spirit.game.scripts.products import loader, PACK_ART_DIR
        from spirit.game.set_utils import eligible_booster_sets
        from spirit.game.attributes import ProductType

        loader.load_all()
        art = {os.path.splitext(f)[0].lower()
               for f in os.listdir(PACK_ART_DIR) if f.lower().endswith(".png")}
        eligible = {c.upper() for c in eligible_booster_sets()}

        for p in loader.products:
            if p.product_type != ProductType.PACKS.value or p.key.upper() not in eligible:
                continue
            image_name = p.get_attribute_value(AttrID.IMAGE_NAME)
            self.assertIn(image_name, art,
                          f"Pack {p.key} IMAGE_NAME '{image_name}' has no matching art file")

    def test_resolve_pack_image_prefers_exact_then_prefix_then_generic(self):
        from spirit.game.scripts.products import resolve_pack_image, GENERIC_PACK_IMAGE
        # SWSH12 has {set}_booster_{name}.png -> prefix match
        self.assertTrue(resolve_pack_image("SWSH12").startswith("swsh12_booster"))
        # A set with no art at all falls back to the generic placeholder
        self.assertEqual(resolve_pack_image("ZZZ_NO_SUCH_SET"), GENERIC_PACK_IMAGE)


class TestPackRarityData(unittest.TestCase):
    def test_every_pack_carries_nonnull_rarity_data(self):
        """Attr 202250 (a.g[]) MUST be a non-empty array on every booster pack; the info-popup
        does new List<a.g>(ValueFor) and NREs on null (crashing on the 'i' button)."""
        from spirit.game.scripts.products import loader
        from spirit.game.attributes import ProductType

        loader.load_all()
        packs = [p for p in loader.products if p.product_type == ProductType.PACKS.value]
        self.assertTrue(packs, "no booster packs loaded")
        for p in packs:
            data = p.get_attribute_value(AttrID.PACK_RARITY_DATA)
            self.assertIsInstance(data, list, f"{p.key} rarity data must be a list, got {data!r}")
            self.assertTrue(data, f"{p.key} rarity data is empty")
            for slot in data:
                self.assertIn("rarityIcon", slot)
                self.assertIn("count", slot)
                self.assertIsInstance(slot["rarityName"]["id"], str)

    def test_rarity_data_survives_sku_alias(self):
        """The shop lists packs under a SKU alias; it must inherit 202250 so the shop 'i' popup works."""
        from spirit.game.models.product import make_shop_sku
        pack = BoosterPackDef(guid="11111111-2222-3333-4444-555555555555",
                              key="SWSH12", name="Test Pack", image_url="swsh12_booster")
        arch = pack.to_archetype_dict()
        prod = BoosterPack(arch["guid"], arch["key"], arch["attributes"])
        sku = make_shop_sku(prod)
        self.assertTrue(sku.get_attribute_value(AttrID.PACK_RARITY_DATA))


class TestPackPreviewCards(unittest.TestCase):
    def test_packs_get_valid_preview_cards(self):
        """Attr 201505 routes the "i" popup marquee through the cache-safe GetArchetype filter.
        Every preview GUID must be a real loaded card (the unfiltered set-featured path crashes)."""
        import spirit.packets.handlers.data_sync  # noqa: F401 - loads cards at import
        from spirit.game.scripts.cards import loader as card_loader
        from spirit.game.scripts.products import loader
        from spirit.game.attributes import ProductType

        loader.load_all()
        card_guids = {c.guid for c in card_loader.cards}
        packs = [p for p in loader.products if p.product_type == ProductType.PACKS.value]
        for p in packs:
            attr = p.attributes.get(str(AttrID.PACK_PREVIEW_CARDS.value))
            self.assertIsNotNone(attr, f"{p.key} has no preview cards (201505)")
            preview = json.loads(attr["value"])
            self.assertTrue(1 <= len(preview) <= 3, f"{p.key} preview size {len(preview)}")
            for guid in preview:
                self.assertIn(guid, card_guids, f"{p.key} preview {guid} is not a loaded card")

    def test_reload_sets_clears_featured_archetypes(self):
        """The set-featured GUIDs are original-PTCGO cards we never load; the pack popup feeds them
        UNFILTERED into CachedViewModel (KeyNotFoundException), so they must be cleared on load."""
        from spirit.packets.handlers import data_sync
        data_sync.reload_sets()
        self.assertTrue(data_sync.SETS_DB, "no sets loaded")
        self.assertTrue(all(not s.get("featuredArchetypes") for s in data_sync.SETS_DB))


if __name__ == '__main__':
    unittest.main()
