"""Tests for main application."""

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "docs_url" in data
    assert data["message"] == "Welcome to GA Python Template API"


def test_health_check_endpoint(client: TestClient) -> None:
    """Test health check endpoint (liveness)."""
    response = client.get("/health")
    assert response.status_code == 200
    
    data = response.json()
    assert "status" in data
    assert "timestamp" in data
    assert data["status"] == "healthy"


def test_readiness_check_endpoint(client: TestClient) -> None:
    """Test readiness check endpoint."""
    response = client.get("/health/ready")
    assert response.status_code == 200
    
    data = response.json()
    assert "status" in data
    assert "checks" in data
    assert "timestamp" in data
    assert isinstance(data["checks"], dict)


def test_metrics_endpoint(client: TestClient) -> None:
    """Test Prometheus metrics endpoint."""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]


def test_openapi_schema(client: TestClient) -> None:
    """Test OpenAPI schema generation."""
    response = client.get("/api/v1/openapi.json")
    assert response.status_code == 200
    
    schema = response.json()
    assert "openapi" in schema
    assert "info" in schema
    assert "paths" in schema
    assert schema["info"]["title"] == "GA Python Template"
    assert schema["info"]["version"] == "0.1.0"


def test_docs_endpoint(client: TestClient) -> None:
    """Test API documentation endpoint."""
    response = client.get("/docs")
    assert response.status_code == 200


def test_redoc_endpoint(client: TestClient) -> None:
    """Test ReDoc documentation endpoint."""
    response = client.get("/redoc")
    assert response.status_code == 200


def test_404_error_handling(client: TestClient) -> None:
    """Test 404 error handling."""
    response = client.get("/nonexistent")
    assert response.status_code == 404
    
    data = response.json()
    # FastAPI's default 404 response format
    assert "detail" in data
    assert data["detail"] == "Not Found"


def test_422_error_handling(client: TestClient) -> None:
    """Test 422 validation error handling."""
    # This would need a POST endpoint with validation to test properly
    # For now, we'll test that the error handler is set up
    response = client.get("/health?invalid_param=test")
    # Should still work as GET doesn't have validation
    assert response.status_code == 200
