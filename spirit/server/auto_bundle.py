import os
import sys
import logging
import subprocess
import json
from PIL import Image, ImageDraw

from spirit.game.attributes import AttrID, TrainerType
from spirit.game.content.definitions import def_for
from spirit.game.scripts.cards import loader
from spirit.server.auto_bundle_cosmetics import compile_all_cosmetics
from spirit.server import dynamic_pages
from spirit.server import foil_mask_gen

ASSETS_DIR = "spirit/assets"
BUNDLE_CACHE_DIR = os.path.join(ASSETS_DIR, "bundleCache")
PIP_CACHE_DIR = os.path.join(BUNDLE_CACHE_DIR, "pips")
PIP_BORDER_DIR = os.path.join(BUNDLE_CACHE_DIR, "pips_borders")
CARDS_IMG_DIR = os.path.join(ASSETS_DIR, "cards")
CREATE_BUNDLE_SCRIPT = "re_tools/create_card_bundle.py"
# The default template used by create_card_bundle.py
DEFAULT_TEMPLATE = "spirit/templates/card_bundle"

def _generate_bundle(bundle_name, mapping, keep_size=False) -> int:
    bundle_path = os.path.join(BUNDLE_CACHE_DIR, bundle_name, "00000000000000000000000001000000", "__data")

    # Rebuild check
    map_path = "spirit/server/asset_map.json"
    rebuild_needed = not os.path.exists(bundle_path)

    if not rebuild_needed and os.path.exists(map_path):
        try:
            with open(map_path, "r") as f:
                amap = json.load(f)
            existing_assets = amap.get(bundle_name, [])
            for asset in mapping.keys():
                if asset not in existing_assets:
                    rebuild_needed = True
                    break
        except Exception:
            rebuild_needed = True

    # Rebuild when any source image is newer than the built bundle
    # (replaced card art, regenerated energy pips, new foil masks).
    if not rebuild_needed:
        bundle_mtime = os.path.getmtime(bundle_path)
        for src in mapping.values():
            if os.path.exists(src) and os.path.getmtime(src) > bundle_mtime:
                rebuild_needed = True
                break

    if rebuild_needed:
        logging.info(f"[AutoBundle] Generating bundle '{bundle_name}' ({len(mapping)} assets)...")
        temp_mapping_path = os.path.join(BUNDLE_CACHE_DIR, f"temp_{bundle_name}.json")
        with open(temp_mapping_path, "w") as f:
            json.dump(mapping, f)

        try:
            cmd = [
                sys.executable,
                CREATE_BUNDLE_SCRIPT,
                "--bundle", bundle_name,
                "--mapping", temp_mapping_path,
                "--template", DEFAULT_TEMPLATE
            ]
            if keep_size:
                cmd.append("--keep-size")
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                logging.error(f"[AutoBundle] Bundle build failed for {bundle_name}: {result.stderr[-500:]}")
            return 1
        finally:
            if os.path.exists(temp_mapping_path):
                os.remove(temp_mapping_path)
    return 0


def self_generate_set_bundle(set_code, set_mapping) -> int:
    return _generate_bundle(f"en_US_{set_code}", set_mapping)


# Foil-mask PNG suffix next to the card art -> the wp_ bundle kind the client
# requests it from ({SET}_wp_{kind}_Foil2/{num}; Reverse masks ride ph,
# Cracked_Ice pcd, second foil effects secondary).
FOIL_KIND_SUFFIXES = {
    "_foil": "std",
    "_foil_ph": "ph",
    "_foil_pcd": "pcd",
    "_foil_secondary": "secondary",
}
FOIL_SUFFIX_BY_KIND = {v: k for k, v in FOIL_KIND_SUFFIXES.items()}
FOIL_GEN_DIR = os.path.join(BUNDLE_CACHE_DIR, "foil_masks")


def ensure_generated_mask(art_png, set_code, asset_name, kind, style):
    """Path to a generated mask PNG, regenerating when the art or the
    generator changed; None on failure."""
    out_path = os.path.join(FOIL_GEN_DIR, set_code,
                            f"{asset_name}{FOIL_SUFFIX_BY_KIND[kind]}.png")
    if os.path.exists(out_path):
        m = os.path.getmtime(out_path)
        if (m >= os.path.getmtime(art_png)
                and m >= os.path.getmtime(foil_mask_gen.__file__)):
            return out_path
    logging.info(f"[AutoBundle] Generating foil mask {set_code}/{asset_name} ({kind}, {style})")
    return out_path if foil_mask_gen.generate_mask_png(art_png, out_path, style) else None


def generate_foil_bundles(foil_sets) -> int:
    """foil_sets: {set_code: {kind: {padded_num: png_path}}} -> built count."""
    count = 0
    for set_code, kinds in foil_sets.items():
        for kind, mapping in kinds.items():
            if mapping:
                count += _generate_bundle(
                    f"en_US_{set_code}_wp_{kind}_Foil2", mapping, keep_size=True
                )
    return count

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


def generate_energy_pip_png(png_path, set_code, asset_name, card_def, out_dir=None):
    """Crop the energypip, resize it, and put the border over it."""
    out_dir = out_dir or PIP_CACHE_DIR
    pip_path = os.path.join(out_dir, f"{set_code}_{asset_name}_energypip.png")
    icon_path = os.path.join(out_dir, f"{set_code}_{asset_name}_energyicon.png")
    if getattr(card_def, "inherits", None):
        # Gold should be added as a reprint so the pip defaults to
        # Common via "inherits" and uses its artwork.
        artwork_path = os.path.join(CARDS_IMG_DIR, f"{card_def.inherits}.png")
    else:
        artwork_path = png_path
    pip_border_path = os.path.join(PIP_BORDER_DIR, "energypip_border.png")
    icon_border_path = os.path.join(PIP_BORDER_DIR, "energyicon_border.png")

    stale_after = max(os.path.getmtime(artwork_path), os.path.getmtime(__file__))
    if (
        os.path.exists(pip_path)
        and os.path.exists(icon_path)
        and os.path.getmtime(pip_path) >= stale_after
        and os.path.getmtime(icon_path) >= stale_after
    ):
        return pip_path, icon_path

    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(artwork_path).convert("RGBA")
    artwork = img.crop((29, 140, 704, 662))
    crop_width, crop_height = artwork.size
    square_size = crop_height
    left_trim = (crop_width - square_size) // 2
    artwork = artwork.crop((left_trim, 0, left_trim + square_size, square_size))
    artwork = artwork.resize((117, 117), Image.Resampling.LANCZOS)
    mask = Image.new("L", (117, 117), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 116, 116), fill=255)
    artwork.putalpha(mask)

    # Generate the pip and icon.
    border_outputs = [(pip_border_path, pip_path), (icon_border_path, icon_path)]
    for border_path, output_path in border_outputs:
        output = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
        output.alpha_composite(artwork, (7, 5))
        border = Image.open(border_path).convert("RGBA")
        border = border.resize((122, 122), Image.Resampling.LANCZOS)
        output.alpha_composite(border, (2, 2))
        output.save(output_path)
    return pip_path, icon_path


def generate_tool_pip_png(png_path, set_code, asset_name, card_def, out_dir=None):
    """Crop the toolpip, resize it, and put the border over it."""
    out_dir = out_dir or PIP_CACHE_DIR
    pip_path = os.path.join(out_dir, f"{set_code}_{asset_name}_toolpip.png")
    if getattr(card_def, "inherits", None):
        # Gold should be added as a reprint so the pip defaults to
        # Common via "inherits" and uses its artwork with the appropriate border.
        artwork_path = os.path.join(CARDS_IMG_DIR, f"{card_def.inherits}.png")
        border_path = os.path.join(PIP_BORDER_DIR, "toolpip_gold_border.png")
    else:
        artwork_path = png_path
        border_path = os.path.join(PIP_BORDER_DIR, "toolpip_border.png")

    stale_after = max(os.path.getmtime(artwork_path), os.path.getmtime(__file__))
    if os.path.exists(pip_path) and os.path.getmtime(pip_path) >= stale_after:
        return pip_path

    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(artwork_path).convert("RGBA")
    artwork = img.crop((33, 120, 695, 548))
    artwork = artwork.resize((130, 85), Image.Resampling.LANCZOS)
    output = Image.new("RGBA", (138, 91), (0, 0, 0, 0))
    output.alpha_composite(artwork, (4, 3))
    # Resize and overlay the border.
    border = Image.open(border_path).convert("RGBA")
    border = border.resize((138, 91), Image.Resampling.LANCZOS)
    output.alpha_composite(border)
    output.save(pip_path)
    return pip_path

def check_and_generate_bundles(set_codes=None) -> int:
    """Builds missing/stale card bundles; an optional set filter skips cosmetics."""
    if set_codes is None:
        logging.info("[AutoBundle] Compiling cosmetic bundles...")
        try:
            compile_all_cosmetics()
        except Exception as e:
            logging.error(f"[AutoBundle] Failed to compile cosmetics: {e}")

        logging.info("[AutoBundle] Checking custom landing-page artwork...")
        try:
            dynamic_pages.compile_custom_landing_bundle()
        except Exception as e:
            logging.error(f"[AutoBundle] Failed to compile custom landing pages: {e}")
    else:
        set_codes = set(set_codes)

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
    foil_sets = {} # set_code -> {kind: {padded_num: png_path}}

    scripts_dir = loader.scripts_dir
    for root, _, files in os.walk(scripts_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                rel_dir = os.path.relpath(root, scripts_dir)
                base_name = file[:-3]
                png_path = os.path.join(CARDS_IMG_DIR, rel_dir, f"{base_name}.png")
                
                try:
                    file_path = os.path.join(root, file)
                    reference = os.path.splitext(os.path.relpath(file_path, scripts_dir))[0].replace(os.path.sep, "/")
                    declaration = loader.definitions.get(reference)
                    card_def = def_for(declaration.guid) if declaration is not None else None
                    # Re-executing scripts would replace resolved LEGEND/reprint definitions.
                    if card_def is None:
                        continue
                    set_code = card_def.set_code
                    if set_codes is not None and set_code not in set_codes:
                        continue
                    if getattr(card_def, "runtime_only", False):
                        image_name = getattr(card_def, "image_name", None)
                        if image_name and os.path.exists(png_path):
                            sets.setdefault(set_code, {})[image_name] = {image_name: png_path}
                        continue
                    asset_name = str(card_def.collector_number).zfill(3)
                    
                    if set_code not in sets:
                        sets[set_code] = {}
                    
                    card_assets = {asset_name: png_path}

                    # Foil masks live in their own {SET}_wp_{kind}_Foil2 bundles
                    # with textures named by padded number: the client's request
                    # "{SET}_wp_std_Foil2/127" strips to LoadAsset("127"), so a
                    # mask inside the set bundle can never be reached.
                    for suffix, kind in FOIL_KIND_SUFFIXES.items():
                        foil_png_path = os.path.join(CARDS_IMG_DIR, rel_dir, f"{base_name}{suffix}.png")
                        if os.path.exists(foil_png_path):
                            foil_sets.setdefault(set_code, {}).setdefault(kind, {})[asset_name] = foil_png_path

                    # foil-flagged cards with no extracted/hand-authored mask
                    # get a generated one (explicit _foil PNGs above win)
                    foil_def = getattr(card_def, "foil", None)
                    if foil_def is not None and os.path.exists(png_path):
                        style = foil_def.resolve_style(
                            getattr(card_def, "rarity", None),
                            getattr(card_def, "subtypes", None))
                        kinds = [foil_def.mask_kind()]
                        if len(foil_def.effects) > 1:
                            kinds.append("secondary")
                        for kind in kinds:
                            kind_map = foil_sets.setdefault(set_code, {}).setdefault(kind, {})
                            if asset_name in kind_map:
                                continue
                            gen_path = ensure_generated_mask(png_path, set_code, asset_name, kind, style)
                            if gen_path:
                                kind_map[asset_name] = gen_path

                    if _is_special_energy(card_def) and os.path.exists(png_path):
                        pip_path, icon_path = generate_energy_pip_png(png_path, set_code, asset_name, declaration)
                        if pip_path:
                            card_assets[f"{asset_name}_energypip"] = pip_path
                            card_assets[f"{asset_name}_energyicon"] = icon_path
                    elif _is_pokemon_tool(card_def) and os.path.exists(png_path):
                        pip_path = generate_tool_pip_png(png_path, set_code, asset_name, declaration)
                        if pip_path:
                            card_assets[f"{asset_name}_toolpip"] = pip_path

                    sets[set_code][asset_name] = card_assets

                except Exception as e:
                    logging.error(f"[AutoBundle] Failed to parse {file}: {e}")

    generated_count = 0

    for set_code, cards_dict in sets.items():
        # Merge all card assets for this set into one mapping
        set_mapping = {}
        for coll_num, card_assets in cards_dict.items():
            set_mapping.update(card_assets)

        generated_count += self_generate_set_bundle(set_code, set_mapping)

    generated_count += generate_foil_bundles(foil_sets)

    logging.info(f"[AutoBundle] Scan complete. Generated/Updated: {generated_count} set bundles.")
    return generated_count
