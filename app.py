import click

from database import Database


@click.group()
def cli() -> None:
    """Simple CRUD app with SQLite"""


@cli.command()
@click.argument("name")
@click.argument("email")
def add(name: str, email: str) -> None:
    """Add a new entry to the database."""
    with Database() as db:
        try:
            entry_id = db.add_entry(name, email)
            click.echo(f"Added entry with id {entry_id}")
        except ValueError as exc:
            click.echo(f"Error: {exc}")


@cli.command(name="list")
def list_entries() -> None:
    """List all entries in the database."""
    with Database() as db:
        entries = db.list_entries()
        for entry in entries:
            click.echo(entry)


@cli.command()
@click.argument("entry_id", type=int)
def get(entry_id: int) -> None:
    """Retrieve a single entry by its ID."""
    with Database() as db:
        entry = db.get_entry(entry_id)
        if entry:
            click.echo(entry)
        else:
            click.echo("Entry not found")


@cli.command()
@click.argument("entry_id", type=int)
@click.argument("name")
@click.argument("email")
def update(entry_id: int, name: str, email: str) -> None:
    """Update an existing entry."""
    with Database() as db:
        try:
            db.update_entry(entry_id, name, email)
            click.echo("Entry updated")
        except ValueError as exc:
            click.echo(f"Error: {exc}")


@cli.command()
@click.argument("entry_id", type=int)
def delete(entry_id: int) -> None:
    """Delete an entry from the database."""
    with Database() as db:
        try:
            db.delete_entry(entry_id)
            click.echo("Entry deleted")
        except ValueError as exc:
            click.echo(f"Error: {exc}")


if __name__ == "__main__":
    cli()
