import unittest
import json
from spirit.game.attributes import AttrID, PokemonTypes, CardType, PokemonStage
from spirit.game.data_utils import PokemonCardDef
from spirit.game.models.card import PokemonCard

class TestWeaknessResistance(unittest.TestCase):
    def test_pokemon_card_def_serializes_weakness_resistance_operators_and_amounts(self):
        # 1. Define a Pokemon with weakness and resistance
        card_def = PokemonCardDef(
            guid="test-pokemon-guid",
            key="BW1",
            name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
            collector_number=79,
            set_code="BW1",
            rarity=1,
            hp=90,
            elements=[PokemonTypes.COLORLESS],
            stage=PokemonStage.STAGE1,
            retreat_cost=1,
            weakness_type=PokemonTypes.FIGHTING,
            weakness_amount=2,
            resistance_type=PokemonTypes.PSYCHIC,
            resistance_amount=30
        )

        archetype = card_def.to_archetype_dict()
        attrs = archetype["attributes"]

        # Verify weakness attributes are serialized correctly
        self.assertEqual(attrs[str(AttrID.WEAKNESS_TYPES.value)]["value"], f"[{PokemonTypes.FIGHTING.value}]")
        self.assertEqual(attrs[str(AttrID.WEAKNESS_OPERATOR.value)]["value"], "x")
        self.assertEqual(attrs[str(AttrID.WEAKNESS_AMOUNT.value)]["value"], 2)

        # Verify resistance attributes are serialized correctly
        self.assertEqual(attrs[str(AttrID.RESISTANCE_TYPES.value)]["value"], PokemonTypes.PSYCHIC.value)
        self.assertEqual(attrs[str(AttrID.RESISTANCE_OPERATOR.value)]["value"], "-")
        self.assertEqual(attrs[str(AttrID.RESISTANCE_AMOUNT.value)]["value"], 30)

    def test_pokemon_card_model_dynamic_operator_and_amount_fallbacks(self):
        # 1. Set up attributes representing a loaded Pokemon card with weakness/resistance but missing operators/amounts
        attributes = {
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.POKEMON.value},
            str(AttrID.HP.value): {"type": "int", "value": 90},
            str(AttrID.STAGE.value): {"type": "int", "value": PokemonStage.STAGE1.value},
            str(AttrID.POKEMON_TYPES.value): {"type": "json", "value": json.dumps([PokemonTypes.COLORLESS.value])},
            str(AttrID.RETREAT_COST.value): {"type": "int", "value": 1},
            str(AttrID.WEAKNESS_TYPES.value): {"type": "json", "value": json.dumps([PokemonTypes.FIGHTING.value])},
            str(AttrID.RESISTANCE_TYPES.value): {"type": "int", "value": PokemonTypes.PSYCHIC.value},
        }

        pokemon_card = PokemonCard(guid="test-dynamic-guid", key="BW1", attributes=attributes)

        # Convert to archetype attributes
        final_attrs = pokemon_card.to_archetype_attributes(download_key="BW1")

        # Verify that weakness and resistance operators and amounts were dynamically added as fallbacks
        self.assertEqual(final_attrs[str(AttrID.WEAKNESS_OPERATOR.value)]["value"], "x")
        self.assertEqual(final_attrs[str(AttrID.WEAKNESS_AMOUNT.value)]["value"], 2)
        self.assertEqual(final_attrs[str(AttrID.RESISTANCE_OPERATOR.value)]["value"], "-")
        self.assertEqual(final_attrs[str(AttrID.RESISTANCE_AMOUNT.value)]["value"], 30)

    def test_pokemon_card_model_does_not_add_fallbacks_when_unset(self):
        # 1. Set up a Pokemon with NO weakness and NO resistance
        attributes = {
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.POKEMON.value},
            str(AttrID.HP.value): {"type": "int", "value": 90},
            str(AttrID.STAGE.value): {"type": "int", "value": PokemonStage.BASIC.value},
            str(AttrID.POKEMON_TYPES.value): {"type": "json", "value": json.dumps([PokemonTypes.COLORLESS.value])},
            str(AttrID.RETREAT_COST.value): {"type": "int", "value": 1},
            str(AttrID.WEAKNESS_TYPES.value): {"type": "json", "value": "[]"},
            str(AttrID.RESISTANCE_TYPES.value): {"type": "int", "value": PokemonTypes.UNSET.value},
        }

        pokemon_card = PokemonCard(guid="test-dynamic-guid", key="BW1", attributes=attributes)

        final_attrs = pokemon_card.to_archetype_attributes(download_key="BW1")

        # Verify operators and amounts are NOT added when weakness or resistance are unset
        self.assertNotIn(str(AttrID.WEAKNESS_OPERATOR.value), final_attrs)
        self.assertNotIn(str(AttrID.WEAKNESS_AMOUNT.value), final_attrs)
        self.assertNotIn(str(AttrID.RESISTANCE_OPERATOR.value), final_attrs)
        self.assertNotIn(str(AttrID.RESISTANCE_AMOUNT.value), final_attrs)

    def test_evolution_logic_name_always_populated_on_non_pokemon_defs(self):
        from spirit.game.data_utils import ItemCardDef, EnergyCardDef
        
        # 1. Test Trainer Def
        trainer_def = ItemCardDef(
            guid="test-trainer-guid",
            key="BW1",
            name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
            collector_number=100,
            set_code="BW1",
            rarity=0
        )
        trainer_arch = trainer_def.to_archetype_dict()
        self.assertEqual(trainer_arch["attributes"][str(AttrID.EVOLUTION_LOGIC_NAME.value)]["value"], "Potion")

        # 2. Test Energy Def
        energy_def = EnergyCardDef(
            guid="test-energy-guid",
            key="BW1",
            name="com.direwolfdigital.cake.data.archetypes.energy.DoubleColorless.Name",
            collector_number=101,
            set_code="BW1",
            rarity=0,
            energy_type=PokemonTypes.COLORLESS,
            is_special=True
        )
        energy_arch = energy_def.to_archetype_dict()
        self.assertEqual(energy_arch["attributes"][str(AttrID.EVOLUTION_LOGIC_NAME.value)]["value"], "DoubleColorless")

    def test_evolution_logic_name_always_populated_on_non_pokemon_models(self):
        from spirit.game.models.card import Card
        
        # Setup loaded attributes without EVOLUTION_LOGIC_NAME
        attributes = {
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.ENERGY.value},
            str(AttrID.NAME.value): {"type": "json", "value": json.dumps({"id": "DoubleColorless"})},
        }
        card = Card(guid="test-energy-model", key="BW1", attributes=attributes)
        final_attrs = card.to_archetype_attributes(download_key="BW1")
        
        # Verify it got added dynamically
        self.assertIn(str(AttrID.EVOLUTION_LOGIC_NAME.value), final_attrs)
        self.assertEqual(final_attrs[str(AttrID.EVOLUTION_LOGIC_NAME.value)]["value"], "DoubleColorless")

if __name__ == "__main__":
    unittest.main()
