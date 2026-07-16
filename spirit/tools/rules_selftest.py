"""Self-tests for deck-legality validation (spirit/game/rules.py + format_manager).

Runs headless on the loaded card scripts (no network/DB).
Usage: python -m spirit.tools.rules_selftest -- exit 0 iff every assertion passes.
"""

import sys
import uuid

from spirit.game.attributes import AttrID, CardType, DeckFormat, PokemonStage
from spirit.game.format_manager import FormatManager, is_basic_energy_card
from spirit.game import rules
from spirit.game.scripts.cards import loader as card_loader

FAILURES = []


def check(cond, label):
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILURES.append(label)


def deck(guids, name="Test Deck", pile_name="deck"):
    return {"deckID": str(uuid.uuid4()), "deckName": name, "piles": {pile_name: list(guids)}}


def failure_types(row):
    return {d["failureType"] for d in row["results"]}


def find_card(predicate):
    for c in card_loader.cards:
        if predicate(c):
            return c
    return None


def is_basic_pokemon(c):
    return (c.get_attribute_value(AttrID.CARD_TYPE) == CardType.POKEMON.value
            and c.get_attribute_value(AttrID.STAGE, 0) == PokemonStage.BASIC.value)


def main():
    card_loader.load_all()
    manager = FormatManager()

    swsh_basic = find_card(lambda c: c.key == "SWSH8" and is_basic_pokemon(c))
    bw_card = find_card(lambda c: c.key == "BW1"
                        and c.get_attribute_value(AttrID.CARD_TYPE) == CardType.POKEMON.value)
    water = find_card(lambda c: c.key == "Free_Energy"
                      and rules.card_display_name(c) == "Water Energy")
    assert swsh_basic and bw_card and water, "fixture cards missing from loaded scripts"

    # Two printings sharing a display name (the 4-copy rule counts names, not GUIDs)
    by_name = {}
    reprint_pair = None
    for c in card_loader.cards:
        if is_basic_energy_card(c) or not c.display_name:
            continue
        other = by_name.setdefault(c.display_name, c)
        if other.guid.lower() != c.guid.lower():
            reprint_pair = (other, c)
            break

    std, exp, unl = DeckFormat.STANDARD.value, DeckFormat.EXPANDED.value, DeckFormat.UNLIMITED.value

    print("[1] legal 60-card deck")
    legal = deck([swsh_basic.guid] * 4 + [water.guid] * 56)
    rows = {r["format"]: r for r in rules.validate_deck(legal, [std, exp, unl])}
    check(all(r["valid"] for r in rows.values()), "valid in Standard/Expanded/Unlimited")
    check(rows[std]["formatName"] == "Modified", "Standard wire name is 'Modified'")
    check(all(r["results"] == [] for r in rows.values()), "no failure details on a valid deck")
    check(set(rules.valid_format_names(legal)) == {"Modified", "Expanded", "Legacy", "Unlimited"}
          or set(rules.valid_format_names(legal)) == {"Modified", "Expanded", "Unlimited"},
          f"attr-10860 names sane: {rules.valid_format_names(legal)}")
    client_legal = deck([swsh_basic.guid] * 4 + [water.guid] * 56, pile_name="CakePile")
    rows = rules.validate_deck(client_legal, [std, exp, unl])
    check(all(r["valid"] for r in rows), "client CakePile accepted as the main deck pile")

    print("[2] deck size must be exactly 60")
    for n, label in ((59, "59 cards"), (61, "61 cards")):
        bad = deck([swsh_basic.guid] * 4 + [water.guid] * (n - 4))
        row = rules.validate_deck(bad, [std])[0]
        check(not row["valid"] and "ExactSize" in failure_types(row), f"{label} -> ExactSize")

    print("[3] max 4 copies with the same name")
    dup = deck([swsh_basic.guid] * 5 + [water.guid] * 55)
    row = rules.validate_deck(dup, [std])[0]
    check(not row["valid"] and "MaxDuplicates" in failure_types(row), "5 copies -> MaxDuplicates")
    detail = next(d for d in row["results"] if d["failureType"] == "MaxDuplicates")
    check(swsh_basic.guid.lower() in detail["offendingArchetypeIDs"], "offender GUID listed")

    if reprint_pair:
        a, b = reprint_pair
        mix = deck([a.guid] * 3 + [b.guid] * 2 + [swsh_basic.guid] * 4 + [water.guid] * 51)
        row = rules.validate_deck(mix, [unl])[0]
        check("MaxDuplicates" in failure_types(row),
              f"3+2 reprints of '{a.display_name}' ({a.key}/{b.key}) -> MaxDuplicates")
        if a.display_name == swsh_basic.display_name:
            check(False, "reprint fixture collides with filler basic")

    print("[4] basic energy is exempt from the 4-copy rule")
    energy_heavy = deck([swsh_basic.guid] * 4 + [water.guid] * 56)
    row = rules.validate_deck(energy_heavy, [std])[0]
    check("MaxDuplicates" not in failure_types(row), "56 Water Energy allowed")

    print("[5] at least one Basic Pokemon")
    no_basic = deck([water.guid] * 60)
    row = rules.validate_deck(no_basic, [std])[0]
    check(not row["valid"] and "MustContain" in failure_types(row), "all-energy deck -> MustContain")

    print("[6] format set legality (BW1 defaults: Expanded yes, Standard no)")
    bw_deck = deck([swsh_basic.guid] * 4 + [bw_card.guid] + [water.guid] * 55)
    rows = {r["format"]: r for r in rules.validate_deck(bw_deck, [std, exp, unl])}
    check(not rows[std]["valid"] and "DeckContainsBannedCards" in failure_types(rows[std]),
          "BW1 card illegal in Standard")
    check(rows[exp]["valid"], "BW1 card legal in Expanded")
    check(rows[unl]["valid"], "BW1 card legal in Unlimited")

    print("[7] banned-card override")
    std_fmt = manager.by_guid(std)
    std_fmt.banned_cards.append(swsh_basic.guid)
    manager._ref_cache.clear()
    try:
        row = rules.validate_deck(legal, [std])[0]
        check(not row["valid"] and "DeckContainsBannedCards" in failure_types(row),
              "banned GUID fails Standard")
        row_unl = rules.validate_deck(legal, [unl])[0]
        check(row_unl["valid"], "ban is per-format (Unlimited unaffected)")
    finally:
        std_fmt.banned_cards.remove(swsh_basic.guid)
        manager._ref_cache.clear()

    print("[8] SET/number card refs resolve")
    num = swsh_basic.get_attribute_value(AttrID.COLLECTOR_NUMBER)
    std_fmt.banned_cards.append(f"{swsh_basic.key}/{num}")
    manager._ref_cache.clear()
    try:
        row = rules.validate_deck(legal, [std])[0]
        check(not row["valid"], f"banned ref '{swsh_basic.key}/{num}' fails Standard")
    finally:
        std_fmt.banned_cards.pop()
        manager._ref_cache.clear()

    print("[9] unknown GUIDs invalidate the deck")
    ghost = deck([swsh_basic.guid] * 4 + [water.guid] * 55 + [str(uuid.uuid4())])
    row = rules.validate_deck(ghost, [std])[0]
    check(not row["valid"] and "MustNotContain" in failure_types(row), "ghost GUID -> MustNotContain")

    print("[10] ownership check")
    row = rules.validate_deck(legal, [std], owned_counts={})[0]
    check(not row["valid"] and "UnownedCards" in failure_types(row), "unowned Pokemon flagged")
    detail = next(d for d in row["results"] if d["failureType"] == "UnownedCards")
    check(water.guid.lower() not in detail["offendingArchetypeIDs"], "basic energy never unowned")
    row = rules.validate_deck(legal, [std], owned_counts={swsh_basic.guid.lower(): 4})[0]
    check(row["valid"], "owning exactly 4 satisfies the check")

    print("[11] unsupported format rows")
    row = rules.validate_deck(legal, [DeckFormat.THEME.value])[0]
    check(not row["valid"] and row["formatName"] == "ThemeDeck", "Theme -> invalid, name kept")

    print("[12] manager set queries")
    swsh8_formats = set(manager.legal_format_guids_for_set("SWSH8"))
    check({std, exp, unl} <= swsh8_formats, "SWSH8 legal in Standard/Expanded/Unlimited")
    check(std not in manager.legal_format_guids_for_set("BW1"), "BW1 not Standard")

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILURE(S):")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    print("All rules self-tests passed.")


if __name__ == "__main__":
    main()
