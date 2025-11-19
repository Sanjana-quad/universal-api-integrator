from src.logger.logger import get_logger

log = get_logger("test_levels")

log.debug("Debug message")
log.info("Info message")
log.warning("Warning!")
log.error("Error occurred")
log.critical("Critical failure")
