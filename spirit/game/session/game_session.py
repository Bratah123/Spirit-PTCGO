import logging
import asyncio
import random
import time
import uuid
from typing import Dict, Any, List, Optional, Sequence, Tuple, Union
from .player_abstract import GamePlayer
from .network_player import NetworkPlayer
from spirit.game.account_attributes import build_account_attributes
from .ai_player import AIPlayer
from .constants import (
    GamePhase,
    SelectionKind,
    STARTING_HAND_SIZE,
    MOVE_ANIM_DURATION_MS,
    SHUFFLE_ANIM_SECONDS,
    BENCH_CAPACITY,
    PRIZE_COUNT,
    MAX_SELECTION_RETRIES,
    MAX_TURNS,
    MAX_ACTIONS_PER_TURN,
    TURN_OFFER_LENGTH_MS,
    TARGET_TYPE_MAIN_TURN,
    EMPTY_SEQUENCE_ID,
    GAME_OPTION_TOKENS_KEY,
    GAME_OPTION_RECONNECTING_KEY,
    GAME_OPTION_RECONNECTING_VALUE,
    RECONNECT_GRACE_SECONDS,
    TOKEN_GX,
    TOKEN_VSTAR,
    TARGET_TYPE_ACTIVE,
    TARGET_TYPE_BENCH,
    PROMPT_SORT_COIN,
    PROMPT_SORT_GO_FIRST,
    PROMPT_SORT_MULLIGAN,
    PROMPT_HEADS,
    PROMPT_TAILS,
    PROMPT_YES,
    PROMPT_NO,
    PROMPT_CHOOSE_ACTIVE,
    PROMPT_CHOOSE_BENCH,
    PROMPT_WAIT_OPPONENT_ACTIVE,
    PROMPT_WAIT_OPPONENT_SETUP,
    PROMPT_WAIT_OPPONENT_DECISION,
    PROMPT_MULLIGAN_EXTRA_DRAW,
    PROMPT_TAKE_PRIZE,
    PROMPT_CHOOSE_NEW_ACTIVE,
    PROMPT_REVEAL_BASIC_FROM_PRIZE,
    TEXT_COIN_TOSS_RESULT,
    TEXT_HEADS_RESULT,
    TEXT_TAILS_RESULT,
    TEXT_MULLIGAN_REVEAL_PROMPT,
    TEXT_SLEEP_CHECK,
    TEXT_WOKE_UP,
    TEXT_STILL_ASLEEP,
    TEXT_BURN_CHECK,
    TEXT_BURN_CURED,
    TEXT_STILL_BURNED,
    TEXT_CONFUSION_CHECK,
    TEXT_CONFUSION_PROCEEDS,
    TEXT_CONFUSION_HURT,
)
from spirit.network.message_names import OutboundMsg
from spirit.game.attributes import (
    AttrID,
    CLIENT_SPECIAL_CONDITION_NAMES,
    GameSequence,
    PlayerAttrID,
    SpecialConditions,
    TrainerType,
)
from spirit.game.data_utils import (
    ABILITIES_BY_ID, Ability, Activations, Triggers, def_for, prize_value,
    subtypes_for, unimplemented,
)
from spirit.database.player_data import COINS_PER_WIN, COINS_PER_LOSS, grant_coins
from spirit.database.versus_data import award_match_points, get_progress
from spirit.database.async_utils import run_db
from spirit.game.models.board import BoardEntity, BoardState, EnergyEntity, PokemonEntity
from .effects import (
    EffectContext,
    resolve_activated_ability,
    resolve_attack,
    resolve_energy_attach_cost,
    resolve_energy_on_attach,
    resolve_trainer_effect,
    resolve_triggered_ability,
)
from .passives import (
    ability_locked, active_passives, burn_recovery_blocked,
    effective_bench_capacity, effective_max_hp, effective_retreat_cost,
    tool_slots_free,
)
from .legal_actions import (
    ACTION_ATTACH_TOOL,
    ACTION_EVOLVE,
    ACTION_PLAY_ENERGY,
    ACTION_PLAY_POKEMON,
    ACTION_PLAY_STADIUM,
    ACTION_RETREAT,
    ACTION_USE_ABILITY,
    ACTION_USE_ATTACK,
    ACTION_USE_TRAINER,
    TurnState,
    compute_legal_actions,
    copy_attack_choice_node,
    energy_provided_count,
)


# Suffixes of the client's playmat.endgame.stat.* rows on the EOG summary page.
EOG_STAT_KEYS = (
    "biggestattack", "damagedealt", "prizecardstaken", "damagehealed",
    "energyplayed", "trainersplayed", "cardsdrawn", "headsflipped",
    "tailsflipped",
)

# Recursion cap on ON_KNOCKED_OUT triggers cascading into further knockouts.
_MAX_KO_TRIGGER_DEPTH = 4

# Ceiling on an AIPlayer prompt wait (simulated answers land in ~1.5s); a
# prompt no simulation answers must never hang the gameplay task.
AI_PROMPT_GRACE_SECONDS = 15.0


class GameOver(Exception):
    """Raised once the game has been decided; unwinds the gameplay sequence."""


class NestedSequence:
    """A child Start/Stop bracket embedded inside a parent game sequence.

    The client's SequenceParser keeps a stack of in-progress sequences: a
    StartSequence (exempt from the envelope sequence-ID check) pushes a child,
    its inner messages must ride the CHILD's sequenceID, and its StopSequence
    folds the child into the parent as a single sequence command. This is how
    GroupedMove batches EntityMoved commands so they animate together instead
    of one-by-one (e.g. a mulliganed hand returning to the deck at once).
    """

    def __init__(self, name, messages: List[Dict[str, Any]]):
        self.name: str = getattr(name, "value", name)
        self.messages: List[Dict[str, Any]] = messages


class GameOptions:
    """
    Represents the gameplay options and match metadata sent to the client
    in MatchFound and SerializedGameState packets.
    
    Includes configuration for turn timers, board themes, and player-specific
    identities/cosmetics (avatars, sleeves, coins, deckboxes).
    """
    def __init__(self, turn_time: str = "45", bench_time: str = "15", theme: str = "ForestPlaymat"):
        self.turn_time: str = turn_time
        self.bench_time: str = bench_time
        self.theme: str = theme
        
        # Player-specific cosmetics and profiles: { player_id: dict }
        self._player_options: Dict[str, Dict[str, str]] = {}

    def add_player(
        self,
        player_id: str,
        name: str,
        avatar_items: List[str],
        sleeve_id: str,
        coin_id: str,
        deckbox_id: str
    ):
        """Registers a player's screen name and selected deck cosmetics for the match."""
        self._player_options[player_id] = {
            f"avatarProfile_name_{player_id}": name,
            f"avatarProfile_{player_id}": ",".join(avatar_items),
            f"gameExtrasSleeve_{player_id}": sleeve_id,
            f"gameExtrasCoin_{player_id}": coin_id,
            # Empty deckbox extras force the client's dependency-free TwoTone box
            # (see the DeckBoxType note above). Leaving these as the GUID/image name
            # routes through the broken cosmetic-bundle texture path -> white box.
            f"gameExtrasDeckBox_{player_id}": "",
            f"gameExtrasDeckImage_{player_id}": "",
        }

    def to_dict(self) -> Dict[str, str]:
        """Serializes the game options into the dictionary structure expected by the client."""
        serialized = {
            "turnTime": self.turn_time,
            "benchTime": self.bench_time,
            "theme": self.theme,
        }
        for player_id, options in self._player_options.items():
            serialized.update(options)
        return serialized


class GameSession:
    # Pacing sleeps for client choreography; headless harnesses flip this off.
    choreography_pauses: bool = True

    def __init__(self, game_id: str, pairing: Dict[str, Any]):
        self.game_id: str = game_id
        self.pairing: Dict[str, Any] = pairing
        self.is_solo: bool = pairing.get("is_solo", False)
        
        self.players: Dict[str, GamePlayer] = {}
        self._initialize_players()
        self.ready_players: set = set()
        # account_ids that have reconnected and are awaiting their PlayerReady so
        # we re-send SerializedGameState (+ replay their pending offer) to them.
        self._reconnecting: set = set()
        # account_ids with an OUTSTANDING disconnect the opponent was told about
        # (a "Disconnection!" dialog is showing on their screen). Pairs 1:1 with a
        # later PlayerReconnected; gates both so eviction races / duplicate
        # ReconnectToGame never orphan a stuck dialog or double the popup.
        self._disconnected: set = set()
        # detached account_id -> grace-window timer task (awards the win on expiry).
        self._grace_tasks: Dict[str, asyncio.Task] = {}

        self._state_dispatched: bool = False
        self.gameplay_task: Optional[asyncio.Task] = None
        # Fire-and-forget tasks (AI simulations) kept referenced until done
        self._background_tasks: set = set()

        self.game_phase: str = GamePhase.INIT
        self.coin_flip_caller_id: Optional[str] = None
        self.coin_flip_winner_id: Optional[str] = None
        # The player who takes the first turn, decided by the go-first choice.
        self.first_player_id: Optional[str] = None
        # Turn-loop bookkeeping (turn number, once-per-turn flags, entry turns).
        self.turn_state = TurnState()
        # entity_id -> stat-modifier PiPs (attr 200370) applied this turn, so
        # they clear when the turn ends (Power Tablet's damage boost).
        self._turn_visualizations: Dict[str, List[Dict[str, Any]]] = {}
        # entity_id -> coins flipped at Pokemon Checkup while Asleep (waking
        # needs ALL heads; Snorlax's Thumping Snore sets 2).
        self.sleep_checkup_coins: Dict[str, int] = {}
        # entity_id -> damage-counter multiplier while Poisoned (10 * count
        # dealt each checkup; default 1).
        self.poison_counters: Dict[str, int] = {}
        # entity_id -> turn number Paralyzed was applied (cures after the
        # checkup following the OWNER's next turn, not the same turn).
        self.paralyzed_since: Dict[str, int] = {}
        # Per-player EOG summary counters (playmat.endgame.stat.* suffixes).
        self.game_stats: Dict[str, Dict[str, int]] = {
            pid: {} for pid in pairing["players"].keys()
        }
        # Per-player damage credited per card for the EOG MVP pick:
        # {player_id: {archetype_guid: [total_damage, name_loc_key]}}
        self.mvp_damage: Dict[str, Dict[str, list]] = {
            pid: {} for pid in pairing["players"].keys()
        }
        self.match_started_at: float = time.time()
        # Set by declare_winner: {"winner", "loser", "reason"} once decided.
        self.game_result: Optional[Dict[str, str]] = None
        # Per-player selection offer counters. The pregame coin flip uses
        # counters 1-2, so later offers continue from 3.
        self._selection_counters: Dict[str, int] = {
            pid: 2 for pid in pairing["players"].keys()
        }

        # Initialize the virtual OOP Board State and populate player decks
        self.board_state = BoardState(self.game_id, list(self.players.keys()))
        self.board_state.turn_state = self.turn_state
        for player_id, player in self.players.items():
            self.board_state.populate_deck(player_id, player.active_deck)
            # Dynamically update the PlayerEntity NAME attribute to the player's screen name
            player_entity = self.board_state.find_player_entity(player_id)
            if player_entity:
                player_entity.set_attribute(AttrID.NAME, player.screen_name)

    def _spawn(self, coro) -> asyncio.Task:
        """Creates a tracked background task that self-removes when done."""
        task = asyncio.create_task(coro)
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)
        return task

    async def choreo_pause(self, seconds: float):
        """Sleep that paces client animations; no-op when pauses are disabled."""
        if self.choreography_pauses:
            await asyncio.sleep(seconds)

    def cleanup(self):
        """Cancels any pending futures, tasks, and cleans up references."""
        logging.info(f"[Session {self.game_id}] Cleaning up session.")
        # 1. Cancel player pending choices
        for player in self.players.values():
            fut = getattr(player, "pending_choice_future", None)
            if fut is not None:
                if not fut.done():
                    fut.cancel()

        # 2. Cancel background AI-simulation tasks
        for task in list(self._background_tasks):
            if not task.done():
                task.cancel()
        self._background_tasks.clear()

        # 3. Cancel gameplay task if any (unless we're running inside it)
        try:
            current = asyncio.current_task()
        except RuntimeError:
            current = None
        task = self.gameplay_task
        if task is not None and not task.done() and task is not current:
            task.cancel()
            logging.info(f"[Session {self.game_id}] Cancelled active gameplay sequence task.")

    def _initialize_players(self):
        """Wraps physical connections or AI players under the uniform GamePlayer abstraction."""
        for account_id, info in self.pairing["players"].items():
            client = info["client"]
            deck = info["deck"]
            
            if client is None:
                # Mock AI Bot
                logging.info(f"[Session {self.game_id}] Initializing AI Bot as opponent.")
                self.players[account_id] = AIPlayer(
                    bot_id=account_id,
                    bot_name="Spirit AI Bot",
                    deck_data=deck,
                    session=self
                )
            else:
                # Real TCP player
                logging.info(f"[Session {self.game_id}] Initializing NetworkPlayer for {client.player.username}.")
                self.players[account_id] = NetworkPlayer(
                    client_handler=client,
                    deck_data=deck
                )

    def _player_rating(self, player) -> int:
        """Ladder rating for the upset-NUX comparison: 1000 + all-time versus points."""
        account_id = getattr(player, "account_id", None)
        if not isinstance(player, NetworkPlayer) or not account_id:
            return 1000
        _, all_time = get_progress(account_id, "")
        return 1000 + all_time

    def _build_game_options(self) -> Dict[str, Any]:
        """Builds the full gameOptions dict (cosmetics, tokens, elo, tournament ID)."""
        options = GameOptions(turn_time="45", bench_time="15", theme="ForestPlaymat")

        for player_id, player in self.players.items():
            # Add player metadata and cosmetics to options
            options.add_player(
                player_id=player_id,
                name=player.screen_name,
                avatar_items=player.avatar_items,
                sleeve_id=player.sleeve_id,
                coin_id=player.coin_id,
                deckbox_id=player.deckbox_id
            )

        game_options_dict = options.to_dict()

        tokens = []
        for player_id in self.players:
            player_entity = self.board_state.find_player_entity(player_id)
            if not player_entity:
                continue
            if player_entity.get_attribute(PlayerAttrID.HAS_GX_TOKEN) and TOKEN_GX not in tokens:
                tokens.append(TOKEN_GX)
            if player_entity.get_attribute(PlayerAttrID.HAS_VSTAR_TOKEN) and TOKEN_VSTAR not in tokens:
                tokens.append(TOKEN_VSTAR)
        if tokens:
            game_options_dict[GAME_OPTION_TOKENS_KEY] = ",".join(tokens)

        # showPlayerUpsetNUX (G.D) float.Parses gameOptions["eloRating_<id>"]
        # unguarded for every match participant — the key must exist.
        for player_id, player in self.players.items():
            game_options_dict[f"eloRating_{player_id}"] = str(
                self._player_rating(player)
            )

        # Legacy bracket matches: the client's TournamentManager reads this key
        legacy_ctx = self.pairing.get("legacy_tournament")
        if legacy_ctx:
            game_options_dict["TournamentID"] = str(legacy_ctx["tournament_id"])

        return game_options_dict

    def _build_match_found_payload(self, reconnecting: bool = False) -> Dict[str, Any]:
        """Builds the MatchFound payload; shared by initial start and reconnect.

        Reads the full gameOptions persisted on board_state (set by start()); the
        Reconnecting flag makes the client rebuild the match model from gameOptions
        and jump straight to the playmat scene.
        """
        # board_state.game_options starts as a bare {"theme": ...}; start() replaces
        # it with the full cosmetics/elo dict before this is ever called. Rebuild
        # defensively only if that hasn't happened yet (no per-player elo keys).
        game_options_dict = self.board_state.game_options
        if not any(k.startswith("eloRating_") for k in game_options_dict):
            game_options_dict = self._build_game_options()
            self.board_state.game_options = game_options_dict
        if reconnecting:
            # Flag on a copy so it never leaks into the persistent SGS gameOptions.
            game_options_dict = {
                **game_options_dict,
                GAME_OPTION_RECONNECTING_KEY: GAME_OPTION_RECONNECTING_VALUE,
            }
        return {
            "gameID": self.game_id,
            "players": list(self.players.keys()),
            "gameOptions": game_options_dict,
        }

    async def start(self):
        """Fires the MatchFound packet to notify clients of the finalized match and start transition."""
        logging.info(f"[Session {self.game_id}] Starting GameSession.")

        # Build the full gameOptions (cosmetics/tokens/elo) once and persist it so
        # both MatchFound and SerializedGameState carry player avatars/cosmetics.
        self.board_state.game_options = self._build_game_options()

        # Broadcast MatchFound packet to all active players
        await self.broadcast_packet(
            OutboundMsg.MATCH_FOUND.value, self._build_match_found_payload()
        )

    def _unique_recipients(self, players=None):
        """Yields (player_id, player) once per distinct client handler (AI players always yielded)."""
        pid_by_obj = {id(p): pid for pid, p in self.players.items()}
        candidates = self.players.values() if players is None else players
        seen_clients = set()
        for player in candidates:
            if isinstance(player, NetworkPlayer) and player.client_handler:
                key = id(player.client_handler)
                if key in seen_clients:
                    continue
                seen_clients.add(key)
            yield pid_by_obj.get(id(player)), player

    async def broadcast_packet(self, name: str, value: Dict[str, Any], flags: int = 0):
        """Utility to send a packet to all network-connected players in the match, ensuring no duplicate transmission to any single client handler."""
        tasks = [player.send_packet(name, value, flags)
                 for _, player in self._unique_recipients()]
        if tasks:
            await asyncio.gather(*tasks)

    @staticmethod
    def _build_msg(name: str, value: Dict[str, Any]) -> Dict[str, Any]:
        """Builds the polymorphic {name, value} envelope for a nested game message."""
        return {"name": name, "value": value}

    def _sequence_envelope(self, sequence_id: str, msg: Dict[str, Any]) -> Dict[str, Any]:
        """Wraps a nested game message inside a SequenceMessage payload."""
        return {
            "sequenceID": sequence_id,
            "gameID": self.game_id,
            "msg": msg,
        }

    async def send_game_sequence(
        self,
        players: List[GamePlayer],
        name: str,
        inner_messages: Sequence[Union[Dict[str, Any], NestedSequence]],
    ):
        """Sends a COMPLETE Start/Stop sequence bracket to the given players.

        The client's SequenceParser only hands a sequence to the visual pump once
        its StopSequence arrives, so a bracket must never be left open while the
        server waits on player input -- nothing renders until it is closed.
        Sequence commands like OpponentPickingHeadsOrTails (M.Q) additionally
        no-op when the bracket contains zero inner messages, so callers must
        always provide at least one.
        """
        # Accept GameSequence enum members or raw strings.
        name = getattr(name, "value", name)
        sequence_id = str(uuid.uuid4())
        packets = [
            self._sequence_envelope(sequence_id, self._build_msg(
                OutboundMsg.START_SEQUENCE.value,
                {"gameID": self.game_id, "sequenceID": sequence_id, "name": name},
            )),
        ]
        for msg in inner_messages:
            if isinstance(msg, NestedSequence):
                packets.extend(self._nested_sequence_envelopes(msg))
            else:
                packets.append(self._sequence_envelope(sequence_id, msg))
        packets.append(
            self._sequence_envelope(sequence_id, self._build_msg(
                OutboundMsg.STOP_SEQUENCE.value,
                {"gameID": self.game_id, "sequenceID": sequence_id, "name": name},
            ))
        )
        for _, player in self._unique_recipients(players):
            for packet in packets:
                await player.send_packet(OutboundMsg.SEQUENCE_MESSAGE.value, packet)

    def _nested_sequence_envelopes(self, nested: NestedSequence) -> List[Dict[str, Any]]:
        """Builds the Start/inner/Stop envelope run for a child sequence.

        Every envelope rides the CHILD's sequenceID: the parser stacks the
        child on StartSequence and requires inner messages to match the
        innermost open sequence.
        """
        child_id = str(uuid.uuid4())
        return [
            self._sequence_envelope(child_id, self._build_msg(
                OutboundMsg.START_SEQUENCE.value,
                {"gameID": self.game_id, "sequenceID": child_id, "name": nested.name},
            )),
            *(self._sequence_envelope(child_id, msg) for msg in nested.messages),
            self._sequence_envelope(child_id, self._build_msg(
                OutboundMsg.STOP_SEQUENCE.value,
                {"gameID": self.game_id, "sequenceID": child_id, "name": nested.name},
            )),
        ]

    async def prompt_selection_message(
        self,
        player: GamePlayer,
        msg_name: str,
        value: Dict[str, Any],
        expected_counter: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Sends a SelectionMessage prompt and waits inline for the reply.

        The prompt rides a standalone SequenceMessage with the empty GUID so it
        executes exactly once (queued pump only). A bare top-level selection
        message is processed twice by the client -- synchronously in
        SessionProvider.Update and again by the Sequences pump -- causing a
        double Selection.BeginOffer.

        expected_counter guards against STALE replies: the client's drag-drop
        path can emit a duplicate response for an already-answered offer
        (l.F.dragEnded advances the root twice), which must not be allowed to
        resolve the NEXT offer. Replies echoing a different counter are
        discarded and the wait continues.
        """
        if self.game_phase == GamePhase.GAME_OVER:
            raise GameOver()
        envelope = self._sequence_envelope(
            EMPTY_SEQUENCE_ID, self._build_msg(msg_name, value)
        )
        loop = asyncio.get_running_loop()
        player.pending_choice_future = loop.create_future()
        player._pending_offer = (OutboundMsg.SEQUENCE_MESSAGE.value, envelope, 0)
        await player.send_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)
        try:
            while True:
                if isinstance(player, AIPlayer):
                    # AI prompts resolve only via simulated tasks (pregame coin
                    # flip); anything else must never hang the gameplay task.
                    try:
                        reply = await asyncio.wait_for(
                            player.pending_choice_future, AI_PROMPT_GRACE_SECONDS
                        )
                    except asyncio.TimeoutError:
                        logging.error(
                            f"[Session {self.game_id}] Prompt '{msg_name}' hit "
                            f"the wire for AI player {player.screen_name} with "
                            f"no auto-answer; returning a null selection."
                        )
                        return {"selection": None}
                else:
                    reply = await player.pending_choice_future
                reply_counter = reply.get("counter") if isinstance(reply, dict) else None
                if expected_counter is None or reply_counter in (None, expected_counter):
                    return reply
                logging.info(
                    f"[Session {self.game_id}] Ignoring stale selection reply "
                    f"(counter {reply_counter}, expected {expected_counter}): {reply}"
                )
                player.pending_choice_future = loop.create_future()
        finally:
            player.pending_choice_future = None
            player._pending_offer = None

    async def _send_pause_prompt(self, player: GamePlayer, prompt_text: str):
        """Shows the center-screen prompt override on one client.

        PauseOnPromptEffect (m.l) with doPause=false displays `prompt` in the
        middle of the playmat and hides the Next button for as long as it is
        up (NextButton checks OverrideShowPrompt). It stays until
        ClosePauseOnPromptEffect.
        """
        envelope = self._sequence_envelope(
            EMPTY_SEQUENCE_ID,
            self._build_msg(
                OutboundMsg.PAUSE_ON_PROMPT_EFFECT.value,
                {
                    "gameID": self.game_id,
                    "prompt": {"id": prompt_text},
                    "buttonText": None,
                    "doPause": False,
                },
            ),
        )
        await player.send_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)

    async def _send_close_pause_prompt(self, player: GamePlayer):
        """Clears the center-screen prompt override (harmless if none is up)."""
        envelope = self._sequence_envelope(
            EMPTY_SEQUENCE_ID,
            self._build_msg(
                OutboundMsg.CLOSE_PAUSE_ON_PROMPT_EFFECT.value,
                {"gameID": self.game_id},
            ),
        )
        await player.send_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)

    def _choice_offer_value(self, selecting_player_id: str, buttons: List[str]) -> Dict[str, Any]:
        """Builds a CustomChoiceOfferMessage value describing the opponent's pending choice.

        With a null sourceEntity the client-side command (D.x) is a pure no-op,
        but its presence inside an OpponentPickingHeadsOrTails /
        OpponentChoosingToGoFirst bracket satisfies the >=1-command requirement
        and -- because it is NOT the observer command (b.O) -- steers the coin
        dialog into the two-player "OpponentPicks..." animator states instead of
        the spectator-only "ObservePlayerXPicks..." chain.
        """
        return {
            "gameID": self.game_id,
            "selectingPlayer": selecting_player_id,
            "prompt": {"id": ""},
            "buttons": [{"id": button} for button in buttons],
            "offerLength": 30000,
            "sourceEntity": None,
            "selection": None,
            "correctChoice": None,
        }

    async def receive_player_action(self, account_id: str, action_data: Dict[str, Any]):
        """Handler for receiving target or action selection inputs from a player (network or AI)."""
        logging.info(f"[Session {self.game_id}] Received action from player {account_id}: {action_data}")
        
        # Resolve any active inline choice first
        player = self.players.get(account_id)
        if player and player.pending_choice_future and not player.pending_choice_future.done():
            player.pending_choice_future.set_result(action_data)
            return

        # TODO(bratah123): Feed selection into Game Engine rules to proceed turn sequence.
        pass

    async def mark_player_ready(self, account_id: str):
        """Marks a player as ready and broadcasts SerializedGameState once both players are ready."""
        logging.info(f"[Session {self.game_id}] Player {account_id} reported ready.")

        # Reconnect: this player's fresh playmat scene is up. Re-send state to
        # just them and replay any offer they owed a reply to. The gameplay task
        # kept running (or parked on their still-live future) throughout.
        if account_id in self._reconnecting:
            self._reconnecting.discard(account_id)
            await self._resend_state_to(account_id)
            return

        self.ready_players.add(account_id)

        if self._state_dispatched:
            return

        # Check if all network players are ready
        network_players_count = sum(1 for p in self.players.values() if isinstance(p, NetworkPlayer))
        if len(self.ready_players) >= network_players_count:
            self._state_dispatched = True
            logging.info(f"[Session {self.game_id}] All network players ready. Dispatched SerializedGameState.")
            await self.send_serialized_game_state()
            # Start the sequential gameplay sequence!
            self.gameplay_task = asyncio.create_task(self.run_gameplay_sequence())

    async def _notify_opponents_connection(self, subject_id: str, message_name: str,
                                           extra: Optional[Dict[str, Any]] = None):
        """Pushes a connection-status message about subject_id to the OTHER connected players."""
        # gameID is REQUIRED: GameQueueManager routes every GameMessage into a
        # per-game queue keyed by it (ContainsKey(null) crashes without it).
        payload = {"gameID": self.game_id, "accountID": subject_id, **(extra or {})}
        for pid, viewer in self.players.items():
            if pid == subject_id:
                continue
            if isinstance(viewer, NetworkPlayer) and viewer.connected:
                await viewer.send_packet(message_name, payload)

    async def on_player_disconnect(self, account_id: str):
        """Detaches a player's socket without ending the game; starts the grace timer.

        The gameplay task keeps running (or parks on the player's still-live
        selection future); their sends no-op until they reconnect.
        """
        player = self.players.get(account_id)
        if not isinstance(player, NetworkPlayer):
            return
        if self.game_phase == GamePhase.GAME_OVER:
            return
        # Detach + (re)arm grace ALWAYS (liveness), but the opponent-facing dialog
        # message is guarded: a 2nd PlayerDisconnected while one is still outstanding
        # stacks a 2nd "Disconnection!" popup the client can no longer dismiss (m.q
        # overwrites its single dialog reference, orphaning the first on-screen).
        already_notified = account_id in self._disconnected
        logging.info(
            f"[Session {self.game_id}] Player {account_id} disconnected — detaching "
            f"(grace {RECONNECT_GRACE_SECONDS}s, already_notified={already_notified})."
        )
        player.client_handler = None
        self._reconnecting.discard(account_id)
        existing = self._grace_tasks.pop(account_id, None)
        if existing is not None and not existing.done():
            existing.cancel()
        self._grace_tasks[account_id] = self._spawn(self._disconnect_grace(account_id))
        if already_notified:
            return
        self._disconnected.add(account_id)
        # PlayerDisconnected (m.q): shows the opponent the "disconnected, waiting Ns"
        # dialog and freezes the chess clock until PlayerReconnected.
        logging.info(f"[Session {self.game_id}] -> PlayerDisconnected to opponents of {account_id}.")
        await self._notify_opponents_connection(
            account_id, OutboundMsg.PLAYER_DISCONNECTED.value,
            {"waitTime": RECONNECT_GRACE_SECONDS * 1000},
        )

    async def _disconnect_grace(self, account_id: str):
        """Awards the game to the connected opponent if the player never returns."""
        try:
            await asyncio.sleep(RECONNECT_GRACE_SECONDS)
        except asyncio.CancelledError:
            return
        self._grace_tasks.pop(account_id, None)
        player = self.players.get(account_id)
        if (player is None or getattr(player, "connected", True)
                or self.game_phase == GamePhase.GAME_OVER):
            return
        logging.info(
            f"[Session {self.game_id}] Reconnect grace expired for {account_id}; "
            f"resolving game."
        )
        opponent_id = self._opponent_id(account_id)
        opponent = self.players.get(opponent_id)
        if isinstance(opponent, NetworkPlayer) and getattr(opponent, "connected", False):
            # Concede on the absent player's behalf: awards the opponent the win.
            await self.concede(account_id)
        else:
            # No connected human to award (both gone / AI opponent): tear down.
            from .manager import GameSessionManager
            GameSessionManager().remove_session(self.game_id)

    async def reconnect_player(self, client_handler, account_id: str):
        """Rebinds a reconnecting player's socket and drives them back onto the playmat.

        Sends MatchFound(Reconnecting); the client rebuilds the match model, loads
        the playmat scene, and sends PlayerReady -> mark_player_ready resync.
        """
        player = self.players.get(account_id)
        if not isinstance(player, NetworkPlayer):
            return
        logging.info(f"[Session {self.game_id}] Player {account_id} reconnecting.")
        grace = self._grace_tasks.pop(account_id, None)
        if grace is not None and not grace.done():
            grace.cancel()
        # Rebind the live socket (self-heal, like live_tournament.resolve_client).
        player.client_handler = client_handler
        self._reconnecting.add(account_id)
        await player.send_packet(
            OutboundMsg.MATCH_FOUND.value,
            self._build_match_found_payload(reconnecting=True),
        )

    async def _resend_state_to(self, account_id: str):
        """Re-sends the board snapshot + replays any pending offer to a reconnected player."""
        player = self.players.get(account_id)
        if not isinstance(player, NetworkPlayer) or not player.connected:
            return
        # Resync the board + replay the pending offer. Never let a serialization
        # error swallow the PlayerReconnected below — that would strand the
        # opponent's "Disconnection!" dialog on-screen forever.
        try:
            await self.send_serialized_game_state(only_player_id=account_id)
            offer = player._pending_offer
            if offer is not None:
                name, value, flags = offer
                await player.send_packet(name, value, flags)
                logging.info(
                    f"[Session {self.game_id}] Replayed pending offer to reconnected {account_id}."
                )
        except Exception as e:
            logging.exception(
                f"[Session {self.game_id}] Error resyncing state to reconnected {account_id}: {e}"
            )
        # PlayerReconnected (m.r): dismisses the opponent's wait dialog and restarts
        # the chess clock. Paired 1:1 with the outstanding disconnect — a duplicate
        # ReconnectToGame still resyncs the board above but must NOT fire a second
        # Reconnection popup, so only send it when a disconnect is actually pending.
        if account_id in self._disconnected:
            self._disconnected.discard(account_id)
            logging.info(f"[Session {self.game_id}] -> PlayerReconnected to opponents of {account_id}.")
            await self._notify_opponents_connection(
                account_id, OutboundMsg.PLAYER_RECONNECTED.value,
            )
        else:
            logging.info(
                f"[Session {self.game_id}] Reconnect resync for {account_id} with no outstanding "
                f"disconnect (duplicate ReconnectToGame) — no PlayerReconnected sent."
            )

    async def run_gameplay_sequence(self):
        """Sequential gameplay workflow starting from the pre-game coin flip."""
        try:
            await self.run_pregame_coin_flip()
            await self.run_setup_phase()
            await self.run_mulligan_phase()
            await self.run_placement_phase()
            await self.run_turn_loop()
        except GameOver:
            logging.info(f"[Session {self.game_id}] Gameplay sequence finished (game over).")
        except Exception as e:
            logging.exception(f"[Session {self.game_id}] Error in gameplay sequence: {e}")
        finally:
            from spirit.game.session.manager import GameSessionManager  # circular-import guard
            GameSessionManager().remove_session(self.game_id)

    def _entity_introduced_msg(self, card) -> Dict[str, Any]:
        """Builds an EntityIntroduced game message (reveals a card's identity).

        Cards serialize un-introduced (attributes=null) in every hidden zone,
        including the owner's own deck and prize pile; this message is how a
        viewer legally learns a card's face (e.g. the owner on draw).
        """
        return self._build_msg(
            OutboundMsg.ENTITY_INTRODUCED.value,
            {
                "gameID": self.game_id,
                "entityID": card.entity_id,
                "entityName": card.get_entity_name(),
                "attributeMap": card.serialize_attributes(),
            },
        )

    def _entity_moved_msg(self, entity_id: str, destination_id: str, position: int) -> Dict[str, Any]:
        """Builds an EntityMoved game message (moves an existing entity into a new parent)."""
        entity = self.board_state.get_entity(entity_id)
        if entity is not None:
            # Mirror the client: every EntityMoved stamps A.m = positionInParent.
            entity.board_slot = position
        return self._build_msg(
            OutboundMsg.ENTITY_MOVED.value,
            {
                "gameID": self.game_id,
                "entityID": entity_id,
                "destinationID": destination_id,
                "positionInParent": position,
                "animDuration": MOVE_ANIM_DURATION_MS,
            },
        )

    def _attributes_reset_msg(self, entity_id: str) -> Dict[str, Any]:
        """AttributesReset: re-hides a revealed card (L.U -> ResetAttributes),
        restoring its face-down back after a "look at your Prizes" reveal."""
        return self._build_msg(
            OutboundMsg.ATTRIBUTES_RESET.value,
            {"gameID": self.game_id, "entityID": entity_id},
        )

    def _entity_id_data_effect_msg(self, key: str, entity_id: str) -> Dict[str, Any]:
        """EntityIDDataEffect: a named entity parameter read by the bracket's executor."""
        return self._build_msg(
            OutboundMsg.ENTITY_ID_DATA_EFFECT.value,
            {"gameID": self.game_id, "key": key, "value": entity_id},
        )

    def _condition_attr_msg(self, pokemon) -> Dict[str, Any]:
        """AttributeModified carrying the entity's FULL Special Conditions
        array; the Add/RemoveSpecialCondition executors diff it themselves."""
        conditions = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        return self._build_msg(
            OutboundMsg.ATTRIBUTE_MODIFIED.value,
            {
                "gameID": self.game_id,
                "entityID": pokemon.entity_id,
                "attribute": {
                    "name": AttrID.SPECIAL_CONDITIONS.value,
                    "value": conditions,
                    "originalValue": conditions,
                    "modValue": None,
                },
            },
        )

    def clear_condition_state(self, entity_id: str):
        """Pops ALL per-entity Special Condition bookkeeping (sleep/poison/
        paralysis maps); call wherever the conditions array is wiped wholesale
        (KO, leaving play, switching out of Active)."""
        self.sleep_checkup_coins.pop(entity_id, None)
        self.poison_counters.pop(entity_id, None)
        self.paralyzed_since.pop(entity_id, None)

    def clear_pokemon_effects(self, pokemon) -> bool:
        """Wipes every effect that ends when a Pokemon leaves the Active spot
        or play entirely: Special Conditions (attr + bookkeeping), attack and
        retreat locks, temporary passives, and entity-keyed history stamps.
        Returns True iff it had any Special Conditions."""
        had_conditions = bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))
        pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, [])
        self.clear_condition_state(pokemon.entity_id)
        entity_id = pokemon.entity_id
        state = self.turn_state
        for key in [k for k in state.attack_locks if k[0] == entity_id]:
            state.attack_locks.pop(key, None)
        state.retreat_locks.pop(entity_id, None)
        state.attach_restrictions.pop(entity_id, None)
        for entity_map in (state.damage_taken, state.damage_taken_last_turn,
                           state.became_active_turn):
            entity_map.pop(entity_id, None)
        # retreated_entities is deliberately kept: the retreat executor stamps
        # it right after calling this on the retreating Pokemon.
        for entity_set in (state.healed_entities, state.healed_entities_last_turn,
                           state.turn_draw_entity_ids,
                           state.turn_draw_entity_ids_last_turn):
            entity_set.discard(entity_id)
        self.board_state.temporary_passives = [
            tp for tp in self.board_state.temporary_passives
            if tp.carrier_entity_id != entity_id
        ]
        return had_conditions

    def reset_pokemon_damage(self, pokemon) -> None:
        """A Pokemon leaving PLAY (to hand/deck/discard/lost zone) becomes a
        fresh card: restore HP to the printed max so no damage counters survive
        to be re-rendered or replayed. NOT for leave-Active moves (retreat/
        switch keep their damage)."""
        printed_max = pokemon.attribute_originals.get(
            AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
        )
        pokemon.set_attribute(AttrID.HP, printed_max)

    def reset_ability_usage(self, pokemon) -> None:
        """A Pokemon leaving PLAY becomes a fresh card: its once-per-turn
        ability usage resets, so a replay (Scoop Up Net) can use it again.
        NOT for leave-Active moves (a retreated Pokemon keeps its usage);
        shared_once_per_turn is a per-turn cap and is intentionally untouched."""
        for key in [k for k in self.turn_state.used_abilities
                    if k[0] == pokemon.entity_id]:
            self.turn_state.used_abilities.discard(key)

    def _remove_single_condition(self, pokemon, condition: SpecialConditions) -> Dict[str, Any]:
        """Removes exactly one Special Condition (sleep wake, burn cure,
        paralysis auto-cure); other conditions (Poisoned stacks with
        everything) are left untouched. Returns the AttributeModified msg."""
        name = CLIENT_SPECIAL_CONDITION_NAMES[condition]
        remaining = [c for c in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
                     if c != name]
        pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, remaining)
        if condition == SpecialConditions.ASLEEP:
            self.sleep_checkup_coins.pop(pokemon.entity_id, None)
        elif condition == SpecialConditions.PARALYZED:
            self.paralyzed_since.pop(pokemon.entity_id, None)
        elif condition == SpecialConditions.POISONED:
            self.poison_counters.pop(pokemon.entity_id, None)
        return self._condition_attr_msg(pokemon)

    def _place_damage_effect_msg(self, target_id: str, amount: int) -> Dict[str, Any]:
        """PlaceDamageEffect: raw damage counters (Poison/Burn checkup ticks,
        Confusion self-hit) -- no W/R, no passive pipeline."""
        return self._build_msg(
            OutboundMsg.PLACE_DAMAGE_EFFECT.value,
            {
                "gameID": self.game_id,
                "destinationID": target_id,
                "originID": None,
                "amount": amount,
                "abilityName": None,
            },
        )

    def _hp_attribute_msg(self, pokemon) -> Dict[str, Any]:
        """AttributeModified for attr 200490 (HP): value=remaining, originalValue=max."""
        return self._build_msg(
            OutboundMsg.ATTRIBUTE_MODIFIED.value,
            {
                "gameID": self.game_id,
                "entityID": pokemon.entity_id,
                "attribute": {
                    "name": AttrID.HP.value,
                    "value": pokemon.get_attribute(AttrID.HP, 0),
                    "originalValue": effective_max_hp(self.board_state, pokemon),
                    "modValue": None,
                },
            },
        )

    async def _apply_raw_damage(self, pokemon, amount: int, bracket: str) -> bool:
        """Lowers HP by `amount` bypassing compute_damage entirely (damage
        counters, not attack damage); sends the bracket. Returns True if this
        would knock it out (the caller resolves the KO after any pacing sleep,
        matching the order the client's KO check needs: bracket, then pacing,
        then the knockout)."""
        current = pokemon.get_attribute(AttrID.HP, 0)
        remaining = max(0, current - amount)
        pokemon.set_attribute(AttrID.HP, remaining)
        await self.send_game_sequence(
            list(self.players.values()), bracket,
            [self._place_damage_effect_msg(pokemon.entity_id, amount),
             self._hp_attribute_msg(pokemon)],
        )
        return remaining <= 0

    async def _resolve_raw_knockout(self, pokemon):
        """Resolves a knockout caused by raw damage (poison/burn/confusion)."""
        ctx = EffectContext(self, pokemon.owning_player_id or "", pokemon, None)
        ctx.knockouts.append(pokemon)
        await self.resolve_knockouts(ctx)

    async def _broadcast_attack_sources(self, entity_ids: List[str]):
        """Points the playmat's attack-source attribute at the acting entities.

        The client's Attack executor dereferences element [0] unconditionally,
        so this must be broadcast before any Attack bracket."""
        self.board_state.playmat.set_attribute(AttrID.ATTACK_SOURCES, entity_ids)
        envelope = self._sequence_envelope(
            EMPTY_SEQUENCE_ID,
            self._build_msg(
                OutboundMsg.ATTRIBUTE_MODIFIED.value,
                {
                    "gameID": self.game_id,
                    "entityID": self.board_state.playmat.entity_id,
                    "attribute": {
                        "name": AttrID.ATTACK_SOURCES.value,
                        "value": entity_ids,
                        "originalValue": entity_ids,
                        "modValue": None,
                    },
                },
            ),
        )
        await self.broadcast_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)

    def _reveal_card_msg(self, entity_id: str, return_to_origin: bool) -> Dict[str, Any]:
        """RevealCardToAllEffect: shows the card large to non-owner viewers."""
        return self._build_msg(
            OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value,
            {
                "gameID": self.game_id,
                "entityID": entity_id,
                "Return": return_to_origin,
                "alwaysReveal": False,
            },
        )

    def _turn_order(self) -> List[str]:
        """Player IDs with the first player first, so draws/prizes animate in turn order."""
        ids = list(self.players.keys())
        if self.first_player_id and self.first_player_id in ids:
            ids = [self.first_player_id] + [pid for pid in ids if pid != self.first_player_id]
        return ids

    def _opponent_id(self, player_id: str) -> str:
        """The other player's account ID."""
        return next(pid for pid in self.players.keys() if pid != player_id)

    def _next_selection_counter(self, player_id: str) -> int:
        """Monotonic per-player counter stamped on each selection offer."""
        self._selection_counters[player_id] = self._selection_counters.get(player_id, 2) + 1
        return self._selection_counters[player_id]

    async def prompt_player_choice(
        self,
        player_id: str,
        prompt: str,
        buttons: List[str],
        sort_type: str = "",
    ) -> int:
        """Shows a button dialog (CustomChoiceRequired) and returns the picked index.

        AI players always pick the first button.
        """
        player = self.players[player_id]
        if isinstance(player, AIPlayer):
            return 0
        counter = self._next_selection_counter(player_id)
        choice_data = await self.prompt_selection_message(
            player,
            OutboundMsg.CUSTOM_CHOICE_REQUIRED.value,
            {
                "gameID": self.game_id,
                "counter": counter,
                "prompt": {"id": prompt},
                "offerLength": 0,
                "startingTimestamp": int(time.time() * 1000),
                "sortType": sort_type,
                "buttons": [{"id": button} for button in buttons],
                "sourceEntity": None,
                "kind": "",
            },
            expected_counter=counter,
        )
        selection = choice_data.get("selection")
        return selection if isinstance(selection, int) else 0

    async def prompt_card_chooser(
        self,
        player_id: str,
        source_entity_id: str,
        cards: List[Any],
        count: int,
        minimum: Optional[int] = None,
        prompt: str = "Choose a card",
        ordered: bool = False,
        display_cards: Optional[List[Any]] = None,
        slot_prompt: str = "",
    ) -> List[str]:
        """Full-screen card browser (SelectionRevealArea): the player picks up
        to `count` of `cards`; returns the picked entity IDs in pick order.

        minimum=None means "exactly count" (auto-reduced when fewer cards
        exist); minimum=0 makes the pick optional. Card faces ride the offer's
        revealEntities inline, so hidden-zone (deck) cards need no prior
        EntityIntroduced and re-hide when the browser closes. display_cards
        (superset of cards, e.g. the whole deck) all show in the carousel;
        only `cards` are selectable and the client sorts them first.
        slot_prompt renders under the empty pick slot ("Choose a Basic
        Pokemon to put into your hand."); empty = a bare slot.
        """
        player = self.players[player_id]
        valid = [c.entity_id for c in cards]
        display = {c.entity_id: c for c in cards}
        for c in display_cards or []:
            display.setdefault(c.entity_id, c)
        if not display or count <= 0:
            return []
        if isinstance(player, AIPlayer):
            return valid[:count]

        min_to_select = count if minimum is None else minimum
        forced = min_to_select > 0
        # The browser DISPLAYS revealEntities' keys; selectability comes from
        # selections[0].validTargets (constraints are read from selections[0],
        # NOT the outer object). The outer targetPrompt is the panel header.
        inner = {
            "name": SelectionKind.ENTITY_LIST.value,
            "selected": True,
            # Must be non-null: UpdateSlotCounts derefs every selection's
            # targetPrompt.DisplayText (null NREs out of Initialize -> blank
            # Show Playmat + soft-lock); empty id = bare unlabeled slot.
            "targetPrompt": {"id": slot_prompt or ""},
            "validTargets": valid,
            "numberToSelect": count,
            "minimumToSelect": min_to_select,
            "forced": forced,
        }
        reveal_info = {
            "name": SelectionKind.COMPOSITE_REVEAL.value,
            "selected": True,
            "targetPrompt": {"id": prompt},
            "revealEntities": {eid: c.serialize_attributes() for eid, c in display.items()},
            "ordered": ordered,
            "selections": [inner],
            "validTargets": valid,
            "numberToSelect": count,
            "minimumToSelect": min_to_select,
            "forced": forced,
        }
        return await self._run_pick_offer(
            player_id, source_entity_id, reveal_info,
            SelectionKind.COMPOSITE_REVEAL.value,
            valid, count, min(min_to_select, len(valid)), forced,
        )

    async def prompt_card_chooser_groups(
        self,
        player_id: str,
        source_entity_id: str,
        groups: List[Dict[str, Any]],
        prompt: str = "Choose a card",
        display_cards: Optional[List[Any]] = None,
        total: Optional[int] = None,
        any_of: bool = False,
    ) -> List[List[str]]:
        """One browser, one labeled pick slot per group (Irida/Korrina style).

        Each group is {"cards", "count", "minimum", "slot_prompt"}; group card
        lists must be disjoint (the client assigns a pick to the first group
        containing it). Returns the picked entity IDs per group. any_of picks
        from any groups under one global `total` cap (Any-composite browser)
        instead of AND-ing every group's own count.
        """
        player = self.players[player_id]
        display: Dict[str, Any] = {}
        for group in groups:
            for c in group["cards"]:
                display.setdefault(c.entity_id, c)
        valid = list(display.keys())
        for c in display_cards or []:
            display.setdefault(c.entity_id, c)
        total_count = sum(group["count"] for group in groups) if total is None else total
        if not display or total_count <= 0:
            return [[] for _ in groups]
        if isinstance(player, AIPlayer):
            return [[c.entity_id for c in g["cards"][:g["count"]]] for g in groups]

        forced = any(group.get("minimum", 0) > 0 for group in groups)
        kind = SelectionKind.ANY_COMPOSITE_REVEAL.value if any_of \
            else SelectionKind.AND_COMPOSITE_REVEAL.value
        selections = [
            {
                "name": SelectionKind.ENTITY_LIST.value,
                "selected": True,
                "targetPrompt": {"id": group.get("slot_prompt") or ""},
                "validTargets": [c.entity_id for c in group["cards"]],
                "numberToSelect": group["count"],
                "minimumToSelect": group.get("minimum", 0),
                "forced": forced,
            }
            for group in groups
        ]
        # Outer numberToSelect sizes the picked strip (one slot per group when
        # each group's count is 1); minimumToSelect 0 defers the Done gate to
        # the per-group minimums (R.m satisfiedFromInnerSelections...).
        reveal_info = {
            "name": kind,
            "selected": True,
            "targetPrompt": {"id": prompt},
            "revealEntities": {eid: c.serialize_attributes() for eid, c in display.items()},
            "ordered": False,
            "selections": selections,
            "validTargets": valid,
            "numberToSelect": total_count,
            "minimumToSelect": 0,
            "forced": forced,
        }
        min_effective = sum(
            min(group.get("minimum", 0), len(group["cards"])) for group in groups
        )
        picked = await self._run_pick_offer(
            player_id, source_entity_id, reveal_info,
            kind,
            valid, total_count, min_effective, forced,
        )
        by_group: List[List[str]] = [[] for _ in groups]
        group_ids = [{c.entity_id for c in group["cards"]} for group in groups]
        for eid in picked:
            for i, ids in enumerate(group_ids):
                if eid in ids and len(by_group[i]) < groups[i]["count"]:
                    by_group[i].append(eid)
                    break
        return by_group

    def _view_cards_offer_info(self, cards: List[Any], prompt: str) -> Dict[str, Any]:
        """Reveal-browser node with NOTHING selectable (view-only): all faces
        in revealEntities, empty validTargets, minimum 0 so Done is always
        enabled."""
        inner = {
            "name": SelectionKind.ENTITY_LIST.value,
            "selected": True,
            "targetPrompt": {"id": ""},
            "validTargets": [],
            "numberToSelect": 0,
            "minimumToSelect": 0,
            "forced": False,
        }
        return {
            "name": SelectionKind.COMPOSITE_REVEAL.value,
            "selected": True,
            "targetPrompt": {"id": prompt},
            "revealEntities": {c.entity_id: c.serialize_attributes() for c in cards},
            "ordered": False,
            "selections": [inner],
            "validTargets": [],
            "numberToSelect": 0,
            "minimumToSelect": 0,
            "forced": False,
        }

    async def prompt_view_cards(
        self, player_id: str, source_entity_id: str, cards: List[Any],
        prompt: str = "Revealed cards",
    ) -> None:
        """View-only reveal browser (E4 reveal_hand): the viewer looks at the
        cards and clicks Done; nothing is selectable. AI viewers skip.
        needs live client verification: zero-count picked strip."""
        player = self.players.get(player_id)
        if player is None or isinstance(player, AIPlayer) or not cards:
            return
        reveal_info = self._view_cards_offer_info(cards, prompt)
        await self._run_pick_offer(
            player_id, source_entity_id, reveal_info,
            SelectionKind.COMPOSITE_REVEAL.value,
            [], 0, 0, False,
        )

    async def prompt_entity_picker(
        self,
        player_id: str,
        source_entity_id: str,
        cards: List[Any],
        count: int,
        minimum: Optional[int] = None,
        prompt: str = "Choose a card",
    ) -> List[str]:
        """In-place picker: the targets glow green where they sit (hand or
        playmat) instead of opening the reveal browser.

        A plain EntityListTargetInformation kind misses the UI-command factory
        table, so the client falls back to the r.e command and PieHinter glows
        the validTargets in place; the node's own targetPrompt renders as the
        center banner (the root prompt does not).
        """
        player = self.players[player_id]
        valid = [c.entity_id for c in cards]
        if not valid or count <= 0:
            return []
        if isinstance(player, AIPlayer):
            return valid[:count]

        min_to_select = count if minimum is None else minimum
        forced = min_to_select > 0
        node = {
            "name": SelectionKind.ENTITY_LIST.value,
            "selected": True,
            "targetPrompt": {"id": prompt},
            "validTargets": valid,
            "numberToSelect": count,
            "minimumToSelect": min_to_select,
            "forced": forced,
        }
        return await self._run_pick_offer(
            player_id, source_entity_id, node,
            SelectionKind.ENTITY_LIST.value,
            valid, count, min(min_to_select, len(valid)), forced,
        )

    async def prompt_damage_counter_placement(
        self,
        player_id: str,
        source_entity_id: str,
        candidates: List[Any],
        count: int,
        amount_per_click: int = 10,
        prompt: str = "Place damage counters",
    ) -> Dict[str, int]:
        """Native click-to-place picker (MultiSelectEntityListTargetInformation,
        command Q.N): the player clicks a valid target repeatedly, each click
        stamping a live +amount_per_click damage bubble; Done gates on exactly
        `count` total clicks (min == max == count).

        Returns entity_id -> counters placed (zero-click targets omitted).
        """
        player = self.players[player_id]
        valid = [c.entity_id for c in candidates]
        if not valid or count <= 0:
            return {}
        if isinstance(player, AIPlayer):
            return {valid[0]: count}

        node = {
            "name": SelectionKind.MULTI_SELECT_ENTITY_LIST.value,
            "selected": True,
            "targetPrompt": {"id": prompt},
            "validTargets": valid,
            "numberToSelect": count,
            "minimumToSelect": count,
            "forced": True,
            "amountPerClick": amount_per_click,
            # Q.m.HintStrength only feeds CheckHintStrength's b.w reveal-composite
            # branch (this node isn't b.w), so an empty map still renders the
            # normal strong glow; must be non-null (unguarded foreach).
            "hintTargetMap": {},
        }
        await self._set_opponents_waiting(player_id, True)
        try:
            for _ in range(MAX_SELECTION_RETRIES):
                counter = self._next_selection_counter(player_id)
                offer = {
                    "gameID": self.game_id,
                    "counter": counter,
                    "prompt": None,
                    "offerLength": 60000,
                    "startingTimestamp": int(time.time() * 1000),
                    "forced": True,
                    "targetType": SelectionKind.MULTI_SELECT_ENTITY_LIST.value,
                    "ignoreFirst": True,
                    "selectionParams": {},
                    "optimalPlayMap": [],
                    "sourceID": source_entity_id,
                    "targetMap": {source_entity_id: [node]},
                }
                reply = await self.prompt_selection_message(
                    player,
                    OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                    offer,
                    expected_counter=counter,
                )
                selection = reply.get("selection") if isinstance(reply, dict) else None
                if not isinstance(selection, dict):
                    logging.warning(
                        f"[Session {self.game_id}] Damage counter placement got no "
                        f"selection; re-offering."
                    )
                    continue
                tally: Dict[str, int] = {}
                total = 0
                for response in selection.get("targetResponses") or []:
                    if not isinstance(response, dict):
                        continue
                    for entry in response.get("entities") or []:
                        if not isinstance(entry, dict) or total >= count:
                            continue
                        target = entry.get("target")
                        clicks = entry.get("selections") or 0
                        if target not in valid or clicks <= 0:
                            continue
                        clicks = min(clicks, count - total)
                        tally[target] = tally.get(target, 0) + clicks
                        total += clicks
                if total != count:
                    logging.warning(
                        f"[Session {self.game_id}] Damage counter placement totaled "
                        f"{total}/{count}; applying as sent."
                    )
                return tally
            return {valid[0]: count}
        finally:
            await self._set_opponents_waiting(player_id, False)

    async def _run_pick_offer(
        self,
        player_id: str,
        source_entity_id: str,
        node: Dict[str, Any],
        target_type: str,
        valid: List[str],
        count: int,
        min_effective: int,
        forced: bool,
    ) -> List[str]:
        """Sends a single-node SelectionWithTargetsRequired pick offer and
        collects the replied entityList; opponents see a waiting banner."""
        player = self.players[player_id]
        await self._set_opponents_waiting(player_id, True)
        try:
            for _ in range(MAX_SELECTION_RETRIES):
                counter = self._next_selection_counter(player_id)
                offer = {
                    "gameID": self.game_id,
                    "counter": counter,
                    "prompt": None,
                    "offerLength": 60000,
                    "startingTimestamp": int(time.time() * 1000),
                    "forced": forced,
                    "targetType": target_type,
                    # ignoreFirst auto-selects the lone map key and dives
                    # straight into the target node.
                    "ignoreFirst": True,
                    "selectionParams": {},
                    "optimalPlayMap": [],
                    "sourceID": source_entity_id,
                    "targetMap": {source_entity_id: [node]},
                }
                reply = await self.prompt_selection_message(
                    player,
                    OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                    offer,
                    expected_counter=counter,
                )
                selection = reply.get("selection")
                if selection is None:
                    if min_effective == 0:
                        return []
                    continue
                picked: List[str] = []
                responses = selection.get("targetResponses") or [] \
                    if isinstance(selection, dict) else []
                for response in responses:
                    if isinstance(response, dict):
                        picked.extend(
                            t for t in (response.get("entityList") or []) if t in valid
                        )
                picked = picked[:count]
                if len(picked) >= min_effective:
                    return picked
                logging.warning(
                    f"[Session {self.game_id}] Card pick under-picked "
                    f"({len(picked)}/{min_effective}); re-offering."
                )
            return valid[:min_effective]
        finally:
            await self._set_opponents_waiting(player_id, False)

    async def _set_opponents_waiting(self, player_id: str, waiting: bool):
        """Shows/clears the "opponent is deciding" banner on the other clients."""
        for pid, viewer in self.players.items():
            if pid == player_id:
                continue
            if waiting:
                await self._send_pause_prompt(viewer, PROMPT_WAIT_OPPONENT_DECISION)
            else:
                await self._send_close_pause_prompt(viewer)

    async def _flush_effect_runs(self, ctx: EffectContext,
                                 default: str = GameSequence.GROUPED_MOVE.value):
        """Sends an effect's queued messages as per-viewer bracket runs."""
        for pid, viewer in self.players.items():
            for name, msgs in ctx.bracket_runs_for(pid, default):
                if msgs:
                    await self.send_game_sequence([viewer], name, msgs)

    # ------------------------------------------------------------------
    # Knockouts, prizes, promotion, game end
    # ------------------------------------------------------------------

    async def resolve_knockouts(self, ctx: EffectContext, _ko_depth: int = 0):
        """Discards each knocked-out stack, awards prizes, promotes a new
        Active for the losing side, and checks every win condition."""
        if not ctx.knockouts:
            return
        # Snapshot ON_KNOCKED_OUT triggers BEFORE any stack moves: ability_locked
        # reads board position, so the carrier must still be top-level in-play.
        ko_triggers: List[Tuple[PokemonEntity, str, Ability]] = []
        for pokemon in ctx.knockouts:
            owner_id = pokemon.owning_player_id
            if owner_id is None or ability_locked(self.board_state, pokemon):
                continue
            for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
                if not isinstance(entry, dict):
                    continue
                ability_id = entry.get("abilityID")
                ability = ABILITIES_BY_ID.get(ability_id) if ability_id else None
                if ability is not None and ability.has_trigger(Triggers.ON_KNOCKED_OUT):
                    ko_triggers.append((pokemon, owner_id, ability))

        # Special-energy leave-play hooks (Gift Energy's draw) snapshotted with
        # the KO'd carrier before any stack moves; run only for attack KOs.
        is_attack_ko = ctx.is_attack_effect()
        energy_ko_hooks: List[Tuple[str, Any]] = []
        for pokemon in ctx.knockouts:
            owner_id = pokemon.owning_player_id
            if owner_id is None or not is_attack_ko \
                    or ctx.attacker.owning_player_id == owner_id:
                continue
            for energy in self.board_state.attached_energies(pokemon):
                definition = def_for(energy.archetype_id)
                hook = getattr(definition, "on_carrier_knocked_out", None)
                if hook is not None and hook is not unimplemented:
                    energy_ko_hooks.append((owner_id, hook))

        # Prize counts/destinations evaluate BEFORE any stack moves so the
        # KO'd Pokemon's own passives and Special Conditions still count.
        passive_pairs = active_passives(self.board_state)
        prize_plans: List[Tuple[str, int, str]] = []
        ally_triggers: List[Tuple[PokemonEntity, str, Ability, PokemonEntity, bool]] = []
        for pokemon in ctx.knockouts:
            owner_id = pokemon.owning_player_id
            if owner_id is None:
                continue
            count = prize_value(pokemon.archetype_id)
            for passive, carrier in passive_pairs:
                count = passive.modify_prizes_for_knockout(pokemon, ctx, count, carrier)
            mode = next(
                (m for passive, carrier in passive_pairs
                 for m in [passive.prize_destination(pokemon, ctx, carrier)] if m),
                "hand",
            )
            prize_plans.append((self._opponent_id(owner_id), max(0, count), mode))
            ko_from_attack = is_attack_ko and ctx.attacker.owning_player_id != owner_id
            for ally in self.board_state.pokemon_in_play(owner_id):
                if ally is pokemon or ally in ctx.knockouts:
                    continue
                locked = ability_locked(self.board_state, ally)
                for entry in ally.get_attribute(AttrID.PIE_ABILITIES) or []:
                    if not isinstance(entry, dict):
                        continue
                    ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
                    if ability is None \
                            or not ability.has_trigger(Triggers.ON_ALLY_KNOCKED_OUT):
                        continue
                    if locked and not ability.is_granted:
                        continue
                    ally_triggers.append(
                        (ally, owner_id, ability, pokemon, ko_from_attack))
        # ON_ALLY_KNOCKED_OUT fires pre-discard: the KO'd stack is still on
        # board with its energies attached (Exp. Share moves one off it).
        for ally, owner_id, ability, victim, from_attack in ally_triggers:
            def _ally_setup(c, _victim=victim, _from_attack=from_attack):
                c.ko_pokemon = _victim
                c.ko_from_attack = _from_attack
                c.ko_attacker = ctx.attacker if _from_attack else None
            await resolve_triggered_ability(
                self, owner_id, ally, ability, ctx_setup=_ally_setup,
                _ko_depth=_ko_depth + 1,
            )

        promotions: List[str] = []
        for pokemon in ctx.knockouts:
            owner_id = pokemon.owning_player_id
            if owner_id is None:
                continue
            taker_id = self._opponent_id(owner_id)
            discard = self.board_state.find_player_area(owner_id, "discard")
            if not discard:
                continue
            was_active = self.board_state.active_pokemon(owner_id) is pokemon
            # Lost City-style passives (Lost Zone) redirect the KO'd Pokemon
            # stack; energy/tools always fall to the discard pile.
            dest_name = next(
                (d for p, c in active_passives(self.board_state)
                 for d in [p.knockout_destination(pokemon, c)] if d),
                "discard",
            )
            dest_area = self.board_state.find_player_area(owner_id, dest_name) or discard
            stack = [pokemon] + _stack_descendants(pokemon)
            moves = []
            for entity in stack:
                area = dest_area if isinstance(entity, PokemonEntity) else discard
                position = len(area.children)
                if self.board_state.move_card(entity.entity_id, area.entity_id):
                    moves.append(self._entity_moved_msg(
                        entity.entity_id, area.entity_id, position
                    ))
            # Every Pokemon in the stack (the KO'd top plus any tucked
            # pre-evolutions) sheds Special Conditions, attack locks, and any
            # turn-scoped stat-modifier PiPs (Power Tablet) -- it has left play.
            viz_msgs = []
            for member in stack:
                if isinstance(member, PokemonEntity):
                    self.clear_pokemon_effects(member)
                    self.reset_ability_usage(member)
                viz_msg = self._clear_entity_visualizations_msg(member)
                if viz_msg is not None:
                    viz_msgs.append(viz_msg)
            # Restore HP to the printed max so the discarded card carries no
            # damage counters (the client keeps rendering attr 200490 there).
            printed_max = pokemon.attribute_originals.get(
                AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
            )
            pokemon.set_attribute(AttrID.HP, printed_max)
            if moves:
                # The attr rides the Knockout bracket (N.k runs non-move
                # commands generically); a move-less bracket would NRE it.
                moves.append(self._build_msg(
                    OutboundMsg.ATTRIBUTE_MODIFIED.value,
                    {
                        "gameID": self.game_id,
                        "entityID": pokemon.entity_id,
                        "attribute": {
                            "name": AttrID.HP.value,
                            "value": printed_max,
                            "originalValue": printed_max,
                            "modValue": None,
                        },
                    },
                ))
                moves.extend(viz_msgs)
                await self.send_game_sequence(
                    list(self.players.values()), GameSequence.KNOCKOUT, moves
                )
            if is_attack_ko and ctx.attacker.owning_player_id != owner_id:
                self.turn_state.kos_by_attack.setdefault(owner_id, []).append({
                    "archetype_id": pokemon.archetype_id,
                    "subtypes": list(subtypes_for(pokemon.archetype_id)),
                })
            if was_active and owner_id not in promotions:
                promotions.append(owner_id)
            logging.info(
                f"[Session {self.game_id}] {pokemon.entity_id} "
                f"({self.players[owner_id].screen_name}) was knocked out."
            )
        prize_awards: Dict[Tuple[str, str], int] = {}
        for taker_id, count, mode in prize_plans:
            if count > 0:
                prize_awards[(taker_id, mode)] = (
                    prize_awards.get((taker_id, mode), 0) + count
                )
        if ctx.extra_prizes and any(t == ctx.player_id for t, _, _ in prize_plans):
            prize_awards[(ctx.player_id, "hand")] = (
                prize_awards.get((ctx.player_id, "hand"), 0) + ctx.extra_prizes
            )
        ctx.knockouts.clear()

        # Fire ON_KNOCKED_OUT triggers after the Knockout brackets/HP resets,
        # before prize taking; ko_from_attack/ko_attacker mirror compute_damage's
        # is_attack/ownership checks.
        trigger_ctxs: List[EffectContext] = []
        if ko_triggers:
            if _ko_depth >= _MAX_KO_TRIGGER_DEPTH:
                logging.error(
                    f"[Session {self.game_id}] ON_KNOCKED_OUT trigger recursion "
                    f"depth exceeded ({_ko_depth}); skipping further triggers."
                )
            else:
                is_attack_ctx = ctx.is_attack_effect()
                for pokemon, owner_id, ability in ko_triggers:
                    ko_from_attack = is_attack_ctx and ctx.attacker.owning_player_id != owner_id
                    ko_attacker = ctx.attacker if ko_from_attack else None

                    def _setup(c, _from_attack=ko_from_attack, _attacker=ko_attacker):
                        c.ko_from_attack = _from_attack
                        c.ko_attacker = _attacker

                    trigger_ctx = await resolve_triggered_ability(
                        self, owner_id, pokemon, ability, ctx_setup=_setup,
                        _ko_depth=_ko_depth + 1,
                    )
                    if trigger_ctx is not None:
                        trigger_ctxs.append(trigger_ctx)

        for owner_id, hook in energy_ko_hooks:
            hook_ctx = EffectContext(self, owner_id, ctx.attacker, None)
            await hook(hook_ctx)
            if hook_ctx._messages:
                await self._flush_effect_runs(hook_ctx)

        for (taker_id, mode), count in prize_awards.items():
            await self._take_prizes(taker_id, count, destination=mode)
        for taker_id in {t for t, _ in prize_awards}:
            prizes = self.board_state.find_player_area(taker_id, "prizePile")
            if prizes is not None and self.board_state.prizes_dealt.get(taker_id) \
                    and not prizes.children:
                await self.end_game(taker_id, "Took all Prize cards")
        for owner_id in promotions:
            if not await self._promote_new_active(owner_id):
                await self.end_game(
                    self._opponent_id(owner_id),
                    f"{self.players[owner_id].screen_name} has no Pokémon left",
                )

        # Trigger effects may cause NEW knockouts of their own;
        # _send_ability_brackets already resolved these inline above, so this
        # is a re-entrant, empty-safe pass (belt-and-suspenders).
        for trigger_ctx in trigger_ctxs:
            if trigger_ctx.knockouts:
                await self.resolve_knockouts(trigger_ctx, _ko_depth=_ko_depth + 1)

    async def _take_prizes(self, player_id: str, count: int,
                           destination: str = "hand"):
        """The player picks `count` face-down prizes and takes them to hand;
        a non-hand `destination` (Billowing Smoke's discard, Barbaracle's
        lostZone) reroutes the picked prizes there after the reveal."""
        prize_area = self.board_state.find_player_area(player_id, "prizePile")
        hand_area = self.board_state.find_player_area(player_id, "hand")
        if not prize_area or not hand_area:
            return
        count = min(count, len(prize_area.children))
        if count <= 0:
            return
        player = self.players[player_id]
        prize_ids = [c.entity_id for c in prize_area.children]
        if isinstance(player, AIPlayer):
            picked = prize_ids[:count]
        else:
            picked = await self._prompt_prize_pick(player_id, prize_ids, count)
        cards = [self.board_state.get_entity(i) for i in picked]
        intros = []
        moves = []
        for card in cards:
            if card is None:
                continue
            position = len(hand_area.children)
            if not self.board_state.move_card(card.entity_id, hand_area.entity_id):
                continue
            intros.append(self._entity_introduced_msg(card))
            moves.append(self._entity_moved_msg(
                card.entity_id, hand_area.entity_id, position
            ))
        if not moves:
            return
        gap_msg = self._refresh_prize_gaps(player_id, prize_area)
        self.turn_state.prizes_taken[player_id] = (
            self.turn_state.prizes_taken.get(player_id, 0) + len(moves)
        )
        self.stat_add(player_id, "prizecardstaken", len(moves))
        logging.info(
            f"[Session {self.game_id}] {player.screen_name} takes "
            f"{len(moves)} Prize card(s)."
        )
        # Prize faces are the taker's knowledge only; the opponent sees the
        # face-down cards fly to hand.
        for pid, viewer in self.players.items():
            await self.send_game_sequence(
                [viewer],
                GameSequence.WITH_OPEN_PRIZE_CARDS,
                ((intros + moves) if pid == player_id else list(moves)) + [gap_msg],
            )
        if destination != "hand":
            # Reroute the taken prizes: a plain GroupedMove after the reveal
            # flow, with intros to the opponent (public-pile arrival reveals).
            # needs live client verification: non-hand prize-take choreography
            dest_area = self.board_state.find_player_area(player_id, destination)
            if dest_area is None:
                return
            reroute_intros, reroute_moves = [], []
            for card in cards:
                if card is None or card.parent is not hand_area:
                    continue
                position = len(dest_area.children)
                if self.board_state.move_card(card.entity_id, dest_area.entity_id):
                    reroute_intros.append(self._entity_introduced_msg(card))
                    reroute_moves.append(self._entity_moved_msg(
                        card.entity_id, dest_area.entity_id, position))
            if reroute_moves:
                opponent = self.players.get(self._opponent_id(player_id))
                if opponent is not None:
                    await self.send_game_sequence(
                        [opponent], GameSequence.SERIAL_SEQUENCE, reroute_intros)
                await self.send_game_sequence(
                    list(self.players.values()), GameSequence.GROUPED_MOVE,
                    reroute_moves)

    def _refresh_prize_gaps(self, player_id: str, prize_area) -> Dict[str, Any]:
        """Marks taken prize positions in the pile's AREA_EMPTY_SLOTS so the
        next pick's fan leaves gaps at them (SlotAssociatedAreaRenderRequester
        skips the listed grid slots); returns the AttributeModified message."""
        dealt = self.board_state.prizes_dealt.get(player_id, 0)
        occupied = {
            c.board_slot if c.board_slot is not None else i
            for i, c in enumerate(prize_area.children)
        }
        gaps = [s for s in range(dealt) if s not in occupied]
        prize_area.set_attribute(AttrID.AREA_EMPTY_SLOTS, gaps)
        return self._build_msg(
            OutboundMsg.ATTRIBUTE_MODIFIED.value,
            {
                "gameID": self.game_id,
                "entityID": prize_area.entity_id,
                "attribute": {
                    "name": AttrID.AREA_EMPTY_SLOTS.value,
                    "value": gaps,
                    "originalValue": gaps,
                    "modValue": None,
                },
            },
        )

    async def _prompt_prize_pick(self, player_id: str, prize_ids: List[str],
                                 count: int) -> List[str]:
        """Prize-pile pick via the r.B fan-out UI; falls back to the top ones."""
        player = self.players[player_id]
        prize_area = self.board_state.find_player_area(player_id, "prizePile")
        info = {
            "name": SelectionKind.PRIZE_CARD.value,
            "selected": True,
            "targetPrompt": {"id": PROMPT_TAKE_PRIZE},
            "validTargets": prize_ids,
            "numberToSelect": count,
            "minimumToSelect": count,
            "forced": True,
            # r.B gates the ENTIRE pile->slots fly-in on this flag; False
            # SetContents the fan cold (cards teleport into the pick grid).
            "presentPrizesAllowed": True,
            "horizontalLayout": False,
        }
        for _ in range(MAX_SELECTION_RETRIES):
            counter = self._next_selection_counter(player_id)
            offer = {
                "gameID": self.game_id,
                "counter": counter,
                "prompt": {"id": PROMPT_TAKE_PRIZE},
                "offerLength": 60000,
                "startingTimestamp": int(time.time() * 1000),
                "forced": True,
                "targetType": SelectionKind.PRIZE_CARD.value,
                "ignoreFirst": True,
                "selectionParams": {},
                "optimalPlayMap": [],
                "sourceID": prize_area.entity_id if prize_area else None,
                "targetMap": {
                    (prize_area.entity_id if prize_area else player_id): [info]
                },
            }
            reply = await self.prompt_selection_message(
                player,
                OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                offer,
                expected_counter=counter,
            )
            selection = reply.get("selection")
            if isinstance(selection, dict):
                picked: List[str] = []
                for response in (selection.get("targetResponses") or []):
                    if isinstance(response, dict):
                        picked.extend(
                            t for t in (response.get("entityList") or [])
                            if t in prize_ids
                        )
                if len(picked) >= count:
                    return picked[:count]
        return prize_ids[:count]

    async def prompt_prize_reveal_pick(
        self, player_id: str, source_id: str,
        prize_ids: List[str], selectable_ids: List[str],
    ) -> Optional[str]:
        """"Look at your Prize cards": reveals every Prize face-up to the picker,
        then offers the standard prize fan restricted to `selectable_ids` (up to
        1, may decline). Returns the picked entityID or None.

        The prize node (PrizeCardTargetInformation) satisfies the client's
        IsInPrizeSelectionNode() so the peek-your-prizes click handler stays
        suppressed -- the reveal browser does NOT, which is why it crashed."""
        player = self.players[player_id]
        prize_area = self.board_state.find_player_area(player_id, "prizePile")
        if isinstance(player, AIPlayer):
            return selectable_ids[0] if selectable_ids else None
        # Reveal every Prize face-up to the picker only (the fan renders faces
        # off the entity attrs; r.B itself carries no reveal). Caller re-hides.
        intros = [self._entity_introduced_msg(self.board_state.get_entity(pid))
                  for pid in prize_ids if self.board_state.get_entity(pid)]
        if intros:
            await self.send_game_sequence([player], GameSequence.SERIAL_SEQUENCE, intros)
        info = {
            "name": SelectionKind.PRIZE_CARD.value,
            "selected": True,
            "targetPrompt": {"id": PROMPT_REVEAL_BASIC_FROM_PRIZE},
            "validTargets": selectable_ids,
            "numberToSelect": 1,
            "minimumToSelect": 0,
            "forced": False,
            "presentPrizesAllowed": True,
            "horizontalLayout": False,
        }
        for _ in range(MAX_SELECTION_RETRIES):
            counter = self._next_selection_counter(player_id)
            offer = {
                "gameID": self.game_id,
                "counter": counter,
                "prompt": {"id": PROMPT_REVEAL_BASIC_FROM_PRIZE},
                "offerLength": 60000,
                "startingTimestamp": int(time.time() * 1000),
                "forced": False,
                "targetType": SelectionKind.PRIZE_CARD.value,
                "ignoreFirst": True,
                "selectionParams": {},
                "optimalPlayMap": [],
                "sourceID": source_id,
                "targetMap": {
                    (prize_area.entity_id if prize_area else player_id): [info]
                },
            }
            reply = await self.prompt_selection_message(
                player,
                OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                offer,
                expected_counter=counter,
            )
            selection = reply.get("selection")
            if selection is None:
                return None
            if isinstance(selection, dict):
                for response in (selection.get("targetResponses") or []):
                    if isinstance(response, dict):
                        for t in (response.get("entityList") or []):
                            if t in selectable_ids:
                                return t
                return None
        return None

    async def _promote_new_active(self, player_id: str) -> bool:
        """The player promotes a benched Pokemon into the empty Active spot.
        Returns False when the bench is empty (a loss condition)."""
        board = self.board_state
        bench_area = board.find_player_area(player_id, "bench")
        active_area = board.find_player_area(player_id, "activePokemonArea")
        if not bench_area or not active_area:
            return False
        candidates = [c for c in bench_area.children if isinstance(c, PokemonEntity)]
        if not candidates:
            return False
        player = self.players[player_id]
        picked = candidates[0]
        if not isinstance(player, AIPlayer) and len(candidates) > 1:
            offer = self._placement_offer_value(
                player_id, PROMPT_CHOOSE_NEW_ACTIVE, candidates, TARGET_TYPE_ACTIVE
            )
            for _ in range(MAX_SELECTION_RETRIES):
                reply = await self.prompt_selection_message(
                    player,
                    OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                    offer,
                    expected_counter=offer["counter"],
                )
                card_id = self._parse_placement_reply(reply, candidates)
                if card_id:
                    picked = self.board_state.get_entity(card_id) or picked
                    break
                offer = self._placement_offer_value(
                    player_id, PROMPT_CHOOSE_NEW_ACTIVE, candidates, TARGET_TYPE_ACTIVE
                )
        board.move_card(picked.entity_id, active_area.entity_id)
        self.turn_state.became_active_turn[picked.entity_id] = \
            self.turn_state.turn_number
        logging.info(
            f"[Session {self.game_id}] {player.screen_name} promoted "
            f"{picked.entity_id} to Active."
        )
        # The bare PlayActive executor lets the EntityMoved animate itself.
        await self.send_game_sequence(
            list(self.players.values()),
            GameSequence.PLAY_ACTIVE,
            [self._entity_moved_msg(picked.entity_id, active_area.entity_id, 0)],
        )
        await self.fire_move_to_active_triggers(picked)
        return True

    def stat_add(self, player_id: str, key: str, amount: int = 1):
        """Bumps a player's EOG summary counter (playmat.endgame.stat.<key>)."""
        stats = self.game_stats.setdefault(player_id, {})
        stats[key] = stats.get(key, 0) + amount

    def stat_max(self, player_id: str, key: str, value: int):
        stats = self.game_stats.setdefault(player_id, {})
        if value > stats.get(key, 0):
            stats[key] = value

    def credit_card_damage(self, player_id: str, entity, amount: int):
        """Accumulates damage per attacking card for the EOG MVP pick."""
        guid = getattr(entity, "archetype_id", None)
        if not guid or amount <= 0:
            return
        name = entity.get_attribute(AttrID.NAME)
        if isinstance(name, dict):
            name = name.get("id", "")
        entry = self.mvp_damage.setdefault(player_id, {}).setdefault(guid, [0, name])
        entry[0] += amount

    def _mvp_for(self, player_id: str) -> Optional[tuple]:
        """(archetype_guid, name_loc_key) of the player's top damage dealer."""
        by_card = self.mvp_damage.get(player_id) or {}
        if not by_card:
            return None
        guid, (_, name) = max(by_card.items(), key=lambda kv: kv[1][0])
        return guid, name

    def _eog_additional_parameters(
        self, viewer_id: str, winner_id: str, reason: str
    ) -> Dict[str, Any]:
        """Per-viewer GameCompletedMessage additionalParameters.

        "GameResult" is REQUIRED: EOGAnimationController_SummaryDialog.Init
        indexes it unguarded and compares against "Win" (KeyNotFoundException
        without it). The me_/opp_ stat keys and GameDuration are optional.
        """
        won = viewer_id == winner_id
        winner_name = self.players[winner_id].screen_name
        params: Dict[str, Any] = {
            "GameResult": {"id": "Win" if won else "Loss"},
            "VictoryReason": {"id": reason},
            "playmat.endgame.stat.gameresult": {
                "id": f"{winner_name} won the match ({reason})."
            },
            # Milliseconds; the summary parses it with double.Parse.
            "GameDuration": {
                "id": str(int((time.time() - self.match_started_at) * 1000))
            },
        }
        for prefix, pid in (("me", viewer_id), ("opp", self._opponent_id(viewer_id))):
            stats = self.game_stats.get(pid, {})
            for key in EOG_STAT_KEYS:
                params[f"{prefix}_playmat.endgame.stat.{key}"] = {
                    "id": str(stats.get(key, 0))
                }
            # Summary-page MVP card render (b.g reads the $...$ key literally).
            mvp = self._mvp_for(pid)
            if mvp:
                guid, name = mvp
                params[f"{prefix}_$playmat.endgame.stat.mvp.archetypeid$"] = {
                    "id": guid
                }
                params[f"{prefix}_playmat.endgame.stat.mvp"] = {"id": name}
        # Summary-page header tiles (EndGameSummaryDamageDealt/CoinRenderer).
        viewer_stats = self.game_stats.get(viewer_id, {})
        params["Damagedealt"] = {"id": str(viewer_stats.get("damagedealt", 0))}
        params["Headsflipped"] = {"id": str(viewer_stats.get("headsflipped", 0))}
        return params

    async def _push_wallet_updates(self):
        """Unsolicited CurrentWallet refresh so earned coins show in the HUD."""
        for player in self.players.values():
            handler = getattr(player, "client_handler", None)
            profile = getattr(handler, "player", None) if handler else None
            if profile is None or getattr(profile, "wallet", None) is None:
                continue
            profile.wallet.refresh_wallet()
            await player.send_packet(
                OutboundMsg.CURRENT_WALLET.value, profile.get_wallet_data()
            )

    def declare_winner(self, winner_id: str, reason: str) -> Dict[str, str]:
        """Pure game-over bookkeeping (no wire/DB): flips the phase and
        records the result; end_game rides it, headless tests call it alone."""
        self.game_result = {
            "winner": winner_id,
            "loser": self._opponent_id(winner_id),
            "reason": reason,
        }
        self.game_phase = GamePhase.GAME_OVER
        return self.game_result

    async def end_game(self, winner_id: str, reason: str):
        """Announces the result on both clients and unwinds the game loop."""
        loser_id = self._opponent_id(winner_id)
        logging.info(
            f"[Session {self.game_id}] Game over: "
            f"{self.players[winner_id].screen_name} wins ({reason})."
        )
        for pid, player in self._unique_recipients():
            coins = COINS_PER_WIN if pid == winner_id else COINS_PER_LOSS
            if isinstance(player, NetworkPlayer):
                grant_coins(player.account_id, coins)
                award_match_points(player.account_id, pid == winner_id)
            reward_list = []
            if coins > 0:
                reward_list.append({
                    "name": "GameReward",
                    "rewardType": "Tokens",
                    "rewardAmount": coins,
                    "rewardProductID": EMPTY_SEQUENCE_ID,
                    "rewardCurrency": "Tokens",
                    # rewardDescription must be non-null: the client's
                    # RewardsList getter dereferences its ID unguarded.
                    "rewardDescription": {"id": "playmat.endgame.gamereward"},
                    "rewardReason": "GameCompleted",
                    "selectedFrom": [],
                    "selectedIndex": 0,
                    "rewardSource": "",
                    "index": 0,
                    "openedReward": None,
                })
            envelope = self._sequence_envelope(
                EMPTY_SEQUENCE_ID,
                self._build_msg(
                    OutboundMsg.GAME_COMPLETED_MESSAGE.value,
                    {
                        "gameID": self.game_id,
                        "winner": winner_id,
                        "loser": loser_id,
                        "endOfGameText": {"id": reason},
                        "coins": coins,
                        "exp": 0,
                        "share": False,
                        "rewardList": reward_list,
                        "additionalParameters": self._eog_additional_parameters(
                            pid, winner_id, reason
                        ),
                    },
                ),
            )
            await player.send_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)
        await self._record_tournament_results(winner_id)
        await self._record_legacy_tournament_result(winner_id)
        await self._push_wallet_updates()
        await self._push_account_updates()
        self.declare_winner(winner_id, reason)
        raise GameOver()

    async def _record_legacy_tournament_result(self, winner_id: str):
        """Advances the live Events-scene bracket this game belonged to."""
        ctx = self.pairing.get("legacy_tournament")
        if not ctx:
            return
        try:
            from spirit.game.live_tournament import LiveTournamentManager
            await LiveTournamentManager().record_game_result(
                ctx["active_id"], self.game_id, winner_id)
        except Exception as e:
            logging.error(f"[Session {self.game_id}] Live tournament result "
                          f"recording failed: {e}", exc_info=True)

    async def _record_tournament_results(self, winner_id: str):
        """Applies a tournament game's result to both runs and pushes progress.

        The client learns tournament results out-of-band: the run's
        AsyncTournamentProgressUpdated after every game, and
        AsyncTournamentRewards (with the prize-table grant) when the run
        reaches its win/loss/game cap."""
        ctx = self.pairing.get("tournament")
        if not ctx:
            return
        from spirit.database import tournament_data
        from spirit.game.tournament_manager import TournamentManager, _client_reward
        tournament = TournamentManager().get(ctx.get("tournament_id", ""))
        definition = tournament.definition if tournament else {}
        run_config = (definition or {}).get("run") or {}
        for pid, player in self.players.items():
            if not isinstance(player, NetworkPlayer):
                continue
            entry_id = (ctx.get("entries") or {}).get(pid)
            if not entry_id:
                continue
            opponent_id = self._opponent_id(pid)
            opponent = self.players.get(opponent_id)
            try:
                entry = await run_db(
                    tournament_data.record_game_result, entry_id,
                    pid == winner_id, opponent_id,
                    opponent.screen_name if opponent else "", run_config)
                if not entry:
                    continue
                await player.send_packet(
                    OutboundMsg.ASYNC_TOURNAMENT_PROGRESS_UPDATED.value,
                    {
                        "tournamentID": entry["tournament_id"],
                        "entryID": entry_id,
                        "wins": entry["wins"],
                        "losses": entry["losses"],
                        "rank": 0,
                        "tiebreakers": entry.get("tiebreakers") or 0,
                    },
                )
                if entry.get("run_complete"):
                    finished, granted = await run_db(
                        tournament_data.finish_entry, entry_id, pid,
                        definition, False)
                    if finished:
                        await player.send_packet(
                            OutboundMsg.ASYNC_TOURNAMENT_REWARDS.value,
                            {
                                "entryID": entry_id,
                                "wins": finished["wins"],
                                "losses": finished["losses"],
                                "rewards": [_client_reward(r) for r in granted],
                            },
                        )
            except Exception as e:
                logging.error(
                    f"[Session {self.game_id}] Tournament result recording "
                    f"failed for {pid}: {e}", exc_info=True)

    async def concede(self, account_id: str):
        """Ends the game with the conceding player as loser.

        Runs in the packet-handler task, so end_game's GameOver is swallowed
        here; the gameplay task unwinds by failing its pending selection
        future (or at its next prompt via the GAME_OVER phase guard).
        """
        if self.game_phase == GamePhase.GAME_OVER or account_id not in self.players:
            return
        loser = self.players[account_id]
        try:
            await self.end_game(
                self._opponent_id(account_id),
                f"{loser.screen_name} conceded",
            )
        except GameOver:
            pass
        for player in self.players.values():
            fut = getattr(player, "pending_choice_future", None)
            if fut is not None and not fut.done():
                fut.set_exception(GameOver())

    async def _push_account_updates(self):
        """Unsolicited AccountUpdated so the versus ladder points refresh.

        The client's ReplaceWith swaps ALL account attributes, so the payload
        must carry the full set (build_account_attributes)."""
        pushed = set()
        for player in self.players.values():
            if not isinstance(player, NetworkPlayer) or player.account_id in pushed:
                continue
            pushed.add(player.account_id)
            await player.send_packet(
                OutboundMsg.ACCOUNT_UPDATED.value,
                {
                    "account": {
                        "username": player.username,
                        "accountID": player.account_id,
                        "attributes": build_account_attributes(player.account_id),
                    }
                },
            )

    async def _run_pokemon_checkup(self, active_id: Optional[str] = None):
        """Between-turns checkup, per player (turn order), on that player's
        ACTIVE only: Poison -> Burn -> Sleep -> Paralysis-cure. Then fires
        BETWEEN_TURNS triggered abilities for every in-play Pokemon."""
        active_id = active_id if active_id is not None else self.turn_state.active_player_id
        turn_number = self.turn_state.turn_number
        poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
        burned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.BURNED]
        asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
        paralyzed = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.PARALYZED]

        for player_id in self._turn_order():
            active = self.board_state.active_pokemon(player_id)
            if active is None:
                continue

            conditions = active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            if poisoned in conditions:
                await self._checkup_poison(active)
            # A poison KO clears `active`'s conditions via resolve_knockouts,
            # so re-reading after each step is safe even if it was replaced.
            conditions = active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            if burned in conditions:
                await self._checkup_burn(player_id, active)
            conditions = active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            if asleep in conditions:
                await self._checkup_sleep(player_id, active)
            conditions = active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            if (
                player_id == active_id
                and paralyzed in conditions
                and self.paralyzed_since.get(active.entity_id, -1) < turn_number
            ):
                await self.send_game_sequence(
                    list(self.players.values()), GameSequence.REMOVE_SPECIAL_CONDITION,
                    # Executor ctor (M.t) indexes the data effects with "Target"
                    [self._entity_id_data_effect_msg("Target", active.entity_id),
                     self._remove_single_condition(active, SpecialConditions.PARALYZED)],
                )

        for player_id in self._turn_order():
            for pokemon in list(self.board_state.pokemon_in_play(player_id)):
                await self._fire_triggered_abilities(
                    player_id, pokemon, Triggers.BETWEEN_TURNS
                )

    async def _checkup_poison(self, active):
        """Poison tick: 10 * poison_counters (default 1) raw damage."""
        amount = 10 * self.poison_counters.get(active.entity_id, 1)
        knocked_out = await self._apply_raw_damage(
            active, amount, GameSequence.POISON_DAMAGE.value
        )
        await self.choreo_pause(1.5)
        if knocked_out:
            await self._resolve_raw_knockout(active)

    async def _checkup_burn(self, player_id: str, active):
        """Burn tick: 2 damage counters (passives may modify), then a flip --
        heads cures; blocks_burn_recovery skips the flip entirely."""
        counters = 2
        for passive, carrier in active_passives(self.board_state):
            counters = passive.modify_burn_counters(counters, active, carrier)
        knocked_out = await self._apply_raw_damage(
            active, max(0, counters) * 10, GameSequence.BURN_DAMAGE.value
        )
        if knocked_out:
            await self.choreo_pause(1.5)
            await self._resolve_raw_knockout(active)
            return
        if burn_recovery_blocked(self.board_state, active):
            return
        flip = random.choice([0, 1])
        heads = flip == 0
        self.stat_add(player_id, "headsflipped", 1 if heads else 0)
        self.stat_add(player_id, "tailsflipped", 0 if heads else 1)
        await self.send_game_sequence(
            list(self.players.values()), GameSequence.FLIP_FOR_BURN,
            [self._build_msg(
                OutboundMsg.MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT.value,
                {
                    "gameID": self.game_id,
                    "resultLst": [flip],
                    "title": {"id": TEXT_BURN_CHECK},
                    "gameText": {"id": TEXT_BURN_CURED if heads else TEXT_STILL_BURNED},
                    "source": active.entity_id,
                    "targets": [active.entity_id],
                },
            )],
        )
        await self.choreo_pause(3.0)
        if heads:
            await self.send_game_sequence(
                list(self.players.values()), GameSequence.REMOVE_SPECIAL_CONDITION,
                [self._entity_id_data_effect_msg("Target", active.entity_id),
                 self._remove_single_condition(active, SpecialConditions.BURNED)],
            )

    async def _checkup_sleep(self, player_id: str, active):
        """Sleep flip: all heads wakes (Thumping Snore's rider flips 2 coins)."""
        coins = self.sleep_checkup_coins.get(active.entity_id, 1)
        flips = [random.choice([0, 1]) for _ in range(coins)]
        woke = all(f == 0 for f in flips)
        self.stat_add(player_id, "headsflipped", flips.count(0))
        self.stat_add(player_id, "tailsflipped", flips.count(1))
        await self.send_game_sequence(
            list(self.players.values()),
            GameSequence.FLIP_TO_WAKE_UP,
            [self._build_msg(
                OutboundMsg.MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT.value,
                {
                    "gameID": self.game_id,
                    "resultLst": flips,
                    "title": {"id": TEXT_SLEEP_CHECK},
                    "gameText": {"id": TEXT_WOKE_UP if woke else TEXT_STILL_ASLEEP},
                    "source": active.entity_id,
                    "targets": [active.entity_id],
                },
            )],
        )
        await self.choreo_pause(3.0)
        if woke:
            await self.send_game_sequence(
                list(self.players.values()),
                GameSequence.REMOVE_SPECIAL_CONDITION,
                # Executor ctor (M.t) indexes the data effects with "Target"
                [self._entity_id_data_effect_msg("Target", active.entity_id),
                 self._remove_single_condition(active, SpecialConditions.ASLEEP)],
            )
        logging.info(
            f"[Session {self.game_id}] Sleep check for {active.entity_id}: "
            f"{'woke up' if woke else 'still Asleep'} ({flips})."
        )

    async def _broadcast_shuffle_deck(self, player_id: str):
        """Shuffles a player's deck server-side and plays the shuffle animation on both clients.
        """
        self.board_state.shuffle_deck(player_id)
        deck_area = self.board_state.find_player_area(player_id, "deck")
        if not deck_area:
            return
        envelope = self._sequence_envelope(
            EMPTY_SEQUENCE_ID,
            self._build_msg(
                OutboundMsg.SHUFFLED.value,
                {"gameID": self.game_id, "entityID": deck_area.entity_id},
            ),
        )
        await self.broadcast_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)

    async def run_setup_phase(self):
        """Shuffles decks and deals opening hands after the coin flip.

        Per-player GroupedMove children animate both hands in parallel, and
        each viewer's own-card reveals go out BEFORE the bracket (in-bracket
        intros would apply only after the deal, dealing the hand face-down).
        """
        self.game_phase = GamePhase.DEAL_HANDS

        # 1. Shuffle each deck and animate it (turn order = first player first).
        for player_id in self._turn_order():
            await self._broadcast_shuffle_deck(player_id)
        await asyncio.sleep(SHUFFLE_ANIM_SECONDS)

        # 2. Deal the opening hands from the (now shuffled) decks.
        moves_by_player: Dict[str, List[Dict[str, Any]]] = {}
        intros_by_player: Dict[str, List[Dict[str, Any]]] = {}
        for player_id in self._turn_order():
            drawn = self.board_state.draw_cards(player_id, STARTING_HAND_SIZE)
            logging.info(
                f"[Session {self.game_id}] Dealt {len(drawn)} cards to "
                f"{self.players[player_id].screen_name}."
            )
            intros_by_player[player_id] = [
                self._entity_introduced_msg(d["card"]) for d in drawn
            ]
            moves_by_player[player_id] = [
                self._entity_moved_msg(
                    d["entity_id"], d["destination_id"], d["position"]
                )
                for d in drawn
            ]

        grouped_moves = [
            NestedSequence(GameSequence.GROUPED_MOVE, moves_by_player[pid])
            for pid in self._turn_order()
            if moves_by_player.get(pid)
        ]
        if grouped_moves:
            for player_id, player in self.players.items():
                for intro in intros_by_player.get(player_id, []):
                    await player.send_packet(
                        OutboundMsg.SEQUENCE_MESSAGE.value,
                        self._sequence_envelope(EMPTY_SEQUENCE_ID, intro),
                    )
                await self.send_game_sequence(
                    [player],
                    GameSequence.DEAL_INITIAL_HANDS,
                    grouped_moves,
                )

        # Hands are dealt; the mulligan check picks up from here.
        self.game_phase = GamePhase.SETUP_PHASE

    async def run_mulligan_phase(self):
        """Reshuffles Basic-less opening hands and offers the opponent extra draws."""
        self.game_phase = GamePhase.MULLIGAN_PHASE
        board = self.board_state
        mulligan_counts: Dict[str, int] = {pid: 0 for pid in self.players}
        # player_id -> list of {entity_id: [attribute dicts]} piles, one per mulligan
        reveal_piles: Dict[str, List[Dict[str, Any]]] = {pid: [] for pid in self.players}

        while True:
            needs_mulligan = [
                pid for pid in self._turn_order()
                if not board.has_basic_pokemon_in_hand(pid)
            ]
            if not needs_mulligan:
                break

            for player_id in needs_mulligan:
                if not board.player_has_any_basic(player_id):
                    logging.error(
                        f"[Session {self.game_id}] Deck of "
                        f"{self.players[player_id].screen_name} contains no Basic "
                        f"Pokemon; skipping impossible mulligan."
                    )
                    needs_mulligan = None
                    break

                hand_area = board.find_player_area(player_id, "hand")
                deck_area = board.find_player_area(player_id, "deck")
                if not hand_area or not deck_area:
                    continue

                # Snapshot the busted hand for the reveal carousel before it
                # goes back into the deck (attributes travel inline).
                reveal_piles[player_id].append({
                    card.entity_id: card.serialize_attributes()
                    for card in hand_area.children
                })
                mulligan_counts[player_id] += 1
                logging.info(
                    f"[Session {self.game_id}] "
                    f"{self.players[player_id].screen_name} mulligans "
                    f"(#{mulligan_counts[player_id]})."
                )

                # The Mulligan executor (M.v) runs its inner commands strictly
                # sequentially, so the hand-return moves ride a nested
                # GroupedMove bracket to animate back into the deck together.
                back_moves = [
                    self._entity_moved_msg(card.entity_id, deck_area.entity_id, i)
                    for i, card in enumerate(hand_area.children)
                ]
                board.return_hand_to_deck(player_id)
                board.shuffle_deck(player_id)
                await self.send_game_sequence(
                    list(self.players.values()),
                    GameSequence.MULLIGAN,
                    [
                        NestedSequence(GameSequence.GROUPED_MOVE, back_moves),
                        self._build_msg(
                            OutboundMsg.SHUFFLED.value,
                            {"gameID": self.game_id, "entityID": deck_area.entity_id},
                        ),
                    ],
                )
                await asyncio.sleep(SHUFFLE_ANIM_SECONDS)

                await self._broadcast_draw(player_id, STARTING_HAND_SIZE)

            if needs_mulligan is None:
                break

        await self._reveal_mulligans(reveal_piles)
        await self._offer_extra_draws(mulligan_counts)

    async def _broadcast_draw(self, player_id: str, count: int):
        """Draws cards server-side and animates them in a Draw bracket on both clients.

        Only the drawing player's bracket carries EntityIntroduced reveals for
        the drawn cards (deck contents are hidden knowledge until drawn); the
        opponent sees face-down moves. The client's Draw executor (m.c) runs
        EntityIntroduced commands first; the moves ride a NESTED GroupedMove
        because flat EntityMoveds get pre-handled and the flip fan's bare
        "Draw" stack misses the path table (default linear curve) -- nested
        moves animate FromDeck|ToHand staggered, like the initial deal.
        """
        drawn = self.board_state.draw_cards(player_id, count)
        if not drawn:
            return
        self.stat_add(player_id, "cardsdrawn", len(drawn))
        nested_moves = NestedSequence(GameSequence.GROUPED_MOVE, [
            self._entity_moved_msg(d["entity_id"], d["destination_id"], d["position"])
            for d in drawn
        ])
        intros = [self._entity_introduced_msg(d["card"]) for d in drawn]
        for pid, player in self.players.items():
            await self.send_game_sequence(
                [player],
                GameSequence.DRAW,
                (intros + [nested_moves]) if pid == player_id else [nested_moves],
            )

    async def _reveal_mulligans(self, reveal_piles: Dict[str, List[Dict[str, Any]]]):
        """Shows each player's mulliganed hands to both clients via the reveal carousel.

        MulliganRevealCardsEffect opens the full-screen MulliganRevealArea
        panel, which introduces the cards from the inline attribute piles and
        un-introduces them again when dismissed, so no hidden information
        leaks past the panel.
        """
        for player_id in self._turn_order():
            piles = reveal_piles.get(player_id) or []
            if not piles:
                continue
            deck_area = self.board_state.find_player_area(player_id, "deck")
            effect = self._build_msg(
                OutboundMsg.MULLIGAN_REVEAL_CARDS_EFFECT.value,
                {
                    "gameID": self.game_id,
                    "player": player_id,
                    "entityIDPiles": piles,
                    "prompt": {"id": TEXT_MULLIGAN_REVEAL_PROMPT},
                    "revealTitle": {"id": f"{self.players[player_id].screen_name} had no Basic Pokémon"},
                    "revealSource": deck_area.entity_id if deck_area else None,
                },
            )
            await self.send_game_sequence(
                list(self.players.values()),
                GameSequence.REVEAL_MULLIGANS,
                [effect],
            )

    async def _offer_extra_draws(self, mulligan_counts: Dict[str, int]):
        """Offers the less-mulliganed player one Yes/No extra draw per net mulligan.

        Uses CustomChoiceRequired (generic R.y button dialog) rather than
        MulliganChoiceRequired: the client contains no UI that can answer a
        MulliganChoiceNode, which would soft-lock the prompt.
        """
        for player_id in self._turn_order():
            opponent_id = self._opponent_id(player_id)
            net_draws = mulligan_counts.get(opponent_id, 0) - mulligan_counts.get(player_id, 0)
            if net_draws <= 0:
                continue
            player = self.players[player_id]
            for i in range(net_draws):
                picked = await self.prompt_player_choice(
                    player_id, PROMPT_MULLIGAN_EXTRA_DRAW,
                    [PROMPT_YES, PROMPT_NO], PROMPT_SORT_MULLIGAN,
                )
                if picked != 0:
                    break
                logging.info(
                    f"[Session {self.game_id}] {player.screen_name} draws an "
                    f"extra card for opponent mulligan ({i + 1}/{net_draws})."
                )
                await self._broadcast_draw(player_id, 1)

    async def run_placement_phase(self):
        """Both players place their Active (required), then their Bench (optional)."""
        self.game_phase = GamePhase.PLACEMENT_PHASE

        done_players: set = set()
        await asyncio.gather(*(
            self._run_active_placement(pid, done_players) for pid in self._turn_order()
        ))
        # Barrier reached: clear any lingering "please wait" prompts.
        for player in self.players.values():
            await self._send_close_pause_prompt(player)

        done_players = set()
        await asyncio.gather(*(
            self._run_bench_placement(pid, done_players) for pid in self._turn_order()
        ))
        for player in self.players.values():
            await self._send_close_pause_prompt(player)

        await self._introduce_initial_pokemon()

        self.game_phase = GamePhase.PRIZE_DEAL
        await self._deal_prize_cards()
        self.game_phase = GamePhase.SETUP_COMPLETE
        logging.info(f"[Session {self.game_id}] Setup complete; board is ready for turn 1.")

    # ------------------------------------------------------------------
    # Main turn loop
    # ------------------------------------------------------------------

    async def run_turn_loop(self):
        """Alternates player turns: turn draw, recomputed action offers, End Turn."""
        self.game_phase = GamePhase.TURN_LOOP
        order = self._turn_order()
        if not order:
            return
        for _ in range(MAX_TURNS):
            active_id = order[self.turn_state.turn_number % len(order)]
            await self._begin_turn(active_id)
            await self._run_player_turn(active_id)
            await self._run_pokemon_checkup(active_id)
        logging.error(
            f"[Session {self.game_id}] MAX_TURNS ({MAX_TURNS}) reached; "
            f"stopping the turn loop."
        )

    async def _begin_turn(self, active_id: str):
        """Advances the turn counter, announces the active player, and draws."""
        # Last turn's stat-modifier PiPs (Power Tablet) expire with the turn.
        await self._clear_turn_visualizations()
        self.turn_state.begin_turn(active_id, self.board_state)
        player = self.players[active_id]
        logging.info(
            f"[Session {self.game_id}] Turn {self.turn_state.turn_number} "
            f"begins for {player.screen_name}."
        )

        drawn = self.board_state.draw_cards(active_id, 1)
        if not drawn:
            # Failing the mandatory turn draw loses the game (deck out).
            await self.end_game(
                self._opponent_id(active_id),
                f"{player.screen_name} has no cards left to draw",
            )
        self.turn_state.turn_draw_entity_ids.update(d["entity_id"] for d in drawn)
        announce = self._build_msg(
            OutboundMsg.ACTIVE_PLAYER_SET.value,
            {"gameID": self.game_id, "accountID": active_id},
        )
        await self.send_game_sequence(
            list(self.players.values()), GameSequence.ACTIVE_PLAYER_SET, [announce],
        )
        # Top-level Draw bracket (never nested inside ActivePlayerSet); the
        # move rides a nested GroupedMove so it animates FromDeck|ToHand
        # instead of the flip fan's default linear curve (no "Draw" path
        # table entry exists).
        if drawn:
            nested_moves = NestedSequence(GameSequence.GROUPED_MOVE, [
                self._entity_moved_msg(d["entity_id"], d["destination_id"], d["position"])
                for d in drawn
            ])
            intros = [self._entity_introduced_msg(d["card"]) for d in drawn]
            for pid, viewer in self.players.items():
                await self.send_game_sequence(
                    [viewer],
                    GameSequence.DRAW,
                    (intros + [nested_moves]) if pid == active_id else [nested_moves],
                )

    async def _run_player_turn(self, active_id: str):
        """Offers recomputed legal actions until the player ends their turn."""
        player = self.players[active_id]
        if isinstance(player, AIPlayer):
            # The AI takes no main-phase actions yet; it simply passes.
            logging.info(f"[Session {self.game_id}] {player.screen_name} (AI) ends turn.")
            return

        for _ in range(MAX_ACTIONS_PER_TURN):
            target_map = compute_legal_actions(
                self.board_state, self.turn_state, active_id, self.game_id
            )
            logging.info(
                f"[Session {self.game_id}] Offering {player.screen_name} "
                f"{len(target_map)} legal action(s) on turn "
                f"{self.turn_state.turn_number}."
            )
            offer = self._main_offer_value(active_id, target_map)
            reply = await self.prompt_selection_message(
                player,
                OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                offer,
                expected_counter=offer["counter"],
            )
            selection = reply.get("selection")
            if selection is None:
                logging.info(f"[Session {self.game_id}] {player.screen_name} ends turn.")
                return
            parsed = self._parse_action_reply(selection, target_map)
            if not parsed:
                continue
            entry, target_ids = parsed
            turn_over = await self._apply_player_action(active_id, entry, target_ids)
            if turn_over:
                return
        logging.warning(
            f"[Session {self.game_id}] {player.screen_name} hit the per-turn "
            f"action cap ({MAX_ACTIONS_PER_TURN}); forcing end of turn."
        )

    def _main_offer_value(
        self, player_id: str, target_map: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Builds the main-turn SelectionWithTargetsAndActionsRequired value."""
        return {
            "gameID": self.game_id,
            "counter": self._next_selection_counter(player_id),
            # No prompt: any DisplayText renders as a persistent banner
            # (CanShowPrompt); the turn announcement is ActivePlayerSet.
            "prompt": None,
            "offerLength": TURN_OFFER_LENGTH_MS,
            "startingTimestamp": int(time.time() * 1000),
            "forced": False,
            "targetType": TARGET_TYPE_MAIN_TURN,
            "ignoreFirst": False,
            "selectionParams": {},
            "optimalPlayMap": [],
            "sourceID": None,
            "targetMap": target_map,
        }

    def _parse_action_reply(
        self,
        selection: Any,
        target_map: List[Dict[str, Any]],
    ) -> Optional[tuple]:
        """Validates a reply ([[entityID, actionID], [targetResponses]]) against
        the offer; returns (target_map_entry, target_ids) or None to re-offer."""
        if not isinstance(selection, (list, tuple)) or not selection:
            logging.warning(f"[Session {self.game_id}] Malformed action reply: {selection}")
            return None
        head = selection[0]
        if not isinstance(head, (list, tuple)) or len(head) < 2:
            logging.warning(f"[Session {self.game_id}] Malformed action head: {head}")
            return None
        entity_id, action_id = head[0], head[1]
        entry = next(
            (
                e for e in target_map
                if e["entityID"] == entity_id
                and e["selectableAction"]["actionID"] == action_id
            ),
            None,
        )
        if entry is None:
            logging.warning(
                f"[Session {self.game_id}] Reply picked non-offered action "
                f"{action_id} on {entity_id}; re-offering."
            )
            return None
        target_ids: List[str] = []
        if len(selection) > 1 and isinstance(selection[1], (list, tuple)):
            for response in selection[1]:
                if isinstance(response, dict):
                    target_ids.extend(response.get("entityList") or [])
        return entry, target_ids

    def _validated_target(
        self, entry: Dict[str, Any], target_ids: List[str]
    ) -> Optional[str]:
        """First replied target that the offer actually declared valid."""
        infos = entry.get("targetInfoLst") or []
        valid = set(infos[0].get("validTargets") or []) if infos else set()
        for target_id in target_ids:
            if target_id in valid:
                return target_id
        return None

    async def _apply_player_action(
        self,
        player_id: str,
        entry: Dict[str, Any],
        target_ids: List[str],
    ) -> bool:
        """Executes a validated action. Returns True if the turn is over."""
        card = self.board_state.get_entity(entry["entityID"])
        if card is None:
            logging.warning(
                f"[Session {self.game_id}] Action on unknown entity "
                f"{entry['entityID']}; re-offering."
            )
            return False
        description = entry["selectableAction"]["description"]
        if description == ACTION_PLAY_POKEMON:
            await self._execute_play_basic(player_id, card)
        elif description == ACTION_PLAY_ENERGY:
            await self._execute_attach_energy(player_id, card, entry, target_ids)
        elif description == ACTION_ATTACH_TOOL:
            await self._execute_attach_tool(player_id, card, entry, target_ids)
        elif description == ACTION_EVOLVE:
            await self._execute_evolve(player_id, card, entry, target_ids)
        elif description == ACTION_USE_TRAINER:
            return await self._execute_play_trainer(player_id, card)
        elif description == ACTION_PLAY_STADIUM:
            await self._execute_play_stadium(player_id, card)
        elif description == ACTION_USE_ABILITY:
            return await self._execute_use_ability(player_id, card, entry)
        elif description == ACTION_USE_ATTACK:
            return await self._execute_attack(player_id, card, entry)
        elif description == ACTION_RETREAT:
            await self._execute_retreat(player_id, card, entry, target_ids)
        else:
            logging.warning(
                f"[Session {self.game_id}] No executor for action "
                f"'{description}'; ignoring."
            )
        return False

    async def _send_play_sequence(self, owner_id: str, sequence_name, moves, reveal_cards):
        """Broadcasts a play bracket, introducing the played cards to non-owners."""
        intros = [self._entity_introduced_msg(c) for c in reveal_cards]
        for pid, viewer in self.players.items():
            if pid == owner_id:
                await self.send_game_sequence([viewer], sequence_name, moves)
                continue
            # Intros ride their own bracket: play executors pick the move
            # animation (l.a) from the card's TYPE before any command in
            # their bracket executes, so attrs must already be applied.
            await self.send_game_sequence(
                [viewer], GameSequence.SERIAL_SEQUENCE, intros
            )
            await self.send_game_sequence([viewer], sequence_name, moves)

    async def _execute_play_basic(self, player_id: str, card):
        """Plays a Basic Pokemon from hand onto the bench."""
        bench_area = self.board_state.find_player_area(player_id, "bench")
        if not bench_area or len(bench_area.children) >= \
                effective_bench_capacity(self.board_state, player_id):
            logging.warning(f"[Session {self.game_id}] Bench unavailable; re-offering.")
            return
        # Lowest free SLOT, not list length: the client never renumbers bench
        # slots, so a promoted/KO'd Pokemon leaves a gap new arrivals must fill.
        position = self.board_state.free_bench_slot(player_id)
        if not self.board_state.move_card(card.entity_id, bench_area.entity_id):
            return
        self.turn_state.mark_entered_play(card.entity_id)
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"benched {card.entity_id}."
        )
        await self._send_play_sequence(
            player_id,
            GameSequence.PLAY_CARD,
            [self._entity_moved_msg(card.entity_id, bench_area.entity_id, position)],
            [card],
        )
        await self._fire_triggered_abilities(player_id, card, Triggers.ON_PLAY)

    async def _fire_triggered_abilities(self, player_id: str, card, trigger: str,
                                        ctx_setup=None):
        """Runs a Pokemon's abilities matching `trigger` (on-play, on-evolve,
        on-knocked-out, between-turns); resolve_knockouts already flushed any
        knockouts the effect caused, so the extra call here is empty-safe."""
        for entry in card.get_attribute(AttrID.PIE_ABILITIES) or []:
            if not isinstance(entry, dict):
                continue
            ability_id = entry.get("abilityID")
            ability = ABILITIES_BY_ID.get(ability_id) if ability_id else None
            if ability is not None and ability.has_trigger(trigger):
                # "1 per turn" abilities shared by name across copies (Dark Asset).
                if ability.shared_once_per_turn \
                        and ability.shared_once_per_turn in self.turn_state.used_named_abilities:
                    continue
                trigger_ctx = await resolve_triggered_ability(
                    self, player_id, card, ability, ctx_setup=ctx_setup)
                # Only a resolved effect (not a declined "you may") consumes the
                # shared-name turn limit.
                if ability.shared_once_per_turn and trigger_ctx is not None \
                        and trigger_ctx._messages:
                    self.turn_state.used_named_abilities.add(ability.shared_once_per_turn)
                if trigger_ctx is not None and trigger_ctx.knockouts:
                    await self.resolve_knockouts(trigger_ctx)

    async def fire_energy_attached_triggers(self, attaching_player_id: str,
                                            energy, receiver):
        """ON_ENERGY_ATTACHED for every in-play Pokemon on BOTH sides
        (Arctozolt observes the opponent's attach); the trigger ctx carries
        attaching_player_id / attached_energy / energy_receiver."""
        def _setup(c):
            c.attaching_player_id = attaching_player_id
            c.attached_energy = energy
            c.energy_receiver = receiver
        for pid in self._turn_order():
            for pokemon in list(self.board_state.pokemon_in_play(pid)):
                await self._fire_triggered_abilities(
                    pid, pokemon, Triggers.ON_ENERGY_ATTACHED, ctx_setup=_setup)

    async def fire_move_to_active_triggers(self, pokemon):
        """ON_MOVE_TO_ACTIVE (Cinderace Libero), at most once per entity per
        turn regardless of how often it re-enters the Active spot."""
        if pokemon is None:
            return
        ts = self.turn_state
        if pokemon.entity_id in ts.on_move_to_active_fired:
            return
        ts.on_move_to_active_fired.add(pokemon.entity_id)
        owner_id = pokemon.owning_player_id
        if owner_id:
            await self._fire_triggered_abilities(
                owner_id, pokemon, Triggers.ON_MOVE_TO_ACTIVE)

    async def _execute_attach_energy(self, player_id, card, entry, target_ids):
        """Attaches an energy card underneath the chosen Pokemon, honoring the
        definition's attach hooks (cost, restrictions, on-attach effects)."""
        target_id = self._validated_target(entry, target_ids)
        if not target_id:
            logging.warning(
                f"[Session {self.game_id}] Energy attach without a valid "
                f"target ({target_ids}); re-offering."
            )
            return
        target = self.board_state.get_entity(target_id)
        if target is None:
            return
        definition = def_for(card.archetype_id)
        if definition is not None and getattr(definition, "attach_to", None) \
                and not definition.attach_to(target):
            logging.warning(
                f"[Session {self.game_id}] Energy {card.entity_id} may not "
                f"attach to {target_id}; re-offering."
            )
            return

        # Attach cost (e.g. Aurora's discard) resolves first; declining the
        # cost cancels the attach and the action re-offers.
        cost_ctx = await resolve_energy_attach_cost(self, player_id, card, target)
        if cost_ctx is None:
            logging.info(
                f"[Session {self.game_id}] Attach cost declined for "
                f"{card.entity_id}; attach cancelled."
            )
            return
        await self._flush_effect_runs(cost_ctx, GameSequence.GROUPED_MOVE.value)

        max_before = effective_max_hp(self.board_state, target)
        position = len(target.children)
        if not self.board_state.attach_card(card.entity_id, target_id):
            return
        self.turn_state.energy_attached = True
        self.stat_add(player_id, "energyplayed")
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"attached energy {card.entity_id} to {target_id}."
        )
        # PlayCard (not PlayEnergy): only executors that WrapSequence get the
        # l.a attach animation; the PlayEnergy executor runs moves raw.
        # No reveal: l.a animates hand->pokemon directly (center-origin is
        # only for cards played from hidden zones like the deck).
        await self._send_play_sequence(
            player_id,
            GameSequence.PLAY_CARD,
            [self._entity_moved_msg(card.entity_id, target_id, position)],
            [card],
        )
        await self._refresh_max_hp(target, max_before)

        attach_ctx = await resolve_energy_on_attach(self, player_id, card, target)
        if attach_ctx is not None:
            await self._flush_effect_runs(attach_ctx)
            await self.resolve_knockouts(attach_ctx)
        # A manual attach from hand is what ON_ENERGY_ATTACHED observes.
        await self.fire_energy_attached_triggers(player_id, card, target)

    async def _refresh_max_hp(self, pokemon, max_before: int):
        """Re-broadcasts HP after a stack change shifted a max-HP bonus
        (e.g. Heat Fire Energy's +20): damage taken stays constant."""
        max_after = effective_max_hp(self.board_state, pokemon)
        delta = max_after - max_before
        if delta == 0:
            return
        current = pokemon.get_attribute(AttrID.HP, 0) + delta
        pokemon.set_attribute(AttrID.HP, max(0, current))
        envelope = self._sequence_envelope(
            EMPTY_SEQUENCE_ID,
            self._build_msg(
                OutboundMsg.ATTRIBUTE_MODIFIED.value,
                {
                    "gameID": self.game_id,
                    "entityID": pokemon.entity_id,
                    "attribute": {
                        "name": AttrID.HP.value,
                        "value": max(0, current),
                        "originalValue": max_after,
                        "modValue": None,
                    },
                },
            ),
        )
        await self.broadcast_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)
        if current <= 0:
            ctx = EffectContext(self, pokemon.owning_player_id or "", pokemon, None)
            ctx.knockouts.append(pokemon)
            await self.resolve_knockouts(ctx)

    async def _broadcast_entity_attribute(self, entity, attr: AttrID, value: Any):
        """Sets `attr` on `entity` and broadcasts a standalone AttributeModified
        to both viewers; the client re-renders on the version bump."""
        entity.set_attribute(attr, value)
        envelope = self._sequence_envelope(
            EMPTY_SEQUENCE_ID,
            self._build_msg(
                OutboundMsg.ATTRIBUTE_MODIFIED.value,
                {
                    "gameID": self.game_id,
                    "entityID": entity.entity_id,
                    "attribute": {
                        "name": attr.value,
                        "value": value,
                        "originalValue": value,
                        "modValue": None,
                    },
                },
            ),
        )
        await self.broadcast_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)

    def _pie_ability_entries(self, pokemon: PokemonEntity) -> List[Dict[str, Any]]:
        """`pokemon`'s canonical PIE_ABILITIES: printed entries plus every
        currently attached tool's granted_abilities (Forest Seal Stone)."""
        definition = def_for(pokemon.archetype_id)
        entries = [a.to_dict() for a in (getattr(definition, "abilities", None) or [])]
        for child in pokemon.children:
            tool_def = def_for(child.archetype_id)
            for granted in (getattr(tool_def, "granted_abilities", None) or []):
                entries.append(granted.to_dict())
        return entries

    async def refresh_granted_abilities(self, pokemon: PokemonEntity):
        """Rebroadcasts `pokemon`'s canonical PIE_ABILITIES (also sheds any
        injected copy-attack rows)."""
        await self._broadcast_entity_attribute(
            pokemon, AttrID.PIE_ABILITIES, self._pie_ability_entries(pokemon)
        )

    async def add_turn_stat_visualization(
        self, pokemon: PokemonEntity, arrow: str, display_type: str,
        source_name: str, card_text: Optional[str] = None,
    ):
        """Adds a stat-modifier PiP (attr 200370) to `pokemon` for the rest of
        the turn (Power Tablet's damage boost). arrow: "Positive" (green up) /
        "Negative" (red down); display_type: a VisualizationTypes member name
        (must be non-null -- s.F derefs .Value unguarded)."""
        viz: Dict[str, Any] = {
            "displayType": display_type,
            "arrow": arrow,
            "sourceName": {"id": source_name},
        }
        if card_text:
            viz["cardText"] = {"id": card_text}
        current = list(pokemon.get_attribute(AttrID.SPECIAL_VISUALIZATIONS) or [])
        current.append(viz)
        self._turn_visualizations.setdefault(pokemon.entity_id, []).append(viz)
        await self._broadcast_entity_attribute(
            pokemon, AttrID.SPECIAL_VISUALIZATIONS, current
        )

    async def _clear_turn_visualizations(self):
        """Removes this turn's stat-modifier PiPs (Power Tablet expires)."""
        for entity_id, added in list(self._turn_visualizations.items()):
            entity = self.board_state.get_entity(entity_id)
            if entity is None:
                continue
            remaining = [
                v for v in (entity.get_attribute(AttrID.SPECIAL_VISUALIZATIONS) or [])
                if v not in added
            ]
            await self._broadcast_entity_attribute(
                entity, AttrID.SPECIAL_VISUALIZATIONS, remaining
            )
        self._turn_visualizations = {}

    def _clear_entity_visualizations_msg(self, entity) -> Optional[Dict[str, Any]]:
        """Drops `entity`'s turn-scoped stat-modifier PiPs (it left play, e.g.
        was knocked out -- the client keeps rendering attr 200370 on discarded
        cards) and returns the AttributeModified to ride its leave-play bracket,
        or None. Retreat/switch keep the PiP: the buff still applies on the
        bench, so those callers do NOT invoke this."""
        added = self._turn_visualizations.pop(entity.entity_id, None)
        if not added:
            return None
        remaining = [
            v for v in (entity.get_attribute(AttrID.SPECIAL_VISUALIZATIONS) or [])
            if v not in added
        ]
        entity.set_attribute(AttrID.SPECIAL_VISUALIZATIONS, remaining)
        return self._build_msg(
            OutboundMsg.ATTRIBUTE_MODIFIED.value,
            {
                "gameID": self.game_id,
                "entityID": entity.entity_id,
                "attribute": {
                    "name": AttrID.SPECIAL_VISUALIZATIONS.value,
                    "value": remaining,
                    "originalValue": remaining,
                    "modValue": None,
                },
            },
        )

    async def _prompt_ability_panel(
        self, player_id: str, source: BoardEntity,
        titles: List[Dict[str, Any]], choices: List[Dict[str, Any]],
        prompt: Optional[str], count: int,
    ) -> Optional[int]:
        """Floating-ability-panel TEXT-button flow (client command R.U):
        `titles`/`choices` are the per-button name/body lines."""
        node = {
            "name": "CustomChoiceAsAbilitySelectTargetInformation",
            "selected": True,
            "targetPrompt": {"id": prompt or ""},
            "sortType": None,
            "titles": titles,
            "choices": choices,
        }
        return await self._send_panel_offer(player_id, source, node, count)

    async def _send_panel_offer(
        self, player_id: str, source: BoardEntity,
        node: Dict[str, Any], count: int,
    ) -> Optional[int]:
        """Sends a custom-choice panel node behind a FORCED ignoreFirst
        SelectionWithTargetsRequired: the root auto-selects `source` and the
        node's command opens the panel immediately. forced+ignoreFirst makes
        the node's mayCancel FALSE client-side -- the cancel shield stays
        disabled and every cancel path no-ops, so the pick cannot be backed
        out of. Reply rides an IntTargetResponse (`amount` = button index);
        returns the index in [0, count) or None if unresolved."""
        player = self.players[player_id]
        counter = self._next_selection_counter(player_id)
        offer = {
            "gameID": self.game_id,
            "counter": counter,
            "prompt": None,
            "offerLength": TURN_OFFER_LENGTH_MS,
            "startingTimestamp": int(time.time() * 1000),
            "forced": True,
            "targetType": node["name"],
            "ignoreFirst": True,
            "selectionParams": {},
            "optimalPlayMap": [],
            "sourceID": source.entity_id,
            "targetMap": {source.entity_id: [node]},
        }
        reply = await self.prompt_selection_message(
            player,
            OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
            offer,
            expected_counter=counter,
        )
        selection = reply.get("selection")
        responses = selection.get("targetResponses") or [] \
            if isinstance(selection, dict) else []
        for response in responses:
            if isinstance(response, dict):
                idx = response.get("amount")
                if isinstance(idx, int) and 0 <= idx < count:
                    return idx
        return None

    async def prompt_attack_selection(
        self, player_id: str, source: PokemonEntity,
        candidates: List[Any], prompt: Optional[str] = None,
    ) -> Optional[int]:
        """Presents `candidates` [(pokemon, attack)] as FULL attack rows (cost
        pips, damage, owner type) in the floating panel on `source`, returning
        the chosen index (None if unresolved). The forced offer makes the pick
        mandatory: once the copy attack is declared it cannot be cancelled."""
        player = self.players[player_id]
        if isinstance(player, AIPlayer) or not candidates:
            return 0 if candidates else None
        node = copy_attack_choice_node(
            source.entity_id, candidates, prompt or ""
        )
        return await self._send_panel_offer(
            player_id, source, node, len(candidates)
        )

    async def prompt_choice_panel(
        self, player_id: str, source: BoardEntity, options: List[str],
        prompt: Optional[str] = None, descriptions: Optional[List[str]] = None,
    ) -> int:
        """Presents a "Choose 1"-style menu as buttons in the floating ability
        panel on `source` (any card in play, e.g. a Supporter on activeTrainer),
        matching how the original client renders trainer option menus. Returns
        the chosen index (defaults to 0 for AI/unresolved)."""
        player = self.players[player_id]
        if isinstance(player, AIPlayer) or not options:
            return 0
        titles = [{"id": option} for option in options]
        bodies = descriptions if descriptions and len(descriptions) == len(options) \
            else [""] * len(options)
        choices = [{"id": body} for body in bodies]
        idx = await self._prompt_ability_panel(
            player_id, source, titles, choices, prompt, len(options)
        )
        return idx if idx is not None else 0

    async def _execute_attach_tool(self, player_id, card, entry, target_ids):
        """Attaches a Pokemon Tool underneath the chosen Pokemon (one each)."""
        target_id = self._validated_target(entry, target_ids)
        target = self.board_state.get_entity(target_id) if target_id else None
        if target is None or tool_slots_free(self.board_state, target) <= 0:
            logging.warning(
                f"[Session {self.game_id}] Tool attach without a valid "
                f"target ({target_ids}); re-offering."
            )
            return
        max_before = effective_max_hp(self.board_state, target)
        position = len(target.children)
        if not self.board_state.attach_card(card.entity_id, target_id):
            return
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"attached tool {card.entity_id} to {target_id}."
        )
        # PlayCard for the WrapSequence attach FX (the PlayTool executor is a
        # bare passthrough that plays moves raw).
        await self._send_play_sequence(
            player_id,
            GameSequence.PLAY_CARD,
            [self._entity_moved_msg(card.entity_id, target_id, position)],
            [card],
        )
        await self._refresh_max_hp(target, max_before)
        await self.refresh_granted_abilities(target)

    async def _execute_use_ability(self, player_id, card, entry) -> bool:
        """Activates a Pokemon's usable ability (once-per-turn / VSTAR).
        Returns True when the ability ends the turn (Ability.ends_turn)."""
        action_id = entry["selectableAction"]["actionID"]
        ability = ABILITIES_BY_ID.get(action_id)
        if ability is None:
            logging.warning(
                f"[Session {self.game_id}] Ability {action_id} on "
                f"{card.entity_id} has no registered definition; ignoring."
            )
            return False
        if ability.activation != Activations.UNLIMITED:
            self.turn_state.used_abilities.add((card.entity_id, action_id))
        if ability.shared_once_per_turn:
            self.turn_state.used_named_abilities.add(ability.shared_once_per_turn)
        if ability.vstar:
            self.turn_state.vstar_used.add(player_id)
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"uses ability '{ability.title}'."
        )
        ctx = await resolve_activated_ability(self, player_id, card, ability)
        return ctx is not None and ctx.ends_turn

    async def _execute_evolve(self, player_id, card, entry, target_ids):
        """Evolves the target: the evolution takes its slot, the old stack tucks underneath."""
        target_id = self._validated_target(entry, target_ids)
        target = self.board_state.get_entity(target_id) if target_id else None
        if not target or not target.parent:
            logging.warning(
                f"[Session {self.game_id}] Evolve without a valid target "
                f"({target_ids}); re-offering."
            )
            return
        await self.perform_evolution(player_id, card, target)

    async def perform_evolution(self, player_id, evolution_card, target,
                                from_zone_intro: bool = False) -> bool:
        """State + bracket core of an evolution (shared by the play executor
        and effect-driven evolution, which bypasses the may-evolve rules).

        from_zone_intro sends the evolution card's intro to the OWNER too
        (hidden-zone sources like the deck; the wrap-FX rule needs the card's
        attrs applied before the Evolve bracket on both viewers).
        """
        card = evolution_card
        area = target.parent if target is not None else None
        if not target or not area:
            return False

        slot = self.board_state.bench_slot_of(target)

        # Damage counters carry through evolution: capture what the
        # pre-evolution had taken (before attachments move off it) so it can be
        # transferred onto the evolution card, which otherwise enters at full HP.
        damage_taken = max(
            0, effective_max_hp(self.board_state, target) - target.get_attribute(AttrID.HP, 0)
        )

        moves = []
        if not self.board_state.move_card(card.entity_id, area.entity_id, slot):
            return False
        moves.append(self._entity_moved_msg(card.entity_id, area.entity_id, slot))

        # Re-nest pre-existing attachments, then the pre-evolution card itself.
        for attachment in list(target.children):
            position = len(card.children)
            self.board_state.attach_card(attachment.entity_id, card.entity_id)
            moves.append(self._entity_moved_msg(attachment.entity_id, card.entity_id, position))
        position = len(card.children)
        self.board_state.attach_card(target.entity_id, card.entity_id)
        moves.append(self._entity_moved_msg(target.entity_id, card.entity_id, position))

        # The counters now live on the evolution; clear the tucked-under
        # pre-evolution's HP so its stale damage isn't re-rendered on inspect.
        self.reset_pokemon_damage(target)
        if damage_taken:
            card.set_attribute(
                AttrID.HP,
                max(0, effective_max_hp(self.board_state, card) - damage_taken),
            )

        # The Evolve executor (M.k) plays the spin FX itself; its ctor requires
        # the "From"/"Into" data effects and crashes without them.
        data_effects = [
            self._entity_id_data_effect_msg("From", target.entity_id),
            self._entity_id_data_effect_msg("Into", card.entity_id),
        ]
        if from_zone_intro:
            # Deck-sourced evolution: the owner is blind too, so their intro
            # rides its own SerialSequence bracket before the Evolve bracket.
            owner_viewer = self.players.get(player_id)
            if owner_viewer is not None:
                await self.send_game_sequence(
                    [owner_viewer], GameSequence.SERIAL_SEQUENCE,
                    [self._entity_introduced_msg(card)],
                )
        await self._send_play_sequence(
            player_id, GameSequence.EVOLVE, data_effects + moves, [card]
        )

        # Push the transferred damage so the evolution renders its HP tracker.
        if damage_taken:
            envelope = self._sequence_envelope(
                EMPTY_SEQUENCE_ID, self._hp_attribute_msg(card)
            )
            await self.broadcast_packet(OutboundMsg.SEQUENCE_MESSAGE.value, envelope)

        # Freshly entered play: cannot evolve again this turn.
        self.turn_state.mark_entered_play(card.entity_id)
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"evolved {target.entity_id} into {card.entity_id}."
        )

        # needs live client verification: condition marker clears on evolve
        if self.clear_pokemon_effects(target):
            await self.send_game_sequence(
                list(self.players.values()), GameSequence.REMOVE_SPECIAL_CONDITION,
                [self._entity_id_data_effect_msg("Target", target.entity_id),
                 self._condition_attr_msg(target)],
            )

        await self._fire_triggered_abilities(player_id, card, Triggers.ON_EVOLVE)
        return True

    async def _execute_play_trainer(self, player_id, card) -> bool:
        """Plays an Item/Supporter: revealed onto activeTrainer, effect resolves,
        then discarded. Returns True when the effect ended the turn (Rotom Bike)."""
        trainer_area = self.board_state.find_global_area("activeTrainer")
        discard_area = self.board_state.find_player_area(player_id, "discard")
        if not trainer_area or not discard_area:
            return False
        if not self.board_state.move_card(card.entity_id, trainer_area.entity_id):
            return False
        card.owning_player_id = player_id  # global area move clears the owner
        if card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value:
            self.turn_state.supporter_played = True
        self._record_trainer_played(card)
        self.stat_add(player_id, "trainersplayed")

        # Stale attack sources make k.z skip the reveal suppression
        # (isRevealDuringAttack) and double-present the card.
        await self._broadcast_attack_sources([])

        # Placement: owner gets TrainerCard (l.c instant-confirms the local
        # drag); non-owners get PlayCard — TrainerCard's l.c wrap hides the
        # ->activeTrainer move from k.z's reveal scan, and only a plain move
        # lets the delegation present the card large before it flies into
        # the slot, where it sits while the effect resolves.
        place = self._entity_moved_msg(card.entity_id, trainer_area.entity_id, 0)
        intros = [self._entity_introduced_msg(card)]
        reveal = self._reveal_card_msg(card.entity_id, True)
        for pid, viewer in self.players.items():
            if pid == player_id:
                await self.send_game_sequence([viewer], GameSequence.TRAINER_CARD, [place])
            else:
                await self.send_game_sequence([viewer], GameSequence.SERIAL_SEQUENCE, intros)
                await self.send_game_sequence([viewer], GameSequence.PLAY_CARD, [reveal, place])

        # Effect dialogs run after placement so both viewers see the card on
        # the trainer slot while the player decides.
        ctx = await resolve_trainer_effect(self, player_id, card)
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"played trainer {card.entity_id}."
        )

        if ctx is not None:
            # Effect messages flush as bracket runs; draws carry their own
            # Draw brackets (m.c plays the staggered card-draw fan), anything
            # untagged rides a plain GroupedMove.
            await self._flush_effect_runs(ctx)

        # Normally the trainer discards after resolving; skip when the effect
        # relocated it elsewhere (Hisuian Heavy Ball swaps itself into prizes).
        if card.parent is trainer_area:
            position = len(discard_area.children)
            self.board_state.move_card(card.entity_id, discard_area.entity_id)
            discard = self._entity_moved_msg(card.entity_id, discard_area.entity_id, position)
            await self.send_game_sequence(
                list(self.players.values()), GameSequence.TRAINER_CARD, [discard]
            )
        if ctx is not None:
            await self.resolve_knockouts(ctx)
            # Effects that vacated the Active spot (Scoop Up Net) promote after
            # the choreography flushes.
            for hook in ctx.deferred_actions:
                await hook()
        return ctx is not None and ctx.ends_turn

    def _record_trainer_played(self, card):
        """Stamps the trainer into this turn's history ledger."""
        name = card.get_attribute(AttrID.NAME)
        name = name.get("id", "") if isinstance(name, dict) else (name or "")
        display = getattr(def_for(card.archetype_id), "display_name", None) or name
        self.turn_state.trainers_played.append(
            (card.archetype_id, display, card.get_attribute(AttrID.TRAINER_TYPE))
        )

    async def _execute_play_stadium(self, player_id, card):
        """Plays a Stadium: the previous one goes to its owner's discard."""
        stadium_area = self.board_state.find_global_area("activeStadium")
        if not stadium_area:
            return
        moves = []
        for existing in list(stadium_area.children):
            owner_id = existing.owning_player_id or player_id
            owner_discard = self.board_state.find_player_area(owner_id, "discard")
            if owner_discard:
                position = len(owner_discard.children)
                self.board_state.move_card(existing.entity_id, owner_discard.entity_id)
                moves.append(self._entity_moved_msg(
                    existing.entity_id, owner_discard.entity_id, position
                ))
        position = len(stadium_area.children)
        if not self.board_state.move_card(card.entity_id, stadium_area.entity_id):
            return
        # Keep the owner so the next stadium can route this one to the right discard.
        card.owning_player_id = player_id
        self._record_trainer_played(card)
        self.stat_add(player_id, "trainersplayed")
        moves.append(self._entity_moved_msg(card.entity_id, stadium_area.entity_id, position))
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"played stadium {card.entity_id} (effect pending effects API)."
        )
        await self._send_play_sequence(player_id, GameSequence.STADIUM_PRESENT, moves, [card])

    async def _execute_retreat(self, player_id, card, entry, target_ids):
        """Retreats the Active: pays the cost to discard, swaps with a benched Pokemon."""
        bench_area = self.board_state.find_player_area(player_id, "bench")
        active_area = self.board_state.find_player_area(player_id, "activePokemonArea")
        discard_area = self.board_state.find_player_area(player_id, "discard")
        if not bench_area or not active_area or not discard_area:
            return

        valid_by_kind = {
            info.get("name"): set(info.get("validTargets") or [])
            for info in (entry.get("targetInfoLst") or [])
        }
        cost_valid = valid_by_kind.get(SelectionKind.RETREAT_COST_ENTITY_LIST.value, set())
        new_active_valid = valid_by_kind.get(SelectionKind.RETREAT_NEW_ACTIVE.value, set())
        discard_ids = [t for t in target_ids if t in cost_valid]
        new_active_id = next((t for t in target_ids if t in new_active_valid), None)
        new_active = self.board_state.get_entity(new_active_id) if new_active_id else None
        if new_active is None or new_active.parent is not bench_area:
            logging.warning(
                f"[Session {self.game_id}] Retreat without a valid new Active "
                f"({target_ids}); re-offering."
            )
            return

        cost = effective_retreat_cost(self.board_state, card)
        energies = [
            e for e in (self.board_state.get_entity(eid) for eid in discard_ids)
            if isinstance(e, EnergyEntity)
        ]
        paid = sum(energy_provided_count(e, self.board_state) for e in energies)
        if paid < cost:
            logging.warning(
                f"[Session {self.game_id}] Retreat cost {cost} underpaid "
                f"({paid}) by {discard_ids}; re-offering."
            )
            return

        # The Retreat executor (N.P) requires the Retreating/NewActive data
        # effects, applies both Pokemon moves data-only (it plays the swap
        # animations itself), and WrapSequences the energy discards.
        messages = [
            self._entity_id_data_effect_msg("Retreating", card.entity_id),
            self._entity_id_data_effect_msg("NewActive", new_active.entity_id),
        ]
        for eid in discard_ids:
            position = len(discard_area.children)
            if self.board_state.move_card(eid, discard_area.entity_id):
                messages.append(self._entity_moved_msg(eid, discard_area.entity_id, position))
        # The old active takes the new active's rendered SLOT (client stamp),
        # captured before the active move overwrites new_active's stamp with 0.
        slot = self.board_state.bench_slot_of(new_active)
        self.board_state.move_card(new_active.entity_id, active_area.entity_id)
        messages.append(self._entity_moved_msg(new_active.entity_id, active_area.entity_id, 0))
        self.board_state.move_card(card.entity_id, bench_area.entity_id, slot)
        messages.append(self._entity_moved_msg(card.entity_id, bench_area.entity_id, slot))

        self.turn_state.retreated = True
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"retreated {card.entity_id} for {new_active.entity_id} "
            f"(discarded {len(discard_ids)} energy)."
        )
        await self.send_game_sequence(
            list(self.players.values()), GameSequence.RETREAT, messages
        )

        # All effects (Special Conditions, attack locks) end when a Pokemon
        # leaves the Active spot; a separate follow-up bracket is the safe
        # pattern here (the Retreat executor's non-move handling is unverified).
        if self.clear_pokemon_effects(card):
            await self.send_game_sequence(
                list(self.players.values()), GameSequence.REMOVE_SPECIAL_CONDITION,
                [self._entity_id_data_effect_msg("Target", card.entity_id),
                 self._condition_attr_msg(card)],
            )
        # History stamps AFTER the effect clear (it prunes entity-keyed maps).
        self.turn_state.retreated_entities.add(card.entity_id)
        self.turn_state.became_active_turn[new_active.entity_id] = \
            self.turn_state.turn_number
        await self.fire_move_to_active_triggers(new_active)

    async def _execute_attack(self, player_id, card, entry) -> bool:
        """Resolves an attack through the effect engine; attacking ends the turn."""
        action_id = entry["selectableAction"]["actionID"]
        ability = ABILITIES_BY_ID.get(action_id)
        if ability is None:
            logging.warning(
                f"[Session {self.game_id}] Attack {action_id} on {card.entity_id} "
                f"has no registered definition; resolving with no effect."
            )
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"attacks with '{ability.title if ability else action_id}'."
        )
        # Confusion flip FIRST: a failed attack never happened for VSTAR
        # usage or "can't use next turn" locks (compendium ruling).
        conditions = card.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED] in conditions:
            if not await self._resolve_confusion_flip(player_id, card):
                return True  # tails: the attack fizzles, but the turn still ends

        if ability is not None:
            if getattr(ability, "locks_next_turn", False):
                self.turn_state.lock_attack(card.entity_id, action_id)
            if ability.vstar:
                self.turn_state.vstar_used.add(player_id)

        await resolve_attack(self, player_id, card, ability, action_id)
        # Effects like Aqua Return can remove the attacker itself from play.
        for pid in list(self.players.keys()):
            if self.board_state.active_pokemon(pid) is None \
                    and not await self._promote_new_active(pid):
                await self.end_game(
                    self._opponent_id(pid),
                    f"{self.players[pid].screen_name} has no Pokémon left",
                )
        return True

    async def _resolve_confusion_flip(self, player_id: str, attacker) -> bool:
        """Confused Pokemon flip before attacking: heads proceeds into the
        normal attack; tails hurts the attacker for 30 raw damage instead."""
        flip = random.choice([0, 1])
        heads = flip == 0
        self.stat_add(player_id, "headsflipped", 1 if heads else 0)
        self.stat_add(player_id, "tailsflipped", 0 if heads else 1)
        await self.send_game_sequence(
            list(self.players.values()), GameSequence.FLIP_FOR_CONFUSION,
            [self._build_msg(
                OutboundMsg.MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT.value,
                {
                    "gameID": self.game_id,
                    "resultLst": [flip],
                    "title": {"id": TEXT_CONFUSION_CHECK},
                    "gameText": {"id": TEXT_CONFUSION_PROCEEDS if heads else TEXT_CONFUSION_HURT},
                    "source": attacker.entity_id,
                    "targets": [attacker.entity_id],
                },
            )],
        )
        # needs live client verification: confusion-heads pulled-out card tuck
        await self.choreo_pause(3.0)
        if heads:
            return True
        knocked_out = await self._apply_raw_damage(
            attacker, 30, GameSequence.HURT_FROM_CONFUSION.value
        )
        if knocked_out:
            await self._resolve_raw_knockout(attacker)
        return False

    async def _run_active_placement(self, player_id: str, done_players: set):
        """Drives one player's required Active Pokemon pick.

        The offer itself is sent with forced=false (a forced bare root
        selection would label the Next button "End Turn"), and the
        PauseOnPromptEffect override hides the button entirely; a premature
        Done/skip reply (selection=null) is simply re-offered.
        """
        player = self.players[player_id]
        board = self.board_state
        active_area = board.find_player_area(player_id, "activePokemonArea")
        if not active_area:
            logging.error(f"[Session {self.game_id}] Missing active area for {player_id}.")
            return

        try:
            if isinstance(player, AIPlayer):
                basics = board.basic_pokemon_in_hand(player_id)
                if basics:
                    await self._place_setup_card(player_id, basics[0].entity_id, active_area)
                return

            await self._send_pause_prompt(player, PROMPT_CHOOSE_ACTIVE)
            for _ in range(MAX_SELECTION_RETRIES):
                if active_area.children:
                    break
                basics = board.basic_pokemon_in_hand(player_id)
                if not basics:
                    logging.error(
                        f"[Session {self.game_id}] {player.screen_name} has no Basic "
                        f"to place as Active; skipping placement."
                    )
                    break
                offer = self._placement_offer_value(
                    player_id, PROMPT_CHOOSE_ACTIVE, basics, TARGET_TYPE_ACTIVE
                )
                reply = await self.prompt_selection_message(
                    player,
                    OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                    offer,
                    expected_counter=offer["counter"],
                )
                picked = self._parse_placement_reply(reply, basics)
                if picked:
                    await self._place_setup_card(player_id, picked, active_area)
        finally:
            done_players.add(player_id)

        # Swap the "choose" prompt for the waiting prompt (or clear it if the
        # opponent already finished -- run_placement_phase closes the rest).
        if isinstance(player, NetworkPlayer):
            if self._opponent_id(player_id) in done_players:
                await self._send_close_pause_prompt(player)
            else:
                await self._send_pause_prompt(player, PROMPT_WAIT_OPPONENT_ACTIVE)

    async def _run_bench_placement(self, player_id: str, done_players: set):
        """Drives one player's optional Bench picks: one offer per placement,
        ended by Done (selection=null) or a full bench. Never auto-ended on an
        empty hand -- instant skips would leak that no Basics remain."""
        player = self.players[player_id]
        board = self.board_state
        bench_area = board.find_player_area(player_id, "bench")
        if not bench_area:
            logging.error(f"[Session {self.game_id}] Missing bench area for {player_id}.")
            return

        try:
            if isinstance(player, AIPlayer):
                for card in board.basic_pokemon_in_hand(player_id)[:BENCH_CAPACITY]:
                    await self._place_setup_card(player_id, card.entity_id, bench_area)
                return

            for _ in range(MAX_SELECTION_RETRIES):
                if len(bench_area.children) >= BENCH_CAPACITY:
                    logging.info(f"[Session {self.game_id}] {player.screen_name}'s bench is full.")
                    break
                basics = board.basic_pokemon_in_hand(player_id)
                logging.info(
                    f"[Session {self.game_id}] Offering {player.screen_name} a bench "
                    f"placement ({len(basics)} Basics in hand)."
                )
                offer = self._placement_offer_value(
                    player_id, PROMPT_CHOOSE_BENCH, basics, TARGET_TYPE_BENCH
                )
                reply = await self.prompt_selection_message(
                    player,
                    OutboundMsg.SELECTION_WITH_TARGETS_REQUIRED.value,
                    offer,
                    expected_counter=offer["counter"],
                )
                if reply.get("selection") is None:
                    # Null-selection Advance ("Done" button) = finished placing.
                    logging.info(f"[Session {self.game_id}] {player.screen_name} is done benching.")
                    break
                picked = self._parse_placement_reply(reply, basics)
                if picked:
                    await self._place_setup_card(player_id, picked, bench_area)
        finally:
            done_players.add(player_id)

        if isinstance(player, NetworkPlayer):
            if self._opponent_id(player_id) in done_players:
                await self._send_close_pause_prompt(player)
            else:
                await self._send_pause_prompt(player, PROMPT_WAIT_OPPONENT_SETUP)

    def _placement_offer_value(
        self,
        player_id: str,
        prompt_text: str,
        basics: List[Any],
        target_type: str,
    ) -> Dict[str, Any]:
        """Builds a SelectionWithTargetsRequired value for setup placement."""
        return {
            "gameID": self.game_id,
            "counter": self._next_selection_counter(player_id),
            "prompt": {"id": prompt_text},
            "offerLength": 60000,
            "startingTimestamp": int(time.time() * 1000),
            "forced": False,
            "targetType": target_type,
            "ignoreFirst": False,
            "selectionParams": {},
            "optimalPlayMap": [],
            "sourceID": None,
            "targetMap": {card.entity_id: [] for card in basics},
        }

    def _parse_placement_reply(
        self,
        reply: Dict[str, Any],
        basics: List[Any],
    ) -> Optional[str]:
        """Extracts and validates the placed card entity ID from a
        SelectionWithTargets reply."""
        selection = reply.get("selection")
        if not selection:
            return None
        if isinstance(selection, dict):
            card_id = selection.get("entityID")
        else:
            logging.warning(f"[Session {self.game_id}] Malformed placement reply: {reply}")
            return None

        valid_ids = {card.entity_id for card in basics}
        if card_id not in valid_ids:
            logging.warning(
                f"[Session {self.game_id}] Placement reply picked non-offered "
                f"entity {card_id}; re-offering."
            )
            return None
        return card_id

    async def _place_setup_card(self, player_id: str, card_entity_id: str, area) -> bool:
        """Moves a setup card into an area and echoes it as an InitialPick bracket."""
        if area.get_attribute(AttrID.NAME) == "bench":
            position = self.board_state.free_bench_slot(player_id)
        else:
            position = len(area.children)
        if not self.board_state.move_card(card_entity_id, area.entity_id):
            logging.warning(
                f"[Session {self.game_id}] Could not move {card_entity_id} "
                f"into {area.get_attribute(AttrID.NAME)}."
            )
            return False
        logging.info(
            f"[Session {self.game_id}] {self.players[player_id].screen_name} "
            f"placed {card_entity_id} into {area.get_attribute(AttrID.NAME)}."
        )
        await self.send_game_sequence(
            list(self.players.values()),
            GameSequence.INITIAL_PICK,
            [self._entity_moved_msg(card_entity_id, area.entity_id, position)],
        )
        return True

    async def _introduce_initial_pokemon(self):
        """Reveals each player's placed Pokemon to their opponent (simultaneous flip)."""
        for player_id, player in self.players.items():
            opponent_id = self._opponent_id(player_id)
            introduces = []
            for area_name in ("activePokemonArea", "bench"):
                area = self.board_state.find_player_area(opponent_id, area_name)
                for card in (area.children if area else []):
                    introduces.append(self._entity_introduced_msg(card))
            if introduces:
                await self.send_game_sequence(
                    [player],
                    GameSequence.INTRODUCE_INITIAL_POKEMON,
                    introduces,
                )

    async def _deal_prize_cards(self):
        """Deals PRIZE_COUNT face-down prize cards per player in one parallel bracket.

        Deliberately NO EntityIntroduced here: prize cards are hidden
        knowledge for both players (including their owner), and deck cards
        are never introduced until drawn, so the moves render as backs.
        """
        nested_sequences = []
        for player_id in self._turn_order():
            dealt = self.board_state.deal_from_deck(player_id, "prizePile", PRIZE_COUNT)
            logging.info(
                f"[Session {self.game_id}] Dealt {len(dealt)} prize cards to "
                f"{self.players[player_id].screen_name}."
            )
            player_moves = [
                self._entity_moved_msg(d["entity_id"], d["destination_id"], d["position"])
                for d in dealt
            ]
            if player_moves:
                nested_sequences.append(
                    NestedSequence(GameSequence.GROUPED_MOVE, player_moves)
                )

        if nested_sequences:
            await self.send_game_sequence(
                list(self.players.values()),
                GameSequence.DEAL_INITIAL_PRIZE_CARDS,
                nested_sequences,
            )

    async def run_pregame_coin_flip(self):
        """Runs the pre-game coin flip and go-first selection."""
        # 1. Choose the coin toss caller randomly
        player_ids = list(self.players.keys())
        caller_id = random.choice(player_ids)
        opponent_id = next(pid for pid in player_ids if pid != caller_id)
        self.coin_flip_caller_id = caller_id
        caller = self.players[caller_id]
        opponent = self.players[opponent_id]
        logging.info(f"[Session {self.game_id}] Selected {caller.screen_name} to call the coin toss.")

        # 2. Show the "opponent is picking Heads or Tails" coin screen on the
        #    non-caller. The bracket is sent complete (Start + offer + Stop) so
        #    the pump renders it immediately instead of waiting on the caller.
        await self.send_game_sequence(
            [opponent],
            GameSequence.OPPONENT_PICKING_HEADS_OR_TAILS,
            [self._build_msg(
                OutboundMsg.CUSTOM_CHOICE_OFFER_MESSAGE.value,
                self._choice_offer_value(caller_id, [PROMPT_HEADS, PROMPT_TAILS]),
            )],
        )

        # If caller is AI, schedule simulated call
        if isinstance(caller, AIPlayer):
            self._spawn(self._simulate_ai_coin_flip_call(caller_id))

        # 3. Prompt the caller and wait for their Heads/Tails pick
        self.game_phase = GamePhase.COIN_FLIP_WAIT_CHOICE
        choice_data = await self.prompt_selection_message(
            caller,
            OutboundMsg.COIN_FLIP_CHOICE_REQUIRED.value,
            {
                "gameID": self.game_id,
                "counter": 1,
                "prompt": {"id": ""},
                "offerLength": 30000,
                "startingTimestamp": int(time.time() * 1000),
                "sortType": PROMPT_SORT_COIN,
                "buttons": [{"id": PROMPT_HEADS}, {"id": PROMPT_TAILS}],
                "sourceEntity": None,
            },
        )
        # GameCustomChoice carries the picked button index in "selection"
        # (see Outgoing.CustomChoice in the client core assembly).
        choice = choice_data.get("selection")

        # 4. Flip the coin and play the result animation on both clients. The.
        actual_result = random.choice([0, 1])
        self.stat_add(caller_id, "headsflipped" if actual_result == 0 else "tailsflipped")
        player_entity = self.board_state.find_player_entity(caller_id)
        caller_entity_id = player_entity.entity_id if player_entity else EMPTY_SEQUENCE_ID

        await self.send_game_sequence(
            list(self.players.values()),
            GameSequence.INITIAL_COIN_FLIP,
            [self._build_msg(
                OutboundMsg.MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT.value,
                {
                    "gameID": self.game_id,
                    "resultLst": [actual_result],
                    "title": {"id": TEXT_COIN_TOSS_RESULT},
                    "gameText": {"id": TEXT_TAILS_RESULT if actual_result == 1 else TEXT_HEADS_RESULT},
                    "source": caller_entity_id,
                    "targets": [caller_entity_id],
                },
            )],
        )

        # Determine toss winner (result 0 = Heads = left button)
        if choice == actual_result:
            winner_id = caller_id
        else:
            winner_id = next(pid for pid in player_ids if pid != caller_id)

        self.coin_flip_winner_id = winner_id
        winner = self.players[winner_id]
        loser = self.players[next(pid for pid in player_ids if pid != winner_id)]
        logging.info(
            f"[Session {self.game_id}] {caller.screen_name} called "
            f"{PROMPT_TAILS if choice == 1 else PROMPT_HEADS}, coin landed "
            f"{PROMPT_TAILS if actual_result == 1 else PROMPT_HEADS} -> "
            f"{winner.screen_name} won the coin toss."
        )

        # Let the flip animation render before the next dialog state
        await asyncio.sleep(3.0)

        # 5. Show the "opponent is choosing to go first" state on the loser and
        #    prompt the winner on their live coin screen.
        await self.send_game_sequence(
            [loser],
            GameSequence.OPPONENT_CHOOSING_TO_GO_FIRST,
            [self._build_msg(
                OutboundMsg.CUSTOM_CHOICE_OFFER_MESSAGE.value,
                self._choice_offer_value(winner_id, [PROMPT_YES, PROMPT_NO]),
            )],
        )

        if isinstance(winner, AIPlayer):
            self._spawn(self._simulate_ai_go_first_call(winner_id))

        self.game_phase = GamePhase.COIN_FLIP_WAIT_GO_FIRST
        go_first_data = await self.prompt_selection_message(
            winner,
            OutboundMsg.GO_FIRST_CHOICE_REQUIRED.value,
            {
                "gameID": self.game_id,
                "counter": 2,
                "prompt": {"id": ""},
                "offerLength": 30000,
                "startingTimestamp": int(time.time() * 1000),
                "sortType": PROMPT_SORT_GO_FIRST,
                "buttons": [{"id": PROMPT_YES}, {"id": PROMPT_NO}],
                "sourceEntity": None,
            },
        )
        go_first_choice = go_first_data.get("selection")

        # Determine active starting player (choice 0 = Yes = winner goes first)
        if go_first_choice == 0:
            first_player_id = winner_id
        else:
            first_player_id = next(pid for pid in player_ids if pid != winner_id)

        first_player = self.players[first_player_id]
        self.first_player_id = first_player_id
        logging.info(f"[Session {self.game_id}] {first_player.screen_name} will go first.")

        # 6. Announce the active player. The ActivePlayerSet sequence command
        #    (l.Z) also hides and deactivates the coin flip screen on both
        #    clients, so no explicit dismissal is needed.
        await self.send_game_sequence(
            list(self.players.values()),
            GameSequence.ACTIVE_PLAYER_SET,
            [self._build_msg(
                OutboundMsg.ACTIVE_PLAYER_SET.value,
                {"gameID": self.game_id, "accountID": first_player_id},
            )],
        )

        self.game_phase = GamePhase.MULLIGAN_PHASE

    async def _simulate_ai_coin_flip_call(self, account_id: str):
        await asyncio.sleep(1.5)
        choice = random.choice([0, 1])
        await self.receive_player_action(account_id, {"selection": choice, "counter": 1})

    async def _simulate_ai_go_first_call(self, account_id: str):
        await asyncio.sleep(1.5)
        await self.receive_player_action(account_id, {"selection": 0, "counter": 2})

    async def send_serialized_game_state(self, only_player_id: Optional[str] = None):
        """Builds and transmits the board layout tree wrapped in a SequenceMessage.

        With only_player_id set, sends to just that player (reconnect resync);
        otherwise to every distinct client (initial game start).
        """
        logging.info(f"[Session {self.game_id}] Building SerializedGameState via OOP BoardState.")
        if only_player_id is not None:
            recipients = [(only_player_id, self.players[only_player_id])]
        else:
            recipients = list(self._unique_recipients())
        for player_id, player in recipients:
            serialized_state = self.board_state.serialize(player_id)
            # The network router only strips the top-level messageName; the nested
            # envelope carries the class name in "name" instead.
            serialized_state.pop("messageName", None)
            payload = {
                "sequenceID": EMPTY_SEQUENCE_ID,
                "gameID": self.game_id,
                "msg": {
                    "name": OutboundMsg.SERIALIZED_GAME_STATE.value,
                    "value": serialized_state,
                },
            }
            await player.send_packet(OutboundMsg.SEQUENCE_MESSAGE.value, payload)


def _stack_descendants(entity) -> List[Any]:
    """Every entity attached under a Pokemon, depth-first."""
    out: List[Any] = []
    for child in entity.children:
        out.append(child)
        out.extend(_stack_descendants(child))
    return out
