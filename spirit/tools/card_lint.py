"""Static and import-time lint for card scripts.

Per set it imports every card module and reports:
  * import failures (syntax errors, bad imports, exceptions at load),
  * global names a module references but never defines (typos, missing
    imports that only fail when the effect runs),
  * duplicate GUIDs (across all scanned sets) and duplicate collector
    numbers within one set (they collide in art bundles and deck refs;
    runtime-only definitions such as combined V-UNIONs are exempt).

Usage: python -m spirit.tools.card_lint --set BW10 [--set BW11 ...]
       python -m spirit.tools.card_lint --all
Exit status is 1 when any problem is found.
"""
import argparse
import ast
import builtins
import dis
import importlib
import os
import sys
import traceback
import types
from collections import defaultdict
from typing import Dict, Iterator, List, Optional, Tuple

CARDS_ROOT = os.path.join("spirit", "game", "scripts", "cards")
SKIP_DIRS = {"__pycache__"}


def set_codes(root: str = CARDS_ROOT) -> List[str]:
    return sorted(d for d in os.listdir(root)
                  if os.path.isdir(os.path.join(root, d)) and d not in SKIP_DIRS)


def script_paths(set_code: str, root: str = CARDS_ROOT) -> List[str]:
    folder = os.path.join(root, set_code)
    return sorted(os.path.join(folder, f) for f in os.listdir(folder)
                  if f.endswith(".py") and f != "__init__.py")


def module_name(path: str) -> str:
    return os.path.splitext(os.path.normpath(path))[0].replace(os.sep, ".")


def _code_objects(code: types.CodeType) -> Iterator[types.CodeType]:
    yield code
    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            yield from _code_objects(const)


def undefined_globals(path: str, namespace: dict) -> List[str]:
    """Global/name loads anywhere in the module that resolve to nothing."""
    with open(path, encoding="utf-8") as fh:
        top = compile(fh.read(), path, "exec")
    missing = set()
    for code in _code_objects(top):
        for ins in dis.get_instructions(code):
            if ins.opname in ("LOAD_GLOBAL", "LOAD_NAME") \
                    and ins.argval not in namespace and not hasattr(builtins, ins.argval):
                missing.add(ins.argval)
    return sorted(missing)


def identity(path: str) -> Tuple[Optional[str], Optional[int]]:
    """(guid, collector_number) read from the `card = XCardDef(...)` call."""
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), path)
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "card" \
                and isinstance(node.value, ast.Call):
            kw = {k.arg: k.value for k in node.value.keywords}
            guid = kw.get("guid")
            num = kw.get("collector_number")
            return (guid.value.lower() if isinstance(guid, ast.Constant) else None,
                    num.value if isinstance(num, ast.Constant) else None)
    return None, None


def lint_sets(codes: List[str], verbose: bool = False) -> int:
    problems = 0
    guid_owner: Dict[str, str] = {}
    for code in codes:
        paths = script_paths(code)
        numbers = defaultdict(list)
        failed = undefined = 0
        for path in paths:
            stem = os.path.splitext(os.path.basename(path))[0]
            try:
                guid, number = identity(path)
            except SyntaxError as exc:
                print(f"IMPORT-FAIL {code}/{stem}: {exc}")
                failed += 1
                continue
            if guid:
                if guid in guid_owner:
                    print(f"DUP-GUID    {code}/{stem} = {guid_owner[guid]} ({guid})")
                    problems += 1
                guid_owner.setdefault(guid, f"{code}/{stem}")
            try:
                module = importlib.import_module(module_name(path))
            except Exception as exc:  # noqa: BLE001 - report every load error
                print(f"IMPORT-FAIL {code}/{stem}: {exc!r}")
                if verbose:
                    traceback.print_exc()
                failed += 1
                continue
            # Runtime-only definitions (combined V-UNION) reuse a piece's number.
            if number is not None and not getattr(getattr(module, "card", None), "runtime_only", False):
                numbers[number].append(stem)
            missing = undefined_globals(path, module.__dict__)
            if missing:
                print(f"UNDEFINED   {code}/{stem}: {', '.join(missing)}")
                undefined += 1
        dups = {n: s for n, s in numbers.items() if len(s) > 1}
        for number, stems in sorted(dups.items()):
            print(f"DUP-NUMBER  {code} #{number}: {', '.join(stems)}")
        problems += failed + undefined + len(dups)
        print(f"{code}: {len(paths)} scripts, {failed} import failures, "
              f"{undefined} with undefined names, {len(dups)} duplicate numbers")
    return problems


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m spirit.tools.card_lint",
        description="Import every card script of a set and report load errors, "
                    "undefined global names, duplicate GUIDs and duplicate collector numbers.")
    parser.add_argument("--set", dest="sets", action="append", default=[],
                        help="Set code (folder under spirit/game/scripts/cards); repeatable.")
    parser.add_argument("--all", action="store_true", help="Lint every set folder.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print tracebacks for import failures.")
    args = parser.parse_args(argv)
    codes = set_codes() if args.all else args.sets
    if not codes:
        parser.error("give --set CODE (repeatable) or --all")
    unknown = [c for c in codes if not os.path.isdir(os.path.join(CARDS_ROOT, c))]
    if unknown:
        parser.error(f"unknown set folder(s): {', '.join(unknown)}")
    problems = lint_sets(codes, verbose=args.verbose)
    print(f"total problems: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
