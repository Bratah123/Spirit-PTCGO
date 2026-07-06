"""Tests for special-energy attachment pip texture generation (auto_bundle)."""

import os
import shutil
import tempfile
import unittest

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef, ItemCardDef, PokemonToolCardDef
from spirit.server.auto_bundle import (
    _detect_emblem_circle,
    _is_pokemon_tool,
    _is_special_energy,
    generate_energy_pip_png,
    generate_tool_pip_png,
)

try:
    from PIL import Image, ImageDraw
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


SPECIAL_ENERGY = EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000p1",
    key="BW1", name="com.test.energy.SpecialPip.Name",
    collector_number=169, set_code="BW1", rarity=0,
    energy_type=PokemonTypes.COLORLESS, is_special=True,
)

BASIC_ENERGY = EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000p2",
    key="BW1", name="com.test.energy.BasicPip.Name",
    collector_number=106, set_code="BW1", rarity=0,
    energy_type=PokemonTypes.FIRE,
)

TOOL_CARD = PokemonToolCardDef(
    guid="00000000-0000-0000-0000-0000000000p3",
    key="BW1", name="com.test.trainer.ToolPip.Name",
    collector_number=156, set_code="BW1", rarity=Rarities.Uncommon,
)

ITEM_CARD = ItemCardDef(
    guid="00000000-0000-0000-0000-0000000000p4",
    key="BW1", name="com.test.trainer.ItemPip.Name",
    collector_number=157, set_code="BW1", rarity=Rarities.Uncommon,
)


class TestSpecialEnergyDetection(unittest.TestCase):
    def test_special_energy_flag(self):
        self.assertTrue(_is_special_energy(SPECIAL_ENERGY))
        self.assertFalse(_is_special_energy(BASIC_ENERGY))

    def test_pokemon_tool_flag(self):
        self.assertTrue(_is_pokemon_tool(TOOL_CARD))
        self.assertFalse(_is_pokemon_tool(ITEM_CARD))
        self.assertFalse(_is_pokemon_tool(BASIC_ENERGY))


@unittest.skipUnless(HAS_PIL, "Pillow not installed")
class TestPipGeneration(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.src = os.path.join(self.temp_dir, "card.png")
        Image.new("RGBA", (734, 1024), (200, 40, 40, 255)).save(self.src)

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_pip_is_a_square_crop_named_energypip(self):
        out = generate_energy_pip_png(self.src, "SWSH12", "169",
                                      out_dir=self.temp_dir)
        self.assertEqual(os.path.basename(out), "SWSH12_169_energypip.png")
        with Image.open(out) as pip:
            self.assertEqual(pip.width, pip.height)
            self.assertGreater(pip.width, 0)

    def test_tool_pip_is_a_square_crop_named_toolpip(self):
        out = generate_tool_pip_png(self.src, "SWSH1", "156",
                                    out_dir=self.temp_dir)
        self.assertEqual(os.path.basename(out), "SWSH1_156_toolpip.png")
        with Image.open(out) as pip:
            self.assertEqual(pip.width, pip.height)
            self.assertGreater(pip.width, 0)

    def test_detection_centers_on_a_drawn_emblem(self):
        img = Image.new("RGBA", (734, 1024), (240, 240, 240, 255))
        # Off-center circle emblem inside the art window.
        ImageDraw.Draw(img).ellipse((150, 250, 500, 600), fill=(30, 60, 200, 255))
        res = _detect_emblem_circle(img)
        self.assertIsNotNone(res)
        cx, cy, r = res
        self.assertAlmostEqual(cx, 325, delta=25)
        self.assertAlmostEqual(cy, 425, delta=25)
        self.assertAlmostEqual(r, 175, delta=30)

    def test_flat_image_falls_back_without_detection(self):
        img = Image.open(self.src)
        self.assertIsNone(_detect_emblem_circle(img))

    def test_pip_is_cached_until_the_source_changes(self):
        out = generate_energy_pip_png(self.src, "SWSH12", "169",
                                      out_dir=self.temp_dir)
        first_mtime = os.path.getmtime(out)
        again = generate_energy_pip_png(self.src, "SWSH12", "169",
                                        out_dir=self.temp_dir)
        self.assertEqual(out, again)
        self.assertEqual(os.path.getmtime(again), first_mtime)


if __name__ == "__main__":
    unittest.main()
