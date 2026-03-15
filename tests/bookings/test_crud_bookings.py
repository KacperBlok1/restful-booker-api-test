import pytest


def create_booking(base_url, session, payload):
    response = session.post(f"{base_url}/booking", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    return body["bookingid"], body["booking"]


@pytest.mark.regression
def test_create_update_delete_booking(base_url, session, auth_token):
    headers = {"Cookie": f"token={auth_token}"}
    payload = {
        "firstname": "Kacper",
        "lastname": "Test",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": "Breakfast"
    }

    booking_id, created_booking = create_booking(base_url, session, payload)
    assert created_booking["firstname"] == payload["firstname"]
    assert created_booking["lastname"] == payload["lastname"]

    get_resp = session.get(f"{base_url}/booking/{booking_id}")
    assert get_resp.status_code == 200
    get_body = get_resp.json()
    assert get_body["totalprice"] == payload["totalprice"]

    updated_payload = {
        **payload,
        "totalprice": 200,
        "additionalneeds": "Breakfast and Dinner"
    }
    update_resp = session.put(
        f"{base_url}/booking/{booking_id}",
        json=updated_payload,
        headers=headers,
    )
    assert update_resp.status_code in (200, 204)
    if update_resp.status_code == 200:
        updated_body = update_resp.json()
        assert updated_body["totalprice"] == 200
        assert updated_body["additionalneeds"] == "Breakfast and Dinner"

    delete_resp = session.delete(
        f"{base_url}/booking/{booking_id}",
        headers=headers,
    )
    assert delete_resp.status_code in (201, 202, 204)

    get_after_delete = session.get(f"{base_url}/booking/{booking_id}")
    assert get_after_delete.status_code in (404, 405)
