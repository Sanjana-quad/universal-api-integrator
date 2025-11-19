import yaml
from pathlib import Path
from src.logger.logger import get_logger

log = get_logger("yaml_parser")

def load_yaml(path: str):
    try:
        path = Path(path)
        if not path.exists():
            log.error(f"YAML file not found: {path}")
            return None

        with path.open() as f:
            data = yaml.safe_load(f)

        log.info(f"Loaded YAML: {path}")
        return data

    except yaml.YAMLError:
        log.exception("Invalid YAML format")
        return None
def save_yaml(data: dict, path: str):
    try:
        path = Path(path)
        with path.open('w') as f:
            yaml.safe_dump(data, f)

        log.info(f"Saved YAML: {path}")

    except Exception:
        log.exception("Failed to save YAML")