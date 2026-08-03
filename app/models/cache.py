from datetime import datetime

from sqlalchemy import JSON, DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class WeatherCache(Base):
    __tablename__ = "api_cache_weather"

    id: Mapped[int] = mapped_column(primary_key=True)

    location_key: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    lat: Mapped[float] = mapped_column(
        Float,
    )

    lon: Mapped[float] = mapped_column(
        Float,
    )

    payload: Mapped[dict] = mapped_column(
        JSON,
    )

    fetched_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
    )


class AirCache(Base):
    __tablename__ = "api_cache_air"

    id: Mapped[int] = mapped_column(primary_key=True)

    location_key: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    payload: Mapped[dict] = mapped_column(
        JSON,
    )

    fetched_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
    )
