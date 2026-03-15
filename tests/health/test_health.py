import pytest

@pytest.mark.smoke
def test_healthcheck_status_code(base_url, session):
    response = session.get(f"{base_url}/ping")
    assert response.status_code in (200, 201)
