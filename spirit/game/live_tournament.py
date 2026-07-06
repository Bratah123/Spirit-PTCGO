"""Legacy Events-scene live bracket tournaments (queue -> rounds -> completion)."""
import asyncio
import logging
import random
import uuid

from typing import Dict, List, Optional

from spirit.network.message_names import OutboundMsg
from spirit.database.async_utils import run_db
from spirit.database import tournament_data
from spirit.game.models.versus import Reward
from spirit.game.tournament_manager import TournamentManager, TournamentDef


class Participant:
    def __init__(self, client, deck: dict):
        self.account_id = client.player.account_id
        self.username = (getattr(client.player, "screen_name", None)
                         or client.player.username)
        self.client = client
        self.deck = deck
        self.withdrawn = False
        self.wins = 0
        self.eliminated_round = 0  # 0 = still alive

    def identity(self) -> dict:
        return {"accountID": self.account_id, "username": self.username}


class Matchup:
    def __init__(self, round_no: int, table: int, players: List[Participant]):
        self.game_id = str(uuid.uuid4())
        self.round = round_no  # 1-based
        self.table = table     # 0-based
        self.players = players
        self.winner: Optional[Participant] = None

    def to_dict(self) -> dict:
        # players must be EXACTLY 2 entries: G.j.get_Player1 NREs otherwise
        return {
            "gameID": self.game_id,
            "winner": self.winner.identity() if self.winner else None,
            "round": self.round,
            "table": self.table,
            "players": [p.identity() for p in self.players],
        }


class LiveTournament:
    """One running single-elimination bracket."""

    def __init__(self, manager: "LiveTournamentManager", definition: TournamentDef,
                 participants: List[Participant]):
        self.manager = manager
        self.definition = definition
        self.active_id = str(uuid.uuid4())
        self.participants = participants
        self.matchups: List[Matchup] = []
        self.current_round = 0
        self.completed = False

    # ------------------------------------------------------------- wire shapes

    def progress_dict(self) -> dict:
        return {
            "activeTournamentID": self.active_id,
            "tournamentData": self.definition.to_legacy_dict(),
            "currentRound": self.current_round,
            "matchups": [m.to_dict() for m in self.matchups],
            "roundLength": int(self.definition.definition.get("roundLength") or 30),
        }

    # ------------------------------------------------------------- lifecycle

    async def start(self):
        random.shuffle(self.participants)
        await self._broadcast({
            "messageName": OutboundMsg.TOURNAMENT_STARTED.value,
            "activeTournamentID": self.active_id,
            "size": len(self.participants),
        })
        await self._begin_round(1, list(self.participants))

    async def _begin_round(self, round_no: int, players: List[Participant]):
        self.current_round = round_no
        new_matchups = []
        for table in range(len(players) // 2):
            m = Matchup(round_no, table, players[table * 2: table * 2 + 2])
            new_matchups.append(m)
        self.matchups.extend(new_matchups)
        await self._push_round_update()
        for m in new_matchups:
            await self._start_or_forfeit(m)

    async def _start_or_forfeit(self, matchup: Matchup):
        """Launches the game, or auto-advances when a seat is withdrawn/offline."""
        live = [p for p in matchup.players
                if not p.withdrawn and self.manager.resolve_client(p) is not None]
        if len(live) < 2:
            winner = live[0] if live else matchup.players[0]
            await self.record_result(matchup.game_id, winner.account_id, forfeit=True)
            return
        from spirit.game.session.manager import GameSessionManager
        gsm = GameSessionManager()
        pairing = {
            "players": {
                p.account_id: {"client": self.manager.resolve_client(p),
                               "deck": p.deck, "ready": False}
                for p in matchup.players
            },
            "is_solo": False,
            "solitaire_id": None,
            "options": {},
            "queue_name": f"Tournament_{self.definition.tournament_id}",
            "legacy_tournament": {
                "active_id": self.active_id,
                "tournament_id": self.definition.tournament_id,
            },
        }
        gsm.pending_pairings[matchup.game_id] = pairing
        gsm._dispatch_ready_check(
            matchup.game_id, pairing["queue_name"],
            [info["client"] for info in pairing["players"].values()])

    async def record_result(self, game_id: str, winner_account_id: str, forfeit: bool = False):
        matchup = next((m for m in self.matchups if m.game_id == game_id), None)
        if matchup is None or matchup.winner is not None or self.completed:
            return
        winner = next((p for p in matchup.players
                       if p.account_id == winner_account_id), matchup.players[0])
        matchup.winner = winner
        winner.wins += 1
        for p in matchup.players:
            if p is not winner:
                p.eliminated_round = matchup.round
        logging.info(f"[LiveTournament {self.active_id[:8]}] R{matchup.round} T{matchup.table} "
                     f"winner: {winner.username}{' (forfeit)' if forfeit else ''}")
        await self._push_round_update()
        await self._check_round_complete(matchup.round)
        if not forfeit and not self.completed:
            # After EOG the client needs a nudge back to the Tournament scene;
            # while still on Playmat the push is ignored, so repeat it briefly.
            self.manager._spawn(self._nudge_back_to_tournament(matchup.players))

    async def _nudge_back_to_tournament(self, players: List[Participant]):
        for delay in (1.5, 10, 30):
            await asyncio.sleep(delay)
            if self.completed:
                return
            for p in players:
                await self._send_to(p, {
                    "messageName": OutboundMsg.USER_IN_ACTIVE_TOURNAMENT.value,
                    "activeTournamentID": self.active_id,
                })

    async def _check_round_complete(self, round_no: int):
        round_matchups = [m for m in self.matchups if m.round == round_no]
        if any(m.winner is None for m in round_matchups):
            return
        winners = [m.winner for m in sorted(round_matchups, key=lambda m: m.table)]
        if len(winners) == 1:
            await self._complete(winners[0])
            return
        delay = max(3, int(self.definition.definition.get("delayBetweenRounds") or 10))
        await self._broadcast({
            "messageName": OutboundMsg.TOURNAMENT_NEXT_ROUND_STARTING.value,
            "activeTournamentID": self.active_id,
            "countdown": delay,
            "suppressPopup": False,
        })
        self.manager._spawn(self._next_round_after(delay, round_no + 1, winners))

    async def _next_round_after(self, delay: int, round_no: int, winners: List[Participant]):
        await asyncio.sleep(delay)
        if not self.completed:
            await self._begin_round(round_no, winners)

    def final_standings(self) -> List[Participant]:
        """Champion first, then by elimination round (later = better), then wins."""
        return sorted(self.participants,
                      key=lambda p: (p.eliminated_round == 0,
                                     p.eliminated_round, p.wins),
                      reverse=True)

    async def _complete(self, champion: Participant):
        self.completed = True
        standings = self.final_standings()
        prize_table = self.definition.run_config.get("prizeTable") or []
        base = self.progress_dict()
        for place, participant in enumerate(standings, start=1):
            granted = tournament_data._prize_rewards_for(prize_table, place)
            if granted and not participant.withdrawn:
                await run_db(tournament_data.grant_prize_rewards,
                             participant.account_id, granted)
            else:
                granted = []
            # prizes must be a non-null array: the final-standings view foreachs it
            await self._send_to(participant, {
                "messageName": OutboundMsg.TOURNAMENT_COMPLETED.value,
                "tournamentData": base,
                "finalStandings": [p.identity() for p in standings],
                "prizes": [Reward.from_dict(r).to_dict(i)
                           for i, r in enumerate(granted)],
            })
            client = self.manager.resolve_client(participant)
            if client is not None and granted:
                await self.manager.push_wallet(client)
        logging.info(f"[LiveTournament {self.active_id[:8]}] Completed — "
                     f"champion {champion.username}")
        self.manager.finish_tournament(self)

    # ------------------------------------------------------------- membership

    def get_participant(self, account_id: str) -> Optional[Participant]:
        return next((p for p in self.participants
                     if p.account_id == account_id), None)

    async def withdraw(self, account_id: str):
        """LeaveActiveTournament: forfeit the player's unresolved matchup."""
        participant = self.get_participant(account_id)
        if participant is None or participant.withdrawn:
            return
        participant.withdrawn = True
        pending = next((m for m in self.matchups
                        if m.winner is None and participant in m.players), None)
        if pending is not None:
            opponent = next(p for p in pending.players if p is not participant)
            await self.record_result(pending.game_id, opponent.account_id, forfeit=True)

    # ------------------------------------------------------------- sends

    async def _send_to(self, participant: Participant, packet: dict):
        client = self.manager.resolve_client(participant)
        if client is None:
            return
        try:
            await client.send_packet(packet, 0)
        except Exception as e:
            logging.error(f"[LiveTournament] send to {participant.username} failed: {e}")

    async def _broadcast(self, packet: dict):
        for p in self.participants:
            await self._send_to(p, packet)

    async def _push_round_update(self):
        await self._broadcast({
            "messageName": OutboundMsg.TOURNAMENT_ROUND_UPDATED.value,
            "activeTournamentID": self.active_id,
            "tournamentData": self.progress_dict(),
        })


class LiveTournamentManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LiveTournamentManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.subscribers: list = []                       # clients on the Events scene
        self.queues: Dict[str, List[Participant]] = {}    # tournament_id -> waiting players
        self.active: Dict[str, LiveTournament] = {}       # active_id -> tournament
        self._background_tasks: set = set()

    def _spawn(self, coro) -> asyncio.Task:
        task = asyncio.create_task(coro)
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)
        return task

    # ------------------------------------------------------------- helpers

    def resolve_client(self, participant: Participant):
        """Returns a live client for the participant (self-heals after reconnect)."""
        client = participant.client
        if client is not None and getattr(client, "running", False) and client.player:
            return client
        server = getattr(client, "server", None)
        for other in list(getattr(server, "clients", []) or []):
            if other.player and other.player.account_id == participant.account_id:
                participant.client = other
                return other
        return None

    async def push_wallet(self, client):
        try:
            wallet = getattr(client.player, "wallet", None)
            if wallet is not None:
                await run_db(wallet.refresh_wallet)
            payload = client.player.get_wallet_data()
            payload["messageName"] = OutboundMsg.CURRENT_WALLET.value
            await client.send_packet(payload, 0)
        except Exception as e:
            logging.error(f"[LiveTournament] wallet push failed: {e}")

    def queue_sizes(self) -> dict:
        return {tid: len(entries) for tid, entries in self.queues.items()}

    def queue_for(self, tournament_id: str) -> List[Participant]:
        return self.queues.setdefault(tournament_id.lower(), [])

    def find_active_for(self, account_id: str) -> Optional[LiveTournament]:
        for t in self.active.values():
            p = t.get_participant(account_id)
            if p is not None and not t.completed and not p.withdrawn:
                return t
        return None

    def find_queued(self, account_id: str):
        for tid, entries in self.queues.items():
            for p in entries:
                if p.account_id == account_id:
                    return tid, p
        return None, None

    # ------------------------------------------------------------- queue flow

    async def join_queue(self, client, tournament: TournamentDef, deck: dict):
        """Adds to the queue (fee already charged); starts the bracket when full."""
        tid = tournament.tournament_id.lower()
        queue = self.queue_for(tid)
        queue.append(Participant(client, deck))
        await self.broadcast_queue_status(tid)
        await self.push_queue_users(tid)
        if len(queue) >= tournament.max_size:
            players = [queue.pop(0) for _ in range(tournament.max_size)]
            await self.broadcast_queue_status(tid)
            live = LiveTournament(self, tournament, players)
            self.active[live.active_id] = live
            logging.info(f"[LiveTournament] Starting '{tournament.definition.get('name')}' "
                         f"({live.active_id}) with {len(players)} players")
            await live.start()

    async def leave_queue(self, client, tournament_id: str) -> bool:
        tid = tournament_id.lower()
        queue = self.queue_for(tid)
        entry = next((p for p in queue
                      if p.account_id == client.player.account_id), None)
        if entry is None:
            return False
        queue.remove(entry)
        tournament = TournamentManager().get(tid)
        if tournament is not None:
            await run_db(tournament_data.refund_fees,
                         entry.account_id, tournament.legacy_entry_fees())
            await self.push_wallet(client)
        await self.broadcast_queue_status(tid)
        await self.push_queue_users(tid)
        return True

    async def broadcast_queue_status(self, tournament_id: str):
        packet = {
            "messageName": OutboundMsg.TOURNAMENT_QUEUE_STATUS.value,
            "tournamentID": tournament_id,
            "size": len(self.queue_for(tournament_id)),
        }
        for client in list(self.subscribers):
            try:
                await client.send_packet(packet, 0)
            except Exception:
                pass
        for p in list(self.queue_for(tournament_id)):
            client = self.resolve_client(p)
            if client is not None and client not in self.subscribers:
                try:
                    await client.send_packet(packet, 0)
                except Exception:
                    pass

    async def push_queue_users(self, tournament_id: str):
        queue = self.queue_for(tournament_id)
        packet = {
            "messageName": OutboundMsg.USERS_IN_TOURNAMENT_QUEUE.value,
            "usernames": [p.username for p in queue],
        }
        for p in list(queue):
            client = self.resolve_client(p)
            if client is not None:
                try:
                    await client.send_packet(packet, 0)
                except Exception:
                    pass

    # ------------------------------------------------------------- results / cleanup

    async def record_game_result(self, active_id: str, game_id: str, winner_account_id: str):
        tournament = self.active.get(active_id)
        if tournament is not None:
            await tournament.record_result(game_id, winner_account_id)

    def finish_tournament(self, tournament: LiveTournament):
        self.active.pop(tournament.active_id, None)

    def subscribe(self, client):
        if client not in self.subscribers:
            self.subscribers.append(client)

    def unsubscribe(self, client):
        if client in self.subscribers:
            self.subscribers.remove(client)

    async def handle_disconnect(self, client):
        """Drops the client from subscribers and queues (with refund)."""
        self.unsubscribe(client)
        if not client.player:
            return
        tid, entry = self.find_queued(client.player.account_id)
        if entry is not None:
            await self.leave_queue(client, tid)
        # Active-tournament participants stay seated: resolve_client() picks the
        # player back up on reconnect, and _start_or_forfeit forfeits no-shows.
