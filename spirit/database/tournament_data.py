import logging
import time
import uuid

from sqlalchemy import func

from spirit.database import (
    db_session, Account, Wallet, AsyncTournament, TournamentEntry,
    TournamentLeaderboardClaim,
)
from spirit.database.versus_data import _grant_rewards_in_session

# JoinAsyncTournament currency string -> Wallet column
CURRENCY_FIELDS = {
    "tokens": "coins",
    "coins": "coins",
    "gems": "gems",
    "tickets": "tickets",
    "tournamentticket": "tickets",
}


def now_ms() -> int:
    return int(time.time() * 1000)


def _entry_to_dict(e: TournamentEntry) -> dict:
    return {
        "entry_id": e.entry_id,
        "tournament_id": e.tournament_id,
        "account_id": e.account_id,
        "deck": e.deck_json or {},
        "wins": e.wins,
        "losses": e.losses,
        "tiebreakers": e.tiebreakers,
        "status": e.status,
        "rewards_claimed": e.rewards_claimed,
        "history": e.history_json or [],
        "last_update": e.last_update,
    }


# ------------------------------------------------------------- definitions

def list_tournaments(enabled_only: bool = False) -> list:
    with db_session() as session:
        q = session.query(AsyncTournament)
        if enabled_only:
            q = q.filter_by(enabled=True)
        rows = q.order_by(AsyncTournament.created_at).all()
        return [{"tournament_id": t.tournament_id,
                 "definition": t.definition_json,
                 "enabled": t.enabled} for t in rows]


def upsert_tournament(definition: dict, tournament_id: str = None, enabled: bool = None) -> dict:
    with db_session() as session:
        row = None
        if tournament_id:
            row = session.query(AsyncTournament).filter_by(tournament_id=tournament_id).first()
        if row is None:
            row = AsyncTournament(
                tournament_id=tournament_id or str(uuid.uuid4()),
                definition_json=definition or {},
                enabled=True if enabled is None else bool(enabled))
            session.add(row)
        else:
            if definition is not None:
                row.definition_json = definition
            if enabled is not None:
                row.enabled = bool(enabled)
        session.flush()
        return {"tournament_id": row.tournament_id,
                "definition": row.definition_json, "enabled": row.enabled}


def delete_tournament(tournament_id: str) -> bool:
    with db_session() as session:
        row = session.query(AsyncTournament).filter_by(tournament_id=tournament_id).first()
        if not row:
            return False
        session.query(TournamentEntry).filter_by(tournament_id=tournament_id).delete()
        session.query(TournamentLeaderboardClaim).filter_by(tournament_id=tournament_id).delete()
        session.delete(row)
        return True


# ------------------------------------------------------------- entries / runs

def get_active_entries(account_id: str) -> list:
    with db_session() as session:
        rows = session.query(TournamentEntry).filter_by(
            account_id=account_id, status="active").all()
        return [_entry_to_dict(e) for e in rows]


def get_entry(entry_id: str) -> dict | None:
    with db_session() as session:
        row = session.query(TournamentEntry).filter_by(entry_id=entry_id).first()
        return _entry_to_dict(row) if row else None


def count_runs(account_id: str, tournament_id: str) -> int:
    with db_session() as session:
        return session.query(TournamentEntry).filter_by(
            account_id=account_id, tournament_id=tournament_id).count()


def create_entry(account_id: str, tournament_id: str, definition: dict,
                 currency: str, deck_json: dict):
    """Joins a run atomically: fee check + deduction + entry creation.

    Returns (entry_dict, None) or (None, error_text)."""
    run = (definition or {}).get("run") or {}
    fees = run.get("entryFee") or []
    max_runs = int((definition or {}).get("maxRuns") or 0)
    with db_session() as session:
        existing = session.query(TournamentEntry).filter_by(
            account_id=account_id, tournament_id=tournament_id).all()
        if any(e.status == "active" for e in existing):
            return None, "You already have an active run in this tournament."
        if max_runs > 0 and len(existing) >= max_runs:
            return None, "No runs remaining for this tournament."

        fee = None
        if fees:
            wanted = (currency or "").lower()
            for f in fees:
                if str(f.get("currency", "")).lower() == wanted:
                    fee = f
                    break
            if fee is None:
                return None, "Invalid entry fee currency."
            field = CURRENCY_FIELDS.get(str(fee.get("currency", "")).lower())
            amount = int(fee.get("amount") or 0)
            if field is None:
                return None, "Invalid entry fee currency."
            if amount > 0:
                wallet = session.query(Wallet).filter_by(account_id=account_id).first()
                if wallet is None or getattr(wallet, field) < amount:
                    return None, "You cannot afford the entry fee."
                setattr(wallet, field, getattr(wallet, field) - amount)

        entry = TournamentEntry(
            entry_id=str(uuid.uuid4()),
            tournament_id=tournament_id,
            account_id=account_id,
            deck_json=deck_json or {},
            history_json=[],
            last_update=now_ms(),
        )
        session.add(entry)
        session.flush()
        return _entry_to_dict(entry), None


def update_entry_deck(entry_id: str, account_id: str, deck_json: dict) -> bool:
    with db_session() as session:
        row = session.query(TournamentEntry).filter_by(
            entry_id=entry_id, account_id=account_id, status="active").first()
        if not row:
            return False
        row.deck_json = deck_json or {}
        row.last_update = now_ms()
        return True


def record_game_result(entry_id: str, won: bool, opponent_id: str,
                       opponent_name: str, run_config: dict) -> dict | None:
    """Applies one game result; returns the updated entry dict with
    'run_complete' set when the run reached its win/loss/game cap."""
    run = run_config or {}
    with db_session() as session:
        row = session.query(TournamentEntry).filter_by(entry_id=entry_id).first()
        if not row or row.status != "active":
            return None
        if won:
            row.wins += 1
        else:
            row.losses += 1
        history = list(row.history_json or [])
        history.append({
            "opponentID": opponent_id,
            "opponentName": opponent_name,
            "gameResult": "Win" if won else "Loss",
        })
        row.history_json = history
        row.last_update = now_ms()

        max_wins = int(run.get("maxWins") or 0)
        max_losses = int(run.get("maxLosses") or 0)
        max_games = int(run.get("maxGames") or 0)
        complete = ((max_wins > 0 and row.wins >= max_wins)
                    or (max_losses > 0 and row.losses >= max_losses)
                    or (max_games > 0 and row.wins + row.losses >= max_games))
        result = _entry_to_dict(row)
        result["run_complete"] = complete
        return result


def _prize_rewards_for(prize_table: list, value: int) -> list:
    for prize in prize_table or []:
        if int(prize.get("start", 0)) <= value <= int(prize.get("end", 0)):
            return list(prize.get("rewards") or [])
    return []


def finish_entry(entry_id: str, account_id: str, definition: dict,
                 resigned: bool = False):
    """Ends a run and grants its prize-table rewards once (idempotent).

    Returns (entry_dict, granted_rewards) or (None, [])."""
    run = (definition or {}).get("run") or {}
    with db_session() as session:
        row = session.query(TournamentEntry).filter_by(entry_id=entry_id).first()
        if not row or row.account_id != account_id:
            return None, []
        granted = []
        if not row.rewards_claimed:
            granted = _prize_rewards_for(run.get("prizeTable"), row.wins)
            if granted:
                _grant_rewards_in_session(session, account_id, granted)
            row.rewards_claimed = True
        if row.status == "active":
            row.status = "resigned" if resigned else "complete"
        row.last_update = now_ms()
        return _entry_to_dict(row), granted


# ------------------------------------------------------------- leaderboard

def leaderboard_standings(tournament_id: str, definition: dict) -> list:
    """All participants ranked by leaderboard points (wins*winValue + losses*lossValue)."""
    lb = (definition or {}).get("leaderboard") or {}
    win_value = int(lb.get("winValue") or 3)
    loss_value = int(lb.get("lossValue") or 0)
    with db_session() as session:
        rows = (session.query(
                    TournamentEntry.account_id,
                    func.sum(TournamentEntry.wins),
                    func.sum(TournamentEntry.losses))
                .filter_by(tournament_id=tournament_id)
                .group_by(TournamentEntry.account_id).all())
        names = {}
        if rows:
            accounts = session.query(Account).filter(
                Account.account_id.in_([r[0] for r in rows])).all()
            names = {a.account_id: (a.screen_name or a.username) for a in accounts}
        standings = []
        for account_id, wins, losses in rows:
            points = (wins or 0) * win_value + (losses or 0) * loss_value
            standings.append({
                "accountID": account_id,
                "displayName": names.get(account_id, "Unknown"),
                "points": float(points),
                "rank": 0,
                "displayRank": "",
            })
        standings.sort(key=lambda s: -s["points"])
        for i, s in enumerate(standings):
            s["rank"] = i + 1
            s["displayRank"] = str(i + 1)
        return standings


def get_leaderboard_claims(account_id: str) -> dict:
    with db_session() as session:
        rows = session.query(TournamentLeaderboardClaim).filter_by(account_id=account_id).all()
        return {r.tournament_id: True for r in rows}


def has_claimed_leaderboard(account_id: str, tournament_id: str) -> bool:
    with db_session() as session:
        return session.query(TournamentLeaderboardClaim).filter_by(
            account_id=account_id, tournament_id=tournament_id).first() is not None


def claim_leaderboard_reward(account_id: str, tournament_id: str, definition: dict,
                             standings: list):
    """Grants leaderboard prize-table rewards by final rank, once per account.

    Returns (rank, granted_rewards) or (None, error_text)."""
    lb = (definition or {}).get("leaderboard") or {}
    rank = next((s["rank"] for s in standings if s["accountID"] == account_id), None)
    if rank is None:
        return None, "You did not participate in this tournament."
    with db_session() as session:
        already = session.query(TournamentLeaderboardClaim).filter_by(
            account_id=account_id, tournament_id=tournament_id).first()
        if already:
            return None, "Leaderboard rewards already claimed."
        granted = _prize_rewards_for(lb.get("prizeTable"), rank)
        if granted:
            _grant_rewards_in_session(session, account_id, granted)
        session.add(TournamentLeaderboardClaim(
            tournament_id=tournament_id, account_id=account_id, rank=rank))
        return rank, granted


# ------------------------------------------------------------- legacy live brackets

def charge_fees(account_id: str, fees: list):
    """Charges every {currency, amount} row atomically. Returns error text or None."""
    with db_session() as session:
        wallet = session.query(Wallet).filter_by(account_id=account_id).first()
        if wallet is None:
            return "You cannot afford the entry fee."
        for fee in fees or []:
            field = CURRENCY_FIELDS.get(str(fee.get("currency", "")).lower())
            amount = int(fee.get("amount") or 0)
            if field is None:
                return "Invalid entry fee currency."
            if amount > 0 and getattr(wallet, field) < amount:
                return "You cannot afford the entry fee."
        for fee in fees or []:
            field = CURRENCY_FIELDS[str(fee.get("currency", "")).lower()]
            setattr(wallet, field, getattr(wallet, field) - int(fee.get("amount") or 0))
        return None


def refund_fees(account_id: str, fees: list):
    with db_session() as session:
        wallet = session.query(Wallet).filter_by(account_id=account_id).first()
        if wallet is None:
            return
        for fee in fees or []:
            field = CURRENCY_FIELDS.get(str(fee.get("currency", "")).lower())
            if field:
                setattr(wallet, field, getattr(wallet, field) + int(fee.get("amount") or 0))


def grant_prize_rewards(account_id: str, rewards: list):
    """Grants rich reward dicts (versus shape) in one session."""
    if not rewards:
        return
    with db_session() as session:
        _grant_rewards_in_session(session, account_id, rewards)
