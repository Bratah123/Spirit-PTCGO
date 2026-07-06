import logging

from spirit.database import db_session, Wallet, Collection, VersusProgress

# Ladder points awarded when a match completes (winner / loser rates)
VERSUS_POINTS_PER_WIN = 5
VERSUS_POINTS_PER_LOSS = 1


def _season_thresholds(season):
    """Flattens a VersusSeason's tiers into {threshold_points: [reward dicts]}."""
    thresholds = {}
    for tier in season.tiers:
        for points, rewards in tier.rewards.items():
            thresholds.setdefault(points, []).extend(r.to_dict() for r in rewards)
    return thresholds


def _grant_rewards_in_session(session, account_id, rewards):
    for reward in rewards:
        rtype = reward.get("rewardType")
        amount = int(reward.get("rewardAmount") or 0)
        if rtype == "Archetype":
            guid = str(reward.get("rewardProductID") or "").lower()
            if not guid:
                continue
            count = max(1, amount)
            item = session.query(Collection).filter_by(
                account_id=account_id, archetype_id=guid).first()
            if item:
                item.nontradable_count += count
            else:
                session.add(Collection(
                    account_id=account_id, archetype_id=guid,
                    tradable_count=0, nontradable_count=count))
        elif rtype == "Tokens" and amount > 0:
            wallet = session.query(Wallet).filter_by(account_id=account_id).first()
            if not wallet:
                wallet = Wallet(account_id=account_id, coins=0, gems=0, tickets=0)
                session.add(wallet)
            currency = (reward.get("rewardCurrency") or "").lower()
            if "gem" in currency:
                wallet.gems += amount
            elif "ticket" in currency:
                wallet.tickets += amount
            else:
                wallet.coins += amount


def get_progress(account_id, season_id):
    """Returns (points, all_time_points) for the account, resetting on season change."""
    try:
        with db_session() as session:
            row = session.query(VersusProgress).filter_by(account_id=account_id).first()
            if not row:
                return 0, 0
            if row.season_id != season_id:
                return 0, row.all_time_points
            return row.points, row.all_time_points
    except Exception as e:
        logging.error(f"[Versus] Failed to read progress for {account_id}: {e}")
        return 0, 0


def award_match_points(account_id, won, season=None):
    """Adds ladder points for a completed match and grants rewards for every
    newly crossed tier threshold. Returns {points, all_time_points, granted}."""
    if season is None:
        from spirit.game.season_manager import VersusSeasonManager
        season = VersusSeasonManager().get_active_season()
    delta = VERSUS_POINTS_PER_WIN if won else VERSUS_POINTS_PER_LOSS
    granted = []
    try:
        with db_session() as session:
            row = session.query(VersusProgress).filter_by(account_id=account_id).first()
            if not row:
                row = VersusProgress(account_id=account_id, season_id="",
                                     points=0, all_time_points=0, granted_json={})
                session.add(row)
            season_id = season.season_id if season else ""
            if row.season_id != season_id:
                row.season_id = season_id
                row.points = 0
                row.granted_json = {}
            old_points = row.points
            row.points = old_points + delta
            row.all_time_points += delta

            if season is not None:
                already = dict(row.granted_json or {})
                for threshold, rewards in sorted(_season_thresholds(season).items()):
                    if threshold <= row.points and str(threshold) not in already:
                        _grant_rewards_in_session(session, account_id, rewards)
                        already[str(threshold)] = True
                        granted.extend(rewards)
                # reassign so the JSONEncodedDict column registers the change
                row.granted_json = already
            return {"points": row.points, "all_time_points": row.all_time_points,
                    "granted": granted}
    except Exception as e:
        logging.error(f"[Versus] Failed to award points to {account_id}: {e}", exc_info=True)
        return {"points": 0, "all_time_points": 0, "granted": []}
