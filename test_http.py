from src.http.http_client import HTTPClient
from src.config import Config

base_url = "https://api.github.com"
client = HTTPClient(base_url, retries=1, timeout=5)

response = client.get("/repos/octocat/Hello-World")

print(response["name"])
