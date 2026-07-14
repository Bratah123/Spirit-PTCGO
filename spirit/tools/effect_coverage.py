"""Coverage report for `effect=unimplemented` card scripts. Parses scripts via
`ast` (never imports them: import/exec would trigger registration side effects)."""
import argparse
import ast
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

CARDS_ROOT = os.path.join("spirit", "game", "scripts", "cards")
SKIP_DIRS = {"__pycache__", "CUSTOM", "Free_Energy"}
CARD_CLASSES = {
    "PokemonCardDef", "ItemCardDef", "SupporterCardDef",
    "StadiumCardDef", "PokemonToolCardDef", "EnergyCardDef",
    "FossilItemCardDef",
}
ABILITY_CALL_NAMES = {"Attack", "Ability"}

# (category, compiled pattern); first match wins.
TRIAGE_RULES: List[Tuple[str, "re.Pattern"]] = [
    ("coin-flip", re.compile(r"flip")),
    ("lost-zone", re.compile(r"lost zone")),
    ("special-condition", re.compile(r"asleep|paralyzed|confused|burned|poisoned")),
    ("search-draw", re.compile(r"search your deck|put it into your hand|into your hand")),
    ("search-draw", re.compile(r"draw")),
    ("shuffle", re.compile(r"shuffle")),
    ("switching", re.compile(r"switch|new active")),
    ("counters", re.compile(r"damage counter")),
    ("damage-mod", re.compile(r"more damage|less damage|takes .* less|does .* more")),
    ("heal", re.compile(r"heal")),
    ("discard", re.compile(r"discard")),
    ("evolution", re.compile(r"evolve")),
    ("energy", re.compile(r"energy")),
    ("repeatable-ability", re.compile(r"as often as you like")),
    ("prizes", re.compile(r"prize")),
]


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip().lower()


def triage(signature: Tuple[str, ...]) -> str:
    joined = " ".join(signature)
    for category, pattern in TRIAGE_RULES:
        if pattern.search(joined):
            return category
    return "other"


@dataclass
class ScriptInfo:
    path: str
    set_code: str
    card_name: str
    collector_number: Optional[int]
    card_class: str
    is_stub: bool
    signature: Tuple[str, ...]


@dataclass
class WorkItem:
    card_name: str
    signature: Tuple[str, ...]
    card_class: str
    category: str = field(init=False)
    scripts: List[ScriptInfo] = field(default_factory=list)

    def __post_init__(self):
        self.category = triage(self.signature)

    @property
    def script_count(self) -> int:
        return len(self.scripts)

    def to_dict(self) -> dict:
        covered = [{"set": s.set_code, "number": s.collector_number} for s in self.scripts]
        return {
            "card_name": self.card_name,
            "card_class": self.card_class,
            "category": self.category,
            "signature": list(self.signature),
            "script_count": self.script_count,
            "covered": covered,
        }


def _str_const(node: Optional[ast.expr]) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _is_unimplemented(node: Optional[ast.expr]) -> bool:
    return isinstance(node, ast.Name) and node.id == "unimplemented"


def _find_card_call(tree: ast.Module) -> Optional[ast.Call]:
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Name) and call.func.id in CARD_CLASSES:
                return call
    return None


def _call_kwargs(call: ast.Call, positional_names: List[str]) -> Dict[str, ast.expr]:
    """Merges positional args (by name, per the callee's signature) with keywords."""
    args: Dict[str, ast.expr] = {}
    for i, arg in enumerate(call.args):
        if i < len(positional_names):
            args[positional_names[i]] = arg
    for kw in call.keywords:
        if kw.arg:
            args[kw.arg] = kw.value
    return args


def parse_script(path: str, set_code: str) -> Optional[ScriptInfo]:
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as exc:
        print(f"warning: failed to parse {path}: {exc}", file=sys.stderr)
        return None

    call = _find_card_call(tree)
    if call is None or not isinstance(call.func, ast.Name):
        print(f"warning: no recognized card definition in {path}", file=sys.stderr)
        return None
    card_class = call.func.id

    card_kwargs = _call_kwargs(call, ["guid", "key", "name", "collector_number", "set_code", "rarity"])
    is_stub = _is_unimplemented(card_kwargs.get("effect"))

    unimplemented_texts: List[str] = []
    for node in ast.walk(call):
        if node is call:
            continue
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ABILITY_CALL_NAMES:
            ability_kwargs = _call_kwargs(node, ["title", "game_text"])
            if _is_unimplemented(ability_kwargs.get("effect")):
                is_stub = True
                text = _str_const(ability_kwargs.get("game_text")) or ""
                unimplemented_texts.append(normalize_text(text))

    stem = os.path.splitext(os.path.basename(path))[0]
    if "_" in stem:
        card_name, num_str = stem.rsplit("_", 1)
    else:
        card_name, num_str = stem, ""
    try:
        collector_number = int(num_str)
    except ValueError:
        collector_number = None

    signature = tuple(sorted(unimplemented_texts))
    return ScriptInfo(
        path=path,
        set_code=set_code,
        card_name=card_name,
        collector_number=collector_number,
        card_class=card_class,
        is_stub=is_stub,
        signature=signature,
    )


def scan_cards(cards_root: str = CARDS_ROOT, only_set: Optional[str] = None) -> List[ScriptInfo]:
    infos: List[ScriptInfo] = []
    if not os.path.isdir(cards_root):
        return infos
    for set_code in sorted(os.listdir(cards_root)):
        set_dir = os.path.join(cards_root, set_code)
        if not os.path.isdir(set_dir) or set_code in SKIP_DIRS:
            continue
        if only_set and set_code != only_set:
            continue
        for filename in sorted(os.listdir(set_dir)):
            if not filename.endswith(".py") or filename == "__init__.py":
                continue
            info = parse_script(os.path.join(set_dir, filename), set_code)
            if info:
                infos.append(info)
    return infos


def group_work_items(infos: List[ScriptInfo]) -> List[WorkItem]:
    groups: Dict[Tuple[str, Tuple[str, ...]], WorkItem] = {}
    for info in infos:
        if not info.is_stub:
            continue
        key = (info.card_name, info.signature)
        item = groups.get(key)
        if item is None:
            item = WorkItem(card_name=info.card_name, signature=info.signature, card_class=info.card_class)
            groups[key] = item
        item.scripts.append(info)
    return list(groups.values())


def print_summary(infos: List[ScriptInfo], work_items: List[WorkItem]):
    by_set: Dict[str, List[ScriptInfo]] = defaultdict(list)
    for info in infos:
        by_set[info.set_code].append(info)

    print(f"{'SET':<10}{'TOTAL':>8}{'STUBS':>8}{'DONE':>8}{'% DONE':>9}")
    total_all = stubs_all = 0
    for set_code in sorted(by_set):
        scripts = by_set[set_code]
        total = len(scripts)
        stubs = sum(1 for s in scripts if s.is_stub)
        done = total - stubs
        pct = (done / total * 100) if total else 0.0
        print(f"{set_code:<10}{total:>8}{stubs:>8}{done:>8}{pct:>8.1f}%")
        total_all += total
        stubs_all += stubs
    done_all = total_all - stubs_all
    pct_all = (done_all / total_all * 100) if total_all else 0.0
    print("-" * 43)
    print(f"{'TOTAL':<10}{total_all:>8}{stubs_all:>8}{done_all:>8}{pct_all:>8.1f}%")

    print()
    print(f"{'CATEGORY':<20}{'WORK ITEMS':>12}{'SCRIPTS':>10}")
    by_category: Dict[str, List[WorkItem]] = defaultdict(list)
    for item in work_items:
        by_category[item.category].append(item)
    for category in sorted(by_category, key=lambda c: -sum(i.script_count for i in by_category[c])):
        items = by_category[category]
        print(f"{category:<20}{len(items):>12}{sum(i.script_count for i in items):>10}")


def print_top(work_items: List[WorkItem], n: int):
    print()
    print(f"Top {n} work items by scripts covered:")
    ranked = sorted(work_items, key=lambda i: -i.script_count)[:n]
    for item in ranked:
        sets = sorted({s.set_code for s in item.scripts})
        print(f"  {item.script_count:>4}x  [{item.category:<18}] {item.card_name}  ({', '.join(sets)})")


def write_json(work_items: List[WorkItem], path: str):
    data = [item.to_dict() for item in sorted(work_items, key=lambda i: -i.script_count)]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Report effect=unimplemented coverage across card scripts.")
    parser.add_argument("--json", help="Write the full work-item list to this JSON path.")
    parser.add_argument("--set", help="Only scan this set code (e.g. SWSH8).")
    parser.add_argument("--top", type=int, help="Print the N work items covering the most scripts.")
    args = parser.parse_args()

    infos = scan_cards(only_set=args.set)
    work_items = group_work_items(infos)

    print_summary(infos, work_items)
    if args.top:
        print_top(work_items, args.top)
    if args.json:
        write_json(work_items, args.json)
        print(f"\nWrote {len(work_items)} work items to {args.json}")


if __name__ == "__main__":
    main()
