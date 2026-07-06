import os
import shutil
import tempfile
import unittest

from spirit.tools.effect_coverage import scan_cards, group_work_items, triage


VANILLA_ATTACK = """from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11111111-1111-1111-1111-111111111111",
    key="SETA",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ratata.Name",
    collector_number=1,
    set_code="SETA",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Attack(title="Tackle", cost={PokemonTypes.COLORLESS: 1}, damage=10),
    ],
)
"""

STUB_ATTACK = """from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="22222222-2222-2222-2222-222222222222",
    key="{key}",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drawmon.Name",
    collector_number={num},
    set_code="{key}",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Attack(
            title="Card Fetch",
            game_text="Draw 2 cards.",
            cost={{PokemonTypes.COLORLESS: 1}},
            effect=unimplemented,
        ),
    ],
)
"""

STUB_TRAINER = """from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="33333333-3333-3333-3333-333333333333",
    key="SETA",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    collector_number=99,
    set_code="SETA",
    rarity=Rarities.Common,
    effect=unimplemented
)
"""


class TestEffectCoverage(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.set_a = os.path.join(self.tmp_dir, "SETA")
        self.set_b = os.path.join(self.tmp_dir, "SETB")
        os.makedirs(self.set_a)
        os.makedirs(self.set_b)

        with open(os.path.join(self.set_a, "Ratata_1.py"), "w") as f:
            f.write(VANILLA_ATTACK)
        with open(os.path.join(self.set_a, "Drawmon_2.py"), "w") as f:
            f.write(STUB_ATTACK.format(key="SETA", num=2))
        with open(os.path.join(self.set_b, "Drawmon_2.py"), "w") as f:
            f.write(STUB_ATTACK.format(key="SETB", num=2))
        with open(os.path.join(self.set_a, "Potion_99.py"), "w") as f:
            f.write(STUB_TRAINER)

        # Should be skipped by the scanner (non-script / dunder file).
        with open(os.path.join(self.set_a, "__init__.py"), "w") as f:
            f.write("")

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def test_scan_counts_scripts_and_flags_stubs(self):
        infos = scan_cards(cards_root=self.tmp_dir)
        self.assertEqual(len(infos), 4)

        by_name = {(i.set_code, i.card_name): i for i in infos}
        self.assertFalse(by_name[("SETA", "Ratata")].is_stub)
        self.assertTrue(by_name[("SETA", "Drawmon")].is_stub)
        self.assertTrue(by_name[("SETA", "Potion")].is_stub)
        self.assertEqual(by_name[("SETA", "Potion")].signature, ())
        self.assertEqual(by_name[("SETA", "Potion")].card_class, "ItemCardDef")

    def test_reprints_dedupe_into_one_work_item(self):
        infos = scan_cards(cards_root=self.tmp_dir)
        work_items = group_work_items(infos)

        drawmon_items = [w for w in work_items if w.card_name == "Drawmon"]
        self.assertEqual(len(drawmon_items), 1)
        self.assertEqual(drawmon_items[0].script_count, 2)
        covered_sets = {s.set_code for s in drawmon_items[0].scripts}
        self.assertEqual(covered_sets, {"SETA", "SETB"})

        # Vanilla card produced no work item at all.
        self.assertFalse([w for w in work_items if w.card_name == "Ratata"])

    def test_triage_keyword_matching(self):
        self.assertEqual(triage(("draw 2 cards.",)), "search-draw")
        self.assertEqual(triage(("flip a coin. if heads, do 20 more damage.",)), "coin-flip")
        self.assertEqual(triage(("heal 30 damage from this pokemon.",)), "heal")
        self.assertEqual(triage(()), "other")

    def test_set_filter(self):
        infos = scan_cards(cards_root=self.tmp_dir, only_set="SETB")
        self.assertEqual(len(infos), 1)
        self.assertEqual(infos[0].set_code, "SETB")

    def test_work_item_json_shape(self):
        infos = scan_cards(cards_root=self.tmp_dir)
        work_items = group_work_items(infos)
        potion_item = next(w for w in work_items if w.card_name == "Potion")
        d = potion_item.to_dict()
        self.assertEqual(d["card_class"], "ItemCardDef")
        self.assertEqual(d["category"], "other")
        self.assertEqual(d["script_count"], 1)
        self.assertEqual(d["covered"], [{"set": "SETA", "number": 99}])


if __name__ == "__main__":
    unittest.main()
