"""Tests for hello world endpoint."""

from fastapi.testclient import TestClient


def test_hello_world_endpoint(client: TestClient) -> None:
    """Test hello world endpoint."""
    response = client.get("/api/v1/hello/world")
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Hello, World!"
    assert data["status"] == "success"


def test_hello_world_response_model(client: TestClient) -> None:
    """Test hello world response model structure."""
    response = client.get("/api/v1/hello/world")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "status" in data
    assert isinstance(data["message"], str)
    assert isinstance(data["status"], str)
