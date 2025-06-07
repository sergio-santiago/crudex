import os
import psycopg2
from dataclasses import dataclass
from typing import List
import argparse

DB_NAME = os.getenv('DB_NAME', 'crudex')
DB_USER = os.getenv('DB_USER', 'crudex')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'crudexpass')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_PORT = int(os.getenv('DB_PORT', '5432'))

@dataclass
class Entry:
    id: int
    name: str
    email: str

class Database:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        self.connection.autocommit = True
        self.create_table()

    def create_table(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS entries (id SERIAL PRIMARY KEY, name TEXT, email TEXT)'
            )

    def add_entry(self, name: str, email: str) -> int:
        with self.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO entries (name, email) VALUES (%s, %s) RETURNING id',
                (name, email),
            )
            entry_id = cursor.fetchone()[0]
        return entry_id

    def list_entries(self) -> List[Entry]:
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT id, name, email FROM entries')
            rows = cursor.fetchall()
            return [Entry(id=row[0], name=row[1], email=row[2]) for row in rows]

    def update_entry(self, entry_id: int, name: str, email: str) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                'UPDATE entries SET name = %s, email = %s WHERE id = %s',
                (name, email, entry_id),
            )

    def delete_entry(self, entry_id: int) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM entries WHERE id = %s', (entry_id,))


def main() -> None:
    parser = argparse.ArgumentParser(description='Simple CRUD app with PostgreSQL')
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
