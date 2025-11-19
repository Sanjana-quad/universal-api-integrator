class APIError(Exception):
    """Base class for all API errors."""

class NetworkError(APIError):
    """Raised when a network issue occurs (DNS failure, connection refused)."""

class TimeoutError(APIError):
    """Raised when request exceeds timeout."""

class AuthenticationError(APIError):
    """Raised when API key/token/credentials are invalid."""

class RateLimitError(APIError):
    """Raised when API returns too many requests."""

class InvalidResponseError(APIError):
    """Raised when response is malformed or missing fields."""

class ParsingError(APIError):
    """Raised when data extraction or parsing fails."""
