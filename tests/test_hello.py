"""Tests for hello world endpoint."""

from fastapi.testclient import TestClient


def test_hello_world_endpoint(client: TestClient) -> None:
    """Test hello world endpoint."""
    response = client.get("/api/v1/hello/world")
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Hello, World!"
    assert data["status"] == "success"
    assert "timestamp" in data


def test_hello_world_response_model(client: TestClient) -> None:
    """Test hello world response model structure."""
    response = client.get("/api/v1/hello/world")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "status" in data
    assert "timestamp" in data
    assert isinstance(data["message"], str)
    assert isinstance(data["status"], str)
    assert isinstance(data["timestamp"], str)


def test_hello_world_request_id_header(client: TestClient) -> None:
    """Test that request ID is included in response headers."""
    response = client.get("/api/v1/hello/world")
    assert response.status_code == 200
    assert "X-Request-ID" in response.headers
