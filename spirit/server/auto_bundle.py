import os
import sys
import logging
import subprocess
import json
import importlib.util
import math
from PIL import Image, ImageFilter

from spirit.game.attributes import AttrID, TrainerType
from spirit.game.scripts.cards import loader
from spirit.server.auto_bundle_cosmetics import compile_all_cosmetics

ASSETS_DIR = "spirit/assets"
BUNDLE_CACHE_DIR = os.path.join(ASSETS_DIR, "bundleCache")
PIP_CACHE_DIR = os.path.join(BUNDLE_CACHE_DIR, "pips")
CARDS_IMG_DIR = os.path.join(ASSETS_DIR, "cards")
CREATE_BUNDLE_SCRIPT = "re_tools/create_card_bundle.py"
# The default template used by create_card_bundle.py
DEFAULT_TEMPLATE = "spirit/templates/card_bundle"

def self_generate_set_bundle(set_code, set_mapping) -> int:
    # Bundle name (e.g., en_US_SWSH12)
    bundle_name = f"en_US_{set_code}"
    bundle_path = os.path.join(BUNDLE_CACHE_DIR, bundle_name, "00000000000000000000000001000000", "__data")
    
    # Rebuild check
    map_path = "spirit/server/asset_map.json"
    rebuild_needed = not os.path.exists(bundle_path)
    
    if not rebuild_needed and os.path.exists(map_path):
        try:
            with open(map_path, "r") as f:
                amap = json.load(f)
            existing_assets = amap.get(bundle_name, [])
            for asset in set_mapping.keys():
                if asset not in existing_assets:
                    rebuild_needed = True
                    break
        except:
            rebuild_needed = True

    # Rebuild when any source image is newer than the built bundle
    # (replaced card art, regenerated energy pips).
    if not rebuild_needed:
        bundle_mtime = os.path.getmtime(bundle_path)
        for src in set_mapping.values():
            if os.path.exists(src) and os.path.getmtime(src) > bundle_mtime:
                rebuild_needed = True
                break

    if rebuild_needed:
        logging.info(f"[AutoBundle] Generating master bundle '{bundle_name}' ({len(set_mapping)} assets)...")
        temp_mapping_path = os.path.join(BUNDLE_CACHE_DIR, f"temp_{set_code}.json")
        with open(temp_mapping_path, "w") as f:
            json.dump(set_mapping, f)
        
        try:
            cmd = [
                sys.executable,
                CREATE_BUNDLE_SCRIPT,
                "--bundle", bundle_name,
                "--mapping", temp_mapping_path,
                "--template", DEFAULT_TEMPLATE
            ]
            subprocess.run(cmd, capture_output=True, text=True)
            return 1
        finally:
            if os.path.exists(temp_mapping_path):
                os.remove(temp_mapping_path)
    return 0

def _is_special_energy(card_def) -> bool:
    spec = (getattr(card_def, "extra_attributes", None) or {}).get(
        str(AttrID.IS_SPECIAL_ENERGY.value)
    )
    return bool(spec and spec.get("value"))


def _is_pokemon_tool(card_def) -> bool:
    kind = (getattr(card_def, "extra_attributes", None) or {}).get(
        str(AttrID.TRAINER_TYPE.value)
    )
    return bool(kind) and kind.get("value") in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value
    )


def _detect_emblem_circle(img):
    """(cx, cy, r) of the special energy's circular emblem, or None.

    Hough-gradient vote on the art window: edge pixels vote along their
    gradient for circle centers; only centers near the art middle compete,
    and a radius bonus prefers the full ball over sharp inner details.
    """

    w, h = img.size
    # Art window of an energy card: skip border, title bar and text box.
    rx0, ry0 = int(w * 0.08), int(h * 0.13)
    rx1, ry1 = int(w * 0.92), int(h * 0.66)
    region = img.crop((rx0, ry0, rx1, ry1)).convert("L")

    ds = 150
    scale = ds / region.width
    resample = getattr(Image, "LANCZOS", getattr(Image, "ANTIALIAS", 1))
    small = region.resize((ds, max(3, int(region.height * scale))),
                          resample).filter(ImageFilter.GaussianBlur(1))
    sw, sh = small.size
    px = list(small.getdata())

    def p(x, y):
        return px[y * sw + x]

    edges = []
    for y in range(1, sh - 1):
        for x in range(1, sw - 1):
            gx = (p(x+1, y-1) + 2*p(x+1, y) + p(x+1, y+1)
                  - p(x-1, y-1) - 2*p(x-1, y) - p(x-1, y+1))
            gy = (p(x-1, y+1) + 2*p(x, y+1) + p(x+1, y+1)
                  - p(x-1, y-1) - 2*p(x, y-1) - p(x+1, y-1))
            mag = gx*gx + gy*gy
            if mag > 0:
                edges.append((x, y, gx, gy, mag))
    edges.sort(key=lambda e: -e[4])
    edges = edges[:max(1, len(edges) // 4)]

    rmin = max(6, int(min(sw, sh) * 0.16))
    rmax = int(min(sw, sh) * 0.60)
    acc = {}
    for x, y, gx, gy, mag in edges:
        norm = math.sqrt(gx*gx + gy*gy)
        ux, uy = gx / norm, gy / norm
        for r in range(rmin, rmax + 1, 2):
            for sgn in (1, -1):
                cx = int(round(x + sgn * ux * r))
                cy = int(round(y + sgn * uy * r))
                if 0 <= cx < sw and 0 <= cy < sh:
                    acc.setdefault((cx, cy), {})
                    acc[(cx, cy)][r] = acc[(cx, cy)].get(r, 0) + 1

    cx_lo, cx_hi = sw * 0.25, sw * 0.75
    cy_lo, cy_hi = sh * 0.15, sh * 0.85
    min_votes = len(edges) * 0.02
    best, best_weighted = None, -1
    for (cx, cy) in list(acc.keys()):
        if not (cx_lo <= cx <= cx_hi and cy_lo <= cy <= cy_hi):
            continue
        pooled = {}
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for r, v in acc.get((cx+dx, cy+dy), {}).items():
                    pooled[r] = pooled.get(r, 0) + v
        for r in pooled:
            score = pooled.get(r-2, 0) + pooled[r] + pooled.get(r+2, 0)
            weighted = score * (1 + 1.5 * r / rmax)
            if weighted > best_weighted and score >= min_votes:
                best, best_weighted = (cx, cy, r), weighted

    if best is None:
        return None
    inv = 1 / scale
    return (rx0 + best[0] * inv, ry0 + best[1] * inv, best[2] * inv)


def _generate_pip_png(png_path, set_code, asset_name, suffix, detect,
                      art_window=(0.12, 0.68), out_dir=None):
    out_dir = out_dir or PIP_CACHE_DIR
    out_path = os.path.join(out_dir, f"{set_code}_{asset_name}_{suffix}.png")
    # Regenerate when the source art OR this module (the crop logic) changes.
    stale_after = max(os.path.getmtime(png_path), os.path.getmtime(__file__))
    if os.path.exists(out_path) and os.path.getmtime(out_path) >= stale_after:
        return out_path
    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(png_path).convert("RGBA")
    w, h = img.size
    # Keep the crop inside the art window (title above, text box below).
    art_top, art_bottom = int(h * art_window[0]), int(h * art_window[1])
    found = _detect_emblem_circle(img) if detect else None
    if found:
        cx, cy, r = found
        side = int(2 * r * 1.16)
    else:
        cx, cy, side = w / 2, (art_top + art_bottom) / 2, art_bottom - art_top
    side = min(side, w, art_bottom - art_top)
    left = int(min(max(cx - side / 2, 0), w - side))
    top = int(min(max(cy - side / 2, art_top), art_bottom - side))
    img.crop((left, top, left + side, top + side)).save(out_path)
    return out_path


def generate_energy_pip_png(png_path, set_code, asset_name, out_dir=None):
    """Square crop around the card's circular emblem for the attachment pip.

    The in-match pip requests bundle asset "{set}/{num}_energypip" for special
    energies (EnergyPipTextureRenderer); without it the type symbol shows.
    """
    return _generate_pip_png(png_path, set_code, asset_name, "energypip",
                             detect=True, out_dir=out_dir)


def generate_tool_pip_png(png_path, set_code, asset_name, out_dir=None):
    """Art-window crop for an attached tool's pip.

    ToolPipTextureRenderer requests "{set}/{num}_toolpip" for every attached
    tool; without it the generic wrench icon shows. Tool art has no fixed
    emblem shape, so the crop is a centered window (no detection). The band
    0.21-0.51h is text-free on BOTH tool layouts: regular tools put the
    "Pokemon Tool" reminder box at ~0.52h, full-arts put it at ~0.14-0.20h.
    """
    return _generate_pip_png(png_path, set_code, asset_name, "toolpip",
                             detect=False, art_window=(0.21, 0.51),
                             out_dir=out_dir)


def check_and_generate_bundles() -> int:
    """
    Scans the loaded card scripts, groups them by set, and generates
    one Unity AssetBundle per set if missing or incomplete. Also compiles cosmetics.
    """
    logging.info("[AutoBundle] Compiling cosmetic bundles...")
    try:
        compile_all_cosmetics()
    except Exception as e:
        logging.error(f"[AutoBundle] Failed to compile cosmetics: {e}")

    logging.info("[AutoBundle] Checking for missing card AssetBundles...")
    
    if not os.path.exists(DEFAULT_TEMPLATE):
        logging.warning(f"[AutoBundle] Template not found: {DEFAULT_TEMPLATE}. Cannot auto-generate bundles.")
        return -1

    if not os.path.exists(BUNDLE_CACHE_DIR):
        os.makedirs(BUNDLE_CACHE_DIR, exist_ok=True)

    if not loader.cards:
        loader.load_all()

    # Group cards by set_code
    sets = {} # set_code -> {coll_num_str: {asset_name: png_path}}
    
    scripts_dir = loader.scripts_dir
    for root, _, files in os.walk(scripts_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                rel_dir = os.path.relpath(root, scripts_dir)
                base_name = file[:-3]
                png_path = os.path.join(CARDS_IMG_DIR, rel_dir, f"{base_name}.png")
                
                try:
                    file_path = os.path.join(root, file)
                    module_name = "autobundle_" + rel_dir.replace(os.path.sep, "_") + "_" + base_name
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    if spec is None or spec.loader is None: continue
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if not hasattr(module, 'card'): continue
                    
                    card_def = module.card
                    set_code = card_def.set_code
                    asset_name = str(card_def.collector_number).zfill(3)
                    
                    if set_code not in sets:
                        sets[set_code] = {}
                    
                    # Create a dict for this card slot to keep image and foil together
                    card_assets = {asset_name: png_path}
                    
                    foil_png_path = os.path.join(CARDS_IMG_DIR, rel_dir, f"{base_name}_foil.png")
                    if os.path.exists(foil_png_path):
                        card_assets[f"foil_{asset_name}"] = foil_png_path

                    if _is_special_energy(card_def) and os.path.exists(png_path):
                        pip_path = generate_energy_pip_png(png_path, set_code, asset_name)
                        if pip_path:
                            card_assets[f"{asset_name}_energypip"] = pip_path
                    elif _is_pokemon_tool(card_def) and os.path.exists(png_path):
                        pip_path = generate_tool_pip_png(png_path, set_code, asset_name)
                        if pip_path:
                            card_assets[f"{asset_name}_toolpip"] = pip_path

                    sets[set_code][asset_name] = card_assets

                except Exception as e:
                    logging.error(f"[AutoBundle] Failed to parse {file}: {e}")

    generated_count = 0

    for set_code, cards_dict in sets.items():
        # Merge all card assets (including foils) for this set into one mapping
        set_mapping = {}
        for coll_num, card_assets in cards_dict.items():
            set_mapping.update(card_assets)
            
        generated_count += self_generate_set_bundle(set_code, set_mapping)

    logging.info(f"[AutoBundle] Scan complete. Generated/Updated: {generated_count} set bundles.")
    return generated_count
