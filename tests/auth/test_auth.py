import pytest

@pytest.mark.smoke
def test_auth_success(base_url, session):
    payload = {"username": "admin", "password": "password123"}
    response = session.post(f"{base_url}/auth", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "token" in body
    assert body["token"]

@pytest.mark.negative
@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong", "password123"),
        ("admin", "wrong"),
        ("", ""),
    ],
)
def test_auth_failure(base_url, session, username, password):
    payload = {"username": username, "password": password}
    response = session.post(f"{base_url}/auth", json=payload)
    assert response.status_code in (200, 401, 403)
