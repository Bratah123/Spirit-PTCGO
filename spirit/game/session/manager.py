import logging
import uuid
import asyncio

from typing import Dict, List, Any, Optional
from spirit.network.message_names import OutboundMsg
from spirit.server import metrics
from .game_session import GameSession

# A client-supplied queueName longer than this is rejected (abuse: the queues dict
# is keyed by this string). Real format/tournament names are short.
_MAX_QUEUE_NAME_LEN = 64


class GameSessionManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameSessionManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        
        # Format queues: { "queue_name": [ { "client": client, "deck": deck, "options": options } ] }
        self.queues: Dict[str, List[Dict[str, Any]]] = {}
        
        # Pending matches during ready-check: 
        # { "game_id": { "players": { "account_id": { "client": client, "deck": deck, "ready": bool } }, "is_solo": bool, "solitaire_id": str, "options": dict, "queue_name": str } }
        self.pending_pairings: Dict[str, Dict[str, Any]] = {}
        
        # Active gameplay sessions: { "game_id": GameSession }
        self.active_sessions: Dict[str, Any] = {}

        # Pending friend challenges: { "path": { "challenger": client, "opponent": client, "deck": dict, "options": dict } }
        self.pending_challenges: Dict[str, Dict[str, Any]] = {}

        # Player index into active_sessions: { "account_id": "game_id" }
        self.session_ids_by_player: Dict[str, str] = {}

        # Fire-and-forget tasks kept referenced until done (GC safety, cancellable on shutdown)
        self._background_tasks: set = set()

        # Flag to automatically confirm matchmaking readiness for real clients (bypassing unused client ready checks)
        self.auto_confirm_ready = True

        metrics.register_gauge("active_matches", lambda: len(self.active_sessions))
        metrics.register_gauge("matchmaking_queued",
                               lambda: sum(len(q) for q in self.queues.values()))
        metrics.register_gauge("pending_pairings", lambda: len(self.pending_pairings))

    def _spawn(self, coro) -> asyncio.Task:
        """Creates a tracked background task that self-removes when done."""
        task = asyncio.create_task(coro)
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)
        return task

    def get_session_by_player_id(self, account_id: str) -> Optional[GameSession]:
        """Looks up an active GameSession containing the specified player ID."""
        game_id = self.session_ids_by_player.get(account_id)
        if game_id is not None:
            session = self.active_sessions.get(game_id)
            if session is not None:
                return session
        # Fallback scan self-heals the index for sessions registered directly
        for game_id, session in self.active_sessions.items():
            if account_id in session.players:
                self.session_ids_by_player[account_id] = game_id
                return session
        return None

    def remove_session_by_player_id(self, account_id: str):
        """Removes any active sessions associated with the player ID."""
        session = self.get_session_by_player_id(account_id)
        if session is not None:
            logging.info(f"[SessionManager] Removing stale/finished session {session.game_id} for player {account_id}")
            self.remove_session(session.game_id, log=False)

    def remove_session(self, game_id: str, log: bool = True):
        """Removes a session by its game ID and cleans it up."""
        session = self.active_sessions.pop(game_id, None)
        if session:
            if log:
                logging.info(f"[SessionManager] Removing session {game_id}")
            for account_id in list(session.players):
                if self.session_ids_by_player.get(account_id) == game_id:
                    del self.session_ids_by_player[account_id]
            try:
                session.cleanup()
            except Exception as e:
                logging.error(f"[SessionManager] Error cleaning up session {game_id}: {e}")

    def remove_pending_pairings_for_client(self, client):
        """Drops any pre-game pairings holding the client (disconnect during ready check)."""
        stale = [gid for gid, p in self.pending_pairings.items()
                 if any(info["client"] is client for info in p["players"].values())]
        for game_id in stale:
            self.pending_pairings.pop(game_id, None)
            logging.info(f"[SessionManager] Dropped pending pairing {game_id} (client disconnected)")

    async def add_to_queue(self, client, queue_name: str, deck_data: dict, client_options: dict,
                           request_id: int = 0, tournament_context: dict = None):
        """Adds a client to the matchmaking queue for a format."""
        if not isinstance(queue_name, str) or len(queue_name) > _MAX_QUEUE_NAME_LEN:
            logging.warning(f"[Matchmaking] Rejecting oversized/invalid queueName from {client.addr}")
            return
        # Clean up any existing queue registrations and active sessions for this client first
        await self.remove_from_queue(client, send_left_packet=False)
        self.remove_session_by_player_id(client.player.account_id)

        logging.info(f"[Matchmaking] Player {client.player.username} ({client.player.account_id}) entering queue '{queue_name}'")

        # MatchQueueEntered transitions the client state machine to Statuses.Waiting
        entered_packet = {
            "messageName": OutboundMsg.MATCH_QUEUE_ENTERED.value,
            "estimatedWaitTime": 10
        }

        # Check if there is another player waiting in this queue
        queue = self.queues.setdefault(queue_name, [])
        if queue:
            # We have a match! Pop the first player
            opponent_entry = queue.pop(0)
            opp_client = opponent_entry["client"]
            opp_deck = opponent_entry["deck"]

            await client.send_packet(entered_packet, request_id)

            game_id = str(uuid.uuid4())
            logging.info(f"[Matchmaking] Pair matched! Creating multiplayer game {game_id} for {client.player.username} vs {opp_client.player.username}")

            pairing = {
                "players": {
                    client.player.account_id: {
                        "client": client,
                        "deck": deck_data,
                        "ready": False
                    },
                    opp_client.player.account_id: {
                        "client": opp_client,
                        "deck": opp_deck,
                        "ready": False
                    }
                },
                "is_solo": False,
                "solitaire_id": None,
                "options": client_options,
                "queue_name": queue_name
            }
            opp_tournament = opponent_entry.get("tournament_context")
            if tournament_context and opp_tournament:
                pairing["tournament"] = {
                    "tournament_id": tournament_context["tournament_id"],
                    "entries": {
                        client.player.account_id: tournament_context["entry_id"],
                        opp_client.player.account_id: opp_tournament["entry_id"],
                    },
                }
            self.pending_pairings[game_id] = pairing

            self._dispatch_ready_check(game_id, queue_name, [client, opp_client])

        else:
            # No player in queue. Queue client and send MatchQueueEntered
            queue.append({
                "client": client,
                "deck": deck_data,
                "options": client_options,
                "tournament_context": tournament_context
            })
            await client.send_packet(entered_packet, request_id)

    async def start_solo_match(self, client, deck_data: dict, solitaire_id: str, match_options: dict, request_id: int = 0):
        """Starts a local/offline single player practice match against an AI opponent."""
        await self.remove_from_queue(client, send_left_packet=False)
        self.remove_session_by_player_id(client.player.account_id)

        game_id = str(uuid.uuid4())
        logging.info(f"[Matchmaking] Starting Single Player match {game_id} for {client.player.username} vs AI ({solitaire_id})")

        self.pending_pairings[game_id] = {
            "players": {
                client.player.account_id: {
                    "client": client,
                    "deck": deck_data,
                    "ready": False
                },
                "mock_ai_bot": {
                    "client": None, # No TCP client connection
                    "deck": {},    # Standard bot deck
                    "ready": True  # AI is instantly ready
                }
            },
            "is_solo": True,
            "solitaire_id": solitaire_id,
            "options": match_options,
            "queue_name": "SinglePlayer"
        }

        # Send ConfirmReadyForMatch to the client
        confirm_packet = {
            "messageName": OutboundMsg.CONFIRM_READY_FOR_MATCH.value,
            "queueName": "SinglePlayer",
            "gameID": game_id,
            "path": f"game_route_{game_id[:8]}"
        }
        await client.send_packet(confirm_packet, request_id)

    def _dispatch_ready_check(self, game_id: str, queue_name: str, clients: list, delay: float = 1.5):
        """Sends ConfirmReadyForMatch to all clients after a short delay, then auto-confirms readiness."""
        async def send_confirm():
            await asyncio.sleep(delay)
            try:
                confirm_packet = {
                    "messageName": OutboundMsg.CONFIRM_READY_FOR_MATCH.value,
                    "queueName": queue_name,
                    "gameID": game_id,
                    "path": f"game_route_{game_id[:8]}"
                }
                for c in clients:
                    await c.send_packet(confirm_packet, 0)
                logging.info(f"[Matchmaking] Dispatched ConfirmReadyForMatch to all players for game {game_id}")

                # The client has no active ConfirmReadyForMatch listener during normal play,
                # so we confirm readiness on its behalf to trigger MatchFound cleanly.
                if getattr(self, "auto_confirm_ready", True):
                    for c in clients:
                        await self.confirm_ready(c, game_id)
            except Exception as e:
                logging.error(f"[Matchmaking] Error in matchmaking transition: {e}")

        self._spawn(send_confirm())

    def _find_online_client(self, source_client, account_id: str):
        """Finds a logged-in client on the same server by account ID. O(1)."""
        return source_client.server.clients_by_account.get(account_id)

    async def _send_challenge_failed(self, client, text: str, request_id: int = 0):
        await client.send_packet({
            "messageName": OutboundMsg.MATCH_REQUEST_WITH_SPECIFIC_CLIENT_FAILED.value,
            "failureType": {"id": text}
        }, request_id)

    async def create_challenge(self, client, opponent_id: str, deck_data: dict, match_options: dict):
        """Handles RequestMatchWithSpecificClient: offers a friend challenge to an online opponent."""
        # A player can only have one outstanding challenge in either direction
        await self.remove_challenges_for_client(client, notify_self=False)

        challenger_id = client.player.account_id
        opponent_client = self._find_online_client(client, opponent_id)
        if opponent_client is None:
            logging.info(f"[Matchmaking] Challenge from {client.player.username} failed: opponent {opponent_id} not online")
            return await self._send_challenge_failed(client, "Your opponent is no longer online.")
        if self.get_session_by_player_id(opponent_id):
            return await self._send_challenge_failed(client, "Your opponent is already in a match.")

        path = f"challenge_{uuid.uuid4()}"
        self.pending_challenges[path] = {
            "challenger": client,
            "opponent": opponent_client,
            "deck": deck_data,
            "options": match_options or {}
        }
        logging.info(f"[Matchmaking] {client.player.username} challenged {opponent_client.player.username} ({path})")

        # Challenger: MatchRequestSent moves its state machine to Waiting (shows the waiting dialog)
        await client.send_packet({
            "messageName": OutboundMsg.MATCH_REQUEST_SENT.value,
            "path": path,
            "opponentID": opponent_id
        }, 0)

        # Challenged: MatchRequested pops the accept dialog (opponentID = the challenger)
        await opponent_client.send_packet({
            "messageName": OutboundMsg.MATCH_REQUESTED.value,
            "path": path,
            "opponentID": challenger_id,
            "matchOptions": match_options or {}
        }, 0)

    async def accept_challenge(self, client, path: str, deck_data: dict):
        """Handles AcceptMatchWithSpecificClient: starts the game between challenger and accepter."""
        entry = self.pending_challenges.pop(path, None)
        if not entry or entry["opponent"] != client:
            if entry:
                self.pending_challenges[path] = entry
            return await self._send_challenge_failed(client, "This challenge is no longer available.")

        challenger = entry["challenger"]
        if not challenger.player or challenger not in client.server.clients:
            return await self._send_challenge_failed(client, "Your opponent is no longer online.")

        # Accepter: MatchRequestSent moves its state machine to Waiting
        await client.send_packet({
            "messageName": OutboundMsg.MATCH_REQUEST_SENT.value,
            "path": path,
            "opponentID": challenger.player.account_id
        }, 0)

        game_id = str(uuid.uuid4())
        logging.info(f"[Matchmaking] Challenge accepted! Creating game {game_id} for {challenger.player.username} vs {client.player.username}")

        self.pending_pairings[game_id] = {
            "players": {
                challenger.player.account_id: {
                    "client": challenger,
                    "deck": entry["deck"],
                    "ready": False
                },
                client.player.account_id: {
                    "client": client,
                    "deck": deck_data,
                    "ready": False
                }
            },
            "is_solo": False,
            "solitaire_id": None,
            "options": entry["options"],
            "queue_name": "Friend"
        }

        self._dispatch_ready_check(game_id, "Friend", [challenger, client])

    async def reject_challenge(self, client, path: str):
        """Handles RejectMatchWithSpecificClient: notifies the challenger their offer was declined."""
        entry = self.pending_challenges.pop(path, None)
        if not entry:
            return
        challenger = entry["challenger"]
        logging.info(f"[Matchmaking] Challenge {path} rejected by {client.player.username}")
        await challenger.send_packet({
            "messageName": OutboundMsg.MATCH_REQUEST_REJECTED.value,
            "path": path,
            "failureType": "Rejected"
        }, 0)

    async def cancel_challenge(self, client, path: str):
        """Handles CancelMatchRequestWithSpecificClient: withdraws a pending challenge."""
        entry = self.pending_challenges.pop(path, None)
        cancelled_packet = {
            "messageName": OutboundMsg.MATCH_REQUEST_CANCELLED.value,
            "path": path
        }
        # Always echo to the canceller so its state machine unwinds from Canceling
        await client.send_packet(cancelled_packet, 0)
        if entry:
            logging.info(f"[Matchmaking] Challenge {path} cancelled by {client.player.username}")
            for party in (entry["challenger"], entry["opponent"]):
                if party != client:
                    await party.send_packet(cancelled_packet, 0)

    async def remove_challenges_for_client(self, client, notify_self: bool = True):
        """Cancels every pending challenge involving the client (used on disconnect)."""
        stale = [p for p, e in self.pending_challenges.items()
                 if e["challenger"] == client or e["opponent"] == client]
        for path in stale:
            entry = self.pending_challenges.pop(path)
            cancelled_packet = {
                "messageName": OutboundMsg.MATCH_REQUEST_CANCELLED.value,
                "path": path
            }
            for party in (entry["challenger"], entry["opponent"]):
                if party == client and not notify_self:
                    continue
                try:
                    await party.send_packet(cancelled_packet, 0)
                except Exception as e:
                    logging.error(f"[Matchmaking] Error notifying challenge cancellation for {path}: {e}")

    async def remove_from_queue(self, client, send_left_packet: bool = True):
        """Removes a client from all format queues."""
        removed = False
        for queue_name in list(self.queues.keys()):
            entries = self.queues[queue_name]
            filtered = [e for e in entries if e["client"] != client]
            if len(filtered) < len(entries):
                removed = True
            if filtered:
                self.queues[queue_name] = filtered
            else:
                # Prune empty queues so the dict can't grow unboundedly under churn.
                del self.queues[queue_name]

        if removed:
            logging.info(f"[Matchmaking] Removed player {client.player.username} from all queues.")
            if send_left_packet:
                left_packet = {
                    "messageName": OutboundMsg.MATCH_QUEUE_LEFT.value
                }
                await client.send_packet(left_packet, 0)

    async def confirm_ready(self, client, game_id: str):
        """Processes ready check confirmation from a client."""
        pairing = self.pending_pairings.get(game_id)
        if not pairing:
            logging.warning(f"[Matchmaking] Received ready confirmation for non-existent pairing {game_id}")
            return

        account_id = client.player.account_id
        if account_id in pairing["players"]:
            pairing["players"][account_id]["ready"] = True
            logging.info(f"[Matchmaking] Player {client.player.username} confirmed ready for game {game_id}")

            # Check if everyone is ready
            all_ready = all(player_info["ready"] for player_info in pairing["players"].values())
            if all_ready:
                await self._transition_to_game(game_id)
        else:
            logging.warning(f"[Matchmaking] Player {client.player.username} not part of pairing {game_id}")

    async def _transition_to_game(self, game_id: str):
        """Instantiates the active GameSession and sends MatchFound to start scene transition."""
        pairing = self.pending_pairings.pop(game_id, None)
        if not pairing:
            return

        logging.info(f"[Matchmaking] All players ready! Transitioning game {game_id} to active gameplay")

        # Instantiate GameSession
        session = GameSession(game_id, pairing)
        self.active_sessions[game_id] = session
        metrics.inc("matches_started")
        for account_id in session.players:
            self.session_ids_by_player[account_id] = game_id

        self._spawn(session.start())
