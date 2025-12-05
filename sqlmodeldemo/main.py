import logging
from typing import Iterable, Optional
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
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    args = parse_cmd_args()
    logging.info(f"Parsed arguments: {args}")
    crud_funcs = CrudFuncs(connection_string=SQLITE_URL)
    if args.command == "seed":
        crud_funcs.seed()
        logging.info("Database seeded successfully.")
    elif args.command == "listall":
        all_heroes = crud_funcs.list_heroes()
        for hero in all_heroes:
            logging.info(hero)
    elif args.command == "delete":
        logging.info(f"Deleted hero with ID {args.id}")
        delete_status = crud_funcs.delete_hero(hero_id=args.id)
        logging.info(f"Delete of ID={args.id} returned {delete_status}")
    elif args.command == "update":
        logging.info(f"Update hero with ID {args.id}")
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
