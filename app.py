import os
import sqlite3
from dataclasses import dataclass
from typing import List
import argparse

DB_NAME = os.getenv('DB_NAME', 'crudex.db')

@dataclass
class Entry:
    id: int
    name: str
    email: str

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DB_NAME)
        self.connection.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self) -> None:
        with self.connection:
            self.connection.execute(
                'CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)'
            )

    def add_entry(self, name: str, email: str) -> int:
        cursor = self.connection.execute(
            'INSERT INTO entries (name, email) VALUES (?, ?)',
            (name, email),
        )
        self.connection.commit()
        return cursor.lastrowid

    def list_entries(self) -> List[Entry]:
        cursor = self.connection.execute('SELECT id, name, email FROM entries')
        rows = cursor.fetchall()
        return [Entry(id=row['id'], name=row['name'], email=row['email']) for row in rows]

    def update_entry(self, entry_id: int, name: str, email: str) -> None:
        self.connection.execute(
            'UPDATE entries SET name = ?, email = ? WHERE id = ?',
            (name, email, entry_id),
        )
        self.connection.commit()

    def delete_entry(self, entry_id: int) -> None:
        self.connection.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
        self.connection.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description='Simple CRUD app with SQLite')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new entry')
    add_parser.add_argument('name')
    add_parser.add_argument('email')

    list_parser = subparsers.add_parser('list', help='List all entries')

    update_parser = subparsers.add_parser('update', help='Update an entry')
    update_parser.add_argument('id', type=int)
    update_parser.add_argument('name')
    update_parser.add_argument('email')

    delete_parser = subparsers.add_parser('delete', help='Delete an entry')
    delete_parser.add_argument('id', type=int)

    args = parser.parse_args()
    db = Database()

    if args.command == 'add':
        entry_id = db.add_entry(args.name, args.email)
        print(f'Added entry with id {entry_id}')
    elif args.command == 'list':
        entries = db.list_entries()
        for e in entries:
            print(e)
    elif args.command == 'update':
        db.update_entry(args.id, args.name, args.email)
        print('Entry updated')
    elif args.command == 'delete':
        db.delete_entry(args.id)
        print('Entry deleted')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
