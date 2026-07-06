import unittest
import asyncio
import uuid
from unittest.mock import MagicMock, AsyncMock

from spirit.network.message_names import InboundMsg, OutboundMsg
from spirit.network.protocol import WargFlags
from spirit.game.session.game_session import GameSession
from spirit.game.session.manager import GameSessionManager
from spirit.packets.handlers.gameplay import GameplayHandler
from spirit.packets.handlers.data_sync import DataSyncHandler


class MockPlayer:
    def __init__(self, account_id, username):
        self.account_id = account_id
        self.username = username
        self.screen_name = username
        self.avatar_decks = []

    def get_avatar_decks_data(self):
        return {"decks": self.avatar_decks}

    def save_deck_data(self, deck_dict: dict, is_avatar: bool = False):
        if is_avatar:
            self.avatar_decks.append(deck_dict)


class MockClientHandler:
    def __init__(self, account_id, username):
        self.player = MockPlayer(account_id, username)
        self.addr = ("127.0.0.1", 12345)
        self.sent_packets = []

    async def send_packet(self, data, request_id=0, flags=0):
        # Handle dict or protobuf
        if hasattr(data, "SerializeToString"):
            # Mock protobuf payload
            self.sent_packets.append({
                "protobuf": data.__class__.__name__,
                "request_id": request_id,
                "flags": flags
            })
        else:
            self.sent_packets.append(data)


class TestGameplayFlow(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.session_manager = GameSessionManager()
        # Reset session manager state
        self.session_manager.active_sessions = {}
        self.session_manager.pending_pairings = {}

    async def test_player_ready_handshake(self):
        # 1. Setup mock clients and deck
        client1 = MockClientHandler("player-1", "Ash")
        client2 = MockClientHandler("player-2", "Gary")
        
        deck1 = {"deckID": "deck-1", "deckName": "Charizard", "cards": [{"guid": "00000000-0000-0000-0000-000000000002", "count": 2}]}
        deck2 = {"deckID": "deck-2", "deckName": "Blastoise", "cards": []}

        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "player-1": {"client": client1, "deck": deck1, "ready": True},
                "player-2": {"client": client2, "deck": deck2, "ready": True}
            }
        }

        # 2. Spawn GameSession
        game_id = str(uuid.uuid4())
        session = GameSession(game_id, pairing)
        self.session_manager.active_sessions[game_id] = session

        # Verify initial ready state is empty
        self.assertEqual(len(session.ready_players), 0)

        # 3. Simulate client 1 sending PlayerReady
        handler1 = GameplayHandler(client1)
        await handler1.handle_player_ready({}, request_id=1, flags=WargFlags.CLEAR)

        # Player 1 should be registered as ready
        self.assertIn("player-1", session.ready_players)
        self.assertEqual(len(session.ready_players), 1)
        
        # No SerializedGameState should be broadcast yet since player 2 is not ready
        self.assertEqual(len(client1.sent_packets), 0)

        # 4. Simulate client 2 sending PlayerReady
        handler2 = GameplayHandler(client2)
        await handler2.handle_player_ready({}, request_id=2, flags=WargFlags.CLEAR)

        # Yield back to the event loop to allow the background gameplay task to start
        await asyncio.sleep(0.01)

        # Both ready, should trigger SerializedGameState broadcast
        self.assertIn("player-2", session.ready_players)
        self.assertEqual(len(session.ready_players), 2)

        # Verify both players received the SerializedGameState packet.
        # The caller receives 2 packets (SerializedGameState + the wrapped
        # CoinFlipChoiceRequired prompt); the non-caller receives 4 (the
        # SerializedGameState + the complete OpponentPickingHeadsOrTails
        # bracket: StartSequence + CustomChoiceOfferMessage + StopSequence).
        self.assertIn(len(client1.sent_packets), [2, 4])
        self.assertIn(len(client2.sent_packets), [2, 4])
        self.assertEqual(len(client1.sent_packets) + len(client2.sent_packets), 6)

        # Every match packet must ride a SequenceMessage: bare messages are
        # executed twice by the client (inline + queued pump).
        for client in (client1, client2):
            for packet in client.sent_packets:
                self.assertEqual(packet["messageName"], "SequenceMessage")

        # The caller's prompt is a standalone empty-GUID SequenceMessage; the
        # non-caller's bracket is complete (Start ... Stop) so the sequence
        # pump renders the waiting screen immediately.
        caller_client, waiting_client = (
            (client1, client2) if len(client1.sent_packets) == 2 else (client2, client1)
        )
        prompt = caller_client.sent_packets[1]
        self.assertEqual(prompt["sequenceID"], "00000000-0000-0000-0000-000000000000")
        self.assertEqual(prompt["msg"]["name"], "CoinFlipChoiceRequired")
        self.assertEqual(len(prompt["msg"]["value"]["buttons"]), 2)

        bracket = waiting_client.sent_packets[1:]
        self.assertEqual(bracket[0]["msg"]["name"], "StartSequence")
        self.assertEqual(bracket[0]["msg"]["value"]["name"], "OpponentPickingHeadsOrTails")
        self.assertEqual(bracket[1]["msg"]["name"], "CustomChoiceOfferMessage")
        self.assertIsNone(bracket[1]["msg"]["value"]["sourceEntity"])
        self.assertEqual(bracket[2]["msg"]["name"], "StopSequence")
        # All three share the same (non-empty) sequence ID.
        self.assertEqual(len({p["sequenceID"] for p in bracket}), 1)
        self.assertNotEqual(bracket[0]["sequenceID"], "00000000-0000-0000-0000-000000000000")

        # The initial state must be wrapped in a standalone SequenceMessage with the
        # empty sequence ID; a bare SerializedGameState is applied twice by the
        # client and the second apply kills the sequence pump.
        gs_packet = client1.sent_packets[0]
        self.assertEqual(gs_packet["messageName"], "SequenceMessage")
        self.assertEqual(gs_packet["sequenceID"], "00000000-0000-0000-0000-000000000000")
        self.assertEqual(gs_packet["gameID"], game_id)
        self.assertEqual(gs_packet["msg"]["name"], "SerializedGameState")
        self.assertEqual(gs_packet["msg"]["value"]["gameID"], game_id)

        # Validate tree structure of Playmat root entity
        entities = gs_packet["msg"]["value"]["entities"]
        self.assertEqual(entities["entityName"], "com.direwolfdigital.cake.rules.entities.CakePlayMat")
        
        # Validate children areas: PlayerEntities
        children_names = [child["entityName"] for child in entities["children"]]
        self.assertIn("com.direwolfdigital.cake.rules.entities.CakePlayerEntity", children_names)
        
        # Confirm PlayAreas exist
        self.assertTrue(any(child["entityName"] == "com.direwolfdigital.game.core.PlayArea" for child in entities["children"]))

    async def test_full_pregame_coin_flip_flow(self):
        """Drives the entire pregame flow: coin call -> flip -> go-first ->
        ActivePlayerSet, and verifies the wire choreography the client's
        sequence pump and Selection system require."""
        from unittest.mock import patch
        from spirit.game.models.card import Card
        from spirit.game.attributes import AttrID, CardType, PokemonStage
        from spirit.game.scripts.cards import loader as card_loader

        # Register a Basic Pokemon so both decks have real, drawable cards.
        mon = Card(
            guid="e2e-basic-mon",
            key="X",
            display_name="Testmon",
            attributes={
                str(AttrID.CARD_TYPE.value): {"value": CardType.POKEMON.value},
                str(AttrID.STAGE.value): {"value": PokemonStage.BASIC.value},
            },
        )
        card_loader.cards_by_guid[mon.guid] = mon
        deck = {"cards": [{"guid": mon.guid, "count": 20}]}

        client1 = MockClientHandler("player-1", "Ash")
        client2 = MockClientHandler("player-2", "Gary")
        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "player-1": {"client": client1, "deck": dict(deck, deckID="d1", deckName="A"), "ready": True},
                "player-2": {"client": client2, "deck": dict(deck, deckID="d2", deckName="B"), "ready": True},
            },
        }

        game_id = str(uuid.uuid4())
        session = GameSession(game_id, pairing)
        self.session_manager.active_sessions[game_id] = session

        clients = {"player-1": client1, "player-2": client2}

        # Neutralize the 3s animation delay without breaking the test's own
        # waits (game_session shares the global asyncio module).
        real_sleep = asyncio.sleep
        with patch(
            "spirit.game.session.game_session.asyncio.sleep",
            new=lambda *_args, **_kwargs: real_sleep(0),
        ):
            await session.mark_player_ready("player-1")
            await session.mark_player_ready("player-2")
            await real_sleep(0.05)

            caller_id = session.coin_flip_caller_id
            self.assertIsNotNone(caller_id)

            # Caller picks Heads (button 0). The live client reports the picked
            # button index in the "selection" field of GameCustomChoice.
            await session.receive_player_action(caller_id, {"selection": 0, "counter": 1})
            await real_sleep(0.05)

            winner_id = session.coin_flip_winner_id
            self.assertIsNotNone(winner_id)

            # Winner chooses to go first (button 0 = Yes)
            await session.receive_player_action(winner_id, {"selection": 0, "counter": 2})
            await real_sleep(0.05)

            # Both decks have Basics in the opening hand, so no mulligans; the
            # session moves straight to concurrent Active placement offers.
            self.assertEqual(session.game_phase, "PLACEMENT_PHASE")

            def latest_offer(client):
                for p in reversed(client.sent_packets):
                    if (
                        p.get("messageName") == "SequenceMessage"
                        and p["msg"]["name"] == "SelectionWithTargetsRequired"
                    ):
                        return p["msg"]["value"]
                return None

            def pause_prompts(client):
                return [
                    p["msg"]["value"]["prompt"]["id"] for p in client.sent_packets
                    if p.get("messageName") == "SequenceMessage"
                    and p["msg"]["name"] == "PauseOnPromptEffect"
                ]

            # Each player places the first offered Basic as their Active.
            # The offer is a single-level SelectionWithTargetsRequired whose
            # targetMap keys are the draggable basics and whose targetType
            # (node Kind) drives the client's active-spot drop machinery.
            for pid, client in clients.items():
                offer = latest_offer(client)
                self.assertIsNotNone(offer, f"{pid} got no active placement offer")
                self.assertEqual(offer["targetType"], "KnockoutPokemonTargetInformation")
                # forced=false keeps the Next button label "Done"; the button is
                # actually hidden by the PauseOnPromptEffect override, which must
                # precede the offer.
                self.assertFalse(offer["forced"])
                self.assertIn(
                    "Choose a Basic Pokémon to be your Active Pokémon",
                    pause_prompts(client),
                )
                card_id = next(iter(offer["targetMap"].keys()))
                await session.receive_player_action(pid, {
                    "gameID": game_id,
                    "selection": {"entityID": card_id, "targetResponses": []},
                    "counter": offer["counter"],
                })
            await real_sleep(0.05)

            # The first player to finish waits on the opponent (center prompt);
            # the barrier then clears the overrides on both clients before bench.
            all_pause_texts = [t for c in clients.values() for t in pause_prompts(c)]
            self.assertIn(
                "Please wait while your opponent chooses an Active Pokémon.",
                all_pause_texts,
            )
            for pid, client in clients.items():
                closes = [
                    p for p in client.sent_packets
                    if p.get("messageName") == "SequenceMessage"
                    and p["msg"]["name"] == "ClosePauseOnPromptEffect"
                ]
                self.assertTrue(closes, f"{pid} never got ClosePauseOnPromptEffect")

            # Both decline the (optional) bench offer: selection null = Done.
            for pid, client in clients.items():
                offer = latest_offer(client)
                self.assertIsNotNone(offer, f"{pid} got no bench offer")
                self.assertEqual(offer["targetType"], "InitialBenchedTargetInformation")
                self.assertFalse(offer["forced"])
                await session.receive_player_action(
                    pid, {"gameID": game_id, "selection": None, "counter": offer["counter"]}
                )
            await real_sleep(0.05)

        # Setup finished and the session moved straight into the turn loop
        # (turn 1's action offer is pending on the active player).
        self.assertEqual(session.game_phase, "TURN_LOOP")

        # The winner chose "Yes" (go first), so every active-player
        # announcement (pregame + turn 1's begin-turn bracket) names the
        # winner.
        active_player_ids = [
            p["msg"]["value"]["accountID"] for p in client1.sent_packets
            if p.get("messageName") == "SequenceMessage"
            and p["msg"]["name"] == "ActivePlayerSet"
        ]
        self.assertTrue(active_player_ids)
        self.assertTrue(all(pid == winner_id for pid in active_player_ids))

        def sequence_names(client):
            return [
                p["msg"]["value"]["name"] for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage" and p["msg"]["name"] == "StartSequence"
            ]

        def message_names(client):
            return [
                p["msg"]["name"] for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage"
            ]

        loser_id = next(pid for pid in ("player-1", "player-2") if pid != winner_id)
        winner_client, loser_client = clients[winner_id], clients[loser_id]

        # ForceSelectionFinished must never be sent: on the client without an
        # active selection it bumps the skip counter that swallows the next
        # selection offer (m.d / E.a).
        for client in (client1, client2):
            self.assertNotIn("ForceSelectionFinished", message_names(client))
            # Both clients see the flip and the active-player announcement.
            self.assertIn("InitialCoinFlip", sequence_names(client))
            self.assertIn("ActivePlayerSet", sequence_names(client))
            # Every bracket sent to a client must be complete (Start/Stop pairs).
            names = message_names(client)
            self.assertEqual(names.count("StartSequence"), names.count("StopSequence"))

        # Selection prompts go only to the choosing player; waiting sequences
        # go only to the other player.
        caller_client = clients[caller_id]
        opponent_client = clients[next(pid for pid in ("player-1", "player-2") if pid != caller_id)]
        self.assertIn("CoinFlipChoiceRequired", message_names(caller_client))
        self.assertNotIn("CoinFlipChoiceRequired", message_names(opponent_client))
        self.assertIn("OpponentPickingHeadsOrTails", sequence_names(opponent_client))
        self.assertNotIn("OpponentPickingHeadsOrTails", sequence_names(caller_client))

        self.assertIn("GoFirstChoiceRequired", message_names(winner_client))
        self.assertNotIn("GoFirstChoiceRequired", message_names(loser_client))
        self.assertIn("OpponentChoosingToGoFirst", sequence_names(loser_client))
        self.assertNotIn("OpponentChoosingToGoFirst", sequence_names(winner_client))

        # Setup phase: each deck's shuffle animation fires (as a standalone
        # empty-GUID Shuffled message) BEFORE the DealInitialHands bracket.
        for client in (client1, client2):
            packets = client.sent_packets
            shuffle_idx = [
                i for i, p in enumerate(packets)
                if p.get("messageName") == "SequenceMessage"
                and p["msg"]["name"] == "Shuffled"
            ]
            deal_start_idx = next(
                i for i, p in enumerate(packets)
                if p.get("messageName") == "SequenceMessage"
                and p["msg"]["name"] == "StartSequence"
                and p["msg"]["value"]["name"] == "DealInitialHands"
            )
            # Both players' decks shuffle, and every shuffle precedes the deal.
            self.assertEqual(len(shuffle_idx), 2)
            self.assertTrue(all(i < deal_start_idx for i in shuffle_idx))
            for i in shuffle_idx:
                self.assertEqual(packets[i]["sequenceID"], "00000000-0000-0000-0000-000000000000")

        def bracket_inner(client, seq_name):
            """Messages between the first Start/Stop pair of the named bracket."""
            msgs, in_bracket = [], False
            for p in client.sent_packets:
                if p.get("messageName") != "SequenceMessage":
                    continue
                m = p["msg"]
                if m["name"] == "StartSequence" and m["value"]["name"] == seq_name:
                    in_bracket = True
                    continue
                if m["name"] == "StopSequence" and m["value"]["name"] == seq_name:
                    break
                if in_bracket:
                    msgs.append(m)
            return msgs

        # Setup phase: EntityIntroduced reveals for the viewer's own 7 cards
        # arrive as standalone empty-GUID messages BEFORE the bracket (the
        # DealInitialHands executor runs GroupedMove children before flat
        # commands, so in-bracket intros would only apply after the deal
        # animation), and the 14 moves ride two GroupedMove children -- one
        # per player -- which the client executes in PARALLEL so both hands
        # fan out simultaneously.
        for pid, client in clients.items():
            self.assertIn("DealInitialHands", sequence_names(client))
            seq_packets = [
                p for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage"
            ]
            deal_start = next(
                i for i, p in enumerate(seq_packets)
                if p["msg"]["name"] == "StartSequence"
                and p["msg"]["value"]["name"] == "DealInitialHands"
            )
            intros = [
                p for p in seq_packets[:deal_start]
                if p["msg"]["name"] == "EntityIntroduced"
            ]
            self.assertEqual(len(intros), 7)
            # Only the recipient's own cards are revealed, as standalone
            # (empty-GUID) messages so they apply before the deal animates.
            hand = session.board_state.find_player_area(pid, "hand")
            active = session.board_state.find_player_area(pid, "activePokemonArea")
            own_ids = {c.entity_id for c in hand.children} | {c.entity_id for c in active.children}
            for intro in intros:
                self.assertEqual(intro["sequenceID"], "00000000-0000-0000-0000-000000000000")
                self.assertIn(intro["msg"]["value"]["entityID"], own_ids)
                self.assertTrue(intro["msg"]["value"]["attributeMap"])

            deal_inner = bracket_inner(client, "DealInitialHands")
            group_starts = [
                m for m in deal_inner
                if m["name"] == "StartSequence" and m["value"]["name"] == "GroupedMove"
            ]
            deal_moves = [m for m in deal_inner if m["name"] == "EntityMoved"]
            self.assertEqual(len(group_starts), 2)
            self.assertEqual(len(deal_moves), 14)
            # 2 GroupedMove children (Start + 7 moves + Stop each).
            self.assertEqual(len(deal_inner), 18)
            self.assertNotIn("EntityIntroduced", [m["name"] for m in deal_inner])

        # Placement: each placed Active is echoed in an InitialPick bracket to
        # both clients, and each client is shown the OPPONENT's placed card via
        # exactly one EntityIntroduced inside IntroduceInitialPokemon.
        for pid, client in clients.items():
            self.assertIn("InitialPick", sequence_names(client))
            introduced = bracket_inner(client, "IntroduceInitialPokemon")
            self.assertEqual([m["name"] for m in introduced], ["EntityIntroduced"])
            opponent_id = next(p for p in clients if p != pid)
            opp_active = session.board_state.find_player_area(opponent_id, "activePokemonArea")
            self.assertEqual(introduced[0]["value"]["entityID"], opp_active.children[0].entity_id)
            # The reveal carries the full render attributes inline.
            self.assertTrue(introduced[0]["value"]["attributeMap"])

        # Prizes: 6 per player dealt in one DealInitialPrizeCards bracket.
        # This uses two GroupedMove children (one per player) to deal prizes in parallel.
        for client in (client1, client2):
            prize_inner = bracket_inner(client, "DealInitialPrizeCards")
            group_starts = [
                m for m in prize_inner
                if m["name"] == "StartSequence" and m["value"]["name"] == "GroupedMove"
            ]
            prize_moves = [m for m in prize_inner if m["name"] == "EntityMoved"]
            self.assertEqual(len(group_starts), 2)
            self.assertEqual(len(prize_moves), 12)
            # 2 GroupedMove children (Start + 6 moves + Stop each)
            self.assertEqual(len(prize_inner), 16)

        # Server-side board reflects the full setup: 6 in hand (7 - active),
        # 1 active, 6 prizes, 7 left in deck (20 - 7 - 6) -- plus the turn-1
        # draw for the going-first player (the winner chose to go first).
        for pid in ("player-1", "player-2"):
            turn_draw = 1 if pid == winner_id else 0
            self.assertEqual(len(session.board_state.find_player_area(pid, "hand").children), 6 + turn_draw)
            self.assertEqual(len(session.board_state.find_player_area(pid, "activePokemonArea").children), 1)
            self.assertEqual(len(session.board_state.find_player_area(pid, "bench").children), 0)
            self.assertEqual(len(session.board_state.find_player_area(pid, "prizePile").children), 6)
            self.assertEqual(len(session.board_state.find_player_area(pid, "deck").children), 7 - turn_draw)

        # ---- Turn 1: only the going-first player gets the action offer ----
        def latest_action_offer(client):
            for p in reversed(client.sent_packets):
                if (
                    p.get("messageName") == "SequenceMessage"
                    and p["msg"]["name"] == "SelectionWithTargetsAndActionsRequired"
                ):
                    return p["msg"]["value"]
            return None

        offer = latest_action_offer(winner_client)
        self.assertIsNotNone(offer, "active player got no main action offer")
        self.assertIsNone(latest_action_offer(loser_client))
        # forced=false lets the root advance with nothing selected (End Turn).
        self.assertFalse(offer["forced"])
        self.assertEqual(offer["targetType"], "Ability")
        # All 7 basics in hand are playable (bench empty); the test Pokemon
        # has no attacks/energy so nothing else is offered.
        self.assertEqual(len(offer["targetMap"]), 7)
        entry = offer["targetMap"][0]
        self.assertEqual(entry["selectableAction"]["description"], "DefaultPokemonPlayAbility")
        self.assertEqual(entry["selectableAction"]["selectionType"], "Ability")
        bench_id = session.board_state.find_player_area(winner_id, "bench").entity_id
        self.assertEqual(entry["targetInfoLst"][0]["validTargets"], [bench_id])
        # No prompt on the main offer -- it would render as a stuck banner.
        self.assertIsNone(offer["prompt"])

        # Bench one basic. The reply mirrors Outgoing.SelectionWithTargetsAndActions:
        # selection = [[entityID, actionID], [targetResponses...]].
        await session.receive_player_action(winner_id, {
            "gameID": game_id,
            "selection": [
                [entry["entityID"], entry["selectableAction"]["actionID"]],
                [],
            ],
            "counter": offer["counter"],
        })
        await real_sleep(0.05)

        bench = session.board_state.find_player_area(winner_id, "bench")
        self.assertEqual([c.entity_id for c in bench.children], [entry["entityID"]])
        # The play is echoed to both viewers in a PlayCard bracket; the
        # opponent gets the intro in a preceding SerialSequence bracket (the
        # play executor reads the card TYPE before its own bracket executes).
        for pid, client in clients.items():
            play_inner = [m["name"] for m in bracket_inner(client, "PlayCard")]
            self.assertEqual(play_inner, ["EntityMoved"])
            intro_inner = [m["name"] for m in bracket_inner(client, "SerialSequence")]
            if pid == winner_id:
                self.assertEqual(intro_inner, [])
            else:
                self.assertEqual(intro_inner, ["EntityIntroduced"])

        # A recomputed offer follows: 6 playable cards left, plus a retreat on
        # the Active now that the bench is occupied (no RETREAT_COST attr =
        # free retreat). Ending the turn (selection null) passes play.
        offer2 = latest_action_offer(winner_client)
        self.assertNotEqual(offer2["counter"], offer["counter"])
        self.assertEqual(len(offer2["targetMap"]), 7)
        retreat_entries = [
            e for e in offer2["targetMap"]
            if e["selectableAction"]["description"] == "BaseRetreat"
        ]
        self.assertEqual(len(retreat_entries), 1)
        self.assertEqual(
            retreat_entries[0]["targetInfoLst"][0]["name"],
            "RetreatNewActiveTargetInformation",
        )
        await session.receive_player_action(winner_id, {
            "gameID": game_id, "selection": None, "counter": offer2["counter"],
        })
        await real_sleep(0.05)

        # Turn 2: the opponent draws their turn card and gets their offer.
        self.assertEqual(session.turn_state.turn_number, 2)
        self.assertEqual(session.turn_state.active_player_id, loser_id)
        self.assertEqual(
            len(session.board_state.find_player_area(loser_id, "hand").children), 7
        )
        self.assertIsNotNone(latest_action_offer(loser_client))

    async def test_draw_and_mulligan_helpers(self):
        """BoardState.draw_cards moves cards deck->hand and reports Basic Pokemon presence."""
        from spirit.game.models.board import BoardState
        from spirit.game.models.card import Card
        from spirit.game.attributes import AttrID, CardType, PokemonStage
        from spirit.game.scripts.cards import loader as card_loader

        basic = Card(
            guid="basic-mon-guid",
            key="X",
            display_name="Basicmon",
            attributes={
                str(AttrID.CARD_TYPE.value): {"value": CardType.POKEMON.value},
                str(AttrID.STAGE.value): {"value": PokemonStage.BASIC.value},
            },
        )
        card_loader.cards_by_guid[basic.guid] = basic

        board = BoardState("game-draw", ["p1"])
        board.populate_deck("p1", {"cards": [{"guid": basic.guid, "count": 10}]})

        deck = board.find_player_area("p1", "deck")
        self.assertEqual(len(deck.children), 10)

        drawn = board.draw_cards("p1", 7)
        self.assertEqual(len(drawn), 7)
        self.assertEqual(len(board.find_player_area("p1", "hand").children), 7)
        self.assertEqual(len(deck.children), 3)
        # Each descriptor targets the hand area with an ascending position.
        hand_id = board.find_player_area("p1", "hand").entity_id
        self.assertTrue(all(d["destination_id"] == hand_id for d in drawn))
        self.assertEqual([d["position"] for d in drawn], list(range(7)))

        # Hand has Basic Pokemon -> no mulligan required.
        self.assertTrue(board.has_basic_pokemon_in_hand("p1"))

        # Shuffling with distinct seeds produces distinct orderings (same deck).
        import random as _random

        board_a = BoardState("ga", ["p1"])
        board_a.populate_deck("p1", {"cards": [{"guid": basic.guid, "count": 20}]})
        deck_a = board_a.find_player_area("p1", "deck")
        original = [c.entity_id for c in deck_a.children]
        board_a.shuffle_deck("p1", rng=_random.Random(1))
        shuffled_1 = [c.entity_id for c in deck_a.children]
        board_a.shuffle_deck("p1", rng=_random.Random(2))
        shuffled_2 = [c.entity_id for c in deck_a.children]
        # A seeded shuffle changes order and is reproducible.
        self.assertNotEqual(original, shuffled_1)
        self.assertNotEqual(shuffled_1, shuffled_2)

        # Returning the hand refills the deck.
        board.return_hand_to_deck("p1")
        self.assertEqual(len(board.find_player_area("p1", "hand").children), 0)
        self.assertEqual(len(deck.children), 10)

    async def test_mulligan_loop_reveal_and_extra_draw(self):
        """A Basic-less hand mulligans (Mulligan bracket + redraw), the busted
        hand is revealed to both clients via MulliganRevealCardsEffect, and the
        opponent gets a Yes/No CustomChoiceRequired extra-draw offer (never
        MulliganChoiceRequired, which has no client UI)."""
        from unittest.mock import patch
        from spirit.game.models.board import PokemonEntity
        from spirit.game.models.card import Card
        from spirit.game.attributes import AttrID, CardType, PokemonStage
        from spirit.game.scripts.cards import loader as card_loader

        basic = Card(
            guid="mull-basic-guid",
            key="X",
            display_name="Mullmon",
            attributes={
                str(AttrID.CARD_TYPE.value): {"value": CardType.POKEMON.value},
                str(AttrID.STAGE.value): {"value": PokemonStage.BASIC.value},
            },
        )
        trainer = Card(
            guid="mull-trainer-guid",
            key="X",
            display_name="Mullhelper",
            attributes={
                str(AttrID.CARD_TYPE.value): {"value": CardType.TRAINER.value},
            },
        )
        card_loader.cards_by_guid[basic.guid] = basic
        card_loader.cards_by_guid[trainer.guid] = trainer

        client1 = MockClientHandler("player-1", "Ash")
        client2 = MockClientHandler("player-2", "Gary")
        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "player-1": {
                    "client": client1,
                    "deck": {
                        "deckID": "d1", "deckName": "A",
                        "cards": [
                            {"guid": basic.guid, "count": 13},
                            {"guid": trainer.guid, "count": 7},
                        ],
                    },
                    "ready": True,
                },
                "player-2": {
                    "client": client2,
                    "deck": {
                        "deckID": "d2", "deckName": "B",
                        "cards": [{"guid": basic.guid, "count": 20}],
                    },
                    "ready": True,
                },
            },
        }

        game_id = str(uuid.uuid4())
        session = GameSession(game_id, pairing)
        board = session.board_state

        # Deterministic opening: player-1's hand is 7 trainers (mulligan),
        # player-2's is 7 basics. The mulligan reshuffle puts basics on top.
        p1_hand = board.find_player_area("player-1", "hand")
        p1_deck = board.find_player_area("player-1", "deck")
        for card in [c for c in list(p1_deck.children) if not isinstance(c, PokemonEntity)]:
            board.move_card(card.entity_id, p1_hand.entity_id)
        board.draw_cards("player-2", 7)
        self.assertEqual(len(p1_hand.children), 7)
        self.assertFalse(board.has_basic_pokemon_in_hand("player-1"))

        def fake_shuffle(player_id, rng=None):
            deck = board.find_player_area(player_id, "deck")
            basics = [c for c in deck.children if isinstance(c, PokemonEntity)]
            others = [c for c in deck.children if not isinstance(c, PokemonEntity)]
            deck.children[:] = others + basics  # basics drawn first (top = end)
            return True

        real_sleep = asyncio.sleep
        with patch.object(board, "shuffle_deck", side_effect=fake_shuffle), patch(
            "spirit.game.session.game_session.asyncio.sleep",
            new=lambda *_a, **_k: real_sleep(0),
        ):
            task = asyncio.create_task(session.run_mulligan_phase())
            # Wait for the extra-draw prompt to reach player-2.
            for _ in range(100):
                await real_sleep(0.01)
                prompt = next(
                    (p["msg"]["value"] for p in reversed(client2.sent_packets)
                     if p.get("messageName") == "SequenceMessage"
                     and p["msg"]["name"] == "CustomChoiceRequired"),
                    None,
                )
                if prompt:
                    break
            self.assertIsNotNone(prompt, "player-2 never got the extra-draw offer")
            self.assertEqual(prompt.get("kind"), "")
            self.assertEqual(prompt.get("offerLength"), 0)
            await session.receive_player_action(
                "player-2", {"gameID": game_id, "selection": 0, "counter": prompt["counter"]}
            )
            await asyncio.wait_for(task, timeout=5)

        def message_names(client):
            return [
                p["msg"]["name"] for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage"
            ]

        def sequence_names(client):
            return [
                p["msg"]["value"]["name"] for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage" and p["msg"]["name"] == "StartSequence"
            ]

        for client in (client1, client2):
            # Mulligan bracket (hand back + Shuffled) then a Draw bracket redraw.
            self.assertIn("Mulligan", sequence_names(client))
            self.assertIn("Draw", sequence_names(client))
            self.assertIn("Shuffled", message_names(client))
            # The hand-return moves ride a nested GroupedMove bracket inside
            # the Mulligan bracket (the Mulligan executor runs inner commands
            # sequentially; GroupedMove animates them together). All 7 moves
            # must carry the CHILD's sequenceID, opened inside the parent.
            envelopes = [
                p for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage"
            ]
            group_start = next(
                i for i, p in enumerate(envelopes)
                if p["msg"]["name"] == "StartSequence"
                and p["msg"]["value"]["name"] == "GroupedMove"
            )
            child_id = envelopes[group_start]["msg"]["value"]["sequenceID"]
            mull_start = next(
                i for i, p in enumerate(envelopes)
                if p["msg"]["name"] == "StartSequence"
                and p["msg"]["value"]["name"] == "Mulligan"
            )
            self.assertLess(mull_start, group_start)
            group_moves = envelopes[group_start + 1:group_start + 8]
            for move in group_moves:
                self.assertEqual(move["msg"]["name"], "EntityMoved")
                self.assertEqual(move["sequenceID"], child_id)
            self.assertEqual(envelopes[group_start + 8]["msg"]["name"], "StopSequence")
            self.assertEqual(
                envelopes[group_start + 8]["msg"]["value"]["sequenceID"], child_id
            )
            # The busted hand is revealed to BOTH clients (the carousel
            # special-cases the owning player), with attributes inline.
            self.assertIn("RevealMulligans", sequence_names(client))
            reveal = next(
                p["msg"]["value"] for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage"
                and p["msg"]["name"] == "MulliganRevealCardsEffect"
            )
            self.assertEqual(reveal["player"], "player-1")
            self.assertEqual(len(reveal["entityIDPiles"]), 1)
            self.assertEqual(len(reveal["entityIDPiles"][0]), 7)
            # Every revealed card must inline attr 10000 (archetype GUID):
            # MulliganSetContents resolves the archetype through it and
            # crashes with ArgumentNullException when it is absent.
            for attr_list in reveal["entityIDPiles"][0].values():
                self.assertIn(
                    {"name": AttrID.ARCHETYPE_ID.value, "value": trainer.guid,
                     "originalValue": trainer.guid, "modValue": trainer.guid},
                    attr_list,
                )
            # MulliganChoiceRequired has no client UI; it must never be sent.
            self.assertNotIn("MulliganChoiceRequired", message_names(client))

        # Only the non-mulliganing player is offered the extra draw.
        self.assertNotIn("CustomChoiceRequired", message_names(client1))
        self.assertIn("CustomChoiceRequired", message_names(client2))

        # player-1 redrew into a Basic hand; player-2 drew the extra card.
        self.assertTrue(board.has_basic_pokemon_in_hand("player-1"))
        self.assertEqual(len(board.find_player_area("player-1", "hand").children), 7)
        self.assertEqual(len(board.find_player_area("player-2", "hand").children), 8)

    async def test_serialized_state_hides_opponent_cards(self):
        """Per-viewer serialization: cards you don't own carry attributes=null
        (un-introduced -> face-down back on the client); your own cards keep
        their full render attributes. Structural entities are never hidden."""
        from spirit.game.models.board import BoardState
        from spirit.game.models.card import Card
        from spirit.game.attributes import AttrID, CardType, PokemonStage
        from spirit.game.scripts.cards import loader as card_loader

        basic = Card(
            guid="hide-basic-guid",
            key="X",
            display_name="Hidemon",
            attributes={
                str(AttrID.CARD_TYPE.value): {"value": CardType.POKEMON.value},
                str(AttrID.STAGE.value): {"value": PokemonStage.BASIC.value},
            },
        )
        card_loader.cards_by_guid[basic.guid] = basic

        board = BoardState("g-hide", ["p1", "p2"])
        deck_data = {"cards": [{"guid": basic.guid, "count": 3}]}
        board.populate_deck("p1", deck_data)
        board.populate_deck("p2", deck_data)

        def collect_cards(node, out):
            if node["entityName"].endswith(".Pokemon"):
                out.append(node)
            for child in node["children"]:
                collect_cards(child, out)

        # All cards start in the decks: hidden from EVERYONE, including their
        # owner (deck order and prize faces are hidden knowledge; the owner
        # only learns a card via EntityIntroduced on draw).
        p1_view_cards = []
        collect_cards(board.serialize("p1")["entities"], p1_view_cards)
        self.assertEqual(len(p1_view_cards), 6)
        for card in p1_view_cards:
            self.assertIsNone(card["attributes"])

        # Own cards in visible zones (hand) serialize introduced; hidden
        # zones (deck, prizePile) stay face-down even for the owner.
        board.draw_cards("p1", 1)
        board.deal_from_deck("p1", "prizePile", 1)
        by_zone = {
            zone: board.find_player_area("p1", zone).children[0].serialize("p1")
            for zone in ("hand", "prizePile", "deck")
        }
        self.assertIsNotNone(by_zone["hand"]["attributes"])
        self.assertIsNone(by_zone["prizePile"]["attributes"])
        self.assertIsNone(by_zone["deck"]["attributes"])
        # The opponent sees all of them face-down.
        for zone in ("hand", "prizePile", "deck"):
            card = board.find_player_area("p1", zone).children[0]
            self.assertIsNone(card.serialize("p2")["attributes"])

        # Omniscient view (no viewer) keeps everything introduced.
        full_view_cards = []
        collect_cards(board.serialize()["entities"], full_view_cards)
        self.assertTrue(all(c["attributes"] is not None for c in full_view_cards))

        # Structural entities are never hidden in any view.
        p2_view = board.serialize("p2")["entities"]
        self.assertIsNotNone(p2_view["attributes"])
        for child in p2_view["children"]:
            self.assertIsNotNone(child["attributes"])

        # The bench area must carry the slot count (201920): the client's
        # BenchLayout divides by it, and a missing value NaNs every benched
        # card's transform (invisible card + collider crash).
        bench = board.find_player_area("p1", "bench")
        self.assertEqual(bench.get_attribute(AttrID.AREA_SLOTS), 5)
        serialized_bench = bench.serialize("p2")
        slot_attrs = [a["value"] for a in serialized_bench["attributes"] if a["name"] == AttrID.AREA_SLOTS.value]
        self.assertEqual(slot_attrs, [5])

    async def test_card_entity_carries_match_render_attributes(self):
        """In-match card faces render from the entity's own attributes (pie k.P
        builds the set/type facets via entity.GetAttribute, no archetype cache).
        Each card entity must carry the set code (200580) and collector number
        (200780) or the client can't form a texture-bundle key. Attribute 10020
        must NOT be the set code (the type facet reads it as an image-name
        override that would replace the collector-number key)."""
        from spirit.game.models.board import BoardState
        from spirit.game.models.card import PokemonCard
        from spirit.game.attributes import AttrID, CardType, PokemonStage
        from spirit.game.scripts.cards import loader as card_loader

        mon = PokemonCard(
            guid="render-mon-guid",
            key="BW1",
            display_name="Rendermon",
            attributes={
                str(AttrID.CARD_TYPE.value): {"value": CardType.POKEMON.value},
                str(AttrID.STAGE.value): {"value": PokemonStage.BASIC.value},
                str(AttrID.COLLECTOR_NUMBER.value): {"value": 79},
            },
        )
        card_loader.cards_by_guid[mon.guid] = mon

        board = BoardState("g-render", ["p1"])
        board.populate_deck("p1", {"cards": [{"guid": mon.guid, "count": 1}]})
        deck = board.find_player_area("p1", "deck")
        card_entity = deck.children[0]

        attrs = card_entity.attributes
        # Load-bearing: set code (bundle name) + collector number.
        self.assertEqual(attrs.get(AttrID.SET_CACHE_KEY.value), "BW1")
        self.assertEqual(attrs.get(AttrID.COLLECTOR_NUMBER.value), 79)
        self.assertEqual(attrs.get(AttrID.CARD_TYPE.value), CardType.POKEMON.value)
        # 10020 must be dropped so it doesn't hijack the texture key.
        self.assertNotIn(AttrID.EXPANSION.value, attrs)

        # Serialized form exposes them in the client's attribute-list shape.
        serialized = card_entity.serialize()
        names = {a["name"]: a["value"] for a in serialized["attributes"]}
        self.assertEqual(names.get(AttrID.SET_CACHE_KEY.value), "BW1")
        self.assertEqual(names.get(AttrID.COLLECTOR_NUMBER.value), 79)
        self.assertNotIn(AttrID.EXPANSION.value, names)

    async def test_serialized_state_dispatched_once_on_repeat_ready(self):
        """A repeat PlayerReady must not re-dispatch SerializedGameState (would crash the
        client loader with '...can't be loaded while a game is in progress!')."""
        client1 = MockClientHandler("player-1", "Ash")
        client2 = MockClientHandler("player-2", "Gary")

        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "player-1": {"client": client1, "deck": {"deckID": "d1", "deckName": "A", "cards": []}, "ready": True},
                "player-2": {"client": client2, "deck": {"deckID": "d2", "deckName": "B", "cards": []}, "ready": True},
            },
        }

        game_id = str(uuid.uuid4())
        session = GameSession(game_id, pairing)
        self.session_manager.active_sessions[game_id] = session

        handler1 = GameplayHandler(client1)
        handler2 = GameplayHandler(client2)

        # Both players ready -> dispatch happens exactly once.
        await handler1.handle_player_ready({}, request_id=1, flags=WargFlags.CLEAR)
        await handler2.handle_player_ready({}, request_id=2, flags=WargFlags.CLEAR)
        await asyncio.sleep(0.01)

        def sgs_count(client):
            return sum(
                1 for p in client.sent_packets
                if p.get("messageName") == "SequenceMessage"
                and isinstance(p.get("msg"), dict)
                and p["msg"].get("name") == "SerializedGameState"
            )

        self.assertEqual(sgs_count(client1), 1)
        self.assertEqual(sgs_count(client2), 1)

        # A duplicate PlayerReady (e.g. scene transition / reconnect) must NOT re-dispatch.
        await handler2.handle_player_ready({}, request_id=3, flags=WargFlags.CLEAR)
        await handler1.handle_player_ready({}, request_id=4, flags=WargFlags.CLEAR)
        await asyncio.sleep(0.01)

        self.assertEqual(sgs_count(client1), 1, "SerializedGameState re-dispatched on repeat PlayerReady")
        self.assertEqual(sgs_count(client2), 1, "SerializedGameState re-dispatched on repeat PlayerReady")

    async def test_deckbox_extras_empty_forces_twotone(self):
        """The deckbox game-extras must be empty so the client renders the
        dependency-free TwoTone box. A GUID/image name routes through the (currently
        broken) cosmetic-bundle texture path and shows a white box. See Q.S:60,70."""
        from spirit.game.session.game_session import GameOptions

        options = GameOptions()
        options.add_player(
            player_id="player-1",
            name="Ash",
            avatar_items=[],
            sleeve_id="sleeve-guid",
            coin_id="coin-guid",
            deckbox_id="e129b0d3-b934-4fbd-b021-545106c75694",
        )
        opts = options.to_dict()

        # Both deckbox keys must be present AND empty (empty image -> TwoTone;
        # empty box -> client skips the GUID/archetype -> white-box branch).
        self.assertEqual(opts["gameExtrasDeckBox_player-1"], "")
        self.assertEqual(opts["gameExtrasDeckImage_player-1"], "")

        # Other cosmetics are unaffected.
        self.assertEqual(opts["gameExtrasCoin_player-1"], "coin-guid")
        self.assertEqual(opts["gameExtrasSleeve_player-1"], "sleeve-guid")

    async def test_get_avatar_deck_fallback(self):
        client = MockClientHandler("player-1", "Ash")
        handler = DataSyncHandler(client)

        # Verify that get_avatar_decks_data returns empty originally
        self.assertEqual(len(client.player.avatar_decks), 0)

        # Call handle_get_avatar_deck_list
        await handler.handle_get_avatar_deck_list({}, request_id=1, flags=WargFlags.CLEAR)

        # Client should receive default avatar deck containing mock items
        self.assertEqual(len(client.sent_packets), 1)
        res = client.sent_packets[0]
        
        self.assertEqual(res["messageName"], OutboundMsg.AVATAR_DECK_LIST.value)
        self.assertEqual(len(res["decks"]), 1)
        
        deck = res["decks"][0]
        self.assertEqual(deck["deckName"], "Default Avatar")
        self.assertEqual(len(deck["piles"]["AvatarItems"]), 16)

    async def test_player_entity_gx_vstar_attribute_attachment(self):
        """Verifies that decks containing GX or VSTAR cards correctly flag physical playmat tokens on PlayerEntity."""
        from spirit.game.models.board import BoardState
        from spirit.game.attributes import PlayerAttrID
        from spirit.game.models.card import Card
        from spirit.game.scripts.cards import loader as card_loader

        # 1. Register a mock GX card into global loader cache
        mock_gx_card = Card(
            guid="mock-gx-card-guid-12345",
            key="CUSTOM",
            display_name="Mewtwo-GX",
            searchable_by=["Mewtwo-GX", "GX"]
        )
        card_loader.cards_by_guid[mock_gx_card.guid] = mock_gx_card

        # 2. Setup board state and populate with GX + VSTAR deck
        board = BoardState("game-123", ["player-ash"])
        
        # This deck has 1 Alolan Vulpix VSTAR and 1 Mock Mewtwo-GX
        deck_data = {
            "deckID": "deck-vstar",
            "deckName": "Power Deck",
            "cards": [
                {"guid": "040f2a64-dffa-52b3-8248-30a1faacf403", "count": 1}, # Alolan Vulpix VSTAR
                {"guid": "mock-gx-card-guid-12345", "count": 1} # Mock Mewtwo-GX
            ]
        }

        # Populate deck and trigger dynamic scanning
        board.populate_deck("player-ash", deck_data)

        # 3. Locate PlayerEntity and verify attributes are attached correctly
        player_entity = board.find_player_entity("player-ash")

        self.assertIsNotNone(player_entity)
        self.assertTrue(player_entity.get_attribute(PlayerAttrID.HAS_GX_TOKEN))
        self.assertTrue(player_entity.get_attribute(PlayerAttrID.HAS_VSTAR_TOKEN))

        # 4. The attributes alone never show the markers: the client's
        # MatchFound handler SetActive()s the playmat token objects only when
        # GameOptions["Tokens"] contains "GXToken"/"VSTARToken" (F.w decoded).
        client1 = MockClientHandler("player-1", "Ash")
        client2 = MockClientHandler("player-2", "Gary")
        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "player-1": {"client": client1, "deck": deck_data, "ready": True},
                "player-2": {"client": client2, "deck": {"deckID": "d2", "deckName": "Plain", "cards": []}, "ready": True},
            },
        }
        session = GameSession(str(uuid.uuid4()), pairing)
        await session.start()

        match_found = next(
            p for p in client1.sent_packets
            if p["messageName"] == OutboundMsg.MATCH_FOUND.value
        )
        tokens = match_found["gameOptions"].get("Tokens", "")
        self.assertIn("GXToken", tokens)
        self.assertIn("VSTARToken", tokens)
        # showPlayerUpsetNUX float.Parses eloRating_<id> unguarded per player.
        for pid in ("player-1", "player-2"):
            float(match_found["gameOptions"][f"eloRating_{pid}"])
        # SerializedGameState mirrors the same options for reconnects.
        self.assertIn("VSTARToken", session.board_state.game_options.get("Tokens", ""))

        # A match with no GX/VSTAR cards must not emit the key at all.
        plain_pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "player-1": {"client": MockClientHandler("player-1", "Ash"), "deck": {"deckID": "d3", "deckName": "Plain", "cards": []}, "ready": True},
                "player-2": {"client": MockClientHandler("player-2", "Gary"), "deck": {"deckID": "d4", "deckName": "Plain", "cards": []}, "ready": True},
            },
        }
        plain_session = GameSession(str(uuid.uuid4()), plain_pairing)
        await plain_session.start()
        self.assertNotIn("Tokens", plain_session.board_state.game_options)


    async def test_game_chat(self):
        # 1. Setup mock clients and deck
        client1 = MockClientHandler("player-1", "Ash")
        client2 = MockClientHandler("player-2", "Gary")
        
        deck1 = {"deckID": "deck-1", "deckName": "Charizard", "cards": []}
        deck2 = {"deckID": "deck-2", "deckName": "Blastoise", "cards": []}

        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "player-1": {"client": client1, "deck": deck1, "ready": True},
                "player-2": {"client": client2, "deck": deck2, "ready": True}
            }
        }

        # 2. Spawn GameSession
        game_id = str(uuid.uuid4())
        session = GameSession(game_id, pairing)
        self.session_manager.active_sessions[game_id] = session

        # 3. Handle GameChat from player 1
        handler1 = GameplayHandler(client1)
        chat_message = {
            "gameID": game_id,
            "message": "Hello Gary!"
        }
        await handler1.handle_game_chat(chat_message, request_id=1, flags=0)
        
        # Give event loop time to broadcast
        await asyncio.sleep(0.01)
        
        # Verify both players received NotifyGameChat
        self.assertEqual(len(client1.sent_packets), 1)
        self.assertEqual(len(client2.sent_packets), 1)
        
        res1 = client1.sent_packets[0]
        self.assertEqual(res1["messageName"], OutboundMsg.NOTIFY_GAME_CHAT.value)
        self.assertEqual(res1["gameID"], game_id)
        self.assertEqual(res1["message"], "Hello Gary!")
        self.assertEqual(res1["userInfo"]["accountID"], "player-1")
        self.assertEqual(res1["userInfo"]["displayName"], "Ash")


class TestEndGamePayload(unittest.IsolatedAsyncioTestCase):
    """GameCompletedMessage wire contract (EOG summary dialog requirements)."""

    def _make_session(self):
        self.client1 = MockClientHandler("eog-p1", "Ash")
        self.client2 = MockClientHandler("eog-p2", "Gary")
        pairing = {
            "is_solo": False,
            "format": "Standard",
            "players": {
                "eog-p1": {"client": self.client1, "deck": {"deckID": "d1", "deckName": "A", "cards": []}, "ready": True},
                "eog-p2": {"client": self.client2, "deck": {"deckID": "d2", "deckName": "B", "cards": []}, "ready": True},
            },
        }
        return GameSession(str(uuid.uuid4()), pairing)

    async def test_knockout_resets_hp_to_printed_max(self):
        from spirit.game.attributes import AttrID
        from spirit.game.data_utils import PokemonCardDef
        from spirit.game.models.board import create_card_entity
        from spirit.game.models.card import Card
        from spirit.game.session.effects import EffectContext

        session = self._make_session()
        card_def = PokemonCardDef(
            guid="00000000-0000-0000-0000-0000000ba001",
            key="BW1", name="com.test.pokemon.KOTarget.Name",
            collector_number=990, set_code="BW1", rarity=1,
            hp=90, elements=[],
        )
        d = card_def.to_archetype_dict()
        pokemon = create_card_entity(
            Card(d["guid"], d["key"], d["attributes"]), owning_player_id="eog-p2"
        )
        # Benched (no promotion prompt) and damaged to 0.
        bench = session.board_state.find_player_area("eog-p2", "bench")
        session.board_state.add_card_to_area(pokemon, bench)
        pokemon.set_attribute(AttrID.HP, 0)

        ctx = EffectContext(session, "eog-p1", pokemon, None)
        ctx.knockouts.append(pokemon)
        await session.resolve_knockouts(ctx)

        discard = session.board_state.find_player_area("eog-p2", "discard")
        self.assertIn(pokemon, discard.children)
        # No damage counters in the discard: HP back at the printed max,
        # both server-side and in the Knockout bracket's AttributeModified.
        self.assertEqual(pokemon.get_attribute(AttrID.HP), 90)
        attr_msgs = [
            pkt["msg"]["value"] for pkt in self.client2.sent_packets
            if (pkt.get("msg") or {}).get("name") == "AttributeModified"
            and pkt["msg"]["value"]["entityID"] == pokemon.entity_id
        ]
        self.assertTrue(attr_msgs)
        self.assertEqual(attr_msgs[-1]["attribute"]["value"], 90)
        self.assertEqual(attr_msgs[-1]["attribute"]["originalValue"], 90)

    async def test_wake_up_bracket_carries_target_data_effect(self):
        from unittest.mock import patch
        from spirit.game.attributes import AttrID
        from spirit.game.data_utils import PokemonCardDef
        from spirit.game.models.board import create_card_entity
        from spirit.game.models.card import Card

        session = self._make_session()
        card_def = PokemonCardDef(
            guid="00000000-0000-0000-0000-0000000ba002",
            key="BW1", name="com.test.pokemon.Sleeper.Name",
            collector_number=991, set_code="BW1", rarity=1,
            hp=150, elements=[],
        )
        d = card_def.to_archetype_dict()
        pokemon = create_card_entity(
            Card(d["guid"], d["key"], d["attributes"]), owning_player_id="eog-p1"
        )
        active = session.board_state.find_player_area("eog-p1", "activePokemonArea")
        session.board_state.add_card_to_area(pokemon, active)
        pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Asleep"])
        session.sleep_checkup_coins[pokemon.entity_id] = 2

        async def instant(_):
            return None

        with patch("spirit.game.session.game_session.random.choice", return_value=0), \
             patch("spirit.game.session.game_session.asyncio.sleep", new=instant):
            await session._run_pokemon_checkup()

        self.assertEqual(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        msgs = [pkt["msg"] for pkt in self.client1.sent_packets if pkt.get("msg")]
        starts = [m for m in msgs if m["name"] == "StartSequence"
                  and m["value"]["name"] == "RemoveSpecialCondition"]
        self.assertTrue(starts)
        # The executor's ctor (M.t) indexes the bracket's data effects with
        # "Target" -- it must ride the bracket before the condition attr.
        idx = msgs.index(starts[0])
        data_effect = msgs[idx + 1]
        self.assertEqual(data_effect["name"], "EntityIDDataEffect")
        self.assertEqual(data_effect["value"]["key"], "Target")
        self.assertEqual(data_effect["value"]["value"], pokemon.entity_id)
        self.assertEqual(msgs[idx + 2]["name"], "AttributeModified")
        self.assertEqual(msgs[idx + 2]["value"]["attribute"]["value"], [])

    @staticmethod
    def _completed_msg(client):
        for pkt in client.sent_packets:
            msg = pkt.get("msg") or {}
            if msg.get("name") == OutboundMsg.GAME_COMPLETED_MESSAGE.value:
                return msg["value"]
        return None

    async def test_game_completed_message_per_viewer(self):
        from spirit.game.session.game_session import GameOver
        from spirit.database.player_data import COINS_PER_WIN, COINS_PER_LOSS

        session = self._make_session()
        session.stat_add("eog-p1", "damagedealt", 120)
        session.stat_max("eog-p1", "biggestattack", 220)
        session.stat_add("eog-p1", "headsflipped", 3)

        class FakeAttacker:
            archetype_id = "00000000-0000-0000-0000-00000000ba99"

            @staticmethod
            def get_attribute(_attr):
                return {"id": "com.test.pokemon.Mvp.Name"}

        session.credit_card_damage("eog-p1", FakeAttacker, 90)
        session.credit_card_damage("eog-p1", FakeAttacker, 130)

        with self.assertRaises(GameOver):
            await session.end_game("eog-p1", "Took all Prize cards")

        winner = self._completed_msg(self.client1)
        loser = self._completed_msg(self.client2)
        self.assertIsNotNone(winner)
        self.assertIsNotNone(loser)

        # GameResult is REQUIRED: the summary dialog indexes it unguarded.
        self.assertEqual(winner["additionalParameters"]["GameResult"], {"id": "Win"})
        self.assertEqual(loser["additionalParameters"]["GameResult"], {"id": "Loss"})

        # Per-viewer stats swap sides between the two messages.
        self.assertEqual(
            winner["additionalParameters"]["me_playmat.endgame.stat.biggestattack"],
            {"id": "220"},
        )
        self.assertEqual(
            loser["additionalParameters"]["opp_playmat.endgame.stat.biggestattack"],
            {"id": "220"},
        )

        # Coins at the configured win/loss rates, mirrored in the rewardList.
        self.assertEqual(winner["coins"], COINS_PER_WIN)
        self.assertEqual(loser["coins"], COINS_PER_LOSS)
        reward = winner["rewardList"][0]
        self.assertEqual(reward["rewardType"], "Tokens")
        self.assertEqual(reward["rewardAmount"], COINS_PER_WIN)
        # rewardDescription must be non-null: RewardsList derefs its ID.
        self.assertTrue(reward["rewardDescription"]["id"])

        self.assertIn("GameDuration", winner["additionalParameters"])
        self.assertEqual(winner["winner"], "eog-p1")
        self.assertEqual(winner["loser"], "eog-p2")

        # Summary-page header tiles are per-viewer plain totals.
        self.assertEqual(winner["additionalParameters"]["Damagedealt"], {"id": "120"})
        self.assertEqual(winner["additionalParameters"]["Headsflipped"], {"id": "3"})
        self.assertEqual(loser["additionalParameters"]["Damagedealt"], {"id": "0"})

        # MVP card = the viewer-side card with the most credited damage.
        self.assertEqual(
            winner["additionalParameters"]["me_$playmat.endgame.stat.mvp.archetypeid$"],
            {"id": "00000000-0000-0000-0000-00000000ba99"},
        )
        self.assertEqual(
            winner["additionalParameters"]["me_playmat.endgame.stat.mvp"],
            {"id": "com.test.pokemon.Mvp.Name"},
        )
        self.assertEqual(
            loser["additionalParameters"]["opp_$playmat.endgame.stat.mvp.archetypeid$"],
            {"id": "00000000-0000-0000-0000-00000000ba99"},
        )
        # A player who dealt no damage gets no MVP keys (client guards them).
        self.assertNotIn(
            "me_$playmat.endgame.stat.mvp.archetypeid$",
            loser["additionalParameters"],
        )

    async def test_concede_completes_the_game_for_both_players(self):
        import asyncio
        from spirit.game.session.constants import GamePhase
        from spirit.game.session.game_session import GameOver

        session = self._make_session()
        # Simulate the gameplay task blocked on the opponent's reply.
        waiter = session.players["eog-p1"]
        waiter.pending_choice_future = asyncio.get_running_loop().create_future()

        await session.concede("eog-p2")

        winner = self._completed_msg(self.client1)
        loser = self._completed_msg(self.client2)
        self.assertIsNotNone(winner)
        self.assertIsNotNone(loser)
        self.assertEqual(winner["winner"], "eog-p1")
        self.assertEqual(winner["additionalParameters"]["GameResult"], {"id": "Win"})
        self.assertEqual(loser["additionalParameters"]["GameResult"], {"id": "Loss"})
        self.assertIn("conceded", winner["endOfGameText"]["id"])

        # The pending wait unwinds the gameplay loop with GameOver.
        self.assertEqual(session.game_phase, GamePhase.GAME_OVER)
        with self.assertRaises(GameOver):
            waiter.pending_choice_future.result()
        # Any later prompt raises instead of blocking forever.
        with self.assertRaises(GameOver):
            await session.prompt_selection_message(waiter, "Noop", {})
        # Conceding an already-decided game is a no-op.
        before = len(self.client1.sent_packets)
        await session.concede("eog-p1")
        self.assertEqual(len(self.client1.sent_packets), before)


if __name__ == "__main__":
    unittest.main()
