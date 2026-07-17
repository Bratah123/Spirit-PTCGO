"""Dynamic-page validation and preview assets for the admin dashboard.

The live client renders landing pages by loading one of a small set of Resources
prefabs and binding page fields to named GameObjects.  Landing artwork lives in
the original ``en_US_LandingPage_*`` Unity bundles as 2048px square textures;
the prefab displays a 1920x1080 UV crop from the middle of each texture.

This module keeps those client details out of the HTTP router.  It indexes the
locally available bundles, renders faithful browser previews with UnityPy, and
copies a selected source bundle into the server's ignored ``externalCache`` so
players can load the same art that an admin selected in the preview.
"""

from __future__ import annotations

import copy
import io
import logging
import os
import shutil
import threading
from collections import OrderedDict
from pathlib import Path

import UnityPy
from PIL import Image


LANDING_TEMPLATES = {
    "LandingPageLeft",
    "LandingPageRight",
    "LandingPageLeftNoButtons",
    "LandingPageRightNoButtons",
}
MAINTENANCE_TEMPLATE = "SplashMaintenanceWindow"
PAGE_TYPES = {"landing", "maintenance"}
ACTION_NAMES = {"NavigateToScene", "NavigateToUrl", "NavigateToUrls"}
ACTION_SLOTS = {"UpsellButton", "CodeRedeemButton"}
SUPPORTED_ACTION_SCENES = {"Shop", "ShopCodeRedemption", "Tournament", "Trade"}
FOREVER_MS = 4_102_444_800_000  # 2100-01-01 UTC

# LandingPageLeft/Right.prefab: UITexture.mRect.  The values are normalized so
# previews still work if a compatible bundle uses a different texture size.
_LANDING_UV_RECT = (0.03125, 0.236328125, 0.9375, 0.52734375)

_SERVER_DIR = Path(__file__).resolve().parent
_SPIRIT_DIR = _SERVER_DIR.parent
_PROJECT_DIR = _SPIRIT_DIR.parent
BUNDLE_CACHE_DIR = _SPIRIT_DIR / "assets" / "bundleCache"
EXTERNAL_CACHE_DIR = _SPIRIT_DIR / "assets" / "externalCache"
ORIGINAL_CACHE_DIR = _PROJECT_DIR / "original_game_cache"

_catalog_lock = threading.RLock()
_catalog: dict[str, dict] | None = None
_catalog_roots: list[dict] = []
_catalog_errors: list[str] = []

_image_lock = threading.RLock()
_image_cache: OrderedDict[tuple, bytes] = OrderedDict()
_IMAGE_CACHE_MAX = 128


class PageValidationError(ValueError):
    """Raised when a page would violate the Unity client's wire contract."""


def _resolved(path: Path) -> Path:
    try:
        return path.resolve()
    except OSError:
        return path.absolute()


def _add_bundle_root(
    roots: list[tuple[Path, bool, str]],
    seen: set[str],
    candidate: Path,
    installed: bool,
    source: str,
) -> None:
    """Adds either a bundleCache directory or a directory containing bundles."""
    candidate = candidate.expanduser()
    possibilities = [candidate]
    if candidate.name.casefold() != "bundlecache":
        possibilities.insert(0, candidate / "bundleCache")

    for path in possibilities:
        if not path.is_dir():
            continue
        try:
            has_landing = any(
                child.is_dir() and child.name.casefold().startswith("en_us_landingpage")
                for child in path.iterdir()
            )
        except OSError:
            continue
        if not has_landing:
            continue
        key = os.path.normcase(str(_resolved(path)))
        if key not in seen:
            seen.add(key)
            roots.append((path, installed, source))
        return


def _candidate_bundle_roots() -> list[tuple[Path, bool, str]]:
    roots: list[tuple[Path, bool, str]] = []
    seen: set[str] = set()

    # These locations are scanned by ManifestManager and are already available
    # to clients, so catalog entries from them do not need installing.
    _add_bundle_root(roots, seen, BUNDLE_CACHE_DIR, True, "server cache")
    _add_bundle_root(roots, seen, EXTERNAL_CACHE_DIR, True, "server external cache")

    configured = os.environ.get("PTCGO_CACHE_DIR")
    if configured:
        _add_bundle_root(roots, seen, Path(configured), True, "configured game cache")

    # Repository-local original cache used by the reverse-engineering workflow.
    # Its known layouts are checked without recursively walking thousands of
    # individual cached bundle directories.
    original_candidates = [
        ORIGINAL_CACHE_DIR,
        ORIGINAL_CACHE_DIR / "bundleCache",
    ]
    if ORIGINAL_CACHE_DIR.is_dir():
        original_candidates.extend(ORIGINAL_CACHE_DIR.glob("*/bundleCache"))
        original_candidates.extend(ORIGINAL_CACHE_DIR.glob("*/*/bundleCache"))
    for candidate in original_candidates:
        _add_bundle_root(roots, seen, candidate, False, "original game cache")
    return roots


def _bundle_data_path(bundle_dir: Path) -> Path | None:
    direct = bundle_dir / "00000000000000000000000001000000" / "__data"
    if direct.is_file():
        return direct
    try:
        return next((p for p in bundle_dir.rglob("__data") if p.is_file()), None)
    except OSError:
        return None


def _asset_rank(asset: dict) -> tuple:
    # Prefer a bundle already served to clients, then the newest local copy.
    return (
        1 if asset["installed"] else 0,
        int(asset.get("mtime_ns", 0)),
        asset["bundle"].casefold(),
    )


def _scan_catalog() -> tuple[dict[str, dict], list[dict], list[str]]:
    assets: dict[str, dict] = {}
    roots_public: list[dict] = []
    errors: list[str] = []

    for root, installed, source in _candidate_bundle_roots():
        bundle_count = 0
        texture_count = 0
        try:
            bundle_dirs = sorted(
                (
                    child
                    for child in root.iterdir()
                    if child.is_dir()
                    and child.name.casefold().startswith("en_us_landingpage")
                ),
                key=lambda p: p.name.casefold(),
            )
        except OSError as exc:
            errors.append(f"Could not read {source}: {exc}")
            continue

        for bundle_dir in bundle_dirs:
            data_path = _bundle_data_path(bundle_dir)
            if data_path is None:
                continue
            bundle_count += 1
            try:
                stat = data_path.stat()
                env = UnityPy.load(str(data_path))
                for obj in env.objects:
                    if obj.type.name != "Texture2D":
                        continue
                    texture = obj.read()
                    name = str(getattr(texture, "m_Name", "") or "").strip()
                    if not name:
                        continue
                    texture_count += 1
                    key = name.casefold()
                    item = {
                        "name": name,
                        "title": _display_name(name),
                        "request_path": f"LandingPage/{name}",
                        "bundle": bundle_dir.name,
                        "width": int(getattr(texture, "m_Width", 0) or 0),
                        "height": int(getattr(texture, "m_Height", 0) or 0),
                        "installed": bool(installed),
                        "source": source,
                        "data_path": str(data_path),
                        "bundle_dir": str(bundle_dir),
                        "mtime_ns": stat.st_mtime_ns,
                        "file_size": stat.st_size,
                    }
                    current = assets.get(key)
                    if current is None or _asset_rank(item) > _asset_rank(current):
                        assets[key] = item
            except Exception as exc:  # UnityPy emits several format-specific exceptions
                logging.warning("[Admin] Could not index landing bundle %s: %s", bundle_dir, exc)
                errors.append(f"{bundle_dir.name}: {exc}")

        roots_public.append(
            {
                "source": source,
                "installed": bool(installed),
                "bundles": bundle_count,
                "textures": texture_count,
            }
        )

    return assets, roots_public, errors


def _display_name(name: str) -> str:
    text = name
    if text.casefold().endswith("_landingpage"):
        text = text[: -len("_landingpage")]
    return " ".join(part for part in text.replace("-", "_").split("_") if part).title()


def invalidate_asset_catalog() -> None:
    global _catalog, _catalog_roots, _catalog_errors
    with _catalog_lock:
        _catalog = None
        _catalog_roots = []
        _catalog_errors = []
    with _image_lock:
        _image_cache.clear()


def _get_catalog() -> dict[str, dict]:
    global _catalog, _catalog_roots, _catalog_errors
    with _catalog_lock:
        if _catalog is None:
            _catalog, _catalog_roots, _catalog_errors = _scan_catalog()
        return _catalog


def asset_catalog_payload() -> dict:
    catalog = _get_catalog()
    with _catalog_lock:
        roots = copy.deepcopy(_catalog_roots)
        errors = list(_catalog_errors)
    public_assets = []
    for item in sorted(catalog.values(), key=lambda a: (a["title"].casefold(), a["name"].casefold())):
        public_assets.append(
            {
                key: item[key]
                for key in (
                    "name",
                    "title",
                    "request_path",
                    "bundle",
                    "width",
                    "height",
                    "installed",
                    "source",
                )
            }
        )
    return {"assets": public_assets, "sources": roots, "errors": errors}


def _lookup_asset(name_or_path: str) -> dict | None:
    name = str(name_or_path or "").strip().replace("\\", "/").rsplit("/", 1)[-1]
    return _get_catalog().get(name.casefold())


def _image_cache_get(key: tuple) -> bytes | None:
    with _image_lock:
        value = _image_cache.get(key)
        if value is not None:
            _image_cache.move_to_end(key)
        return value


def _image_cache_put(key: tuple, value: bytes) -> None:
    with _image_lock:
        _image_cache[key] = value
        _image_cache.move_to_end(key)
        while len(_image_cache) > _IMAGE_CACHE_MAX:
            _image_cache.popitem(last=False)


def render_asset_jpeg(name_or_path: str, variant: str = "preview") -> bytes | None:
    """Returns a cropped browser preview of a landing texture.

    ``thumb`` is 384x216 and ``preview`` is 960x540.  The crop mirrors the
    NGUI UITexture UV rectangle in every shipped landing-page prefab.
    """
    asset = _lookup_asset(name_or_path)
    if asset is None:
        return None
    variant = "thumb" if variant == "thumb" else "preview"
    target_size = (384, 216) if variant == "thumb" else (960, 540)
    cache_key = (
        asset["name"].casefold(),
        variant,
        asset["data_path"],
        asset["mtime_ns"],
        asset["file_size"],
    )
    cached = _image_cache_get(cache_key)
    if cached is not None:
        return cached

    env = UnityPy.load(asset["data_path"])
    image = None
    for obj in env.objects:
        if obj.type.name != "Texture2D":
            continue
        texture = obj.read()
        if str(getattr(texture, "m_Name", "")).casefold() == asset["name"].casefold():
            image = texture.image
            break
    if image is None:
        return None

    image = image.convert("RGB")
    width, height = image.size
    x, y, crop_w, crop_h = _LANDING_UV_RECT
    box = (
        max(0, round(width * x)),
        max(0, round(height * y)),
        min(width, round(width * (x + crop_w))),
        min(height, round(height * (y + crop_h))),
    )
    image = image.crop(box).resize(target_size, Image.Resampling.LANCZOS)
    output = io.BytesIO()
    image.save(output, format="JPEG", quality=84 if variant == "thumb" else 90, optimize=True)
    rendered = output.getvalue()
    _image_cache_put(cache_key, rendered)
    return rendered


def _background_asset_paths(content: dict) -> set[str]:
    paths: set[str] = set()
    images = content.get("images")
    if not isinstance(images, dict):
        return paths
    image = images.get("GameBackground")
    locale_map = image.get("localeImageMap") if isinstance(image, dict) else None
    if not isinstance(locale_map, dict):
        return paths
    for request_path in locale_map.values():
        if isinstance(request_path, str) and request_path.strip():
            paths.add(request_path.strip().replace("\\", "/"))
    return paths


def install_page_assets(content: dict) -> tuple[list[str], list[str]]:
    """Installs bundles referenced by a normalized page; returns (copied, unresolved)."""
    catalog = _get_catalog()
    selected = _background_asset_paths(content)
    bundles_to_copy: dict[str, dict] = {}
    unresolved: list[str] = []

    for request_path in selected:
        parts = request_path.split("/")
        if len(parts) != 2 or parts[0].casefold() != "landingpage":
            unresolved.append(request_path)
            continue
        name = parts[1].casefold()
        asset = catalog.get(name)
        if asset is None:
            unresolved.append(request_path)
        elif not asset["installed"]:
            bundles_to_copy[asset["bundle"].casefold()] = asset

    installed: list[str] = []
    if bundles_to_copy:
        EXTERNAL_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        external_root = _resolved(EXTERNAL_CACHE_DIR)
        for asset in bundles_to_copy.values():
            source = Path(asset["bundle_dir"])
            destination = EXTERNAL_CACHE_DIR / source.name
            if _resolved(destination.parent) != external_root:
                raise RuntimeError("Refusing to install a landing bundle outside externalCache")
            shutil.copytree(source, destination, dirs_exist_ok=True)
            installed.append(source.name)
        invalidate_asset_catalog()

    return sorted(installed), sorted(unresolved)


def _integer(value, field: str, default: int) -> int:
    if value is None or value == "":
        return default
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise PageValidationError(f"{field} must be an integer timestamp") from exc


def _validate_label(labels: dict, key: str, required: bool = False) -> None:
    label = labels.get(key)
    if label is None:
        if required:
            raise PageValidationError(f"labels.{key} is required")
        return
    if not isinstance(label, dict):
        raise PageValidationError(f"labels.{key} must be an object")
    token = label.get("token")
    if token is not None and not isinstance(token, str):
        raise PageValidationError(f"labels.{key}.token must be a string")
    bundle = label.get("bundle")
    if not isinstance(bundle, dict) or not all(
        isinstance(value, str) for value in bundle.values()
    ):
        raise PageValidationError(f"labels.{key}.bundle must be a locale-to-text object")
    localized = list(bundle.values())
    if not localized and not str(token or "").strip():
        raise PageValidationError(
            f"labels.{key} must contain a token or localized text"
        )
    if required and localized and not all(value.strip() for value in localized):
        raise PageValidationError(f"labels.{key}.bundle must contain visible text")


def normalize_page(content: dict, page_type: str, sort_order=0) -> dict:
    """Validates and normalizes an admin page without discarding extra fields."""
    if not isinstance(content, dict):
        raise PageValidationError("content_json must be an object")
    if not isinstance(page_type, str) or page_type not in PAGE_TYPES:
        raise PageValidationError("page_type must be landing or maintenance")

    normalized = copy.deepcopy(content)
    template = str(normalized.get("template") or "").strip()
    allowed_templates = LANDING_TEMPLATES if page_type == "landing" else {MAINTENANCE_TEMPLATE}
    if template not in allowed_templates:
        choices = ", ".join(sorted(allowed_templates))
        raise PageValidationError(f"template must be one of: {choices}")
    normalized["template"] = template
    normalized["sortOrder"] = _integer(sort_order, "sort_order", 0)
    end_time_supplied = normalized.get("endTime") not in (None, "")
    normalized["startTime"] = _integer(normalized.get("startTime"), "startTime", 0)
    normalized["endTime"] = _integer(normalized.get("endTime"), "endTime", FOREVER_MS)
    if normalized["endTime"] and normalized["endTime"] <= normalized["startTime"]:
        raise PageValidationError("endTime must be later than startTime")
    if page_type == "maintenance":
        if normalized["startTime"] <= 0:
            raise PageValidationError("Maintenance startTime is required and is printed in the client")
        if not end_time_supplied or normalized["endTime"] <= 0:
            raise PageValidationError("Maintenance endTime is required and is printed in the client")

    labels = normalized.get("labels")
    if labels is None:
        labels = {}
    if not isinstance(labels, dict):
        raise PageValidationError("labels must be an object")
    normalized["labels"] = labels

    images = normalized.get("images")
    if images is None:
        images = {}
    if not isinstance(images, dict):
        raise PageValidationError("images must be an object")
    normalized["images"] = images

    actions = normalized.get("actions")
    if actions is None:
        actions = {}
    if not isinstance(actions, dict):
        raise PageValidationError("actions must be an object")
    normalized["actions"] = actions

    if page_type == "landing":
        _validate_label(labels, "GameText")
        background = images.get("GameBackground")
        if not isinstance(background, dict):
            raise PageValidationError("images.GameBackground is required")
        locale_map = background.get("localeImageMap")
        if not isinstance(locale_map, dict) or not locale_map:
            raise PageValidationError("images.GameBackground.localeImageMap is required")
        normalized_map = {}
        for locale, request_path in locale_map.items():
            if not isinstance(request_path, str) or not request_path.strip():
                raise PageValidationError("Every background locale needs an asset path")
            request_path = request_path.strip().replace("\\", "/")
            if "/" not in request_path:
                request_path = f"LandingPage/{request_path}"
            normalized_map[str(locale)] = request_path
        background["localeImageMap"] = normalized_map

        unknown_slots = set(actions).difference(ACTION_SLOTS)
        if unknown_slots:
            choices = ", ".join(sorted(ACTION_SLOTS))
            raise PageValidationError(f"Landing-page actions may only target: {choices}")
        active_slots = ACTION_SLOTS.intersection(actions)
        if len(active_slots) > 1:
            raise PageValidationError(
                "UpsellButton and CodeRedeemButton overlap in the client; choose only one"
            )
        if template.endswith("NoButtons") and active_slots:
            raise PageValidationError("The selected No Buttons template cannot contain a CTA action")
        if active_slots:
            # Both button prefabs contain a child GameObject named ButtonText
            # whose DynamicItemUILabel binding supplies the visible caption.
            # An action without this label produces a clickable blank button.
            _validate_label(labels, "ButtonText", required=True)
    else:
        _validate_label(labels, "NotificationBody", required=True)
        if actions:
            raise PageValidationError("SplashMaintenanceWindow does not contain action buttons")

    for slot, action in actions.items():
        if not isinstance(action, dict):
            raise PageValidationError(f"actions.{slot} must be an object")
        name = action.get("name")
        value = action.get("value")
        if name not in ACTION_NAMES or not isinstance(value, dict):
            raise PageValidationError(
                f"actions.{slot} must use NavigateToScene, NavigateToUrl, or NavigateToUrls"
            )
        if name == "NavigateToScene":
            scene = value.get("scene")
            if scene not in SUPPORTED_ACTION_SCENES:
                raise PageValidationError(
                    f"actions.{slot}.value.scene must be Shop, ShopCodeRedemption, Tournament, or Trade"
                )
        elif name == "NavigateToUrl":
            url = value.get("url")
            if not isinstance(url, str) or not url.strip():
                raise PageValidationError(f"actions.{slot}.value.url is required")
        elif name == "NavigateToUrls":
            urls = value.get("urls")
            if (
                not isinstance(urls, dict)
                or not all(isinstance(url, str) for url in urls.values())
                or not any(url.strip() for url in urls.values())
            ):
                raise PageValidationError(f"actions.{slot}.value.urls is required")

    return normalized
