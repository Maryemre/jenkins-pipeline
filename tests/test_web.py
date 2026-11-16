import pytest
from app.web import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_moderate_normal(client):
    response = client.post(
        "/moderate",
        json={"message": "bonjour"}
    )

    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}

def test_moderate_spam(client):
    response = client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}
    )

    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}

def test_moderate_message_absent(client):
    response = client.post(
        "/moderate",
        json={}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


def test_moderate_message_non_string(client):
    response = client.post(
        "/moderate",
        json={"message": 42}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


def test_moderate_message_espaces(client):
    response = client.post(
        "/moderate",
        json={"message": "   "}
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}

def test_moderate_json_liste(client):
    response = client.post(
        "/moderate",
        json=["bonjour", "spam"]
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}


