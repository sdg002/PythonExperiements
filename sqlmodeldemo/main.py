from typing import Iterable, List, Optional
import argparse
from sqlmodel import SQLModel, create_engine
import sqlmodel as sqm
from sqlmodeldemo.hero_model import Hero
from sqlmodeldemo.crudfuncs import CrudFuncs

SQLITE_URL = "sqlite:///database.db"


def parse_cmd_args() -> argparse.Namespace:
    """Parses command-line arguments for the script."""
    parser = argparse.ArgumentParser(
        description="Command-line tool for managing records.")

    # Subcommands
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands")

    # Command: seed
    subparsers.add_parser("seed", help="Seed the database with initial data")

    # Command: update
    update_parser = subparsers.add_parser("update", help="Update a record")
    update_parser.add_argument(
        "--id", type=int, required=True, help="ID of the record to update")
    update_parser.add_argument(
        "--age", type=int, required=True, help="New age for the record")

    # Command: delete
    delete_parser = subparsers.add_parser("delete", help="Delete a record")
    delete_parser.add_argument(
        "--id", type=int, required=True, help="ID of the record to delete")

    # Command: listall
    subparsers.add_parser("listall", help="List all records")

    # Command: get
    get_parser = subparsers.add_parser(
        "get", help="Get details of a specific record")
    get_parser.add_argument("--id", type=int, required=True,
                            help="ID of the record to retrieve")

    # Parse the arguments
    _args = parser.parse_args()
    return _args


def init_db() -> None:
    SQLModel.metadata.create_all(engine, tables=[Hero.__table__])
    # empty tables parameter - will not automatically create any table


def create_heroes(heroes: Iterable[Hero]) -> None:
    with sqm.Session(engine) as session:
        for hero in heroes:
            session.add(hero)
        session.commit()


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
    args = parse_cmd_args()
    print(args)
    crud_funcs = CrudFuncs(connection_string=SQLITE_URL)
    if args.command == "seed":
        engine = create_engine(SQLITE_URL, echo=True)
        seed()
        print("Database seeded.")
    elif args.command == "listall":
        all_heroes = crud_funcs.list_heroes()
        for hero in all_heroes:
            print(hero)
    elif args.command == "delete":
        print(f"Deleted hero with ID {args.id}")
        crud_funcs.delete_hero(hero_id=args.id)
    elif args.command == "update":
        print(f"Update hero with ID {args.id}")
        raise NotImplementedError("Update command not implemented yet.")
        # engine = create_engine(SQLITE_URL, echo=True)
        # updated_hero = update_hero_age(args.id, args.age)
        # if updated_hero:
        #     print(f"Updated Hero: {updated_hero}")
        # else:
        #     print(f"No hero found with ID {args.id}")
    else:
        raise ValueError(f"Unsupported argument {args}")
    exit(0)
    init_db()
    print("This is the main module for sqlmodel.main")
    seed()
    print("All done")
    update_hero_age(all_heroes[0].id, 999)
