"""Transactional daily challenges and exactly-once match credit."""

import datetime as dt
import hashlib
import uuid

from sqlalchemy import text

from spirit.database import db_session
from spirit.database.models import Account, Wallet, QuestAccount, DailyQuest, QuestMatchCredit
from spirit.game.quests import AFFINITIES, MAX_ACTIVE, XP_LEVELS, coin_reward, configuration, load_catalog, quest_payload


def utc_now():
    return dt.datetime.now(dt.timezone.utc)


def _state(session, account_id):
    if session.query(Account).filter_by(account_id=account_id).first() is None:
        raise ValueError("Unknown account")
    state = session.get(QuestAccount, account_id)
    if state is None:
        state = QuestAccount(account_id=account_id, enabled=True, affinity_xp={})
        session.add(state)
        session.flush()
    return state


def account_quest_attributes(account_id):
    with db_session() as session:
        state = session.get(QuestAccount, account_id)
        return {
            "enabled": state.enabled if state else True,
            "xp": {key: (state.affinity_xp or {}).get(key, 0) if state else 0 for key in AFFINITIES},
        }


def _snapshot(session, state, now):
    today = now.date()
    rows = session.query(DailyQuest).filter_by(account_id=state.account_id).all()
    active = [row for row in rows if row.status == "active"]
    for row in rows:
        if row.status == "available" and row.offered_date != today:
            row.status = "expired"
    available = []
    if state.enabled and state.selected_date != today and len(active) < MAX_ACTIVE:
        available = [row for row in rows if row.status == "available"]
        if not available:
            active_keys = {row.definition["key"] for row in active}
            candidates = [row for row in load_catalog() if row["key"] not in active_keys]
            candidates.sort(key=lambda row: hashlib.sha256(
                f"{state.account_id}:{today}:{row['key']}".encode()).digest())
            for template in candidates[:2]:
                quest_id = str(uuid.uuid5(uuid.NAMESPACE_URL,
                                         f"spirit:daily:{state.account_id}:{today}:{template['key']}"))
                row = DailyQuest(quest_id=quest_id, account_id=state.account_id,
                                 offered_date=today, status="available",
                                 definition=dict(template), activations=0)
                session.add(row)
                available.append(row)
    tomorrow = dt.datetime.combine(today + dt.timedelta(days=1), dt.time.min, dt.timezone.utc)
    next_time = now if available else tomorrow
    return {
        "quests": {
            "currentQuests": [quest_payload(row) for row in active] if state.enabled else [],
            "availableQuests": [quest_payload(row) for row in available], "specialQuests": [],
        },
        "configuration": configuration(int(next_time.timestamp() * 1000)),
    }


def get_quests(account_id, *, now=None):
    now = now or utc_now()
    with db_session() as session:
        session.execute(text("BEGIN IMMEDIATE"))
        return _snapshot(session, _state(session, account_id), now)


def set_enabled(account_id, enabled, *, now=None):
    now = now or utc_now()
    with db_session() as session:
        session.execute(text("BEGIN IMMEDIATE"))
        state = _state(session, account_id)
        state.enabled = enabled
        return _snapshot(session, state, now)


def select_quest(account_id, quest_ids, *, now=None):
    now = now or utc_now()
    with db_session() as session:
        session.execute(text("BEGIN IMMEDIATE"))
        state = _state(session, account_id)
        snapshot = _snapshot(session, state, now)
        valid = {q["questDefinition"]["questID"] for q in snapshot["quests"]["availableQuests"]}
        if len(quest_ids) != 1 or quest_ids[0] not in valid:
            return snapshot
        session.flush()
        row = session.get(DailyQuest, quest_ids[0])
        row.status = "active"
        row.accepted_at = now.timestamp()
        state.selected_date = now.date()
        session.flush()
        return _snapshot(session, state, now)


def abandon_quests(account_id, quest_ids, *, now=None):
    now = now or utc_now()
    with db_session() as session:
        session.execute(text("BEGIN IMMEDIATE"))
        state = _state(session, account_id)
        for row in session.query(DailyQuest).filter_by(account_id=account_id, status="active"):
            if row.quest_id in quest_ids:
                row.status = "abandoned"
        session.flush()
        return _snapshot(session, state, now)


def credit_match(account_id, game_id, stats, won, started_at):
    """Applies server-owned counters and grants completed rewards atomically."""
    result = {"completedQuestsAndXPTotal": [], "progressedQuests": [], "rewards": []}
    with db_session() as session:
        session.execute(text("BEGIN IMMEDIATE"))
        state = _state(session, account_id)
        if session.get(QuestMatchCredit, (account_id, game_id)) is not None:
            return result
        session.add(QuestMatchCredit(account_id=account_id, game_id=game_id))
        if not state.enabled:
            return result
        xp = dict(state.affinity_xp or {})
        counters = dict(stats)
        counters["wins"] = int(won)
        for row in session.query(DailyQuest).filter_by(account_id=account_id, status="active"):
            if row.accepted_at is None or row.accepted_at > started_at:
                continue
            delta = max(0, int(counters.get(row.definition["stat"], 0)))
            if not delta:
                continue
            row.activations = min(row.definition["target"], row.activations + delta)
            payload = quest_payload(row)
            if row.activations < row.definition["target"]:
                result["progressedQuests"].append(payload)
                continue
            row.status = "completed"
            old_xp = xp.get("Colorless", 0)
            new_xp = min(max(XP_LEVELS.values()), old_xp + row.definition["xp"])
            xp["Colorless"] = new_xp
            result["completedQuestsAndXPTotal"].append([payload["questDefinition"], new_xp])
            result["rewards"].extend(payload["questDefinition"]["rewards"])
            for level, threshold in XP_LEVELS.items():
                if old_xp < threshold <= new_xp:
                    result["rewards"].append(coin_reward(25, f"ColorlessLevel{level}"))
        state.affinity_xp = xp
        coins = sum(reward["rewardAmount"] for reward in result["rewards"])
        if coins:
            wallet = session.get(Wallet, account_id)
            if wallet is None:
                wallet = Wallet(account_id=account_id, coins=0, gems=0, tickets=0)
                session.add(wallet)
            wallet.coins += coins
    return result
