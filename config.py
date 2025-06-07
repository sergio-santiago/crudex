import json
import os
from pathlib import Path

DEFAULT_DB = "crudex.db"


def get_db_path() -> str:
    env_path = os.getenv("CRUDEX_DB")
    if env_path:
        return env_path

    config_file = Path(os.getenv("CRUDEX_CONFIG", "config.json"))
    if config_file.is_file():
        with open(config_file) as fh:
            data = json.load(fh)
            if isinstance(data, dict) and data.get("db_path"):
                return str(data["db_path"])
    return DEFAULT_DB
