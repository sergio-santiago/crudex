import importlib
import os

import app
from database import Database
import pytest


def test_crud_operations(tmp_path, monkeypatch):
    db_path = tmp_path / 'test.db'
    monkeypatch.setenv('CRUDEX_DB', str(db_path))
    importlib.reload(app)
    with Database() as db:
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

def test_error_cases(tmp_path, monkeypatch):
    db_path = tmp_path / 'error.db'
    monkeypatch.setenv('CRUDEX_DB', str(db_path))
    with Database() as db:
        db.add_entry('John', 'john@example.com')
        with pytest.raises(ValueError):
            db.add_entry('Duplicate', 'john@example.com')
        with pytest.raises(ValueError):
            db.update_entry(999, 'Missing', 'missing@example.com')
        with pytest.raises(ValueError):
            db.delete_entry(999)
