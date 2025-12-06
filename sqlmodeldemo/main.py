import logging
import argparse
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
    subparsers.add_parser(
        "initdb", help="Initialization step. A new database is created")
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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    args = parse_cmd_args()
    logging.info(f"Parsed arguments: {args}")
    crud_funcs = CrudFuncs(connection_string=SQLITE_URL)
    if args.command == "seed":
        crud_funcs.seed()
        logging.info("Database seeded successfully.")
    elif args.command == "initdb":
        crud_funcs.init_db()
        logging.info("Database initialized successfully.")
    elif args.command == "listall":
        all_heroes = crud_funcs.list_heroes()
        for hero in all_heroes:
            logging.info(hero)
        logging.info(f"Total heroes listed: {len(all_heroes)}")
    elif args.command == "delete":
        logging.info(f"Deleted hero with ID {args.id}")
        _delete_status = crud_funcs.delete_hero(hero_id=int(args.id))
        logging.info(f"Delete of ID={args.id} returned {_delete_status}")
    elif args.command == "update":
        logging.info(f"Update hero with ID {args.id}")
        crud_funcs.update_hero_age(hero_id=args.id, age=args.age)
        logging.info(f"Updated hero ID={args.id} to age={args.age}")
    else:
        raise ValueError(f"Unsupported argument {args}")
    exit(0)
