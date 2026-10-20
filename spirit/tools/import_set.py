import json
import os
import re
import sys
import uuid
import argparse
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
    # BW / HGSS-era print rarities (pokemon-tcg-data)
    "Rare Prime": "Rarities.RarePrime",
    "LEGEND": "Rarities.Legendary",
    "Rare ACE": "Rarities.Ace",
}

# JSON abilities[].type -> AbilityTypes enum ref for generated Ability(...)
ABILITY_TYPE_MAP = {
    "Poké-Body": "AbilityTypes.POKE_BODY",
    "Poké-Power": "AbilityTypes.POKE_POWER",
    "Ability": "AbilityTypes.POKE_ABILITY",
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
    return re.sub(r'[^a-zA-Z0-9]', '', name)

# Subset numbers (Radiant Collection "RC1"...) map past the set's highest
# numeric collector number so they never share a number (and art bundle
# asset name) with a main-set card. Set per import in main().
SUBSET_NUMBER_BASE = 0
SUBSET_RE = re.compile(r"^([A-Za-z]+)(\d+)$")

def collector_number_int(number: Any) -> int:
    """Unique int collector number: '57' -> 57, 'RC3' -> SUBSET_NUMBER_BASE + 3."""
    raw = str(number or "0").strip()
    if raw.isdigit():
        return int(raw)
    match = SUBSET_RE.match(raw)
    if match:
        return SUBSET_NUMBER_BASE + int(match[2])
    digits = re.sub(r"\D", "", raw)
    return int(digits) if digits else 0

def subset_number_base(cards: List[Dict[str, Any]]) -> int:
    """Highest plain-numeric collector number in the set (0 if none)."""
    nums = [int(c["number"]) for c in cards if str(c.get("number", "")).isdigit()]
    return max(nums, default=0)

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


def map_ability_type(raw_type: Optional[str]) -> str:
    """Map pokemon-tcg-data abilities[].type to an AbilityTypes.* source ref."""
    if not raw_type:
        return "AbilityTypes.POKE_ABILITY"
    return ABILITY_TYPE_MAP.get(raw_type, "AbilityTypes.POKE_ABILITY")


def map_rarity(raw_rarity: Optional[str]) -> str:
    """Map API rarity string to a Rarities.* source ref.

    Exact RARITY_MAP hits win. Fallback prefers Rare Holo EX over generic
    RareHolo so 'Rare Holo EX' never collapses to RareHolo when unmapped.
    """
    raw = raw_rarity or "Common"
    rarity = RARITY_MAP.get(raw)
    if rarity is not None:
        return rarity
    if raw == "Common":
        return "Rarities.Common"
    # Specific before generic: EX contains 'Holo' and must not become RareHolo.
    if "EX" in raw and "Holo" in raw:
        return "Rarities.RareHoloEX"
    if "Prime" in raw:
        return "Rarities.RarePrime"
    if raw == "LEGEND" or "LEGEND" in raw:
        return "Rarities.Legendary"
    if "ACE" in raw:
        return "Rarities.Ace"
    if "Secret" in raw:
        return "Rarities.RareSecret"
    if "Holo" in raw:
        return "Rarities.RareHolo"
    if "Rare" in raw:
        return "Rarities.Rare"
    return "Rarities.Common"


def build_abilities_src(card: Dict[str, Any]) -> tuple:
    """Renders abilities=[...] entries.

    Returns (source_lines, uses_unimplemented, uses_ability_types).
    """
    lines: List[str] = []
    uses_unimplemented = False
    uses_ability_types = False
    for ability in card.get("abilities", []):
        uses_unimplemented = True
        uses_ability_types = True
        ability_type = map_ability_type(ability.get("type"))
        lines.extend([
            "        Ability(",
            f"            title={py_str(fix_text(ability.get('name', '')))},",
            f"            game_text={py_str(fix_text(ability.get('text', '')))},",
            f"            ability_type={ability_type},",
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
            lines.append("            effect=unimplemented,")
            uses_unimplemented = True
        lines.append("        ),")
    return lines, uses_unimplemented, uses_ability_types

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
    name = card.get("name", "Unknown")
    number = collector_number_int(card.get("number", "0"))
    safe_name = clean_name(name)

    # Prepare script content
    rarity = map_rarity(card.get("rarity", "Common"))

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
        ability_lines, uses_unimplemented, uses_ability_types = build_abilities_src(card)

        imports = "PokemonCardDef, Attack, Ability"
        if uses_unimplemented:
            imports += ", unimplemented"
        attr_imports = "PokemonTypes, PokemonStage, Rarities"
        if uses_ability_types:
            attr_imports += ", AbilityTypes"

        content = f"""from spirit.game.data_utils import {imports}
from spirit.game.attributes import {attr_imports}

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
        # GAP notes (BW-era subtypes with no dedicated *CardDef subclass):
        # - Technical Machine: no TechnicalMachineCardDef; emit TrainerCardDef
        #   with TrainerType.TECHNICAL_MACHINE. Engine has the enum + AbilityTypes
        #   but no TM attach / granted-attack play path like DP-era TMs.
        # - ACE SPEC: no AceSpecCardDef; keep as Item/Tool/Stadium and leave
        #   'ACE SPEC' in subtypes (deck singleton enforced in validation).
        trainer_extra_kw = ""
        attr_imports = "Rarities"
        if "Supporter" in subtypes:
            trainer_class = "SupporterCardDef"
        elif "Stadium" in subtypes:
            trainer_class = "StadiumCardDef"
        elif any("Pok" in s and "Tool" in s for s in subtypes):
            trainer_class = "PokemonToolCardDef"
        elif "Technical Machine" in subtypes:
            trainer_class = "TrainerCardDef"
            trainer_extra_kw = "    trainer_type=TrainerType.TECHNICAL_MACHINE,\n"
            attr_imports = "Rarities, TrainerType"
        else:
            trainer_class = "ItemCardDef"

        ace_comment = ""
        if "ACE SPEC" in subtypes:
            ace_comment = (
                "    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only\n"
            )

        content = f"""from spirit.game.data_utils import {trainer_class}, unimplemented
from spirit.game.attributes import {attr_imports}

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
{trainer_extra_kw}{ace_comment}    effect=unimplemented
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

        content = f"""from spirit.game.data_utils import EnergyCardDef
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
    is_special={is_special}
)
"""

    return content or None

def process_card(card: Dict[str, Any], skip_existing: bool = False):
    filename = f"{clean_name(card.get('name', 'Unknown'))}_{card.get('number', '0')}"
    script_path = os.path.join(SCRIPT_OUTPUT_DIR, f"{filename}.py")
    asset_path = os.path.join(ASSET_OUTPUT_DIR, f"{filename}.png")

    content = render_script(card)
    if content:
        if skip_existing and os.path.exists(script_path):
            print(f"Skipping existing script: {script_path}")
        else:
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
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Do not overwrite card scripts that already exist (keeps hand-written BW stubs).",
    )
    args = parser.parse_args()

    JSON_PATH = args.json_path
    
    # Determine the set code
    if args.set_code:
        SET_CODE = args.set_code.upper()
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
    
    global SUBSET_NUMBER_BASE
    SUBSET_NUMBER_BASE = subset_number_base(cards)
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
        task = process_card(card, skip_existing=args.skip_existing)
        if task:
            download_tasks.append(task)
            
    print(f"Starting download of {len(download_tasks)} images...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url, path in download_tasks:
            executor.submit(download_image, url, path)

if __name__ == "__main__":
    main()
