import logging
import uuid

from spirit.network.message_names import InboundMsg, OutboundMsg
from spirit.database.async_utils import run_db
from spirit.database import tournament_data
from spirit.database.player_data import get_owned_counts
from spirit.game import rules
from spirit.game.format_manager import FormatManager
from spirit.game.tournament_manager import (
    TournamentManager, STATE_OPEN, STATE_ENTRY_CLOSED, STATE_RESOLVED, STATE_HIDDEN,
    now_ms,
)
from spirit.game.session.manager import GameSessionManager
from spirit.game.live_tournament import LiveTournamentManager
from .base import BaseHandler, handle
from spirit.game.tournament_manager import _client_reward


def serializable_deck(deck_data: dict, name: str = "Tournament Deck") -> dict:
    """Normalizes a stored deck_data dict into the client SerializableDeck shape."""
    deck_data = deck_data or {}
    if "piles" in deck_data:
        out = dict(deck_data)
        out.setdefault("deckID", str(uuid.uuid4()))
        out.setdefault("deckName", name)
        out.setdefault("attributes", [])
        return out
    guids = []
    for card in deck_data.get("cards", []):
        guids.extend([card.get("guid")] * int(card.get("count") or 0))
    return {
        "deckID": deck_data.get("deckID") or str(uuid.uuid4()),
        "deckName": deck_data.get("deckName") or name,
        "piles": {"deck": guids},
        "attributes": deck_data.get("attributes") or [],
    }


def tournament_format_value(tournament, legacy: bool = False):
    """Returns the configured format identifier for one tournament flow."""
    definition = getattr(tournament, "definition", {}) or {}
    if legacy:
        return definition.get("format") or "Unlimited"
    game = definition.get("game") or {}
    return game.get("format") or definition.get("format") or "Unlimited"


def validate_tournament_deck(deck: dict, tournament, owned_counts=None,
                             legacy: bool = False):
    """Validates a tournament deck and returns (results, format_error)."""
    format_value = tournament_format_value(tournament, legacy=legacy)
    format_guid = FormatManager().resolve_format_guid(format_value)
    if format_guid is None:
        return [], f"The {format_value} tournament format is not available on this server."
    return rules.validate_deck(
        deck, [format_guid], owned_counts=owned_counts), None


def validation_error_text(results: list) -> str:
    """Returns the first human-readable deck validation failure."""
    if results:
        details = results[0].get("results") or []
        if details:
            explanation = details[0].get("explanation") or {}
            if explanation.get("id"):
                return str(explanation["id"])
    return "This deck is not valid for this tournament."


def progress_dict(entry: dict) -> dict:
    """AsyncTournamentProgress wire shape from a tournament_data entry dict."""
    return {
        "tournamentDefID": entry["tournament_id"],
        "entryID": entry["entry_id"],
        "deck": entry.get("deck") or {},
        "wins": entry["wins"],
        "losses": entry["losses"],
        "lastUpdate": entry.get("last_update") or 0,
        "limitedCollection": [],
        "tiebreakers": entry.get("tiebreakers") or 0,
    }


def client_rewards(rewards: list) -> list:
    return [_client_reward(r) for r in rewards or []]


class TournamentHandler(BaseHandler):
    def _account_id(self):
        return self.client.player.account_id

    async def _error(self, message_name: str, text: str, request_id: int = 0):
        await self.send({
            "messageName": message_name,
            "error": {"id": text},
        }, request_id)

    def _resolve_deck_json(self, deck_id: str):
        """Snapshot the player's stored deck (by GUID) as a SerializableDeck."""
        if not deck_id:
            return None
        for d in getattr(self.client.player, "decks", []):
            if str(d.get("id", "")).lower() == str(deck_id).lower() and d.get("deck_data"):
                return serializable_deck(d["deck_data"], d.get("name") or "Tournament Deck")
        return None

    async def _validate_tournament_deck(self, deck: dict, tournament, legacy: bool = False):
        owned = await run_db(get_owned_counts, self._account_id())
        return validate_tournament_deck(
            deck, tournament, owned_counts=owned, legacy=legacy)

    # ------------------------------------------------------------- listing

    @handle(InboundMsg.GET_ACTIVE_ASYNC_TOURNAMENTS)
    async def handle_get_active_async_tournaments(self, message, request_id, flags):
        manager = TournamentManager()
        account_id = self._account_id()
        entries = await run_db(tournament_data.get_active_entries, account_id)
        claimed = await run_db(tournament_data.get_leaderboard_claims, account_id)
        visible = manager.visible_tournaments()
        visible_ids = {t.tournament_id.lower() for t in visible}
        await self.send({
            "messageName": OutboundMsg.ACTIVE_ASYNC_TOURNAMENTS.value,
            "tournamentDefinitions": [t.to_client_dict() for t in visible],
            "tournamentProgress": [
                progress_dict(e) for e in entries
                if e["tournament_id"].lower() in visible_ids
            ],
            "claimedLeaderboard": claimed,
        }, request_id)

    # ------------------------------------------------- legacy Events scene

    def _queue_counts(self) -> dict:
        """{tournamentID: queue size} — must be non-null (client ContainsKey NRE)."""
        live = LiveTournamentManager()
        return {t.tournament_id.lower(): len(live.queue_for(t.tournament_id))
                for t in TournamentManager().visible_tournaments()}

    async def _join_failed(self, text: str, request_id: int = 0):
        await self.send({
            "messageName": OutboundMsg.JOIN_TOURNAMENT_FAILED.value,
            "reason": {"id": text},
        }, request_id)

    async def _join_invalid_deck(self, results: list, request_id: int = 0):
        await self.send({
            "messageName": OutboundMsg.JOIN_TOURNAMENT_FAILED_INVALID_DECK.value,
            "deckValidationResult": results,
        }, request_id)

    @handle(InboundMsg.GET_ACTIVE_TOURNAMENTS)
    async def handle_get_active_tournaments_legacy(self, message, request_id, flags):
        # Zero active entries safely renders the maintenance/"no events" panel.
        await self.send({
            "messageName": OutboundMsg.AVAILABLE_TOURNAMENT_LIST.value,
            "tournamentList": [t.to_legacy_dict()
                               for t in TournamentManager().visible_tournaments()],
            "tournamentQueues": self._queue_counts(),
        }, request_id)

    @handle(InboundMsg.SUBSCRIBE_TO_TOURNAMENTS_CHANNEL)
    async def handle_subscribe_to_tournament_channel(self, message, request_id, flags):
        LiveTournamentManager().subscribe(self.client)
        await self.send({
            "messageName": OutboundMsg.SUBSCRIBE_TO_TOURNAMENT_CHANNEL_SUCCESSFUL.value,
            "tournamentQueues": self._queue_counts(),
        }, request_id)

    @handle(InboundMsg.UNSUBSCRIBE_TO_TOURNAMENTS_CHANNEL)
    async def handle_unsubscribe_to_tournament_channel(self, message, request_id, flags):
        LiveTournamentManager().unsubscribe(self.client)

    @handle(InboundMsg.JOIN_TOURNAMENT)
    async def handle_join_tournament(self, message, request_id, flags):
        tournament_id = str(message.get("tournamentID", ""))
        tournament = TournamentManager().get(tournament_id)
        live = LiveTournamentManager()
        account_id = self._account_id()

        if tournament is None or not tournament.enabled or tournament.state() != STATE_OPEN:
            return await self._join_failed("tournament.error.not_available", request_id)
        queued_tid, _ = live.find_queued(account_id)
        if queued_tid is not None or live.find_active_for(account_id) is not None:
            return await self._join_failed("You are already in a tournament.", request_id)

        deck_json = self._resolve_deck_json(message.get("deck"))
        if not deck_json:
            return await self._join_failed("The selected deck could not be found.", request_id)
        validation, format_error = await self._validate_tournament_deck(
            deck_json, tournament, legacy=True)
        if format_error:
            return await self._join_failed(format_error, request_id)
        if not validation or not validation[0]["valid"]:
            return await self._join_invalid_deck(validation, request_id)

        fees = tournament.legacy_entry_fees()
        error = await run_db(tournament_data.charge_fees, account_id, fees)
        if error:
            # WalletFailed makes the client undo its optimistic local deduction;
            # follow with a wallet push so the HUD resyncs regardless.
            await self._join_failed("event.join.error.WalletFailed", request_id)
            return await self.push_wallet()

        logging.info(f"[Tournaments] {self.client.player.username} queued for "
                     f"'{tournament.definition.get('name')}'")
        await self.send({
            "messageName": OutboundMsg.TOURNAMENT_QUEUE_JOINED.value,
            "tournamentID": tournament.tournament_id,
        }, request_id)
        await self.push_wallet()
        await live.join_queue(self.client, tournament, deck_json)

    @handle(InboundMsg.LEAVE_TOURNAMENT_QUEUE)
    async def handle_leave_tournament_queue(self, message, request_id, flags):
        tournament_id = str(message.get("tournamentID", ""))
        left = await LiveTournamentManager().leave_queue(self.client, tournament_id)
        await self.send({
            "messageName": (OutboundMsg.TOURNAMENT_QUEUE_LEFT.value if left
                            else OutboundMsg.TOURNAMENT_QUEUE_LEFT_FAILED.value),
            "tournamentID": tournament_id,
        }, request_id)

    @handle(InboundMsg.GET_PLAYERS_IN_QUEUE)
    async def handle_get_players_in_queue(self, message, request_id, flags):
        queue = LiveTournamentManager().queue_for(str(message.get("tournamentID", "")))
        await self.send({
            "messageName": OutboundMsg.USERS_IN_TOURNAMENT_QUEUE.value,
            "usernames": [p.username for p in queue],
        }, request_id)

    @handle(InboundMsg.GET_TOURNAMENT_IN_PROGRESS)
    async def handle_get_tournament_in_progress(self, message, request_id, flags):
        active_id = str(message.get("activeTournamentID", "")).lower()
        live = LiveTournamentManager()
        tournament = live.active.get(active_id)
        if tournament is None:
            tournament = live.find_active_for(self._account_id())
        data = []
        if tournament is not None:
            participant = tournament.get_participant(self._account_id())
            if participant is not None:
                participant.client = self.client
            data = [tournament.progress_dict()]
        await self.send({
            "messageName": OutboundMsg.TOURNAMENTS_IN_PROGRESS_DATA.value,
            "tournamentData": data,
        }, request_id)

    @handle(InboundMsg.LEAVE_ACTIVE_TOURNAMENT)
    async def handle_leave_active_tournament(self, message, request_id, flags):
        active_id = str(message.get("activeTournamentID", "")).lower()
        tournament = LiveTournamentManager().active.get(active_id)
        if tournament is not None:
            await tournament.withdraw(self._account_id())
        await self.send({
            "messageName": OutboundMsg.TOURNAMENT_LEFT.value,
            "activeTournamentID": active_id,
        }, request_id)

    @handle(InboundMsg.IS_USER_IN_ACTIVE_TOURNAMENT)
    @handle(InboundMsg.GET_ACTIVE_TOURNAMENT)
    async def handle_is_user_in_active_tournament(self, message, request_id, flags):
        tournament = LiveTournamentManager().find_active_for(self._account_id())
        active_id = "00000000-0000-0000-0000-000000000000"
        if tournament is not None:
            participant = tournament.get_participant(self._account_id())
            if participant is not None:
                participant.client = self.client
            active_id = tournament.active_id
        await self.send({
            "messageName": OutboundMsg.USER_IN_ACTIVE_TOURNAMENT.value,
            "activeTournamentID": active_id,
        }, request_id)

    @handle(InboundMsg.GET_NUMBER_OF_PLAYER_RUNS)
    async def handle_get_number_of_player_runs(self, message, request_id, flags):
        tournament_id = str(message.get("tournamentID", ""))
        runs = await run_db(tournament_data.count_runs, self._account_id(), tournament_id)
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_NUMBER_OF_PLAYER_RUNS.value,
            "tournamentID": tournament_id,
            "runs": runs,
        }, request_id)

    # ------------------------------------------------------------- join / play

    @handle(InboundMsg.JOIN_ASYNC_TOURNAMENT)
    async def handle_join_async_tournament(self, message, request_id, flags):
        tournament_id = str(message.get("tournamentID", ""))
        currency = str(message.get("currency", "") or "")
        deck_id = message.get("deckID")

        tournament = TournamentManager().get(tournament_id)
        if tournament is None or not tournament.enabled:
            return await self._error(
                OutboundMsg.JOIN_ASYNC_TOURNAMENT_ERROR.value,
                "This tournament is not available.", request_id)
        if tournament.state() != STATE_OPEN:
            return await self._error(
                OutboundMsg.JOIN_ASYNC_TOURNAMENT_ERROR.value,
                "This tournament is not open for entries.", request_id)

        deck_json = self._resolve_deck_json(deck_id)
        if not deck_json:
            return await self._error(
                OutboundMsg.JOIN_ASYNC_TOURNAMENT_ERROR.value,
                "The selected deck could not be found.", request_id)
        validation, format_error = await self._validate_tournament_deck(
            deck_json, tournament)
        if format_error:
            return await self._error(
                OutboundMsg.JOIN_ASYNC_TOURNAMENT_ERROR.value,
                format_error, request_id)
        if not validation or not validation[0]["valid"]:
            return await self._error(
                OutboundMsg.JOIN_ASYNC_TOURNAMENT_ERROR.value,
                validation_error_text(validation), request_id)
        entry, error = await run_db(
            tournament_data.create_entry, self._account_id(),
            tournament.tournament_id, tournament.definition, currency, deck_json)
        if error:
            return await self._error(
                OutboundMsg.JOIN_ASYNC_TOURNAMENT_ERROR.value, error, request_id)

        logging.info(f"[Tournaments] {self.client.player.username} joined "
                     f"'{tournament.definition.get('name')}' (entry {entry['entry_id']})")
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_JOINED.value,
            "tournamentID": tournament.tournament_id,
            "entryID": entry["entry_id"],
            "deck": entry["deck"],
            "progress": progress_dict(entry),
        }, request_id)
        await self.push_wallet()

    @handle(InboundMsg.START_ASYNC_TOURNAMENT_GAME)
    async def handle_start_async_tournament_game(self, message, request_id, flags):
        entry_id = str(message.get("entryID", ""))
        deck_id = message.get("deckID")

        entry = await run_db(tournament_data.get_entry, entry_id)
        if not entry or entry["account_id"] != self._account_id():
            return await self._error(
                OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                "Tournament run not found.", request_id)
        if entry["status"] != "active":
            return await self._error(
                OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                "This tournament run is already complete.", request_id)

        tournament = TournamentManager().get(entry["tournament_id"])
        if tournament is None or not tournament.enabled:
            return await self._error(
                OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                "This tournament is no longer available.", request_id)
        if tournament.state() in (STATE_RESOLVED, STATE_HIDDEN):
            return await self._error(
                OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                "This tournament has ended.", request_id)

        run = tournament.run_config
        if deck_id and run.get("allowDeckSwitching", True):
            deck_json = self._resolve_deck_json(deck_id)
            if not deck_json:
                return await self._error(
                    OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                    "The selected deck could not be found.", request_id)
            validation, format_error = await self._validate_tournament_deck(
                deck_json, tournament)
            if format_error:
                return await self._error(
                    OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                    format_error, request_id)
            if not validation or not validation[0]["valid"]:
                return await self._error(
                    OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                    validation_error_text(validation), request_id)
            await run_db(tournament_data.update_entry_deck,
                         entry_id, self._account_id(), deck_json)
            entry["deck"] = deck_json
            await self.send({
                "messageName": OutboundMsg.ASYNC_TOURNAMENT_DECK_UPDATED.value,
                "tournamentID": entry["tournament_id"],
                "entryID": entry_id,
                "deck": deck_json,
                "limitedCollection": [],
            }, 0)

        deck = entry.get("deck") or {}
        validation, format_error = await self._validate_tournament_deck(
            deck, tournament)
        if format_error:
            return await self._error(
                OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                format_error, request_id)
        if not validation or not validation[0]["valid"]:
            return await self._error(
                OutboundMsg.START_ASYNC_TOURNAMENT_GAME_ERROR.value,
                validation_error_text(validation), request_id)

        # Complete the RPC, then ride the normal matchmaking pipeline
        # (MatchQueueEntered -> ConfirmReadyForMatch -> MatchFound).
        await self.client.send_packet({}, request_id)
        await GameSessionManager().add_to_queue(
            self.client, f"AsyncTournament_{tournament.tournament_id}", deck, {},
            0, tournament_context={
                "tournament_id": tournament.tournament_id,
                "entry_id": entry_id,
            })

    @handle(InboundMsg.RESIGN_TOURNAMENT_RUN)
    async def handle_resign_tournament_run(self, message, request_id, flags):
        entry_id = str(message.get("entryID", ""))
        entry = await run_db(tournament_data.get_entry, entry_id)
        if not entry or entry["account_id"] != self._account_id():
            return
        tournament = TournamentManager().get(entry["tournament_id"])
        definition = tournament.definition if tournament else {}
        finished, granted = await run_db(
            tournament_data.finish_entry, entry_id, self._account_id(),
            definition, True)
        if finished:
            await self.send({
                "messageName": OutboundMsg.ASYNC_TOURNAMENT_REWARDS.value,
                "entryID": entry_id,
                "wins": finished["wins"],
                "losses": finished["losses"],
                "rewards": client_rewards(granted),
            }, request_id)
            await self.push_wallet()
            if any(r.get("rewardType") == "Archetype" for r in granted):
                await self.push_collection()

    @handle(InboundMsg.CLAIM_ASYNC_TOURNAMENT_REWARD)
    async def handle_claim_async_tournament_reward(self, message, request_id, flags):
        entry_id = str(message.get("entryID", ""))
        entry = await run_db(tournament_data.get_entry, entry_id)
        if not entry or entry["account_id"] != self._account_id():
            return await self._error(
                OutboundMsg.CLAIM_ASYNC_TOURNAMENT_REWARD_ERROR.value,
                "Tournament run not found.", request_id)
        tournament = TournamentManager().get(entry["tournament_id"])
        definition = tournament.definition if tournament else {}
        finished, granted = await run_db(
            tournament_data.finish_entry, entry_id, self._account_id(),
            definition, False)
        if not finished:
            return await self._error(
                OutboundMsg.CLAIM_ASYNC_TOURNAMENT_REWARD_ERROR.value,
                "Unable to claim rewards for this run.", request_id)
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_REWARDS.value,
            "entryID": entry_id,
            "wins": finished["wins"],
            "losses": finished["losses"],
            "rewards": client_rewards(granted),
        }, request_id)
        await self.push_wallet()
        if any(r.get("rewardType") == "Archetype" for r in granted):
            await self.push_collection()

    # ------------------------------------------------------------- history

    @handle(InboundMsg.GET_ASYNC_TOURNAMENT_GAME_HISTORY)
    async def handle_get_async_tournament_game_history(self, message, request_id, flags):
        entry_id = str(message.get("entryID", ""))
        entry = await run_db(tournament_data.get_entry, entry_id)
        games = []
        if entry and entry["account_id"] == self._account_id():
            games = entry.get("history") or []
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_GAME_HISTORY_LIST.value,
            "tournamentID": str(message.get("tournamentID", "")),
            "entryID": entry_id,
            "games": games,
        }, request_id)

    # ------------------------------------------------------------- standings

    async def _standings(self, tournament_id: str) -> list:
        tournament = TournamentManager().get(tournament_id)
        definition = tournament.definition if tournament else {}
        return await run_db(
            tournament_data.leaderboard_standings, tournament_id, definition)

    @handle(InboundMsg.GET_ASYNC_TOURNAMENT_STANDINGS)
    async def handle_get_async_tournament_standings(self, message, request_id, flags):
        standings = await self._standings(str(message.get("tournamentID", "")))
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_STANDINGS.value,
            "standings": standings,
        }, request_id)

    @handle(InboundMsg.GET_TOP_RANKED_STANDINGS)
    async def handle_get_top_ranked_standings(self, message, request_id, flags):
        standings = await self._standings(str(message.get("tournamentID", "")))
        count = max(1, int(message.get("count") or 10))
        me = next((s for s in standings if s["accountID"] == self._account_id()), None)
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_LEADERBOARD_TOP_RANKED_STANDINGS.value,
            "standings": standings[:count],
            "playerRank": me["rank"] if me else 0,
            "playerStanding": me,
        }, request_id)

    @handle(InboundMsg.GET_PLAYER_RANK_AND_SURROUNDING_STANDINGS)
    async def handle_get_player_rank_and_surrounding(self, message, request_id, flags):
        standings = await self._standings(str(message.get("tournamentID", "")))
        above = max(0, int(message.get("above") or 0))
        below = max(0, int(message.get("below") or 0))
        me = next((s for s in standings if s["accountID"] == self._account_id()), None)
        standing_map = {}
        if me:
            lo = max(0, me["rank"] - 1 - above)
            hi = min(len(standings), me["rank"] + below)
            for s in standings[lo:hi]:
                standing_map[s["rank"]] = s
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_LEADERBOARD_PLAYER_RANK_AND_SURROUNDING_STANDINGS.value,
            "standingMap": standing_map,
        }, request_id)

    # ------------------------------------------------------------- leaderboard claims

    @handle(InboundMsg.GET_CAN_CLAIM_LEADERBOARD_REWARDS_FOR_TOURNAMENT)
    async def handle_get_can_claim_leaderboard_rewards(self, message, request_id, flags):
        tournament_id = str(message.get("tournamentID", ""))
        tournament = TournamentManager().get(tournament_id)
        runs = await run_db(tournament_data.count_runs, self._account_id(), tournament_id)
        claimed = await run_db(
            tournament_data.has_claimed_leaderboard, self._account_id(), tournament_id)
        resolved = tournament is not None and tournament.state() in (STATE_RESOLVED, STATE_HIDDEN)
        rank = None
        if runs and resolved:
            standings = await self._standings(tournament_id)
            me = next((s for s in standings if s["accountID"] == self._account_id()), None)
            rank = me["rank"] if me else None
        available_in = 0
        if tournament is not None and not resolved:
            available_in = max(0, tournament.resolution_time - now_ms())
        await self.send({
            "messageName": OutboundMsg.CAN_CLAIM_LEADERBOARD_REWARDS_FOR_TOURNAMENT.value,
            "tournamentID": tournament_id,
            "hasParticipated": runs > 0,
            "claimAvailable": runs > 0 and resolved and not claimed,
            "rank": rank,
            "availableIn": available_in,
        }, request_id)

    @handle(InboundMsg.HAS_CLAIMED_ASYNC_TOURNAMENT_LEADERBOARD_REWARD)
    async def handle_has_claimed_leaderboard_reward(self, message, request_id, flags):
        tournament_id = str(message.get("tournamentID", ""))
        claimed = await run_db(
            tournament_data.has_claimed_leaderboard, self._account_id(), tournament_id)
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_HAS_CLAIMED_LEADERBOARD_REWARD.value,
            "tournamentID": tournament_id,
            "claimed": claimed,
        }, request_id)

    @handle(InboundMsg.CLAIM_ASYNC_TOURNAMENT_LEADERBOARD_REWARD)
    async def handle_claim_async_tournament_leaderboard_reward(self, message, request_id, flags):
        tournament_id = str(message.get("tournamentID", ""))
        tournament = TournamentManager().get(tournament_id)
        if tournament is None or tournament.state() not in (STATE_RESOLVED, STATE_HIDDEN):
            return await self._error(
                OutboundMsg.CLAIM_ASYNC_TOURNAMENT_REWARD_ERROR.value,
                "Leaderboard rewards are not available yet.", request_id)
        standings = await self._standings(tournament_id)
        rank, granted = await run_db(
            tournament_data.claim_leaderboard_reward, self._account_id(),
            tournament_id, tournament.definition, standings)
        if rank is None:
            return await self._error(
                OutboundMsg.CLAIM_ASYNC_TOURNAMENT_REWARD_ERROR.value,
                str(granted), request_id)
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_LEADERBOARD_REWARDS.value,
            "tournamentID": tournament_id,
            "rank": rank,
            "rewards": client_rewards(granted),
        }, request_id)
        await self.push_wallet()
        if any(r.get("rewardType") == "Archetype" for r in granted):
            await self.push_collection()

    # ------------------------------------------------------------- packs / league stubs

    @handle(InboundMsg.GET_UNACKNOWLEDGED_PACKS)
    async def handle_get_unacknowledged_packs(self, message, request_id, flags):
        # Product rewards are granted straight to the collection; no pack-opening queue.
        await self.send({
            "messageName": OutboundMsg.ASYNC_TOURNAMENT_UNACKNOWLEDGED_PACKS.value,
            "tournamentEntryID": str(message.get("entryID", "")),
            "packs": [],
            "additionalRewards": None,
        }, request_id)

    @handle(InboundMsg.ACKNOWLEDGE_PACK)
    async def handle_acknowledge_pack(self, message, request_id, flags):
        await self.send({
            "messageName": OutboundMsg.PACK_ACKNOWLEDGED.value,
            "tournamentEntryID": str(message.get("entryID", "")),
            "packID": str(message.get("packID", "")),
        }, request_id)

    @handle(InboundMsg.GET_LEAGUE_TIEBREAKERS_REMAINING)
    async def handle_get_league_tiebreakers_remaining(self, message, request_id, flags):
        await self.send({
            "messageName": OutboundMsg.LEAGUE_TIEBREAKERS_REMAINING.value,
            "tournamentID": str(message.get("tournamentID", "")),
            "entryID": str(message.get("entryID", "")),
            "week": 0,
            "tiebreakersPlayedThisWeek": 0,
            "tiebreakersRemaining": 0,
        }, request_id)
