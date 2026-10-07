"""Headless AI-vs-AI runner for the deck strategic-brain pipeline.

Boots a real GameSession with two AIPlayer seats (no sockets), runs the full
pregame -> setup -> turn loop, and reports who won, how the game went, and
every strategic decision the brains made (deck searches, damage-counter
plans, trainer/ability plays).

Default mode is A/B: seat1 uses the deck's brain, seat2 is the same deck
played by the generic AI (deck_strategy stripped), so the win split shows
what the brain is worth.

Usage (from repo root):
    .\\venv\\Scripts\\python.exe tools\\sim_bot_match.py --games 4
    .\\venv\\Scripts\\python.exe tools\\sim_bot_match.py --games 2 --trace
"""

import argparse
import asyncio
import logging
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from spirit.game.content.bot_decks import BOT_DECK_LISTS  # noqa: E402
from spirit.game.content.starter import build_deck_data  # noqa: E402
from spirit.game.session import game_session as gs_mod  # noqa: E402
from spirit.game.session.game_session import GameSession  # noqa: E402


DECK_NAME = "Dragapult Inteleon"

DESCRIPTION_LABELS = {
    "DefaultPokemonPlayAbility": "bench",
    "DefaultEnergyPlayAbility": "energy",
    "EvolvePokemonPlayAbility": "evolve",
    "DefaultLegendPokemonPlayAbility": "legend",
    "UsePokemonAbility": "ability",
    "UseTrainerCard": "trainer",
    "DefaultStadiumPlayAbility": "stadium",
    "DefaultToolPlayAbility": "tool",
    "UsePokemonAttack": "attack",
    "BaseRetreat": "retreat",
}


class CaptureHandler(logging.Handler):
    """Grabs every log line produced during one game (incl. tracebacks)."""

    def __init__(self):
        super().__init__(level=logging.INFO)
        self.lines = []

    def emit(self, record):
        try:
            message = record.getMessage()
            if record.exc_info and record.exc_info[0] is not None:
                message += "\n" + logging.Formatter().formatException(record.exc_info)
            self.lines.append(message)
        except Exception:
            pass


def classify(lines, seat_ids):
    """Turn captured log lines into per-seat action counts + highlight reels."""
    stats = {pid: {} for pid in seat_ids}
    searches = {pid: [] for pid in seat_ids}
    counters = {pid: [] for pid in seat_ids}
    errors = []
    for line in lines:
        if record_is_error(line):
            errors.append(line)
        for pid in seat_ids:
            marker = f"AI {pid} plays "
            if marker in line and line.endswith(")."):
                desc = line[line.rfind("(") + 1:-2]
                label = DESCRIPTION_LABELS.get(desc, desc)
                stats[pid][label] = stats[pid].get(label, 0) + 1
            if f"AI {pid} deck search picks" in line:
                searches[pid].append(line)
            if f"AI {pid} places" in line and "damage counters" in line:
                counters[pid].append(line)
    return stats, searches, counters, errors


def record_is_error(line):
    return ("Error in gameplay sequence" in line
            or "Traceback (most recent call last)" in line)


async def run_game(game_no, seat1_brain, seat2_brain, trace, grace_seconds,
                   deck_name=DECK_NAME):
    deck_data_1 = build_deck_data(deck_name, BOT_DECK_LISTS[deck_name])
    deck_data_2 = build_deck_data(deck_name, BOT_DECK_LISTS[deck_name])
    pairing = {
        "players": {
            "ai1": {"client": None, "deck": deck_data_1, "ready": True},
            "ai2": {"client": None, "deck": deck_data_2, "ready": True},
        },
        "is_solo": False,
    }
    session = GameSession(f"sim-{game_no}", pairing)
    session.choreography_pauses = False
    if not seat1_brain:
        session.players["ai1"].deck_strategy = None
    if not seat2_brain:
        session.players["ai2"].deck_strategy = None

    capture = CaptureHandler()
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(capture)
    gs_mod.AI_PROMPT_GRACE_SECONDS = grace_seconds

    started = time.time()
    timeout = False
    try:
        await session.start()
        await session.mark_player_ready("ai1")
        assert session.gameplay_task is not None, "gameplay never spawned"
        try:
            await asyncio.wait_for(asyncio.shield(session.gameplay_task), 240)
        except asyncio.TimeoutError:
            timeout = True
            session.gameplay_task.cancel()
            try:
                await session.gameplay_task
            except (asyncio.CancelledError, Exception):
                pass
        except asyncio.CancelledError:
            # Normal teardown: cleanup() cancels the gameplay task (which is
            # itself still inside its finally) -- the result is already decided.
            if session.game_result is None and not timeout:
                pass
    finally:
        root.removeHandler(capture)

    elapsed = time.time() - started
    result = session.game_result or {}
    winner = result.get("winner")
    reason = result.get("reason") or ("timeout" if timeout else "no result")
    stats, searches, counters, errors = classify(capture.lines, ("ai1", "ai2"))

    if trace:
        print(f"--- game {game_no} trace ---")
        for line in capture.lines:
            if (" plays " in line and "AI ai" in line) or "deck search picks" in line \
                    or "damage counters" in line or "(AI) ends turn" in line:
                print("   ", line)

    return {
        "game": game_no,
        "winner": winner,
        "reason": reason,
        "turns": session.turn_state.turn_number,
        "seconds": round(elapsed, 1),
        "stats": stats,
        "searches": searches,
        "counters": counters,
        "errors": errors,
        "trace": capture.lines,
    }


def seat_label(pid, seat1_brain, seat2_brain):
    if pid == "ai1":
        return "ai1 (brain)" if seat1_brain else "ai1 (generic)"
    return "ai2 (brain)" if seat2_brain else "ai2 (generic)"


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=4)
    parser.add_argument("--trace", action="store_true",
                        help="print every AI decision line per game")
    parser.add_argument("--mode", choices=["ab", "mirror"], default="ab",
                        help="ab: brain vs generic | mirror: brain vs brain")
    parser.add_argument("--grace", type=float, default=3.0,
                        help="AI prompt grace seconds (stall guard)")
    parser.add_argument("--deck", default=DECK_NAME,
                        choices=sorted(BOT_DECK_LISTS),
                        help="deck both seats play")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        stream=sys.stdout,
        force=True,
    )

    seat1_brain = True
    seat2_brain = args.mode == "mirror"

    results = []
    for n in range(1, args.games + 1):
        res = await run_game(n, seat1_brain, seat2_brain, args.trace,
                             args.grace, args.deck)
        results.append(res)
        stats = res["stats"]
        parts = []
        for pid in ("ai1", "ai2"):
            counts = ", ".join(f"{k}x{v}" for k, v in sorted(stats[pid].items())) or "-"
            parts.append(f"{pid}: {counts}")
        print(
            f"Game {res['game']}: winner={res['winner']} ({res['reason']}) "
            f"turns={res['turns']} time={res['seconds']}s"
        )
        for part in parts:
            print(f"    {part}")
        for pid in ("ai1", "ai2"):
            for line in res["searches"][pid]:
                print(f"    {line}")
            for line in res["counters"][pid]:
                print(f"    {line}")
        for line in res["errors"][:5]:
            print(f"    ERROR: {line}")

    print("\n=== summary ===")
    wins = {"ai1": 0, "ai2": 0}
    for res in results:
        if res["winner"] in wins:
            wins[res["winner"]] += 1
    print(f"ai1 ({'brain' if seat1_brain else 'generic'}) wins: {wins['ai1']}/{len(results)}")
    print(f"ai2 ({'brain' if seat2_brain else 'generic'}) wins: {wins['ai2']}/{len(results)}")
    crash = sum(1 for r in results if "game error" in r["reason"].lower())
    print(f"crash-fallback results: {crash}/{len(results)}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
