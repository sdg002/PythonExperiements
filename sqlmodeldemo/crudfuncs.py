import logging
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
