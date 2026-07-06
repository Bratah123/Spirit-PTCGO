import os
import json
import sys

# Paths
SETS_JSON_PATH = os.path.join("spirit", "database", "json_data", "sets.json")
CARDS_DIR = os.path.join("spirit", "game", "scripts", "cards")

def diagnose():
    if not os.path.exists(SETS_JSON_PATH):
        print(f"Error: {SETS_JSON_PATH} not found.")
        return

    # Load sets
    with open(SETS_JSON_PATH, "r") as f:
        sets_data = json.load(f)
    
    set_names = {s["name"] for s in sets_data}
    set_ext_ids = {s["externalId"] for s in sets_data}

    print(f"Loaded {len(set_names)} unique set names from sets.json")

    # Scan card scripts
    card_sets = set()
    for root, _, files in os.walk(CARDS_DIR):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    for line in lines:
                        if "set_code=" in line:
                            # Extract set code
                            parts = line.split("set_code=")
                            if len(parts) > 1:
                                val = parts[1].strip().split(",")[0].strip("\"'")
                                card_sets.add(val)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

    print(f"Found {len(card_sets)} unique set_codes used in card scripts: {sorted(list(card_sets))}")
    
    missing_from_names = card_sets - set_names
    print(f"Set codes used in cards but NOT matching any 'name' in sets.json:")
    for ms in sorted(list(missing_from_names)):
        matching_ext = [s for s in sets_data if s["externalId"] == ms]
        if matching_ext:
            print(f"  - {ms} (Exists as externalId in sets.json under name: '{matching_ext[0]['name']}')")
        else:
            print(f"  - {ms} (NOT found in sets.json at all!)")

if __name__ == "__main__":
    diagnose()
