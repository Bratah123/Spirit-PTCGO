import json
from sqlalchemy import ForeignKey, TypeDecorator, TEXT
from sqlalchemy.orm import relationship, Mapped, mapped_column
from spirit.database.base import Base

class JSONEncodedDict(TypeDecorator):
    """Represents an immutable structure as a JSON-encoded string in SQLite."""
    impl = TEXT
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            return json.dumps(value)
        return None

    def process_result_value(self, value, dialect):
        if value is not None:
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError):
                return {}
        return {}

class Wallet(Base):
    __tablename__ = 'wallets'

    account_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), primary_key=True)
    coins: Mapped[int] = mapped_column(default=1000)
    gems: Mapped[int] = mapped_column(default=0)
    tickets: Mapped[int] = mapped_column(default=100)

    # Relationship back to Account
    account = relationship("Account", back_populates="wallet")

class Deck(Base):
    __tablename__ = 'decks'

    id: Mapped[str] = mapped_column(primary_key=True)
    account_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), nullable=False, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    deck_data: Mapped[dict] = mapped_column(JSONEncodedDict, nullable=False)
    is_avatar: Mapped[bool] = mapped_column(default=False)
    overall_wins: Mapped[int] = mapped_column(default=0)
    overall_played: Mapped[int] = mapped_column(default=0)
    wins_since_last_edit: Mapped[int] = mapped_column(default=0)
    played_since_last_edit: Mapped[int] = mapped_column(default=0)

    # Relationship back to Account
    account = relationship("Account", back_populates="decks")

class Collection(Base):
    __tablename__ = 'collection'

    account_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), primary_key=True)
    archetype_id: Mapped[str] = mapped_column(primary_key=True)
    tradable_count: Mapped[int] = mapped_column(default=0)
    nontradable_count: Mapped[int] = mapped_column(default=0)

    # Relationship back to Account
    account = relationship("Account", back_populates="collections")

class ArchetypeFlag(Base):
    __tablename__ = 'archetype_flags'

    account_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), primary_key=True)
    archetype_id: Mapped[str] = mapped_column(primary_key=True)
    wanted: Mapped[int] = mapped_column(default=0)
    for_trade: Mapped[int] = mapped_column(default=0)
    review: Mapped[int] = mapped_column(default=0)

    # Relationship back to Account
    account = relationship("Account", back_populates="archetype_flags")
