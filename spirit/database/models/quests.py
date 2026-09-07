import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from spirit.database.base import Base
from spirit.database.models.inventory import JSONEncodedDict


class QuestAccount(Base):
    __tablename__ = "quest_accounts"

    account_id: Mapped[str] = mapped_column(ForeignKey("accounts.account_id"), primary_key=True)
    enabled: Mapped[bool] = mapped_column(default=True)
    selected_date: Mapped[datetime.date | None] = mapped_column(nullable=True)
    affinity_xp: Mapped[dict] = mapped_column(JSONEncodedDict, default=dict)


class DailyQuest(Base):
    __tablename__ = "daily_quests"

    quest_id: Mapped[str] = mapped_column(primary_key=True)
    account_id: Mapped[str] = mapped_column(ForeignKey("accounts.account_id"), index=True)
    offered_date: Mapped[datetime.date] = mapped_column()
    status: Mapped[str] = mapped_column(default="available")
    definition: Mapped[dict] = mapped_column(JSONEncodedDict)
    activations: Mapped[int] = mapped_column(default=0)
    accepted_at: Mapped[float | None] = mapped_column(nullable=True)


class QuestMatchCredit(Base):
    __tablename__ = "quest_match_credits"

    account_id: Mapped[str] = mapped_column(ForeignKey("accounts.account_id"), primary_key=True)
    game_id: Mapped[str] = mapped_column(primary_key=True)
