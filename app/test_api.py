import httpx
import pytest
import random
import string

API_BASE_URL = "http://host.docker.internal/flask"

def test_get_messages_for_recipient():
    sender = "anySender"
    recipient = "anyRecipient"
    message_content = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    data = {"message": message_content}
    response = httpx.post(f"{API_BASE_URL}/addMessage/{sender}/{recipient}", json=data)
    assert response.status_code == 200

    params = {"index": -1, "number_of_messages": 1}
    response = httpx.get(f"{API_BASE_URL}/getMessagesSlice/{recipient}", params=params)
    assert response.status_code == 200
    assert response.json() == {'messages': [{'message_content': message_content, 'sender': sender}]}
