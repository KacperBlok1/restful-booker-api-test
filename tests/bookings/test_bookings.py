import pytest

@pytest.mark.smoke
def test_get_bookings_list(base_url, session):
    response = session.get(f"{base_url}/booking")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    if body:
        assert "bookingid" in body[0]
