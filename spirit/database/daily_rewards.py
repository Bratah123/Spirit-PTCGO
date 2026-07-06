import datetime
import logging
import random
import uuid

from spirit.database import db_session, engine
from spirit.database.models.economy import DailyLoginProgress
from spirit.database.economy_data import _grant_reward_in_session
from spirit.game.daily_rewards import DailyRewardManager

_schema_checked = False


def _ensure_activations_column():
    """Adds the activations column to daily_login_progress tables created before it existed."""
    global _schema_checked
    if _schema_checked:
        return
    with engine.connect() as conn:
        cols = [row[1] for row in conn.exec_driver_sql("PRAGMA table_info(daily_login_progress)")]
        if cols and "activations" not in cols:
            conn.exec_driver_sql(
                "ALTER TABLE daily_login_progress ADD COLUMN activations INTEGER DEFAULT 0")
            conn.commit()
    _schema_checked = True


def _random_pack_guid():
    from spirit.game.models.product import BoosterPack
    from spirit.game.scripts.products import loader as product_loader, BOOSTER_GUID_NAMESPACE
    packs = [p.guid for p in product_loader.products if isinstance(p, BoosterPack)]
    if not packs:
        from spirit.game.set_utils import eligible_booster_sets
        packs = [str(uuid.uuid5(BOOSTER_GUID_NAMESPACE, s.upper()))
                 for s in eligible_booster_sets()]
    return random.choice(packs) if packs else None


def build_grant_payload(rewards):
    """Maps daily Reward objects onto the shared reward-grant dict shape."""
    payload = {"products": {}, "coins": 0, "tickets": 0}
    for r in rewards:
        amount = max(int(r.reward_amount or 0), 0)
        if r.reward_type == "Tokens":
            payload["coins"] += amount
        elif r.reward_type == "TournamentTicket":
            payload["tickets"] += amount
        elif r.reward_type == "RandomBooster":
            guid = _random_pack_guid()
            if guid:
                payload["products"][guid] = payload["products"].get(guid, 0) + max(amount, 1)
            else:
                logging.warning("[DailyRewards] No booster packs available for RandomBooster")
        elif r.reward_type == "Archetype" and r.reward_product_id:
            guid = r.reward_product_id
            payload["products"][guid] = payload["products"].get(guid, 0) + max(amount, 1)
    return payload


def process_daily_login(account_id: str) -> dict:
    """Advances the account's daily-login state, granting today's reward once per UTC day."""
    _ensure_activations_column()
    manager = DailyRewardManager()
    today = datetime.datetime.now(datetime.timezone.utc).date()

    with db_session() as session:
        progress = session.query(DailyLoginProgress).filter_by(account_id=account_id).first()
        if not progress:
            progress = DailyLoginProgress(account_id=account_id)
            session.add(progress)

        first_daily_login = progress.last_claim_date != today
        granted = []
        if first_daily_login:
            broke_streak = (progress.last_claim_date is None
                            or (today - progress.last_claim_date).days > 1)
            progress.streak = 1 if broke_streak else (progress.streak or 0) + 1
            progress.activations = (progress.activations or 0) + 1
            progress.last_claim_date = today
            granted = manager.rewards_for(progress.streak, progress.activations)
            payload = build_grant_payload(granted)
            if payload["products"] or payload["coins"] or payload["tickets"]:
                _grant_reward_in_session(session, account_id, payload)

        activations = progress.activations or 0
        streak = progress.streak or 0

    next_midnight = datetime.datetime.combine(
        today + datetime.timedelta(days=1), datetime.time.min,
        tzinfo=datetime.timezone.utc)
    return {
        "firstDailyLogin": first_daily_login,
        "activations": activations,
        "rewardDay": manager.reward_day(streak, activations),
        # client countdown runs WargTime.FromMilliseconds(timestamp) - serverNow
        "nextRewardTimestampMs": int(next_midnight.timestamp() * 1000),
        "granted": granted,
    }
