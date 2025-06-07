import argparse

from database import Database


def add_entry(args: argparse.Namespace) -> None:
    """Add a new entry to the database."""
    with Database() as db:
        try:
            entry_id = db.add_entry(args.name, args.email)
            print(f"Added entry with id {entry_id}")
        except ValueError as exc:
            print(f"Error: {exc}")


def list_entries(args: argparse.Namespace) -> None:
    """List all entries in the database."""
    with Database() as db:
        entries = db.list_entries()
        for entry in entries:
            print(entry)


def get_entry(args: argparse.Namespace) -> None:
    """Retrieve a single entry by its ID."""
    with Database() as db:
        entry = db.get_entry(args.entry_id)
        if entry:
            print(entry)
        else:
            print("Entry not found")


def update_entry(args: argparse.Namespace) -> None:
    """Update an existing entry."""
    with Database() as db:
        try:
            db.update_entry(args.entry_id, args.name, args.email)
            print("Entry updated")
        except ValueError as exc:
            print(f"Error: {exc}")


def delete_entry(args: argparse.Namespace) -> None:
    """Delete an entry from the database."""
    with Database() as db:
        try:
            db.delete_entry(args.entry_id)
            print("Entry deleted")
        except ValueError as exc:
            print(f"Error: {exc}")


def main(argv: list[str] | None = None) -> None:
    """Run the command-line interface using argparse."""
    parser = argparse.ArgumentParser(description="Simple CRUD app with SQLite")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new entry")
    add_parser.add_argument("name")
    add_parser.add_argument("email")
    add_parser.set_defaults(func=add_entry)

    list_parser = subparsers.add_parser("list", help="List all entries")
    list_parser.set_defaults(func=list_entries)

    get_parser = subparsers.add_parser("get", help="Retrieve a single entry")
    get_parser.add_argument("entry_id", type=int)
    get_parser.set_defaults(func=get_entry)

    update_parser = subparsers.add_parser("update", help="Update an entry")
    update_parser.add_argument("entry_id", type=int)
    update_parser.add_argument("name")
    update_parser.add_argument("email")
    update_parser.set_defaults(func=update_entry)

    delete_parser = subparsers.add_parser("delete", help="Delete an entry")
    delete_parser.add_argument("entry_id", type=int)
    delete_parser.set_defaults(func=delete_entry)

    args = parser.parse_args(argv)
    args.func(args)

if __name__ == "__main__":
    main()
