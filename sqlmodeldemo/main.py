from typing import Iterable, List, Optional
from sqlmodel import SQLModel, create_engine
import sqlmodel as sqm
from sqlmodeldemo.hero_model import Hero

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


def update_hero_age(hero_id: int, age: int) -> Optional[Hero]:
    with sqm.Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            return None
        hero.age = age
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero


if __name__ == "__main__":
    engine = create_engine(SQLITE_URL, echo=True)
    init_db()
    print("This is the main module for sqlmodel.main")
    seed()
    all_heroes = list_heroes()
    for hero in all_heroes:
        print(hero)
    print("All done")
    update_hero_age(all_heroes[0].id, 999)
