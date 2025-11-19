from src.logger.logger import get_logger
from src.errors.exceptions import (
    AuthenticationError,   
    RateLimitError,
    TimeoutError,
    NetworkError,
    InvalidResponseError,
)

log = get_logger("error_handler")

def handle_exception(e, context=""):
    # log.error(f"Error occurred | {type(e).__name__} | {e} | context={context}", exc_info=True)
    # Additional error handling logic can be added here
    error_type = type(e).__name__

    if isinstance(e, AuthenticationError):
        category = "AUTH"
    elif isinstance(e, RateLimitError):
        category = "RATE_LIMIT"
    elif isinstance(e, TimeoutError):
        category = "TIMEOUT"
    elif isinstance(e, NetworkError):
        category = "NETWORK"
    elif isinstance(e, InvalidResponseError):
        category = "INVALID_RESPONSE"
    else:
        category = "UNKNOWN"

    log.error(
        f"[{category}] | {error_type} | {e} | context={context}",
        exc_info=True
    )


def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        handle_exception(e, context=f"Function={func.__name__}")
        return None  # or return fallback