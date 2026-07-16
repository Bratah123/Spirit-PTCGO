from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from spirit.database.base import Base

class Friendship(Base):
    __tablename__ = 'friends'

    account_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), primary_key=True)
    # index: the composite PK (account_id, friend_id) cannot serve friend_id-first
    # lookups (incoming-invite queries filter on friend_id).
    friend_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), primary_key=True, index=True)
    status: Mapped[int] = mapped_column(nullable=False)
