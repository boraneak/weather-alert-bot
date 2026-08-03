from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class AlertSettings(Base):
    __tablename__ = "alert_settings"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True,
    )

    alerts_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    hot_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    hot_threshold_c: Mapped[float] = mapped_column(
        Float,
        default=35.0,
    )

    hot_cooldown_minutes: Mapped[int] = mapped_column(
        Integer,
        default=120,
    )

    rain_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    rain_probability_threshold: Mapped[float] = mapped_column(
        Float,
        default=0.50,
    )

    rain_within_minutes: Mapped[int] = mapped_column(
        Integer,
        default=60,
    )

    rain_cooldown_minutes: Mapped[int] = mapped_column(
        Integer,
        default=45,
    )

    aqi_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    aqi_threshold: Mapped[int] = mapped_column(
        Integer,
        default=100,
    )

    aqi_cooldown_minutes: Mapped[int] = mapped_column(
        Integer,
        default=60,
    )

    last_hot_alert_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    last_rain_alert_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    last_aqi_alert_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        back_populates="alert_settings",
    )
