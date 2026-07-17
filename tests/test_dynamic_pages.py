import gzip
import io
import json
import shutil
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image, ImageDraw

from spirit.packets.handlers.data_sync import _dynamic_page_is_active
from spirit.server import dynamic_pages
from spirit.server.manifest_manager import ManifestManager


def localized(text):
    return {"token": "spirit.test", "bundle": {"en_US": text}}


@contextmanager
def workspace_temp_dir():
    """Avoid Python 3.14's restrictive Windows TemporaryDirectory ACLs."""
    root = Path("tests") / f".tmp_dynamic_pages_{uuid.uuid4().hex}"
    root.mkdir()
    try:
        yield root
    finally:
        shutil.rmtree(root)


def landing_page(template="LandingPageRight", actions=None, button_text="OPEN SHOP"):
    labels = {"GameText": localized("A visual landing page")}
    if actions:
        labels["ButtonText"] = localized(button_text)
    return {
        "template": template,
        "sortOrder": 99,
        "startTime": 0,
        "endTime": dynamic_pages.FOREVER_MS,
        "labels": labels,
        "images": {
            "GameBackground": {
                "localeImageMap": {"en_US": "preview_art"},
            }
        },
        "actions": actions or {},
    }


class DynamicPageValidationTests(unittest.TestCase):
    def test_normalizes_client_asset_path_and_database_sort_order(self):
        page = landing_page()

        normalized = dynamic_pages.normalize_page(page, "landing", sort_order="7")

        self.assertEqual(normalized["sortOrder"], 7)
        self.assertEqual(
            normalized["images"]["GameBackground"]["localeImageMap"]["en_US"],
            "LandingPage/preview_art",
        )
        self.assertEqual(
            page["images"]["GameBackground"]["localeImageMap"]["en_US"],
            "preview_art",
            "normalization must not mutate the caller's editor state",
        )

    def test_rejects_overlapping_client_buttons(self):
        page = landing_page(
            actions={
                "UpsellButton": {"name": "NavigateToScene", "value": {"scene": "Shop"}},
                "CodeRedeemButton": {
                    "name": "NavigateToScene",
                    "value": {"scene": "ShopCodeRedemption"},
                },
            }
        )

        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "overlap"):
            dynamic_pages.normalize_page(page, "landing")

    def test_rejects_action_without_visible_button_caption(self):
        page = landing_page(
            actions={
                "UpsellButton": {"name": "NavigateToScene", "value": {"scene": "Shop"}},
            }
        )
        del page["labels"]["ButtonText"]

        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "ButtonText"):
            dynamic_pages.normalize_page(page, "landing")

        page["labels"]["ButtonText"] = localized("   ")
        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "visible text"):
            dynamic_pages.normalize_page(page, "landing")

    def test_rejects_cta_on_no_buttons_template(self):
        page = landing_page(
            template="LandingPageRightNoButtons",
            actions={
                "UpsellButton": {"name": "NavigateToUrl", "value": {"url": "https://example.test"}},
            },
        )

        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "No Buttons"):
            dynamic_pages.normalize_page(page, "landing")

    def test_rejects_action_slot_typo_that_unity_cannot_bind(self):
        page = landing_page(
            actions={
                "ShopButton": {"name": "NavigateToScene", "value": {"scene": "Shop"}},
            }
        )

        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "only target"):
            dynamic_pages.normalize_page(page, "landing")

    def test_maintenance_requires_native_notice_label(self):
        page = {
            "template": "SplashMaintenanceWindow",
            "startTime": 10,
            "endTime": 20,
            "labels": {},
            "images": {},
            "actions": {},
        }

        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "NotificationBody"):
            dynamic_pages.normalize_page(page, "maintenance")

        page["labels"]["NotificationBody"] = localized("Maintenance")
        page["startTime"] = 0
        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "startTime"):
            dynamic_pages.normalize_page(page, "maintenance")

        page["startTime"] = 10
        normalized = dynamic_pages.normalize_page(page, "maintenance")
        self.assertEqual(normalized["template"], "SplashMaintenanceWindow")

        del page["endTime"]
        with self.assertRaisesRegex(dynamic_pages.PageValidationError, "endTime"):
            dynamic_pages.normalize_page(page, "maintenance")

    def test_landing_visibility_schedule_is_server_enforced(self):
        now = 1_000_000
        self.assertTrue(_dynamic_page_is_active({"startTime": 0, "endTime": 0}, now))
        self.assertTrue(
            _dynamic_page_is_active({"startTime": now - 1, "endTime": now + 1}, now)
        )
        self.assertFalse(
            _dynamic_page_is_active({"startTime": now + 1, "endTime": now + 2}, now)
        )
        self.assertFalse(
            _dynamic_page_is_active({"startTime": 0, "endTime": now}, now)
        )


class DynamicPageAssetTests(unittest.TestCase):
    def tearDown(self):
        dynamic_pages.invalidate_asset_catalog()

    @staticmethod
    def fake_environment(name="preview_art", image=None):
        texture = SimpleNamespace(
            m_Name=name,
            m_Width=image.width if image else 2048,
            m_Height=image.height if image else 2048,
            image=image,
        )
        obj = SimpleNamespace(
            type=SimpleNamespace(name="Texture2D"),
            read=lambda: texture,
        )
        return SimpleNamespace(objects=[obj])

    def test_scans_landing_bundle_metadata_without_extracting_pngs(self):
        with workspace_temp_dir() as root:
            data_path = root / "en_US_LandingPage_Test_1" / "cab" / "__data"
            data_path.parent.mkdir(parents=True)
            data_path.write_bytes(b"test bundle")
            env = self.fake_environment()

            with (
                patch.object(dynamic_pages, "_candidate_bundle_roots", return_value=[(root, False, "test cache")]),
                patch.object(dynamic_pages.UnityPy, "load", return_value=env),
            ):
                catalog, sources, errors = dynamic_pages._scan_catalog()

        self.assertFalse(errors)
        self.assertIn("preview_art", catalog)
        self.assertEqual(catalog["preview_art"]["request_path"], "LandingPage/preview_art")
        self.assertFalse(catalog["preview_art"]["installed"])
        self.assertEqual(sources[0]["textures"], 1)

    def test_preview_uses_the_unity_prefab_crop_and_expected_size(self):
        image = Image.new("RGB", (2048, 2048), "black")
        ImageDraw.Draw(image).rectangle((64, 484, 1984, 1564), fill=(220, 40, 30))
        env = self.fake_environment(image=image)
        asset = {
            "name": "preview_art",
            "data_path": "fake/__data",
            "mtime_ns": 1,
            "file_size": 1,
        }

        with (
            patch.object(dynamic_pages, "_get_catalog", return_value={"preview_art": asset}),
            patch.object(dynamic_pages.UnityPy, "load", return_value=env),
        ):
            payload = dynamic_pages.render_asset_jpeg("LandingPage/preview_art", "thumb")

        rendered = Image.open(io.BytesIO(payload))
        self.assertEqual(rendered.size, (384, 216))
        red, green, blue = rendered.getpixel((192, 108))
        self.assertGreater(red, 190)
        self.assertLess(green, 70)
        self.assertLess(blue, 70)

    def test_install_copies_the_selected_source_bundle_to_external_cache(self):
        with workspace_temp_dir() as root:
            source = root / "source" / "en_US_LandingPage_Test_1"
            source_data = source / "cab" / "__data"
            source_data.parent.mkdir(parents=True)
            source_data.write_bytes(b"whole unity bundle")
            destination = root / "externalCache"
            catalog = {
                "preview_art": {
                    "name": "preview_art",
                    "bundle": source.name,
                    "bundle_dir": str(source),
                    "installed": False,
                }
            }
            page = dynamic_pages.normalize_page(landing_page(), "landing")

            with (
                patch.object(dynamic_pages, "_get_catalog", return_value=catalog),
                patch.object(dynamic_pages, "EXTERNAL_CACHE_DIR", destination),
                patch.object(dynamic_pages, "invalidate_asset_catalog") as invalidate,
            ):
                installed, unresolved = dynamic_pages.install_page_assets(page)

            self.assertEqual(installed, [source.name])
            self.assertFalse(unresolved)
            self.assertEqual(
                (destination / source.name / "cab" / "__data").read_bytes(),
                b"whole unity bundle",
            )
            invalidate.assert_called_once_with()

            custom_page = landing_page()
            custom_page["images"]["GameBackground"]["localeImageMap"]["en_US"] = (
                "Custom/preview_art"
            )
            with (
                patch.object(dynamic_pages, "_get_catalog", return_value=catalog),
                patch.object(dynamic_pages, "EXTERNAL_CACHE_DIR", root / "unused"),
            ):
                installed, unresolved = dynamic_pages.install_page_assets(custom_page)
            self.assertFalse(installed)
            self.assertEqual(unresolved, ["Custom/preview_art"])

    def test_custom_art_is_packed_into_the_native_visible_texture_region(self):
        source = Image.new("RGB", (1600, 900), (25, 140, 220))

        texture = dynamic_pages._prepare_custom_texture(source, (2048, 2048))

        self.assertEqual(texture.size, (2048, 2048))
        self.assertEqual(texture.getpixel((0, 0)), (0, 0, 0, 255))
        red, green, blue, alpha = texture.getpixel((1024, 1024))
        self.assertLess(red, 35)
        self.assertGreater(green, 130)
        self.assertGreater(blue, 210)
        self.assertEqual(alpha, 255)

    def test_custom_upload_normalizes_saves_and_rebuilds_the_bundle(self):
        image = Image.new("RGB", (1280, 720), "purple")
        payload = io.BytesIO()
        image.save(payload, format="PNG")
        asset_name = "summer_event_landingpage"
        catalog_asset = {
            "name": asset_name,
            "custom": True,
            "request_path": f"LandingPage/{asset_name}",
        }

        with workspace_temp_dir() as root:
            with (
                patch.object(dynamic_pages, "CUSTOM_IMAGE_DIR", root),
                patch.object(
                    dynamic_pages,
                    "_get_catalog",
                    side_effect=[{}, {asset_name: catalog_asset}],
                ),
                patch.object(
                    dynamic_pages,
                    "compile_custom_landing_bundle",
                    return_value={"built": True, "assets": 1},
                ) as compile_bundle,
            ):
                imported = dynamic_pages.save_custom_landing_image(
                    "Summer Event.jpg", payload.getvalue()
                )

            saved = root / f"{asset_name}.png"
            self.assertTrue(saved.is_file())
            with Image.open(saved) as saved_image:
                self.assertEqual(saved_image.size, (1280, 720))
            self.assertEqual(imported["name"], asset_name)
            compile_bundle.assert_called_once_with(force=True)

    def test_custom_upload_does_not_shadow_original_game_art(self):
        image = Image.new("RGB", (640, 360), "blue")
        payload = io.BytesIO()
        image.save(payload, format="PNG")
        original = {"summer_landingpage": {"custom": False}}

        with patch.object(dynamic_pages, "_get_catalog", return_value=original):
            with self.assertRaisesRegex(
                dynamic_pages.PageValidationError, "conflicts with original game artwork"
            ):
                dynamic_pages.save_custom_landing_image(
                    "summer", payload.getvalue()
                )


class LandingPageManifestTests(unittest.TestCase):
    def test_manifest_publishes_prefixed_landing_texture_key(self):
        with workspace_temp_dir() as root:
            bundle = root / "en_US_LandingPage_AdminPreview_9371"
            data_path = bundle / "cab" / "__data"
            data_path.parent.mkdir(parents=True)
            data_path.write_bytes(b"test bundle")
            texture = SimpleNamespace(m_Name="Preview_Art")
            obj = SimpleNamespace(
                type=SimpleNamespace(name="Texture2D"),
                read=lambda: texture,
            )
            env = SimpleNamespace(objects=[obj])

            with patch("spirit.server.manifest_manager.UnityPy.load", return_value=env):
                manager = ManifestManager([str(root)])
                manifest = json.loads(gzip.decompress(manager.generate_manifest()))

        landing = next(bundle for bundle in manifest["bundles"] if bundle["name"] == "LandingPage")
        assets = {asset["name"] for asset in landing["assets"]}
        self.assertIn("preview_art", assets)
        self.assertIn("LandingPage/preview_art", assets)
        self.assertFalse(any(bundle["name"].endswith("_water") for bundle in manifest["bundles"]))


if __name__ == "__main__":
    unittest.main()
