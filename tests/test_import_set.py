"""Unit tests for BW-era spirit.tools.import_set helpers."""

import os
import tempfile
import unittest
from unittest import mock

import spirit.tools.import_set as import_set


class MapAbilityTypeTests(unittest.TestCase):
    def test_poke_body_power_and_ability(self):
        self.assertEqual(
            import_set.map_ability_type("Poké-Body"), "AbilityTypes.POKE_BODY"
        )
        self.assertEqual(
            import_set.map_ability_type("Poké-Power"), "AbilityTypes.POKE_POWER"
        )
        self.assertEqual(
            import_set.map_ability_type("Ability"), "AbilityTypes.POKE_ABILITY"
        )

    def test_unknown_defaults_to_poke_ability(self):
        self.assertEqual(
            import_set.map_ability_type("Pokémon Power"),
            "AbilityTypes.POKE_ABILITY",
        )
        self.assertEqual(import_set.map_ability_type(None), "AbilityTypes.POKE_ABILITY")


class MapRarityTests(unittest.TestCase):
    def test_bw_era_rarities(self):
        self.assertEqual(import_set.map_rarity("Rare Holo EX"), "Rarities.RareHoloEX")
        self.assertEqual(import_set.map_rarity("Rare Prime"), "Rarities.RarePrime")
        self.assertEqual(import_set.map_rarity("LEGEND"), "Rarities.Legendary")
        self.assertEqual(import_set.map_rarity("Rare ACE"), "Rarities.Ace")
        self.assertEqual(import_set.map_rarity("Rare Secret"), "Rarities.RareSecret")

    def test_ex_does_not_fall_through_to_rare_holo(self):
        # Simulate an unmapped EX string: fallback must pick RareHoloEX.
        with mock.patch.dict(import_set.RARITY_MAP, {}, clear=True):
            self.assertEqual(
                import_set.map_rarity("Rare Holo EX"), "Rarities.RareHoloEX"
            )
            self.assertNotEqual(
                import_set.map_rarity("Rare Holo EX"), "Rarities.RareHolo"
            )


class RenderScriptBwTests(unittest.TestCase):
    def setUp(self):
        import_set.SET_CODE = "BW1"

    def test_ability_emits_ability_type(self):
        src = import_set.render_script({
            "id": "bw1-1",
            "name": "Serperior",
            "supertype": "Pokémon",
            "subtypes": ["Stage 2"],
            "hp": "140",
            "types": ["Grass"],
            "number": "5",
            "rarity": "Rare Holo",
            "convertedRetreatCost": 2,
            "nationalPokedexNumbers": [497],
            "abilities": [{
                "name": "Royal Heal",
                "text": "Heal 10 damage from each of your Pokémon.",
                "type": "Ability",
            }],
            "attacks": [],
        })
        self.assertIn("ability_type=AbilityTypes.POKE_ABILITY", src)
        self.assertIn("AbilityTypes", src.split("from spirit.game.attributes import ")[1])

    def test_poke_body_emits_poke_body(self):
        src = import_set.render_script({
            "id": "hgss1-1",
            "name": "Example",
            "supertype": "Pokémon",
            "subtypes": ["Basic"],
            "hp": "60",
            "types": ["Colorless"],
            "number": "1",
            "rarity": "Common",
            "convertedRetreatCost": 1,
            "abilities": [{
                "name": "Body",
                "text": "Does nothing.",
                "type": "Poké-Body",
            }],
            "attacks": [],
        })
        self.assertIn("ability_type=AbilityTypes.POKE_BODY", src)

    def test_ace_spec_item_keeps_subtype_and_item_def(self):
        src = import_set.render_script({
            "id": "bw7-137",
            "name": "Computer Search",
            "supertype": "Trainer",
            "subtypes": ["Item", "ACE SPEC"],
            "number": "137",
            "rarity": "Rare ACE",
            "rules": ["ACE SPEC card"],
        })
        self.assertIn("ItemCardDef", src)
        self.assertIn("Rarities.Ace", src)
        self.assertIn('"ACE SPEC"', src)
        self.assertIn("no AceSpecCardDef", src)

    def test_technical_machine_uses_trainer_card_def(self):
        src = import_set.render_script({
            "id": "dp6-1",
            "name": "Technical Machine TS-1",
            "supertype": "Trainer",
            "subtypes": ["Technical Machine"],
            "number": "1",
            "rarity": "Uncommon",
        })
        self.assertIn("TrainerCardDef", src)
        self.assertIn("trainer_type=TrainerType.TECHNICAL_MACHINE", src)
        self.assertIn("TrainerType", src)


class SkipExistingTests(unittest.TestCase):
    def test_skip_existing_preserves_hand_written_script(self):
        with tempfile.TemporaryDirectory() as tmp:
            scripts = os.path.join(tmp, "scripts")
            assets = os.path.join(tmp, "assets")
            os.makedirs(scripts)
            os.makedirs(assets)
            path = os.path.join(scripts, "Potion_100.py")
            with open(path, "w", encoding="utf-8") as f:
                f.write("# hand-written\n")

            import_set.SET_CODE = "BW1"
            import_set.SCRIPT_OUTPUT_DIR = scripts
            import_set.ASSET_OUTPUT_DIR = assets
            import_set.process_card(
                {
                    "id": "bw1-100",
                    "name": "Potion",
                    "supertype": "Trainer",
                    "subtypes": ["Item"],
                    "number": "100",
                    "rarity": "Common",
                },
                skip_existing=True,
            )
            with open(path, encoding="utf-8") as f:
                self.assertEqual(f.read(), "# hand-written\n")


if __name__ == "__main__":
    unittest.main()
