"""Check card scripts' printed numbers against pokemon-tcg-data JSON.

Cards are matched by GUID (import_set derives it from the JSON card id), so
file names and accent handling don't matter; scripts carrying another GUID
(e.g. original client GUIDs) fall back to a collector-number match. Per card it compares:
  * collector number (subset numbers such as RC1 use import_set's mapping),
  * HP, retreat cost, attack count, and per attack name / damage / energy count,
  * explicit `base=` in damage_per / flip_damage / bonus_if effects of "+"
    or plain attacks against the printed damage (copied effects often keep
    the source card's base).

Usage: python -m spirit.tools.numcheck --set BW11 [--data path/to/bw11.json]
The JSON defaults to <data dir>/<set lower>.json; the data dir comes from
--data-dir, else $SPIRIT_TCG_DATA_DIR, else ../pokemon-tcg-data/cards/en.
--fix-base rewrites mismatched explicit base= values to the printed damage.
Exit status is 1 when any mismatch is found.
"""
import argparse
import ast
import json
import os
import re
import sys
from typing import Dict, List, Optional, Tuple

from spirit.tools import import_set

CARDS_ROOT = os.path.join("spirit", "game", "scripts", "cards")
DEFAULT_DATA_DIR = os.environ.get(
    "SPIRIT_TCG_DATA_DIR", os.path.join("..", "pokemon-tcg-data", "cards", "en"))
BASE_FNS = ("damage_per", "flip_damage", "bonus_if")


def _card_call(tree: ast.Module) -> Optional[ast.Call]:
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "card" \
                and isinstance(node.value, ast.Call):
            return node.value
    return None


def _lit(node, default=None):
    try:
        return ast.literal_eval(node) if node is not None else default
    except ValueError:
        return default


def load_scripts(set_code: str) -> Dict[str, Tuple[str, str, ast.Module]]:
    """{guid: (path, source, tree)} for every script in the set folder."""
    out = {}
    folder = os.path.join(CARDS_ROOT, set_code)
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".py") or name == "__init__.py":
            continue
        path = os.path.join(folder, name)
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        tree = ast.parse(src, path)
        call = _card_call(tree)
        if call is None:
            continue
        guid = _lit(next((k.value for k in call.keywords if k.arg == "guid"), None))
        if guid:
            out[guid.lower()] = (path, src, tree)
    return out


def _attacks(call: ast.Call) -> List[ast.Call]:
    kw = {k.arg: k.value for k in call.keywords}
    abilities = kw.get("abilities")
    if not isinstance(abilities, ast.List):
        return []
    return [a for a in abilities.elts if isinstance(a, ast.Call) and getattr(a.func, "id", "") == "Attack"]


def _energy_count(cost) -> int:
    if isinstance(cost, ast.Dict):
        return sum(_lit(v, 0) for v in cost.values)
    return 0


def base_mismatches(tree: ast.Module) -> List[Tuple[ast.Constant, int, str, str]]:
    """(base literal node, printed damage, attack title, helper) per mismatch."""
    found = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and getattr(node.func, "id", None) == "Attack"):
            continue
        kw = {k.arg: k.value for k in node.keywords}
        if "effect" not in kw or "damage" not in kw:
            continue
        if _lit(kw.get("damage_operator"), "") not in ("+", ""):
            continue
        printed = _lit(kw["damage"], 0)
        effect = kw["effect"]
        if not (isinstance(effect, ast.Call) and getattr(effect.func, "id", None) in BASE_FNS):
            continue
        if effect.func.id == "flip_damage" and any(k.arg == "per_heads" for k in effect.keywords):
            continue
        for k in effect.keywords:
            if k.arg == "base" and isinstance(k.value, ast.Constant) and k.value.value != printed:
                found.append((k.value, printed, _lit(kw.get("title"), "?"), effect.func.id))
    return found


def check_card(card: dict, path: str, tree: ast.Module) -> List[str]:
    call = _card_call(tree)
    kw = {k.arg: k.value for k in call.keywords}
    errs = []
    want_num = import_set.collector_number_int(card.get("number", "0"))
    if _lit(kw.get("collector_number")) != want_num:
        errs.append(f"collector_number {_lit(kw.get('collector_number'))} != {want_num}")
    if "Pok" not in card.get("supertype", ""):
        return errs
    if _lit(kw.get("hp")) != int(card.get("hp") or 0):
        errs.append(f"hp {_lit(kw.get('hp'))} != {card.get('hp')}")
    if _lit(kw.get("retreat_cost"), 0) != card.get("convertedRetreatCost", 0):
        errs.append(f"retreat {_lit(kw.get('retreat_cost'), 0)} != {card.get('convertedRetreatCost', 0)}")
    script_attacks = _attacks(call)
    data_attacks = card.get("attacks", [])
    if len(script_attacks) != len(data_attacks):
        errs.append(f"attack count {len(script_attacks)} != {len(data_attacks)}")
    for attack, data in zip(script_attacks, data_attacks):
        akw = {k.arg: k.value for k in attack.keywords}
        title = _lit(akw.get("title"), "?")
        damage = _lit(akw.get("damage"), 0)
        printed = int(re.sub(r"\D", "", data.get("damage", "")) or 0)
        if title != data.get("name"):
            errs.append(f"attack name {title!r} != {data.get('name')!r}")
        if damage != printed:
            errs.append(f"{title}: damage {damage} != {data.get('damage') or 0!r}")
        if _energy_count(akw.get("cost")) != data.get("convertedEnergyCost", 0):
            errs.append(f"{title}: energy {_energy_count(akw.get('cost'))} != {data.get('convertedEnergyCost', 0)}")
    for _node, printed, title, fn in base_mismatches(tree):
        errs.append(f"{title}: {fn} base {_node.value} != printed {printed}")
    return errs


def fix_bases(path: str, src: str, tree: ast.Module) -> int:
    edits = base_mismatches(tree)
    if not edits:
        return 0
    lines = src.splitlines(keepends=True)
    for node, printed, _title, _fn in sorted(edits, key=lambda e: (-e[0].lineno, -e[0].col_offset)):
        line = lines[node.lineno - 1]
        lines[node.lineno - 1] = line[:node.col_offset] + str(printed) + line[node.end_col_offset:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("".join(lines))
    return len(edits)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m spirit.tools.numcheck",
        description="Compare a set's card scripts (collector number, HP, retreat, attack "
                    "names/damage/energy, effect base= damage) with pokemon-tcg-data JSON.")
    parser.add_argument("--set", required=True, help="Set code / script folder, e.g. BW11.")
    parser.add_argument("--data", help="Card JSON for the set (default: <data dir>/<set lower>.json).")
    parser.add_argument("--data-dir", default=DEFAULT_DATA_DIR,
                        help="pokemon-tcg-data cards/en folder (default: $SPIRIT_TCG_DATA_DIR "
                             "or ../pokemon-tcg-data/cards/en).")
    parser.add_argument("--fix-base", action="store_true",
                        help="Rewrite mismatched explicit base= values to the printed damage.")
    args = parser.parse_args(argv)
    data_path = args.data or os.path.join(args.data_dir, f"{args.set.lower()}.json")
    if not os.path.exists(data_path):
        parser.error(f"card data not found: {data_path} (use --data or --data-dir)")
    if not os.path.isdir(os.path.join(CARDS_ROOT, args.set)):
        parser.error(f"unknown set folder: {args.set}")
    with open(data_path, encoding="utf-8") as fh:
        cards = json.load(fh)
    import_set.SUBSET_NUMBER_BASE = import_set.subset_number_base(cards)
    scripts = load_scripts(args.set)
    by_number = {}
    for key, (path, _src, tree) in scripts.items():
        num = _lit(next((k.value for k in _card_call(tree).keywords if k.arg == "collector_number"), None))
        by_number.setdefault(num, []).append(key)
    guids = {import_set.get_guid(c.get("id")).lower() for c in cards}
    bad = missing = fixed = 0
    for card in cards:
        guid = import_set.get_guid(card.get("id"))
        entry = scripts.pop(guid.lower(), None)
        label = f"{card.get('name')} #{card.get('number')}"
        if entry is None:
            want = import_set.collector_number_int(card.get("number", "0"))
            alt = [k for k in by_number.get(want, []) if k in scripts and k not in guids]
            if len(alt) == 1:
                entry = scripts.pop(alt[0])
                print(f"NOTE     {label}: matched {os.path.basename(entry[0])[:-3]} by number (script GUID {alt[0]})")
        if entry is None:
            print(f"MISSING  {label} (no script with guid {guid})")
            missing += 1
            continue
        path, src, tree = entry
        errs = check_card(card, path, tree)
        if errs:
            bad += 1
            print(f"MISMATCH {os.path.basename(path)[:-3]}: " + "; ".join(errs))
            if args.fix_base:
                fixed += fix_bases(path, src, tree)
    for path, _src, _tree in scripts.values():
        print(f"EXTRA    {os.path.basename(path)[:-3]} (no card in data)")
    print(f"{args.set}: {len(cards)} cards checked, {bad} mismatched, {missing} missing, "
          f"{len(scripts)} extra" + (f", {fixed} base= fixed" if args.fix_base else ""))
    return 1 if (bad or missing) else 0


if __name__ == "__main__":
    sys.exit(main())
