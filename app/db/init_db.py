import app.models  # noqa: F401
from app.db.base import Base
from app.db.database import engine


def init_database() -> None:
    """Create all database tables."""

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()
    print("Database initialized")
