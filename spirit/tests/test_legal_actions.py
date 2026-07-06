"""Unit tests for the main-turn legal-action engine (legal_actions.py)."""

import unittest

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import (
    Attack,
    EnergyCardDef,
    ItemCardDef,
    PokemonCardDef,
    SupporterCardDef,
    ability_id_for,
)
from spirit.game.models.board import BoardState, create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.constants import SelectionKind
from spirit.game.session.legal_actions import (
    ACTION_EVOLVE,
    ACTION_PLAY_ENERGY,
    ACTION_PLAY_POKEMON,
    ACTION_RETREAT,
    ACTION_USE_ATTACK,
    ACTION_USE_TRAINER,
    TurnState,
    attack_cost_satisfied,
    compute_legal_actions,
    energy_provided_count,
)

P1 = "player-1"
P2 = "player-2"
GAME_ID = "test-game"


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


BASIC_POKEMON = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000b1",
    key="BW1", name="com.test.pokemon.Patrat.Name",
    collector_number=1, set_code="BW1", rarity=1,
    hp=60, elements=[PokemonTypes.COLORLESS],
    abilities=[
        Attack("Tackle", "tackle.text", {PokemonTypes.COLORLESS: 1}, damage=10),
        Attack("Big Bite", "bite.text",
               {PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30),
    ],
))

STAGE1_POKEMON = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000s1",
    key="BW1", name="com.test.pokemon.Watchog.Name",
    collector_number=2, set_code="BW1", rarity=2,
    hp=90, elements=[PokemonTypes.COLORLESS], stage=__import__(
        "spirit.game.attributes", fromlist=["PokemonStage"]).PokemonStage.STAGE1,
    evolves_from="com.test.pokemon.Patrat.Name",
))

FIRE_ENERGY = make_card(EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000e1",
    key="BW1", name="com.test.energy.Fire.Name",
    collector_number=106, set_code="BW1", rarity=0,
    energy_type=PokemonTypes.FIRE,
))

ITEM_CARD = make_card(ItemCardDef(
    guid="00000000-0000-0000-0000-0000000000i1",
    key="BW1", name="com.test.trainer.Potion.Name",
    collector_number=100, set_code="BW1", rarity=0,
))

SUPPORTER_CARD = make_card(SupporterCardDef(
    guid="00000000-0000-0000-0000-0000000000su",
    key="BW1", name="com.test.trainer.Cheren.Name",
    collector_number=101, set_code="BW1", rarity=0,
))


class LegalActionsTestBase(unittest.TestCase):
    def setUp(self):
        self.board = BoardState(GAME_ID, [P1, P2])
        self.state = TurnState()

    def add_to(self, area_name: str, card: Card, player_id: str = P1):
        entity = create_card_entity(card, owning_player_id=player_id)
        area = self.board.find_player_area(player_id, area_name)
        self.board.add_card_to_area(entity, area)
        return entity

    def actions(self, player_id: str = P1):
        return compute_legal_actions(self.board, self.state, player_id, GAME_ID)

    def actions_for(self, entity, player_id: str = P1):
        return [
            e for e in self.actions(player_id)
            if e["entityID"] == entity.entity_id
        ]


class TestPokemonPlays(LegalActionsTestBase):
    def test_basic_playable_while_bench_has_space(self):
        basic = self.add_to("hand", BASIC_POKEMON)
        self.state.begin_turn(P1)

        entries = self.actions_for(basic)
        self.assertEqual(len(entries), 1)
        action = entries[0]["selectableAction"]
        self.assertEqual(action["description"], ACTION_PLAY_POKEMON)
        self.assertEqual(action["selectionType"], "Ability")
        bench = self.board.find_player_area(P1, "bench")
        info = entries[0]["targetInfoLst"][0]
        self.assertEqual(info["validTargets"], [bench.entity_id])

    def test_basic_not_playable_with_full_bench(self):
        basic = self.add_to("hand", BASIC_POKEMON)
        for _ in range(BENCH_CAPACITY):
            self.add_to("bench", BASIC_POKEMON)
        self.state.begin_turn(P1)

        self.assertEqual(self.actions_for(basic), [])

    def test_evolution_requires_settled_target_and_turn_three(self):
        stage1 = self.add_to("hand", STAGE1_POKEMON)
        target = self.add_to("activePokemonArea", BASIC_POKEMON)

        # Turn 1: never evolvable.
        self.state.begin_turn(P1)
        self.assertEqual(self.actions_for(stage1), [])

        # Turn 3 (both players have had a turn), target from setup (turn 0).
        self.state.begin_turn(P2)
        self.state.begin_turn(P1)
        entries = self.actions_for(stage1)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["selectableAction"]["description"], ACTION_EVOLVE)
        info = entries[0]["targetInfoLst"][0]
        self.assertEqual(info["name"], "EntityListTargetInformation")
        self.assertEqual(info["validTargets"], [target.entity_id])

    def test_pokemon_played_this_turn_cannot_evolve(self):
        stage1 = self.add_to("hand", STAGE1_POKEMON)
        target = self.add_to("bench", BASIC_POKEMON)
        self.state.begin_turn(P1)
        self.state.begin_turn(P2)
        self.state.begin_turn(P1)
        self.state.mark_entered_play(target.entity_id)  # benched this turn

        self.assertEqual(self.actions_for(stage1), [])


class TestEnergyPlays(LegalActionsTestBase):
    def test_energy_attach_offered_once_per_turn(self):
        energy = self.add_to("hand", FIRE_ENERGY)
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        benched = self.add_to("bench", BASIC_POKEMON)
        self.state.begin_turn(P1)

        entries = self.actions_for(energy)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["selectableAction"]["description"], ACTION_PLAY_ENERGY)
        self.assertCountEqual(
            entries[0]["targetInfoLst"][0]["validTargets"],
            [active.entity_id, benched.entity_id],
        )

        self.state.energy_attached = True
        self.assertEqual(self.actions_for(energy), [])

    def test_energy_needs_a_pokemon_in_play(self):
        energy = self.add_to("hand", FIRE_ENERGY)
        self.state.begin_turn(P1)
        self.assertEqual(self.actions_for(energy), [])


class TestTrainerPlays(LegalActionsTestBase):
    def test_item_always_playable_supporter_once_and_not_turn_one(self):
        item = self.add_to("hand", ITEM_CARD)
        supporter = self.add_to("hand", SUPPORTER_CARD)

        self.state.begin_turn(P1)  # turn 1
        self.assertEqual(len(self.actions_for(item)), 1)
        self.assertEqual(self.actions_for(supporter), [])

        self.state.begin_turn(P2)  # turn 2
        entries = self.actions_for(supporter, P1)
        # Not P1's turn state anymore, but legality is computed per player id;
        # supporter is allowed from turn 2 onward when the flag is clear.
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["selectableAction"]["description"], ACTION_USE_TRAINER)

        self.state.supporter_played = True
        self.assertEqual(self.actions_for(supporter, P1), [])
        self.assertEqual(len(self.actions_for(item, P1)), 1)


class TestAttacks(LegalActionsTestBase):
    def attach_energy(self, pokemon, energy_card, player_id: str = P1):
        entity = create_card_entity(energy_card, owning_player_id=player_id)
        area = self.board.find_player_area(player_id, "discard")
        self.board.add_card_to_area(entity, area)  # register in cache
        self.board.attach_card(entity.entity_id, pokemon.entity_id)
        return entity

    def advance_to_turn(self, n: int, player_id: str = P1):
        for _ in range(n - 1):
            self.state.begin_turn(P2)
        self.state.begin_turn(player_id)

    def test_attack_offered_when_cost_met(self):
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        self.advance_to_turn(3)

        # No energy: no attacks.
        self.assertEqual(self.actions_for(active), [])

        # One fire energy pays Tackle (1 colorless) but not Big Bite (F+C).
        self.attach_energy(active, FIRE_ENERGY)
        entries = self.actions_for(active)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["selectableAction"]["description"], ACTION_USE_ATTACK)
        # Attacks open the K.O ability panel, not the j.V play-from-hand flow.
        self.assertEqual(entries[0]["selectableAction"]["selectionType"], "AbilitySelection")
        self.assertEqual(
            entries[0]["selectableAction"]["actionID"],
            ability_id_for(BASIC_POKEMON.guid, 0),
        )

        # Second fire energy also pays Big Bite.
        self.attach_energy(active, FIRE_ENERGY)
        entries = self.actions_for(active)
        self.assertEqual(len(entries), 2)

    def test_benched_pokemon_do_not_offer_attacks(self):
        benched = self.add_to("bench", BASIC_POKEMON)
        self.attach_energy(benched, FIRE_ENERGY)
        self.advance_to_turn(3)
        self.assertEqual(self.actions_for(benched), [])

    def test_no_attacks_on_the_games_first_turn(self):
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        self.attach_energy(active, FIRE_ENERGY)

        # Turn 1: the player going first cannot attack.
        self.state.begin_turn(P1)
        self.assertEqual(self.actions_for(active), [])

        # Turn 2: the second player can.
        self.state.begin_turn(P2)
        p2_active = self.add_to("activePokemonArea", BASIC_POKEMON, P2)
        self.attach_energy(p2_active, FIRE_ENERGY, P2)
        entries = [
            e for e in self.actions(P2)
            if e["entityID"] == p2_active.entity_id
        ]
        self.assertEqual(len(entries), 1)


FREE_RETREATER = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000fr",
    key="BW1", name="com.test.pokemon.Emolga.Name",
    collector_number=5, set_code="BW1", rarity=1,
    hp=70, elements=[PokemonTypes.LIGHTNING],
    retreat_cost=0,
))


class TestRetreat(LegalActionsTestBase):
    def attach_energy(self, pokemon, energy_card=FIRE_ENERGY):
        entity = create_card_entity(energy_card, owning_player_id=P1)
        self.board.add_card_to_area(entity, self.board.find_player_area(P1, "discard"))
        self.board.attach_card(entity.entity_id, pokemon.entity_id)
        return entity

    def retreat_entries(self, entity):
        return [
            e for e in self.actions_for(entity)
            if e["selectableAction"]["description"] == ACTION_RETREAT
        ]

    def test_retreat_offered_with_bench_and_paid_cost(self):
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        benched = self.add_to("bench", BASIC_POKEMON)
        energy = self.attach_energy(active)
        self.state.begin_turn(P1)

        entries = self.retreat_entries(active)
        self.assertEqual(len(entries), 1)
        action = entries[0]["selectableAction"]
        # Retreat rides the K.O pulled-back panel next to the attacks.
        self.assertEqual(action["selectionType"], "AbilitySelection")
        infos = entries[0]["targetInfoLst"]
        self.assertEqual(len(infos), 2)
        # New active first, cost last: the Done button only renders on the
        # final node, and the pip tray label reads the cost node's prompt.
        new_active_info, cost_info = infos
        self.assertEqual(new_active_info["name"], SelectionKind.RETREAT_NEW_ACTIVE.value)
        self.assertEqual(new_active_info["validTargets"], [benched.entity_id])
        self.assertTrue(new_active_info["targetPrompt"]["id"])
        self.assertEqual(cost_info["name"], SelectionKind.RETREAT_COST_ENTITY_LIST.value)
        self.assertEqual(cost_info["validTargets"], [energy.entity_id])
        self.assertEqual(cost_info["valueToSelect"], 1)
        self.assertEqual(cost_info["numberToSelect"], 1)
        self.assertTrue(cost_info["targetPrompt"]["id"])

    def test_retreat_needs_a_benched_pokemon(self):
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        self.attach_energy(active)
        self.state.begin_turn(P1)
        self.assertEqual(self.retreat_entries(active), [])

    def test_retreat_needs_the_cost_paid(self):
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        self.add_to("bench", BASIC_POKEMON)
        self.state.begin_turn(P1)
        self.assertEqual(self.retreat_entries(active), [])

    def test_retreat_only_once_per_turn(self):
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        self.add_to("bench", BASIC_POKEMON)
        self.attach_energy(active)
        self.state.begin_turn(P1)
        self.assertEqual(len(self.retreat_entries(active)), 1)

        self.state.retreated = True
        self.assertEqual(self.retreat_entries(active), [])

        self.state.begin_turn(P2)
        self.state.begin_turn(P1)  # flag resets each turn
        self.assertEqual(len(self.retreat_entries(active)), 1)

    def test_free_retreat_skips_the_cost_node(self):
        active = self.add_to("activePokemonArea", FREE_RETREATER)
        benched = self.add_to("bench", BASIC_POKEMON)
        self.state.begin_turn(P1)

        entries = self.retreat_entries(active)
        self.assertEqual(len(entries), 1)
        infos = entries[0]["targetInfoLst"]
        self.assertEqual(len(infos), 1)
        self.assertEqual(infos[0]["name"], SelectionKind.RETREAT_NEW_ACTIVE.value)
        self.assertEqual(infos[0]["validTargets"], [benched.entity_id])

    def test_double_energy_pays_two_retreat_cost(self):
        two_cost = make_card(PokemonCardDef(
            guid="00000000-0000-0000-0000-0000000000r2",
            key="BW1", name="com.test.pokemon.Stoutland.Name",
            collector_number=6, set_code="BW1", rarity=2,
            hp=130, elements=[PokemonTypes.COLORLESS], retreat_cost=2,
        ))
        active = self.add_to("activePokemonArea", two_cost)
        self.add_to("bench", BASIC_POKEMON)
        double = self.attach_energy(active)
        # One card providing two energy (client tallies EnergyProvidedCount).
        double.set_attribute(AttrID.ENERGY_INFO, {
            "options": [[PokemonTypes.COLORLESS.value, PokemonTypes.COLORLESS.value]]
        })
        self.state.begin_turn(P1)

        self.assertEqual(energy_provided_count(double), 2)
        entries = self.retreat_entries(active)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["targetInfoLst"][1]["valueToSelect"], 2)


class TestAttackCostSatisfied(unittest.TestCase):
    def energy_entities(self, *types):
        entities = []
        for t in types:
            card = make_card(EnergyCardDef(
                guid=f"00000000-0000-0000-0000-00000000{t.value:04d}",
                key="BW1", name=f"com.test.energy.{t.name}.Name",
                collector_number=200 + t.value, set_code="BW1", rarity=0,
                energy_type=t,
            ))
            entities.append(create_card_entity(card, owning_player_id=P1))
        return entities

    def test_typed_and_colorless_costs(self):
        energies = self.energy_entities(PokemonTypes.FIRE, PokemonTypes.WATER)

        self.assertTrue(attack_cost_satisfied({"Fire": 1, "Colorless": 1}, energies))
        self.assertTrue(attack_cost_satisfied({"Colorless": 2}, energies))
        self.assertFalse(attack_cost_satisfied({"Fire": 2}, energies))
        self.assertFalse(attack_cost_satisfied({"Fire": 1, "Colorless": 2}, energies))
        self.assertTrue(attack_cost_satisfied({}, []))
        # Legacy numeric-string keys still parse.
        self.assertTrue(attack_cost_satisfied(
            {str(PokemonTypes.FIRE.value): 1}, energies))

    def test_typed_requirements_consume_matching_energy_first(self):
        energies = self.energy_entities(PokemonTypes.FIRE)
        # The single fire energy must not double-count for fire AND colorless.
        self.assertFalse(attack_cost_satisfied({"Fire": 1, "Colorless": 1}, energies))

    def test_double_provide_energy_pays_two_colorless(self):
        double = create_card_entity(make_card(EnergyCardDef(
            guid="00000000-0000-0000-0000-0000000000dt",
            key="BW1", name="com.test.energy.DoubleTurbo.Name",
            collector_number=151, set_code="BW1", rarity=0,
            energy_type=PokemonTypes.COLORLESS, is_special=True,
            provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
        )), owning_player_id=P1)

        self.assertTrue(attack_cost_satisfied({"Colorless": 2}, [double]))
        self.assertFalse(attack_cost_satisfied({"Colorless": 3}, [double]))
        # One basic + Double Turbo covers a 3-Colorless cost (Lugia V).
        basic = self.energy_entities(PokemonTypes.GRASS)
        self.assertTrue(attack_cost_satisfied({"Colorless": 3}, basic + [double]))
        # Colorless-only options never pay a typed requirement.
        self.assertFalse(attack_cost_satisfied({"Fire": 1}, [double]))

    def test_typed_consumption_leaves_remaining_capacity_for_colorless(self):
        double_water = create_card_entity(make_card(EnergyCardDef(
            guid="00000000-0000-0000-0000-0000000000dw",
            key="BW1", name="com.test.energy.DoubleWater.Name",
            collector_number=152, set_code="BW1", rarity=0,
            energy_type=PokemonTypes.WATER, is_special=True,
            provides=[[PokemonTypes.WATER, PokemonTypes.WATER]],
        )), owning_player_id=P1)

        self.assertTrue(attack_cost_satisfied(
            {"Water": 1, "Colorless": 1}, [double_water]))
        self.assertFalse(attack_cost_satisfied(
            {"Water": 1, "Colorless": 2}, [double_water]))


class TestActionIDsAreGuids(LegalActionsTestBase):
    def test_every_offered_action_id_parses_as_guid(self):
        """AbilityID (TypedID) runs `new Guid(id)` client-side: one bad
        actionID kills deserialization of the whole offer."""
        import uuid
        self.add_to("hand", BASIC_POKEMON)
        self.add_to("hand", FIRE_ENERGY)
        self.add_to("hand", ITEM_CARD)
        active = self.add_to("activePokemonArea", BASIC_POKEMON)
        energy = create_card_entity(FIRE_ENERGY, owning_player_id=P1)
        self.board.add_card_to_area(energy, self.board.find_player_area(P1, "discard"))
        self.board.attach_card(energy.entity_id, active.entity_id)
        self.state.begin_turn(P1)

        entries = self.actions()
        self.assertTrue(entries)
        for entry in entries:
            uuid.UUID(entry["selectableAction"]["actionID"])


class TestAbilityIDAssignment(unittest.TestCase):
    def test_pie_abilities_carry_deterministic_guid_ability_ids(self):
        import json
        import uuid
        abilities = BASIC_POKEMON.get_attribute_value(AttrID.PIE_ABILITIES)
        parsed = json.loads(abilities)
        self.assertEqual(parsed[0]["abilityID"], ability_id_for(BASIC_POKEMON.guid, 0))
        self.assertEqual(parsed[1]["abilityID"], ability_id_for(BASIC_POKEMON.guid, 1))
        # The client's AbilityID ctor runs `new Guid(id)` -- every ability ID
        # on the wire must parse as a GUID.
        for ability in parsed:
            uuid.UUID(ability["abilityID"])

    def test_cost_keys_are_client_type_names(self):
        """Dictionary<PokemonTypes,int> keys coerce by NAME on the client;
        numeric-string keys crash archetype sync at login."""
        import json
        parsed = json.loads(BASIC_POKEMON.get_attribute_value(AttrID.PIE_ABILITIES))
        self.assertEqual(parsed[0]["cost"], {"Colorless": 1})
        self.assertEqual(parsed[1]["cost"], {"Fire": 1, "Colorless": 1})

    def test_ability_type_is_a_type_hint_class_name(self):
        """abilityType is the PieAbilityDescription subclass name: JsonFx
        resolves it through TypeHintedClasses (an int crashes login sync)."""
        import json
        hint_classes = {
            "Attack", "PokeAbility", "PokePower", "PokeBody", "AncientTrait",
            "EnergyAbility", "PlayAbility", "RetreatAbility", "StadiumAbility",
            "TechnicalMachine", "TrainerAbility",
        }
        parsed = json.loads(BASIC_POKEMON.get_attribute_value(AttrID.PIE_ABILITIES))
        for ability in parsed:
            self.assertIn(ability["abilityType"], hint_classes)


if __name__ == "__main__":
    unittest.main()
