import csv
from pathlib import Path
from src.logger.logger import get_logger

log = get_logger("csv_parser")

def load_csv(path: str):
    try:
        path = Path(path)
        if not path.exists():
            log.error(f"CSV file not found: {path}")
            return None

        with path.open() as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        log.info(f"Loaded CSV with {len(rows)} rows")
        return rows

    except Exception:
        log.exception("CSV parsing failed")
        return None
