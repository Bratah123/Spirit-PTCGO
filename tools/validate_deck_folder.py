#!/usr/bin/env python3
"""Check every deck in spirit/tools/DECKS against this client's card catalog.

A deck imports only if every (set, collector number) it lists exists in
spirit/game/scripts/cards, so this reports which saved lists are usable and
which cards are missing (older sets, promos, typos).

Usage:
    python tools/validate_deck_folder.py             # problems only + summary
    python tools/validate_deck_folder.py --ok        # also list the clean decks
    python tools/validate_deck_folder.py --move-bad  # park them in unsupported/
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import convert_deck  # noqa: E402

from spirit.game.scripts.cards import loader  # noqa: E402
from spirit.game.attributes import AttrID  # noqa: E402
from spirit.game.content.starter import SET_CODE_MAP  # noqa: E402


def display(card):
    d = card.display_name
    if isinstance(d, str) and d:
        return d
    raw = str(card.get_attribute_value(AttrID.NAME))
    if raw.startswith('{"id": "'):
        return raw.split('"')[3]
    return raw


def norm(s: str) -> str:
    return s.lower().replace(" ", "").replace("'", "").replace("-", "")


def build_index():
    index = {}
    names = {}
    for card in loader.load_all():
        number = str(card.get_attribute_value(AttrID.COLLECTOR_NUMBER) or "").strip()
        index[(card.key.upper(), number)] = card
        names.setdefault(norm(display(card)), card)
    return index, names


def card_rows(path: Path):
    return convert_deck.parse_card_lines(path.read_text(encoding="utf-8-sig"))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dir", default=str(convert_deck.DECKS_DIR))
    ap.add_argument("--ok", action="store_true", help="also list clean decks")
    ap.add_argument("--move-bad", action="store_true",
                    help="move decks with missing cards into <dir>/unsupported/")
    args = ap.parse_args(argv)

    index, names = build_index()
    files = sorted(Path(args.dir).glob("*.txt"))
    clean, dirty = [], {}

    for path in files:
        problems = []
        for section, count, name, set_code, number in card_rows(path):
            if set_code and number:
                local = SET_CODE_MAP.get(set_code.upper(), set_code.upper())
                if (local, number) not in index:
                    problems.append(f"{name} ({set_code} {number})")
            elif section == "energy":
                if norm(name) not in names:
                    problems.append(f"{name} (no set/number)")
            else:
                problems.append(f"{name} (no set code)")
        if problems:
            uniq = []
            for p in problems:
                if p not in uniq:
                    uniq.append(p)
            dirty[path.name] = uniq
        else:
            clean.append(path.name)

    for deck, cards in dirty.items():
        print(f"[BAD] {deck}")
        for c in cards:
            print(f"        ! {c}")
    if args.ok:
        for deck in clean:
            print(f"[OK ] {deck}")
    if args.move_bad and dirty:
        target = Path(args.dir) / "unsupported"
        target.mkdir(parents=True, exist_ok=True)
        moved = 0
        for deck in dirty:
            src = Path(args.dir) / deck
            if src.exists():
                src.replace(target / deck)
                moved += 1
        print(f"\nmoved {moved} deck(s) to {target}")

    print(f"\n{len(clean)} clean / {len(dirty)} with missing cards "
          f"/ {len(files)} total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
