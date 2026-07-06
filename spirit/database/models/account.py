import datetime
from sqlalchemy import func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from spirit.database.base import Base
from spirit.database.models.inventory import JSONEncodedDict

class Account(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account_id: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    screen_name: Mapped[str | None] = mapped_column(nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    # Client-persisted settings dict {settingNumber: value} (attr 10230)
    settings_json: Mapped[dict] = mapped_column(JSONEncodedDict, default=dict)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    # Relationships
    wallet = relationship("Wallet", uselist=False, back_populates="account", cascade="all, delete-orphan")
    decks = relationship("Deck", back_populates="account", cascade="all, delete-orphan")
    collections = relationship("Collection", back_populates="account", cascade="all, delete-orphan")
    archetype_flags = relationship("ArchetypeFlag", back_populates="account", cascade="all, delete-orphan")
