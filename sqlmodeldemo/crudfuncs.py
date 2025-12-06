import logging
from typing import Iterable, Optional
import sqlmodel as sqm
from sqlmodeldemo.hero_model import Hero


class CrudFuncs:
    """
    CRUD functions for Hero model.
    """

    def __init__(self, connection_string: str):
        self.engine = sqm.create_engine(connection_string, echo=True)
        logging.info(
            f"Engine created with connection string: {connection_string}")

    def init_db(self) -> None:
        sqm.SQLModel.metadata.create_all(self.engine, tables=[Hero.__table__])
        # empty tables parameter - will not automatically create any table

    def delete_hero(self, hero_id: int) -> bool:
        logging.info(f"Deleting hero with ID: {hero_id}")
        with sqm.Session(self.engine) as session:
            hero = session.get(Hero, hero_id)
            if not hero:
                return False
            session.delete(hero)
            session.commit()
        return True

    def list_heroes(self) -> list[Hero]:
        with sqm.Session(self.engine) as session:
            statement = sqm.select(Hero)
            return session.exec(statement).all()

    def create_heroes(self, heroes: Iterable[Hero]) -> None:
        with sqm.Session(self.engine) as session:
            for hero in heroes:
                session.add(hero)
            session.commit()

    def seed(self) -> None:
        heroes = [
            Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=15),
            Hero(name="Captain North", secret_name="Bob Canada"),
            Hero(name="Madame Invisible", secret_name="Jane Doe", age=32),
        ]
        self.create_heroes(heroes)
        logging.info(f"Database seeded with {len(heroes)} heroes.")

    def update_hero_age(self, hero_id: int, age: int) -> Optional[Hero]:
        with sqm.Session(self.engine) as session:
            hero = session.get(Hero, hero_id)
            if not hero:
                return None
            hero.age = age
            session.add(hero)
            session.commit()
            session.refresh(hero)
            return hero
