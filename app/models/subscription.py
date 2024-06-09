from typing import List, Optional
from datetime import datetime, timedelta

from .base import Base
from .db_enums import SubscriptionType

from aiogram import html
from aiogram.utils.link import create_tg_link

from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Subscriptions(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[SubscriptionType] = mapped_column(default=SubscriptionType.STANDART)
    expire_date: Mapped[datetime] = mapped_column(default=func.now())
    account_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    account: Mapped["Users"] = relationship(backref="subscriptions", single_parent=True)

    def set_expire_date(self) -> None:

        if self.type != SubscriptionType.STANDART:
            self.expire_date = func.now() + timedelta(month=1)
