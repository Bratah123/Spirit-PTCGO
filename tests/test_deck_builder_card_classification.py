"""Deck-builder tab classification (attr 200300 CardType only).

The Unity deck builder bins cards by Cake CardType member NAME. Sending our
internal IntEnum ordinals mis-bins Trainers onto the Energy tab. These tests
pin CARD_TYPE wire form to Cake names while leaving Stage/TrainerType/Rarity/
PokemonTypes/EnergyInfo serialization as upstream ints/JSON ordinals.
"""
import json
import unittest
import uuid

from spirit.game.attributes import (
    AttrID, CardType, PokemonStage, PokemonTypes, Rarities, TrainerType,
)
from spirit.game.content.definitions import (
    EnergyCardDef, PokemonCardDef, ItemCardDef, Attack,
)
from spirit.game.models.card import Card, PokemonCard, apply_client_card_type
from spirit.game.scripts.cards import loader as card_loader


def _attr(attrs, attr_id):
    return attrs[str(attr_id.value)]


def _card_from_def(card_def):
    """Mirror scripts.cards.CardLoader._add_card without mutating the loader."""
    archetype = card_def.to_archetype_dict()
    c_type = archetype["attributes"].get(
        str(AttrID.CARD_TYPE.value), {},
    ).get("value", CardType.UNSET)
    model = PokemonCard if c_type == CardType.POKEMON else Card
    return model(
        archetype["guid"], archetype["key"], archetype["attributes"],
        archetype.get("display_name"), archetype.get("searchable_by", []),
        getattr(card_def, "subtypes", []),
    )


class ClientCardTypeUnitTests(unittest.TestCase):
    def test_card_type_ordinals_become_client_names(self):
        # Internal TRAINER=2 must ship as the documented TrainerCard name.
        attrs = apply_client_card_type({
            str(AttrID.CARD_TYPE.value): {
                "type": "int", "value": CardType.TRAINER.value,
            },
            str(AttrID.TRAINER_TYPE.value): {
                "type": "int", "value": TrainerType.ITEM.value,
            },
        })
        self.assertEqual(_attr(attrs, AttrID.CARD_TYPE), {
            "type": "string", "value": "TrainerCard",
        })
        # Unrelated attrs stay numeric / untouched.
        self.assertEqual(_attr(attrs, AttrID.TRAINER_TYPE), {
            "type": "int", "value": TrainerType.ITEM.value,
        })

    def test_legend_half_and_energy_names(self):
        for ct, name in (
            (CardType.ENERGY, "Energy"),
            (CardType.POKEMON, "Pokemon"),
            (CardType.LEGEND_HALF, "LegendHalf"),
            (CardType.TRAINER, "TrainerCard"),
        ):
            attrs = apply_client_card_type({
                str(AttrID.CARD_TYPE.value): {"type": "int", "value": ct.value},
            })
            self.assertEqual(_attr(attrs, AttrID.CARD_TYPE)["value"], name)

    def test_idempotent_on_existing_client_name(self):
        attrs = apply_client_card_type({
            str(AttrID.CARD_TYPE.value): {"type": "string", "value": "Energy"},
        })
        self.assertEqual(_attr(attrs, AttrID.CARD_TYPE), {
            "type": "string", "value": "Energy",
        })


class DeckBuilderClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()

    def _wire(self, card):
        return card.to_archetype_attributes(card.key)

    def test_basic_energy_classified_as_energy(self):
        card = next(
            c for c in card_loader.cards
            if c.key == "Free_Energy"
            and not c.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)
        )
        # Internal storage stays numeric for engine logic.
        self.assertEqual(
            card.get_attribute_value(AttrID.CARD_TYPE), CardType.ENERGY.value,
        )
        wire = self._wire(card)
        self.assertEqual(_attr(wire, AttrID.CARD_TYPE), {
            "type": "string", "value": "Energy",
        })
        self.assertNotIn(str(AttrID.TRAINER_TYPE.value), wire)
        # EnergyInfo stays upstream ordinal JSON (not name-normalized).
        info = json.loads(_attr(wire, AttrID.ENERGY_INFO)["value"])
        self.assertTrue(info["options"])
        self.assertTrue(all(
            isinstance(t, int) for option in info["options"] for t in option
        ))
        self.assertIsNone(card.get_attribute_value(AttrID.IS_SPECIAL_ENERGY))

    def test_special_energy_classified_as_energy(self):
        card = next(
            c for c in card_loader.cards
            if c.get_attribute_value(AttrID.CARD_TYPE) == CardType.ENERGY.value
            and c.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)
        )
        wire = self._wire(card)
        self.assertEqual(_attr(wire, AttrID.CARD_TYPE)["value"], "Energy")
        self.assertTrue(card.get_attribute_value(AttrID.IS_SPECIAL_ENERGY))
        info = json.loads(_attr(wire, AttrID.ENERGY_INFO)["value"])
        self.assertTrue(all(
            isinstance(t, int) for option in info["options"] for t in option
        ))

    def test_trainer_not_on_energy_tab(self):
        card = next(
            c for c in card_loader.cards
            if c.get_attribute_value(AttrID.CARD_TYPE) == CardType.TRAINER.value
        )
        wire = self._wire(card)
        self.assertEqual(_attr(wire, AttrID.CARD_TYPE), {
            "type": "string", "value": "TrainerCard",
        })
        self.assertNotEqual(_attr(wire, AttrID.CARD_TYPE)["value"], "Energy")
        self.assertNotEqual(
            _attr(wire, AttrID.CARD_TYPE).get("value"), CardType.ENERGY.value,
        )
        # TrainerType stays upstream int.
        trainer_type = _attr(wire, AttrID.TRAINER_TYPE)
        self.assertEqual(trainer_type["type"], "int")
        self.assertIsInstance(trainer_type["value"], int)

    def test_pokemon_classified_as_pokemon(self):
        card = next(
            c for c in card_loader.cards
            if c.get_attribute_value(AttrID.CARD_TYPE) == CardType.POKEMON.value
        )
        self.assertIsInstance(card, PokemonCard)
        wire = self._wire(card)
        self.assertEqual(_attr(wire, AttrID.CARD_TYPE), {
            "type": "string", "value": "Pokemon",
        })
        # Stage / types / rarity remain upstream ordinals.
        stage = _attr(wire, AttrID.STAGE)
        self.assertEqual(stage["type"], "int")
        self.assertIsInstance(stage["value"], int)
        types = json.loads(_attr(wire, AttrID.POKEMON_TYPES)["value"])
        self.assertTrue(types)
        self.assertTrue(all(isinstance(t, int) for t in types))
        rarity = _attr(wire, AttrID.RARITY)
        self.assertEqual(rarity["type"], "int")
        self.assertIsInstance(rarity["value"], int)

    def test_legend_half_classified_as_legend_half(self):
        half = Card(
            str(uuid.uuid4()), "TEST",
            {
                str(AttrID.CARD_TYPE.value): {
                    "type": "int", "value": CardType.LEGEND_HALF.value,
                },
                str(AttrID.STAGE.value): {
                    "type": "int", "value": PokemonStage.LEGEND.value,
                },
                str(AttrID.NAME.value): {"type": "string", "value": "test.LegendHalf"},
                str(AttrID.RARITY.value): {
                    "type": "int", "value": Rarities.RareHolo.value,
                },
            },
        )
        self.assertEqual(
            half.get_attribute_value(AttrID.CARD_TYPE), CardType.LEGEND_HALF.value,
        )
        wire = half.to_archetype_attributes("TEST")
        self.assertEqual(_attr(wire, AttrID.CARD_TYPE), {
            "type": "string", "value": "LegendHalf",
        })
        self.assertEqual(_attr(wire, AttrID.STAGE)["type"], "int")
        self.assertEqual(_attr(wire, AttrID.STAGE)["value"], PokemonStage.LEGEND.value)

    def test_repeated_serialization_stable_and_internals_unchanged(self):
        energy = next(
            c for c in card_loader.cards
            if c.key == "Free_Energy"
            and not c.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)
        )
        trainer = next(
            c for c in card_loader.cards
            if c.get_attribute_value(AttrID.CARD_TYPE) == CardType.TRAINER.value
        )
        pokemon = next(
            c for c in card_loader.cards
            if isinstance(c, PokemonCard)
        )
        for card, expected in (
            (energy, "Energy"),
            (trainer, "TrainerCard"),
            (pokemon, "Pokemon"),
        ):
            internal_before = card.get_attribute_value(AttrID.CARD_TYPE)
            first = card.to_archetype_attributes(card.key)
            second = card.to_archetype_attributes(card.key)
            self.assertEqual(_attr(first, AttrID.CARD_TYPE)["value"], expected)
            self.assertEqual(
                _attr(first, AttrID.CARD_TYPE), _attr(second, AttrID.CARD_TYPE),
            )
            self.assertEqual(
                card.get_attribute_value(AttrID.CARD_TYPE), internal_before,
            )
            self.assertIsInstance(
                card.get_attribute_value(AttrID.CARD_TYPE), int,
            )

    def test_synthetic_defs_card_type_names_only(self):
        basic = _card_from_def(EnergyCardDef(
            guid=str(uuid.uuid4()), key="TEST", name="test.BasicEnergy",
            collector_number=1, set_code="TEST", rarity=Rarities.Common,
            energy_type=PokemonTypes.FIRE,
        ))
        special = _card_from_def(EnergyCardDef(
            guid=str(uuid.uuid4()), key="TEST", name="test.SpecialEnergy",
            collector_number=2, set_code="TEST", rarity=Rarities.Uncommon,
            energy_type=PokemonTypes.COLORLESS, is_special=True,
            provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
        ))
        trainer = _card_from_def(ItemCardDef(
            guid=str(uuid.uuid4()), key="TEST", name="test.Item",
            collector_number=3, set_code="TEST", rarity=Rarities.Common,
        ))
        pokemon = _card_from_def(PokemonCardDef(
            guid=str(uuid.uuid4()), key="TEST", name="test.Pokemon",
            collector_number=4, set_code="TEST", rarity=Rarities.Rare,
            hp=60, stage=PokemonStage.BASIC,
            elements=[PokemonTypes.GRASS],
            abilities=[Attack("Tackle", cost={PokemonTypes.COLORLESS: 1}, damage=10)],
        ))

        self.assertEqual(
            _attr(basic.to_archetype_attributes("TEST"), AttrID.CARD_TYPE)["value"],
            "Energy",
        )
        special_wire = special.to_archetype_attributes("TEST")
        self.assertEqual(_attr(special_wire, AttrID.CARD_TYPE)["value"], "Energy")
        self.assertEqual(
            json.loads(_attr(special_wire, AttrID.ENERGY_INFO)["value"]),
            {"options": [[PokemonTypes.COLORLESS.value, PokemonTypes.COLORLESS.value]]},
        )
        self.assertTrue(special.get_attribute_value(AttrID.IS_SPECIAL_ENERGY))
        self.assertEqual(
            _attr(trainer.to_archetype_attributes("TEST"), AttrID.CARD_TYPE)["value"],
            "TrainerCard",
        )
        poke_wire = pokemon.to_archetype_attributes("TEST")
        self.assertEqual(_attr(poke_wire, AttrID.CARD_TYPE)["value"], "Pokemon")
        self.assertEqual(_attr(poke_wire, AttrID.STAGE)["type"], "int")
        self.assertIsInstance(pokemon, PokemonCard)
        self.assertIsInstance(basic, Card)


if __name__ == "__main__":
    unittest.main()
