import datetime
from sqlalchemy import func, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from spirit.database.base import Base
from spirit.database.models.inventory import JSONEncodedDict


class RedemptionCode(Base):
    __tablename__ = 'redemption_codes'

    code_string: Mapped[str] = mapped_column(primary_key=True)
    # {"products": {archetype_guid: count}, "coins": n, "gems": n, "tickets": n}
    reward_json: Mapped[dict] = mapped_column(JSONEncodedDict, nullable=False)
    max_uses: Mapped[int] = mapped_column(default=1)  # 0 = unlimited
    current_uses: Mapped[int] = mapped_column(default=0)
    enabled: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class CodeRedemptionEntry(Base):
    __tablename__ = 'code_redemption_entries'
    __table_args__ = (UniqueConstraint('code_string', 'account_id'),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code_string: Mapped[str] = mapped_column(ForeignKey('redemption_codes.code_string'), nullable=False)
    account_id: Mapped[str] = mapped_column(nullable=False)
    redeemed_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class ShopItem(Base):
    __tablename__ = 'shop_items'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_guid: Mapped[str] = mapped_column(unique=True, nullable=False)
    display_name: Mapped[str] = mapped_column(default="")
    currency: Mapped[int] = mapped_column(default=-1784319558)  # AttrID.TRAINER_TOKENS
    price: Mapped[int] = mapped_column(default=200)
    enabled: Mapped[bool] = mapped_column(default=True)
    featured: Mapped[bool] = mapped_column(default=False)
    top_selling: Mapped[bool] = mapped_column(default=False)
    sort_order: Mapped[int] = mapped_column(default=0)


class TradeOffer(Base):
    __tablename__ = 'trade_offers'
    # Composite indexes for the public/private/my-lots tab filters (status + owner).
    __table_args__ = (
        Index('ix_trade_offers_status_created', 'status', 'created_at'),
        Index('ix_trade_offers_status_recipient', 'status', 'recipient_id'),
        Index('ix_trade_offers_status_sender', 'status', 'sender_id'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    offer_id: Mapped[str] = mapped_column(unique=True, nullable=False)
    sender_id: Mapped[str] = mapped_column(nullable=False, index=True)
    recipient_id: Mapped[str | None] = mapped_column(nullable=True, index=True)  # None = public offer
    # {archetype_guid: count}
    offering_json: Mapped[dict] = mapped_column(JSONEncodedDict, nullable=False)
    requesting_json: Mapped[dict] = mapped_column(JSONEncodedDict, nullable=False)
    status: Mapped[str] = mapped_column(default="open")  # open | accepted | cancelled | declined
    accepted_by: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class VersusProgress(Base):
    __tablename__ = 'versus_progress'

    account_id: Mapped[str] = mapped_column(primary_key=True)
    season_id: Mapped[str] = mapped_column(default="")
    points: Mapped[int] = mapped_column(default=0)
    all_time_points: Mapped[int] = mapped_column(default=0)
    # {str(threshold): true} thresholds whose rewards were already granted
    granted_json: Mapped[dict] = mapped_column(JSONEncodedDict, default=dict)


class DynamicPage(Base):
    __tablename__ = 'dynamic_pages'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # "landing" (login carousel) or "maintenance"
    page_type: Mapped[str] = mapped_column(default="landing")
    sort_order: Mapped[int] = mapped_column(default=0)
    # Full client page object (template, labels, images, actions, ...)
    content_json: Mapped[dict] = mapped_column(JSONEncodedDict, nullable=False)
    enabled: Mapped[bool] = mapped_column(default=True)


class DailyLoginProgress(Base):
    __tablename__ = 'daily_login_progress'

    account_id: Mapped[str] = mapped_column(primary_key=True)
    last_claim_date: Mapped[datetime.date | None] = mapped_column(nullable=True)
    # consecutive-day counter (resets on a missed day)
    streak: Mapped[int] = mapped_column(default=0)
    # lifetime claim count; client shows the 3-slot newbie dialog while <= 3
    activations: Mapped[int] = mapped_column(default=0)

