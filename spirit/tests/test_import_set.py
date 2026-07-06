"""Unit tests for the set importer's script generation (spirit/tools/import_set.py)."""

import unittest

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import unimplemented
from spirit.tools.import_set import fix_text, parse_damage, render_script

SAMPLE_POKEMON = {
    "id": "swsh12-4",
    "name": "Ariados",
    "supertype": "Pokémon",
    "subtypes": ["Stage 1"],
    "hp": "90",
    "types": ["Grass"],
    "evolvesFrom": "Spinarak",
    "abilities": [
        {"name": "Hidden Threads",
         "text": "Your opponent's PokÃ©mon VSTAR's attacks cost more.",
         "type": "Ability"},
    ],
    "attacks": [
        {"name": "Pierce", "cost": ["Grass", "Colorless"],
         "convertedEnergyCost": 2, "damage": "50", "text": ""},
        {"name": "Poison Sting", "cost": ["Grass"],
         "convertedEnergyCost": 1, "damage": "10+",
         "text": "Flip a coin. If heads, this attack does 20 more damage."},
    ],
    "weaknesses": [{"type": "Fire", "value": "Ã—2"}],
    "resistances": [{"type": "Fighting", "value": "-30"}],
    "retreatCost": ["Colorless"],
    "convertedRetreatCost": 1,
    "number": "4",
    "rarity": "Rare Holo",
    "nationalPokedexNumbers": [168],
    "images": {"large": "https://example.test/4.png"},
}


def exec_script(source: str):
    namespace = {}
    exec(compile(source, "<generated>", "exec"), namespace)
    return namespace["card"]


class TestHelpers(unittest.TestCase):
    def test_fix_text_repairs_mojibake(self):
        self.assertEqual(fix_text("PokÃ©mon"), "Pokémon")
        self.assertEqual(fix_text("plain text"), "plain text")

    def test_parse_damage(self):
        self.assertEqual(parse_damage("50"), (50, ""))
        self.assertEqual(parse_damage("10+"), (10, "+"))
        self.assertEqual(parse_damage("20×"), (20, "x"))
        self.assertEqual(parse_damage("220-"), (220, "-"))
        self.assertEqual(parse_damage(""), (0, ""))


class TestPokemonGeneration(unittest.TestCase):
    def setUp(self):
        self.card = exec_script(render_script(SAMPLE_POKEMON))

    def test_subtypes_imported(self):
        self.assertEqual(self.card.subtypes, ["Stage 1"])

    def test_vanilla_attack_auto_allocated(self):
        pierce = self.card.abilities[1]
        self.assertEqual(pierce.title, "Pierce")
        self.assertIsNone(pierce.effect)
        self.assertEqual(pierce.damage, 50)
        self.assertEqual(pierce.cost,
                         {PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1})

    def test_texted_attack_marked_unimplemented(self):
        sting = self.card.abilities[2]
        self.assertIs(sting.effect, unimplemented)
        self.assertEqual(sting.damage, 10)
        self.assertEqual(sting.damage_operator, "+")
        self.assertIn("Flip a coin", sting.game_text)

    def test_ability_marked_unimplemented_with_repaired_text(self):
        ability = self.card.abilities[0]
        self.assertIs(ability.effect, unimplemented)
        self.assertIn("Pokémon VSTAR", ability.game_text)

    def test_weakness_and_resistance_imported(self):
        attrs = self.card.to_archetype_dict()["attributes"]
        weakness = attrs[str(AttrID.WEAKNESS_TYPES.value)]["value"]
        self.assertEqual(weakness, f"[{PokemonTypes.FIRE.value}]")
        resistance = attrs[str(AttrID.RESISTANCE_TYPES.value)]["value"]
        self.assertEqual(resistance, PokemonTypes.FIGHTING.value)

        # Verify the operators and amounts are correctly serialized for the client
        self.assertEqual(attrs[str(AttrID.WEAKNESS_OPERATOR.value)]["value"], "x")
        self.assertEqual(attrs[str(AttrID.WEAKNESS_AMOUNT.value)]["value"], 2)
        self.assertEqual(attrs[str(AttrID.RESISTANCE_OPERATOR.value)]["value"], "-")
        self.assertEqual(attrs[str(AttrID.RESISTANCE_AMOUNT.value)]["value"], 30)

    def test_ability_ids_assigned_deterministically(self):
        for ability in self.card.abilities:
            self.assertIsNotNone(ability.ability_id)


class TestNonPokemonGeneration(unittest.TestCase):
    def test_trainer_renders_without_abilities(self):
        trainer = {
            "id": "swsh12-153", "name": "Capturing Aroma",
            "supertype": "Trainer", "subtypes": ["Item"],
            "rules": ["Flip a coin."], "number": "153", "rarity": "Uncommon",
        }
        card_src = render_script(trainer)
        self.assertIn("effect=unimplemented", card_src)
        self.assertIn("from spirit.game.data_utils import ItemCardDef, unimplemented", card_src)

        card = exec_script(card_src)
        self.assertEqual(card.collector_number, 153)
        self.assertIs(card.effect, unimplemented)
        self.assertEqual(card.subtypes, ["Item"])

    def test_energy_renders_with_subtypes(self):
        energy = {
            "id": "swsh12-156", "name": "V Guard Energy",
            "supertype": "Energy", "subtypes": ["Special"],
            "number": "156", "rarity": "Uncommon",
        }
        card_src = render_script(energy)
        self.assertIn("is_special=True", card_src)
        card = exec_script(card_src)
        self.assertEqual(card.subtypes, ["Special"])


if __name__ == "__main__":
    unittest.main()
