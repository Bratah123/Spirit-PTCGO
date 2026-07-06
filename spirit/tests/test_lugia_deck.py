"""End-to-end unit tests for the Lugia VSTAR deck cards and the engine
features they exercise (passives, choosers, switches, conditions, VSTAR)."""

import unittest

from spirit.tests.test_effects import EffectsTestBase, P1, P2

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID, EnergyCardDef
from spirit.game.models.board import BoardState
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import (
    EffectContext,
    resolve_attack,
    resolve_energy_attach_cost,
    resolve_energy_on_attach,
    resolve_trainer_effect,
)
from spirit.game.session.legal_actions import (
    ACTION_ATTACH_TOOL,
    ACTION_PLAY_ENERGY,
    ACTION_RETREAT,
    ACTION_USE_ABILITY,
    ACTION_USE_ATTACK,
    ACTION_USE_TRAINER,
    TurnState,
    compute_legal_actions,
)
from spirit.game.session.passives import (
    compute_damage,
    effective_attack_cost,
    effective_max_hp,
)

GAME_ID = "test-game"

# Archetype GUIDs of the deck's printings (spirit/game/scripts/cards).
DUNSPARCE = "294dcbed-7729-5d2d-bee6-0f911544a3cf"
LUGIA_V = "fb5563a2-d94c-5699-b89a-834d1c68c53c"
LUGIA_VSTAR = "03ef5e0c-e166-56af-9dd9-3fc40b576f39"
ARCHEOPS = "b1ff4ef4-88a9-5f17-b940-0194d40dff6f"
ORANGURU = "caae62aa-a272-51ae-8178-079147fd65aa"
SNORLAX = "4915ec3e-4ad8-59dd-b135-e34a0b43e434"
STOUTLAND_V = "c25c58bd-765c-55fc-b661-aec1b4aef657"
YVELTAL = "69e7c69a-a11f-5f8f-a4c5-483669997e7f"
RADIANT_CHARIZARD = "dbdfb6ff-6850-5078-972c-47c3ce9ed97c"
RAIKOU = "a4d02546-82ac-5b28-8171-04f4e4f14409"
PUMPKABOO = "04560a42-d19b-5255-9214-ab55f98a18ee"
LUMINEON_V = "b4ce3a0e-da4d-5478-899a-ec0a364bc59a"
MANAPHY = "fe53515c-30ea-5867-bd89-f4ee7b6fc52c"

PROF_RESEARCH = "39450361-45e4-5450-b8eb-e0d5b5b4789b"
MARNIE = "ed3f56a6-383b-516b-a693-6f903d6b679f"
BOSSS_ORDERS = "6bf73995-dba1-5433-bc30-fbbd15d6d282"
SERENA = "9da91305-afcf-57f7-971a-c0ab57422f13"
IRIDA = "99351945-9d97-5a0e-a68f-3cead4b2ba95"
QUICK_BALL = "cdaf82a1-0150-5052-b1ee-eb3fbe5437b6"
EVOLUTION_INCENSE = "74403d98-c7f0-5c0c-8cf8-82bb6f1a51b6"
LOST_VACUUM = "60a35514-a1e0-5c3a-9ff0-1fe1dd718e18"
CHOICE_BELT = "a4309622-34a1-5398-9237-091ad3bc0acd"
ESCAPE_ROPE = "49a44b53-3548-5b2f-ab20-68bf4bab240a"
ULTRA_BALL = "fb774725-4a88-5dd0-888d-b53a1488c226"

POWERFUL_COLORLESS = "f38454bf-14b8-5b80-906d-feb90569337c"
AURORA = "cd7f0518-76e6-5249-bd0a-b7c75e76e096"
CAPTURE = "7622bd93-cd34-54c4-8104-a93f372d145e"
DOUBLE_TURBO = "f2c20770-b08b-5f5b-bb9a-7ec86ad399a6"
HEAT_FIRE = "2d92cb2b-50fc-5129-875d-e9ab2a698d74"
SPEED_LIGHTNING = "9ddcc31e-666e-5832-9071-54d5cb2e6bdf"
V_GUARD = "77d43395-0432-5739-84d4-4581bd0a5a83"

# Plain typed energy for stocking attack costs in tests.
FIRE_TEST_ENERGY = EnergyCardDef(
    guid="00000000-0000-0000-0000-00000000fe01",
    key="BW1", name="com.test.energy.Fire.Name",
    collector_number=901, set_code="BW1", rarity=0,
    energy_type=PokemonTypes.FIRE,
)


def setUpModule():
    if not loader.cards_by_guid:
        loader.load_all()


def deck_card(guid):
    return loader.cards_by_guid[guid]


def ability_named(guid, title):
    definition = CARD_DEFS_BY_GUID[guid]
    return next(a for a in definition.abilities if a.title == title)


class LugiaDeckTestBase(EffectsTestBase):
    def add_deck_card(self, area_name, guid, player_id):
        return self.add_to(area_name, deck_card(guid), player_id)

    def attach(self, guid, pokemon, player_id):
        card = self.add_to("discard", deck_card(guid), player_id)
        self.board.attach_card(card.entity_id, pokemon.entity_id)
        return card

    def attack_ctx(self, attacker, guid, title):
        return EffectContext(self.session, P1, attacker, ability_named(guid, title))


# ----------------------------------------------------------------------
# Damage-pipeline passives
# ----------------------------------------------------------------------

class TestDamagePassives(LugiaDeckTestBase):
    def test_choice_belt_adds_30_versus_active_v(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        stoutland = self.add_deck_card("activePokemonArea", STOUTLAND_V, P2)
        self.attach(CHOICE_BELT, lugia, P1)
        calc = compute_damage(self.board, lugia, stoutland, 130)
        self.assertEqual(calc.amount, 160)

    def test_choice_belt_ignores_non_v_targets(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        snorlax = self.add_deck_card("activePokemonArea", SNORLAX, P2)
        self.attach(CHOICE_BELT, lugia, P1)
        calc = compute_damage(self.board, lugia, snorlax, 130)
        self.assertEqual(calc.amount, 130)

    def test_powerful_colorless_adds_20_to_active_only(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        active = self.add_deck_card("activePokemonArea", SNORLAX, P2)
        benched = self.add_deck_card("bench", ORANGURU, P2)
        self.attach(POWERFUL_COLORLESS, lugia, P1)
        self.assertEqual(compute_damage(self.board, lugia, active, 130).amount, 150)
        self.assertEqual(
            compute_damage(self.board, lugia, benched, 30, apply_modifiers=False).amount,
            30,
        )

    def test_double_turbo_reduces_damage_by_20(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        snorlax = self.add_deck_card("activePokemonArea", SNORLAX, P2)
        self.attach(DOUBLE_TURBO, lugia, P1)
        self.assertEqual(compute_damage(self.board, lugia, snorlax, 130).amount, 110)

    def test_v_guard_reduces_damage_from_v_attackers(self):
        stoutland = self.add_deck_card("activePokemonArea", STOUTLAND_V, P1)
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P2)
        self.attach(V_GUARD, lugia, P2)
        self.assertEqual(compute_damage(self.board, stoutland, lugia, 40).amount, 10)

    def test_v_guard_ignores_non_v_attackers(self):
        snorlax = self.add_deck_card("activePokemonArea", SNORLAX, P1)
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P2)
        self.attach(V_GUARD, lugia, P2)
        self.assertEqual(compute_damage(self.board, snorlax, lugia, 180).amount, 180)

    def test_v_guard_does_not_stack(self):
        stoutland = self.add_deck_card("activePokemonArea", STOUTLAND_V, P1)
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P2)
        self.attach(V_GUARD, lugia, P2)
        self.attach(V_GUARD, lugia, P2)
        # "This effect can't be applied more than once at a time."
        self.assertEqual(compute_damage(self.board, stoutland, lugia, 70).amount, 40)

    def test_mysterious_nest_removes_colorless_weakness(self):
        raikou = self.add_deck_card("activePokemonArea", RAIKOU, P1)
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P2)
        self.assertEqual(compute_damage(self.board, raikou, lugia, 120).amount, 240)
        self.add_deck_card("bench", DUNSPARCE, P1)
        self.assertEqual(compute_damage(self.board, raikou, lugia, 120).amount, 120)

    def test_excited_heart_discounts_colorless_cost(self):
        charizard = self.add_deck_card("activePokemonArea", RADIANT_CHARIZARD, P1)
        printed = {"Fire": 1, "Colorless": 4}
        self.assertEqual(
            effective_attack_cost(self.board, charizard, printed), printed
        )
        # Two prizes taken by the opponent: 6 dealt, 4 left in the pile.
        self.board.prizes_dealt[P2] = 6
        for _ in range(4):
            self.add_deck_card("prizePile", DUNSPARCE, P2)
        self.assertEqual(
            effective_attack_cost(self.board, charizard, printed),
            {"Fire": 1, "Colorless": 2},
        )

    def test_heat_fire_grants_20_max_hp(self):
        charizard = self.add_deck_card("activePokemonArea", RADIANT_CHARIZARD, P1)
        self.assertEqual(effective_max_hp(self.board, charizard), 160)
        self.attach(HEAT_FIRE, charizard, P1)
        self.assertEqual(effective_max_hp(self.board, charizard), 180)

    def test_heat_fire_grants_no_hp_to_non_fire_pokemon(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        base = effective_max_hp(self.board, lugia)
        self.attach(HEAT_FIRE, lugia, P1)
        self.assertEqual(effective_max_hp(self.board, lugia), base)


# ----------------------------------------------------------------------
# Pokemon effects
# ----------------------------------------------------------------------

class TestPokemonEffects(LugiaDeckTestBase):
    async def test_read_the_wind_discards_then_draws_3(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        self.add_deck_card("activePokemonArea", SNORLAX, P2)
        fodder = self.add_deck_card("hand", QUICK_BALL, P1)
        for _ in range(3):
            self.add_deck_card("deck", DUNSPARCE, P1)
        await resolve_attack(self.session, P1, lugia,
                             ability_named(LUGIA_V, "Read the Wind"), "a-1")
        discard = self.board.find_player_area(P1, "discard")
        self.assertIn(fodder, discard.children)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 3)

    async def test_tempest_dive_discards_stadium_on_yes(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_VSTAR, P1)
        self.add_deck_card("activePokemonArea", SNORLAX, P2)
        stadium_area = self.board.find_global_area("activeStadium")
        stadium = self.add_deck_card("discard", QUICK_BALL, P1)
        self.board.move_card(stadium.entity_id, stadium_area.entity_id)
        self.session.choice_replies = [0]  # Yes
        ctx = self.attack_ctx(lugia, LUGIA_VSTAR, "Tempest Dive")
        await ability_named(LUGIA_VSTAR, "Tempest Dive").effect(ctx)
        self.assertEqual(stadium_area.children, [])

    async def test_summoning_star_benches_only_rule_box_free_colorless(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_VSTAR, P1)
        dunsparce = self.add_deck_card("discard", DUNSPARCE, P1)
        lugia_v = self.add_deck_card("discard", LUGIA_V, P1)
        ctx = EffectContext(self.session, P1, lugia,
                            ability_named(LUGIA_VSTAR, "Summoning Star"))
        await ability_named(LUGIA_VSTAR, "Summoning Star").effect(ctx)
        offered = self.session.chooser_calls[0][1]
        self.assertEqual(offered, [dunsparce.entity_id])
        # The discard pile is public: the pick may not choose zero.
        self.assertEqual(self.session.chooser_calls[0][3], 1)
        bench = self.board.find_player_area(P1, "bench")
        self.assertIn(dunsparce, bench.children)
        self.assertNotIn(lugia_v, bench.children)

    async def test_primate_wisdom_swaps_hand_card_with_deck_top(self):
        oranguru = self.add_deck_card("bench", ORANGURU, P1)
        hand_card = self.add_deck_card("hand", QUICK_BALL, P1)
        bottom = self.add_deck_card("deck", DUNSPARCE, P1)
        top = self.add_deck_card("deck", MANAPHY, P1)
        ctx = EffectContext(self.session, P1, oranguru,
                            ability_named(ORANGURU, "Primate Wisdom"))
        await ability_named(ORANGURU, "Primate Wisdom").effect(ctx)
        deck = self.board.find_player_area(P1, "deck")
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(top, hand.children)
        self.assertEqual(deck.children[-1], hand_card)  # new deck top
        self.assertIn(bottom, deck.children)

    async def test_thumping_snore_puts_self_asleep_with_two_coin_checkup(self):
        snorlax = self.add_deck_card("activePokemonArea", SNORLAX, P1)
        self.add_deck_card("activePokemonArea", LUGIA_V, P2)
        ctx = self.attack_ctx(snorlax, SNORLAX, "Thumping Snore")
        await ability_named(SNORLAX, "Thumping Snore").effect(ctx)
        self.assertEqual(
            snorlax.get_attribute(AttrID.SPECIAL_CONDITIONS), ["Asleep"]
        )
        self.assertEqual(self.session.sleep_checkup_coins[snorlax.entity_id], 2)
        # The AddSpecialCondition bracket must lead with the "Target" data
        # effect (the executor's ctor indexes it, same as Remove/Evolve).
        runs = ctx.bracket_runs_for(P1)
        add_run = next(msgs for name, msgs in runs if name == "AddSpecialCondition")
        self.assertEqual(add_run[0]["name"], "EntityIDDataEffect")
        self.assertEqual(add_run[0]["value"]["key"], "Target")
        self.assertEqual(add_run[0]["value"]["value"], snorlax.entity_id)

    async def test_unfazed_fat_blocks_amazing_destruction(self):
        yveltal = self.add_deck_card("activePokemonArea", YVELTAL, P1)
        snorlax = self.add_deck_card("activePokemonArea", SNORLAX, P2)
        ctx = self.attack_ctx(yveltal, YVELTAL, "Amazing Destruction")
        await ability_named(YVELTAL, "Amazing Destruction").effect(ctx)
        self.assertEqual(ctx.knockouts, [])
        self.assertGreater(snorlax.get_attribute(AttrID.HP), 0)

    async def test_amazing_destruction_kos_unprotected_active(self):
        yveltal = self.add_deck_card("activePokemonArea", YVELTAL, P1)
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P2)
        ctx = self.attack_ctx(yveltal, YVELTAL, "Amazing Destruction")
        await ability_named(YVELTAL, "Amazing Destruction").effect(ctx)
        self.assertIn(lugia, ctx.knockouts)

    async def test_amazing_shot_bench_damage_blocked_by_wave_veil(self):
        raikou = self.add_deck_card("activePokemonArea", RAIKOU, P1)
        active = self.add_deck_card("activePokemonArea", SNORLAX, P2)
        manaphy = self.add_deck_card("bench", MANAPHY, P2)
        ctx = self.attack_ctx(raikou, RAIKOU, "Amazing Shot")
        await ability_named(RAIKOU, "Amazing Shot").effect(ctx)
        self.assertEqual(active.get_attribute(AttrID.HP), 150 - 120)
        self.assertEqual(manaphy.get_attribute(AttrID.HP), 70)  # protected

    async def test_double_dip_fangs_takes_extra_prize_on_basic_ko(self):
        stoutland = self.add_deck_card("activePokemonArea", STOUTLAND_V, P1)
        dunsparce = self.add_deck_card("activePokemonArea", DUNSPARCE, P2)
        dunsparce.set_attribute(AttrID.HP, 30)
        ctx = self.attack_ctx(stoutland, STOUTLAND_V, "Double Dip Fangs")
        await ability_named(STOUTLAND_V, "Double Dip Fangs").effect(ctx)
        self.assertIn(dunsparce, ctx.knockouts)
        self.assertEqual(ctx.extra_prizes, 1)

    async def test_wild_tackle_self_damage(self):
        stoutland = self.add_deck_card("activePokemonArea", STOUTLAND_V, P1)
        self.add_deck_card("activePokemonArea", LUGIA_V, P2)
        ctx = self.attack_ctx(stoutland, STOUTLAND_V, "Wild Tackle")
        await ability_named(STOUTLAND_V, "Wild Tackle").effect(ctx)
        self.assertEqual(stoutland.get_attribute(AttrID.HP), 210 - 30)

    async def test_aqua_return_shuffles_stack_into_deck(self):
        lumineon = self.add_deck_card("activePokemonArea", LUMINEON_V, P1)
        energy = self.attach(POWERFUL_COLORLESS, lumineon, P1)
        self.add_deck_card("activePokemonArea", SNORLAX, P2)
        await resolve_attack(self.session, P1, lumineon,
                             ability_named(LUMINEON_V, "Aqua Return"), "a-2")
        deck = self.board.find_player_area(P1, "deck")
        self.assertIn(lumineon, deck.children)
        self.assertIn(energy, deck.children)
        self.assertIsNone(self.board.active_pokemon(P1))

    async def test_luminous_sign_searches_supporter(self):
        lumineon = self.add_deck_card("bench", LUMINEON_V, P1)
        marnie = self.add_deck_card("deck", MARNIE, P1)
        self.add_deck_card("deck", DUNSPARCE, P1)
        ctx = EffectContext(self.session, P1, lumineon,
                            ability_named(LUMINEON_V, "Luminous Sign"))
        await ability_named(LUMINEON_V, "Luminous Sign").effect(ctx)
        self.assertEqual(self.session.chooser_calls[0][1], [marnie.entity_id])
        self.assertIn(marnie, self.board.find_player_area(P1, "hand").children)

    async def test_primal_turbo_attaches_special_energy_from_deck(self):
        archeops = self.add_deck_card("bench", ARCHEOPS, P1)
        lugia = self.add_deck_card("activePokemonArea", LUGIA_VSTAR, P1)
        aurora = self.add_deck_card("deck", AURORA, P1)
        powerful = self.add_deck_card("deck", POWERFUL_COLORLESS, P1)
        self.add_deck_card("deck", DUNSPARCE, P1)
        # Chooser 1: the two Special Energies; chooser 2: the target Pokemon.
        self.session.chooser_replies = [
            [aurora.entity_id, powerful.entity_id],
            [lugia.entity_id],
        ]
        ctx = EffectContext(self.session, P1, archeops,
                            ability_named(ARCHEOPS, "Primal Turbo"))
        await ability_named(ARCHEOPS, "Primal Turbo").effect(ctx)
        self.assertIn(aurora, lugia.children)
        self.assertIn(powerful, lugia.children)


# ----------------------------------------------------------------------
# Trainer effects
# ----------------------------------------------------------------------

class TestTrainerEffects(LugiaDeckTestBase):
    async def play_trainer(self, guid, player_id=P1):
        """Runs a trainer's registered effect the way the session does."""
        card = self.add_to("discard", deck_card(guid), player_id)
        trainer_area = self.board.find_global_area("activeTrainer")
        self.board.move_card(card.entity_id, trainer_area.entity_id)
        card.owning_player_id = player_id
        return await resolve_trainer_effect(self.session, player_id, card)

    async def test_professors_research_discards_hand_draws_7(self):
        held = [self.add_deck_card("hand", DUNSPARCE, P1) for _ in range(3)]
        for _ in range(8):
            self.add_deck_card("deck", QUICK_BALL, P1)
        await self.play_trainer(PROF_RESEARCH)
        discard = self.board.find_player_area(P1, "discard")
        for card in held:
            self.assertIn(card, discard.children)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 7)

    async def test_marnie_bottoms_hands_and_draws_5_and_4(self):
        mine = [self.add_deck_card("hand", DUNSPARCE, P1) for _ in range(2)]
        theirs = [self.add_deck_card("hand", MANAPHY, P2) for _ in range(3)]
        for _ in range(8):
            self.add_deck_card("deck", QUICK_BALL, P1)
            self.add_deck_card("deck", QUICK_BALL, P2)
        await self.play_trainer(MARNIE)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 5)
        self.assertEqual(len(self.board.find_player_area(P2, "hand").children), 4)
        p1_deck = self.board.find_player_area(P1, "deck")
        p2_deck = self.board.find_player_area(P2, "deck")
        # Old hands sit at the BOTTOM of the decks (positions 0..n-1).
        self.assertEqual(set(p1_deck.children[:2]), set(mine))
        self.assertEqual(set(p2_deck.children[:3]), set(theirs))

    async def test_marnie_choreography_is_sequential_per_player(self):
        for _ in range(2):
            self.add_deck_card("hand", DUNSPARCE, P1)
            self.add_deck_card("hand", MANAPHY, P2)
        for _ in range(8):
            self.add_deck_card("deck", QUICK_BALL, P1)
            self.add_deck_card("deck", QUICK_BALL, P2)
        hand = self.board.find_player_area(P1, "hand")
        deck = self.board.find_player_area(P1, "deck")
        ctx = await self.play_trainer(MARNIE)
        # Player's shuffle-to-bottom and draw fully precede the opponent's.
        runs = ctx.bracket_runs_for(P1)
        self.assertEqual(
            [name for name, _ in runs],
            ["HandShuffledAndMovedToDeck", "Draw",
             "HandShuffledAndMovedToDeck", "Draw"],
        )
        msgs = runs[0][1]
        self.assertEqual(msgs[0]["name"], "Shuffled")
        self.assertEqual(msgs[0]["value"]["entityID"], hand.entity_id)
        self.assertEqual(msgs[-1]["name"], "PlaceOnBottom")
        self.assertEqual(msgs[-1]["value"]["entityID"], hand.entity_id)
        self.assertEqual(msgs[-1]["value"]["target"], deck.entity_id)

    async def test_bosss_orders_gusts_chosen_bench_pokemon(self):
        self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        old_active = self.add_deck_card("activePokemonArea", SNORLAX, P2)
        benched = self.add_deck_card("bench", MANAPHY, P2)
        await self.play_trainer(BOSSS_ORDERS)
        self.assertIs(self.board.active_pokemon(P2), benched)
        bench = self.board.find_player_area(P2, "bench")
        self.assertIn(old_active, bench.children)

    async def test_escape_rope_switches_both_sides_opponent_first(self):
        my_active = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        my_bench = self.add_deck_card("bench", ORANGURU, P1)
        their_active = self.add_deck_card("activePokemonArea", SNORLAX, P2)
        their_bench = self.add_deck_card("bench", MANAPHY, P2)
        await self.play_trainer(ESCAPE_ROPE)
        self.assertIs(self.board.active_pokemon(P1), my_bench)
        self.assertIs(self.board.active_pokemon(P2), their_bench)
        # The opponent's chooser was prompted before the player's.
        self.assertEqual(self.session.chooser_calls[0][0], P2)
        self.assertEqual(self.session.chooser_calls[1][0], P1)
        self.assertIn(my_active, self.board.find_player_area(P1, "bench").children)
        self.assertIn(their_active, self.board.find_player_area(P2, "bench").children)

    async def test_quick_ball_discards_then_fetches_basic(self):
        fodder = self.add_deck_card("hand", EVOLUTION_INCENSE, P1)
        basic = self.add_deck_card("deck", DUNSPARCE, P1)
        self.add_deck_card("deck", ARCHEOPS, P1)  # not Basic: filtered out
        await self.play_trainer(QUICK_BALL)
        self.assertIn(fodder, self.board.find_player_area(P1, "discard").children)
        search_offer = self.session.chooser_calls[1][1]
        self.assertEqual(search_offer, [basic.entity_id])
        self.assertIn(basic, self.board.find_player_area(P1, "hand").children)

    async def test_ultra_ball_discards_two_then_fetches_any_pokemon(self):
        for _ in range(2):
            self.add_deck_card("hand", EVOLUTION_INCENSE, P1)
        archeops = self.add_deck_card("deck", ARCHEOPS, P1)
        self.add_deck_card("deck", QUICK_BALL, P1)
        await self.play_trainer(ULTRA_BALL)
        self.assertEqual(
            len(self.board.find_player_area(P1, "discard").children), 2
        )
        self.assertIn(archeops, self.board.find_player_area(P1, "hand").children)

    async def test_evolution_incense_fetches_evolution_pokemon(self):
        archeops = self.add_deck_card("deck", ARCHEOPS, P1)
        self.add_deck_card("deck", DUNSPARCE, P1)
        await self.play_trainer(EVOLUTION_INCENSE)
        self.assertEqual(self.session.chooser_calls[0][1], [archeops.entity_id])
        self.assertIn(archeops, self.board.find_player_area(P1, "hand").children)

    async def test_irida_fetches_water_pokemon_and_item(self):
        manaphy = self.add_deck_card("deck", MANAPHY, P1)
        quick_ball = self.add_deck_card("deck", QUICK_BALL, P1)
        self.add_deck_card("deck", DUNSPARCE, P1)  # neither Water nor Item
        await self.play_trainer(IRIDA)
        # One AND-composite browser with a Water group and an Item group,
        # not one combined pick of any 2 matches.
        water_offer, item_offer = self.session.chooser_calls[:2]
        self.assertEqual(water_offer[1], [manaphy.entity_id])
        self.assertEqual(item_offer[1], [quick_ball.entity_id])
        hand = self.board.find_player_area(P1, "hand")
        self.assertIn(manaphy, hand.children)
        self.assertIn(quick_ball, hand.children)

    async def test_serena_gust_mode_targets_only_pokemon_v(self):
        self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        self.add_deck_card("activePokemonArea", SNORLAX, P2)
        manaphy = self.add_deck_card("bench", MANAPHY, P2)
        lugia_v = self.add_deck_card("bench", LUGIA_V, P2)
        # Empty hand: the gust mode is auto-selected.
        await self.play_trainer(SERENA)
        offered = self.session.chooser_calls[0][1]
        self.assertEqual(offered, [lugia_v.entity_id])
        self.assertIs(self.board.active_pokemon(P2), lugia_v)
        self.assertIsNot(self.board.active_pokemon(P2), manaphy)

    async def test_serena_discard_mode_draws_to_five(self):
        self.add_deck_card("activePokemonArea", SNORLAX, P2)  # no V bench
        for _ in range(3):
            self.add_deck_card("hand", DUNSPARCE, P1)
        for _ in range(8):
            self.add_deck_card("deck", QUICK_BALL, P1)
        self.session.chooser_replies = [
            [self.board.find_player_area(P1, "hand").children[0].entity_id]
        ]
        await self.play_trainer(SERENA)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 5)

    async def test_lost_vacuum_sends_cost_and_target_to_lost_zone(self):
        fodder = self.add_deck_card("hand", DUNSPARCE, P1)
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        belt = self.attach(CHOICE_BELT, lugia, P1)
        await self.play_trainer(LOST_VACUUM)
        lost = self.board.find_player_area(P1, "lostZone")
        self.assertIn(fodder, lost.children)
        self.assertIn(belt, lost.children)
        self.assertNotIn(belt, lugia.children)


# ----------------------------------------------------------------------
# Special-energy hooks
# ----------------------------------------------------------------------

class TestEnergyHooks(LugiaDeckTestBase):
    async def test_aurora_attach_cost_discards_a_card(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        aurora = self.add_deck_card("hand", AURORA, P1)
        fodder = self.add_deck_card("hand", DUNSPARCE, P1)
        ctx = await resolve_energy_attach_cost(self.session, P1, aurora, lugia)
        self.assertIsNotNone(ctx)
        self.assertIn(fodder, self.board.find_player_area(P1, "discard").children)
        # The energy being attached is never offered as its own cost.
        self.assertNotIn(aurora.entity_id, self.session.chooser_calls[0][1])

    async def test_capture_energy_benches_a_basic_from_deck(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        capture = self.attach(CAPTURE, lugia, P1)
        basic = self.add_deck_card("deck", DUNSPARCE, P1)
        self.add_deck_card("deck", ARCHEOPS, P1)
        ctx = await resolve_energy_on_attach(self.session, P1, capture, lugia)
        self.assertIsNotNone(ctx)
        self.assertIn(basic, self.board.find_player_area(P1, "bench").children)
        self.assertIn(basic.entity_id, self.session.turn_state.entered_play_turn)

    async def test_speed_lightning_draws_two(self):
        raikou = self.add_deck_card("activePokemonArea", RAIKOU, P1)
        speed = self.attach(SPEED_LIGHTNING, raikou, P1)
        for _ in range(2):
            self.add_deck_card("deck", DUNSPARCE, P1)
        ctx = await resolve_energy_on_attach(self.session, P1, speed, raikou)
        self.assertIsNotNone(ctx)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 2)

    async def test_speed_lightning_no_draw_on_non_lightning_target(self):
        lugia = self.add_deck_card("activePokemonArea", LUGIA_V, P1)
        speed = self.attach(SPEED_LIGHTNING, lugia, P1)
        for _ in range(2):
            self.add_deck_card("deck", DUNSPARCE, P1)
        await resolve_energy_on_attach(self.session, P1, speed, lugia)
        self.assertEqual(len(self.board.find_player_area(P1, "hand").children), 0)


# ----------------------------------------------------------------------
# Legal-action gating
# ----------------------------------------------------------------------

class TestLegalActionGating(unittest.TestCase):
    def setUp(self):
        if not loader.cards_by_guid:
            loader.load_all()
        self.board = BoardState(GAME_ID, [P1, P2])
        self.state = TurnState()
        self.state.begin_turn(P1)
        self.state.begin_turn(P1)  # turn 2: attacks/supporters allowed

    def add(self, area_name, guid, player_id=P1):
        from spirit.game.models.board import create_card_entity
        entity = create_card_entity(deck_card(guid), owning_player_id=player_id)
        area = self.board.find_player_area(player_id, area_name)
        self.board.add_card_to_area(entity, area)
        return entity

    def actions(self, description):
        return [
            e for e in compute_legal_actions(self.board, self.state, P1, GAME_ID)
            if e["selectableAction"]["description"] == description
        ]

    def test_tool_offered_only_for_pokemon_without_a_tool(self):
        lugia = self.add("activePokemonArea", LUGIA_V)
        oranguru = self.add("bench", ORANGURU)
        self.add("hand", CHOICE_BELT)
        belt = self.add("discard", CHOICE_BELT)
        self.board.attach_card(belt.entity_id, lugia.entity_id)
        entries = self.actions(ACTION_ATTACH_TOOL)
        self.assertEqual(len(entries), 1)
        self.assertEqual(
            entries[0]["targetInfoLst"][0]["validTargets"], [oranguru.entity_id]
        )

    def test_special_energies_attach_to_any_pokemon(self):
        # SWSH special energies carry no attach restriction; their benefits
        # are type-gated in the passive/on_attach instead.
        lugia = self.add("activePokemonArea", LUGIA_V)
        charizard = self.add("bench", RADIANT_CHARIZARD)
        self.add("hand", HEAT_FIRE)
        entries = self.actions(ACTION_PLAY_ENERGY)
        self.assertEqual(len(entries), 1)
        self.assertEqual(
            set(entries[0]["targetInfoLst"][0]["validTargets"]),
            {lugia.entity_id, charizard.entity_id},
        )

    def test_aurora_needs_another_card_in_hand(self):
        self.add("activePokemonArea", LUGIA_V)
        self.add("hand", AURORA)
        self.assertEqual(self.actions(ACTION_PLAY_ENERGY), [])
        self.add("hand", DUNSPARCE)
        self.assertEqual(len(self.actions(ACTION_PLAY_ENERGY)), 1)

    def test_quick_ball_needs_another_card_to_discard(self):
        self.add("activePokemonArea", LUGIA_V)
        self.add("hand", QUICK_BALL)
        self.assertEqual(self.actions(ACTION_USE_TRAINER), [])
        self.add("hand", MANAPHY)
        self.assertEqual(len(self.actions(ACTION_USE_TRAINER)), 1)

    def test_bosss_orders_needs_an_opposing_bench(self):
        self.add("activePokemonArea", LUGIA_V)
        self.add("activePokemonArea", SNORLAX, P2)
        self.add("hand", BOSSS_ORDERS)
        self.assertEqual(self.actions(ACTION_USE_TRAINER), [])
        self.add("bench", MANAPHY, P2)
        self.assertEqual(len(self.actions(ACTION_USE_TRAINER)), 1)

    def test_activatable_ability_once_per_turn(self):
        archeops = self.add("bench", ARCHEOPS)
        self.add("activePokemonArea", LUGIA_V)
        entries = self.actions(ACTION_USE_ABILITY)
        self.assertEqual(len(entries), 1)
        ability_id = entries[0]["selectableAction"]["actionID"]
        self.state.used_abilities.add((archeops.entity_id, ability_id))
        self.assertEqual(self.actions(ACTION_USE_ABILITY), [])

    def test_vstar_power_once_per_game(self):
        self.add("activePokemonArea", LUGIA_VSTAR)
        # No valid discard target: Summoning Star may not be used at all.
        self.assertEqual(self.actions(ACTION_USE_ABILITY), [])
        self.add("discard", DUNSPARCE)
        self.assertEqual(len(self.actions(ACTION_USE_ABILITY)), 1)
        self.state.vstar_used.add(P1)
        self.assertEqual(self.actions(ACTION_USE_ABILITY), [])

    def test_combustion_blast_locked_after_use(self):
        charizard = self.add("activePokemonArea", RADIANT_CHARIZARD)
        for _ in range(5):
            energy = self.add("discard", HEAT_FIRE)
            self.board.attach_card(energy.entity_id, charizard.entity_id)
        entries = self.actions(ACTION_USE_ATTACK)
        self.assertEqual(len(entries), 1)
        self.state.lock_attack(
            charizard.entity_id, entries[0]["selectableAction"]["actionID"]
        )
        self.assertEqual(self.actions(ACTION_USE_ATTACK), [])
        # The lock expires after the user's next turn.
        self.state.turn_number += 3
        self.assertEqual(len(self.actions(ACTION_USE_ATTACK)), 1)

    def test_asleep_active_cannot_attack_or_retreat(self):
        snorlax = self.add("activePokemonArea", SNORLAX)
        self.add("bench", MANAPHY)
        for _ in range(4):
            energy = self.add("discard", POWERFUL_COLORLESS)
            self.board.attach_card(energy.entity_id, snorlax.entity_id)
        self.assertEqual(len(self.actions(ACTION_USE_ATTACK)), 1)
        self.assertEqual(len(self.actions(ACTION_RETREAT)), 1)
        snorlax.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Asleep"])
        self.assertEqual(self.actions(ACTION_USE_ATTACK), [])
        self.assertEqual(self.actions(ACTION_RETREAT), [])


if __name__ == "__main__":
    unittest.main()
