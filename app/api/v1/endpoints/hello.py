"""Hello world endpoint."""

from fastapi import APIRouter, HTTPException

from app.schemas.hello import HelloResponse
from app.services.hello import HelloService

router = APIRouter(tags=["hello"])


@router.get("/world", response_model=HelloResponse, summary="Hello world")
async def hello_world() -> HelloResponse:
    """
    Hello world endpoint.

    Returns a simple hello world message with timestamp.
    """
    try:
        return await HelloService.get_hello_world()
    except Exception as e:
        # This will be caught by the global exception handler
        raise HTTPException(status_code=500, detail=str(e))
