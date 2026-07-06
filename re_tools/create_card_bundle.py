import os
import sys
import json
import re
import argparse
import copy
import hashlib

# Ensure UnityPy is available
try:
    import UnityPy
    from PIL import Image
except ImportError:
    print("Error: UnityPy or Pillow (PIL) not installed.")
    print("Please run: pip install UnityPy Pillow")
    sys.exit(1)

ASSET_MAP_PATH = "spirit/server/asset_map.json"
OUTPUT_DIR = "spirit/assets/bundleCache"

def create_card_set_bundle(png_mapping, template_path, target_bundle_name):
    """
    Creates a custom PTCGO AssetBundle for a SET of cards using Dynamic Appending.
    png_mapping: dict of {asset_name: png_path}
    """
    
    # 1. Resolve template data path
    data_path = template_path
    if os.path.isdir(template_path):
        for root, _, files in os.walk(template_path):
            if "__data" in files:
                data_path = os.path.join(root, "__data")
                break
    
    if not os.path.exists(data_path):
        print(f"Error: Template not found at {data_path}")
        return

    print(f"Loading template: {data_path}")
    env = UnityPy.load(data_path)
    
    def pad_to_square(img):
        width, height = img.size
        if width == height:
            return img
        
        new_size = max(width, height)
        bg_color = (0, 0, 0, 0) if img.mode == 'RGBA' else (0, 0, 0)
        padded_img = Image.new(img.mode, (new_size, new_size), bg_color)
        offset = ((new_size - width) // 2, (new_size - height) // 2)
        padded_img.paste(img, offset)
        return padded_img

    # We use the first texture in the template as a blueprint for format and settings
    prototype_obj = None
    for obj in env.objects:
        if obj.type.name == "Texture2D":
            prototype_obj = obj
            break
    
    if not prototype_obj:
        print("Error: No Texture2D found in template to use as prototype.")
        return

    proto_data = prototype_obj.read()
    target_size = (proto_data.m_Width, proto_data.m_Height)
    print(f"Prototype size: {target_size}")

    unique_prefix = target_bundle_name.replace(".unity3d", "")

    # Locate the AssetBundle object to update its container mapping later
    asset_bundle_obj = None
    for obj in env.objects:
        if obj.type.name == "AssetBundle":
            asset_bundle_obj = obj
            break

    if not asset_bundle_obj:
        print("Error: Could not find AssetBundle object in template.")
        return

    asset_bundle_data = asset_bundle_obj.read()

    # Find the original AssetInfo corresponding to the prototype PathID
    proto_info = None
    for name, info in asset_bundle_data.m_Container:
        if info.asset.m_PathID == prototype_obj.path_id:
            proto_info = info
            break

    if not proto_info:
        print(f"Error: Could not find AssetBundle container entry for prototype PathID {prototype_obj.path_id}")
        return

    asset = env.assets[0]
    next_path_id = max(asset.objects.keys()) + 1
    
    new_mappings = []
    appended_path_ids = set()

    # Process all custom pngs using dynamic appending
    for asset_name, png_path in png_mapping.items():
        if not os.path.exists(png_path):
            print(f"Warning: PNG not found: {png_path}")
            continue
            
        print(f"Processing asset: {asset_name} from {png_path}")
        try:
            img = Image.open(png_path)
            img_square = pad_to_square(img)
            resample_filter = getattr(Image, 'LANCZOS', getattr(Image, 'ANTIALIAS', 1))
            resized_img = img_square.resize(target_size, resample_filter)

            new_path_id = next_path_id
            next_path_id += 1
            appended_path_ids.add(new_path_id)

            # 1. Clone the prototype ObjectReader
            cloned_obj = copy.copy(prototype_obj)
            cloned_obj.path_id = new_path_id
            asset.objects[new_path_id] = cloned_obj

            # 2. Update the cloned texture with our custom PNG data
            read_obj = cloned_obj.read()
            read_obj.m_Name = asset_name
            read_obj.image = resized_img
            cloned_obj.save_typetree(read_obj)

            # 3. Create a cloned AssetInfo pointing to the new PathID
            new_info = copy.copy(proto_info)
            new_info.asset = copy.copy(proto_info.asset)
            new_info.asset.m_PathID = new_path_id

            # Set up variants for this card asset
            variants = [asset_name]
            # "072", "foil_072", "072_energypip" also map without leading zeros
            num_match = re.match(r'^(foil_)?(\d+)(_energypip|_toolpip)?$', asset_name)
            if num_match:
                short_num = num_match.group(2).lstrip("0") or "0"
                if short_num != num_match.group(2):
                    variants.append(
                        f"{num_match.group(1) or ''}{short_num}{num_match.group(3) or ''}"
                    )

            # Add prefixed entry and raw entry to the container maps
            for v in variants:
                new_mappings.append((v, new_info))
                
                # Also support set-prefixed variants (SWSH12/072)
                set_match = re.search(r'en_US_([A-Za-z0-9_]+)', target_bundle_name)
                if set_match:
                    set_code = set_match.group(1)
                    # Strip part number suffix (e.g. SWSH12_1 -> SWSH12)
                    set_code = re.sub(r'_\d+$', '', set_code)
                    new_mappings.append((f"{set_code}/{v}", new_info))
                    new_mappings.append((f"{set_code}_{v}", new_info))

            print(f"Dynamically appended card '{asset_name}' at PathID {new_path_id}")

        except Exception as e:
            print(f"Error appending card '{asset_name}': {e}")

    # 4. Rebuild the AssetBundle Container Map cleanly
    # Update AssetBundle container by removing original template Texture2D entries and keeping other assets
    original_non_textures = []
    for name, asset_info in asset_bundle_data.m_Container:
        # Check if this asset_info corresponds to an original Texture2D from the template
        is_template_tex = False
        for obj in env.objects:
            if obj.path_id == asset_info.asset.m_PathID and obj.type.name == "Texture2D":
                # Ensure it's not one of our newly appended PathIDs
                if obj.path_id not in appended_path_ids:
                    is_template_tex = True
                    break
        if not is_template_tex:
            # Keep original shader, material, or non-texture assets, prefixing them correctly
            unique_path = name
            if not name.startswith(unique_prefix) and "/" not in name:
                unique_path = f"{unique_prefix}/{name}"
            original_non_textures.append((unique_path, asset_info))

    asset_bundle_data.m_Container = original_non_textures + new_mappings
    asset_bundle_data.m_Name = unique_prefix
    asset_bundle_obj.save_typetree(asset_bundle_data)
    print(f"Updated AssetBundle container with {len(asset_bundle_data.m_Container)} entries (Dynamic Appending Complete).")

    # Save
    bundle_logical_name = target_bundle_name.replace(".unity3d", "")
    structure_path = os.path.join(OUTPUT_DIR, bundle_logical_name, "00000000000000000000000001000000")
    os.makedirs(structure_path, exist_ok=True)
    final_data_path = os.path.join(structure_path, "__data")
    
    # Ensure each master bundle has a unique CAB (SerializedFile) identifier to prevent Unity duplicate load errors
    old_cab = 'CAB-698f1293cb9396443b3f13ebe0cec855'
    h = hashlib.md5(target_bundle_name.encode('utf-8')).hexdigest()
    new_cab = f"CAB-{h}"
    if hasattr(env.file, 'files') and old_cab in env.file.files:
        env.file.files[new_cab] = env.file.files.pop(old_cab)
    if len(env.assets) > 0:
        env.assets[0].name = new_cab

    with open(final_data_path, "wb") as f:
        f.write(env.file.save(packer="lz4"))
    
    print(f"Successfully created SET bundle: {final_data_path}")
    
    # Update asset map for the whole set
    update_asset_map_bulk(bundle_logical_name, list(png_mapping.keys()))

def update_asset_map_bulk(bundle_name, asset_names):
    if not os.path.exists(ASSET_MAP_PATH):
        return
    try:
        with open(ASSET_MAP_PATH, "r") as f:
            amap = json.load(f)
        amap[bundle_name] = asset_names
        with open(ASSET_MAP_PATH, "w") as f:
            json.dump(amap, f)
        print(f"Updated asset_map.json for set '{bundle_name}' with {len(asset_names)} assets.")
    except Exception as e:
        print(f"Error updating asset_map.json: {e}")

def create_card_bundle(png_path, template_path, target_bundle_name, asset_name):
    # Backward compatibility for single card calls
    create_card_set_bundle({asset_name: png_path}, template_path, target_bundle_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reconstruct a custom card AssetBundle.")
    parser.add_argument("--bundle", help="The target bundle name (e.g., en_US_XY11)")
    parser.add_argument("--asset", help="The internal asset name (e.g., 072) (for single card mode)")
    parser.add_argument("--mapping", help="JSON mapping of {asset_name: png_path} for batch mode")
    parser.add_argument("--template", help="Path to template bundle",
                        default=r"spirit/templates/card_bundle")

    # This is for backward compatibility with the old positional argument style
    parser.add_argument("pos_png", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("pos_bundle", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("pos_asset", nargs="?", help=argparse.SUPPRESS)

    args = parser.parse_args()
    
    if args.mapping:
        with open(args.mapping, 'r') as f:
            mapping = json.load(f)
        create_card_set_bundle(mapping, args.template, args.bundle)
    elif args.png and args.bundle and args.asset:
        create_card_bundle(args.png, args.template, args.bundle, args.asset)
    elif args.pos_png and args.pos_bundle and args.pos_asset:
        # Fallback for old positional calls
        create_card_bundle(args.pos_png, args.template, args.pos_bundle, args.pos_asset)
    else:
        print("Error: Must provide either --mapping OR (--png, --bundle, and --asset)")
