from src.errors.exceptions import *
from src.errors.handlers import safe_execute

def bad_fn():
    raise InvalidResponseError("API returned empty JSON")

result = safe_execute(bad_fn)

print("Result:", result)
