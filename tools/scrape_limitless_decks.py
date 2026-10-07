#!/usr/bin/env python3
"""Fetch top decklists from play.limitlesstcg.com and save them for the client.

For every archetype on https://play.limitlesstcg.com/decks?format=ss this takes
the *first* (best finishing) list, grabs the exact text behind the site's
"Copy to Clipboard" button, converts it to the format the old client imports,
and writes it to spirit/tools/DECKS/<first Pokemon>.txt.

Variants of the same run:
    python tools/scrape_limitless_decks.py --combine --all-lists --out DIR
        # with the site's "Combine related deck variants" checkbox on: fetch
        # EVERY decklist of every archetype (all Best Finishes rows) and write
        # them into one folder per archetype under DIR:
        #   DIR/<Archetype>/01 <first Pokemon> - <player>.txt ...
        # nothing is written for archetypes whose decks are already on disk
        # (use --force to overwrite).

Usage:
    python tools/scrape_limitless_decks.py --limit 3      # trial run
    python tools/scrape_limitless_decks.py                # everything
    python tools/scrape_limitless_decks.py --only dragapult-vmax,zacian-v
    python tools/scrape_limitless_decks.py --dry-run      # parse, don't write
    python tools/scrape_limitless_decks.py --combine --all-lists \
        --out spirit/tools/DECKS_combined --delay 0.3
"""
import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import convert_deck  # noqa: E402  (same folder)

# Player/tournament names carry accents the console codepage cannot encode;
# never let a print() abort a long scrape.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

BASE = "https://play.limitlesstcg.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ARCHETYPE_RE = re.compile(r'<td><a href="/decks/([a-z0-9-]+)\?format=[^"]+">([^<]+)</a></td>')
LIST_RE = re.compile(r'href="(/tournament/[^"]+/decklist)"')
CLIPBOARD_RE = re.compile(r"const decklist = `(.*?)`", re.DOTALL)
# Best-Finishes rows carry their metadata as data-* attributes.
ROW_RE = re.compile(r'<tr\s+((?:data-[\w-]+="[^"]*"\s*)+)>(.*?)</tr>', re.DOTALL)
ATTR_RE = re.compile(r'(data-[\w-]+)="([^"]*)"')
BAD_CHARS = re.compile(r'[\\/:*?"<>|\x00-\x1f]')


def fetch(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Language": "en-US,en;q=0.9"})
    for attempt in (0, 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return ""
            if attempt:
                raise
        except urllib.error.URLError:
            if attempt:
                raise
        time.sleep(2)
    return ""


def safe(text: str, limit: int = 70) -> str:
    """Filesystem-safe single path component."""
    text = BAD_CHARS.sub("_", re.sub(r"\s+", " ", text).strip(" ."))
    return text[:limit].rstrip(" .") or "deck"


def combine_query(fmt: str, combine: bool) -> str:
    return f"?format={fmt}" + ("&combine=true" if combine else "")


def archetypes(fmt: str, combine: bool = False):
    html = fetch(f"{BASE}/decks{combine_query(fmt, combine)}")
    seen = set()
    for slug, name in ARCHETYPE_RE.findall(html):
        if slug in seen:
            continue
        seen.add(slug)
        yield slug, name.strip()


def finish_rows(fmt: str, slug: str, combine: bool = False) -> list:
    """[(decklist_href, player, tournament), ...] from an archetype's
    Best Finishes table, deduped, best finish first."""
    page = fetch(f"{BASE}/decks/{slug}{combine_query(fmt, combine)}")
    if not page:
        return []
    rows, seen = [], set()
    for attrs, body in ROW_RE.findall(page):
        m = LIST_RE.search(body)
        if not m or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        meta = dict(ATTR_RE.findall(attrs))
        rows.append((m.group(1),
                     meta.get("data-player", "").strip(),
                     meta.get("data-tournament", "").strip()))
    if not rows:  # layout fallback: plain deduped hrefs, no metadata
        for href in LIST_RE.findall(page):
            if href not in seen:
                seen.add(href)
                rows.append((href, "", ""))
    return rows


def deck_clip(href: str) -> str:
    """Clipboard text of one decklist detail page ('' when not found)."""
    detail = fetch(f"{BASE}{href}")
    if not detail:
        return ""
    m = CLIPBOARD_RE.search(detail)
    return m.group(1) if m else ""


def unique_path(name: str, slug: str) -> Path:
    path = convert_deck.DECKS_DIR / f"{name}.txt"
    if not path.exists():
        return path
    return convert_deck.DECKS_DIR / f"{name} ({slug}).txt"


def unique_folder(root: Path, label: str, slug: str) -> Path:
    """<root>/<label>, disambiguated with the slug when another archetype
    already owns that name (identity recorded in <folder>/.slug)."""
    folder = root / safe(label)
    marker = folder / ".slug"
    if marker.exists() and marker.read_text(encoding="utf-8").strip() != slug:
        return root / f"{safe(label)} ({slug})"
    return folder


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--format", default="ss", help="limitless format id (default: ss)")
    ap.add_argument("--limit", type=int, default=0, help="stop after N archetypes")
    ap.add_argument("--only", default="", help="comma-separated slugs to fetch")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds between requests")
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    ap.add_argument("--dry-run", action="store_true", help="parse only, write nothing")
    ap.add_argument("--combine", action="store_true",
                    help="site's 'Combine related deck variants' checkbox")
    ap.add_argument("--all-lists", action="store_true",
                    help="fetch every decklist of an archetype, not just the best")
    ap.add_argument("--per", type=int, default=0,
                    help="with --all-lists: take at most N lists per archetype")
    ap.add_argument("--out", default="",
                    help="foldered output root: <out>/<Archetype>/<NN ...>.txt "
                         "(default: flat spirit/tools/DECKS, best list only)")
    args = ap.parse_args(argv)

    only = {s.strip() for s in args.only.split(",") if s.strip()}
    rows = [(s, n) for s, n in archetypes(args.format, args.combine)]
    if only:
        rows = [(s, n) for s, n in rows if s in only]
    elif args.limit:
        rows = rows[:args.limit]
    print(f"{len(rows)} archetype(s) to fetch")

    foldered = bool(args.out)
    out_root = Path(args.out) if foldered else None
    if foldered and not args.dry_run:
        out_root.mkdir(parents=True, exist_ok=True)
    saved, skipped, failed = [], [], []
    for i, (slug, label) in enumerate(rows, 1):
        try:
            entries = finish_rows(args.format, slug, args.combine)
        except Exception as e:  # keep going, report at the end
            failed.append(f"{slug}: fetch error {e}")
            continue
        if not entries:
            failed.append(f"{slug}: no decklists found")
            continue
        if not args.all_lists:
            entries = entries[:1]
        if args.per:
            entries = entries[:args.per]
        folder = None
        if foldered:
            folder = unique_folder(out_root, label, slug)
            marker = folder / ".slug"
            if not args.dry_run and not marker.exists():
                folder.mkdir(parents=True, exist_ok=True)
                marker.write_text(slug, encoding="utf-8")
        print(f"{i:>3}. {label:<28} {len(entries)} list(s)"
              + (f" -> {folder.name}/" if folder else ""))
        for j, (href, player, tournament) in enumerate(entries, 1):
            try:
                raw = deck_clip(href)
            except Exception as e:
                failed.append(f"{slug}: {href}: fetch error {e}")
                continue
            if not raw:
                failed.append(f"{slug}: {href}: no clipboard text")
                continue
            converted, warns, counts, total = convert_deck.convert(raw)
            name = convert_deck.first_pokemon_name(converted) or "deck"
            if foldered:
                title = " - ".join(x for x in (player, tournament) if x)
                stem = f"{j:02d} {name}" + (f" - {title}" if title else "")
                path = folder / (safe(stem, 100) + ".txt")
            else:
                path = unique_path(name, slug)
            note = f"     {j:>2}. {player or '?':<20} {counts['pokemon']}/" \
                   f"{counts['trainer']}/{counts['energy']} = {total}"
            if total != 60:
                note += "  ! total != 60"
            print(note)
            for w in warns:
                print(f"          ! {w}")
            if path.exists() and not args.force:
                skipped.append(str(path))
                time.sleep(args.delay)
                continue
            if not args.dry_run:
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(converted)
            saved.append(str(path))
            time.sleep(args.delay)

    print(f"\nsaved {len(saved)}, skipped {len(skipped)} existing, failed {len(failed)}")
    for f in failed:
        print(f"  ! {f}")
    if args.dry_run:
        print("(dry run - nothing written)")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
