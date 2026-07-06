from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from spirit.database.base import Base

class Friendship(Base):
    __tablename__ = 'friends'

    account_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), primary_key=True)
    friend_id: Mapped[str] = mapped_column(ForeignKey('accounts.account_id'), primary_key=True)
    status: Mapped[int] = mapped_column(nullable=False)
