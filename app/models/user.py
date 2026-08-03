from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.alert_settings import AlertSettings
    from app.models.location import UserLocation


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    telegram_user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        index=True,
    )

    display_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    location: Mapped["UserLocation"] = relationship(
        back_populates="user",
        uselist=False,
    )

    alert_settings: Mapped["AlertSettings"] = relationship(
        back_populates="user",
        uselist=False,
    )
