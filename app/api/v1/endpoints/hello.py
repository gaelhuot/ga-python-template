"""Hello world endpoint."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HelloResponse(BaseModel):
    """Hello world response model."""

    message: str
    status: str = "success"


@router.get("/world", response_model=HelloResponse)
async def hello_world() -> HelloResponse:
    """
    Hello world endpoint.

    Returns a simple hello world message.
    """
    return HelloResponse(message="Hello, World!")
