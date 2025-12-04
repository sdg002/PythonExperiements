from typing import Iterable, List
from sqlmodel import SQLModel, create_engine
from sqlmodeldemo.hero_model import Hero
import sqlmodel as sqm

SQLITE_URL = "sqlite:///database.db"


def init_db() -> None:
    SQLModel.metadata.create_all(engine, tables=[Hero.__table__])
    # empty tables parameter - will not automatically create any table


def create_heroes(heroes: Iterable[Hero]) -> None:
    with sqm.Session(engine) as session:
        for hero in heroes:
            session.add(hero)
        session.commit()


def list_heroes() -> List[Hero]:
    with sqm.Session(engine) as session:
        statement = sqm.select(Hero)
        return session.exec(statement).all()


def seed() -> None:
    heroes = [
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=15),
        Hero(name="Captain North", secret_name="Bob Canada"),
        Hero(name="Madame Invisible", secret_name="Jane Doe", age=32),
    ]
    create_heroes(heroes)


if __name__ == "__main__":
    engine = create_engine(SQLITE_URL, echo=True)
    init_db()
    print("This is the main module for sqlmodel.main")
    seed()
    heroes = list_heroes()
    for hero in heroes:
        print(hero)
    print("All done")
