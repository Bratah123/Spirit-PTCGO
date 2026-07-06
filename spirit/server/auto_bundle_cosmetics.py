import os
import shutil
import logging
import copy
from PIL import Image
import UnityPy

from spirit import config

logging.basicConfig(level=logging.INFO)

ASSETS_DIR = "spirit/assets"
TEMPLATES_DIR = "spirit/templates/cosmetic_templates"
BUNDLE_CACHE_DIR = os.path.join(ASSETS_DIR, "bundleCache")

def compile_cosmetic_bundle(category, custom_dir, template_file, target_bundle_folder, prefix):
    """
    Loads the original template, dynamically clones new Texture2D slots for each custom PNG,
    injects them without overwriting or losing any original game cosmetics, updates
    the AssetBundle container with client-prefixed paths, and compresses the final bundle via LZ4.
    """
    template_path = os.path.join(TEMPLATES_DIR, template_file)
    if not os.path.exists(template_path):
        logging.warning(f"[Cosmetics] Template '{template_path}' not found. Cannot compile {category}.")
        return False

    os.makedirs(custom_dir, exist_ok=True)
    custom_pngs = [f for f in os.listdir(custom_dir) if f.endswith(".png")]

    output_dir = os.path.join(BUNDLE_CACHE_DIR, target_bundle_folder, "00000000000000000000000001000000")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "__data")

    # Only compile or copy if the template or custom PNG files are newer than the output file
    max_mtime = os.path.getmtime(template_path)
    for png in custom_pngs:
        png_path = os.path.join(custom_dir, png)
        max_mtime = max(max_mtime, os.path.getmtime(png_path))

    if os.path.exists(output_path):
        output_mtime = os.path.getmtime(output_path)
        if output_mtime >= max_mtime:
            logging.info(f"[Cosmetics] {category} bundle is up-to-date. Skipping compilation to preserve stable version in manifest.")
            return True

    # If there are no custom PNGs, copy the master template directly (zero-cost original fallback)
    if not custom_pngs:
        logging.info(f"[Cosmetics] No custom assets for {category}. Copying master template directly...")
        shutil.copy2(template_path, output_path)
        return True

    logging.info(f"[Cosmetics] Compiling {category} bundle with {len(custom_pngs)} custom textures (Dynamic Appending)...")

    # Load the template with UnityPy
    env = UnityPy.load(template_path)
    asset = env.assets[0]

    # Find a Texture2D object to act as our clone prototype
    prototype_id = None
    prototype_obj = None
    for pid, obj in asset.objects.items():
        if obj.type.name == "Texture2D":
            prototype_id = pid
            prototype_obj = obj
            break

    if not prototype_obj:
        logging.error(f"[Cosmetics] Could not find any Texture2D prototype in {template_file}!")
        return False

    prototype_read = prototype_obj.read()
    logging.info(f"[Cosmetics] Using PathID {prototype_id} ('{prototype_read.m_Name}') as prototype slot.")

    # Locate the AssetBundle object to update its container mapping later
    asset_bundle_obj = None
    for obj in asset.objects.values():
        if obj.type.name == "AssetBundle":
            asset_bundle_obj = obj
            break

    if not asset_bundle_obj:
        logging.error(f"[Cosmetics] Could not find AssetBundle object in template {template_file}!")
        return False

    asset_bundle_data = asset_bundle_obj.read()

    # Find the original AssetInfo corresponding to the prototype PathID
    proto_info = None
    for name, info in asset_bundle_data.m_Container:
        if info.asset.m_PathID == prototype_id:
            proto_info = info
            break

    if not proto_info:
        logging.error(f"[Cosmetics] Could not find AssetBundle container entry for prototype PathID {prototype_id}!")
        return False

    existing_textures = {}
    for pid, obj in asset.objects.items():
        if obj.type.name == "Texture2D":
            existing_textures[obj.read().m_Name.lower()] = obj

    # Perform dynamic appending for each custom PNG
    new_mappings = []
    for png_file in custom_pngs:
        png_path = os.path.join(custom_dir, png_file)
        custom_name = os.path.splitext(png_file)[0].lower() # logical asset names are lowercase in client

        if custom_name in existing_textures:
            try:
                replace_obj = existing_textures[custom_name]
                replace_read = replace_obj.read()
                with Image.open(png_path) as img:
                    if img.width != replace_read.m_Width or img.height != replace_read.m_Height:
                        replace_img = img.resize((replace_read.m_Width, replace_read.m_Height), Image.Resampling.LANCZOS)
                    else:
                        replace_img = img.copy()
                    replace_read.image = replace_img
                    replace_obj.save_typetree(replace_read)
                logging.info(f"[Cosmetics] Replaced template texture '{custom_name}' in-place")
            except Exception as e:
                logging.error(f"[Cosmetics] Failed to replace template texture '{custom_name}': {e}")
            continue

        # Create a unique new PathID
        new_path_id = max(asset.objects.keys()) + 1

        try:
            # 1. Clone the prototype ObjectReader
            cloned_obj = copy.copy(prototype_obj)
            cloned_obj.path_id = new_path_id
            
            # Put it into the SerializedFile dictionary
            asset.objects[new_path_id] = cloned_obj

            # 2. Update the cloned texture with our custom PNG data
            read_obj = cloned_obj.read()
            with Image.open(png_path) as img:
                target_width = prototype_read.m_Width
                target_height = prototype_read.m_Height
                
                # Resize if dimensions differ to ensure perfect texture formatting
                if img.width != target_width or img.height != target_height:
                    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                else:
                    resized_img = img.copy()

                read_obj.m_Name = custom_name
                read_obj.image = resized_img
                cloned_obj.save_typetree(read_obj)

            # 3. Create a cloned AssetInfo pointing to the new PathID
            new_info = copy.copy(proto_info)
            new_info.asset = copy.copy(proto_info.asset)
            new_info.asset.m_PathID = new_path_id

            # Add prefixed entry and raw entry to the container maps
            if prefix:
                new_mappings.append((f"{prefix}/{custom_name}", new_info))
                new_mappings.append((f"{prefix}//{custom_name}", new_info))
                # Add full URL container aliases to allow the client to resolve HTTP URL strings in AssetBundle-mode seamlessly
                for base_url in {config.HTTP_BASE_URL, "http://127.0.0.1:8000"}:
                    new_mappings.append((f"{base_url}/products/{custom_name}.png", new_info))
                    new_mappings.append((f"{base_url}/products/{custom_name}", new_info))
                    new_mappings.append((f"{prefix}/{base_url}/products/{custom_name}.png", new_info))
                    new_mappings.append((f"{prefix}/{base_url}/products/{custom_name}", new_info))
                    new_mappings.append((f"{prefix}//{base_url}/products/{custom_name}.png", new_info))
                    new_mappings.append((f"{prefix}//{base_url}/products/{custom_name}", new_info))
            new_mappings.append((custom_name, new_info))

            logging.info(f"[Cosmetics] Dynamically appended '{custom_name}' at PathID {new_path_id}")

        except Exception as e:
            logging.error(f"[Cosmetics] Failed to dynamically append '{png_file}': {e}")

    # 4. Save all new mappings into the AssetBundle container (appending without overwriting)
    try:
        asset_bundle_data.m_Container.extend(new_mappings)
        asset_bundle_obj.save_typetree(asset_bundle_data)
        logging.info(f"[Cosmetics] AssetBundle container appended with {len(new_mappings)} new mapping routes.")
    except Exception as e:
        logging.error(f"[Cosmetics] Failed to update AssetBundle container with appended mappings: {e}")

    # 5. Serialize the expanded, LZ4-compressed bundle back to disk
    with open(output_path, "wb") as f:
        f.write(env.file.save(packer="lz4"))
    
    logging.info(f"[Cosmetics] Successfully compiled expanded bundle at: {output_path}")
    return True

def compile_all_cosmetics():
    """Compiles cardSleeves, coins, deckBoxes, packs, and pcdBoxes using dynamic appending."""
    # 1. Card Sleeves
    compile_cosmetic_bundle(
        category="Sleeves",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_sleeves"),
        template_file="cardSleeves.template",
        target_bundle_folder="en_US_cardSleeves",
        prefix="cardSleeves"
    )

    # 2. Coins
    compile_cosmetic_bundle(
        category="Coins",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_coins"),
        template_file="coins.template",
        target_bundle_folder="en_US_coins",
        prefix="coins"
    )

    # 3. Deck Boxes
    compile_cosmetic_bundle(
        category="Deck Boxes",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_deckboxes"),
        template_file="deckBoxes.template",
        target_bundle_folder="en_US_deckBoxes",
        prefix="deckBoxes"
    )

    # 4. Booster Packs
    compile_cosmetic_bundle(
        category="Booster Packs",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_packs"),
        template_file="packs.template",
        target_bundle_folder="en_US_packs",
        prefix="packs"
    )

    # 5. Theme Decks (PCDs)
    compile_cosmetic_bundle(
        category="Theme Decks (PCDs)",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_pcds"),
        template_file="pcdBoxes.template",
        target_bundle_folder="en_US_pcdBoxes",
        prefix="pcdBoxes"
    )

    # 6. Avatars
    compile_cosmetic_bundle(
        category="Avatars",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_avatars"),
        template_file="avatar.template",
        target_bundle_folder="en_US_avatar_1_CR72_14",
        prefix="avatar"
    )

    # 7. Avatar Thumbs
    compile_cosmetic_bundle(
        category="Avatar Thumbs",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_avatar_thumbs"),
        template_file="avatar_thumbs.template",
        target_bundle_folder="en_US_avatar_thumbs_1_CR72_5",
        prefix="avatar_thumbs"
    )

    # 8. GX Token
    compile_cosmetic_bundle(
        category="GX Token",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_gxtoken"),
        template_file="GXToken.template",
        target_bundle_folder="en_US_GXToken_CRR59_5",
        prefix="gxtoken"
    )

    # 9. VStar Token
    compile_cosmetic_bundle(
        category="VStar Token",
        custom_dir=os.path.join(ASSETS_DIR, "products", "custom_vstartoken"),
        template_file="VSTARToken.template",
        target_bundle_folder="en_US_VSTARToken_CRR86_3",
        prefix="vstartoken"
    )

if __name__ == "__main__":
    compile_all_cosmetics()
