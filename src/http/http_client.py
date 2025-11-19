import time
import requests

from src.logger.logger import get_logger
from src.config import Config
from src.errors.exceptions import (
    APIError,
    NetworkError,
    TimeoutError,
    AuthenticationError,
    RateLimitError,
    InvalidResponseError
)

log = get_logger("http_client")

class HTTPClient:
    def __init__(self, base_url: str, retries=3, timeout=5, headers=None):
        self.base_url = base_url
        self.retries = retries
        self.timeout = timeout
        self.default_headers = headers or {}

    def _prepare_headers(self, headers):
        final_headers = self.default_headers.copy()
        if headers:
            final_headers.update(headers)
        return final_headers

    def _handle_errors(self, response):
        if response.status_code == 401 or response.status_code == 403:
            raise AuthenticationError("Invalid API key or permissions")

        if response.status_code == 429:
            raise RateLimitError("Rate limit exceeded")

        if 500 <= response.status_code < 600:
            raise APIError(f"Server error: {response.status_code}")

        if not response.ok:
            raise APIError(f"API returned bad status: {response.status_code}")

    def _request(self, method, path, **kwargs):
        url = self.base_url + path
        headers = self._prepare_headers(kwargs.pop("headers", None))

        for attempt in range(1, self.retries + 1):
            try:
                log.info(f"[REQUEST] {method.upper()} {url} attempt={attempt}")

                response = requests.request(
                    method,
                    url,
                    headers=headers,
                    timeout=self.timeout,
                    **kwargs
                )

                self._handle_errors(response)

                # Parsing
                try:
                    data = response.json()
                    log.info(f"[RESPONSE] success url={url}")
                    return data
                except Exception as e:
                    raise InvalidResponseError("Failed to parse JSON") from e

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
                log.error(f"[TIMEOUT] url={url}")
                if attempt == self.retries:
                    raise TimeoutError("Request timed out")

            except requests.exceptions.ConnectionError:
                log.error(f"[NETWORK ERROR] url={url}")
                if attempt == self.retries:
                    raise NetworkError("Network connection failed")

            # Backoff
            backoff = attempt * 1.5
            log.warning(f"Retrying in {backoff} seconds...")
            time.sleep(backoff)

        raise APIError("Unknown error")

    # -------------- PUBLIC METHODS --------------

    def get(self, path, **kwargs):
        return self._request("get", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("post", path, **kwargs)

    def put(self, path, **kwargs):
        return self._request("put", path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("delete", path, **kwargs)
