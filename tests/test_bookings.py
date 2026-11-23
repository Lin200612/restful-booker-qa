import pytest
import requests


@pytest.mark.smoke
def test_healthcheck(base_url):
    resp = requests.get(f"{base_url}/ping", timeout=10)
    assert resp.status_code == 201


@pytest.mark.smoke
def test_get_booking_ids_returns_list(base_url):
    resp = requests.get(f"{base_url}/booking", timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert "bookingid" in data[0]


def test_create_booking(base_url, booking_payload, auth_token):
    resp = requests.post(f"{base_url}/booking", json=booking_payload, timeout=10)
    assert resp.status_code == 200
    body = resp.json()
    assert body["booking"]["firstname"] == booking_payload["firstname"]
    assert body["booking"]["totalprice"] == booking_payload["totalprice"]
    # уборка за собой
    requests.delete(
        f"{base_url}/booking/{body['bookingid']}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=10,
    )


def test_get_booking_by_id(base_url, created_booking, booking_payload):
    resp = requests.get(f"{base_url}/booking/{created_booking}", timeout=10)
    assert resp.status_code == 200
    assert resp.json()["lastname"] == booking_payload["lastname"]


def test_update_booking(base_url, created_booking, booking_payload, auth_token):
    booking_payload["firstname"] = "Petr"
    resp = requests.put(
        f"{base_url}/booking/{created_booking}",
        json=booking_payload,
        headers={"Cookie": f"token={auth_token}"},
        timeout=10,
    )
    assert resp.status_code == 200
    assert resp.json()["firstname"] == "Petr"


def test_delete_booking(base_url, booking_payload, auth_token):
    created = requests.post(f"{base_url}/booking", json=booking_payload, timeout=10)
    booking_id = created.json()["bookingid"]
    resp = requests.delete(
        f"{base_url}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=10,
    )
    assert resp.status_code == 201
    after = requests.get(f"{base_url}/booking/{booking_id}", timeout=10)
    assert after.status_code == 404


@pytest.mark.negative
def test_get_nonexistent_booking(base_url):
    resp = requests.get(f"{base_url}/booking/999999999", timeout=10)
    assert resp.status_code == 404


@pytest.mark.negative
def test_delete_without_token(base_url, created_booking):
    resp = requests.delete(f"{base_url}/booking/{created_booking}", timeout=10)
    assert resp.status_code == 403


@pytest.mark.negative
def test_auth_with_wrong_password(base_url):
    resp = requests.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "wrong"},
        timeout=10,
    )
    # API отвечает 200 с сообщением об ошибке: опиши это в баг-репорте или как особенность
    assert "token" not in resp.json()
