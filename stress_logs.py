from src.logger.logger import get_logger

log = get_logger("stress")

for i in range(50_000):
    log.info(f"Log line {i}")
