import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

ASSETS_DIR = "spirit/assets"
TEMPLATES_DIR = "spirit/templates/cosmetic_templates"
CACHE_ROOT = "original_game_cache"

def discover_and_copy_templates():
    """
    Scans original_game_cache for the largest master bundles for cardSleeves,
    coins, and deckBoxes, and copies them to the templates folder.
    """
    bundle_cache_dir = None
    for root, dirs, _ in os.walk(CACHE_ROOT):
        if 'bundleCache' in dirs:
            bundle_cache_dir = os.path.join(root, 'bundleCache')
            break

    if not bundle_cache_dir:
        logging.warning(f"[Cosmetics] Could not find bundleCache inside '{CACHE_ROOT}'. Skipping template auto-discovery.")
        return False

    os.makedirs(TEMPLATES_DIR, exist_ok=True)

    categories = {
        'cardSleeves': 'cardSleeves.template',
        'coins': 'coins.template',
        'deckBoxes': 'deckBoxes.template',
        'packs': 'packs.template',
        'pcdBoxes': 'pcdBoxes.template',
        'avatar_thumbs': 'avatar_thumbs.template',
        'avatar': 'avatar.template'
    }

    success = True
    for pattern, template_name in categories.items():
        # Find all matching folders
        candidates = []
        for name in os.listdir(bundle_cache_dir):
            if pattern == 'avatar' and 'thumbs' in name.lower():
                continue
            if pattern.lower() in name.lower():
                folder_path = os.path.join(bundle_cache_dir, name)
                data_path = os.path.join(folder_path, "00000000000000000000000001000000", "__data")
                if os.path.exists(data_path):
                    candidates.append((data_path, os.path.getsize(data_path)))

        if not candidates:
            logging.warning(f"[Cosmetics] No master bundle candidates found for '{pattern}'.")
            success = False
            continue

        # Sort by size to get the master/largest bundle
        candidates.sort(key=lambda x: x[1], reverse=True)
        best_data_path, size = candidates[0]
        
        target_path = os.path.join(TEMPLATES_DIR, template_name)
        logging.info(f"[Cosmetics] Found master bundle for {pattern}: {os.path.dirname(best_data_path)} ({size / (1024*1024):.2f} MB)")
        shutil.copy2(best_data_path, target_path)
        logging.info(f"[Cosmetics] Successfully copied to template: {target_path}")

    return success

if __name__ == "__main__":
    discover_and_copy_templates()
