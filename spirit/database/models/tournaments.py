import datetime
from sqlalchemy import func, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from spirit.database.base import Base
from spirit.database.models.inventory import JSONEncodedDict


class AsyncTournament(Base):
    __tablename__ = 'async_tournaments'

    tournament_id: Mapped[str] = mapped_column(primary_key=True)
    # Full admin-shaped definition (times in epoch ms, run/leaderboard configs,
    # rich reward dicts in the versus Reward shape for granting)
    definition_json: Mapped[dict] = mapped_column(JSONEncodedDict, nullable=False)
    enabled: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class TournamentEntry(Base):
    __tablename__ = 'tournament_entries'

    entry_id: Mapped[str] = mapped_column(primary_key=True)
    tournament_id: Mapped[str] = mapped_column(ForeignKey('async_tournaments.tournament_id'), nullable=False, index=True)
    account_id: Mapped[str] = mapped_column(nullable=False, index=True)
    # SerializableDeck snapshot taken at join time
    deck_json: Mapped[dict] = mapped_column(JSONEncodedDict, default=dict)
    wins: Mapped[int] = mapped_column(default=0)
    losses: Mapped[int] = mapped_column(default=0)
    tiebreakers: Mapped[int] = mapped_column(default=0)
    status: Mapped[str] = mapped_column(default="active")  # active | complete | resigned
    rewards_claimed: Mapped[bool] = mapped_column(default=False)
    # [{"opponentID", "opponentName", "gameResult"}] in play order
    history_json: Mapped[list] = mapped_column(JSONEncodedDict, default=list)
    last_update: Mapped[int] = mapped_column(default=0)  # epoch ms
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class TournamentLeaderboardClaim(Base):
    __tablename__ = 'tournament_leaderboard_claims'
    __table_args__ = (UniqueConstraint('tournament_id', 'account_id'),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tournament_id: Mapped[str] = mapped_column(nullable=False)
    account_id: Mapped[str] = mapped_column(nullable=False)
    rank: Mapped[int] = mapped_column(default=0)
    claimed_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
