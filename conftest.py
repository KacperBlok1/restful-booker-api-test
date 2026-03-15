import pytest
import requests
from utils.config import BASE_URL

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    return s

@pytest.fixture(scope="session")
def auth_token(base_url, session):
    payload = {"username": "admin", "password": "password123"}
    response = session.post(f"{base_url}/auth", json=payload)
    response.raise_for_status()
    return response.json().get("token")
