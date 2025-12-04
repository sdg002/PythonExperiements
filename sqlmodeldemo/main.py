import sys
from sqlmodel import SQLModel, create_engine
from sqlmodeldemo.hero_model import Hero

SQLITE_URL = "sqlite:///database.db"


def init_db() -> None:
    engine = create_engine(SQLITE_URL, echo=True)
    SQLModel.metadata.create_all(engine, tables=[Hero.__table__])
    # empty tables parameter - will not automatically create any table


if __name__ == "__main__":
    init_db()
    print("This is the main module for sqlmodel.main")
