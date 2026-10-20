import json
import os
import re
import sys
import uuid
import argparse
import unicodedata
import requests
from typing import Dict, Any, List, Optional
from concurrent.futures import ThreadPoolExecutor

# Configuration (defaults, will be dynamically overridden in main)
SET_CODE = "SWSH12"
JSON_PATH = f"spirit/game/scripts/cards/{SET_CODE}/swsh12.json"
SCRIPT_OUTPUT_DIR = f"spirit/game/scripts/cards/{SET_CODE}"
ASSET_OUTPUT_DIR = f"spirit/assets/cards/{SET_CODE}"

# Mapping for Rarities (Client-synced)
RARITY_MAP = {
    "Common": "Rarities.Common",
    "Uncommon": "Rarities.Uncommon",
    "Rare": "Rarities.Rare",
    "Rare Holo": "Rarities.RareHolo",
    "Rare Holo V": "Rarities.RareHoloV",
    "Rare Holo VMAX": "Rarities.RareHoloVMAX",
    "Rare Holo VSTAR": "Rarities.RareHoloVSTAR",
    "Rare Ultra": "Rarities.RareUltra",
    "Rare Secret": "Rarities.RareSecret",
    "Rare Rainbow": "Rarities.RareRainbow",
    "Rare Promo": "Rarities.RarePromo",
    "Promo": "Rarities.RarePromo",
    "Amazing Rare": "Rarities.Amazing", 
    "Radiant Rare": "Rarities.RareRadiant",
}

# Mapping for Types
TYPE_MAP = {
    "Grass": "PokemonTypes.GRASS",
    "Fire": "PokemonTypes.FIRE",
    "Water": "PokemonTypes.WATER",
    "Lightning": "PokemonTypes.LIGHTNING",
    "Psychic": "PokemonTypes.PSYCHIC",
    "Fighting": "PokemonTypes.FIGHTING",
    "Darkness": "PokemonTypes.DARKNESS",
    "Metal": "PokemonTypes.METAL",
    "Colorless": "PokemonTypes.COLORLESS",
    "Dragon": "PokemonTypes.DRAGON",
    "Fairy": "PokemonTypes.FAIRY",
}

# Mapping for Stages (Client-synced)
STAGE_MAP = {
    "Basic": "PokemonStage.BASIC",
    "Stage 1": "PokemonStage.STAGE1",
    "Stage 2": "PokemonStage.STAGE2",
    "Restored": "PokemonStage.RESTORED",
    "VMAX": "PokemonStage.VMAX",
    "VSTAR": "PokemonStage.VSTAR",
    "V-UNION": "PokemonStage.VUNION",
    "BREAK": "PokemonStage.BREAK",
    "MEGA": "PokemonStage.STAGE1",
}

def clean_name(name: str) -> str:
    """ASCII stem for filenames: Flabébé -> Flabebe, Pokémon -> Pokemon."""
    decomposed = unicodedata.normalize("NFKD", name or "")
    ascii_only = decomposed.encode("ascii", "ignore").decode("ascii")
    return re.sub(r'[^a-zA-Z0-9]', '', ascii_only)

# Unique int collector numbers. Spirit keys cards (art bundle asset names,
# "SET/number" deck refs, the starter index) by (set, int number), so every
# printed number of a set must map to its own int:
#   "57"   -> 57
#   "RC3"  -> highest plain number + 3   (prefix subsets: Radiant Collection,
#             promo "BW04"; a second prefix group continues after the first)
#   "28a"  -> after everything above, in data order (alternate prints)
# Any other collision also moves past the top. Set per import by
# set_numbering(cards); unknown numbers fall back to their digits.
NUMBER_MAP: Dict[str, int] = {}
SUBSET_RE = re.compile(r"^([A-Za-z]+)0*(\d+)$")

def assign_collector_numbers(cards: List[Dict[str, Any]]) -> Dict[str, int]:
    raws = [str(c.get("number", "0")).strip() for c in cards]
    out: Dict[str, int] = {}
    taken = set()
    for raw in raws:
        if raw.isdigit() and int(raw) not in taken:
            out[raw] = int(raw)
            taken.add(int(raw))
    offset = max(taken, default=0)
    groups: Dict[str, List[str]] = {}
    for raw in raws:
        match = SUBSET_RE.match(raw)
        if match and raw not in out:
            groups.setdefault(match[1].upper(), []).append(raw)
    for prefix, members in groups.items():
        top = offset
        for raw in members:
            value = offset + int(SUBSET_RE.match(raw)[2])
            if value in taken:
                continue
            out[raw] = value
            taken.add(value)
            top = max(top, value)
        offset = top
    top = max(taken, default=0)
    for raw in raws:
        if raw not in out:
            top += 1
            out[raw] = top
            taken.add(top)
    return out

def set_numbering(cards: List[Dict[str, Any]]) -> Dict[str, int]:
    global NUMBER_MAP
    NUMBER_MAP = assign_collector_numbers(cards)
    return NUMBER_MAP

def collector_number_int(number: Any) -> int:
    """Unique int collector number for a printed number (see NUMBER_MAP)."""
    raw = str(number or "0").strip()
    if raw in NUMBER_MAP:
        return NUMBER_MAP[raw]
    digits = re.sub(r"\D", "", raw)
    return int(digits) if digits else 0

def stub_header(reason: str, rules: Optional[List[str]] = None) -> str:
    """Module docstring marking a card (or effect) as intentionally stubbed."""
    lines = [
        "STUB: effect not implemented — do not guess mechanics.",
        reason,
    ]
    if rules:
        lines.append("")
        lines.append("Card text:")
        for rule in rules:
            text = fix_text(rule).strip()
            if text:
                lines.append(f"  - {text}")
    body = "\n".join(lines)
    return f'"""{body}\n"""\n\n'

def get_guid(card_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"spirit.ptcgo.{card_id}"))

def fix_text(s: str) -> str:
    """Repairs cp1252 mojibake from the source API (e.g. 'PokÃ©mon' -> 'Pokémon')."""
    try:
        return s.encode("cp1252").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s

def py_str(s: str) -> str:
    """A safe Python string literal for generated scripts."""
    return json.dumps(s)

def parse_damage(damage: str) -> tuple:
    """Splits an API damage string into (amount, operator): '50+' -> (50, '+')."""
    match = re.match(r"(\d+)\s*(.*)", damage or "")
    if not match:
        return 0, ""
    operator = match.group(2).replace("×", "x")
    return int(match.group(1)), operator

def build_cost_src(cost: List[str]) -> str:
    counts: Dict[str, int] = {}
    for type_name in cost or []:
        enum_ref = TYPE_MAP.get(type_name)
        if enum_ref:
            counts[enum_ref] = counts.get(enum_ref, 0) + 1
    return "{" + ", ".join(f"{k}: {v}" for k, v in counts.items()) + "}"

def build_abilities_src(card: Dict[str, Any]) -> tuple:
    """Renders the abilities=[...] entries; returns (source_lines, uses_unimplemented)."""
    lines: List[str] = []
    uses_unimplemented = False
    for ability in card.get("abilities", []):
        uses_unimplemented = True
        lines.extend([
            "        Ability(",
            f"            title={py_str(fix_text(ability.get('name', '')))},",
            f"            game_text={py_str(fix_text(ability.get('text', '')))},",
            "            # STUB: ability effect not implemented",
            "            effect=unimplemented,",
            "        ),",
        ])
    for attack in card.get("attacks", []):
        damage, operator = parse_damage(fix_text(attack.get("damage", "")))
        text = fix_text(attack.get("text", "") or "").strip()
        lines.append("        Attack(")
        lines.append(f"            title={py_str(fix_text(attack.get('name', '')))},")
        if text:
            lines.append(f"            game_text={py_str(text)},")
        lines.append(f"            cost={build_cost_src(attack.get('cost', []))},")
        if damage:
            lines.append(f"            damage={damage},")
        if operator:
            lines.append(f"            damage_operator={py_str(operator)},")
        if text:
            # Attacks with effect text stay playable (base damage only) until scripted.
            lines.append("            # STUB: attack effect not implemented")
            lines.append("            effect=unimplemented,")
            uses_unimplemented = True
        lines.append("        ),")
    return lines, uses_unimplemented

def download_image(url: str, filepath: str):
    if os.path.exists(filepath):
        return
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filepath}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

NAME_TO_CARD = {}
FAMILY_CACHE = {}

def get_family_id(card: Dict[str, Any]) -> Optional[int]:
    name = card.get("name")
    if name in FAMILY_CACHE:
        return FAMILY_CACHE[name]
    
    evolves_from = card.get("evolvesFrom")
    if not evolves_from or evolves_from not in NAME_TO_CARD:
        pokedex_nums = card.get("nationalPokedexNumbers", [])
        fid = pokedex_nums[0] if pokedex_nums else None
        FAMILY_CACHE[name] = fid
        return fid
    
    fid = get_family_id(NAME_TO_CARD[evolves_from])
    FAMILY_CACHE[name] = fid
    return fid

def render_script(card: Dict[str, Any]) -> Optional[str]:
    """Renders the card definition script source for one API card dict."""
    supertype = card.get("supertype", "")
    name = fix_text(card.get("name", "Unknown"))
    number_raw = card.get("number", "0")
    number = collector_number_int(number_raw)
    safe_name = clean_name(name)
    rules = [fix_text(r) for r in (card.get("rules") or []) if r]

    # Prepare script content
    raw_rarity = card.get("rarity", "Common")
    rarity = RARITY_MAP.get(raw_rarity, "Rarities.Common")

    # Fallback for complex rarity strings
    if rarity == "Rarities.Common" and raw_rarity != "Common":
        if "Holo" in raw_rarity:
            rarity = "Rarities.RareHolo"
        elif "Rare" in raw_rarity:
            rarity = "Rarities.Rare"

    guid = get_guid(card.get("id"))

    # Search keywords
    subtypes = card.get("subtypes", [])
    search_keywords = [name] + subtypes
    if "Pok" in supertype:
        search_keywords.append(safe_name)

    content = ""
    if "Pok" in supertype:
        hp = card.get("hp", "0")
        elements = [TYPE_MAP.get(t, "PokemonTypes.COLORLESS") for t in card.get("types", [])]
        stage = "PokemonStage.BASIC"
        for s in subtypes:
            if s in STAGE_MAP:
                stage = STAGE_MAP[s]
                break

        retreat_cost = card.get("convertedRetreatCost", 0)
        evolves_from = card.get("evolvesFrom")
        family_id = get_family_id(card)
        weaknesses = card.get("weaknesses") or []
        resistances = card.get("resistances") or []
        ability_lines, uses_unimplemented = build_abilities_src(card)

        imports = "PokemonCardDef, Attack, Ability"
        if uses_unimplemented:
            imports += ", unimplemented"

        header = ""
        if uses_unimplemented:
            header = stub_header(
                f"{name} ({SET_CODE} #{number_raw}): one or more attacks/abilities use "
                "effect=unimplemented until a matching prefab or known script exists."
            )

        content = f"""{header}from spirit.game.data_utils import {imports}
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="{guid}",
    key="{SET_CODE}",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.{safe_name}.Name",
    display_name="{name}",
    searchable_by={json.dumps(search_keywords)},
    subtypes={json.dumps(subtypes)},
    collector_number={number},
    set_code="{SET_CODE}",
    rarity={rarity},
    hp={hp},
    elements=[{", ".join(elements)}],
    stage={stage},
    retreat_cost={retreat_cost},
"""
        if weaknesses:
            weak_type = TYPE_MAP.get(weaknesses[0].get("type"))
            if weak_type:
                content += f"    weakness_type={weak_type},\n"

        if resistances:
            resist_type = TYPE_MAP.get(resistances[0].get("type"))
            if resist_type:
                content += f"    resistance_type={resist_type},\n"

        if evolves_from:
            content += f"    evolves_from=\"com.direwolfdigital.cake.data.archetypes.pokemon.{clean_name(evolves_from)}.Name\",\n"

        if family_id:
            content += f"    family_id={family_id},\n"

        if ability_lines:
            content += "    abilities=[\n" + "\n".join(ability_lines) + "\n    ],\n"

        content += ")"

    elif supertype == "Trainer":
        if "Supporter" in subtypes:
            trainer_class = "SupporterCardDef"
        elif "Stadium" in subtypes:
            trainer_class = "StadiumCardDef"
        elif any("Pok" in s and "Tool" in s for s in subtypes):
            trainer_class = "PokemonToolCardDef"
        else:
            trainer_class = "ItemCardDef"

        header = stub_header(
            f"{name} ({SET_CODE} #{number_raw}): trainer effect stubbed.",
            rules=rules,
        )
        content = f"""{header}from spirit.game.data_utils import {trainer_class}, unimplemented
from spirit.game.attributes import Rarities

card = {trainer_class}(
    guid="{guid}",
    key="{SET_CODE}",
    name="com.direwolfdigital.cake.data.archetypes.trainer.{safe_name}.Name",
    display_name="{name}",
    searchable_by={json.dumps(search_keywords)},
    subtypes={json.dumps(subtypes)},
    collector_number={number},
    set_code="{SET_CODE}",
    rarity={rarity},
    # STUB: trainer effect not implemented
    effect=unimplemented
)
"""
    elif supertype == "Energy":
        is_special = "Special" in subtypes
        energy_type = "PokemonTypes.COLORLESS"
        if not is_special:
            for t_name, t_enum in TYPE_MAP.items():
                if t_name in name:
                    energy_type = t_enum
                    break

        header = ""
        extra_lines = ""
        # Known special energy with no conditional text beyond provides.
        if name == "Double Colorless Energy":
            extra_lines = (
                "    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],\n"
            )
        elif is_special:
            header = stub_header(
                f"{name} ({SET_CODE} #{number_raw}): special energy provides/passive/attach "
                "rules stubbed until matched to a known energy pattern.",
                rules=rules,
            )
            extra_lines = "    # STUB: special energy mechanics not implemented\n"
        content = f"""{header}from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="{guid}",
    key="{SET_CODE}",
    name="{name}",
    display_name="{name}",
    searchable_by={json.dumps(search_keywords)},
    subtypes={json.dumps(subtypes)},
    collector_number={number},
    set_code="{SET_CODE}",
    rarity={rarity},
    energy_type={energy_type},
    is_special={is_special},
{extra_lines})
"""

    return content or None

def process_card(card: Dict[str, Any]):
    filename = f"{clean_name(card.get('name', 'Unknown'))}_{card.get('number', '0')}"
    script_path = os.path.join(SCRIPT_OUTPUT_DIR, f"{filename}.py")
    asset_path = os.path.join(ASSET_OUTPUT_DIR, f"{filename}.png")

    content = render_script(card)
    if content:
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(content)

    image_url = card.get("images", {}).get("large")
    if image_url:
        return (image_url, asset_path)
    return None

def main():
    global SET_CODE, JSON_PATH, SCRIPT_OUTPUT_DIR, ASSET_OUTPUT_DIR
    
    parser = argparse.ArgumentParser(description="Import a Pokemon TCG set from a JSON file.")
    parser.add_argument("json_path", nargs="?", default="spirit/game/scripts/cards/SWSH12/swsh12.json", help="Path to the TCG JSON file to import.")
    parser.add_argument("--set-code", help="The set code to use (defaults to upper case of JSON filename).")
    args = parser.parse_args()

    JSON_PATH = args.json_path
    
    # Determine the set code. Preserve caller casing when --set-code is given
    # (sets.json uses mixed-case names like TwentiethAnn).
    if args.set_code:
        SET_CODE = args.set_code
    else:
        # Get uppercase filename without extension
        SET_CODE = os.path.splitext(os.path.basename(JSON_PATH))[0].upper()
        
    SCRIPT_OUTPUT_DIR = f"spirit/game/scripts/cards/{SET_CODE}"
    ASSET_OUTPUT_DIR = f"spirit/assets/cards/{SET_CODE}"
    
    # Ensure directories exist
    os.makedirs(SCRIPT_OUTPUT_DIR, exist_ok=True)
    os.makedirs(ASSET_OUTPUT_DIR, exist_ok=True)

    print(f"Loading {JSON_PATH}...")
    if not os.path.exists(JSON_PATH):
        print(f"Error: JSON file not found at {JSON_PATH}")
        sys.exit(1)
        
    with open(JSON_PATH, "r") as f:
        cards = json.load(f)
    
    set_numbering(cards)
    numbers = [collector_number_int(c.get("number", "0")) for c in cards]
    if len(set(numbers)) != len(numbers):
        print("Error: collector numbers collide after subset mapping")
        sys.exit(1)

    # Build name map for family resolution
    for card in cards:
        if "Pok" in card.get("supertype", ""):
            NAME_TO_CARD[card.get("name")] = card

    print(f"Processing {len(cards)} cards...")
    download_tasks = []
    for card in cards:
        task = process_card(card)
        if task:
            download_tasks.append(task)
            
    print(f"Starting download of {len(download_tasks)} images...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url, path in download_tasks:
            executor.submit(download_image, url, path)

if __name__ == "__main__":
    main()
