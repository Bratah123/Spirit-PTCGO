"""Unit tests for the card-effect engine (spirit/game/session/effects.py)."""

import unittest

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import (
    Ability,
    Attack,
    EnergyCardDef,
    PokemonCardDef,
    Triggers,
    prize_value,
    unimplemented,
)
from spirit.game.models.board import BoardState, create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.effects import (
    EffectContext,
    resolve_attack,
    resolve_on_play_ability,
)
from spirit.game.session.game_session import NestedSequence
from spirit.game.session.legal_actions import TurnState
from spirit.network.message_names import OutboundMsg

P1 = "player-1"
P2 = "player-2"
GAME_ID = "test-game"


def make_card(card_def) -> Card:
    d = card_def.to_archetype_dict()
    return Card(d["guid"], d["key"], d["attributes"])


ATTACKER_DEF = PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000a1",
    key="BW1", name="com.test.pokemon.Snivy.Name",
    collector_number=1, set_code="BW1", rarity=1,
    hp=60, elements=[PokemonTypes.GRASS],
    abilities=[
        Attack("Vine Whip", cost={PokemonTypes.GRASS: 1}, damage=30),
        Attack("Leaf Storm", "storm.text", cost={PokemonTypes.GRASS: 2},
               damage=20, effect=unimplemented),
    ],
)
ATTACKER = make_card(ATTACKER_DEF)
VANILLA_ATTACK = ATTACKER_DEF.abilities[0]
UNIMPLEMENTED_ATTACK = ATTACKER_DEF.abilities[1]

WEAK_DEFENDER = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000d1",
    key="BW1", name="com.test.pokemon.Oshawott.Name",
    collector_number=2, set_code="BW1", rarity=1,
    hp=180, elements=[PokemonTypes.WATER],
    weakness_type=PokemonTypes.GRASS,
))

RESISTANT_DEFENDER = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000d2",
    key="BW1", name="com.test.pokemon.Pidove.Name",
    collector_number=3, set_code="BW1", rarity=1,
    hp=60, elements=[PokemonTypes.COLORLESS],
    resistance_type=PokemonTypes.GRASS,
))

PLAIN_DEFENDER = make_card(PokemonCardDef(
    guid="00000000-0000-0000-0000-0000000000d3",
    key="BW1", name="com.test.pokemon.Patrat.Name",
    collector_number=4, set_code="BW1", rarity=1,
    hp=30, elements=[PokemonTypes.COLORLESS],
))

GRASS_ENERGY = make_card(EnergyCardDef(
    guid="00000000-0000-0000-0000-0000000000e1",
    key="BW1", name="com.test.energy.Grass.Name",
    collector_number=100, set_code="BW1", rarity=0,
    energy_type=PokemonTypes.GRASS,
))


class FakePlayer:
    def __init__(self, name):
        self.screen_name = name


class FakeSession:
    """Duck-typed GameSession capturing sequence brackets per viewer."""

    def __init__(self, board):
        self.board_state = board
        self.game_id = GAME_ID
        self.players = {P1: FakePlayer("P1"), P2: FakePlayer("P2")}
        self.turn_state = TurnState()
        self.sleep_checkup_coins = {}
        self.poison_counters = {}
        self.paralyzed_since = {}
        self.sent = []  # (player_ids, sequence_name, inner_messages)
        self.prompts = []  # (player_id, prompt, buttons)
        self.choice_replies = []  # queued button indices, popped per prompt
        self.chooser_calls = []  # (player_id, [card ids], count, minimum, prompt)
        self.panel_calls = []  # (player_id, source_entity_id, prompt, buttons)
        self.chooser_replies = []  # queued entity-id lists, popped per chooser
        self.entity_picker_calls = []  # (player_id, [card ids]) routed in-place
        self.damage_counter_calls = []  # (player_id, [card ids], count, prompt)
        self.damage_counter_replies = []  # queued {entity_id: counters}, popped per call
        self.prize_reveal_calls = []  # (player_id, prize ids, selectable ids)
        self.prize_reveal_replies = []  # queued picked prize id (or None), popped
        self.attack_sources = None  # last _broadcast_attack_sources payload
        self.prize_awards = []  # (player_id, count) awarded by resolve_knockouts
        self.game_over = None  # (winner_id, reason) when a win condition fired
        self.game_stats = {P1: {}, P2: {}}
        self.mvp_damage = {P1: {}, P2: {}}

    def credit_card_damage(self, player_id, entity, amount):
        guid = getattr(entity, "archetype_id", None)
        if not guid or amount <= 0:
            return
        entry = self.mvp_damage.setdefault(player_id, {}).setdefault(guid, [0, ""])
        entry[0] += amount

    def stat_add(self, player_id, key, amount=1):
        stats = self.game_stats.setdefault(player_id, {})
        stats[key] = stats.get(key, 0) + amount

    def stat_max(self, player_id, key, value):
        stats = self.game_stats.setdefault(player_id, {})
        if value > stats.get(key, 0):
            stats[key] = value

    def _opponent_id(self, player_id):
        return P2 if player_id == P1 else P1

    def clear_condition_state(self, entity_id):
        self.sleep_checkup_coins.pop(entity_id, None)
        self.poison_counters.pop(entity_id, None)
        self.paralyzed_since.pop(entity_id, None)

    def clear_pokemon_effects(self, pokemon):
        had_conditions = bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))
        pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, [])
        self.clear_condition_state(pokemon.entity_id)
        for key in [k for k in self.turn_state.attack_locks if k[0] == pokemon.entity_id]:
            self.turn_state.attack_locks.pop(key, None)
        return had_conditions

    def reset_pokemon_damage(self, pokemon):
        printed_max = pokemon.attribute_originals.get(
            AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
        )
        pokemon.set_attribute(AttrID.HP, printed_max)

    def reset_ability_usage(self, pokemon):
        for key in [k for k in self.turn_state.used_abilities
                    if k[0] == pokemon.entity_id]:
            self.turn_state.used_abilities.discard(key)

    @staticmethod
    def _build_msg(name, value):
        return {"name": name, "value": value}

    def _entity_introduced_msg(self, card):
        return self._build_msg(OutboundMsg.ENTITY_INTRODUCED.value, {
            "gameID": self.game_id,
            "entityID": card.entity_id,
            "entityName": card.get_entity_name(),
            "attributeMap": card.serialize_attributes(),
        })

    def _entity_moved_msg(self, entity_id, destination_id, position):
        return self._build_msg(OutboundMsg.ENTITY_MOVED.value, {
            "gameID": self.game_id,
            "entityID": entity_id,
            "destinationID": destination_id,
            "positionInParent": position,
            "animDuration": 300,
        })

    async def send_game_sequence(self, players, name, inner_messages):
        viewer_ids = [pid for pid, p in self.players.items() if p in players]
        self.sent.append((viewer_ids, getattr(name, "value", name), list(inner_messages)))

    async def prompt_player_choice(self, player_id, prompt, buttons, sort_type=""):
        self.prompts.append((player_id, prompt, buttons))
        return self.choice_replies.pop(0) if self.choice_replies else 0

    async def prompt_choice_panel(self, player_id, source, options,
                                  prompt=None, descriptions=None):
        self.prompts.append((player_id, prompt, options))
        self.panel_calls.append((player_id, source.entity_id, prompt, options))
        return self.choice_replies.pop(0) if self.choice_replies else 0

    async def prompt_card_chooser(self, player_id, source_entity_id, cards,
                                  count, minimum=None, prompt="", ordered=False,
                                  display_cards=None, slot_prompt=""):
        ids = [c.entity_id for c in cards]
        self.chooser_calls.append((player_id, ids, count, minimum, prompt))
        if self.chooser_replies:
            return [i for i in self.chooser_replies.pop(0) if i in ids][:count]
        return ids[:count]

    async def prompt_entity_picker(self, player_id, source_entity_id, cards,
                                   count, minimum=None, prompt=""):
        self.entity_picker_calls.append((player_id, [c.entity_id for c in cards]))
        return await self.prompt_card_chooser(
            player_id, source_entity_id, cards, count, minimum, prompt
        )

    async def prompt_card_chooser_groups(self, player_id, source_entity_id,
                                         groups, prompt="", display_cards=None,
                                         total=None, any_of=False):
        picked = []
        for group in groups:
            picked.append(await self.prompt_card_chooser(
                player_id, source_entity_id, group["cards"], group["count"],
                group.get("minimum", 0), prompt,
            ))
        return picked

    async def prompt_damage_counter_placement(self, player_id, source_entity_id,
                                              candidates, count,
                                              amount_per_click=10, prompt=""):
        ids = [c.entity_id for c in candidates]
        self.damage_counter_calls.append((player_id, ids, count, prompt))
        if self.damage_counter_replies:
            return self.damage_counter_replies.pop(0)
        return {ids[0]: count} if ids else {}

    async def _broadcast_attack_sources(self, entity_ids):
        self.attack_sources = entity_ids

    def _reveal_card_msg(self, entity_id, return_to_origin):
        return self._build_msg(OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value, {
            "gameID": self.game_id,
            "entityID": entity_id,
            "Return": return_to_origin,
            "alwaysReveal": False,
        })

    def _entity_id_data_effect_msg(self, key, entity_id):
        return self._build_msg(OutboundMsg.ENTITY_ID_DATA_EFFECT.value, {
            "gameID": self.game_id, "key": key, "value": entity_id,
        })

    def _attributes_reset_msg(self, entity_id):
        return self._build_msg(OutboundMsg.ATTRIBUTES_RESET.value, {
            "gameID": self.game_id, "entityID": entity_id,
        })

    async def prompt_prize_reveal_pick(self, player_id, source_id,
                                       prize_ids, selectable_ids):
        self.prize_reveal_calls.append((player_id, list(prize_ids), list(selectable_ids)))
        if self.prize_reveal_replies:
            reply = self.prize_reveal_replies.pop(0)
            return reply if reply in selectable_ids else None
        return selectable_ids[0] if selectable_ids else None

    def _condition_attr_msg(self, pokemon):
        conditions = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        return self._build_msg(OutboundMsg.ATTRIBUTE_MODIFIED.value, {
            "gameID": self.game_id,
            "entityID": pokemon.entity_id,
            "attribute": {
                "name": AttrID.SPECIAL_CONDITIONS.value,
                "value": conditions,
                "originalValue": conditions,
                "modValue": None,
            },
        })

    async def send_game_sequence_flush(self, ctx):
        for pid in self.players:
            for name, msgs in ctx.bracket_runs_for(pid):
                await self.send_game_sequence([self.players[pid]], name, msgs)

    async def resolve_knockouts(self, ctx, _ko_depth=0):
        """Mirror of GameSession.resolve_knockouts' discard/prize accounting,
        without the interactive prize pick and promotion prompts."""
        for pokemon in ctx.knockouts:
            owner_id = pokemon.owning_player_id
            taker_id = self._opponent_id(owner_id)
            discard = self.board_state.find_player_area(owner_id, "discard")
            stack = [pokemon]
            queue = list(pokemon.children)
            while queue:
                entity = queue.pop(0)
                stack.append(entity)
                queue.extend(entity.children)
            moves = []
            for entity in stack:
                position = len(discard.children)
                if self.board_state.move_card(entity.entity_id, discard.entity_id):
                    moves.append(self._entity_moved_msg(
                        entity.entity_id, discard.entity_id, position
                    ))
            if moves:
                await self.send_game_sequence(
                    list(self.players.values()), "Knockout", moves
                )
            self.prize_awards.append((taker_id, prize_value(pokemon.archetype_id)))
        ctx.knockouts.clear()

    async def end_game(self, winner_id, reason):
        self.game_over = (winner_id, reason)

    async def _broadcast_entity_attribute(self, entity, attr, value):
        entity.set_attribute(attr, value)

    async def _promote_new_active(self, player_id):
        from spirit.game.models.board import PokemonEntity
        bench = self.board_state.find_player_area(player_id, "bench")
        active = self.board_state.find_player_area(player_id, "activePokemonArea")
        cands = [c for c in (bench.children if bench else [])
                 if isinstance(c, PokemonEntity)]
        if not cands:
            return False
        self.board_state.move_card(cands[0].entity_id, active.entity_id)
        return True


class EffectsTestBase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.board = BoardState(GAME_ID, [P1, P2])
        self.session = FakeSession(self.board)

    def add_to(self, area_name, card, player_id):
        entity = create_card_entity(card, owning_player_id=player_id)
        area = self.board.find_player_area(player_id, area_name)
        self.board.add_card_to_area(entity, area)
        return entity

    def brackets(self, name):
        return [s for s in self.session.sent if s[1] == name]

    @staticmethod
    def flat_msgs(msgs):
        """Bracket messages with nested child sequences folded in."""
        out = []
        for m in msgs:
            out.extend(m.messages if isinstance(m, NestedSequence) else [m])
        return out

    def attack_bracket_for(self, viewer_id):
        for viewer_ids, name, msgs in self.session.sent:
            if name == "Attack" and viewer_ids == [viewer_id]:
                return msgs
        return None


class TestVanillaAttack(EffectsTestBase):
    async def test_base_damage_with_weakness(self):
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        defender = self.add_to("activePokemonArea", WEAK_DEFENDER, P2)

        await resolve_attack(self.session, P1, attacker, VANILLA_ATTACK,
                             VANILLA_ATTACK.ability_id)

        # 30 base doubled by Grass weakness = 60; 180 -> 120.
        self.assertEqual(defender.get_attribute(AttrID.HP), 120)

        for pid in (P1, P2):
            msgs = self.attack_bracket_for(pid)
            self.assertIsNotNone(msgs)
            names = [m["name"] for m in msgs]
            self.assertEqual(names[0], "AbilityPlayedEffect")
            self.assertEqual(names[-1], "AbilityFinishedEffect")
            self.assertIn("CakeAttackEffect", names)
            # Damaging attacks get the client's lunge group, not the orb.
            self.assertNotIn("NonDamagingTargetsEffect", names)
            self.assertIn("AttributeModified", names)
            # The damage popup must precede the HP change: the client's KO
            # check compares damageAmount against the pre-hit HP value.
            self.assertLess(
                names.index("CakeAttackEffect"), names.index("AttributeModified")
            )
            cake = next(m for m in msgs if m["name"] == "CakeAttackEffect")
            self.assertEqual(cake["value"]["damageAmount"], 60)
            self.assertTrue(cake["value"]["weaknessTriggered"])
            self.assertEqual(cake["value"]["entityID"], defender.entity_id)
            self.assertEqual(cake["value"]["damageSource"], attacker.entity_id)
            attr = next(m for m in msgs if m["name"] == "AttributeModified")
            self.assertEqual(attr["value"]["attribute"]["value"], 120)
            self.assertEqual(attr["value"]["attribute"]["originalValue"], 180)

        # The attacker's pulled-back panel is tucked home first.
        dismiss = self.brackets("DismissAbilitySelect")
        self.assertEqual(len(dismiss), 1)
        self.assertEqual(dismiss[0][0], [P1])
        self.assertEqual(self.brackets("Knockout"), [])

    async def test_resistance_reduces_to_floor_zero(self):
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        defender = self.add_to("activePokemonArea", RESISTANT_DEFENDER, P2)

        await resolve_attack(self.session, P1, attacker, VANILLA_ATTACK,
                             VANILLA_ATTACK.ability_id)

        self.assertEqual(defender.get_attribute(AttrID.HP), 60)
        cake = next(m for m in self.attack_bracket_for(P1)
                    if m["name"] == "CakeAttackEffect")
        self.assertTrue(cake["value"]["resistanceTrigger"])
        self.assertEqual(cake["value"]["damageAmount"], 0)

    async def test_damaged_entity_serializes_max_as_original_value(self):
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        defender = self.add_to("activePokemonArea", WEAK_DEFENDER, P2)
        await resolve_attack(self.session, P1, attacker, VANILLA_ATTACK,
                             VANILLA_ATTACK.ability_id)

        hp_attr = next(a for a in defender.serialize_attributes()
                       if a["name"] == AttrID.HP.value)
        self.assertEqual(hp_attr["value"], 120)
        self.assertEqual(hp_attr["originalValue"], 180)


class TestUnimplementedAttack(EffectsTestBase):
    async def test_resolves_base_damage_and_logs(self):
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        defender = self.add_to("activePokemonArea", WEAK_DEFENDER, P2)

        with self.assertLogs(level="WARNING") as logs:
            await resolve_attack(self.session, P1, attacker, UNIMPLEMENTED_ATTACK,
                                 UNIMPLEMENTED_ATTACK.ability_id)
        self.assertTrue(any("unimplemented" in line for line in logs.output))
        # 20 base doubled by weakness = 40; 180 -> 140.
        self.assertEqual(defender.get_attribute(AttrID.HP), 140)


class TestKnockout(EffectsTestBase):
    async def test_knockout_discards_stack_with_attachments(self):
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        defender = self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)  # 30 HP
        energy = self.add_to("discard", GRASS_ENERGY, P2)
        self.board.attach_card(energy.entity_id, defender.entity_id)

        await resolve_attack(self.session, P1, attacker, VANILLA_ATTACK,
                             VANILLA_ATTACK.ability_id)

        self.assertEqual(defender.get_attribute(AttrID.HP), 0)
        discard = self.board.find_player_area(P2, "discard")
        self.assertIn(defender, discard.children)
        self.assertIn(energy, discard.children)
        self.assertIsNone(self.board.active_pokemon(P2))

        knockouts = self.brackets("Knockout")
        self.assertEqual(len(knockouts), 1)
        moved_ids = [m["value"]["entityID"] for m in knockouts[0][2]]
        self.assertEqual(moved_ids, [defender.entity_id, energy.entity_id])


class TestCustomEffect(EffectsTestBase):
    async def test_effect_can_deal_damage_and_draw(self):
        async def effect(ctx):
            await ctx.deal_damage(10)
            await ctx.draw_cards(1)

        attack = Attack("Custom", cost={PokemonTypes.GRASS: 1},
                        damage=10, effect=effect)
        attack.ability_id = "00000000-0000-0000-0000-00000000ab01"
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        defender = self.add_to("activePokemonArea", WEAK_DEFENDER, P2)
        deck_card = self.add_to("deck", GRASS_ENERGY, P1)

        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)

        # 10 doubled by weakness = 20; 180 -> 160.
        self.assertEqual(defender.get_attribute(AttrID.HP), 160)
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(deck_card, hand.children)

        # Draws flush as their own Draw bracket after the attack; faces
        # reveal only to the drawing player, and the moves ride a nested
        # GroupedMove (a flat move would take the flip fan's default curve).
        p1_names = [m["name"] for m in self.attack_bracket_for(P1)]
        self.assertNotIn("EntityIntroduced", p1_names)
        draw_brackets = self.brackets("Draw")
        self.assertEqual(len(draw_brackets), 2)
        for viewer_ids, _, msgs in draw_brackets:
            nested = [m for m in msgs if isinstance(m, NestedSequence)]
            self.assertEqual([n.name for n in nested], ["GroupedMove"])
            names = [m["name"] for m in self.flat_msgs(msgs)]
            if viewer_ids == [P1]:
                self.assertIn("EntityIntroduced", names)
            else:
                self.assertNotIn("EntityIntroduced", names)
            self.assertIn("EntityMoved", [m["name"] for m in nested[0].messages])

    async def test_non_damaging_attack_carries_orb_at_the_deck(self):
        async def read_wind(ctx):
            await ctx.draw_cards(1)

        attack = Attack("Wind", cost={PokemonTypes.GRASS: 1}, effect=read_wind)
        attack.ability_id = "00000000-0000-0000-0000-00000000ab03"
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)
        self.add_to("deck", GRASS_ENERGY, P1)

        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)

        # No CakeAttackEffect means M.N only clears the pulled-out attacker
        # via the r.u orb -- built from NonDamagingTargetsEffect's targets.
        deck = self.board.find_player_area(P1, "deck")
        for pid in (P1, P2):
            msgs = self.attack_bracket_for(pid)
            orb = next(m for m in msgs if m["name"] == "NonDamagingTargetsEffect")
            self.assertEqual(orb["value"]["targets"], [deck.entity_id])

    async def test_bench_damage_skips_modifiers(self):
        async def snipe(ctx):
            await ctx.deal_damage(30, target=ctx.opponent_bench()[0])

        attack = Attack("Snipe", cost={PokemonTypes.GRASS: 1}, effect=snipe)
        attack.ability_id = "00000000-0000-0000-0000-00000000ab02"
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)
        benched = self.add_to("bench", WEAK_DEFENDER, P2)

        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)

        # Weakness does not apply off-Active by default: 180 - 30.
        self.assertEqual(benched.get_attribute(AttrID.HP), 150)


class TestOnPlayAbility(EffectsTestBase):
    def make_on_play_pokemon(self):
        async def dark_asset(ctx):
            if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
                await ctx.draw_until(6)

        card_def = PokemonCardDef(
            guid="00000000-0000-0000-0000-0000000000c1",
            key="BW1", name="com.test.pokemon.CrobatV.Name",
            collector_number=5, set_code="BW1", rarity=3,
            hp=180, elements=[PokemonTypes.DARKNESS],
            abilities=[
                Ability("Dark Asset", "darkasset.text",
                        trigger=Triggers.ON_PLAY, effect=dark_asset),
            ],
        )
        return make_card(card_def), card_def.abilities[0]

    async def test_draws_until_six_with_orb_choreography(self):
        card, ability = self.make_on_play_pokemon()
        pokemon = self.add_to("bench", card, P1)
        for _ in range(2):
            self.add_to("hand", GRASS_ENERGY, P1)
        for _ in range(6):
            self.add_to("deck", GRASS_ENERGY, P1)

        await resolve_on_play_ability(self.session, P1, pokemon, ability)

        hand = self.board.find_player_area(P1, "hand")
        self.assertEqual(len(hand.children), 6)

        # The "you may" prompt went to the ability's owner as a Yes/No dialog.
        self.assertEqual(len(self.session.prompts), 1)
        prompt_player, _, buttons = self.session.prompts[0]
        self.assertEqual(prompt_player, P1)
        self.assertEqual(buttons, ["Yes", "No"])

        # Attack bracket per viewer: markers + the orb shot at the deck; the
        # playmat attack-source attr points at the ability's Pokemon.
        self.assertEqual(self.session.attack_sources, [pokemon.entity_id])
        attack_brackets = self.brackets("Attack")
        self.assertEqual(len(attack_brackets), 2)
        deck = self.board.find_player_area(P1, "deck")
        for _, _, msgs in attack_brackets:
            names = [m["name"] for m in msgs]
            self.assertEqual(
                names,
                ["AbilityPlayedEffect", "NonDamagingTargetsEffect",
                 "AbilityFinishedEffect"],
            )
            head = msgs[0]["value"]
            self.assertEqual(head["abilityType"], "PokeAbility")
            self.assertEqual(head["abilityID"], ability.ability_id)
            self.assertEqual(msgs[1]["value"]["targets"], [deck.entity_id])

        # A Draw bracket per viewer carries the draws (moves nested in a
        # GroupedMove child); drawn faces reveal only to the drawing player.
        draw_brackets = self.brackets("Draw")
        self.assertEqual(len(draw_brackets), 2)
        for viewer_ids, _, msgs in draw_brackets:
            nested = [m for m in msgs if isinstance(m, NestedSequence)]
            self.assertEqual([n.name for n in nested], ["GroupedMove"])
            names = [m["name"] for m in self.flat_msgs(msgs)]
            if viewer_ids == [P1]:
                self.assertEqual(names.count("EntityIntroduced"), 4)
            else:
                self.assertNotIn("EntityIntroduced", names)
            self.assertEqual(names.count("EntityMoved"), 4)

    async def test_declining_the_prompt_draws_nothing(self):
        card, ability = self.make_on_play_pokemon()
        pokemon = self.add_to("bench", card, P1)
        deck_card = self.add_to("deck", GRASS_ENERGY, P1)
        self.session.choice_replies.append(1)  # "No"

        await resolve_on_play_ability(self.session, P1, pokemon, ability)

        deck = self.board.find_player_area(P1, "deck")
        self.assertIn(deck_card, deck.children)
        # The ability still announces itself (popin/gamelog), but no orb plays.
        self.assertEqual(len(self.brackets("PokeAbility")), 2)
        self.assertEqual(self.brackets("Attack"), [])

    async def test_hand_already_full_draws_nothing(self):
        card, ability = self.make_on_play_pokemon()
        pokemon = self.add_to("bench", card, P1)
        for _ in range(6):
            self.add_to("hand", GRASS_ENERGY, P1)
        deck_card = self.add_to("deck", GRASS_ENERGY, P1)

        await resolve_on_play_ability(self.session, P1, pokemon, ability)

        deck = self.board.find_player_area(P1, "deck")
        self.assertIn(deck_card, deck.children)

    async def test_unimplemented_on_play_ability_is_skipped(self):
        ability = Ability("Mystery", "mystery.text",
                          trigger=Triggers.ON_PLAY, effect=unimplemented)
        ability.ability_id = "00000000-0000-0000-0000-00000000ab04"
        pokemon = self.add_to("bench", PLAIN_DEFENDER, P1)

        with self.assertLogs(level="WARNING") as logs:
            await resolve_on_play_ability(self.session, P1, pokemon, ability)
        self.assertTrue(any("unimplemented" in line for line in logs.output))
        self.assertEqual(self.brackets("PokeAbility"), [])


class TestHeal(EffectsTestBase):
    async def test_heal_caps_at_max_hp(self):
        async def mend(ctx):
            await ctx.heal(40)

        attack = Attack("Mend", cost={PokemonTypes.GRASS: 1}, effect=mend)
        attack.ability_id = "00000000-0000-0000-0000-00000000ab03"
        attacker = self.add_to("activePokemonArea", ATTACKER, P1)
        self.add_to("activePokemonArea", PLAIN_DEFENDER, P2)
        attacker.set_attribute(AttrID.HP, 40)  # 20 damage on a 60 HP Pokemon

        await resolve_attack(self.session, P1, attacker, attack, attack.ability_id)

        self.assertEqual(attacker.get_attribute(AttrID.HP), 60)


class TestChooserRouting(EffectsTestBase):
    """choose_cards routes in-play targets (incl. attachments and the Stadium)
    to the in-place picker: the reveal browser can never display them (their
    renders belong to higher-layer playmat requesters -> empty carousel)."""

    def ctx_for(self, player_id=P1):
        source = self.add_to("hand", ATTACKER, player_id)
        return EffectContext(self.session, player_id, source, None)

    def attach(self, card, pokemon, player_id):
        entity = create_card_entity(card, owning_player_id=player_id)
        self.board.add_card_to_area(entity, self.board.find_player_area(player_id, "hand"))
        self.board.attach_card(entity.entity_id, pokemon.entity_id)
        return entity

    async def test_attached_energy_uses_in_place_picker(self):
        ctx = self.ctx_for()
        active = self.add_to("activePokemonArea", WEAK_DEFENDER, P2)
        benched = self.add_to("bench", PLAIN_DEFENDER, P2)
        energies = [self.attach(GRASS_ENERGY, active, P2),
                    self.attach(GRASS_ENERGY, benched, P2)]

        picks = await ctx.choose_cards(energies, 1, minimum=1, prompt="pick")

        self.assertEqual(len(self.session.entity_picker_calls), 1)
        self.assertEqual(picks[0].entity_id, energies[0].entity_id)

    async def test_tools_and_stadium_mix_uses_in_place_picker(self):
        ctx = self.ctx_for()
        active = self.add_to("activePokemonArea", WEAK_DEFENDER, P2)
        tool = self.attach(GRASS_ENERGY, active, P2)
        stadium = create_card_entity(ATTACKER, owning_player_id=P2)
        self.board.add_card_to_area(stadium, self.board.find_global_area("activeStadium"))

        await ctx.choose_cards([tool, stadium], 1, minimum=1, prompt="pick")

        self.assertEqual(len(self.session.entity_picker_calls), 1)

    async def test_discard_pile_still_uses_browser(self):
        ctx = self.ctx_for()
        discarded = self.add_to("discard", PLAIN_DEFENDER, P1)

        await ctx.choose_cards([discarded], 1, prompt="pick")

        self.assertEqual(self.session.entity_picker_calls, [])
        self.assertEqual(len(self.session.chooser_calls), 1)

    async def test_attachment_on_discarded_stack_uses_browser(self):
        ctx = self.ctx_for()
        discarded = self.add_to("discard", PLAIN_DEFENDER, P1)
        energy = self.attach(GRASS_ENERGY, discarded, P1)

        await ctx.choose_cards([energy], 1, prompt="pick")

        self.assertEqual(self.session.entity_picker_calls, [])

    async def test_opponent_hand_uses_browser(self):
        ctx = self.ctx_for()
        opp_card = self.add_to("hand", PLAIN_DEFENDER, P2)

        await ctx.choose_cards([opp_card], 1, prompt="pick")

        self.assertEqual(self.session.entity_picker_calls, [])


class TestHisuianHeavyBall(EffectsTestBase):
    """look_at_prizes_take_basic drives the prize-fan reveal/pick/swap/shuffle."""

    def _inner_names(self):
        names = []
        for _viewers, _name, msgs in self.session.sent:
            names.extend(m["name"] for m in self.flat_msgs(msgs))
        return names

    def _reset_targets(self):
        out = []
        for viewer_ids, _name, msgs in self.session.sent:
            for m in self.flat_msgs(msgs):
                if m["name"] == OutboundMsg.ATTRIBUTES_RESET.value:
                    out.extend((v, m["value"]["entityID"]) for v in viewer_ids)
        return out

    async def test_reveal_basic_takes_it_and_swaps_in(self):
        source = self.add_to("hand", ATTACKER, P1)
        ctx = EffectContext(self.session, P1, source, None)
        basic = self.add_to("prizePile", WEAK_DEFENDER, P1)
        energy = self.add_to("prizePile", GRASS_ENERGY, P1)

        took = await ctx.look_at_prizes_take_basic()

        self.assertTrue(took)
        # The offer reveals every Prize but only the Basic is selectable.
        _pid, prize_ids, selectable = self.session.prize_reveal_calls[0]
        self.assertEqual(set(prize_ids), {basic.entity_id, energy.entity_id})
        self.assertEqual(selectable, [basic.entity_id])
        # Basic -> hand; Heavy Ball takes the vacated face-down Prize slot.
        hand = self.board.find_player_area(P1, "hand")
        prize = self.board.find_player_area(P1, "prizePile")
        self.assertIn(basic, hand.children)
        self.assertIn(source, prize.children)
        self.assertNotIn(basic, prize.children)
        # The Basic is taken via WithOpenPrizeCards -- that bracket closes the
        # prize present (a plain move leaves the fan on screen).
        wopc = [s for s in self.session.sent if s[1] == "WithOpenPrizeCards"]
        self.assertTrue(wopc)
        moved = {m["value"]["entityID"] for _v, _n, msgs in wopc
                 for m in msgs if m["name"] == OutboundMsg.ENTITY_MOVED.value}
        self.assertIn(basic.entity_id, moved)
        # The revealed Prizes are re-hidden and then shuffled.
        inner = self._inner_names()
        self.assertIn(OutboundMsg.ATTRIBUTES_RESET.value, inner)
        self.assertIn(OutboundMsg.SHUFFLED.value, inner)
        # The swapped-in Heavy Ball is re-hidden for the OPPONENT too (it sat
        # revealed on the trainer slot).
        self.assertIn((P2, source.entity_id), self._reset_targets())

    async def test_decline_keeps_card_for_discard_but_shuffles(self):
        source = self.add_to("hand", ATTACKER, P1)
        ctx = EffectContext(self.session, P1, source, None)
        basic = self.add_to("prizePile", WEAK_DEFENDER, P1)
        self.add_to("prizePile", GRASS_ENERGY, P1)
        self.session.prize_reveal_replies = [None]

        took = await ctx.look_at_prizes_take_basic()

        self.assertFalse(took)
        prize = self.board.find_player_area(P1, "prizePile")
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(source, hand.children)       # left for the normal discard
        self.assertNotIn(source, prize.children)
        self.assertIn(basic, prize.children)
        inner = self._inner_names()
        self.assertIn(OutboundMsg.ATTRIBUTES_RESET.value, inner)
        self.assertIn(OutboundMsg.SHUFFLED.value, inner)

    async def test_no_basic_present_declines(self):
        source = self.add_to("hand", ATTACKER, P1)
        ctx = EffectContext(self.session, P1, source, None)
        self.add_to("prizePile", GRASS_ENERGY, P1)
        self.add_to("prizePile", GRASS_ENERGY, P1)

        took = await ctx.look_at_prizes_take_basic()

        self.assertFalse(took)
        _pid, _prize_ids, selectable = self.session.prize_reveal_calls[0]
        self.assertEqual(selectable, [])

    async def test_no_prizes_is_a_noop(self):
        source = self.add_to("hand", ATTACKER, P1)
        ctx = EffectContext(self.session, P1, source, None)

        took = await ctx.look_at_prizes_take_basic()

        self.assertFalse(took)
        self.assertEqual(self.session.prize_reveal_calls, [])


class TestLeavePlayResetsAbilityUsage(EffectsTestBase):
    """A Pokemon that used a once-per-turn ability, then left play (Scoop Up
    Net -> hand), is a fresh card: its usage resets so a replay can use it."""

    async def test_put_in_hand_clears_once_per_turn_usage(self):
        pokemon = self.add_to("activePokemonArea", ATTACKER, P1)
        action_id = "11111111-2222-3333-4444-555555555555"
        self.session.turn_state.used_abilities.add((pokemon.entity_id, action_id))

        ctx = EffectContext(self.session, P1, pokemon, None)
        await ctx.put_in_hand([pokemon], reveal=False)

        self.assertNotIn(
            (pokemon.entity_id, action_id), self.session.turn_state.used_abilities
        )

    async def test_other_pokemon_usage_survives(self):
        scooped = self.add_to("activePokemonArea", ATTACKER, P1)
        other = self.add_to("bench", ATTACKER, P1)
        action_id = "11111111-2222-3333-4444-555555555555"
        self.session.turn_state.used_abilities.add((scooped.entity_id, action_id))
        self.session.turn_state.used_abilities.add((other.entity_id, action_id))

        ctx = EffectContext(self.session, P1, scooped, None)
        await ctx.put_in_hand([scooped], reveal=False)

        self.assertNotIn(
            (scooped.entity_id, action_id), self.session.turn_state.used_abilities
        )
        self.assertIn(
            (other.entity_id, action_id), self.session.turn_state.used_abilities
        )


if __name__ == "__main__":
    unittest.main()
