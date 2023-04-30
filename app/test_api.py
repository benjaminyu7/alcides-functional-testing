import httpx
import pytest

API_BASE_URL = "http://host.docker.internal/flask"

def test_get_messages_for_recipient():
    recipient = "anyRecipient"
    response = httpx.get(f"{API_BASE_URL}/getMessages/{recipient}")
    assert response.status_code == 200
    assert response.json() == {'status': 'OK'}
