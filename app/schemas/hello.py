"""Hello world schemas."""

from pydantic import BaseModel, Field


class HelloResponse(BaseModel):
    """Hello world response schema."""

    message: str = Field(..., description="Hello message")
    status: str = Field(default="success", description="Response status")
    timestamp: str = Field(..., description="Response timestamp")
