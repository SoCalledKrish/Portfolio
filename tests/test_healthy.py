from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_version():
    response = client.get("/version")

    assert response.status_code == 200

    data = response.json()

    assert "version" in data


def test_ready():
    response = client.get("/ready")

    assert response.status_code == 200

    data = response.json()

    assert data["ready"] is True


def test_live():
    response = client.get("/live")

    assert response.status_code == 200

    data = response.json()

    assert data["live"] is True