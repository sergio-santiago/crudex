import importlib
import os

import app


def test_crud_operations(tmp_path, monkeypatch):
    db_path = tmp_path / 'test.db'
    monkeypatch.setenv('DB_NAME', str(db_path))
    importlib.reload(app)
    db = app.Database()

    # Add
    entry_id = db.add_entry('John', 'john@example.com')
    assert entry_id == 1

    # List
    entries = db.list_entries()
    assert len(entries) == 1
    assert entries[0].name == 'John'
    assert entries[0].email == 'john@example.com'

    # Update
    db.update_entry(entry_id, 'Jane', 'jane@example.com')
    updated = db.list_entries()[0]
    assert updated.name == 'Jane'
    assert updated.email == 'jane@example.com'

    # Delete
    db.delete_entry(entry_id)
    assert db.list_entries() == []
