import importlib
import os

import console
from app import Database


def test_interactive_menu_add_entry(monkeypatch, tmp_path):
    db_path = tmp_path / 'console.db'
    monkeypatch.setenv('DB_NAME', str(db_path))
    importlib.reload(console)

    inputs = iter([
        '1',
        'Alice',
        'alice@example.com',
        '',
        '6'
    ])
    monkeypatch.setattr('builtins.input', lambda *args: next(inputs))
    monkeypatch.setattr('os.system', lambda *args, **kwargs: None)

    console.interactive_menu()

    db = Database()
    entries = db.list_entries()
    assert len(entries) == 1
    assert entries[0].name == 'Alice'
    assert entries[0].email == 'alice@example.com'
