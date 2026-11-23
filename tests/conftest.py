import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Ivan",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-12-01", "checkout": "2026-12-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture(scope="session")
def auth_token(base_url):
    resp = requests.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=10,
    )
    assert resp.status_code == 200
    return resp.json()["token"]


@pytest.fixture
def created_booking(base_url, booking_payload, auth_token):
    """Создаёт бронь для теста и удаляет её после."""
    resp = requests.post(f"{base_url}/booking", json=booking_payload, timeout=10)
    assert resp.status_code == 200
    booking_id = resp.json()["bookingid"]
    yield booking_id
    requests.delete(
        f"{base_url}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=10,
    )
