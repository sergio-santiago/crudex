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

    # Get
    single = db.get_entry(entry_id)
    assert single is not None
    assert single.name == 'John'

    # Update
    db.update_entry(entry_id, 'Jane', 'jane@example.com')
    updated = db.list_entries()[0]
    assert updated.name == 'Jane'
    assert updated.email == 'jane@example.com'

    # Get after update
    updated_single = db.get_entry(entry_id)
    assert updated_single is not None
    assert updated_single.name == 'Jane'
    assert updated_single.email == 'jane@example.com'

    # Delete
    db.delete_entry(entry_id)
    assert db.list_entries() == []
    assert db.get_entry(entry_id) is None
