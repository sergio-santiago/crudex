import sqlite3
from dataclasses import dataclass
from typing import List, Optional
from contextlib import contextmanager

from config import get_db_path


@dataclass
class Entry:
    id: int
    name: str
    email: str


class Database:
    """SQLite wrapper providing CRUD operations."""

    def __init__(self, db_path: Optional[str] = None) -> None:
        self.db_path = db_path or get_db_path()
        self.connection: Optional[sqlite3.Connection] = None

    def __enter__(self) -> "Database":
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.create_table()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self.connection:
            self.connection.close()

    # context manager for convenience
    @contextmanager
    def connect(self) -> sqlite3.Connection:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            yield conn

    def create_table(self) -> None:
        if not self.connection:
            return
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT UNIQUE
                )
                """
            )

    def add_entry(self, name: str, email: str) -> int:
        if not self.connection:
            raise RuntimeError("Database connection is not open")
        try:
            cursor = self.connection.execute(
                "INSERT INTO entries (name, email) VALUES (?, ?)",
                (name, email),
            )
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as exc:
            raise ValueError("Duplicate entry") from exc

    def list_entries(self) -> List[Entry]:
        if not self.connection:
            raise RuntimeError("Database connection is not open")
        cursor = self.connection.execute("SELECT id, name, email FROM entries")
        rows = cursor.fetchall()
        return [Entry(id=row["id"], name=row["name"], email=row["email"]) for row in rows]

    def get_entry(self, entry_id: int) -> Optional[Entry]:
        if not self.connection:
            raise RuntimeError("Database connection is not open")
        cursor = self.connection.execute(
            "SELECT id, name, email FROM entries WHERE id = ?",
            (entry_id,),
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return Entry(id=row["id"], name=row["name"], email=row["email"])

    def update_entry(self, entry_id: int, name: str, email: str) -> None:
        if not self.connection:
            raise RuntimeError("Database connection is not open")
        cursor = self.connection.execute(
            "UPDATE entries SET name = ?, email = ? WHERE id = ?",
            (name, email, entry_id),
        )
        self.connection.commit()
        if cursor.rowcount == 0:
            raise ValueError("Entry not found")

    def delete_entry(self, entry_id: int) -> None:
        if not self.connection:
            raise RuntimeError("Database connection is not open")
        cursor = self.connection.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
        self.connection.commit()
        if cursor.rowcount == 0:
            raise ValueError("Entry not found")
