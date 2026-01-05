import yaml
from src.utility import open_log_file

def load_config(config_path: str):
    if not config_path:
        return {}

    with open_log_file(config_path) as f:
        return yaml.safe_load(f) or {}