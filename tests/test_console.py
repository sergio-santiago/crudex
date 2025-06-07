import importlib
import os

from database import Database


def test_interactive_menu_add_entry(monkeypatch, tmp_path):
    db_path = tmp_path / 'console.db'
    monkeypatch.setenv('CRUDEX_DB', str(db_path))
    import console
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

    with Database() as db:
        entries = db.list_entries()
        assert len(entries) == 1
        assert entries[0].name == 'Alice'
        assert entries[0].email == 'alice@example.com'
