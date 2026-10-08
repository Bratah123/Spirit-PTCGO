import re
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

import convert_deck  # noqa: E402

CLIPBOARD = """Pokemon: 4
1 Sobble CRE 41
3 Dreepy RCL 93
Trainer: 8
4 Marnie CPA 56
4 Professor's Research SHF 60
Energy: 4
4 Grass Energy Energy 36
"""

CLIPBOARD_OUT = """****** Pokémon Trading Card Game Deck List ******

Pokémon - 4

1 Sobble CRE 41
3 Dreepy RCL 93

Trainer Cards - 8

4 Marnie CPA 56
4 Professor's Research SHF 60

Energy Cards - 4

4 Grass Energy Energy 1

Total Cards - 16

****** Deck list generated on Pokemon.com ******
"""

RENDERED = """Pokémon (7)

4 Dragapult VMAX (RCL-93)
3 Pumpkaboo (CEL-16)

Trainer (6)

4 Marnie
2 Professor's Research

Energy (10)

4 Horror Psychic Energy
3 Fire Energy
2 Capture Energy
1 Grass Energy
"""

BAD_WARNINGS = ("missing a set code", "no collector number", "card line before")


def card_lines(text):
    return [l for l in text.splitlines() if re.match(r"^\d+ \S", l)]


class ClipboardFormatTest(unittest.TestCase):
    def test_golden_output_unchanged(self):
        body, warns, counts, total = convert_deck.convert(CLIPBOARD)
        self.assertEqual(body, CLIPBOARD_OUT)
        self.assertEqual(total, 16)
        self.assertEqual(counts, {"pokemon": 4, "trainer": 8, "energy": 4})
        for w in warns:
            self.assertNotIn("filled", w)
        for w in warns:
            self.assertNotIn("missing", w)

    def test_idempotent(self):
        body, _, _, _ = convert_deck.convert(CLIPBOARD)
        body2, warns2, _, _ = convert_deck.convert(body)
        self.assertEqual(body2, body)


class RenderedFormatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.body, cls.warns, cls.counts, cls.total = convert_deck.convert(RENDERED)

    def test_sections_and_totals(self):
        self.assertEqual(self.total, 23)
        self.assertEqual(self.counts, {"pokemon": 7, "trainer": 6, "energy": 10})
        self.assertIn("Pokémon - 7", self.body)
        self.assertIn("Trainer Cards - 6", self.body)
        self.assertIn("Energy Cards - 10", self.body)

    def test_every_card_line_is_importable(self):
        lines = card_lines(self.body)
        self.assertEqual(len(lines), 8)
        for line in lines:
            self.assertRegex(line, r"^\d+ \S.* [A-Za-z0-9\-]+ \d+$", line)

    def test_no_unfilled_warnings(self):
        for w in self.warns:
            for bad in BAD_WARNINGS:
                self.assertNotIn(bad, w, w)

    def test_fill_warnings_present(self):
        self.assertTrue(
            any(w.startswith("filled from card catalog") for w in self.warns),
            self.warns)
        self.assertTrue(
            any(w.startswith("filled basic energy number") for w in self.warns),
            self.warns)

    def test_special_energy_filled(self):
        self.assertIn("4 Horror Psychic Energy RCL 172", self.body)
        self.assertIn("2 Capture Energy DAA 201", self.body)

    def test_basic_energies_use_pokemon_com_numbers(self):
        self.assertIn("3 Fire Energy Energy 2", self.body)
        self.assertIn("1 Grass Energy Energy 1", self.body)

    def test_paren_set_stripped(self):
        self.assertIn("4 Dragapult VMAX RCL 93", self.body)
        self.assertIn("3 Pumpkaboo CEL 16", self.body)

    def test_idempotent(self):
        body2, warns2, _, _ = convert_deck.convert(self.body)
        self.assertEqual(body2, self.body)
        for w in warns2:
            for bad in BAD_WARNINGS + ("filled",):
                self.assertNotIn(bad, w, w)


class HeaderCountsTest(unittest.TestCase):
    def test_paren_count_mismatch_warns(self):
        _, warns, _, _ = convert_deck.convert(
            "Pokémon (4)\n4 Sobble (CRE-41)\n3 Dreepy (RCL-93)\n")
        self.assertTrue(
            any("header says 4, lines add up to 7" in w for w in warns), warns)

    def test_paren_count_match_silent(self):
        _, warns, _, _ = convert_deck.convert(
            "Energy (3)\n3 Grass Energy\n")
        self.assertFalse(
            any("header says" in w for w in warns), warns)

    def test_old_style_headers_still_work(self):
        _, warns, counts, total = convert_deck.convert(
            "##Pokemon - 4\n4 Sobble CRE 41\n##Energy - 4\n4 Grass Energy 36\n")
        self.assertEqual(counts, {"pokemon": 4, "trainer": 0, "energy": 4})
        self.assertEqual(total, 8)

    def test_new_style_energy_cards_header_parses(self):
        _, _, counts, total = convert_deck.convert(
            "Energy Cards - 4\n4 Fire Energy Energy 2\n")
        self.assertEqual(counts, {"pokemon": 0, "trainer": 0, "energy": 4})
        self.assertEqual(total, 4)


class ParseCardLinesTest(unittest.TestCase):
    def test_paren_set_parsed(self):
        rows = convert_deck.parse_card_lines("Pokémon:\n4 Sobble (CRE-41)\n")
        self.assertEqual(rows, [("pokemon", 4, "Sobble", "CRE", "41")])

    def test_clipboard_rows_unchanged(self):
        rows = convert_deck.parse_card_lines(CLIPBOARD)
        self.assertEqual(rows[0], ("pokemon", 1, "Sobble", "CRE", "41"))
        self.assertEqual(rows[2], ("trainer", 4, "Marnie", "CPA", "56"))
        self.assertEqual(rows[4], ("energy", 4, "Grass Energy", None, "36"))

    def test_pokemon_com_output_parses(self):
        rows = convert_deck.parse_card_lines(CLIPBOARD_OUT)
        self.assertEqual(rows[0], ("pokemon", 1, "Sobble", "CRE", "41"))
        self.assertEqual(rows[4], ("energy", 4, "Grass Energy", None, "1"))


class DegradationTest(unittest.TestCase):
    def test_catalog_unavailable_warns_and_keeps_line(self):
        with patch.object(convert_deck, "_load_catalog", return_value=None):
            body, warns, _, _ = convert_deck.convert(
                "Trainer:\n1 Definitely Not A Card\n")
        self.assertIn("1 Definitely Not A Card", body)
        self.assertTrue(
            any("missing a set code" in w and "catalog unavailable" in w
                for w in warns),
            warns)

    def test_basic_energy_number_table_works_without_catalog(self):
        with patch.object(convert_deck, "_load_catalog", return_value=None):
            body, warns, _, _ = convert_deck.convert("Energy:\n10 Grass Energy\n")
        self.assertIn("10 Grass Energy Energy 1", body)
        self.assertTrue(
            any("filled basic energy number" in w for w in warns), warns)


if __name__ == "__main__":
    unittest.main()
