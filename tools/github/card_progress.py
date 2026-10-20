"""Card support progress: renders gallery SVGs and syncs card-support issue bodies."""
import argparse
import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from html import escape
from string import Template
from typing import Dict, List, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CATALOG_DIR = os.path.join(HERE, "catalog")
TEMPLATE_DIR = os.path.join(HERE, "templates")
CARDS_ROOT = os.path.join(ROOT, "spirit", "game", "scripts", "cards")
GALLERY_DIR = os.path.join(ROOT, "gallery")
REPO = os.environ.get("GITHUB_REPOSITORY", "Bratah123/Spirit-PTCGO")
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/main"
SCRIPT_NAME = re.compile(r"_(\d+)\.py$")
PROMO_NUMBER = re.compile(r"[A-Za-z]+0*(\d+)")
SET_TITLE = re.compile(r"^Set support: .+ \(([a-z0-9.]+)\)$", re.I)
LABEL = "card-support"
EPIC_LABEL = "epic"


@dataclass
class SetProgress:
    meta: dict
    era: dict
    cards: List[dict] = field(default_factory=list)

    @property
    def done(self) -> int:
        return sum(1 for c in self.cards if c["done"])

    @property
    def total(self) -> int:
        return len(self.cards)

    @property
    def complete(self) -> bool:
        return self.total > 0 and self.done == self.total


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def template(name) -> Template:
    with open(os.path.join(TEMPLATE_DIR, name), encoding="utf-8") as f:
        return Template(f.read())


def load_catalog():
    eras = read_json(os.path.join(CATALOG_DIR, "eras.json"))
    sets = read_json(os.path.join(CATALOG_DIR, "sets.json"))
    return eras, sets


def load_cards(set_id) -> List[dict]:
    return read_json(os.path.join(CATALOG_DIR, "cards", f"{set_id}.json"))


def is_stub(tree) -> bool:
    return any(
        isinstance(node, ast.keyword) and node.arg == "effect"
        and isinstance(node.value, ast.Name) and node.value.id == "unimplemented"
        for node in ast.walk(tree))


def collector_number(tree) -> Optional[int]:
    for node in ast.walk(tree):
        if (isinstance(node, ast.keyword) and node.arg == "collector_number"
                and isinstance(node.value, ast.Constant) and isinstance(node.value.value, int)):
            return node.value.value
    return None


def scan_scripts(script_dirs) -> Dict[int, bool]:
    found: Dict[int, bool] = {}
    for dirname in script_dirs:
        path = os.path.join(CARDS_ROOT, dirname)
        if not os.path.isdir(path):
            continue
        for filename in sorted(os.listdir(path)):
            match = SCRIPT_NAME.search(filename)
            if not match:
                continue
            with open(os.path.join(path, filename), encoding="utf-8") as f:
                try:
                    tree = ast.parse(f.read())
                except SyntaxError:
                    continue
            number = collector_number(tree) or int(match.group(1))
            found[number] = found.get(number, True) and not is_stub(tree)
    return found


def card_key(card, promo) -> Optional[int]:
    if card.get("subset"):
        return None
    number = card["number"]
    if number.isdigit():
        return int(number)
    match = PROMO_NUMBER.fullmatch(number)
    return int(match.group(1)) if promo and match else None


def compute_progress() -> List[SetProgress]:
    eras, sets = load_catalog()
    era_by_key = {e["key"]: e for e in eras}
    out = []
    for meta in sets:
        implemented = scan_scripts(meta.get("script_dirs", []))
        promo = meta.get("promo", False)
        progress = SetProgress(meta, era_by_key[meta["era"]])
        for card in load_cards(meta["id"]):
            key = card_key(card, promo)
            progress.cards.append({**card, "done": key is not None and implemented.get(key, False)})
        out.append(progress)
    return out


def fmt_percent(done, total) -> str:
    if total and done == total:
        return "100%"
    return f"{100 * done / total:.1f}%" if total else "0%"


def colored_percent(done, total) -> str:
    color = "green" if total and done == total else "red"
    text = fmt_percent(done, total).replace("%", "\\\\%")
    return f"${{\\color{{{color}}}\\mathsf{{{text}}}}}$"


def bar_svg(name, done, total, color) -> str:
    width = 608
    fill_width = width * done / total if total else 0
    fill = (f'<rect x="16" y="44" width="{max(fill_width, 14):.1f}" height="14" rx="7" fill="{color}"/>'
            if done else "")
    ticks = "\n".join(
        f'<rect x="{16 + width * i / 10:.1f}" y="44" width="1" height="14" class="bg" opacity="0.55"/>'
        for i in range(1, 10))
    return template("set_progress.svg").substitute(
        name=escape(name), done=done, total=total, done_fmt=f"{done:,}", total_fmt=f"{total:,}",
        status="Complete" if total and done == total else fmt_percent(done, total),
        fill=fill, ticks=ticks)


def overall_svg(eras, progress) -> str:
    total = sum(p.total for p in progress)
    done = sum(p.done for p in progress)
    segments, rows = [], []
    x, strip = 24.0, 792
    row_top, row_height, label_x = 150, 26, 300
    row_width = 840 - 24 - label_x - 150
    for i, era in enumerate(eras):
        members = [p for p in progress if p.era["key"] == era["key"]]
        era_total = sum(p.total for p in members)
        era_done = sum(p.done for p in members)
        width = strip * era_total / total if total else 0
        segments.append(f'<rect x="{x:.1f}" y="92" width="{width:.1f}" height="20" fill="{era["color"]}" opacity="0.18"/>')
        if era_done:
            segments.append(f'<rect x="{x:.1f}" y="92" width="{width * era_done / era_total:.1f}" height="20" fill="{era["color"]}"/>')
        segments.append(f'<rect x="{x + width - 1:.1f}" y="92" width="2" height="20" class="bg"/>')
        x += width
        y = row_top + i * row_height
        rows.append(f'<circle cx="30" cy="{y + 9}" r="5" fill="{era["color"]}"/>')
        rows.append(f'<text class="t" x="44" y="{y + 13}" font-size="13">{escape(era["name"])}</text>')
        rows.append(f'<text class="m" x="{label_x - 12}" y="{y + 13}" font-size="11" text-anchor="end">{era["years"]}</text>')
        rows.append(f'<rect class="trk" x="{label_x}" y="{y + 4}" width="{row_width}" height="10" rx="5"/>')
        if era_done:
            rows.append(f'<rect x="{label_x}" y="{y + 4}" width="{max(row_width * era_done / era_total, 10):.1f}" '
                        f'height="10" rx="5" fill="{era["color"]}"/>')
        rows.append(f'<text class="m" x="816" y="{y + 13}" font-size="12" text-anchor="end">'
                    f'<tspan class="t">{era_done:,}</tspan> / {era_total:,} ({fmt_percent(era_done, era_total)})</text>')
    height = row_top + row_height * len(eras) + 18
    return template("overall_progress.svg").substitute(
        height=height, inner_height=height - 1, done=done, total=total,
        done_fmt=f"{done:,}", total_fmt=f"{total:,}", percent=fmt_percent(done, total),
        complete_count=sum(1 for p in progress if p.complete), set_count=len(progress),
        segments="\n".join(segments), rows="\n".join(rows))


def set_image_path(set_id) -> str:
    return f"gallery/{set_id}/progress.svg"


def era_image_path(era_key) -> str:
    return f"gallery/eras/{era_key}/progress.svg"


def write_file(rel_path, content) -> bool:
    path = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            if f.read() == content:
                return False
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return True


def render_gallery(eras, progress) -> int:
    changed = write_file("gallery/progress.svg", overall_svg(eras, progress))
    for era in eras:
        members = [p for p in progress if p.era["key"] == era["key"]]
        svg = bar_svg(era["name"], sum(p.done for p in members), sum(p.total for p in members), era["color"])
        changed += write_file(era_image_path(era["key"]), svg)
    for p in progress:
        changed += write_file(set_image_path(p.meta["id"]), bar_svg(p.meta["name"], p.done, p.total, p.era["color"]))
    return changed


def image_url(rel_path, sha) -> str:
    return f"{RAW_BASE}/{rel_path}?v={sha}"


def set_progress_block(p: SetProgress, sha) -> str:
    return template("set_progress_block.md").substitute(
        name=p.meta["name"], done=f"{p.done:,}", total=f"{p.total:,}",
        percent=fmt_percent(p.done, p.total), sha=sha,
        image_url=image_url(set_image_path(p.meta["id"]), sha)).strip()


def card_line(card) -> str:
    number = card["number"].zfill(3) if card["number"].isdigit() else card["number"]
    return f'- [{"x" if card["done"] else " "}] `{number}` {card["name"]}'


def card_checklist_block(p: SetProgress) -> str:
    groups = []
    subsets = {s["id"]: s["name"] for s in p.meta.get("subsets", [])}
    for subset_id in [None] + list(subsets):
        cards = [c for c in p.cards if c.get("subset") == subset_id]
        if not cards:
            continue
        title = "Main set" if subset_id is None else subsets[subset_id]
        done = sum(1 for c in cards if c["done"])
        heading = f"#### {title} ({done} / {len(cards)})\n" if subsets else ""
        groups.append(heading + "\n".join(card_line(c) for c in cards))
    return template("card_checklist.md").substitute(
        done=p.done, total=p.total, groups="\n\n".join(groups)).strip()


def epic_progress_block(era, members: List[SetProgress], sha, numbers: Dict[str, int]) -> str:
    rows = []
    for p in members:
        ref = f'#{numbers[p.meta["id"]]}' if p.meta["id"] in numbers else p.meta["name"]
        rows.append(f'| {ref} | {p.meta["release"]} | {p.done:,} / {p.total:,} | {colored_percent(p.done, p.total)} |')
    done = sum(p.done for p in members)
    total = sum(p.total for p in members)
    return template("epic_progress_block.md").substitute(
        name=era["name"], done=f"{done:,}", total=f"{total:,}", percent=fmt_percent(done, total),
        set_count=len(members), complete_count=sum(1 for p in members if p.complete), sha=sha,
        image_url=image_url(era_image_path(era["key"]), sha), set_rows="\n".join(rows)).strip()


def wrap(name, content) -> str:
    return f"<!-- {name}:start -->\n{content}\n<!-- {name}:end -->"


def replace_block(body, name, content) -> str:
    pattern = re.compile(rf"<!-- {name}:start -->.*?<!-- {name}:end -->", re.S)
    if not pattern.search(body):
        return body
    return pattern.sub(lambda _: wrap(name, content), body, count=1)


def current_sha() -> str:
    sha = os.environ.get("GITHUB_SHA")
    if not sha:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout.strip()
    return sha[:7]


def gh(*args, input_text=None) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8",
                            input=input_text, check=True)
    return result.stdout


def list_issues() -> List[dict]:
    return json.loads(gh("issue", "list", "--repo", REPO, "--label", LABEL, "--state", "all",
                         "--limit", "1000", "--json", "number,title,body,state,labels"))


def edit_body(number, body):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(body)
    try:
        gh("issue", "edit", str(number), "--repo", REPO, "--body-file", f.name)
    finally:
        os.unlink(f.name)


def sync_issues(eras, progress, sha, dry_run, close_complete):
    issues = list_issues()
    by_set = {}
    epics = {}
    for issue in issues:
        labels = {label["name"] for label in issue["labels"]}
        match = SET_TITLE.match(issue["title"])
        if match:
            by_set[match.group(1)] = issue
        elif EPIC_LABEL in labels:
            for era in eras:
                if f'era:{era["key"]}' in labels:
                    epics[era["key"]] = issue
    numbers = {set_id: issue["number"] for set_id, issue in by_set.items()}
    actions = []
    for p in progress:
        issue = by_set.get(p.meta["id"])
        if issue is None:
            continue
        body = replace_block(issue["body"], "progress", set_progress_block(p, sha))
        body = replace_block(body, "cards", card_checklist_block(p))
        if strip_sha(body) != strip_sha(issue["body"]):
            actions.append(("edit", issue["number"], body))
        if close_complete and p.complete and issue["state"] == "OPEN":
            actions.append(("close", issue["number"], None))
    for era in eras:
        issue = epics.get(era["key"])
        if issue is None:
            continue
        members = [p for p in progress if p.era["key"] == era["key"]]
        body = replace_block(issue["body"], "progress", epic_progress_block(era, members, sha, numbers))
        if strip_sha(body) != strip_sha(issue["body"]):
            actions.append(("edit", issue["number"], body))
    for kind, number, body in actions:
        print(f"{'would ' if dry_run else ''}{kind} #{number}")
        if dry_run:
            continue
        if kind == "edit":
            edit_body(number, body)
        else:
            gh("issue", "close", str(number), "--repo", REPO, "--reason", "completed")
    print(f"{len(actions)} issue update(s){' planned' if dry_run else ''}")


def strip_sha(body) -> str:
    return re.sub(r"(\?v=|updated at `)[0-9a-f]{7}", r"\1", body)


def print_summary(eras, progress):
    for era in eras:
        members = [p for p in progress if p.era["key"] == era["key"]]
        done = sum(p.done for p in members)
        total = sum(p.total for p in members)
        print(f"{era['name']:<34} {done:>6,} / {total:>6,}  {fmt_percent(done, total):>6}")
    done = sum(p.done for p in progress)
    total = sum(p.total for p in progress)
    print(f"{'TOTAL':<34} {done:>6,} / {total:>6,}  {fmt_percent(done, total):>6}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("summary", help="print per-era progress")
    sub.add_parser("render", help="write gallery/ progress SVGs")
    sync = sub.add_parser("sync-issues", help="rewrite the bot-owned sections of card-support issues")
    sync.add_argument("--dry-run", action="store_true")
    sync.add_argument("--no-close", action="store_true", help="never close completed set issues")
    args = parser.parse_args()
    eras, _ = load_catalog()
    progress = compute_progress()
    if args.command == "summary":
        print_summary(eras, progress)
    elif args.command == "render":
        print(f"{render_gallery(eras, progress)} SVG(s) changed")
        print_summary(eras, progress)
    else:
        sync_issues(eras, progress, current_sha(), args.dry_run, not args.no_close)


if __name__ == "__main__":
    sys.exit(main())
