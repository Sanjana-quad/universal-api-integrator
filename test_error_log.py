from src.logger.logger import get_logger

log = get_logger("error_test")

def divide(a, b):
    return a / b

try:
    divide(10, 0)
except Exception as e:
    log.exception("Something went wrong during division!")
