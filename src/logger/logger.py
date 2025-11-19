# import logging
# from logging.handlers import RotatingFileHandler
# import os

# def get_logger(name: str):

#     os.makedirs("logs", exist_ok=True)

#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)

#     handler = RotatingFileHandler(
#         "logs/app.log", maxBytes=5_000_000, backupCount=3
#     )
#     handler.setLevel(logging.DEBUG)

#     fmt = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
#     handler.setFormatter(logging.Formatter(fmt))

#     if not logger.handlers:
#         logger.addHandler(handler)

#     return logger

import logging
from logging.handlers import RotatingFileHandler
import os

class ColorFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[94m",   # Blue
        "INFO": "\033[92m",    # Green
        "WARNING": "\033[93m", # Yellow
        "ERROR": "\033[91m",   # Red
        "CRITICAL": "\033[95m" # Magenta
    }
    RESET = "\033[0m"
    def format(self, record):
            color = self.COLORS.get(record.levelname, self.RESET)
            message = super().format(record)
            return f"{color}{message}{self.RESET}"
    

class RequestContextFilter(logging.Filter):
    def __init__(self, request_id=None, user=None):
        super().__init__()
        self.request_id = request_id
        self.user = user

    def filter(self, record):
        record.request_id = self.request_id or "N/A"
        record.user = self.user or "N/A"
        return True


def get_logger(name: str):
    # ensure logs directory exists
    os.makedirs("logs", exist_ok=True)
    
    context_filter = RequestContextFilter(request_id="12345", user="system")
    

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addFilter(context_filter)
    if not logger.handlers:
        # File handler
        file_handler = RotatingFileHandler(
            "logs/app.log",
            maxBytes=5_000_000,
            backupCount=3
        )
        file_handler.setLevel(logging.DEBUG)

        # Console handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # Log format
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | module=%(name)s | request=%(request_id)s | user=%(user)s | %(message)s"
        )
        color_formatter = ColorFormatter(
            "%(asctime)s | %(levelname)s | module=%(name)s | request=%(request_id)s | user=%(user)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(color_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        logger.propagate = False

    return logger
