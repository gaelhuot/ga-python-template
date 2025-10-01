"""Common schemas for API responses."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response schema."""

    status: str = Field(..., description="Health status")
    timestamp: Optional[str] = Field(None, description="Check timestamp")


class ReadyResponse(BaseModel):
    """Readiness check response schema."""

    status: str = Field(..., description="Readiness status")
    checks: Dict[str, str] = Field(..., description="Individual service checks")
    timestamp: Optional[str] = Field(None, description="Check timestamp")


class ErrorResponse(BaseModel):
    """Error response schema."""

    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    detail: Optional[Any] = Field(None, description="Additional error details")
    request_id: Optional[str] = Field(None, description="Request correlation ID")


class RootResponse(BaseModel):
    """Root endpoint response schema."""

    message: str = Field(..., description="Welcome message")
    version: str = Field(..., description="API version")
    docs_url: str = Field(..., description="API documentation URL")
