import json
from pathlib import Path
from src.logger.logger import get_logger

log = get_logger("json_parser")

def load_json(path: str):
    """Load JSON file and return dict."""
    try:
        path = Path(path)
        if not path.exists():
            log.error(f"File not found: {path}")
            return None
        
        with path.open() as f:
            data = json.load(f)
        
        log.info(f"Loaded JSON: {path}")
        return data
    
    except json.JSONDecodeError as e:
        log.exception(f"Invalid JSON format: {path}")
        return None
