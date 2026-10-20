"""Reuse already-scripted effect code for a set's `unimplemented` stubs.

Two passes over the target set (reference = every other set folder):

1. Whole-card reprints: a stub whose name and gameplay signature (stats plus
   every attack/ability title, text, cost and damage; trainer/energy text)
   equal an implemented script is replaced by that script, keeping the stub's
   identity fields (guid, key, name, set, number, rarity...). References to the
   source GUID inside the copied code are rewritten to the stub's GUID.
2. Text matches: each remaining `effect=unimplemented` Attack/Ability whose
   normalized game text matches an implemented one gets that call's effect
   keywords, plus the module-level helpers and imports they need.

Damage-number check: when the reference attack's printed damage differs from
the target's and the copied effect hard-codes the reference damage (a literal
or `base=` that is not a number from the shared text), the match is reported as MISMATCH and left as a stub.

Scripts are parsed with `ast`, never imported.

Usage: python -m spirit.tools.reuse_effects --set BW11 --dry-run
       python -m spirit.tools.reuse_effects --set BW11 [--prefer BW,DV] [--no-whole-card]
"""
import argparse
import ast
import os
import re
import sys
from typing import Dict, List, Optional, Set, Tuple

CARDS_ROOT = os.path.join("spirit", "game", "scripts", "cards")
SKIP_DIRS = {"__pycache__"}
CARD_CLASSES = {"PokemonCardDef", "ItemCardDef", "SupporterCardDef", "StadiumCardDef",
                "PokemonToolCardDef", "EnergyCardDef", "FossilItemCardDef"}
IDENTITY = ("guid", "key", "name", "display_name", "searchable_by", "subtypes",
            "collector_number", "set_code", "rarity")
STATS = ("hp", "elements", "stage", "retreat_cost", "weakness_type", "resistance_type",
         "evolves_from", "is_special", "energy_type")
CORE = {"title", "game_text", "cost", "damage", "damage_operator", "ability_type"}


def norm(text) -> str:
    return re.sub(r"\W+", "", str(text).lower().replace("\u00e9", "e"))


def _lit(node, default=None):
    try:
        return ast.literal_eval(node) if node is not None else default
    except (ValueError, SyntaxError):
        return default


def _card_call(tree: ast.Module) -> Optional[ast.Call]:
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "card" \
                and isinstance(node.value, ast.Call):
            return node.value
    return None


def _is_unimpl(node) -> bool:
    return node is not None and ast.unparse(node) == "unimplemented"


def _ability_calls(tree: ast.AST) -> List[ast.Call]:
    return [n for n in ast.walk(tree) if isinstance(n, ast.Call)
            and getattr(n.func, "id", None) in ("Attack", "Ability")]


def _body_after_card(src: str) -> str:
    return src.split("\ncard = ")[-1]


class Script:
    def __init__(self, path: str):
        self.path = path
        with open(path, encoding="utf-8") as fh:
            self.src = fh.read()
        self.tree = ast.parse(self.src, path)
        self.card = _card_call(self.tree)
        self.set_code = os.path.basename(os.path.dirname(path))

    @property
    def stem(self) -> str:
        return os.path.splitext(os.path.basename(self.path))[0]

    def implemented(self) -> bool:
        return "unimplemented" not in _body_after_card(self.src)

    def signature(self) -> Optional[tuple]:
        if self.card is None or getattr(self.card.func, "id", None) not in CARD_CLASSES:
            return None
        kw = {k.arg: k.value for k in self.card.keywords}
        sig = [self.card.func.id, norm(_lit(kw.get("display_name"), ""))]
        sig += [(k, ast.unparse(kw[k])) for k in STATS if k in kw]
        if "game_text" in kw:
            sig.append(("gt", norm(ast.unparse(kw["game_text"]))))
        abilities = kw.get("abilities")
        for a in (abilities.elts if isinstance(abilities, ast.List) else []):
            ak = {k.arg: k.value for k in a.keywords}
            sig.append((getattr(a.func, "id", ""), norm(_lit(ak.get("title"), "")),
                        norm(_lit(ak.get("game_text"), "")),
                        ast.unparse(ak["cost"]) if "cost" in ak else "",
                        ast.unparse(ak["damage"]) if "damage" in ak else "0",
                        ast.unparse(ak["damage_operator"]) if "damage_operator" in ak else ""))
        return tuple(map(str, sig))


def all_scripts(exclude: str) -> List[Script]:
    out = []
    for code in sorted(os.listdir(CARDS_ROOT)):
        folder = os.path.join(CARDS_ROOT, code)
        if code in SKIP_DIRS or code == exclude or not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".py") and name != "__init__.py":
                try:
                    out.append(Script(os.path.join(folder, name)))
                except (SyntaxError, UnicodeDecodeError):
                    continue
    return out


def _rank(prefer: List[str]):
    def key(script: Script):
        preferred = any(script.set_code.upper().startswith(p.upper()) for p in prefer)
        return (0 if preferred else 1, len(script.src), script.path)
    return key


# ---------------------------------------------------------------- whole card

def copy_whole_card(stub: Script, ref: Script) -> str:
    out = ref.src
    for field in IDENTITY:
        mine = re.search(rf"^    {field}=.*$", stub.src, re.M)
        if mine and re.search(rf"^    {field}=.*$", out, re.M):
            out = re.sub(rf"^    {field}=.*$", lambda _m: mine.group(0), out, count=1, flags=re.M)
    old = re.search(r'^    guid="([^"]+)"', ref.src, re.M)
    new = re.search(r'^    guid="([^"]+)"', stub.src, re.M)
    if old and new:
        out = out.replace(old.group(1), new.group(1))
    return out


# --------------------------------------------------------------- text match

def _names(node) -> Set[str]:
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def _int_literals(node) -> Set[int]:
    return {n.value for n in ast.walk(node)
            if isinstance(n, ast.Constant) and type(n.value) is int}


class Transplant:
    """Effect keywords + helper definitions + imports taken from one reference call."""

    def __init__(self, ref: Script, call: ast.Call):
        self.ref = ref
        self.extra = [k for k in call.keywords if k.arg not in CORE]
        used: Set[str] = set()
        for k in self.extra:
            used |= _names(k.value)
        top = {}
        for node in ref.tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                top[node.name] = node
            elif isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) for t in node.targets) \
                    and node.targets[0].id != "card":
                top[node.targets[0].id] = node
        self.defs: Dict[str, str] = {}
        stack = list(used)
        all_used = set(used)
        while stack:
            name = stack.pop()
            if name in top and name not in self.defs:
                self.defs[name] = ast.get_source_segment(ref.src, top[name])
                inner = _names(top[name])
                all_used |= inner
                stack += list(inner)
        self.imports: List[Tuple[str, str, Optional[str]]] = []
        for node in ref.tree.body:
            if isinstance(node, ast.ImportFrom) and node.module:
                for alias in node.names:
                    if (alias.asname or alias.name) in all_used:
                        self.imports.append((node.module, alias.name, alias.asname))
        self.damage = _lit({k.arg: k.value for k in call.keywords}.get("damage"), 0)

    def hardcodes_damage(self, text: str) -> bool:
        """The source's printed damage appears as a literal in the copied code
        (and is not simply a number from the shared card text)."""
        if not self.damage or str(self.damage) in re.findall(r"\d+", text or ""):
            return False
        literals = set()
        for k in self.extra:
            literals |= _int_literals(k.value)
        for src in self.defs.values():
            literals |= _int_literals(ast.parse(src))
        return self.damage in literals

    def keyword_text(self, indent: str) -> str:
        return (",\n" + indent).join(f"{k.arg}={ast.unparse(k.value)}" for k in self.extra)


def apply_transplants(stub: Script, plans: List[Tuple[ast.keyword, Transplant]]) -> str:
    src = stub.src
    lines = src.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    for kw, plan in sorted(plans, key=lambda p: (p[0].value.lineno, p[0].value.col_offset), reverse=True):
        start = offsets[kw.lineno - 1] + kw.col_offset
        end = offsets[kw.value.end_lineno - 1] + kw.value.end_col_offset
        src = src[:start] + plan.keyword_text(" " * kw.col_offset) + src[end:]
    tree = ast.parse(src)
    defined = {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
    defined |= {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    imported = {(a.asname or a.name) for n in tree.body if isinstance(n, ast.ImportFrom) for a in n.names}
    imports: Dict[str, List[str]] = {}
    defs: List[str] = []
    for _kw, plan in plans:
        for module, name, asname in plan.imports:
            local = asname or name
            if local in imported or local in defined:
                continue
            imported.add(local)
            imports.setdefault(module, []).append(f"{name} as {asname}" if asname else name)
        for name, code in plan.defs.items():
            if name not in defined:
                defined.add(name)
                defs.append(code)
    head, tail = src.split("\ncard = ", 1)
    import_lines = "".join(f"from {m} import {', '.join(n)}\n" for m, n in imports.items())
    defs_text = ("\n\n" + "\n\n\n".join(defs) + "\n") if defs else ""
    return head.rstrip("\n") + "\n" + import_lines + defs_text + "\n\ncard = " + tail


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m spirit.tools.reuse_effects",
        description="Fill a set's unimplemented stubs from scripted cards with identical text "
                    "(whole-card reprints, then per-attack text matches); flags damage-number mismatches.")
    parser.add_argument("--set", required=True, help="Target set code / script folder, e.g. BW11.")
    parser.add_argument("--dry-run", action="store_true", help="Report the plan without writing files.")
    parser.add_argument("--prefer", default="",
                        help="Comma-separated set-code prefixes to prefer as sources "
                             "(default: the target's letter prefix, e.g. BW for BW11).")
    parser.add_argument("--no-whole-card", action="store_true", help="Skip the whole-card reprint pass.")
    parser.add_argument("--allow-mismatch", action="store_true",
                        help="Apply text matches even when the source hard-codes a different damage.")
    args = parser.parse_args(argv)
    folder = os.path.join(CARDS_ROOT, args.set)
    if not os.path.isdir(folder):
        parser.error(f"unknown set folder: {args.set}")
    prefer = [p for p in args.prefer.split(",") if p] or [re.match(r"[A-Za-z]*", args.set).group(0) or args.set]
    refs = [s for s in all_scripts(args.set) if s.card is not None]
    rank = _rank(prefer)

    targets = [Script(os.path.join(folder, n)) for n in sorted(os.listdir(folder))
               if n.endswith(".py") and n != "__init__.py"]
    targets = [t for t in targets if t.card is not None and not t.implemented()]
    whole = text_hits = mismatches = misses = 0

    if not args.no_whole_card:
        by_sig: Dict[tuple, List[Script]] = {}
        for ref in refs:
            if ref.implemented():
                sig = ref.signature()
                if sig:
                    by_sig.setdefault(sig, []).append(ref)
        remaining = []
        for stub in targets:
            match = by_sig.get(stub.signature())
            if not match:
                remaining.append(stub)
                continue
            ref = sorted(match, key=rank)[0]
            print(f"CARD     {stub.stem} <- {ref.set_code}/{ref.stem}")
            whole += 1
            if not args.dry_run:
                with open(stub.path, "w", encoding="utf-8") as fh:
                    fh.write(copy_whole_card(stub, ref))
        targets = remaining

    index: Dict[str, List[Tuple[Script, ast.Call]]] = {}
    for ref in refs:
        for call in _ability_calls(ref.tree):
            kw = {k.arg: k.value for k in call.keywords}
            effect = kw.get("effect", kw.get("passive"))
            if effect is None or _is_unimpl(effect) or "game_text" not in kw:
                continue
            text = _lit(kw["game_text"])
            if text:
                index.setdefault(norm(text), []).append((ref, call))

    for stub in targets:
        plans = []
        for call in _ability_calls(stub.tree):
            kw = {k.arg: k for k in call.keywords}
            if "effect" not in kw or not _is_unimpl(kw["effect"].value):
                continue
            title = _lit(kw["title"].value, "?")
            text = _lit(kw.get("game_text").value if "game_text" in kw else None, "")
            candidates = [(r, c) for r, c in index.get(norm(text), [])
                          if getattr(c.func, "id", None) == call.func.id]
            if not candidates:
                misses += 1
                print(f"MISS     {stub.stem} | {title} | {text[:90]}")
                continue
            ref, ref_call = sorted(candidates, key=lambda rc: rank(rc[0]))[0]
            plan = Transplant(ref, ref_call)
            if any(_is_unimpl(k.value) for k in plan.extra):
                misses += 1
                continue
            mine = _lit(kw["damage"].value, 0) if "damage" in kw else 0
            if mine != plan.damage and plan.hardcodes_damage(text) and not args.allow_mismatch:
                mismatches += 1
                print(f"MISMATCH {stub.stem} | {title} | source {ref.set_code}/{ref.stem} "
                      f"hard-codes {plan.damage}, this card prints {mine}")
                continue
            note = f" (damage {plan.damage} -> {mine})" if mine != plan.damage else ""
            print(f"TEXT     {stub.stem} | {title} <- {ref.set_code}/{ref.stem}: "
                  f"{plan.keyword_text(' ').replace(chr(10), ' ')[:110]}{note}")
            plans.append((kw["effect"], plan))
            text_hits += 1
        if plans and not args.dry_run:
            new_src = apply_transplants(stub, plans)
            with open(stub.path, "w", encoding="utf-8") as fh:
                fh.write(new_src)

    mode = "dry run" if args.dry_run else "applied"
    print(f"{args.set} ({mode}): {whole} whole-card copies, {text_hits} text matches, "
          f"{mismatches} damage mismatches skipped, {misses} unmatched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
