from src.logger.logger import get_logger
log = get_logger("calculator")

def add(a, b):
    log.debug(f"Adding {a} and {b}")
    return a + b
